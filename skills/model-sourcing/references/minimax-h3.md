# MiniMax H3 — Local Setup Notes (verified Aug 2026)

Open-weights omni-modal video model from MiniMax (3rd gen after Hailuo 01/02).
Released 2026-08-02 with **day-0 native ComfyUI support** (requires ComfyUI ≥ 0.30.0).

Source: blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui · hf.co/Comfy-Org/MiniMax-H3

## Capabilities

- Text-to-video, image-to-video, first/last-frame, reference-to-video
  (up to 9 refs — images, video, or audio in one prompt)
- Up to 2K output, up to 15s clips, **native stereo audio** (same pass, not post)
- Multimodal context: prompt describes relationships between mixed inputs

## How it fits consumer GPUs

ComfyUI pruned the modulation weights (~40% of params) → functionally equivalent
lookup table. Ships int8-convrot + fp8 quants; custom kernels cut peak VRAM;
dynamic VRAM offloading. Total footprint reduced 66%: 123.6 GB full-precision →
42.5 GB smallest variants. **Official claim: runs on an RTX 3060.**
Community-verified on 8 GB cards at reduced resolutions.

Practical targets on 12 GB (RTX 4070 Ti class): ~720p/5s comfortable,
480–540p for 10–15s, 2K only with aggressive offloading.

## File → folder map (hf.co/Comfy-Org/MiniMax-H3, sizes verified via HF API)

```
models/diffusion_models/
  minimax_h3_fl2va_pruned_fp8_scaled.safetensors      20.96 GB  ← t2v/i2v/flf pick for 12 GB
  minimax_h3_ref2va_pruned_fp8_scaled.safetensors     20.96 GB  ← reference-to-video variant
  (bf16 = 66.28 GB each, pruned_bf16 = 40.23 GB, int8_convrot = 20.97–34.04 GB — skip on consumer)
models/text_encoders/
  qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors        15.69 GB  ← pick for 12 GB
  (int8_convrot = 27.14 GB, bf16 = 51.51 GB)
models/vae/
  minimax_h3_video_vae_fp16.safetensors                5.21 GB
  minimax_h3_audio_vae_fp32.safetensors                0.61 GB
```

**12 GB minimum set ≈ 42.5 GB** (fl2va pruned fp8 + nvfp4 encoder + both VAEs);
add ref2va (+21 GB) only if reference-to-video is needed.

## Workflow templates (official, in Comfy-Org/workflow_templates)

- T2V: templates/video_minimax_h3_t2v.json
- I2V: templates/video_minimax_h3_i2v.json
- R2V: templates/video_minimax_h3_r2v.json

## Enumerating file sizes without cloning

```
curl -s "https://huggingface.co/api/models/Comfy-Org/MiniMax-H3/tree/main?recursive=true"
```
Returns JSON array; each entry has `path` and `size` (bytes). Sum before downloading.
