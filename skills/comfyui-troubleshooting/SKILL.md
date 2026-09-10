---
name: comfyui-troubleshooting
description: "Use when a ComfyUI run errors: diagnose via /history."
version: 1.0.0
license: MIT
---
# ComfyUI Troubleshooting

Diagnose ComfyUI jobs that fail at runtime (server up, job errors). Complements
the `comfyui` skill, which covers execution and dependency management: that skill
runs jobs; this one figures out why a job died.

## When to use
- User reports an error when running a workflow / image fails to generate.
- Need to identify which node/model failed and whether the cause is a missing
  file, corruption, or an environmental/transient issue.
- Authoring/maintaining `run_workflow.py` parameter injection or clean
  API-format workflows → see `references/run-workflow-params-and-names.md`
  (verified arg-key names, sampler-name mapping, `_comment` trap).

## Diagnostic sequence (do this first, in order)
1. **Server state:** `curl -s http://127.0.0.1:8188/system_stats` → note
   `comfyui_version`, `ram_free`, `vram_free`. Low free RAM (<~10 GB) plus
   multi-GB checkpoints = streaming-error risk.
2. **Last error:** `python3 scripts/last_error.py` → failing node, exception,
   traceback tail, submitted inputs. (Manual equivalent: GET
   `/history?max_items=5`, find `status.status_str == "error"`, read
   `messages[].execution_error`.)
3. **Classify** with the table below and follow that playbook.
4. **Discriminate transient vs persistent** before re-downloading anything:
   validate the file (`scripts/safetensors_check.py`) and smoke-test the model
   with a minimal workflow (CheckpointLoaderSimple → CLIPTextEncode →
   EmptyLatentImage → KSampler 4 steps → VAEDecode → SaveImage). If the smoke
   test succeeds, the file is fine and the original failure was
   environmental — retry.

## Error classification
| Signature (exception_message) | Meaning | Playbook |
|---|---|---|
| `hostbuf_file_reader_read failed` / `HostBuffer.read_file_slice failed` | DynamicVRAM file→pinned-RAM streaming read failed (ComfyUI ≥0.30, comfy-aimdo) | DynamicVRAM below |
| HTTP 500 on EVERY `/api/prompt` submission, log: `AttributeError: 'str' object has no attribute 'get'` at `execution.py validate_prompt` | Workflow JSON has a top-level non-node key (e.g. `"_comment": "..."`) | `_comment`/workflow-validation crash below |
| `Windows fatal exception: access violation`, exit code 139 mid-run | Native segfault in a custom node (not a catchable Python exception) — observed in vslinx `UpscaleByFactorWithModel` | vslinx/node crash below |
| `Windows fatal exception: access violation` in `torch/storage.py __getitem__` → `load_torch_file` → `load_clip`/`load_vae` | Native crash while READING a model file into RAM — legacy full-file load (aimdo off via `--disable-dynamic-vram`) while VAEs/LLM already resident; RAM exhaustion (32 GB box + 15 GB text encoder + ~10 GB fp32 VAE + ~10 GB LLM) | Legacy-loader/DynamicVRAM tradeoff below; file usually validates fine — loader strategy, not corruption |
| `class_type not found` / node missing | Custom node not installed | `comfyui` skill: auto_fix_deps.py |
| `value not in list` / missing required input | Model file absent or misnamed | Check model dir; `comfyui` skill check_deps.py |
| `CUDA out of memory` | VRAM exhausted | Lower res/batch; `POST /free`; `--lowvram`/`--novram` |
| llama_cpp / LLM nodes run entirely on CPU | CPU-only llama-cpp-python wheel in python_embeded — `n_gpu_layers`/`vram_limit` silently ignored | LLM/llama_cpp offload playbook below |

## `_comment` / non-node key in workflow JSON → every submission 500s
ComfyUI 0.30's `execution.validate_prompt` iterates **every** top-level key of the
prompt dict and, for any value lacking `class_type`, does `node_data.get('_meta', {}).get('title')`.
A `"_comment": "..."` string at the top level makes `node_data` a **str**, so
`.get()` raises `AttributeError: 'str' object has no attribute 'get'`. The
result: **every** `/api/prompt` submission returns HTTP 500 `Server got itself
in trouble`, regardless of content — because the workflow dict is malformed for
this validator.
- **Fix:** remove ALL top-level non-node keys from workflow JSON. The bundled
  `sdxl_txt2img.json` example ships with a `"_comment"` key that triggers this —
  strip it on this ComfyUI version. Keep the file to only `"<node_id>": {…}` entries.
