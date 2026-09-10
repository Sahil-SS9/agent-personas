# MiniMax H3 in ComfyUI — VRAM → variant cheat sheet

H3: open-weights omni-modal video model (MiniMax, Aug 2 2026), day-0 native
ComfyUI support (requires ComfyUI >= 0.30.0). T2V / I2V / first-last-frame /
reference-to-video (up to 9 refs), up to 2K, up to 15s, native stereo audio.
Weights: huggingface.co/Comfy-Org/MiniMax-H3 (repackaged for ComfyUI layout).

ComfyUI's optimizations: modulation-weight pruning (~40% of params → lookup
table), int8 convrot quantization, custom kernels, dynamic VRAM offloading.
Full precision footprint 123.6 GB → smallest variant 42.5 GB total.

## Which diffusion weights for which VRAM

| Variant | VRAM needed | Notes |
|---|---|---|
| `*_ref2va_pruned_int8_convrot.safetensors` (~21 GB) | **12 GB** | consumer sweet spot |
| `*_ref2va_int8_convrot.safetensors` (~34 GB) | 16 GB | |
| `*_ref2va_bf16.safetensors` (~66 GB) | 16 GB+ | avoid — datacenter only |
| `*_fl2va_*` counterparts | same tiers | T2V/I2V/first-last-frame path |

Rule of thumb: match the variant to the user's card BEFORE downloading —
the pruned int8 convrot files are the ones that fit 12 GB cards (RTX 3060/4070
class). ref2va = reference-to-video; fl2va = frame/text-to-video. Both share
the text encoder and VAEs.

Shared deps for either path:
- `models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` (15.7 GB)
  (also int8 27 GB and bf16 52 GB variants exist)
- `models/vae/minimax_h3_video_vae_fp16.safetensors` (5.2 GB)
- `models/vae/minimax_h3_audio_vae_fp32.safetensors` (0.6 GB)

## Realistic output targets on 12 GB (community-verified)
~720p / 5s comfortable; 480–540p for 10–15s (RTX 5060 Ti 16GB reference:
~950 s for a 10s 480p clip). 2K only with heavy offloading.

## Workflow-side extras (seen on Civitai H3 workflows)
Community "auto-prompt" H3 workflows add a llama.cpp VLM node
(ComfyUI-llama-cpp_vlm) with Qwen3.5-9B GGUF from
huggingface.co/AVert888/Qwen3.5-9B-mmproj-q8_0-GGUF.
Pitfall: the node needs BOTH the model GGUF and the mmproj GGUF — loading
only the model raises "Image input detected, but the loaded model is not
configured with a mmproj module."

## Official workflow templates (Comfy-Org)
github.com/Comfy-Org/workflow_templates/templates/:
video_minimax_h3_t2v.json, video_minimax_h3_i2v.json, video_minimax_h3_r2v.json
(Also in the ComfyUI template library UI.)

Sources: blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui,
huggingface.co/Comfy-Org/MiniMax-H3, civitai model 2832542 (DeepWhiteAI
workflow + community discussion), Aug 2026.
