#!/usr/bin/env python3
"""Resumable Civitai manifest downloader.

Usage: python download_civitai.py [--comfy <ComfyUI dir>] [--manifest manifest.json] [--env secrets/civitai.env]
Reads a manifest.json shaped like:
  {"results": [{"name", "type", "files": [{"file", "size_mb", "url"}]}]}
Routes files by Civitai type, skips existing, auto-unzips workflow zips.
"""
import argparse, json, os, re, subprocess, zipfile

DEST = {
    "Checkpoint": "models/checkpoints", "CheckpointMerge": "models/checkpoints",
    "LORA": "models/loras", "LoCon": "models/loras",
    "TextualInversion": "models/embeddings",
    "Workflows": "user_data/workflows", "Wildcards": "wildcards",
}

def curl(url, out):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    return subprocess.run(["curl", "-L", "-f", "--retry", "5", "--retry-delay", "3",
                           "-C", "-", "-o", out, url]).returncode in (0, 33)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comfy", default=os.path.join(os.path.expanduser("~"), "ComfyUI",
                    "ComfyUI_windows_portable", "ComfyUI"))
    ap.add_argument("--manifest", default=os.path.join(os.path.expanduser("~"), "ComfyUI", "manifest.json"))
    ap.add_argument("--env", default=os.path.join(os.path.expanduser("~"), "ComfyUI", "secrets", "civitai.env"))
    a = ap.parse_args()
    key = re.search(r"CIVITAI_API_TOKEN=(\S+)", open(a.env, encoding="utf-8").read()).group(1)
    data = json.load(open(a.manifest, encoding="utf-8"))
    ok, fail = [], []
    for e in data["results"]:
        dest_dir = os.path.join(a.comfy, DEST.get(e["type"], "models/loras"))
        for f in e["files"]:
            url = f["url"] + ("&" if "?" in f["url"] else "?") + "token=" + key
            out = os.path.join(dest_dir, f["file"])
            if os.path.exists(out) and os.path.getsize(out) > 1000:
                print(f"[skip] {f['file']} already present", flush=True); ok.append(out); continue
            print(f"[get ] {f['file']} ({f['size_mb']} MB) -> {DEST.get(e['type'])}", flush=True)
            if curl(url, out):
                ok.append(out)
                if out.lower().endswith(".zip"):
                    try:
                        ex = os.path.join(dest_dir, os.path.splitext(os.path.basename(out))[0])
                        with zipfile.ZipFile(out) as z: z.extractall(ex)
                        print(f"[unzip] -> {ex}", flush=True)
                    except Exception as err: print(f"[warn] unzip failed: {err}", flush=True)
            else:
                print(f"[FAIL] {f['file']}", flush=True); fail.append(f)
    print(f"\n=== DONE: {len(ok)} ok, {len(fail)} failed ===")
    for f in fail: print("  FAILED:", f["file"])

if __name__ == "__main__":
    main()
