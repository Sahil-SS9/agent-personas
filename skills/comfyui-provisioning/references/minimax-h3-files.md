# MiniMax H3 on a 12 GB card — file map & ecosystem (verified 2026-08)

Released 2026-08-02, open weights, **day-0 native ComfyUI support in v0.30.0**.
ComfyUI pruned ~40% of the model (modulation weights → lookup table) + ships
int8-convrot / fp8 quantizations + dynamic VRAM offloading → officially runs on
an RTX 3060; 12 GB cards (e.g. RTX 4070 Ti) are comfortable: ~720p/5s, longer
clips at 480–540p. Weights: https://huggingface.co/Comfy-Org/MiniMax-H3

## File → folder map
```
ComfyUI/
├── models/diffusion_models/   minimax_h3_{ref2va|fl2va}[_pruned]_{bf16|int8_convrot|fp8_scaled}.safetensors
├── models/text_encoders/      qwen3vl_32b_minimax_h3_{bf16|int8_convrot|nvfp4_awq}.safetensors
└── models/vae/                minimax_h3_video_vae_fp16.safetensors (5.2 GB)
                               minimax_h3_audio_vae_fp32.safetensors (0.6 GB)
```
fl2va = text/image/first-last-frame→video · ref2va = reference-to-video (up to 9 refs).

## Variant sizes (pruned = 12 GB-card tier)
| Diffusion variant | Size | VRAM tier |
|---|---|---|
| bf16 | 40 GB (66 GB unpruned) | 16 GB+ / datacenter — skip |
| int8_convrot | 21 GB (34 unpruned) | 16 GB unpruned / **12 GB pruned** |
| fp8_scaled (pruned) | 21 GB | 12 GB |
| Text encoder nvfp4_awq | 15.7 GB | ← use with 12 GB cards |

Community-verified 12 GB pick (Civitai H3 workflow): `ref2va_pruned_int8_convrot`.
Testing both int8 and fp8 pruned ref2va is reasonable — quality/speed differ per scene.

## Companion pieces
- Official workflow templates (T2V/I2V/R2V): github.com/Comfy-Org/workflow_templates
  `video_minimax_h3_{t2v,i2v,r2v}.json` — also in ComfyUI's template library.
- **kijai/ComfyUI-KJNodes** — has H3-specific commits ("Tiny VAE for H3",
  MiniMaxH3MemoryEfficientSageAttentionPatch). Update it before H3 sessions.
  Note: TinyVAEDecoder (nodes/tiny_vae.py) is an INTERNAL preview helper that
  loads tiny VAEs from models/vae_approx — it is deliberately NOT a registered
  node, so don't hunt for it in object_info or NODE_CONFIG.
  PatchTritonVAE (optional) needs triton/triton-windows; harmless to skip.
- **Tr1dae/ComfyUI-MiniMaxH3_LatentUpscaler** — 2-pass latent upscale between H3
  samplers (NestedTensor-aware; stock LatentUpscaleBy crashes on H3 AV latents).
  Wiring: sampler1 denoised_output → upscaler (+MODEL/NOISE/SIGMAS, cond) → NEW
  Guider from returned pos/neg → sampler2 with DisableNoise + low sigmas.
  `audio_denoise` knob: 0 = lock pass-1 audio, 1 = full audio remix.
- Civitai "MiniMax H3 All-in-One Reference Automatic Prompt Workflow" (DeepWhiteAI)
  adds llama-cpp auto-prompting: needs **lihaoyun6/ComfyUI-llama-cpp_vlm** node + BOTH
  `Qwen3.5-9B-Q8_0.gguf` and `mmproj-Q8_0.gguf` from
  huggingface.co/AVert888/Qwen3.5-9B-mmproj-q8_0-GGUF (missing mmproj =
  "not configured with a mmproj module" error — seen in the wild).
