---
name: comfyui-character-gen
description: "Use for identity-preserving character generation workflows."
version: 1.0.0
license: MIT
---
# ComfyUI Character Generation Expert

Build production-ready ComfyUI workflows for consistent character generation across image, video, and voice modalities.

Source: https://github.com/mckruz/comfyui-expert (installed from skills hub, normalized frontmatter)

## Quick Decision: Which Approach?

**Starting from reference images (like 3D renders)?**
→ **InfiniteYou** (state-of-the-art 2025) or InstantID + IP-Adapter (proven, lower VRAM)

**Need highest identity fidelity?**
→ **FLUX.2** (up to 10 ref images) or **PuLID Flux II** (no model pollution)

**Want iterative editing without retraining?**
→ **FLUX Kontext** (context-aware, maintains consistency across edits)

**Creating video content?**
→ **LTX-2** (4K production-ready), **Wan 2.2 MoE** (film-level), or **FramePack** (60-sec on 6GB!)

**Need voice for character?**
→ **TTS Audio Suite** (unified platform, 23 languages) or **F5-TTS Cross-Lingual**

## Core Workflow Patterns

### Pattern 1: Zero-Shot Character Generation (No Training)

Best for: Quick iteration, 3D-to-photorealism conversion, limited reference images

```
Load Reference Face → InstantID + IP-Adapter FaceID → ControlNet Pose → KSampler → FaceDetailer → Upscale
```

**Critical settings:**
- CFG: 4-5 (prevents burning with InstantID)
- Resolution: 1016×1016 (avoids watermark artifacts)
- IP-Adapter weight: 0.6-0.8
- InstantID noise injection: 35% to negative

### Pattern 2: LoRA + Identity Methods (Maximum Consistency)

Best for: Production work, character series, video generation base

```
Train LoRA → Load LoRA + Checkpoint → Add InstantID/PuLID → Generate → FaceDetailer → ReActor (optional) → Upscale
```

**Training requirements:**
- 15-30 images, varied poses/expressions/lighting
- Unique trigger word (e.g., "sage_character")
- See `comfyui-lora-training` skill for full parameters

### Pattern 3: Video Generation Pipeline

Best for: Talking heads, character animation, promotional content

```
Generate/Load Hero Image → Wan 2.1 I2V OR AnimateDiff → FaceDetailer per frame → Frame Interpolation → Video Combine
```

**Model selection:**
- Wan 2.1 14B: Best quality, 24GB+ VRAM, slower
- Wan 2.1 1.3B: 8GB VRAM, good quality, faster
- AnimateDiff Lightning: Fastest, best for iteration

### Pattern 4: Talking Head with Voice

Best for: Character dialogue, presentations, social content

```
Approach 1 (Image → Talking Head):
Character Portrait → Generate Audio → SadTalker/LivePortrait → CodeFormer Enhancement → Final Video

Approach 2 (Video → Add Voice):
Existing Video → Generate Audio → Wav2Lip Lip-Sync → CodeFormer Enhancement → Final Video
```

## Model Recommendations

### Image Generation
| Use Case | Model | Notes |
|----------|-------|-------|
| Best photorealism | FLUX.1-dev | Slow but superior quality |
| Multi-reference consistency | FLUX.2 | Up to 10 ref images, strong identity preservation |
| Fast iteration | RealVisXL V5.0 | Good balance speed/quality |
| Character editing | FLUX Kontext | Context-aware, maintains consistency across edits |

### Identity Preservation (State-of-Art)
| Method | Best For | VRAM | Notes |
|--------|----------|------|-------|
| FLUX.2 | Multi-reference consistency | 24GB+ | Up to 10 ref images, branded content |
| InfiniteYou | Highest identity match | 24GB | ICCV 2025 Highlight, SIM/AES variants |
| FLUX Kontext | Iterative editing | 12-32GB | Built-in consistency, no retraining |
| PuLID Flux II | Dual characters, no pollution | 24-40GB | Contrastive alignment solves model pollution |
| AuraFace | Commercial identity encoding | 12GB | Open-source ArcFace alternative |
| InstantID | Style transfer, 3D→realistic | 12GB | Maintenance mode but still excellent |
| IP-Adapter FaceID | Speed, lower VRAM | 6GB+ | Good baseline approach |

### Video Generation
| Model | Quality | Speed | VRAM | Notes |
|-------|---------|-------|------|-------|
| LTX-2 | ★★★★★ | Medium | 16GB+ | First open-source 4K audio+video, production-ready |
| Wan 2.2 MoE | ★★★★★ | Slow | 24GB+ | Film-level aesthetics, first+last frame control |
| FramePack | ★★★★★ | Medium | 6GB | 60-sec videos, VRAM-invariant breakthrough |
| Wan 2.1 1.3B | ★★★★ | Medium | 8GB+ | Consumer-friendly |
| AnimateDiff V3 | ★★★ | Fast | 8GB | Motion/camera LoRAs, infinite length |

## Essential Custom Nodes

Install via ComfyUI-Manager:

```
ComfyUI-Manager              # Must install first
ComfyUI_IPAdapter_plus       # IP-Adapter and FaceID
ComfyUI_InstantID            # InstantID workflow
ComfyUI-Impact-Pack          # FaceDetailer
ComfyUI-ReActor              # Face swapping
ComfyUI-AnimateDiff-Evolved  # Video generation
ComfyUI-VideoHelperSuite     # Video I/O
comfyui_controlnet_aux       # Pose/depth preprocessors
ComfyUI_UltimateSDUpscale    # Tiled upscaling
ComfyUI-Frame-Interpolation  # Smooth video
```

## RTX 50 Series Optimization

ComfyUI v0.8.1 adds major RTX 50 Series enhancements:

```
Launch flags: --highvram --fp8_e4m3fn-unet
```

- **NVFP4/NVFP8 precision formats**: 3x faster performance, 60% VRAM reduction on RTX 50 Series
- **Weight streaming**: Uses system RAM when VRAM exhausted, enables larger models on mid-range GPUs
- Enable tiled VAE for 8K+ upscaling
- Batch 4× 1024×1024 generations in parallel
- Use FP8 quantization for FLUX (50% VRAM reduction)

## Workflow Generation Process

When building a workflow for a user:

1. **Clarify the goal**: Image only? Video? With voice? What's the source material?
2. **Select the pipeline pattern** from above based on requirements
3. **Generate the workflow** following node configurations
4. **Include model downloads** with exact filenames and paths
5. **Provide parameter recommendations** specific to their hardware/use case

## Example: 3D Render to Photorealistic Character

For converting stylized 3D renders (like game/VN characters) to photorealistic images:

**Recommended approach:** InstantID + IP-Adapter FaceID on FLUX

```
1. Load 3D render reference (best quality, front-facing)
2. Apply InstantID (extracts identity + facial keypoints)
3. Apply IP-Adapter FaceID Plus V2 (weight 0.7)
4. Use FLUX.1-dev checkpoint
5. Prompt: "photorealistic portrait, detailed skin texture, natural lighting, [character description]"
6. CFG: 4-5, Steps: 25-30
7. FaceDetailer pass (denoise 0.35)
8. Upscale with 4x-UltraSharp
```

This converts the stylized look to photorealism while preserving the core identity features.

## Pitfalls & Notes

- The failing node in an error is often NOT the root cause — check the traceback tail (see `comfyui-troubleshooting` skill).
- VRAM figures assume the model is the sole consumer; ComfyUI weight-streaming / FP8 can shrink requirements.
- Verify current model availability on HuggingFace/Civitai before pinning to a specific release — the image-gen space moves fast.
