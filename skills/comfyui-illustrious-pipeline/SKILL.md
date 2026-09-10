---
name: comfyui-illustrious-pipeline
description: "Use for text-to-image on Illustrious models with local ComfyUI."
version: 1.0.0
license: MIT
---
# ComfyUI Illustrious Text-to-Image Pipeline

Drive text-to-image generation on your **local ComfyUI** against the installed
**Illustrious XL** checkpoints, with per-model prompting/settings from the
official Civitai notes. Builds on the bundled `comfyui` skill (this handles the
**Illustrious-specific workflow + model catalog**; `comfyui` handles install/launch/troubleshooting).

## Environment (this machine)

- Server: `http://127.0.0.1:8188` (ComfyUI 0.30.0 portable, running with `--disable-dynamic-vram`)
- Checkpoints: `C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI\models\checkpoints\`
- Skill scripts (run_workflow.py etc.):
  `C:\Users\Hermes\AppData\Local\hermes\profiles\creative\skills\creative\comfyui\scripts\`
- This skill's curated workflow: `workflows/illustrious_txt2img.json`
- Full model catalog + Civitai notes: `references/model-catalog.md`

**Prereqs:** ComfyUI server must be running (see `comfyui` skill / provisioning).
Check: `curl http://127.0.0.1:8188/system_stats`.

## The pipeline (one shot)

```bash
SCRIPTS="C:/Users/Hermes/AppData/Local/hermes/profiles/creative/skills/creative/comfyui/scripts"
WF="C:/Users/Hermes/AppData/Local/hermes/profiles/creative/skills/creative/comfyui-illustrious-pipeline/workflows/illustrious_txt2img.json"

python3 "$SCRIPTS/run_workflow.py" \
  --workflow "$WF" \
  --args '{
    "ckpt_name": "divingIllustrious_nijimutedcolorVol2.safetensors",
    "prompt": "masterpiece, best quality, absurdres, 1girl, [YOUR TAGS]",
    "negative_prompt": "(worst quality, low quality, normal quality, caucasian:1), lowres, bad anatomy, bad hands, signature, watermarks, ugly, imperfect eyes, unnatural face, unnatural body, error, extra limb, missing limbs, child, muscular, chinese, colored skin",
    "seed": -1,
    "steps": 28,
    "cfg": 4.0,
    "sampler_name": "euler_ancestral",
    "scheduler": "karras",
    "width": 896,
    "height": 1152
  }' \
  --output-dir "C:/Users/Hermes/outputs"
```

Outputs land in `--output-dir`; the script prints a JSON manifest of saved files.

### ⚠️ Valid param names (verified against run_workflow.py schema)

| Arg key | Maps to |
|---|---|
| `prompt` | positive CLIP text (node 6) |
| `negative_prompt` | negative CLIP text (node 7) — **NOT `negative`** |
| `ckpt_name` | checkpoint loader (node 4) |
| `seed` / `steps` / `cfg` / `sampler_name` / `scheduler` / `denoise` | KSampler (node 3) |
| `width` / `height` / `batch_size` | EmptyLatentImage (node 5) |
| `filename_prefix` | SaveImage (node 9) |

### ⚠️ ComfyUI sampler names (do NOT use A1111/Civitai names)

Civitai pages say "Euler a", "DPM++ 2M", etc. ComfyUI uses underscored names — map them:

| Civitai/UI name | ComfyUI `sampler_name` value |
|---|---|
| Euler a | `euler_ancestral` |
| Euler | `euler` |
| DPM++ 2M | `dpmpp_2m` |
| DPM++ 2M SDE | `dpmpp_2m_sde` |
| DPM++ SDE | `dpmpp_sde` |
| HeunPP2 | `heunpp2` |
| DPM++ 3M SDE | `dpmpp_3m_sde` |

Schedulers are identical: `karras`, `sgm_uniform`, `simple`, etc.
`Restart` sampler is NOT in KSampler's list on this build — use a DPM++/euler variant instead.

### ⚠️ DO NOT put a `_comment` / non-node key in workflow JSON

ComfyUI 0.30's `execution.validate_prompt` iterates every top-level key and
calls `.get('_meta', {})` on the value. A `"_comment": "..."` string at the top
level crashes **every submission** with `AttributeError: 'str' object has no
attribute 'get'` → HTTP 500. Keep the workflow file to only `"<node_id>"` keys.

## Model selection — `ckpt_name` values (exact)

| Model | ckpt_name |
|---|---|
| Diving Niji-Muted vol2 | `divingIllustrious_nijimutedcolorVol2.safetensors` |
| Hyphoria v0.02 | `hyphoria_v002.safetensors` |
| Retrordinary v1.0 | `retrordinary_v10.safetensors` |
| Amanesse Works v2.0 | `amanesseWorks_v20.safetensors` |
| Plant Milk Hemp II | `plantMilkModelSuite_hempII.safetensors` |

