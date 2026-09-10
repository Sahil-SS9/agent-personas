#!/usr/bin/env python3
"""last_error.py — pull the most recent failed ComfyUI job from /history.

Usage:
  python3 last_error.py [--host http://127.0.0.1:8188] [--max 5]

Prints: failing node, exception message/type, full traceback, executed-nodes
list, and the API-format inputs of the failing node (from the actually
submitted graph — trust this over the workflow .json on disk).
"""
import argparse
import json
import sys
import urllib.request


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="http://127.0.0.1:8188")
    ap.add_argument("--max", type=int, default=5)
    args = ap.parse_args()

    try:
        h = json.load(urllib.request.urlopen(
            f"{args.host}/history?max_items={args.max}", timeout=10))
    except Exception as e:
        print(f"ERROR: cannot reach {args.host}: {e}")
        sys.exit(1)

    items = h if isinstance(h, list) else list(h.values())
    errors = []
    for it in items:
        st = it.get("status", {})
        if st.get("status_str") != "error":
            continue
        errs = [m[1] for m in st.get("messages", [])
                if m and m[0] == "execution_error"]
        for d in errs:
            errors.append((it, d))

    if not errors:
        print(f"No errors in the last {args.max} history entries.")
        return

    it, d = errors[-1]  # most recent error
    print(f"prompt_id : {d.get('prompt_id')}")
    print(f"node      : {d.get('node_id')} ({d.get('node_type')})")
    print(f"exception : {d.get('exception_type')}: {d.get('exception_message')}")
    print(f"executed  : {d.get('executed')}")
    print("--- traceback tail ---")
    print("".join(d.get("traceback", []))[-2500:])

    p = it.get("prompt")
    g = p[2] if isinstance(p, list) and len(p) > 2 else p
    nid = d.get("node_id")
    if isinstance(g, dict) and nid in g:
        print(f"--- inputs of {nid} as submitted ---")
        print(json.dumps(g[nid], indent=1))


if __name__ == "__main__":
    main()