- **Cause of the 500 gap:** the API returns a bare `500 Internal Server Error`
  with no body detail, so the first symptom in the log is
  `uncaught` `AttributeError` in `post_prompt` → `validate_prompt`. Grep the
  server log (`-> post_prompt`, `-> line NNN in validate_prompt`) rather than
  trusting the response body.
- Note: `extract_schema.py`/`_inline_schema` handles a `_comment` key fine, so a
  workflow can pass `run_workflow.py --schema` extraction yet still crash at
  submit — the schema path and the validation path diverge.

## Native access-violation crash in a custom node (vslinx upscale) — exit 139
vslinx `vsLinx_UpscaleByFactorWithModel` (`upscale_by_factor_with_model.py:39`,
`torch.clamp(s.movedim(-3, -1), ...)` after `tiled_scale` on an upscale model)
can throw a **hard `Windows fatal exception: access violation`** during the
upscale phase, segfaulting the whole Python/ComfyUI process (exit 139). It is a
native crash — NOT a catchable Python exception — so no `try/except` in the node
or in `run_workflow.py` survives it; the server just dies.
- **Trigger profile:** running an ESRGAN-class upscale model through
  `tiled_scale` while VRAM is constrained and other weights are resident (e.g.
  a 12 GB card with LoRA/checkpoint loaded).
- **Response:** check `process(log)` / `exit 139` + the traceback tail showing
  the custom node frame; restart ComfyUI; for scripted workflows, **prefer a
  workflow with no upscale-model node** (plain txt2img or a standard
  `common_upscale` resize) rather than the crashy node.
- **Correction (verified 2026-08):** the vslinx all-in-one TXT2IMG workflow IS
  headless-scriptable. Have the user export it via *Workflow → Export (API)*,
  then apply the two patches in "Running exported all-in-one workflows
  headless" below. The full 200+ node pipeline (base gen → LoRA stack →
  FaceDetailer chain → upscale + HiRes → Image Saver) ran clean end-to-end via
  `/prompt` on the RTX 4070 Ti in ~60 s. Editor format remains non-executable;
  the API export is the unlock.

## Running exported all-in-one workflows headless (vslinx / mxSlider stacks)

UI-built "all-in-one" workflows (vslinx ADetailer stacks, 200+ nodes, mxSlider
consoles) work via `/api/prompt` after a one-time *Workflow → Export (API)*,
with two runtime patches — the export preserves a few frontend-only nodes that
crash or fail validation headless:

1. **`WidgetToString` → `TypeError: 'NoneType' object is not subscriptable`.**
   It reads widget values from `extra_pnginfo` (browser canvas state), absent in
   API runs. Typically feeds Image Saver's `modelname`. Fix: set the consumer's
   input to a literal string (`d['259']['inputs']['modelname'] = '<ckpt name>'`)
   and delete the WidgetToString node. (Alternative: pass
   `extra_data.extra_pnginfo.workflow` = the editor JSON in the POST — untested
   here; the literal-string patch is proven.)
2. **Orphaned `PreviewImage`** (no `images` input) — flagged as
   `required_input_missing` in the POST response's `node_errors`, and fails if
   executed. Fix: delete it from the dict. NOTE: `node_errors` in the POST
   response are warnings — the job still queues. Only a `/history`
   `execution_error` is fatal.

Facts that make these workflows agent-friendly once patched:
- rgthree **Power LoRA Loader** stacks serialize into API inputs as
  `lora_1: {on, lora, strength}` dicts — editable per run.
- **mxSlider** widgets export as `{Xi, Xf, isfloatX}` — write `Xi` when
  `isfloatX: 0`, `Xf` when `1`. mxSlider2D = `{Xi, Yi, ...}` for resolution.
- Component/subgraph nodes get colon-suffixed IDs (`546:82`) in the export —
  valid API IDs, don't rewrite them.
- `LoadImage` nodes pointing at `example.png` in bypassed branches are harmless.
- Control map + patch code for this user's workflow:
  `references/vslinx-allinone-headless.md`.

## DynamicVRAM (comfy-aimdo) playbook — ComfyUI ≥0.30
ComfyUI 0.30's DynamicVRAM streams weight slices straight from the model file
to the GPU through a pinned host buffer. `hostbuf_file_reader_read failed` /
`HostBuffer.read_file_slice failed` (raised in `comfy_aimdo/host_buffer.py`)
means the file→pinned-RAM read failed — before the GPU is even involved. The
reported node (often KSampler) is only where it surfaced. Typical
environmental causes: tight system RAM (pinned memory cannot page out),
Windows Defender scanning a multi-GB file on first access, VRAM contention.
Protocol: header-validate → smoke-test → retry. If it recurs: launch with
`--disable-dynamic-vram`, add a Defender exclusion for the models dir, and/or
`POST /free` before heavy runs. Full anatomy + worked case:
`references/dynamic-vram-errors.md`. Recurring resident-VRAM incident (worked
numbers + kill/relaunch sequence, RTX 4070 Ti): `references/dynamic-vram-resident-ram-case.md`.