## Per-model settings (via --args)

Pick **sampler/scheduler/cfg/steps/res** from the matrix in
`references/model-catalog.md`. Quick lookup:

| Model | sampler | cfg | steps | res |
|---|---|---|---|---|
| Diving vol2 | `euler_ancestral` | 4–6 | 20–30 | 896×1152 |
| Hyphoria | `euler_ancestral`/`dpmpp_2m` | 3 | 20–35 | 1024–1280 |
| Retrordinary | `dpmpp_2m` | 3–8 | 25–50 | 832×1216 / 1024² |
| Amanesse | `dpmpp_2m`/`euler_ancestral` | 3–5 | 20–30 | 832×1216 / 1024² |
| Plant Milk Hemp II | `euler`/`euler_ancestral` | ~3 | ~28 | 1024+ |

## Workflow reference

`workflows/illustrious_txt2img.json` (API format, injectable params auto-detected):
- Node **4** = `CheckpointLoaderSimple` → `ckpt_name`
- Node **6** = positive CLIP encode → `prompt`
- Node **7** = negative CLIP encode → `negative`
- Node **3** = KSampler → `seed`, `steps`, `cfg`, `sampler_name`, `scheduler`, `denoise`
- Node **5** = EmptyLatentImage → `width`, `height`, `batch_size`
- Default envelope: `euler_ancestral`, `karras`, cfg 4, 28 steps, 896×1152 portrait
- VAE is baked into each checkpoint (node 4 outputs CONDTIONING/MODEL/VAE).

## Prompting conventions (Illustrious)

- **Danbooru-style tags** — comma-separated, lowercase tags; quality tags come first.
- **Positive quality tags:** `masterpiece, best quality, absurdres`.
- **Negative (universal base):** the Diving negative in `references/model-catalog.md`.
  Add `nsfw, explicit, nude` for SFW (esp. Plant Milk).
- **Lean beats verbose:** Hyphoria and Diving both warn that over-stacking quality
  tags makes results glossier but less flexible and less controlled. Keep the
  subject tags specific and intentional.
- **Aspect ratios:** portrait 832–896 × 1152 is the sweet spot for most; keep
  total pixels ~1–1.5 MP (≈ 896×1152 = 1.03 MP). Avoid ultra-wide on Hyphoria.

## Variants

- **Hires pass / img2img:** use the matching `sdxl_img2img.json` workflow in the
  `comfyui` skill (`--input-image image=./x.png`, lower `denoise` to ~0.4–0.55,
  esp. Retrordinary which is finnicky on img2img upscales).
- **Inpaint:** `comfyui` skill `sdxl_inpaint.json`.
- **Video:** `comfyui` skill `wan_video_t2v.json`.

## NOTES / Caveats

- **vslinx `vsLinx_UpscaleByFactorWithModel` node HARD-CRASHES the server** (access violation segfault, exit 139) during the upscale phase — observed in ComfyUI 0.30 + `--disable-dynamic-vram` while VRAM was constrained. It's a native crash (`Windows fatal exception: access violation` in `upscale_by_factor_with_model.py:39`), NOT catchable in Python. The vslinx all-in-one TXT2IMG/IMG2IMG workflows contain this node → avoid running the upscale-model branch on a 12 GB card when other models are loaded; using this skill's clean workflow (no upscale-model node) sidesteps it entirely.
- `--disable-dynamic-vram` is applied at THIS server launch only. If ComfyUI is
  relaunched without it, DynamicVRAM streaming re-engages — see troubleshooting.
- The big vslinx `allInOneDetailer…TXT2IMG/IMG2IMG` editor-format workflows in
  `user/default/workflows/` are **not scriptable** via run_workflow.py (215+
  nodes, editor format, sliders/wildcards) AND carry the crashy upscale node.
  Use them in the ComfyUI UI for manual ADetailer+ControlNet+IPAdapter work;
  for scripted T2I use this skill's clean API workflow.
- If a run errors: `curl http://127.0.0.1:8188/history?max_items=5` and see
  `comfyui-troubleshooting` skill (DynamicVRAM/`hostbuf` playbook especially).
- Checkpoint names are **case-sensitive and include the extension** — typos give
  `value not in list` errors; verify with `comfy model list` or the models dir.

## Verification

- [ ] Server up: `curl http://127.0.0.1:8188/system_stats`
- [ ] Model present in `models/checkpoints/` (exact filename)
- [ ] Workflow JSON exists at the skill path
- [ ] Test run with a small one completes and outputs land in `--output-dir`
