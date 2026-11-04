#!/usr/bin/env python3
"""Dependency-free structural checker for BPMN 2.0 XML files. Python 3.9+.

Checks what a BPMN linter often skips: reference integrity, lane membership,
pool boundaries for sequence and message flows, and diagram-interchange (DI)
coverage so the file renders when imported into a modelling tool.

Usage: python3 check_bpmn.py FILE.bpmn [FILE.bpmn ...]
Exit code 0 when no errors (warnings allowed), 1 otherwise.
"""
import json
import sys
import xml.etree.ElementTree as ET

MODEL = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
DDI = 'http://www.omg.org/spec/DD/20100524/DI'

FLOW_NODES = {
    'task', 'userTask', 'serviceTask', 'manualTask', 'sendTask', 'receiveTask',
    'scriptTask', 'businessRuleTask', 'subProcess', 'callActivity', 'transaction',
    'adHocSubProcess', 'startEvent', 'endEvent', 'intermediateCatchEvent',
    'intermediateThrowEvent', 'boundaryEvent', 'exclusiveGateway',
    'parallelGateway', 'inclusiveGateway', 'eventBasedGateway', 'complexGateway',
}
ACTIVITIES = {n for n in FLOW_NODES if n.endswith('Task') or n in
              {'task', 'subProcess', 'callActivity', 'transaction', 'adHocSubProcess'}}
CONTAINERS = {'process', 'subProcess', 'transaction', 'adHocSubProcess'}
SPLITTING = {'exclusiveGateway', 'inclusiveGateway'}


def local(tag):
    return tag.split('}', 1)[1] if '}' in tag else tag


