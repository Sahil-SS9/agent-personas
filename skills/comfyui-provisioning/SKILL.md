---
name: comfyui-provisioning
description: "Install ComfyUI locally; acquire Civitai/HF models & nodes."
version: 1.0.0
license: MIT
---
# ComfyUI Provisioning — Local Deployment & Model/Node Acquisition

Companion to the `comfyui` skill (generation/execution layer). THIS skill owns
getting ComfyUI standing on a local machine and getting models/nodes/workflows
into the right folders — the deployment + acquisition layer.

## When to use
- Installing, updating, or launching ComfyUI locally (Windows portable build)
- Downloading Civitai models/LoRAs/embeddings/workflows/wildcards at scale
- Installing custom node packs from GitHub
- Turning a user's list of Civitai links into a resolved download manifest

## Hardware pre-check (30s)
`nvidia-smi` (VRAM), `df -h /c` (disk), RAM. 12 GB VRAM runs SDXL, Flux-fp8,
Wan 2.2 5B, and MiniMax H3 pruned quants. Budget ~100 GB disk for a
video-capable install (portable 4.4 GB + models).

## Windows portable install
1. **7-Zip required** (archive is .7z): `winget install 7zip.7zip`

### ComfyUI-Manager registry migration
The modern Manager is a **Manager database/package-registry migration**, not automatically a ComfyUI-core upgrade. Before changing it:

1. Check the live Manager clone and current config: `git -C custom_nodes/ComfyUI-Manager status --short --branch`; inspect `user/__manager/config.ini`.
2. Make a rollback copy of `custom_nodes/ComfyUI-Manager` and `user/__manager` before editing.
3. Update the Manager clone with `git fetch origin main --prune` followed by `git pull --ff-only origin main`; do not overwrite local changes.
4. Select the newer registry database by setting `db_mode = new` in `user/__manager/config.ini`. Preserve security/network/install-policy settings unless there is a separate reason to change them.
5. Restart ComfyUI using the normal launcher or the embedded interpreter. Manager mode cannot be verified while the server is stopped.
6. Verify the live `/system_stats`, ComfyUI log, Manager UI, registry reachability, custom-node registration, and workflow validation. A successful git pull or config edit alone is not proof of a successful migration.
7. Keep the rollback path documented until the existing workflows and at least one representative render pass after restart.

The Manager migration does not migrate checkpoints, LoRAs, VAEs, or workflow compatibility automatically. Treat it as a dependency-management change and re-audit workflow node classes after restart. Session-specific rollback and verification details are in `references/manager-registry-migration.md`.
2. Download: `https://github.com/Comfy-Org/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z`
   (CUDA 13 / Py 3.13 for RTX cards; `_cu126` variant for 10-series and older). ~2.1 GB.
3. Extract with **native Windows paths** — `7z.exe` fails on MSYS paths:
   `"/c/Program Files/7-Zip/7z.exe" x "C:\dest\archive.7z" -o"C:\dest" -y`
4. Launch: `run_nvidia_gpu.bat` only works in a real console (it ends in `pause`).
   From agent/background shells launch python directly from the portable root:
   `./python_embeded/python.exe -s ComfyUI/main.py --windows-standalone-build`
5. Verify: `curl http://127.0.0.1:8188/system_stats` → version, GPU, VRAM.
   (MiniMax H3 day-0 support needs ComfyUI ≥ 0.30.0.)
6. Updating: `update/update_comfyui_stable.bat` (console) or `git pull` inside `ComfyUI/`.

## Custom node packs
- Clone into `ComfyUI/custom_nodes/`, `--depth 1`; install **ComfyUI-Manager first** (ltdrdata/ComfyUI-Manager).
- Repos with submodules need `git clone --recursive` — e.g. ssitu/ComfyUI_UltimateSDUpscale (repositories/ultimate_sd_upscale); missing submodule = broken nodes.
- Deps ONLY with the embedded Python, never system Python:
  `python_embeded\python.exe -m pip install -r custom_nodes\<repo>\requirements.txt`
- comfyui_controlnet_aux auto-downloads annotator weights on first use (`models\annotators`, grows 1–3 GB).
- Restart server after installs; `class_type not found` at workflow load = missing pack.
- Some authors prescribe a specific clone dir name (e.g. vslinx → lowercase `comfyui-vslinx-nodes`) — check the repo README.
- Auto-prompt/LLM nodes in H3-style workflows: the pack is **lihaoyun6/ComfyUI-llama-cpp_vlm** (nodes `llama_cpp_model_loader`, `llama_cpp_instruct_adv`). Its requirements.txt pins platform-specific llama-cpp-python wheels — installs clean on Windows portable Py3.13.

## Workflow readiness audit (before telling a user "it's ready")
Never answer "are the workflows ready?" from memory — audit every workflow JSON
against the live registry: `scripts/audit_workflow_nodes.py <dir-or-file>`
(handles API + editor formats, categorizes noise vs real gaps). Rules encoded:
- UUID-typed nodes = frontend GROUP NODE instances (resolve at load) — noise.
- `Reroute` / `MarkdownNote` / `PrimitiveNode` = frontend/core, absent from
  object_info — noise. (MarkdownNote only exists on newer ComfyUI.)
