---
name: comfyui-mcp-models
description: "Drive local ComfyUI via comfy-mcp; find model paths."
version: 1.1.0
license: MIT
---
# ComfyUI MCP + Model Location Reference

## When to Use
- User says "comfy", "run a workflow", "generate an image", "which model/LoRA/VAE do I have", "where is X stored", or asks to swap/use a specific model, LoRA, embedding, upscaler, or detector.
- You need to drive the local ComfyUI install (run/submit/poll a workflow) via MCP or CLI.
- You need the exact on-disk path or canonical dropdown name for any ComfyUI asset.
- You need to know what the running server, GPU, models, or saved workflows currently are.

Single source of truth for (a) driving the local ComfyUI install through the
`comfy-mcp` MCP server / `comfy-cli`, and (b) **where every model, LoRA, VAE,
embedding, detection model, upscaler, wildcard, and workflow physically lives**
on disk. Load this whenever you touch ComfyUI so you never guess a path or a
model name.

Companion skills: `comfyui` (generation/execution layer, REST scripts),
`comfyui-provisioning` (install/acquisition/inspection + MCP wiring), `civitai`
(Civitai downloads). THIS skill is the **map + control surface**.

---

## 1. The environment (Windows, portable, verified)

| Key | Value |
|---|---|
| **Workspace root** | `C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI` |
| **Server** | `http://127.0.0.1:8188` (running: RTX 4070 Ti 12 GB, ComfyUI v0.34.0) |
| **MCP server** | `comfy-mcp` (stdio) — tools prefixed `mcp__comfy_mcp__` |
| **MCP venv** | `C:\Users\Hermes\hermes-mcp\comfy-mcp-env\` (`comfy-mcp.exe`, `comfy.exe`) |
| **comfy-cli workspace** | inner `ComfyUI/` dir (contains `main.py`) — NOT the portable wrapper |
| **custom_nodes/** | 22 packs loaded (vslinx, rgthree, Impact, Easy-Use, mxToolkit, IPAdapter+, ControlNet-aux, UltimateSDUpscale, Image-Saver, Comfyroll, llama-cpp_vlm, MiniMaxH3, ...) |
| **ComfyUI core** | v0.34.0 installed; live `server_info`/`system_stats` are the source of truth for drift |

### Activation (in a shell / execute_code)
```bash
source /c/Users/Hermes/hermes-mcp/comfy-mcp-env/Scripts/activate
comfy --workspace "C:/Users/Hermes/ComfyUI/ComfyUI_windows_portable/ComfyUI" <cmd>
```
Prefer the **MCP tools** (`mcp__comfy_mcp__*`) — they already have the workspace
and `COMFY_BIN` wired; no activation needed. Use the CLI when you need a command
that isn't an MCP tool.

---

## 2. The MCP tool surface — the primary control panel

Drive everything through these. Grouped by job:

### Environment / health
- `server_info`, `system_stats`, `get_logs`, `which` — status, GPU, VRAM, versions, pack freshness.

### Execution — the core
- `run_workflow <workflow_path>` — submit a workflow to the live server (API or editor format via `workflow_path`). This is how you actually **generate**.
- `job <job_id>` — inspect/wait/watch/cancel a submitted job. **Always poll to completion.**
- `validate_workflow <workflow_path>` — pre-flight check before running (catches missing nodes/models).
- `fetch_outputs <job_id> <out_dir>` — download a finished job's files.
- `run_template <name> <params>` / `search_templates` / `get_template` — built-in gallery templates.
- `generate_image <prompt>` — the fast text-to-image on-ramp (no workflow file needed).
- `partner_generate` / `list_partner_models` / `partner_model_schema` — cloud partner models (Flux, Ideogram, DALL·E).

### Workflow authoring / inspection
- `list_workflow_notes`, `list_workflow_slots`, `set_workflow_slot`, `vary_workflow`, `nodes`, `workflow_deps`, `list_prompts`, `get_prompt`, `emit_partner_workflow`.

### Models / transfer / node management
- `search_models`, `download_model`, `download`, `list_resources`, `read_resource`, `upload_file(piece)`, `install_node`, `update_comfyui`, `switch_comfyui_version`, `free_memory`, `launch_comfyui`/`stop_comfyui`/`restart_comfyui`, `auth_login`/`auth_status`.

### CLI-only commands (no MCP tool)
`comfy workflow list/get/save/delete`, `comfy models search/show/list-folders`,
`comfy node ls/search/upstream/downstream`, `comfy templates ls/fetch`, `comfy skills`,
`comfy jobs ls/status/wait`, `comfy preview`, `comfy assets push`, `comfy project`.
Full schema: call `mcp__comfy_mcp__discover` (returns the complete `command_schemas` map).

---

## 3. WORKSPACE ROOT — the one path that anchors everything

```
C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI
├── models\            ← ALL model files (see §4 map)
├── custom_nodes\      ← node packs (22 installed)
├── user\default\workflows\ ← saved workflows (.json)
├── user\default\      ← comfy.settings.json, comfyui.db
├── wildcards\         ← Impact-Pack wildcard cards (.txt / .yaml / dirs)
├── input\             ← images you load into workflows (LoadImage "example.png")
├── output\            ← generated images land here
├── user\comfyui.log   ← server log (also via get_logs)
└── main.py            ← workspace anchor (comfy-cli root)
```

**Input/output note:** `LoadImage` in a workflow references files in `input\` by bare
filename. Generated images save to `output\` (prefix-configured per workflow).

---

## 4. MODEL LOCATION MAP (full inventory, live-verified)

Every path is relative to the WORKSPACE ROOT above. Models load by **exact
filename incl. extension** in the node dropdowns.

### Checkpoints — `models\checkpoints\`
| File | Identity / use |
|---|---|
| `hyphoria_v002.safetensors` | **your current default** — NoobAI-XL/Illustrious base (used by Basic_V37) |
| `amanesseWorks_v20.safetensors` | Illustrious-family checkpoint |
| `divingIllustrious_nijimutedcolorVol2.safetensors` | Illustrious base (used as refiner in vsLinx v5.1) |
| `plantMilkModelSuite_hempII.safetensors` | plant-milk suite alt |
| `retrordinary_v10.safetensors` | Illustrious-family (base in vsLinx v5.1) |

### Diffusion models (UNet) — `models\diffusion_models\`
| File | Identity |
|---|---|
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | MiniMax H3 ref2va, int8-convrot quant |
| `minimax_h3_ref2va_pruned_fp8_scaled.safetensors` | MiniMax H3 ref2va, fp8 scaled quant (primary) |

### VAEs — `models\vae\`
| File | Identity |
|---|---|
| `sdxl_vae.safetensors` | standard SDXL VAE (use for NoobAI/Illustrious) |
| `minimax_h3_video_vae_fp16.safetensors` | **visual** VAE — use for H3 image/video decode |
| `minimax_h3_audio_vae_fp32.safetensors` | **audio** VAE — only for H3 audio, NOT image decode |

### Text encoders — `models\text_encoders\`
| File | Identity |
|---|---|
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | Qwen3-VL 32B quantized TE (MiniMax H3), type `lumina2` in CLIPLoader |

### LoRAs — `models\loras\` (flat + subfolders)
Style/character (NoobAI/Illustrious): `4_Winged_Angel-000011`, `69yottea_illu_v2`,
`AfricanQueen_Illu`, `BedouinDreams_Illu`, `Cabyss - Heavy/Light/Medium`,
`cryosistyle`, `DuskyDravidion_Illu`, `EveningElvan_illu`, `gothicneon`,
`illu-giant-sword`, `Male_Rover_-_ILL`, `MoriiMee_Gothic_Realistic`,
`New_Fantasy_CoreV5_-_ILL`, `To be hero X - Queen`, `onTopOfPoleConcept_illustrious01`.

Detail/skin/body: `AddMicroDetails_Illustrious_v6` (micro-detail), `NOOB_EPSv1_1_detailer_by_vlnvk_v1_0` (detailer), `Matte_Skin_Illustrious_v4` (skin), `Breasts_size_sliderIllustriousXL3`, `MuscleSlider_Illustrious2`, `male_type`, `Mechanism-Illustious`, `detailed hand focus style illustriousXL v1.1`, `illustrious_masterpieces_v3`.
Eyes/hair/accessory: `Eyes_for_Illustrious_Lora_Perfect_anime_eyes`, `KMS_hair-003_high-spiked_ponytail_IL`, `stiletto_nails`, `Improved Archery`.

MiniMax H3: `minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors` (Turbo LoRA for H3).

### Embeddings — `models\embeddings\` (referenced in prompts as `embedding:<name>`)
Quality/style: `lazypos`, `lazynsfw`, `lazyhand`, `lazyneg`, `lazywet`, `lazyloli`, `cr1sp`, `IllusP0s`, `IllusN3g`, `S0ft`, `F4st`, `raf1n33`, `Smooth_Quality`, `Smooth_Negative-neg`, `SmoothNegative_Hands-neg`.

### ControlNet — `models\controlnet\`
**Live inventory:** 4 ControlNet models are installed; verify exact names against the live `/models/controlnet` endpoint before wiring a graph. Workflows with a `ControlNetLoader` that have `control_net_name: null` will **not** apply ControlNet until a model is added here. vsLinx docs reference `noobaiXLControlnet_epsCanny` etc. — not present.

### Upscalers — `models\upscale_models\`
`4xOpscaler_mixed.pth`, `4xNMKDSuperscale_4xNMKDSuperscale.pth`, `4xUltrasharp_4xUltrasharpV10.pth`, `4x_NMKD-Siax_200k.pth`, `nmkdSiaxCX_200k.safetensors`, `remacri_original.safetensors`.

### ADetailer / detection (Ultralytics) — `models\ultralytics\`
`segm\` (image-seg): `Anzhc Face seg 640 v3 y11n.pt` (face), `Anzhc Eyes -seg-hd.pt` (eyes), `Anzhc Breasts Seg v1 1024s.pt`, `adetailer2dMouth_v10.pt`, `2DCockAndBallYolo8x.pt`, `ntd11_anime_nsfw_segm_v4_*` (all/nipples/penis/pussy), `99coins_anime_girl_face_m_seg.pt`.
`bbox\`: `hand_yolov9c.pt` (hands). These are selected as the `model_name` in `UltralyticsDetectorProvider` (prefix path: `segm/...` or `bbox/...`).

### SAM — `models\sams\`
`sam_vit_b_01ec64.pth` — segmentation for FaceDetailer/Detailer masks.

### LLM (auto-prompting, llama-cpp_vlm) — `models\LLM\`
`Qwen3.5-9B-Q8_0.gguf` (+ `mmproj-Q8_0.gguf`) — local vision/LLM for prompt gen in H3/large workflows. Both must be present and appear in node dropdowns.

### Style models — `models\style_models\`
Empty (placeholder only). No T2I-Adapter style models.

### Inpaint / Latent upscale / Clip vision / Detection / Onnx / Classifiers
EMPTY (placeholders only).

### MiniMax H3 Latent Upscale — `models\latent_upscale_models\`
Empty. (H3 latent upscaler is a custom node pack, `ComfyUI-MiniMaxH3_LatentUpscaler`.)

---

## 5. Saved WORKFLOWS — `user\default\workflows\`

| File | What it is |
|---|---|
| `Basic_V37.json` | **Legendaer NoobAI Mega — Basic tier.** 76 nodes. Base `hyphoria_v002`, 1024², KSampler(20 steps, CFG 8, euler_ancestral/normal, denoise 1.0), CLIP −2, `ModelSamplingDiscrete` v-pred+ZSNR, Epsilon Scaling 1.005, 5-stage ADetailer chain (hands `bbox/hand_yolov9c`, face/eyes/breasts Anzhc seg + SAM), Hi-Res via `easy hiresFix` (4xUltrasharp/4xNMKD @50%) + `UltimateSDUpscale` 1.5× denoise 0.16. Wildcard-driven prompts (`lazypos/lazynsfw/lazyhand`). ControlNet loader present but **no model → CN dormant.** |
| `Standard_V37.json` | NoobAI Mega — Standard tier (116 KB). |
| `Advanced_V37.json` | NoobAI Mega — Advanced tier (249 KB). |
| `Advanced_Gemma_V37.json` | Advanced + local **Gemma** auto-prompt (334 KB). |
| `Advanced_QwenVL_V37.json` | Advanced + local **QwenVL** auto-prompt (331 KB). |
| `Detailer_V37.json` | Mega detailer-only (241 KB). |
| `allInOneDetailerAdetailerControlnet_v51TXT2IMG/TXT2IMG-ADetailer-v5.1-vslinx.json` | vsLinx all-in-one TXT2IMG: 215 nodes, 8-stage detailer, refiner `divingIllustrious`, ControlNet/IPAdapter subsystems (dormant by default). |
| `allInOneDetailerAdetailerControlnet_v51IMG2IMG/IMG2IMG-ADetailer-v5.1-vslinx.json` | vsLinx all-in-one IMG2IMG version. |
| `minimaxH3AllInOne_v10/MiniMax+H3+全能参考+自动提示词工作流.json` | MiniMax H3 all-in-one (CN + auto-prompt). |
| `MiniMaxH3_Turbo/drbaph_turbo_lora_ref.json` | H3 Turbo LoRA ref workflow. |
| `Hermes Text2Image 5.1.json` | earlier custom txt2img. |

**Inspection warnings:** `Advanced_Gemma_V37` / `Advanced_QwenVL_V37` / `Detailer_V37`
have `created` timestamps far earlier than `modified` — these are preserved save-times.
The vsLinx TXT2IMG and Basic_V37 are your two most actively-used builds.

---

## 6. WILDCARDS — `wildcards\` (referenced as `__name__` or `__dir/file__`)
41 files/dirs: camera angles, `casualSummerOutfits_v10/` & `casualWinterWear_v10/` (whis outfit YAMLs referenced as `__whis-statement-outfits/one_piece__`), **eventide_*** (full body-edit wildcard suite), `illustriousxl_magic`, `fujiWildcardsRandom_*`, and quality/pose cards. Needs Impact-Pack wildcard engine (installed).

---

## 7. LIGHTNING-FAST WORKFLOW: "user gives a want → you act"

1. **Read the intent.** Which model family? (NoobAI/Illustrious → the `checkpoints/` map; MiniMax H3 → `diffusion_models/` + `text_encoders/` + `vae/` video). Which workflow? (if not named, ask or use Basic_V37).
2. **Reference paths by category** from §4 — never guess the parent folder.
3. **Pre-flight** `validate_workflow <path>` (or `comfy validate`).
4. **Run** `run_workflow <path>` with parameter/prompt injection (seed, positive/negative prompt, model swap to one of the §4 files).
5. **Poll** the `job` until done; `fetch_outputs` to a target dir; deliver the image (`MEDIA:` path).

### Model-name accuracy rules
- Model filenames are **case-sensitive incl. extension** and match the node dropdown option exactly (`comfy models search "<name>"` to confirm any name).
- Embeddings → `embedding:<name>`; LoRAs → `models/loras/<file>` in the Power-LoRA/wildcard selector.
- Detectors need the subfolder prefix: `segm/Anzhc Face seg 640 v3 y11n.pt` (not just the filename).

---

## 8. PITFALLS (learned the hard way)

1. **Never assume "what workflow is running" from files or the browser.** The newest-saved JSON and a CDP/browser snapshot of the ComfyUI tab can BOTH be wrong (a stale/unsaved tab shows `*Unsaved Workflow`). If the user asks, ask them or cross-check `comfy workflow list --where local`. (Your active daily driver is usually **Basic_V37**.)
2. **`ControlNetLoader` with `control_net_name: null` = ControlNet silently OFF** — the live install currently has 4 ControlNet models, but a graph must select one explicitly. Verify the active workflow value before claiming CN is applying.
3. **Never write slots via `set_workflow_slot` on dynamic-combo nodes** (`UltimateSDUpscale`, `FaceDetailerPipe`, `DetailerForEach`). The MCP mis-pairs names onto values positionally → your write lands in the wrong field. Edit `widgets_values` in the workflow JSON directly.
4. **`minimax_h3_audio_vae_fp32` is the AUDIO VAE** — for image/video H3 decode use `minimax_h3_video_vae_fp16`. Wrong VAE = broken/blank decode.
5. **Checkpoints ≠ what's loaded.** `object_info` lists installed; the in-canvas `CheckpointLoader` picks one. Read the workflow's actual `ckpt_name`.
6. **Live core is v0.34.0** (comfy-cli 1.15.0; packs report current) — use `server_info`/`system_stats` as the source of truth and don't upgrade unprompted mid-session.
7. **Port:** server is currently on `:8188` with `--windows-standalone-build`; do not add `--disable-dynamic-vram` because it defeats lazy-mmap loading for large H3 assets and can trigger memory pressure. Restart is required to change launch flags.
8. **uv mangles POSIX paths** — if ever reinstalling MCP, use native `C:/...` paths (see comfyui-provisioning MCP wiring ref).
9. **`search_files (target='files')` missed workflow JSONs under `user/default/workflows/`** (subdirs) — use `find`/the terminal when inventorying; the GUI browser surfaces folder names under user data.

---

## 9. VERIFY AFTER ANY CHANGE
```bash
# server + GPU
curl -s http://127.0.0.1:8188/system_stats | head -c 300
```
```python
# a model is where you expect
from hermes_tools import search_files
search_files(target="files", pattern="*.safetensors", path="C:/Users/Hermes/ComfyUI/ComfyUI_windows_portable/ComfyUI/models/<category>")
```
```bash
# confirm name canonically
source /c/Users/Hermes/hermes-mcp/comfy-mcp-env/Scripts/activate
comfy --workspace "C:/Users/Hermes/ComfyUI/ComfyUI_windows_portable/ComfyUI" models search "<name>"
```

When in doubt about a model path or name, **list the folder first** (native
`search_files (target='files')` or `comfy models list-folder --where local
<category>`), never write to disk blind. Report to the user with actual file
paths and confirm outputs landed before declaring success.
