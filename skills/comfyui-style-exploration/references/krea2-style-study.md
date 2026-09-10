# Krea-2 Style Study Reference

## Tested local pattern

The local gallery template `image_krea2_turbo_t2i` was fetched with `check_local: true` and reported `runnable: true` on the Windows portable install. It uses Krea-2 Turbo with the installed `krea2_turbo_fp8_scaled.safetensors`, Qwen3-VL text encoder, and Qwen image VAE.

Useful exposed addresses observed in the study:

- `29.filename_prefix` — SaveImage prefix
- `30/19.value` — user prompt text
- `30/15.lora_name` — style LoRA filename
- `30/15.strength_model` — LoRA model strength
- `30/22.switch` — LoRA enable switch
- `30/5.width`, `30/5.height`, `30/5.batch_size` — image dimensions and batch
- `30/3.seed`, `30/3.steps`, `30/3.cfg` — sampler controls
- `49.aspect_ratio`, `49.megapixels`, `49.multiple` — resolution selector

Re-list slots after fetching because dynamic subgraph schemas can change. The slot listing warned that `30/16.thinking` was suspect; do not write that slot positionally.

## Style cards used successfully

- **OVA / Neo-Tokyo:** hand-painted cel shading, dramatic navy shadows, electric cyan rim light, rainy rooftop skyline, wet reflections, subtle film grain. Used `krea2_retroanime.safetensors` at 1.0.
- **Retro-futurist editorial:** geometric architecture, chrome/silver accents, razor-sharp graphic shadows, sculptural negative space, cool blue-grey studio, one cyan accent. Used `krea2_neondrip.safetensors` at 1.0 as the installed Krea style asset; describe the result as prompt-led editorial direction plus that asset, not as a dedicated retro-futurist LoRA.
- **Ink-wash / darkbrush:** sumi-e brushwork, bold gestural black strokes, pale paper-like negative space, selective blue-grey accents, soft bleeding ink textures. Used `krea2_darkbrush.safetensors` at 1.0.
- **Mecha command:** structured black command uniform, silver piping, cyan insignia, 1980s military science-fiction bridge, crisp cel shading, controlled heroic framing. Used `krea2_retroanime.safetensors` at 1.0.
- **Minimalist manga cover:** high-contrast black-and-white negative space, crisp linework, restrained halftone texture, one cool-blue accent, no readable text or logos. Used `krea2_retroanime.safetensors` at 1.0.

## Pacing and output

When the user asks for deliberate pacing, submit one job, wait for terminal completion, fetch its output, then submit the next. A successful run returned a completed job with `error: null`, an output URL from node `29`, and a downloaded 1024×1024 RGB PNG. The tested comparison outputs were saved under `C:/Users/Hermes/Downloads/Luna-Krea-Style-Comparison/` with descriptive prefixes.

## Important distinction

A prompt can describe a style while a LoRA supplies it. Report both separately. The retro-futurist editorial card used a prompt-led direction paired with an installed style asset; it should not be described as a dedicated retro-futurist LoRA unless one was actually selected.