- Display-name keys like `Label (rgthree)`, `Fast Bypasser (rgthree)` — some
  packs register display-style class_type keys; if the pack is installed they
  load fine in the UI — cosmetic, not blockers (verified: generation ran).
- Anything else missing = real gap → install the providing pack, restart, re-audit.

### Delivering workflows the user can't find
Workflows in `user_data/workflows/<folder>/` don't always surface in the in-UI
browser for freshly created folders. Foolproof handoff: copy the .json files to
the user's Desktop and have them drag-and-drop onto the canvas (or Workflow →
Open). In-UI path otherwise: Browse → folder names under user_data.

## Civitai acquisition
Base `https://civitai.com/api/v1`, auth header `Authorization: Bearer <key>`.
civitai.red and civitai.com are the same backend. Full endpoint notes, quirks,
and the collection workarounds: `references/civitai-api.md`. Headlines:

- Identity: `GET /me` (there is NO `/user` — it 404s).
- Resolve a link: `GET /models/{id}` → pick `modelVersions[].id` → `GET /model-versions/{vid}` → `files[]` with `downloadUrl`. If the user's URL already carries `?modelVersionId=NNNN`, skip straight to `GET /model-versions/NNNN` — that's the whole resolution in one call.
- **Collections API can never list a user's own/private collections nor ANY collection's items** — don't burn calls probing; ask the user for model links (or scrape `__NEXT_DATA__` from the rendered page).
- Downloads: append `&token=<key>` to `downloadUrl`; resumable: `curl -L -f --retry 5 -C - -o out url`.
- Newly-public collections sit behind a "Pending review" moderation gate for non-owners — retry later, not an auth failure.

