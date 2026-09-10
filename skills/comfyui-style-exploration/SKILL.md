---
name: comfyui-style-exploration
description: "Use when comparing ComfyUI styles."
version: 1.0.0
license: MIT
---
# ComfyUI Style Exploration

A class-level workflow for exploring multiple visual treatments of the same subject in ComfyUI. The goal is a useful comparison, not a pile of unrelated renders: hold identity, framing, palette, and scene constants steady wherever possible, then vary one style axis at a time.

## When to Use

- The user wants to compare several art directions, genres, or style LoRAs.
- A character or brand subject must remain recognizable across variants.
- The user wants a small style study before committing to a final image.
- The user asks for several generations with deliberate sequential pacing.

## Core Method

1. Lock the approved subject identity core: face, hair, eyes, signature features, palette, and age/build cues.
2. Keep aspect ratio, resolution, crop, pose, outfit, and environment constant wherever possible. Use a stable seed for pure style comparisons; use fresh seeds for independent alternatives.
3. Define concrete style cards with visual vocabulary, palette rules, and the exact LoRA/model used.
4. Verify the exact LoRA filename in the live models/loras inventory. Preserve case and extension.
5. Prefer the native `image_krea2_turbo_t2i` local template for Krea-2. Fetch with local checking enabled and require `runnable: true`.
6. For a LoRA study, enable it explicitly: set the exact `lora_name`, set `strength_model` explicitly, and turn on the LoRA switch. For a native-model baseline, explicitly disable the LoRA switch and do not rely on a prior workflow state. For dynamic subgraphs, use stable template params and avoid positional writes to suspect slots.
7. Treat aspect ratio as a separate verification target. The template's nested `ResolutionSelector` may override direct `width`/`height` parameters; set `49.aspect_ratio` (and re-list slots after fetching) rather than assuming width/height writes are authoritative. Verify the downloaded image dimensions—successful generation alone does not prove the requested ratio.
8. For a baseline capability study, keep LoRA/reference off, start with prompt enhancement off, use the official Turbo defaults (8 steps, CFG 0), and vary one composition or aspect-ratio concept at a time. Distinguish intended framing in the prompt from actual pixel dimensions.
9. Run sequentially when the user requests deliberate pacing, when VRAM is limited, or when failure observation matters.
10. Save all outputs into a dedicated comparison directory with descriptive prefixes. Verify every file exists and has valid image metadata, including dimensions.
11. Deliver every real saved path as `MEDIA:<absolute path>`, with compact labels for comparison.
12. Review the actual output before making aesthetic claims. Distinguish identity fidelity, mood, intended use (avatar, cover, poster), and whether the render genuinely achieved the requested aspect ratio.

## Prompt Structure

Use: identity core → fixed outfit/pose/composition → setting/lighting → concrete style vocabulary → palette constraints → identity-preservation instruction.

Strong style wording is specific: `1980s OVA cel shading, painted background, navy shadows, cyan rim light` is better than `retro anime look` alone.

## Krea-2 Pattern

The Krea-2 local text-to-image template commonly exposes `30/19.value` for the prompt, `29.filename_prefix` for output naming, `30/15.lora_name` for the style LoRA, `30/15.strength_model` for strength, and `30/22.switch` for LoRA enablement. Re-list slots for the current template because dynamic-combo pairing can drift.

Conceptual parameter set:

```json
{
  "29.filename_prefix": "Subject_StyleName",
  "30/19.value": "<identity + fixed composition + style card>",
  "30/15.lora_name": "exact_style_lora.safetensors",
  "30/15.strength_model": 1.0,
  "30/22.switch": true
}
```

Use template params rather than editing a copied workflow unless slot pairing is suspect. If no dedicated LoRA exists, label the direction as prompt-led or an explicit approximation; never imply a dedicated asset was used.

## Comparison Study Example

A five-card Luna study can keep platinum-white hair, light-blue eyes, freckles, dark matte lips, a black mock-turtleneck, upper-body framing, and a cool monochrome palette constant while varying:

- 1980s OVA / Neo-Tokyo — `krea2_retroanime.safetensors`
- Retro-futurist editorial — installed style asset plus prompt-led geometric direction, explicitly labeled
- Ink-wash / darkbrush — `krea2_darkbrush.safetensors`
- Mecha command — retroanime LoRA plus command-portrait vocabulary
- Minimalist manga cover — retroanime LoRA plus graphic negative-space vocabulary

Generate one at a time and save all five together when requested.

## Verification Checklist

- [ ] Identity block is consistent.
- [ ] Exact LoRA exists and matches the requested style.
- [ ] LoRA enable switch is true when requested.
- [ ] Strength is explicitly set and reported.
- [ ] Each job reaches `completed` with `error: null`.
- [ ] Every output is downloaded to the intended directory.
- [ ] Every delivered path is a real file with valid image metadata.
- [ ] Labels distinguish actual LoRA usage from prompt-only style direction.

## References

- `references/krea2-style-study.md` — tested Krea-2 parameter addresses, style-card vocabulary, pacing, and delivery notes.