### Systemic trigger: VRAM stays resident after successful runs
The most common recurring pattern is NOT a single OOM — it's that a model
stack stays loaded in VRAM after a successful batch, so the *next* heavy
generation (especially one applying a LoRA — traceback tops at
`cast_bias_weight`) is forced to stream weights through a nearly-full card.
Tell-tales:
- `system_stats` shows `vram_free` ≪ total (e.g. ~2 GB of 12.8 GB) even with
  `queue_running == 0 && queue_pending == 0`.
- `POST /free` returns 200 **but `vram_free` does not meaningfully recover** —
  this means a model is resident and won't be unloaded by `/free`; only a full
  process kill + relaunch clears it.

### `--disable-dynamic-vram` is launch-scoped, not persistent
The flag applies ONLY to the process it was started with. Any relaunch (manual
batch launcher, server restart, a Hermes background relaunch) drops it. To keep
it permanently, bake it into the launch method (edited `.bat` or the exact
`python_embeded\python.exe -s ComfyUI\main.py --flag` command you use). Verify
it took effect via `system_stats` → `system.argv` should contain the flag.

### `--disable-dynamic-vram` tradeoff: it forces full-file RAM loads (MiniMax H3 case, verified 2026-08)
With DynamicVRAM disabled, `main.py` never sets `aimdo_enabled = True`, so
`load_torch_file` takes the LEGACY branch: `safetensors.safe_open(...).get_tensor(k)`
reads each model file **fully into RAM** at load time. On a 32 GB machine, loading a
15 GB text encoder while a ~10 GB fp32 VAE and ~10 GB Q8 LLM are resident segfaults
natively: `Windows fatal exception: access violation` in `torch/storage.py __getitem__`
→ `comfy/utils.py load_torch_file` → `comfy/sd.py load_clip` (kills the whole server,
exit 2816 observed on Windows). The file validates fine with `safetensors_check.py` —
the loader strategy, not corruption.
- **Rule:** prefer DynamicVRAM ON (default: `enables_dynamic_vram()` in `cli_args.py`
  returns True unless `--disable-dynamic-vram`/`--highvram`/`--gpu-only`/etc.).
  aimdo's `load_safetensors` mmaps the file and exposes lazy `TensorFileSlice`
  tensors — a 15 GB CLIP never fully materializes in RAM.
- Reserve `--disable-dynamic-vram` for when aimdo STREAMING errors
  (`hostbuf_file_reader_read failed`) dominate; the two failure modes are
  distinguishable: streaming errors surface at SAMPLING time, the legacy full-load
  crash at LOAD time inside `load_torch_file`.
- **Confirm which branch ran:** the crash stack's line number inside `utils.py
  load_torch_file` tells you — line ~136 (`f.get_tensor(k)`) = legacy branch
  (aimdo off); the mmap/memoryview path = aimdo on.
- Launcher must bake the choice (flags are launch-scoped). H3 crash ladder + editor
  workflow patching recipe: `references/llama-cpp-vlm-workflow-patching.md`.

### Windows Defender exclusion needs elevation
Adding/viewing `Add-MpPreference -ExclusionPath` requires an elevated shell.
From a non-elevated git-bash: launch
`powershell.exe -NoProfile -Command "Start-Process powershell -Verb RunAs -ArgumentList '-NoProfile','-Command','Add-MpPreference -ExclusionPath \"C:\...\ComfyUI_windows_portable\"'"`
— this pops a UAC prompt the user must approve. Confirm via a second elevated
`Get-MpPreference` write to a file, then read it back (viewing also needs admin).

## Empty model dropdowns (e.g., Impact Pack SAMLoader)
An empty dropdown = the source folder is missing/empty, not a code bug. Impact
Pack's SAMLoader lists `models/sams/` (.pt/.pth/.safetensors, names containing
'hq' excluded); create the dir, add a SAM file, reopen the node. Also:
`sam_model_opt` is OPTIONAL on FaceDetailer — a SAMLoader with
`model_name: null` that never executed cannot cause generation errors; check
the executed-nodes list in history before chasing SAM. **But** a saved workflow
that baked in `null` silently dead-ends the detailer branch (run reports
success with no preview). Fix: download `sam_vit_b_01ec64.pth` into
`models/sams/`, patch the null widget in `definitions/subgraphs[0]/nodes[..]`,
reload, verify via `/object_info`. Details + code:
`references/impact-pack-sam.md`.

## LLM / llama_cpp nodes all-CPU (CPU-only llama-cpp-python)
Symptom: `llama_cpp_model_loader` / `llama_cpp_instruct_adv` nodes (ComfyUI-llama-cpp_vlm
pack) run the LLM stage entirely on CPU — task manager shows CPU/RAM, prompt-writing takes
minutes — even though the loader defaults `vram_limit = -1` (offload everything).
- **Root cause:** the `llama-cpp-python` wheel inside `python_embeded` was built WITHOUT
  CUDA. `n_gpu_layers`/`vram_limit` are silently ignored by a CPU-only build. A smaller
  model does NOT fix this — it just runs less slowly on CPU.
- **Verify (do this first):**
  `python_embeded\python.exe -c "from llama_cpp import llama_cpp as lc; print(lc.llama_supports_gpu_offload())"`
  → `False` = CPU-only build. Also note `llama_cpp.__version__` and the Python version.
- **Fix:** install the prebuilt CUDA wheel that matches BOTH the installed version and the
  Python version, from `https://github.com/JamePeng/llama-cpp-python/releases`
  (e.g. `llama_cpp_python-0.3.46+cu131-cp313-cp313-win_amd64.whl` for 0.3.46 + Python 3.13):
  `python_embeded\python.exe -m pip install --force-reinstall --no-deps <wheel-url>`
  then restart ComfyUI and re-verify. Rollback: reinstall the plain PyPI wheel of the same
  version. Full worked case, machine topology, and VRAM fit math:
  `references/llama-cpp-offload-cpu-build.md`.