### Civitai type → ComfyUI folder
| Civitai type | Destination |
|---|---|
| Checkpoint, CheckpointMerge | `models\checkpoints` |
| LORA, LoCon, DoRA | `models\loras` (DoRA loads fine in LoRA loaders) |
| TextualInversion | `models\embeddings` |
| Upscaler (ESRGAN) | `models\upscale_models` — **rename `.pt` → `.pth`** (Civitai ships PickleTensor; loaders only list `.pth`) |
| Detection (ADetailer) | `models\ultralytics` (bbox/seg subfolders) |
| Workflows | `user_data\workflows` (unzip) |
| Wildcards | `wildcards` (unzip `wildpack_*.zip` → contains .txt cards; needs Impact-Pack wildcard engine) |
| Other — autocomplete tag lists (Danbooru/e621/Gelbooru) | NOT a models folder → `user\default\comfyui_custom_scripts\assets\` for ComfyUI-Custom-Scripts (pyssss) tagcomplete |
| LLM GGUFs (auto-prompting in H3 workflows) | `models\LLM` (folder scanned by ComfyUI-llama-cpp_vlm; GGUF + its mmproj must both be present and appear in the node dropdowns) |

### Manifest pattern (proven, 40+ links across multi-type batches → 0 failures)
Resolve every link via the API into `manifest.json`
(`{model_id, version_id, name, type, files[{file, size_mb, url}], dest}`),
then run `scripts/download_civitai.py` — resumable, skips existing files,
auto-extracts workflow zips alongside the archive. For mixed-type batches
(LoRAs + upscalers + wildcards + zips) route by the resolved `type` field per
the table above, apply post-download fixes (`.pt`→`.pth` rename, wildcard
unzip), then run the inventory sweep in `references/verification-and-smoke-test.md`
§6 and report a per-folder file/size table.

## Hugging Face video models
Same resumable curl pattern via `scripts/download_hf.py` (repo + hf-path →
local-subfolder pairs). MiniMax H3 file map, 12 GB variant picks, the
ref2va↔fl2va distinction, Turbo LoRA pruned-base compatibility (larryvrh original
vs drbaph conversion), the uncensored "Ultra Heretic" text encoder, and the
companion nodes/apps around it: `references/minimax-h3-files.md`.

For image-model acquisition, exact manifests and official workflow-template URLs for Krea 2 Turbo, Ideogram 4, and Qwen-Image-2512 are recorded in `references/image-model-acquisition.md`. Use the per-file resumable download and byte-count verification procedure there; keep each large download in its own background process on Windows/MSYS.

### Agent-side workflow INSPECTION (what's loaded, reviewing a saved graph)
When a user asks "what workflow am I running?" there is **no reliable server-side or
browser-tab answer** — ask them, cross-check `comfy workflow list --where local`, and never
trust the newest-saved file or a CDP browser snapshot (both were wrong guesses this session).
Full recipe for reviewing any saved workflow JSON end-to-end (node census, link tracing,
active/bypassed state, dormant-subsystem tells) and the `list_workflow_slots` positional
misalignment trap on dynamic-combo nodes (UltimateSDUpscale / FaceDetailerPipe — **never
write those via set-slot; edit the JSON directly**): `references/workflow-inspection.md`.

## Wiring ComfyUI to an agent (Comfy MCP)
To let an agent drive the local install it provisioned (run workflows, list live models/nodes,
generate), add the official `comfy-mcp` server. Two packages: `comfy-cli` (engine) + `comfy-mcp`
(MCP server). Install them into a **dedicated venv outside the agent's own venv** (e.g.
`~/hermes-mcp/comfy-mcp-env`) and reference by **absolute path + `COMFY_BIN` env** — that is what
survives an agent update. Full steps, config, registration workaround, tool surface, and gotchas:
`references/comfy-mcp-wiring.md`.
- **Inspection quirk:** `list_workflow_slots` pairs slot names onto values positionally; nodes
  with dynamic/partner combos (UltimateSDUpscale, FaceDetailerPipe, DetailerForEach) shift every
  later pairing, so their slot names/values show mispaired (`48.steps`→"randomize"). Read
  `widgets_values` from the JSON instead; do NOT set-slot those nodes — the write lands in the
  wrong field. See `references/workflow-inspection.md` §3.
- **Headless-execution footguns** — running mega-workflows via `comfy run` /
  `run_workflow` (not the UI) has three verified traps that waste GPU time:
  (1) the vsLinx All-in-One's interactive `Image Filter` node times out at 90s
  and kills headless runs (`Processing interrupted` ~90-140s in, no output);
  (2) `easy hiresFix.rescale_after_model` is an unresolvable comfy-cli
  client-vs-server type conflict (blocks Basic_V37) -- bypass the hiresFix nodes;
  (3) rgthree display-name `class_type` nodes (Label, Fast Groups Bypasser, ...)
  are accepted by the UI but `comfy run` rejects. The reliable path for agent
  renders is a clean standard-node API txt2img graph (7 nodes); for a specific
  mega-workflow, extract the exact API graph from server history. Full
  diagnosis, fixes, and the proven template:
  `references/headless-execution-footguns.md`.

## Pitfalls
1. **"What workflow am I running?" is NOT answerable from files or the browser.** The
   newest-saved JSON in `user/default/workflows/` and a CDP snapshot of the ComfyUI tab can
   both be wrong (a stale/unsaved tab shows `*Unsaved Workflow`). Ask the user; cross-check
   `comfy workflow list --where local`. Installed checkpoints (`object_info`) ≠ loaded.
   Recipe: `references/workflow-inspection.md` §1.
1b. **Never write slots on dynamic-combo nodes via set-slot / set_workflow_slot.**
   `list_workflow_slots` pairs names positionally and under-reports UltimateSDUpscale /
   FaceDetailerPipe / DetailerForEach, misaligning every later field — the write lands in
   the wrong slot. Edit `widgets_values` in the JSON directly. See `references/workflow-inspection.md` §3.
1c. **UUID-typed node names = frontend GROUP NODE instances** (also `Reroute`,
   `MarkdownNote`, `PrimitiveNode`) — resolve at load, NOT missing packs. Don't report them
   as gaps during workflow audits. (See `scripts/audit_workflow_nodes.py`.)
1d. `7z.exe` + MSYS paths (`/c/...`) = "system cannot find the path" → always pass `C:\...`.
1b. **uv on Windows mangles POSIX paths** (creates a bogus `C:\c\...` venv) → always pass native
   `C:/...` paths to `uv venv`/`uv pip`.
1c. **comfy-cli `set-default` rejects the portable wrapper dir** — workspace root is the inner
   `ComfyUI` folder containing `main.py`.
1d. **`hermes mcp add` can connect+report success yet silently fail to persist** the config entry;
   when `hermes mcp list` shows nothing new, write it via `hermes config set mcp_servers.<name>.<key>`
   instead (agent tools cannot `patch` config.yaml directly).
2. Portable `.bat` launchers exit instantly under agent/background shells (`pause` at the end) → invoke `python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build` directly.
3. Civitai private collections are API-invisible **by design** (docs say so). Stop probing `/collections` with user filters — they're ignored; get direct model URLs.
4. `LoCon` is a real Civitai type missing from naive mapping tables → route to `models\loras` (loads fine).
5. Embeddings are referenced in prompts as `embedding:<name>`.
6. Never `pip install` node deps with system Python — it must be the portable env or imports break at load.
7. Community workflow JSON executes arbitrary Python — stick to reputable/high-star repos.
8. Large model downloads: run in background with `notify_on_complete`, verify bytes landing via `find -newer`/`ls`, keep `-C -` so interruptions resume.
9. **Writing downloads to MSYS `/tmp` can silently not persist** under git-bash — curl reports exit 0 and creates nothing (and `ls` then fails). Always write intermediate downloads to a **Windows-native path** (e.g. `C:\\Users\\<user>\\Downloads\\...` or the target model folder), not `/tmp`. Verify with `ls -la` + size after download.
10. **Mega-workflows fail headless differently than in the UI.** Interactive-gate and
    validator-strictness traps (`Image Filter` 90s timeout, `easy hiresFix`
    client/runtime type conflict, rgthree display-node class_type rejection) make
    `comfy run` abort what the UI runs. When a headless job returns `cancelled`
    ~90-140s in with no output, check the log for `Processing interrupted`, then
    bypass the gate / build a clean standard-node graph (template in
    `references/headless-execution-footguns.md`).
