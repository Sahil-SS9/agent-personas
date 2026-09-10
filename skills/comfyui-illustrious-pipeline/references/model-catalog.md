# Illustrious Model Catalog — installed checkpoints + Civitai notes

All five are **Illustrious XL** base checkpoints under
`C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI\models\checkpoints\`.
VAE is baked into each. Use these exact `ckpt_name` values (case-sensitive, extension included).

## Quick settings matrix

> **Sampler names are ComfyUI internal names** (underscored), NOT A1111/Civitai labels ("Euler a" → `euler_ancestral`, "DPM++ 2M" → `dpmpp_2m`).

| Model (file) | Sampler | Scheduler | CFG | Steps | Res (px) | VAE |
|---|---|---|---|---|---|---|
| **Diving Niji-Muted vol2** `divingIllustrious_nijimutedcolorVol2.safetensors` | **`euler_ancestral`** | Karras | **4–6** | **20–30** | **896×1152** | baked |
| **Hyphoria v0.02** `hyphoria_v002.safetensors` | **`euler_ancestral`** / `dpmpp_2m` | Karras/"stable" | **3** (2.5–6) | **20–35** | 1024–1280 sq / 1–1.5 MP | baked |
| **Retrordinary v1.0** `retrordinary_v10.safetensors` | **`dpmpp_2m`** (best) | Karras | 3–8 | **25–50** | 1216×832–832×1216 or 1024² | baked |
| **Amanesse Works v2.0** `amanesseWorks_v20.safetensors` | `dpmpp_2m` / `euler_ancestral` | Karras | 3–5 | 20–30 | 1216×832–832×1216 or 1024² | XL_VAE_C |
| **Plant Milk Hemp II** `plantMilkModelSuite_hempII.safetensors` | **`euler`** / **`euler_ancestral`** | — | **~3** | **~28** | 1024+ | baked |

## Model-by-model notes (from official Civitai pages)

### Diving-Illustrious Anime — Niji-Muted Color vol2
Model id 1170176, version 2939886 (`nijiMutedColor_vol2+VAE`), creator DivingSuit.
> "Incorporates elements of Japanese illustration."
- Sampler: **Euler a** / Restart / DPM++ 2M / DPM++ SDE · Scheduler: **Karras**
- Size: **896 × 1152** · Steps **20–30** · CFG **4–6**
- ADetailer: `face_yolov8s.pt` (Impact-Pack FaceDetailer)
- Recommended negative:
  `(worst quality, low quality, normal quality, caucasian:1), lowres, bad anatomy, bad hands, signature, watermarks, ugly, imperfect eyes, unnatural face, unnatural body, error, extra limb, missing limbs, child, muscular, chinese, colored skin`
- NSFW OK; **sales prohibited** (personal use only).

### Hyphoria v0.02
Model id 1595884, creator hdparm.
> "Less is more, I often don't even use quality tags outside of worst quality in the negatives."
- Steps **20–35** · CFG **3** (2.5–6) · Sampler **Euler a** or **DPM++ 2M**
- Scheduler: stable on most (Karras fine)
- Resolution **1 MP – 1.5 MP**; portrait aspects more stable than ultra-wide wide
- Prompt lean & focused — it listens hard to tags. Skip heavy quality tag stacking.
  Minimal pos: `masterpiece, best quality, absurdres` · neg: `worst quality, low quality`
- v0.02: better contrast (fixes v0.01 washout on img2img/hires), better 1.5MP stability → great hires pass source.
- ⚠️ ultra-wide/high-res wide aspects can duplicate/warp anatomy.

### Retrordinary v1.0
Model id 2765743, creator Amanesse. Retro/nostalgic specialist.
- Sampler **DPM++ 2M** (works best) · Euler a OK · **min 20 steps, sweet spot 25–50**
- Scheduler **Karras** · Res 1216×832–832×1216 or 1024² · CFG **3–8** · VAE baked
- Retro style tags (no LoRA needed): `1990s_style`, `1980s_(style)`, `1980s city pop style`,
  `1970s (style)`, `(80s anime style vintage)`, `vhs aesthetic`, `scanlines`, `cinematic grain`,
  `retro art`, `g-taste style`, `(houjou raita)`, `kadoi aya style`, `(hyde tabakko style)`.
- Example:
  `1990s (style), (anime coloring, anime screencap, official art:1), chainsword_man, masterpiece, best quality, ultra-detailed, 1girl, 1990s anime style, vhs aesthetic, tracking noise, distorted frame, color transfer, scanlines, retro fashion, nostalgic mood, analog glitch, cinematic grain`
- **ADetailer:** prefer **segment** face models (e.g. Anime Girl Face Segmentation/manhole) over square-detection ones — square masks stand out on dark scenes.
- Img2img upscaling can be finnicky — lower denoise for hires.

### Amanesse Works v2.0
Model id 1965943, creator Amanesse. Flat/artistic merge.
> "More flat focused but somewhat artistic... capable of light 2.5D."
- Merges: Amanatsu + Aüngir + Duchesse + Pony NoobAI · **VAE: XL_VAE_C** (SDXL VAE)
- Sampler **DPM++ 2M** / **Euler a** · Scheduler **Karras**
- Res 1216×832–832×1216 or 1024² · Steps **20–30** · CFG **3–5**

### Plant Milk Model Suite — Hemp II
Model id 1162518, version 1714314 (Hemp II, series ldbr). Author recommends per-version sampler.
- **Hemp II:** Sampler **Euler** / **Euler a** recommended · CFG **~3** (3–6) · Steps **~28**
- Start point: *"Euler, 3 cfg, 28 steps is a good starting point for most versions."*
- Alt profile: Euler a + CFG++ sampler, SGM Uniform scheduler, ~2 cfg, ~28 steps
- Hires fix optional (example images use on/off)
- ⚠️ May output NSFW unintentionally — put `nsfw` in **negative** for SFW.
- **License:** derivatives cannot be used commercially (no generative services, SeaArt, PixAI, commissioned models, etc.).

## Default negative prompt (all models)
The Diving negative is a safe universal base for Illustrious:
```
(worst quality, low quality, normal quality, caucasian:1), lowres, bad anatomy, bad hands, signature, watermarks, ugly, imperfect eyes, unnatural face, unnatural body, error, extra limb, missing limbs, child, muscular, chinese, colored skin
```
For SFW add `nsfw, explicit, nude` (esp. Plant Milk).
