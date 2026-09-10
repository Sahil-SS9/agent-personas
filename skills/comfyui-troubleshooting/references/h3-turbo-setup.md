# MiniMax H3 Turbo route (fl2va, 4-8 steps) — setup recipe (verified 2026-08)

Base setup (see `llama-cpp-vlm-workflow-patching.md` + `llama-cpp-offload-cpu-build.md`):
All-in-One ref2va workflow at `user_data/workflows/minimaxH3AllInOne_v10/`, 25 steps
`res_multistep` = the SLOW path. Turbo = fl2va model + Turbo LoRA + 4-8 steps (~3-5x faster).

## What's needed
| File | Source | Size |
|---|---|---|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `Comfy-Org/MiniMax-H3` HF -> diffusion_models | **19.53 GB** (the right pick for 12 GB VRAM; non-pruned int8 = 31.7 GB, bf16 = 61.7 GB) |
| Turbo LoRA `minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors` | already in `models/loras/` (620 MB, pruned ComfyUI form) | larryvrh/MiniMax-H3-Turbo-Lora hosts 10 GB experimental .bin checkpoints — do NOT use those |
| Community node pack | `mistaken-contadino194/ComfyUI-MiniMax-H3-Turbo` (git clone into custom_nodes/) | provides `MiniMaxH3TurboLoRA` + `MiniMaxH3TurboSampler`; bundles `h3_silu_temb_grid.safetensors` loaded from the pack's OWN dir (no placement needed) |
| Ready-made workflow | `example_workflows/minimax_h3_t2v_turbo.json` (i2v: MiniMaxH3ImageToVideo 1344x768, 73 frames ~= 3s @ 24fps, 6 steps, BasicGuider + SamplerCustomAdvanced) | copy to `user_data/workflows/MiniMaxH3_Turbo/` |

## Pointer swaps in the downloaded workflow (editor-format: nodes[] array, positional widgets_values)
- UNETLoader widgets_values[0]: `minimax_h3_fl2va_int8_convrot.safetensors` -> `minimax_h3_fl2va_pruned_int8_convrot.safetensors`
- CLIPLoader widgets_values[0]: `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` -> `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` (user's 14.6 GB TE; nvfp4_awq is the smallest TE quant: 14.6 GB vs int8 25.3 GB vs bf16 48 GB)
- MiniMaxH3TurboLoRA widgets_values[0]: `minimax_h3_turbo_4step_ema_ckpt500.safetensors` -> `minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors` (strength 1.0; dropdown reads `models/loras/`)

## Node-pack internals (why the LoRA gamble exists)
- The pack's LoRA node is a custom `LoRAAdapter` subclass + runtime adaln injection using the
  bundled silu(t_emb) grid (`_egrid()` reads `h3_silu_temb_grid.safetensors` from the pack dir).
  Standard `LoraLoader` / `DiTBlockLoraLoader` may NOT apply H3 Turbo LoRAs correctly — use the
  pack's node. This is why the "copy All-in-One + swap a few nodes" route is risky at exactly one point.
- `MiniMaxH3TurboSampler` drives the 4-step sampling; the workflow pairs it with BasicScheduler
  simple/6 steps. Do NOT force drbaph's beta/euler settings onto this workflow — it has its own sampler.

## Fallback: hand-modifying the All-in-One (untested LoRA loader)
Swap list if the user prefers no new node pack: UNETLoader -> fl2va pruned; `MiniMaxH3ReferenceToVideo`
-> `MiniMaxH3ImageToVideo` (exists in install); add LoRA (uncertain loader); BasicScheduler steps 25->6,
scheduler simple->beta; KSamplerSelect res_multistep->euler; sigma shifts video 12 / audio 4-6
(`MiniMaxH3SigmaShift` node exists). CLIP/VAEs/Video-out unchanged.

## Gotchas
- Custom node pack requires a ComfyUI restart to load (do it AFTER any running render).
- 1344x768 ~= 1.03 MP > the 0.9 MP 4070 Ti sweet spot — drop to 1280x736 if VRAM pressure.
- Original `drbaph/MiniMax-H3-Turbo-Lora-ComfyUI` repo 404s; successors:
  `mistaken-contadino194/ComfyUI-MiniMax-H3-Turbo` (used here) and `shuaixn/ComfyUI-MiniMaxH3DualClockSampler`.
- NEVER combine Spectrum-H3 with Turbo LoRA (incompatible). Spectrum ~= 1.7x faster on ref2va with
  no new downloads; Turbo ~= 3-5x on fl2va but needs the 19.53 GB model.
