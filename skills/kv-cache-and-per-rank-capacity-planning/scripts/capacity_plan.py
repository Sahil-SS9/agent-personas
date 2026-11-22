#!/usr/bin/env python3
"""Stdlib MHA/GQA capacity estimate. Not a model loader or fit guarantee."""
import argparse
import json
import math


def number(value, field, integer=False, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(field + ': numeric value required')
    if not math.isfinite(value) or value < 0 or (not allow_zero and value == 0):
        raise ValueError(field + ': finite positive value required')
    if integer and (not isinstance(value, int)):
        raise ValueError(field + ': integer required')
    return value


def plan(data):
    if not isinstance(data, dict) or data.get('architecture') not in ('mha', 'gqa'):
        raise ValueError('Only explicit mha/gqa cache layouts are supported')
    ranks = data.get('ranks')
    if not isinstance(ranks, list) or not ranks:
        raise ValueError('Nonempty per-rank budget list required')
    minimum = number(data['required_context'], 'required_context', True)
    proposed = number(data['proposed_context'], 'proposed_context', True)
    sequences = number(data['sequences'], 'sequences', True)
    layers = number(data['layers'], 'layers', True)
    head_dim = number(data['head_dim'], 'head_dim', True)
    dtype_bytes = number(data['kv_element_bytes'], 'kv_element_bytes')
    if dtype_bytes not in (1, 2, 4):
        raise ValueError('Unsupported KV element width; explicit layout required')
    overhead = number(data['kv_layout_multiplier'], 'kv_layout_multiplier')
    if overhead < 1:
        raise ValueError('Layout multiplier must be at least 1; sharing needs a separate model')
    result = []
    for i, r in enumerate(ranks):
        heads = number(r['resident_kv_heads'], 'resident_kv_heads', True)
        available = number(r['available_bytes'], 'available_bytes', True)
        allocations = {k: number(r[k], k, True, True) for k in (
            'weight_bytes', 'workspace_bytes', 'draft_bytes', 'graph_bytes', 'reserve_bytes')}
        kv = math.ceil(2 * layers * heads * head_dim * proposed * sequences * dtype_bytes * overhead)
        required = kv + sum(allocations.values())
        result.append({'rank': i, 'kv_bytes': kv, 'required_bytes': required,
                       'headroom_bytes': available - required,
                       'within_estimated_capacity': available >= required})
    return {'status': 'estimate-only', 'meets_required_context': proposed >= minimum,
            'estimated_admissible': proposed >= minimum and all(r['within_estimated_capacity'] for r in result),
            'ranks': result, 'limits': 'No live hardware, allocator, prefix-sharing or model-layout validation. Confirm actual peak load before deployment.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fixture', help='JSON input using per-rank bytes, not total advertised VRAM')
    args = parser.parse_args()
    try:
        with open(args.fixture, encoding='utf-8') as f:
            result = plan(json.load(f))
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
        print(json.dumps({'status': 'invalid-input', 'error': str(exc)}))
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result['estimated_admissible'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
