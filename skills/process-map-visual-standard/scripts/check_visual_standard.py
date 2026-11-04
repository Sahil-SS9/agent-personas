#!/usr/bin/env python3
"""Check a Lucid Standard Import document (document.json or a .lucid zip)
against a process-map house style (house-style.json). Python 3.9+, stdlib only.

Usage: python3 check_visual_standard.py DOC.lucid|document.json [--style house-style.json]
Exit 0 when no errors (warnings allowed), 1 on errors, 2 on usage problems.
"""
import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_STYLE = HERE.parent / 'templates' / 'house-style.json'

ACTIVITY = {'bpmnActivity', 'process', 'predefinedProcess'}
EVENT = {'bpmnEvent'}
GATEWAY = {'bpmnGateway', 'decision'}
POOLS = {'bpmnPool', 'swimLanes'}
BLACKBOX = {'bpmnBlackBoxPool'}
ARTEFACT = {'bpmnTextAnnotation', 'bpmnDataObject', 'bpmnDataStore', 'note'}
SIZE_KEY = {'bpmnActivity': 'activity', 'bpmnEvent': 'event', 'bpmnGateway': 'gateway',
            'bpmnDataObject': 'data_object', 'bpmnDataStore': 'data_store'}
TAG_RE = re.compile(r'<[^>]+>')


def plain(text):
    if isinstance(text, dict):
        text = text.get('text', '')
    return TAG_RE.sub(' ', str(text or '')).replace('&nbsp;', ' ').strip()


def raw(text):
    return text.get('text', '') if isinstance(text, dict) else str(text or '')


def norm(colour):
    if not isinstance(colour, str):
        return None
    c = colour.strip().upper()
    if re.fullmatch(r'#[0-9A-F]{8}', c):
        c = c[:7]
    if re.fullmatch(r'#[0-9A-F]{3}', c):
        c = '#' + ''.join(ch * 2 for ch in c[1:])
    return c if re.fullmatch(r'#[0-9A-F]{6}', c) else None