- **deepbeepmeep/Wan2GP** — standalone Gradio app (NOT a ComfyUI node), added
  MiniMax H3 support 2026-08-03 (v12.42). Own folder + own venv. Good A/B rig
  against ComfyUI-native H3; also runs Wan 2.1/2.2, LTX-2, Hunyuan, Qwen Image.
  - ⭐ **v12.42 uses ComfyUI-compatible pruned H3 checkpoints** — point it at the
    same weights you downloaded for ComfyUI; zero duplicate downloads.
  - Install: `scripts\install.bat` (1-click, picks best kernels for the GPU) or
    manual venv: `pip install torch==2.10.0 torchvision==0.25.0 torchaudio==2.10.0
    --index-url https://download.pytorch.org/whl/cu130` + `-r requirements.txt`.
  - Author tuning notes for consumer GPUs: 15-20 steps minimum (no distilled H3
    ckpt yet); FL2VA = shot creation/continuation + sliding windows, Ref2VA =
    reference-guided (no sliding windows); default memory mode "Lower VRAM";
    Spectrum step-skipping ≈ 2× faster (Advanced Mode); generate 480p then upscale
    with SeedVR2 (VRAM cut to ~⅓ in WanGP) or FlashVSR instead of native hi-res.

## Runtime reference (RTX 5060 Ti 16GB + 32GB RAM, per author)
10s 480p clip ≈ 950 s with int8_convrot. Expect more on 12 GB.

## Turbo LoRA — few-step (4–8 steps) generation & pruned-base gotcha
The Turbo LoRA renders video+audio in **4–8 sampling steps** instead of ~25
(multiple × faster on a 12 GB card). Recommended checkpoint:
**`minimax_h3_turbo_v4_step600_ema`**. Apply strength 1.0; stay in the 4–8 step
window (past 8 over-sharpens). Scheduler `simple` (larryvrh default) or
`euler`+`beta` with video sigma shift 12 / audio 4–6 (drbaph's pruned workflow).

**⚠️ THE critical gotcha — pruned-base LoRA key namespacing:**
- **larryvrh/MiniMax-H3-Turbo-Lora** (original) uses keys like
  `blocks.0.attn.qkv_proj.lora_A.weight` — these **do NOT load on the pruned/curve
  base** (ComfyUI logs "lora key not loaded: ..."). His custom node pack
  (`Larryvrh/ComfyUI-MiniMax-H3-Turbo`, search "MiniMax-H3 Turbo" in Manager)
  auto-detects a pruned base and re-injects time-conditioning, so one LoRA covers
  full + pruned **only if you run through his nodes**.
- **drbaph/MiniMax-H3-Turbo-Lora-ComfyUI** = third-party conversion re-keyed to
  `diffusion_model.blocks.*` and stripped of the 51 AdaLN pairs (259→208 pairs)
  so it loads cleanly with ComfyUI's built-in LoRA loader on the **pruned** model.
  **Use the drbaph conversion when on a pruned base.** Ships a ready-to-run
  example workflow (`fl_minimax_h3_turbo_lora_example_workflow.json`).
  All release lines available (v4_step600_ema recommended, plus ckpt500/850 and
  initial preview). Optional SageAttention / SolAttention / Spectrum / Gradient
  acceleration patches.
- **Turbo targets the fl2va (or full) diffusion model — NOT ref2va.** Verify which
  diffusion model is loaded in the UNETLoader before expecting Turbo to work.

## Uncensored text encoder alternative
**ethanfel/Qwen3-VL-32B-Ultra-Heretic-H3-ComfyUI-INT8-ConvRot** — abliterated
("Ultra Heretic", from llmfan46) Qwen3-VL-32B repackaged as an H3 conditioning
encoder (layers 0–49, ~24.6 GB INT8 ConvRot or ~48 GB BF16) + optional generation
tails (layers 50–63, for standalone text gen). Swap in place of the stock
`qwen3vl_32b_minimax_h3_nvfp4_awq` encoder to cut refusals while prompting, at a
VRAM cost. Needs a current ComfyUI + pinned `comfy-kitchen` dependency; loads via
the `minimax` CLIPLoader type.
