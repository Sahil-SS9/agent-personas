#!/usr/bin/env python3
"""Resolve Civitai model URLs/IDs into a ComfyUI download manifest.

Usage:
  python resolve_links.py 1297813:2776351 1377820 1302719:2121199 ...
    each arg is modelId or modelId:versionId (omit version -> latest)
  --token-file PATH   file containing CIVITAI_API_TOKEN=<key> (or set env var)
  --out PATH          manifest output (default: manifest.json)

Outputs manifest.json with per-file downloadUrl, size, and ComfyUI dest folder.
Stdlib only. Tested against civitai.com API 2026-08-04 (22/22 links resolved).
"""
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://civitai.com/api/v1"

DEST = {
    "Checkpoint": "models/checkpoints",
    "CheckpointMerge": "models/checkpoints",
    "LORA": "models/loras",
    "LoCon": "models/loras",          # modern ComfyUI loads LoCon from loras
    "TextualInversion": "models/embeddings",
    "Workflows": "user_data/workflows",
    "Wildcards": "wildcards",          # needs a wildcard node pack installed
}


def get_token():
    for arg_i, a in enumerate(sys.argv):
        if a == "--token-file":
            txt = open(sys.argv[arg_i + 1], encoding="utf-8").read()
            m = re.search(r"CIVITAI_API_TOKEN=(\S+)", txt)
            if m:
                return m.group(1)
    return os.environ.get("CIVITAI_API_TOKEN")


def api(url, token):
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}",
                 "User-Agent": "HermesComfySetup/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def resolve(model_id, version_id, token):
    if version_id is None:
        m = api(f"{BASE}/models/{model_id}", token)
        version_id = m["modelVersions"][0]["id"]
    v = api(f"{BASE}/model-versions/{version_id}", token)
    rtype = v.get("model", {}).get("type", "?")
    return {
        "model_id": model_id,
        "version_id": version_id,
        "name": v.get("model", {}).get("name"),
        "version_name": v.get("name"),
        "type": rtype,
        "base_model": v.get("baseModel"),
        "dest": DEST.get(rtype, "REVIEW"),
        "files": [
            {
                "file_id": f.get("id"),
                "file": f.get("name"),
                "size_mb": round(f.get("sizeKB", 0) / 1024, 2),
                "url": f.get("downloadUrl"),
                "fp": (f.get("metadata") or {}).get("fp"),
            }
            for f in v.get("files", [])
        ],
    }


def main():
    # strip --flag value pairs, keep positional model[:version] args
    skip = set()
    argv = sys.argv[1:]
    for i, a in enumerate(argv):
        if a.startswith("--") and i + 1 < len(argv):
            skip.add(argv[i + 1])
    args = [a for a in argv if not a.startswith("--") and a not in skip]

    token = get_token()
    if not token:
        sys.exit("No token: set CIVITAI_API_TOKEN env or pass --token-file")

    results, errors = [], []
    for arg in args:
        try:
            mid, _, vid = arg.partition(":")
            entry = resolve(int(mid), int(vid) if vid else None, token)
            results.append(entry)
            for f in entry["files"]:
                print(f"  [{entry['type']:>16}] {entry['name']} "
                      f"[{entry['version_name']}] {f['file']} "
                      f"({f['size_mb']} MB) -> {entry['dest']}")
            time.sleep(0.3)  # be polite to rate limits
        except Exception as e:
            errors.append({"arg": arg, "error": str(e)[:200]})
            print(f"  ERROR {arg}: {e}", file=sys.stderr)

    out = "manifest.json"
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    total_mb = sum(f["size_mb"] for e in results for f in e["files"])
    json.dump({"results": results, "errors": errors},
              open(out, "w", encoding="utf-8"), indent=1)
    print(f"\nResolved {len(results)}/{len(args)} -> {out} "
          f"({total_mb / 1024:.2f} GB total)")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