def check(path):
    errors, warnings = [], []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return {'file': path, 'status': 'fail', 'errors': ['not-well-formed: ' + str(exc)], 'warnings': []}
    if root.tag != '{%s}definitions' % MODEL:
        errors.append('root-not-bpmn-definitions')

    ids = {}
    for el in root.iter():
        i = el.get('id')
        if i:
            if i in ids:
                errors.append('duplicate-id: ' + i)
            ids[i] = el

    nodes, container_of, process_of = {}, {}, {}
    flows = []

    def walk(container, process_id):
        for child in container:
            name = local(child.tag)
            if child.tag.startswith('{%s}' % MODEL) and name in FLOW_NODES:
                nodes[child.get('id')] = child
                container_of[child.get('id')] = container.get('id')
                process_of[child.get('id')] = process_id
                if name in CONTAINERS:
                    walk(child, process_id)
            elif child.tag == '{%s}sequenceFlow' % MODEL:
                flows.append((child, container.get('id')))

    processes = root.findall('{%s}process' % MODEL)
    if not processes:
        errors.append('no-process')
    for proc in processes:
        walk(proc, proc.get('id'))

    # Sequence flows: resolve and stay inside one container (never cross pools).
    incoming, outgoing = {}, {}
    for flow, cont in flows:
        fid, src, tgt = flow.get('id'), flow.get('sourceRef'), flow.get('targetRef')
        for end, ref in (('source', src), ('target', tgt)):
            if ref not in nodes:
                errors.append('unresolved-%s: %s -> %s' % (end, fid, ref))
        if src in nodes and tgt in nodes:
            if container_of[src] != cont or container_of[tgt] != cont:
                errors.append('sequence-flow-crosses-container: ' + fid)
            outgoing.setdefault(src, []).append(flow)
            incoming.setdefault(tgt, []).append(flow)

    # Message flows: must join two different participants (pools).
    participants = {}
    for p in root.iter('{%s}participant' % MODEL):
        participants[p.get('id')] = p.get('processRef')
    for mf in root.iter('{%s}messageFlow' % MODEL):
        ends = []
        for ref in (mf.get('sourceRef'), mf.get('targetRef')):
            if ref in participants:
                ends.append(participants[ref] or ref)
            elif ref in nodes:
                ends.append(process_of[ref])
            else:
                errors.append('unresolved-message-flow-end: %s -> %s' % (mf.get('id'), ref))
        if len(ends) == 2 and ends[0] == ends[1]:
            errors.append('message-flow-inside-one-pool: ' + str(mf.get('id')))

    # Node-level rules.
    for nid, el in nodes.items():
        kind = local(el.tag)
        nin, nout = len(incoming.get(nid, [])), len(outgoing.get(nid, []))
        is_event_sub = el.get('triggeredByEvent') == 'true'
        if kind == 'startEvent':
            if nin:
                errors.append('start-event-has-incoming: ' + nid)
            if not nout and not is_event_sub:
                errors.append('start-event-has-no-outgoing: ' + nid)
        elif kind == 'endEvent':
            if nout:
                errors.append('end-event-has-outgoing: ' + nid)
            if not nin:
                errors.append('end-event-unreachable: ' + nid)
            if not (el.get('name') or '').strip():
                warnings.append('end-event-unnamed (name the end state): ' + nid)
        elif kind == 'boundaryEvent':
            if el.get('attachedToRef') not in nodes:
                errors.append('boundary-event-unattached: ' + nid)
            if not nout:
                errors.append('boundary-event-has-no-outgoing: ' + nid)
        else:
            if not nin and not is_event_sub:
                errors.append('no-incoming-flow: ' + nid)
            if not nout and not is_event_sub:
                errors.append('no-outgoing-flow: ' + nid)
        if kind in ACTIVITIES and not (el.get('name') or '').strip():
            errors.append('activity-unnamed: ' + nid)
        if kind in ACTIVITIES and nin > 1:
            warnings.append('implicit-join (merge with a gateway): ' + nid)
        if kind in SPLITTING and nout > 1:
            unlabelled = [f for f in outgoing[nid]
                          if not (f.get('name') or '').strip() and el.get('default') != f.get('id')]
            for f in unlabelled:
                warnings.append('unlabelled-gateway-branch: %s from %s' % (f.get('id'), nid))
            if unlabelled and not (el.get('name') or '').strip():
                warnings.append('splitting-gateway-unnamed (state the question): ' + nid)
        # Style rules (Method and Style, eCH-0158, 7PMG, Camunda practice).
        named = (el.get('name') or '').strip()
        if kind.endswith('Gateway') and named and (kind in ('parallelGateway', 'eventBasedGateway') or nin > 1 >= nout):
            warnings.append('label-on-join-parallel-or-event-gateway (leave unlabelled): ' + nid)
        if kind == 'inclusiveGateway':
            warnings.append('inclusive-gateway (7PMG G5: avoid OR unless evidence needs it): ' + nid)
        if kind in ACTIVITIES and nout > 1:
            warnings.append('implicit-split-from-activity (use a gateway): ' + nid)
        if kind in ('exclusiveGateway', 'inclusiveGateway') and nout > 1:
            preds = [f.get('sourceRef') for f in incoming.get(nid, [])]
            if any(local(nodes[p].tag) in ('exclusiveGateway', 'inclusiveGateway') and len(outgoing.get(p, [])) > 1
                   for p in preds if p in nodes):
                chain = [p for p in preds if p in nodes and any(
                    local(nodes[q].tag) in ('exclusiveGateway', 'inclusiveGateway') and len(outgoing.get(q, [])) > 1
                    for q in [g.get('sourceRef') for g in incoming.get(p, [])] if q in nodes)]
                if chain:
                    warnings.append('gateway-cascade (3+ decisions in a row: use a decision table): ' + nid)

    # Process-level style rules: names, size limits.
    for proc_id in {p.get('id') for p in processes}:
        members = [n for n, p in process_of.items() if p == proc_id]
        acts = [n for n in members if local(nodes[n].tag) in ACTIVITIES]
        for label, kinds in (('activity', ACTIVITIES), ('end-event', {'endEvent'})):
            names = {}
            for n in members:
                if local(nodes[n].tag) in kinds and (nodes[n].get('name') or '').strip():
                    names.setdefault(nodes[n].get('name').strip().lower(), []).append(n)
            for nm, ids in names.items():
                if len(ids) > 1:
                    warnings.append('duplicate-%s-name "%s": %s' % (label, nm, ', '.join(sorted(ids))))
        if len(acts) > 15:
            warnings.append('activities-%d-in-%s > 15 (eCH-0158: split into sub-processes)' % (len(acts), proc_id))
        if len(members) > 50:
            warnings.append('flow-nodes-%d-in-%s > 50 (7PMG G7: decompose)' % (len(members), proc_id))

    # Lanes: every top-level node of a laned process sits in exactly one lane.
    for proc in processes:
        lane_sets = proc.findall('{%s}laneSet' % MODEL)
        if not lane_sets:
            continue
        seen = {}
        for lane in proc.iter('{%s}lane' % MODEL):
            if lane.find('{%s}childLaneSet' % MODEL) is not None:
                continue
            for ref in lane.findall('{%s}flowNodeRef' % MODEL):
                seen.setdefault(ref.text, []).append(lane.get('id'))
        for nid in [n for n, c in container_of.items() if c == proc.get('id')]:
            count = len(seen.get(nid, []))
            if count != 1:
                errors.append('lane-membership-%d: %s' % (count, nid))
        for ref in seen:
            if ref not in nodes:
                errors.append('lane-references-missing-node: ' + str(ref))

    # Diagram interchange coverage.
    shapes = {s.get('bpmnElement') for s in root.iter('{%s}BPMNShape' % DI)}
    edges = {}
    for e in root.iter('{%s}BPMNEdge' % DI):
        edges[e.get('bpmnElement')] = len(e.findall('{%s}waypoint' % DDI))
    if not shapes and not edges:
        errors.append('no-diagram-interchange (most tools will not render it)')
    else:
        wanted = list(nodes) + list(participants)
        wanted += [l.get('id') for l in root.iter('{%s}lane' % MODEL)]
        for i in wanted:
            if i not in shapes:
                errors.append('missing-shape: ' + i)
        for f, _ in flows:
            if edges.get(f.get('id'), 0) < 2:
                errors.append('missing-edge-or-waypoints: ' + str(f.get('id')))
        for mf in root.iter('{%s}messageFlow' % MODEL):
            if edges.get(mf.get('id'), 0) < 2:
                errors.append('missing-edge-or-waypoints: ' + str(mf.get('id')))
        # One size per element type (eCH-0158 2.3.2; size implies importance).
        sizes = {}
        for s in root.iter('{%s}BPMNShape' % DI):
            el = nodes.get(s.get('bpmnElement'))
            b = s.find('{http://www.omg.org/spec/DD/20100524/DC}Bounds')
            if el is None or b is None:
                continue
            kind = local(el.tag)
            group = 'activity' if kind in ACTIVITIES and s.get('isExpanded') != 'true' else (
                'event' if kind.endswith('Event') else 'gateway' if kind.endswith('Gateway') else None)
            if group:
                sizes.setdefault(group, set()).add((b.get('width'), b.get('height')))
        for group, variants in sizes.items():
            if len(variants) > 1:
                warnings.append('mixed-%s-sizes %s (one size per element type)' % (group, sorted(variants)))

    counts = {
        'participants': len(participants), 'processes': len(processes),
        'flow_nodes': len(nodes), 'sequence_flows': len(flows),
        'message_flows': len(list(root.iter('{%s}messageFlow' % MODEL))),
        'lanes': len(list(root.iter('{%s}lane' % MODEL))),
    }
    return {'file': path, 'status': 'fail' if errors else 'pass',
            'errors': sorted(set(errors)), 'warnings': sorted(set(warnings)), 'counts': counts}


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    results = [check(p) for p in argv[1:]]
    print(json.dumps(results, indent=2))
    return 1 if any(r['status'] == 'fail' for r in results) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
