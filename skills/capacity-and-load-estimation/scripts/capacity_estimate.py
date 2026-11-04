#!/usr/bin/env python3
"""Back-of-the-envelope capacity estimator for system designs. Python 3.9+, stdlib only.

Input: a JSON file of stated assumptions (see templates/estimate-input.example.json).
Output: JSON with every derived figure, the formula used, its unit, and warnings.
Every number in the output comes from the stated assumptions; nothing is invented.

Usage: python3 capacity_estimate.py assumptions.json [--markdown]
Exit 0 on success (warnings allowed), 1 on invalid or missing assumptions.
"""
import argparse
import json
import math
import sys

SECONDS_PER_DAY = 86_400
UNITS = [(1e15, 'PB'), (1e12, 'TB'), (1e9, 'GB'), (1e6, 'MB'), (1e3, 'KB')]


def human_bytes(n):
    for size, unit in UNITS:
        if n >= size:
            return f'{n / size:.3g} {unit}'
    return f'{n:.3g} B'


def human_rate(n, unit):
    for size, prefix in ((1e12, 'T'), (1e9, 'G'), (1e6, 'M'), (1e3, 'K')):
        if n >= size:
            return f'{n / size:.3g}{prefix} {unit}'
    return f'{n:.3g} {unit}'


class Estimator:
    def __init__(self, a):
        self.a, self.rows, self.warnings, self.errors = a, [], [], []

    def need(self, path, positive=True, required=True):
        cur = self.a
        for key in path.split('.'):
            if not isinstance(cur, dict) or key not in cur:
                if required:
                    self.errors.append('missing-assumption: ' + path)
                return None
            cur = cur[key]
        if not isinstance(cur, (int, float)) or isinstance(cur, bool) or (positive and cur <= 0) or (not positive and cur < 0):
            self.errors.append(f'invalid-assumption: {path}={cur!r}')
            return None
        return float(cur)

    def row(self, key, value, unit, formula, pretty=None):
        self.rows.append({'figure': key, 'value': value, 'unit': unit, 'formula': formula,
                          'readable': pretty or (human_bytes(value) if unit == 'bytes' else
                                                 human_rate(value, unit))})
        return value

    def run(self):
        a = self.a
        t = a.get('traffic')
        if t:
            dau = self.need('traffic.dau')
            peak = self.need('traffic.peak_factor')
            acts = t.get('actions_per_user_per_day') or {}
            if not acts:
                self.errors.append('missing-assumption: traffic.actions_per_user_per_day')
            if peak is not None and peak < 1.5:
                self.warnings.append('peak_factor below 1.5: justify it with measured traffic shape')
            qps = {}
            for kind in sorted(acts):
                n = self.need(f'traffic.actions_per_user_per_day.{kind}')
                if None in (dau, n, peak):
                    continue
                avg = self.row(f'{kind}_qps_avg', dau * n / SECONDS_PER_DAY, 'req/s', f'dau x {kind}_per_user_per_day / 86400')
                self.row(f'{kind}_qps_peak', avg * peak, 'req/s', f'{kind}_qps_avg x peak_factor')
                qps[kind] = avg
            if 'read' in qps and 'write' in qps and qps['write'] > 0:
                self.row('read_write_ratio', qps['read'] / qps['write'], 'ratio', 'read_qps_avg / write_qps_avg', f"{qps['read'] / qps['write']:.3g}:1")
            s = a.get('storage')
            if s and 'write' in qps:
                per_day = 0.0
                for i, obj in enumerate(s.get('objects') or []):
                    size = obj.get('bytes_per_write')
                    frac = obj.get('fraction_of_writes', 1)
                    if not isinstance(size, (int, float)) or size <= 0 or not isinstance(frac, (int, float)) or not 0 < frac <= 1:
                        self.errors.append(f'invalid-assumption: storage.objects[{i}]')
                        continue
                    day = self.row(f"storage_per_day_{obj.get('name', i)}", qps['write'] * SECONDS_PER_DAY * frac * size, 'bytes',
                                   f'write_qps_avg x 86400 x {frac} x {size} B')
                    per_day += day
                if not s.get('objects'):
                    self.errors.append('missing-assumption: storage.objects')
                ret = self.need('storage.retention_days')
                rf = self.need('storage.replication_factor')
                if rf is not None and rf < 2:
                    self.warnings.append('replication_factor below 2: a single copy is lost with one disk or node')
                if per_day and ret is not None:
                    raw = self.row('storage_raw_over_retention', per_day * ret, 'bytes', 'sum(storage_per_day) x retention_days')
                    if rf is not None:
                        self.row('storage_replicated', raw * rf, 'bytes', 'storage_raw_over_retention x replication_factor')
            bw = a.get('bandwidth')
            if bw:
                for kind, key in (('read', 'read_response_bytes'), ('write', 'write_request_bytes')):
                    size = self.need(f'bandwidth.{key}', required=False)
                    if size is not None and kind in qps and peak is not None:
                        self.row(f'{kind}_bandwidth_peak', qps[kind] * peak * size * 8, 'bit/s',
                                 f'{kind}_qps_peak x {key} x 8', human_rate(qps[kind] * peak * size * 8, 'bit/s'))
            node = a.get('node')
            if node and qps and peak is not None:
                per = self.need('node.qps_per_node')
                util = node.get('target_utilisation', 0.6)
                if not isinstance(util, (int, float)) or not 0 < util <= 1:
                    self.errors.append('invalid-assumption: node.target_utilisation')
                elif per is not None:
                    total_peak = sum(v * peak for v in qps.values())
                    n = math.ceil(total_peak / (per * util))
                    self.row('nodes_for_peak', n, 'nodes', f'ceil(total_qps_peak / (qps_per_node x {util}))', str(n))
                    fd = node.get('failure_domains')
                    if isinstance(fd, int) and fd >= 2:
                        self.row('nodes_n_plus_one_domain', math.ceil(n * fd / (fd - 1)), 'nodes',
                                 f'ceil(nodes_for_peak x {fd} / ({fd} - 1)): survive loss of one failure domain',
                                 str(math.ceil(n * fd / (fd - 1))))
                    else:
                        self.warnings.append('node.failure_domains not set: capacity does not survive losing a zone')
        llm = a.get('llm')
        if llm:
            avg = self.need('llm.requests_per_s_avg')
            peak = self.need('llm.peak_factor')
            tin = self.need('llm.input_tokens')
            tout = self.need('llm.output_tokens')
            if None not in (avg, peak, tin, tout):
                self.row('llm_input_tokens_per_s_peak', avg * peak * tin, 'tok/s', 'requests_per_s_avg x peak_factor x input_tokens')
                outp = self.row('llm_output_tokens_per_s_peak', avg * peak * tout, 'tok/s', 'requests_per_s_avg x peak_factor x output_tokens')
                self.row('llm_tokens_per_day', avg * SECONDS_PER_DAY * (tin + tout), 'tok/day', 'requests_per_s_avg x 86400 x (input + output tokens)')
                gpu = llm.get('output_tokens_per_s_per_replica')
                if isinstance(gpu, (int, float)) and gpu > 0:
                    util = llm.get('target_utilisation', 0.6)
                    self.row('llm_replicas_for_peak', math.ceil(outp / (gpu * util)), 'replicas',
                             f'ceil(output_tok_s_peak / (output_tokens_per_s_per_replica x {util}))', str(math.ceil(outp / (gpu * util))))
                pin, pout = llm.get('usd_per_million_input'), llm.get('usd_per_million_output')
                if isinstance(pin, (int, float)) and isinstance(pout, (int, float)):
                    day = avg * SECONDS_PER_DAY * (tin * pin + tout * pout) / 1e6
                    self.row('llm_cost_per_day_usd', day, 'USD/day', 'requests_per_s_avg x 86400 x (in x price_in + out x price_out) / 1e6', f'${day:,.0f}/day')
                    self.row('llm_cost_per_request_usd', (tin * pin + tout * pout) / 1e6, 'USD', '(in x price_in + out x price_out) / 1e6',
                             f'${(tin * pin + tout * pout) / 1e6:.4f}')
                if tin > 32_000:
                    self.warnings.append('input_tokens above 32K per request: check context assembly; long contexts cost latency and lose mid-context facts')
        if not t and not llm:
            self.errors.append('missing-assumption: traffic or llm block')
        return {'name': a.get('name'), 'status': 'fail' if self.errors else 'ok', 'errors': self.errors,
                'warnings': self.warnings, 'figures': self.rows, 'assumptions': a}


def to_markdown(r):
    out = [f"# Estimate: {r.get('name') or 'unnamed'}", '', '| Figure | Value | Formula |', '|---|---|---|']
    out += [f"| {x['figure']} | {x['readable']} | {x['formula']} |" for x in r['figures']]
    if r['warnings']:
        out += ['', 'Warnings:'] + [f'- {w}' for w in r['warnings']]
    if r['errors']:
        out += ['', 'Errors:'] + [f'- {e}' for e in r['errors']]
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('assumptions')
    ap.add_argument('--markdown', action='store_true')
    args = ap.parse_args(argv)
    try:
        with open(args.assumptions) as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError('top level must be an object')
    except (OSError, ValueError) as exc:
        print(json.dumps({'status': 'fail', 'errors': ['unreadable: ' + str(exc)]}))
        return 1
    result = Estimator(data).run()
    print(to_markdown(result) if args.markdown else json.dumps(result, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