def lum(hexcolour):
    r, g, b = (int(hexcolour[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def font_sizes(text):
    return [float(x) for x in re.findall(r'font-size:\s*([0-9.]+)pt', raw(text))]


def load(path):
    p = Path(path)
    if p.suffix == '.lucid':
        with zipfile.ZipFile(p) as z:
            return json.loads(z.read('document.json'))
    return json.loads(p.read_text())


def inside(inner, outer):
    a, b = inner.get('boundingBox', {}), outer.get('boundingBox', {})
    try:
        return (a['x'] >= b['x'] and a['y'] >= b['y'] and a['x'] + a['w'] <= b['x'] + b['w']
                and a['y'] + a['h'] <= b['y'] + b['h'])
    except (KeyError, TypeError):
        return False


def check(doc, style):
    errors, warnings = [], []
    cols, lim, sizes, fonts = style['colours'], style['limits'], style['sizes_px'], style['fonts']
    sem = cols['semantic']
    allowed_fill = {norm(cols['fill']), norm(cols['header_fill']), '#FFFFFF'} | {norm(v['fill']) for v in sem.values()}
    allowed_stroke = {norm(cols['line'])} | {norm(v['border']) for v in sem.values()}
    allowed_text = {norm(cols['text']), norm(cols['text_secondary'])}
    sem_by_border = {norm(v['border']): (k, v) for k, v in sem.items() if v.get('tag')}
    title_re = re.compile(style['page']['title_pattern'])

    if doc.get('version') != 1:
        errors.append('standard-import-version-not-1')
    pages = doc.get('pages') or []
    if not pages:
        errors.append('no-pages')
    page_ids = {p.get('id') for p in pages}
    seen = set()
    for page in pages:
        for group in ('shapes', 'lines', 'groups', 'layers'):
            for item in page.get(group, []) or []:
                i = item.get('id')
                if i in seen:
                    errors.append('duplicate-id: ' + str(i))
                seen.add(i)

    for page in pages:
        pid = page.get('id')
        shapes = page.get('shapes', []) or []
        lines = page.get('lines', []) or []
        by_id = {s.get('id'): s for s in shapes}
        texts = [plain(s.get('text')) for s in shapes]

        # Page furniture.
        titles = [t for t in texts if title_re.search(t)]
        if not titles:
            errors.append(f'{pid}: missing-title-block (level, number, name, as-is/to-be, version, status)')
        if not any(t.startswith(style['page']['legend_prefix']) for t in texts):
            errors.append(f'{pid}: missing-legend')
        level = titles[0][:2] if titles else None
        if level in ('L2', 'L3', 'L4'):
            crumbs = [s for s in shapes if plain(s.get('text')).startswith(style['page']['breadcrumb_prefix'])]
            if not crumbs:
                errors.append(f'{pid}: missing-breadcrumb-to-parent')
            elif not any(a.get('type') == 'gotoPage' and a.get('pageId') in page_ids
                         for s in crumbs for a in (s.get('actions') or [])):
                warnings.append(f'{pid}: breadcrumb-has-no-working-gotoPage-link')

        # Colours, contrast, borders, text.
        semantic_used = set()
        for s in shapes:
            sid, t = s.get('id'), s.get('type')
            st = s.get('style') or {}
            fill = norm((st.get('fill') or {}).get('color')) if (st.get('fill') or {}).get('type') == 'color' else None
            stroke = st.get('stroke') or {}
            scol = norm(stroke.get('color'))
            tcol = norm(st.get('textColor')) or norm(cols['text'])
            if fill and fill not in allowed_fill:
                errors.append(f'{pid}/{sid}: fill-colour-not-in-palette {fill}')
            if scol and scol not in allowed_stroke:
                errors.append(f'{pid}/{sid}: border-colour-not-in-palette {scol}')
            if st.get('textColor') and tcol not in allowed_text:
                errors.append(f'{pid}/{sid}: text-colour-not-in-palette {tcol}')
            if stroke.get('style') in ('dashed', 'dotted') and t not in BLACKBOX:
                errors.append(f'{pid}/{sid}: reserved-border-style {stroke.get("style")} (dashed/dotted belong to message flow/association)')
            label = plain(s.get('text'))
            if fill and label and contrast(tcol, fill) < cols['min_text_contrast']:
                errors.append(f'{pid}/{sid}: text-contrast {contrast(tcol, fill):.2f} < {cols["min_text_contrast"]}')
            if scol and contrast(scol, fill or '#FFFFFF') < cols['min_non_text_contrast']:
                errors.append(f'{pid}/{sid}: border-contrast {contrast(scol, fill or "#FFFFFF"):.2f} < {cols["min_non_text_contrast"]}')
            if scol in sem_by_border:
                key, spec = sem_by_border[scol]
                semantic_used.add(key)
                tagged = spec['tag'] in label
                if not tagged:
                    for ln in lines:
                        ends = {ln.get('endpoint1', {}).get('shapeId'), ln.get('endpoint2', {}).get('shapeId')}
                        if sid in ends:
                            other = (ends - {sid}).pop() if len(ends) > 1 else None
                            if other in by_id and spec['tag'] in plain(by_id[other].get('text')):
                                tagged = True
                if not tagged:
                    errors.append(f'{pid}/{sid}: colour-only-meaning: {key} colour without {spec["tag"]} tag (WCAG 1.4.1)')
                if (stroke.get('width') or 1) < spec['border_px']:
                    warnings.append(f'{pid}/{sid}: semantic-border-thinner-than-{spec["border_px"]}px')
            if t in ACTIVITY | EVENT | GATEWAY and label:
                sz = font_sizes(s.get('text'))
                if not sz:
                    warnings.append(f'{pid}/{sid}: no-explicit-font-size (Lucid auto-scales; sizes drift)')
                elif min(sz) < fonts['min_pt']:
                    errors.append(f'{pid}/{sid}: font-below-{fonts["min_pt"]}pt')
                if not fonts['bold_or_italic_in_element_labels'] and re.search(r'<(b|i|strong|em)\b|<br', raw(s.get('text')), re.I):
                    warnings.append(f'{pid}/{sid}: formatting-or-manual-break-in-element-label')
            if t in ACTIVITY and not label:
                errors.append(f'{pid}/{sid}: activity-unlabelled')
        if len(semantic_used - {'happy_path'}) > lim['semantic_colours_per_page_max']:
            errors.append(f'{pid}: too-many-semantic-colours')

        # Sizes: house sizes for BPMN types and one size per type on the page.
        per_type = {}
        for s in shapes:
            bb = s.get('boundingBox') or {}
            if s.get('type') in SIZE_KEY:
                per_type.setdefault(s['type'], set()).add((bb.get('w'), bb.get('h')))
                want = tuple(sizes[SIZE_KEY[s['type']]])
                if (bb.get('w'), bb.get('h')) != want:
                    warnings.append(f'{pid}/{s.get("id")}: size {bb.get("w")}x{bb.get("h")} != house {want[0]}x{want[1]}')
            elif s.get('type') in ACTIVITY | GATEWAY:
                per_type.setdefault(s['type'], set()).add((bb.get('w'), bb.get('h')))
        for typ, variants in per_type.items():
            if len(variants) > 1:
                errors.append(f'{pid}: mixed-sizes-for-{typ} {sorted(variants)}')

        # Pools and lanes.
        for s in shapes:
            if s.get('type') in POOLS:
                lanes = s.get('lanes') or []
                if len(lanes) > lim['lanes_per_pool_max']:
                    warnings.append(f'{pid}/{s.get("id")}: {len(lanes)}-lanes > {lim["lanes_per_pool_max"]}')
                bb = s.get('boundingBox') or {}
                vertical = s.get('vertical', s.get('type') == 'bpmnPool')
                span = bb.get('w') if vertical else bb.get('h')
                total = sum(l.get('width', 0) for l in lanes)
                if span is not None and abs(total - span) > 0.5:
                    errors.append(f'{pid}/{s.get("id")}: lane-widths {total} != pool span {span}')

        # Counts.
        acts = sum(1 for s in shapes if s.get('type') in ACTIVITY)
        flow = sum(1 for s in shapes if s.get('type') in ACTIVITY | EVENT | GATEWAY)
        if acts > lim['activities_per_page_target']:
            warnings.append(f'{pid}: {acts}-activities > target {lim["activities_per_page_target"]} (split into sub-processes)')
        if flow > lim['flow_elements_per_page_max']:
            errors.append(f'{pid}: {flow}-flow-elements > {lim["flow_elements_per_page_max"]} (decompose)')

        # Lines.
        pools = [s for s in shapes if s.get('type') in POOLS | BLACKBOX]
        def pool_of(shape_id):
            sh = by_id.get(shape_id)
            for p in pools:
                if sh is not None and (sh is p or inside(sh, p)):
                    return p.get('id')
            return None
        outgoing = {}
        for ln in lines:
            lid = ln.get('id')
            e1, e2 = ln.get('endpoint1') or {}, ln.get('endpoint2') or {}
            ends = []
            for e in (e1, e2):
                if e.get('type') == 'shapeEndpoint':
                    if e.get('shapeId') not in by_id:
                        errors.append(f'{pid}/{lid}: endpoint-shape-missing {e.get("shapeId")}')
                    ends.append(e.get('shapeId'))
            if ln.get('lineType') != style['lines']['shape']:
                errors.append(f'{pid}/{lid}: line-type {ln.get("lineType")} != {style["lines"]["shape"]}')
            stroke = ln.get('stroke') or {}
            lstyle = stroke.get('style', 'solid')
            lcol = norm(stroke.get('color')) or norm(cols['line'])
            if lcol not in allowed_stroke:
                errors.append(f'{pid}/{lid}: line-colour-not-in-palette {lcol}')
            types = {by_id[e].get('type') for e in ends if e in by_id}
            if len(ends) == 2 and ends[0] in by_id and ends[1] in by_id:
                cross_pool = pool_of(ends[0]) != pool_of(ends[1]) or types & BLACKBOX
                if types & ARTEFACT:
                    expected = 'dotted'
                elif cross_pool:
                    expected = 'dashed'
                else:
                    expected = 'solid'
                if lstyle != expected:
                    errors.append(f'{pid}/{lid}: line-style {lstyle} != {expected} for this connection')
                if expected == 'solid':
                    outgoing.setdefault(ends[0], []).append(ln)
        for gid, outs in outgoing.items():
            if by_id.get(gid, {}).get('type') in GATEWAY and len(outs) > 1:
                g = by_id[gid]
                if g.get('gatewayType', 'exclusive') in ('exclusive', 'inclusive', 'none') or g.get('type') == 'decision':
                    for ln in outs:
                        if not any(plain(x) for x in (ln.get('text') or [])):
                            warnings.append(f'{pid}/{ln.get("id")}: unlabelled-branch-from-{gid}')
    return {'status': 'fail' if errors else 'pass', 'errors': sorted(set(errors)), 'warnings': sorted(set(warnings)),
            'pages': len(pages)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('document')
    ap.add_argument('--style', default=str(DEFAULT_STYLE))
    a = ap.parse_args(argv)
    try:
        doc, style = load(a.document), json.loads(Path(a.style).read_text())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(json.dumps({'status': 'fail', 'errors': ['unreadable: ' + str(exc)]}))
        return 2
    result = check(doc, style)
    result['file'] = a.document
    print(json.dumps(result, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
