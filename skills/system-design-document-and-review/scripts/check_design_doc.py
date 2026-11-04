#!/usr/bin/env python3
"""Check a system design document (Markdown) for the completeness rules of the
system-designer persona. Python 3.9+, stdlib only. Structural checks only: it
cannot judge whether the design is good, only whether the required reasoning is
present and internally consistent.

Usage: python3 check_design_doc.py design.md
Exit 0 when no errors (warnings allowed), 1 on errors.
"""
import json
import re
import sys
from pathlib import Path

SECTIONS = {
    'context': r'context|goals|problem',
    'requirements': r'requirement',
    'estimates': r'estimat|capacity|assumption',
    'high_level': r'high.level|architecture overview|components',
    'data': r'\bdata\b|storage|persistence',
    'failure': r'failure|resilien|reliab',
    'overload': r'overload|traffic|load management|retr',
    'security': r'security|trust|privacy',
    'operations': r'operat|rollout|observab|deploy',
    'cost': r'\bcost',
    'alternatives': r'alternativ|options considered|trade.?offs',
    'open_questions': r'open question|risks',
}
AI_TRIGGER = re.compile(r'\b(LLM|large language model|RAG|retrieval.augmented|embedding|agent(ic)?|prompt|foundation model|inference|GPT|Claude|Gemini|Llama)\b', re.I)
UNIT = re.compile(r'\d[\d,.]*\s*(?:[KMGT]?\s?(?:req/s|rps|qps|QPS|ops/s|tok/s|tokens?/s|B\b|KB|MB|GB|TB|PB|bit/s|bps|Mbps|Gbps)|ms\b|s\b|seconds|minutes|hours|days|USD|\$|%|x\b|nodes|replicas|GPUs?)', re.I)
SLO_ROW = re.compile(r'(p(50|9\d(\.\d+)?)\b.*\d\s*(ms|s)\b)|(\d{2}(\.\d+)?\s*%)', re.I)


def split_sections(text):
    out, current = {}, None
    for line in text.splitlines():
        m = re.match(r'^(#{1,3})\s+(.*)', line)
        if m and len(m.group(1)) == 2:
            current = m.group(2).strip()
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return {k: '\n'.join(v) for k, v in out.items()}


def find(sections, pattern):
    for title, body in sections.items():
        if re.search(pattern, title, re.I):
            return title, body
    return None, ''


def table_rows(body):
    rows = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith('|') and not re.fullmatch(r'\|[\s:|-]+\|?', s):
            rows.append([c.strip() for c in s.strip('|').split('|')])
    return rows[1:] if rows else []


