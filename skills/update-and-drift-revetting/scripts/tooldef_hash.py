#!/usr/bin/env python3
"""Hash and diff MCP tool definitions to detect rug pulls and drift.

Usage:
  tooldef_hash.py snapshot <tools.json>               -> prints {tool: sha256} for approval records
  tooldef_hash.py diff <approved.json> <current.json>  -> field-level diff, exit 1 on any change

<tools.json> is the result of an MCP `tools/list` call: either {"tools": [...]}
or a bare list. <approved.json> is either another tools list or a saved
snapshot ({tool: sha256}); with a snapshot the diff can say WHICH tools
changed, but not which fields.

The WHOLE definition is hashed (name, title, description, inputSchema,
outputSchema, annotations, and any other field), canonicalised with sorted
keys. Hashing only the description misses a flipped readOnlyHint or a new
parameter. This detects definition changes. It cannot see server code that
changed behind an identical definition: re-vet code on every version.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

RUG_PULL_FIELDS = {
    "annotations": "approval-behaviour change (annotations are publisher hints, not enforcement)",
    "inputSchema": "parameter change",
    "description": "instruction/trigger change: re-read for injection",
    "outputSchema": "output contract change",
}


def load_tools(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    tools = data.get("tools", data) if isinstance(data, dict) else data
    if not isinstance(tools, list) or not all(isinstance(t, dict) and "name" in t for t in tools):
        raise ValueError(f"{path}: expected a tools/list result with named tools")
    names = [t["name"] for t in tools]
    if len(names) != len(set(names)):
        raise ValueError(f"{path}: duplicate tool names {sorted({n for n in names if names.count(n) > 1})}")
    return tools


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def snapshot(tools: list[dict]) -> dict[str, str]:
    return {t["name"]: hashlib.sha256(canon(t).encode()).hexdigest() for t in tools}


def schema_params(t: dict) -> dict:
    return (t.get("inputSchema") or {}).get("properties") or {}


def diff(old: list[dict] | dict, new: list[dict]) -> dict:
    new_by = {t["name"]: t for t in new}
    if isinstance(old, dict):  # snapshot form
        new_snap = snapshot(new)
        return {"added": sorted(set(new_snap) - set(old)), "removed": sorted(set(old) - set(new_snap)),
                "changed": [{"tool": n, "fields": ["unknown (approved record is a hash snapshot)"]}
                            for n in sorted(set(old) & set(new_snap)) if old[n] != new_snap[n]]}
    old_by = {t["name"]: t for t in old}
    changed = []
    for n in sorted(set(old_by) & set(new_by)):
        a, b = old_by[n], new_by[n]
        if canon(a) == canon(b):
            continue
        fields = sorted(k for k in set(a) | set(b) if canon(a.get(k)) != canon(b.get(k)))
        entry = {"tool": n, "fields": fields, "signals": [RUG_PULL_FIELDS[f] for f in fields if f in RUG_PULL_FIELDS]}
        pa, pb = schema_params(a), schema_params(b)
        entry["params_added"] = sorted(set(pb) - set(pa))
        entry["params_removed"] = sorted(set(pa) - set(pb))
        ha, hb = a.get("annotations") or {}, b.get("annotations") or {}
        entry["annotation_changes"] = {k: [ha.get(k), hb.get(k)] for k in sorted(set(ha) | set(hb)) if ha.get(k) != hb.get(k)}
        changed.append(entry)
    return {"added": sorted(set(new_by) - set(old_by)), "removed": sorted(set(old_by) - set(new_by)), "changed": changed}


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 2 and argv[0] == "snapshot":
            print(json.dumps(snapshot(load_tools(Path(argv[1]))), indent=2, sort_keys=True))
            return 0
        if len(argv) == 3 and argv[0] == "diff":
            raw_old = json.loads(Path(argv[1]).read_text())
            is_snap = isinstance(raw_old, dict) and "tools" not in raw_old and all(isinstance(v, str) for v in raw_old.values())
            old = raw_old if is_snap else load_tools(Path(argv[1]))
            d = diff(old, load_tools(Path(argv[2])))
            print(json.dumps(d, indent=2))
            return 1 if (d["added"] or d["removed"] or d["changed"]) else 0
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
