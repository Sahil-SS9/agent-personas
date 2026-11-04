"""Generate the Lucid Standard Import house-style template (L1, L2, L3 pages)."""
import json, sys, zipfile
from pathlib import Path

S = json.loads((Path(__file__).parent / 'house-style.json').read_text())
C = S['colours']; F = S['fonts']['pt']; SZ = S['sizes_px']
TXT = C['text']

def t(s, pt, bold=False):
    w = 'font-weight: bold; ' if bold else ''
    return f'<span style="font-size: {pt}pt; {w}color: {TXT}">{s}</span>'

def box(x, y, w, h):
    return {'x': x, 'y': y, 'w': w, 'h': h}

def style(fill=None, stroke=None, width=1):
    return {'fill': {'type': 'color', 'color': fill or C['fill']},
            'stroke': {'color': stroke or C['line'], 'width': width, 'style': 'solid'}, 'textColor': TXT}

def text_block(i, x, y, w, h, s):
    return {'id': i, 'type': 'text', 'boundingBox': box(x, y, w, h), 'text': s}

def line(i, a, b, label=None):
    ln = {'id': i, 'lineType': 'elbow',
          'endpoint1': {'type': 'shapeEndpoint', 'style': 'none', 'shapeId': a},
          'endpoint2': {'type': 'shapeEndpoint', 'style': 'arrow', 'shapeId': b},
          'stroke': {'color': C['line'], 'width': 1, 'style': 'solid'}}
    if label:
        ln['text'] = [{'text': t(label, F['flow_label']), 'position': 0.3, 'side': 'top'}]
    return ln

def legend(i, x, y, extra):
    rows = ['Legend', 'Rounded box = activity; diamond = decision (question, labelled answers)',
            'Thin circle = start (trigger); thick circle = end (result)',
            '[ISSUE] vermillion thick border = evidenced issue (see register)',
            '[CONTROL] blue thick border = internal control',
            '[CHANGE] green thick border = new or changed in to-be'] + extra
    return {'id': i, 'type': 'rectangle', 'boundingBox': box(x, y, 420, 20 * len(rows) + 20),
            'style': style(C['header_fill']),
            'text': '<span style="font-size: 10pt; color: #1A1A1A; text-align: left">' + '<br>'.join(rows) + '</span>'}

def activity(i, x, y, label, fill=None, stroke=None, width=1, marker='none'):
    w, h = SZ['activity']
    return {'id': i, 'type': 'bpmnActivity', 'boundingBox': box(x, y, w, h), 'style': style(fill, stroke, width),
            'text': t(label, F['activity']), 'activityType': 'task', 'taskType': 'none',
            'activityMarker1': marker, 'activityMarker2': 'none'}

def event(i, x, y, group, label, etype='none'):
    w, h = SZ['event']
    return {'id': i, 'type': 'bpmnEvent', 'boundingBox': box(x, y, w, h), 'style': style(),
            'text': t(label, F['event_or_gateway_label']), 'eventGroup': group, 'eventType': etype}

def gateway(i, x, y, label):
    w, h = SZ['gateway']
    return {'id': i, 'type': 'bpmnGateway', 'boundingBox': box(x, y, w, h), 'style': style(),
            'text': t(label, F['event_or_gateway_label']), 'gatewayType': 'exclusive'}

L1 = {'id': 'p-l1', 'title': 'L1 Landscape', 'shapes': [
    text_block('l1-title', 40, 20, 900, 40, t('L1 0 Process landscape | As-is | v0.1 | Draft | Owner: COO', F['page_title'], True)),
    {'id': 'l1-mgmt', 'type': 'rectangle', 'boundingBox': box(40, 80, 900, 90), 'style': style(C['header_fill']), 'text': t('Management processes', F['lane_title'])},
    {'id': 'l1-core', 'type': 'rectangle', 'boundingBox': box(40, 190, 900, 120), 'style': style(C['header_fill']), 'text': t('Core processes', F['lane_title'])},
    {'id': 'l1-supp', 'type': 'rectangle', 'boundingBox': box(40, 330, 900, 90), 'style': style(C['header_fill']), 'text': t('Support processes', F['lane_title'])},
    {'id': 'l1-p2', 'type': 'process', 'boundingBox': box(300, 230, *SZ['activity']), 'style': style(),
     'text': t('2 Procure to pay', F['activity']), 'actions': [{'type': 'gotoPage', 'pageId': 'p-l2'}]},
    legend('l1-legend', 40, 440, ['Click a process to open its L2 page']),
]}

L2 = {'id': 'p-l2', 'title': 'L2 2 Procure to pay', 'shapes': [
    text_block('l2-title', 40, 20, 900, 40, t('L2 2 Procure to pay | As-is | v0.1 | Draft | Owner: Finance director', F['page_title'], True)),
    {'id': 'l2-crumb', 'type': 'text', 'boundingBox': box(40, 60, 400, 24), 'text': t('Parent: L1 0 Process landscape', 10),
     'actions': [{'type': 'gotoPage', 'pageId': 'p-l1'}]},
    event('l2-start', 60, 172, 'start', 'Purchase need raised'),
    activity('l2-s1', 140, 150, '2.1 Request purchase', marker='subProcess'),
    activity('l2-s2', 290, 150, '2.2 Order goods', marker='subProcess'),
    {**activity('l2-s3', 440, 150, '2.3 Approve supplier invoices', marker='subProcess'), 'actions': [{'type': 'gotoPage', 'pageId': 'p-l3'}]},
    activity('l2-s4', 590, 150, '2.4 Pay supplier', marker='subProcess'),
    {**event('l2-end', 740, 172, 'end', 'Supplier paid')},
    legend('l2-legend', 40, 300, ['Collapsed sub-process (+) = has its own L3 page; click to open']),
], 'lines': [line('l2-f1', 'l2-start', 'l2-s1'), line('l2-f2', 'l2-s1', 'l2-s2'), line('l2-f3', 'l2-s2', 'l2-s3'),
             line('l2-f4', 'l2-s3', 'l2-s4'), line('l2-f5', 'l2-s4', 'l2-end')]}

