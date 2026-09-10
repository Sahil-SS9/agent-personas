---
name: comfyui-creative-suite
description: "Run ComfyUI workflows; orchestrates the suite."
version: 1.0.0
license: MIT
---
# ComfyUI Creative Suite — Orchestration Skill

This is the **umbrella / entry-point skill** for driving the local ComfyUI
creative stack on this machine. It tells Hermes **what to do when the user asks
to create, run, or build ComfyUI content** — which workflow to reach for, what
model/package each one uses, what's safe to tweak, and how to deliver output.
It is the "how to operate the suite" layer.

**Model map lives elsewhere** (kept DRY):
- `comfyui-mcp-models` — the exhaustive catalog of every model/LoRA/VAE/embedding/
  upscaler/detector/wildcard/workflow **and its exact on-disk path**. Load it too.
- `comfyui-provisioning` — installing/acquiring assets, MCP wiring, workflow inspection.
- `comfyui` — low-level CLI/REST execution scripts.
- `civitai` — downloading models.

THIS skill decides **what to run and how**, and drives the MCP tools to do it.

**Live-install note (2026-08-27):** the saved Basic_V37 and vsLinx all-in-one exports currently contain stale widget/class/model values and fail live validation. The MiniMax H3 all-in-one export passes. For new agent-driven image work, prefer a clean standard-node API graph and validate against the live server before running.

---

## When to Use
- User says: "create an image", "generate X", "run this workflow", "make a character",
  "let's set up a workflow", "use the all-in-one", "use basic v37", "which workflow should I use".
- User names a saved workflow, a model, a LoRA, a style, or a character and wants a render.
- User asks to build/edit/troubleshoot a ComfyUI workflow and execute it.

## Decision Tree — pick the right workflow FIRST

| User wants | Workflow | Why |
|---|---|---|
| Fast clean **anime/2.5D character** image, balanced quality | **Basic_V37** | Lean (76 nodes), fast, quality prompt pipeline, 1.5× upscale. Default for most requests. |
| **Heaviest detail / body-refinement** pipeline (multi-part ADetailer: face/eyes/hands/nsfw detail) | **All-in-One TXT2IMG** (vsLinx v5.1) | 8-stage detailer chain + refiner; slowest but most control. |
| **IMG2IMG / edit an existing image** | **All-in-One IMG2IMG** (vsLinx v5.1) | Same suite, inpaint/refine from a source image. |
| **Video** (MiniMax H3) | `minimaxH3AllInOne_v10` or `MiniMaxH3_Turbo` | text/models differ (see §4). |
| **Anything with a pose/imgs ref composition** | All-in-One TXT2IMG (+ CN/IPAdapter if models present) | Subsystems dormant — only if models exist. |
| Wants to **build from scratch** | see §5 (Create a New Workflow) | — |

**Default, when the user doesn't specify:** run **Basic_V37**. It's the fast,
correct, quality-default path. Only escalate to the All-in-One for heavy detail work.

---

## 1. Anchor Workflow Guide — Basic_V37 (default daily driver)

**File:** `user\default\workflows\Basic_V37.json` (76 nodes, 141 links)

**What it is:** Legendaer-style **NoobAI Mega — Basic tier**. A clean
txt2img → ADetailer → Hi-Res pipeline for anime/2.5D character shots.

