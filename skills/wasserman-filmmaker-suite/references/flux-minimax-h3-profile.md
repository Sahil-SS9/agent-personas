# Flux 3 & MiniMax H3 Generator Profiles for Wasserman Suite

## Overview
Blockout and ScriptBreak export prompts in dialects for Seedance, Veo, Kling, LTX, Wan, plus stills targets like Midjourney and GPT-Image. **FLUX 3 and MiniMax H3 are NOT built-in.**

However, both are configurable via JSON profile files. Drop a `flux3.json` or `minimax-h3.json` into `<project>/profiles/` (or Blockout build) to enable them.

### Flux 3 profile (`flux3.json`)
```json
{
  "kind": "video",
  "name": "Flux-3",
  "maxDuration": 60,
  "aspects": ["16:9", "1:1", "9:16"],
  "exportWidth": 896,
  "fps": 24,
  "refModes": ["firstFrame", "lastFrame"],
  "attachHint": "Flux 3 via Hailuo API; use first-frame still as composition ref, prompt from Blockout prompt.txt",
  "adherenceClause": "video"
}
```

### MiniMax H3 profile (`minimax-h3.json`)
```json
{
  "kind": "video",
  "name": "MiniMax-H3",
  "maxDuration": 60,
  "aspects": ["16:9"],
  "exportWidth": 1280,
  "fps": 24,
  "refModes": ["referenceVideo", "firstFrame", "lastFrame"],
  "attachHint": "Local ComfyUI ref2va; use Blockout MP4 as reference video, stills for keyframes",
  "adherenceClause": "video"
}
```

## Generator-specific workflow notes

### Flux 3 (Hailuo API)
- **Input:** first-frame still + prompt.txt + timing/sequence prose
- **Output:** MP4 clip up to 2 minutes (free tier limits apply)
- **Integration:** Upload via Flux website after crafting prompt in Slate or ScriptBreak

### MiniMax H3 (Local ComfyUI)
- **Models needed:**
  - `minimax_h3_ref2va_pruned_int8_convrot.safetensors` (video)
  - `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` (text encoder)
  - `minimax_h3_video_vae_fp16.safetensors`
  - `minimax_h3_audio_vae_fp32.safetensors`
  - LLM: `Qwen3.5-9B-Q8_0.gguf` + `mmproj-Q8_0.gguf`
- **Workflow:** `minimaxH3AllInOne_v10` JSON → load reference video → enter prompt → queue → MP4 in `ComfyUI/output/video/`

## Blockout → Generator Handoff
1. Set camera marks, blocks, and composition in Blockout.
2. Export package → gives `first_frame.png`, `prompt.txt`, `reference.mp4` (optional).
3. **Flux 3:** Use `first_frame.png` as visual ref on website; paste prompt from `prompt.txt`.
4. **MiniMax H3:** Open `minimaxH3AllInOne_v10.json` in ComfyUI → drag `reference.mp4` into `LoadVideo` → paste prompt → queue.