lanes = [{'title': 'AP clerk', 'width': 150, 'laneFill': C['fill']},
         {'title': 'Budget holder', 'width': 150, 'laneFill': C['fill']},
         {'title': 'Finance system', 'width': 150, 'laneFill': C['fill']}]
sem = C['semantic']
L3 = {'id': 'p-l3', 'title': 'L3 2.3 Approve supplier invoices', 'shapes': [
    text_block('l3-title', 40, 20, 1100, 40, t('L3 2.3 Approve supplier invoices | As-is | v0.1 | Draft | Owner: AP lead', F['page_title'], True)),
    {'id': 'l3-crumb', 'type': 'text', 'boundingBox': box(40, 60, 400, 24), 'text': t('Parent: L2 2 Procure to pay', 10),
     'actions': [{'type': 'gotoPage', 'pageId': 'p-l2'}]},
    {'id': 'l3-pool', 'type': 'bpmnPool', 'boundingBox': box(40, 100, 1100, 450), 'style': style(C['header_fill']),
     'title': 'Accounts payable', 'lanes': lanes, 'vertical': False, 'verticalLaneText': True, 'magnetize': True},
    event('l3-start', 100, 157, 'start', 'Invoice received', 'message'),
    activity('l3-a1', 170, 135, 'Register invoice'),
    activity('l3-a2', 330, 435, 'Match invoice to PO', sem['control']['fill'], sem['control']['border'], sem['control']['border_px']),
    gateway('l3-g1', 490, 450, 'Invoice matches PO?'),
    activity('l3-a3', 580, 285, 'Review mismatch', sem['issue']['fill'], sem['issue']['border'], sem['issue']['border_px']),
    gateway('l3-g2', 740, 300, 'Mismatch approved?'),
    gateway('l3-g3', 830, 450, ''),
    activity('l3-a4', 910, 435, 'Schedule payment'),
    event('l3-end1', 1070, 457, 'end', 'Invoice scheduled for payment'),
    activity('l3-a5', 830, 135, 'Send rejection to supplier'),
    event('l3-end2', 1000, 157, 'end', 'Invoice rejected'),
    {'id': 'l3-ann1', 'type': 'bpmnTextAnnotation', 'boundingBox': box(580, 200, 160, 50), 'style': style(),
     'text': t('[ISSUE] I-01 Approval takes 5-7 days vs 2-day policy (F06, C1)', 10)},
    {'id': 'l3-ann2', 'type': 'bpmnTextAnnotation', 'boundingBox': box(300, 360, 160, 50), 'style': style(),
     'text': t('[CONTROL] Three-way match (F04)', 10)},
    legend('l3-legend', 40, 570, ['Dotted line = annotation; layers: Issues and Controls overlays']),
], 'lines': [
    line('l3-f1', 'l3-start', 'l3-a1'), line('l3-f2', 'l3-a1', 'l3-a2'), line('l3-f3', 'l3-a2', 'l3-g1'),
    line('l3-f4', 'l3-g1', 'l3-g3', 'Yes'), line('l3-f5', 'l3-g1', 'l3-a3', 'No'), line('l3-f6', 'l3-a3', 'l3-g2'),
    line('l3-f7', 'l3-g2', 'l3-g3', 'Approved'), line('l3-f8', 'l3-g2', 'l3-a5', 'Rejected'),
    line('l3-f9', 'l3-g3', 'l3-a4'), line('l3-f10', 'l3-a4', 'l3-end1'), line('l3-f11', 'l3-a5', 'l3-end2'),
    {**line('l3-as1', 'l3-ann1', 'l3-a3'), 'stroke': {'color': C['line'], 'width': 1, 'style': 'dotted'},
     'endpoint2': {'type': 'shapeEndpoint', 'style': 'none', 'shapeId': 'l3-a3'}},
    {**line('l3-as2', 'l3-ann2', 'l3-a2'), 'stroke': {'color': C['line'], 'width': 1, 'style': 'dotted'},
     'endpoint2': {'type': 'shapeEndpoint', 'style': 'none', 'shapeId': 'l3-a2'}},
]}

DOC = {'version': 1, 'documentSettings': {'units': 'px'}, 'pages': [L1, L2, L3]}

if __name__ == '__main__':
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    (out / 'lucid-template-document.json').write_text(json.dumps(DOC, indent=2) + '\n')
    zi = zipfile.ZipInfo('document.json', date_time=(2026, 1, 1, 0, 0, 0))
    with zipfile.ZipFile(out / 'process-map-template.lucid', 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(zi, json.dumps(DOC, indent=2) + '\n')
    print('written', out)