- **VRAM math for a 12 GB card:** 9B Q8 (~9.5 GB) + mmproj (~0.6 GB) ≈ 10.1 GB — offloads
  fully but tight; if it spills, set the loader's `vram_limit` to ~10-11 GB (offload what
  fits, rest on CPU) or use a Q5_K_M/Q4_K_M quant of the same model (~6.5/5.5 GB).

## MiniMax H3 Turbo route (fl2va, 4-8 steps) — ready-made community setup
The fast tier exists as a ready-made community workflow + node pack; pointer-swap recipe, model-size
table, node-pack internals, and gotchas: `references/h3-turbo-setup.md`. Core rules: download the
fl2va PRUNED int8 (19.53 GB), not non-pruned/bf16; use the community pack's LoRA node (standard
loaders may not apply H3 Turbo LoRAs); never stack Turbo LoRA with Spectrum; 1344x768 may need
dropping to 1280x736 on 12 GB. User's Turbo workflow lives at
`user_data/workflows/MiniMaxH3_Turbo/minimax_h3_t2v_turbo.json`.

## Pitfalls
- The failing node is where the exception surfaced, not the cause — read the
  traceback TAIL (innermost frame).
- History's `prompt` field is the API-format graph that was actually submitted —
  trust it over the workflow .json on disk (the user may have changed settings
  since saving).
- Editor-format workflow JSON hides group-node internals; grep the raw JSON
  (e.g., for "SAMLoader") to find widgets inside group nodes. Nodes live in the
  `nodes` ARRAY with POSITIONAL `widgets_values` (never top-level dict keys); the
  browser keeps its in-memory copy until the workflow is reloaded from disk.
  Patch recipe + `llama_cpp_instruct_adv` widget map:
  `references/llama-cpp-vlm-workflow-patching.md`.
- Never declare a model corrupt without header validation + smoke test;
  transient streaming failures mimic corruption.
- Prefer `last_error.py` over hand-rolling `/history` parsing. The exception
  text sits nested inside `status.messages` in a structure that naive scans for
  `execution_error` / `'error' in str(msg)` frequently MISS — this session's
  ad-hoc inline parsers kept returning empty while `last_error.py` surfaced the
  full `RuntimeError: HostBuffer.read_file_slice failed` traceback. If you must
  parse `/history` directly, search `status.messages` for a dict whose `type`
  field equals `execution_error` and read its `data`, digesting the whole
  serialized message — not substring matching on the message string.
- `curl taskkill //PID N //F` (double slash) fails in git-bash — MSYS mangles
  it. Use single-slash `taskkill /PID N /F`.
- Before claiming a tool/build is absent from the machine, search ALL install
  forms: native source trees (`~/llama.cpp/build/bin`, CMakeCache `GGML_CUDA`
  flag), venv site-packages, other drives. A CUDA-native C++ build and a
  CPU-only Python wheel of the same project can coexist — ComfyUI nodes import
  the Python binding in `python_embeded` and never use native binaries. Verify,
  don't speculate.

## Verification
- Re-run the originally failing job (or its smoke test) → status success and
  output files land on disk.
