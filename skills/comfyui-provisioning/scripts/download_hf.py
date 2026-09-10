#!/usr/bin/env python3
"""Resumable Hugging Face downloader into ComfyUI folders (no HF CLI needed).

Edit FILES with (repo-relative path, ComfyUI subfolder) pairs, or import and
call download() with your own list. Each file is curl -C - resumable.
"""
import os, subprocess

COMFY = os.path.join(os.path.expanduser("~"), "ComfyUI",
                     "ComfyUI_windows_portable", "ComfyUI")

# Example: MiniMax H3 phase-1 (pruned quantizations for a 12 GB card)
FILES = [
    ("Comfy-Org/MiniMax-H3", "diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors", "models/diffusion_models"),
    ("Comfy-Org/MiniMax-H3", "diffusion_models/minimax_h3_ref2va_pruned_fp8_scaled.safetensors",  "models/diffusion_models"),
    ("Comfy-Org/MiniMax-H3", "text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",       "models/text_encoders"),
    ("Comfy-Org/MiniMax-H3", "vae/minimax_h3_video_vae_fp16.safetensors",                        "models/vae"),
    ("Comfy-Org/MiniMax-H3", "vae/minimax_h3_audio_vae_fp32.safetensors",                        "models/vae"),
]

def download(files=FILES, comfy=COMFY, token=None):
    ok, fail = [], []
    for repo, path, sub in files:
        base = f"https://huggingface.co/{repo}/resolve/main/{path}"
        if token: base += (f"?token={token}" if "?" not in base else f"&token={token}")
        out = os.path.join(comfy, sub, os.path.basename(path))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        if os.path.exists(out) and os.path.getsize(out) > 1_000_000:
            print(f"[skip] {os.path.basename(path)} ({os.path.getsize(out)/1e9:.2f} GB)", flush=True)
            ok.append(out); continue
        print(f"[get ] {os.path.basename(path)}", flush=True)
        r = subprocess.run(["curl", "-L", "-f", "--retry", "8", "--retry-delay", "5",
                            "-C", "-", "-o", out, base])
        (ok.append(out) if r.returncode in (0, 33) else fail.append(path))
        if fail and fail[-1] == path:
            print(f"[FAIL] {os.path.basename(path)} rc={r.returncode}", flush=True)
    print(f"\n=== DONE: {len(ok)} ok, {len(fail)} failed ===")
    return ok, fail

if __name__ == "__main__":
    download()
