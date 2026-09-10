#!/usr/bin/env python3
"""Audit ComfyUI workflow JSON files against a live server's node registry.

Usage:
  python audit_workflow_nodes.py [--server http://127.0.0.1:8188] <workflow.json | dir>...

Handles BOTH formats:
  - API format:    {"<id>": {"class_type": "...", "inputs": {...}}}
  - Editor format: {"nodes": [{"type": "...", ...}], "links": [...]}

Output per file: READY or GAP with categorized missing types.
Exit code 0 = all audited files READY (noise categories excluded).

NOISE CATEGORIES (reported but not treated as blockers):
  - UUID-looking types: frontend GROUP NODE instances; they resolve to their
    inner nodes at load time. Always tolerate.
  - Core frontend pseudo-nodes: Reroute, PrimitiveNode, MarkdownNote — these
    live in the frontend/core, not object_info. MarkdownNote only exists on
    newer ComfyUI versions; tolerate on any.
  - Display-name-keyed nodes: packs like rgthree register class types with
    display-style keys such as "Label (rgthree)" / "Fast Bypasser (rgthree)".
    If the pack IS installed and these show "missing", treat as cosmetic —
    they load fine in the UI (verified: generation succeeded with all flagged).
The REAL signal = missing class_type from a custom pack (e.g. llama_cpp_*,
impact nodes) → that pack must be installed before the workflow can run.
"""
import json, os, re, sys, urllib.request, argparse, glob

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
PSEUDO = {"Reroute", "PrimitiveNode", "MarkdownNote", "Note"}

def load_node_types(server):
    url = server.rstrip("/") + "/object_info"
    with urllib.request.urlopen(url, timeout=120) as r:
        return set(json.loads(r.read().decode()).keys())

def extract_types(path):
    d = json.load(open(path, encoding="utf-8"))
    types = []
    if isinstance(d, dict):
        if isinstance(d.get("nodes"), list):          # editor format
            types = [n.get("type") for n in d["nodes"]]
        else:                                          # API format
            types = [v.get("class_type") for v in d.values()
                     if isinstance(v, dict) and "class_type" in v]
    return [t for t in types if t]

def audit(path, known):
    types = extract_types(path)
    if not types:
        return None
    groups, pseudo, display, missing = set(), set(), set(), set()
    for t in types:
        if t in known:
            continue
        if UUID_RE.match(t):
            groups.add(t)
        elif t in PSEUDO:
            pseudo.add(t)
        elif "(" in t and t.endswith(")"):   # "Name (pack)" display-style keys
            display.add(t)
        else:
            missing.add(t)
    return dict(total=len(types), groups=groups, pseudo=pseudo,
                display=display, missing=missing)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--server", default="http://127.0.0.1:8188")
    ap.add_argument("paths", nargs="+")
    args = ap.parse_args()

    known = load_node_types(args.server)
    print(f"server {args.server}: {len(known)} node types registered\n")

    files = []
    for p in args.paths:
        files.extend(glob.glob(os.path.join(p, "**", "*.json"), recursive=True)
                     if os.path.isdir(p) else [p])

    fail = 0
    for f in sorted(files):
        try:
            r = audit(f, known)
        except Exception as e:
            print(f"[ERR  ] {f}: {e}"); fail += 1; continue
        if r is None:
            print(f"[SKIP ] {f}: no recognizable node list"); continue
        if not r["missing"]:
            print(f"[READY] {os.path.basename(f)}: {r['total']} nodes OK"
                  + (f"  (noise: {len(r['groups'])} group, {len(r['pseudo'])} pseudo, "
                     f"{len(r['display'])} display-name)" if (r['groups'] or r['pseudo'] or r['display']) else ""))
        else:
            fail += 1
            print(f"[GAP  ] {os.path.basename(f)}: MISSING {sorted(r['missing'])}")
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    main()