**Stack (verified):**
- **Base model:** the checkpoint saved in the workflow; the live install currently exposes `JANKUTrainedChenkinNoobai_v777.safetensors`, `amanesseWorks_v20.safetensors`, `animayhemPaleRider_v40LongRider.safetensors`, and `divingIllustrious_nijimutedcolorVol2.safetensors` (`models\checkpoints\`)
- **VAE:** `sdxl_vae.safetensors`
- **Resolution:** 1024×1024 (latent via `EmptyLatentImage` 512→upscaled) · batch 1
- **KSampler:** steps **20**, CFG **8**, `euler_ancestral` / `normal`, denoise 1.0, seed randomize
- **CLIP:** stop_at_clip_layer **−2**
- **Sampling:** `ModelSamplingDiscrete` v_prediction + ZSNR on, `Epsilon Scaling` 1.005
- **LoRA stack (base):** `AddMicroDetails_Illustrious_v6` + `NOOB_EPSv1_1_detailer_by_vlnvk_v1_0` + `Cabyss - Medium` + `Matte_Skin_Illustrious_v4`
- **ADetailer chain (via Impact DetailerPipe):**
  - Hands — `UltralyticsDetectorProvider bbox/hand_yolov9c.pt`
  - Face — `segm/Anzhc Face seg 640 v3 y11n.pt` + SAM
  - Eyes — `segm/Anzhc Eyes -seg-hd.pt`
  - Breasts — `segm/Anzhc Breasts Seg v1 1024s.pt`
- **Prompts:** `ImpactWildcardProcessor` — quality embedded + wildcards. Positive uses `embedding:lazypos`, negative `embedding:lazyneg/lazyhand/lazywet`.

### How Hermes should run Basic_V37
1. If the user gives a character/scene prompt, **inject it into node 3** (`ImpactWildcardProcessor` positive `wildcard_text`) — it already tacks on quality+embeddings. Keep/rotate the `__whis-*` outfit wildcard only if the user wants.
2. Keep `embedding:lazyneg ...` negative as-is unless user specifies.
3. Leave KSampler seed auto (or set one for reproducibility the user asks).
4. Run via MCP `run_workflow`; poll `job`; output lands in `output\ComfyUI/ComfyUI_Upscaled_*.png`.

---

## 2. Anchor Workflow Guide — All-in-One TXT2IMG (vsLinx v5.1)

**File:** `user\default\workflows\allInOneDetailerAdetailerControlnet_v51TXT2IMG\TXT2IMG-ADetailer-v5.1-vslinx.json` (215 nodes, 418 links)

**What it is:** vsLinx **all-in-one** — the heaviest pipeline. 8-stage body
ADetailer chain + 2-stage refiner. Most control, slowest.

**Stack (verified):**
- **Base model:** `retrordinary_v10.safetensors` (`models\checkpoints\`)
- **Refiner:** `divingIllustrious_nijimutedcolorVol2.safetensors` (steps spent on base = 20)
- **VAE:** `sdxl_vae.safetensors`
- **LoRA stack (base):** `AddMicroDetails_Illustrious_v6` (str 1.3) + `NOOB_EPSv1_1_detailer` (0.65) + `Matte_Skin_Illustrious_v4` (0.65)
- **Per-part LoRAs:** Face/Eyes → `Eyes_for_Illustrious...`; Lips → `NOOB_EPS...`; Hands → `detailed hand focus...` + `stiletto_nails`
- **8 detailers:** Face, Eyes, Lips, Nose, Hands, Nipples, Vagina, Penis (several bypassed by default — Face/Eyes/Hands/Vagina active)
- **ADetailer detectors:** `segm/Anzhc Face`, `segm/Anzhc Eyes -seg-hd`, `bbox/hand_yolov9c`, `segm/ntd11_anime_nsfw_segm_v4_pussy`, etc.
- **Samplers:** main `euler_ancestral`/`sgm_uniform`; secondary `dpmpp_2m`/`karras` (off unless toggled)
- **Upscale:** `4xOpscaler_mixed.pth` @ 1.5×, Hi-Res denoise 0.36
- **Prompts:** `vsLinx_ImpactMultilineWildcardText` — quality + embeddings (`lazypos/lazynsfw/...`)

### Dormant subsystems (do NOT claim they're active)
- **ControlNet:** OFF (no model in `models\controlnet\`; loader null)
- **IP-Adapter:** Style/Composition bypassed
- **Pose/preprocessor:** bypassed

### How Hermes should run the All-in-One
1. This is for **heavy body-detail work**. Inject the character prompt into the
   **positive `PrimitiveStringMultiline` / `ImpactMultilineWildcardText`** node.
2. Optionally toggle individual body-part detailers via their `bypass` booleans
   (`Face bypass`, `Eyes bypass`, etc.) — all `False` by default (running).
3. Watch VRAM: 1024² base + 1.5× upscale + 8 detailers on 12 GB is heavy; may need
   batch=1 (it's already set to 4 at node 142 — **lower to 1 if OOM**).
4. Run via `run_workflow`; poll; output `output\TXT2IMG_ADetailer_<time>.png`.

---

## 3. How to RUN anything (the universal MCP recipe)

The user wants an image → use the MCP tools (they carry workspace + COMFY_BIN):

```
1. validate_workflow "<abs path to workflow json>"     # pre-flight, catches miss
2. run_workflow "<abs path>"                            # submit
3. job <id>  (poll until complete)                      # wait
4. fetch_outputs <id> "<dest dir>"                      # grab files
5. Deliver image via MEDIA:<path>                       # show the user
```

- **Absolute path** to the workflow file (workspace root prefixed): e.g.
  `C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\ComfyUI\user\default\workflows\Basic_V37.json`.
- For **parameter injection** (prompt/seed/model/LoRA), edit the workflow JSON's
  relevant `widgets_values` **before** submitting, or use the CLI. Never use
  `set_workflow_slot` on dynamic-combo nodes (UltimateSDUpscale/FaceDetailerPipe/DetailerForEach).
- **Model names must be exact** (case + extension) and match the `comfyui-mcp-models` map.
- If a tool isn't available as an MCP tool, use the CLI from the venv:
  `source /c/Users/Hermes/hermes-mcp/comfy-mcp-env/Scripts/activate && comfy --workspace "C:/Users/Hermes/ComfyUI/ComfyUI_windows_portable/ComfyUI" <cmd>`.

---

## 4. Model families — how to route by what the user asks

Load `comfyui-mcp-models` for the full catalog + exact paths. Quick routing:

| User wants | Reach for |
|---|---|
| Anime/2.5D character, Illustrious/NoobAI look | `models\checkpoints\` (hyphoria, retrordinary, divingIllustrious...) + `models\loras\` (Illu) + embeddings `lazy*` |
| Detail/skin refinement | Detail LoRAs: `AddMicroDetails`, `NOOB_EPSv1_1_detailer`, `Matte_Skin` |
| Facial feature emphasis | ADetailer detectors `segm\Anzhc*` + LoRAs `Eyes_for_*`, `detailed hand focus*` |
| Body/NSFW specifics | `segm\ntd11_anime_nsfw_segm_v4_*` detectors + per-part LoRAs |
| Upscale / Hi-Res final | `models\upscale_models\` (4xOpscaler, 4xNMKD, 4xUltrasharp) |
| Video (H3) | `models\diffusion_models\` + `models\text_encoders\qwen3vl...` + `models\vae\minimax_h3_video_vae` |
| Auto-prompting (LLM) | `models\LLM\Qwen3.5-9B-Q8_0.gguf` + mmproj |

---

## 5. Creating a NEW workflow (the right way)

When the user wants a brand-new/edited workflow:

1. **Decide the architecture** from the model map: base model family →
   checkpoint/diffusion model, VAE, text encoder, any LoRAs, output size.
2. **Prefer a template** first: `search_templates` / `run_template` (built-in
   gallery) — fastest starting point. Otherwise draft from the closest existing
   workflow (Basic_V37 for anime, All-in-One for detail) and modify.
3. **Build the graph** in API format (`class_type` per node). Assemble:
   Loaders → CLIP/VAE encode → (LoRA/CN) → EmptyLatent → KSampler → VAE Decode → SaveImage.
   For SDXL/Illustrious: add `ModelSamplingDiscrete` (v_prediction+ZSNR) + `Epsilon Scaling`.
4. **Wire models by exact name** from the catalog; keep every filename exact incl. extension.
5. **Pre-flight** `validate_workflow` (catches missing nodes/models) before running.
6. **Save** under `user\default\workflows\<name>.json` and register via
   `comfy workflow save` if needed.
7. If it's a new reusable recipe, offer to save it as a skill or update this one's guides.

---

## 6. Pitfalls (specific to orchestrating this suite)

1. **Never claim a subsystem works from defaults** — ControlNet/IP-Adapter in the
   All-in-One may be dormant even though the live install now has compatible
   ControlNet/IPAdapter assets. Verify the loader value and active link before
   promising a feature.
2. **Name everything exactly** — a wrong-extension or wrong-case model name
   silently fails or loads the wrong thing. Check against the catalog.
3. **Do not trust "what workflow is running" from a browser tab** — ask the user;
   the tab may be stale. The two you keep set up: Basic_V37 (daily) and All-in-One TXT2IMG.
4. **VRAM ceiling (12 GB):** the All-in-One at batch 4 + 8 detailers + 1.5× upscale
   can OOM. Drop batch to 1 for the Big pipeline. Basic_V37 at 1024² is comfortable.
5. **When in doubt, default to Basic_V37** and upgrade to the All-in-One only when
   the request needs heavy body-part refinement.
6. Load `comfyui-mcp-models` alongside this skill whenever you actually execute.

---

## 7. Verification checklist (before reporting "done")
- [ ] Chose the right workflow (Basic_V37 by default; All-in-One for heavy detail).
- [ ] Prompt/model swapped to what the user asked (exact names from catalog).
- [ ] `validate_workflow` passed.
- [ ] `run_workflow` submitted, `job` completed, output file **physically exists**.
- [ ] Delivered the image to the user with its real path (`MEDIA:<path>`).
- [ ] When in doubt about a model path/name, listed the folder first (native
      `search_files (target='files')` or the catalog) before acting.