def check(text):
    errors, warnings = [], []
    secs = split_sections(text)
    if not secs:
        return {'status': 'fail', 'errors': ['no-level-2-sections'], 'warnings': []}
    found = {}
    for key, pat in SECTIONS.items():
        title, body = find(secs, pat)
        if title is None:
            errors.append('missing-section: ' + key)
        elif not body.strip():
            errors.append('empty-section: ' + key)
        found[key] = body

    req = found.get('requirements', '')
    if req and not any(SLO_ROW.search(' '.join(r)) for r in table_rows(req)) and not SLO_ROW.search(req):
        errors.append('no-measurable-slo: state at least one target as a percentile latency with a unit or an availability percentage')
    if re.search(r'\b100(\.0+)?\s*%\s*(availab|uptime)', text, re.I):
        warnings.append('100%-availability-target: no real system meets it; state a budgeted SLO')
    if re.search(r'\baverage\s+latency\b', text, re.I) and not re.search(r'\bp(9\d|50)\b', text, re.I):
        warnings.append('average-latency-only: use percentiles for latency targets')

    est = found.get('estimates', '')
    if est:
        if len(UNIT.findall(est)) < 3:
            errors.append('estimates-without-units: give at least three derived figures with units')
        if not re.search(r'assum', est, re.I):
            errors.append('estimates-without-stated-assumptions')

    components = []
    _, hl = find(secs, SECTIONS['high_level'])
    for row in table_rows(hl):
        if row and row[0] and not re.match(r'^(component|name)$', row[0], re.I):
            components.append(re.sub(r'[`*]', '', row[0]).strip())
    if not components:
        errors.append('no-component-table: list components in a table (component | responsibility | ...)')
    frows = table_rows(found.get('failure', ''))
    if not frows:
        errors.append('no-failure-mode-table')
    else:
        covered = ' '.join(r[0].lower() for r in frows if r)
        for c in components:
            if c.lower() not in covered:
                errors.append('component-without-failure-mode: ' + c)
        for r in frows:
            if len(r) < 4 or any(not x or x in ('-', 'TBD', '?') for x in r[1:4]) or not r[-1] or r[-1] in ('-', 'TBD', '?'):
                errors.append('incomplete-failure-row: ' + (r[0] if r else '?'))

    if re.search(r'\bretr(y|ies)\b', text, re.I):
        ov = found.get('overload', '')
        scope = ov if re.search(r'\bretr', ov, re.I) else '\n'.join(l for l in text.splitlines() if re.search(r'retr', l, re.I))
        for need, msg in ((r'backoff', 'retries-without-backoff'), (r'jitter', 'retries-without-jitter'),
                          (r'idempot', 'retries-without-idempotency'),
                          (r'retry budget|budget of|single layer|one layer|only (in|at) the (edge|client|dispatcher|caller)', 'retries-without-budget-or-single-layer')):
            if not re.search(need, scope if msg != 'retries-without-idempotency' else text, re.I):
                errors.append(msg)
    if re.search(r'timeout', text, re.I) is None and re.search(r'\b(call|rpc|http|dependency|downstream)\b', text, re.I):
        errors.append('no-timeouts-stated')
    if re.search(r'two.phase commit|\b2pc\b', text, re.I) and not re.search(r'avoid|instead|rejected', text, re.I):
        warnings.append('two-phase-commit-across-services: justify or use saga/outbox')
    if re.search(r'exactly.once', text, re.I) and not re.search(r'idempot|dedup', text, re.I):
        errors.append('exactly-once-claim-without-idempotency-or-dedup')
    if re.search(r'\bfallback\b', text, re.I) and not re.search(r'exercis|tested|regularly|continuous|shadow', text, re.I):
        warnings.append('fallback-not-exercised: untested fallback paths widen outages; exercise it or fail fast')

    alt = found.get('alternatives', '')
    if alt and not (table_rows(alt) or re.search(r'^\s*[-*]\s+\S', alt, re.M)):
        errors.append('alternatives-not-listed')
    oq = found.get('open_questions', '')
    if oq and not (table_rows(oq) or re.search(r'^\s*[-*\d.]+\s+\S', oq, re.M)):
        errors.append('open-questions-empty')

    ai = bool(AI_TRIGGER.search(text))
    if ai:
        title, body = find(secs, r'\bAI\b|LLM|model|agent|retrieval')
        if title is None:
            errors.append('ai-components-without-ai-section')
        else:
            for need, msg in ((r'eval', 'ai-no-evaluation-plan'),
                              (r'token|step|budget|cost limit|spend', 'ai-no-consumption-budget'),
                              (r'prompt injection|untrusted|indirect injection', 'ai-no-prompt-injection-control'),
                              (r'gateway|fallback|provider|rate limit', 'ai-no-model-access-or-outage-plan')):
                if not re.search(need, body, re.I):
                    errors.append(msg)
            acts = re.search(r'\b(tools?|write actions?|function.calling|can (send|update|create|delete|refund|email|change))\b', body, re.I)
            denies = re.search(r'\bno (agent and no )?(tools|write actions)\b|\bcannot (send|change|write|act)\b|\bread.only\b', body, re.I)
            if acts and not denies and not re.search(r'approv|human.in.the.loop|confirm', body, re.I):
                errors.append('ai-write-actions-without-approval-gate')
    return {'status': 'fail' if errors else 'pass', 'errors': sorted(set(errors)), 'warnings': sorted(set(warnings)),
            'components': components, 'ai_section_required': ai}


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        text = Path(argv[0]).read_text()
    except (OSError, UnicodeDecodeError) as exc:
        print(json.dumps({'status': 'fail', 'errors': ['unreadable: ' + str(exc)]}))
        return 1
    result = check(text)
    result['file'] = argv[0]
    print(json.dumps(result, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
