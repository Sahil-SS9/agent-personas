# ComfyUI MiniMax H3 Workflow (Cheonma Setup)

Quick reference for generating with MiniMax H3 in your local ComfyUI.

## Models Required
- Video: `minimax_h3_ref2va_pruned_int8_convrot.safetensors`
- Text encoder: `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`
- Video VAE: `minimax_h3_video_vae_fp16.safetensors`
- Audio VAE: `minimax_h3_audio_vae_fp32.safetensors`
- LLM: `Qwen3.5-9B-Q8_0.gguf` + `mmproj-Q8_0.gguf`

## Stages (per the Beginner's Guide)
| Stage | Tool/Node | What to provide |
|---|---|---|
| A – Load brain | UNETLoader, CLIPLoader, VAELoader×2 | Models above |
| B – Build prompt | Input Text widget | Rough prompt + reference images |
| C – Sample | BasicScheduler (25 steps) | Resolution, duration |
| D – Save video | VAEDecode + CreateVideo + SaveVideo | Output in `ComfyUI/output/video/` |

## Workflow steps
1. Launch ComfyUI: `python -s main.py --disable-dynamic-vram`
2. Open workflow: drag `minimaxH3AllInOne_v10` JSON onto canvas.
3. Replace reference images (4 `LoadImage` nodes).
4. In `Input Text`, write: `让这张图的角色在夜里飞过城市上空...`
5. Queue → watch preview. Done in ~minutes depending on steps.
6. Find MP4 at `output/video/MiniMax_H3/`

## Turbo variant (for speed)
- Use `drbaph_turbo_lora_ref.json` workflow.
- Steps: 6–8, sampler: euler, scheduler: beta, sigma shift: 12.

## Prompt integration with Wasserman Suite
- **Blockout/ScriptBreak** → gives `prompt.txt` + first/last frames.
- Drop into `Input Text` node or concatenate; LLM can prefill from prompt.txt.
- **Reference MP4**: replace one `LoadVideo` or use `reference_video` node.

## Output locations
```
/c/Users/Hermes/ComfyUI/ComfyUI_windows_portable/ComfyUI/output/video/MiniMax_H3/
```