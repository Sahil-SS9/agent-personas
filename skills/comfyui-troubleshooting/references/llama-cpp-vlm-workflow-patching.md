# ComfyUI llama-cpp_vlm node pack + editor-format workflow patching (verified 2026-08, MiniMax H3 all-in-one)

Covers: (1) making the prompt-writing LLM actually use the GPU, (2) editing
editor-format workflow JSON safely, (3) the H3 native-crash ladder on a
12 GB VRAM / 32 GB RAM box (RTX 4070 Ti, ComfyUI 0.30.0).

## 1. llama-cpp-python inside ComfyUI portable (`python_embeded`)

- ComfyUI portable ships its own Python 3.13 runtime. Its `llama-cpp-python` is a
  SEPARATE install from any `~/llama.cpp` native build or agent venv. ComfyUI nodes
  (`llama_cpp_model_loader`, `llama_cpp_instruct_adv` from the ComfyUI-llama-cpp_vlm
  pack) import the Python binding in `python_embeded` — they never use native
  binaries like `llama-server.exe`.
- CPU-only symptom: LLM stage runs entirely on CPU regardless of `n_gpu_layers`.
  Check: `python_embeded\python.exe -c "from llama_cpp import llama_cpp as lc; print(lc.llama_supports_gpu_offload())"`
- Fix: JamePeng prebuilt CUDA wheel matching version + Python:
  `pip install --force-reinstall --no-deps https://github.com/JamePeng/llama-cpp-python/releases/download/<tag>/llama_cpp_python-<ver>+cu131-cp313-cp313-win_amd64.whl`
  (wheel bundles its own CUDA runtime DLLs; only needs a recent driver ≥ ~580).
- **GOTCHA:** `llama_supports_gpu_offload()` returns False even on the working CUDA
  build (JamePeng fork). Verify functionally instead: load any GGUF with
  `n_gpu_layers=4, verbose=True` and grep for `ggml_cuda_init` /
  `offloaded N/33 layers to GPU`. Trust the functional test, never that helper.
- Loader node semantics (`ComfyUI-llama-cpp_vlm/nodes.py`): `vram_limit = -1`
  (default) → `n_gpu_layers = -1` (all layers to GPU); `vram_limit >= 0` → computes
  layers that fit the budget, remainder on CPU. `mmproj` + a non-None `chat_handler`
  required for vision (reads reference images).
- Model swap constraints: replacement must be a VLM with an `mmproj` GGUF in
  `models/LLM/` AND a `chat_handler` the pack supports (Qwen3.5, Qwen3-VL,
  MiniCPM-v4.5/4.6, Gemma3, GLM-4.6V, ...). Swap families → change `chat_handler`.
  For vision grounding set `image_min_tokens` ≥ 1024 (llama.cpp warns otherwise).

## 2. Editor-format workflow JSON patching (no UI needed)

- Editor workflows have top-level bookkeeping keys (`last_node_id`, `nodes`,
  `links`, `groups`, `config`, `extra`) — **nodes live in `data["nodes"]`, an
  ARRAY**, each with `"id"`, `"type"`, `"widgets_values"`. API format is a flat
  `{node_id: {...}}` dict. A patch script that scans top-level keys silently
  matches nothing (both formats are valid JSON; check for `nodes` first).
- `widgets_values` is POSITIONAL (node-definition input order). For
  `llama_cpp_instruct_adv`: `[0]`=preset_prompt, `[1]`=custom_prompt,
  `[2]`=system_prompt, `[3]`=inference_mode, `[4]`=max_frames, `[5]`=max_size,
  `[6]`=seed, `[7]`=seed_mode ("fixed"/"randomize"), `[8]`=force_offload,
  `[9]`=save_states. `force_offload=true` = "Unload the model after inference"
  (frees ~10 GB VRAM/RAM before downstream stages — REQUIRED when the LLM stage
  precedes a heavy VAE/UNET on a 12 GB card).
- Always back up first (`cp file.json file.json.bak`), then write back with
  `json.dump(data, f, ensure_ascii=False, indent="\t")`. Re-load and verify the
  exact widget values after writing.
- **The open browser tab keeps its in-memory copy**: edits on disk only appear
  after Workflow → Open / re-drag. Display nodes (ShowText|pysssss) cache the
  last output until re-run. If the user has loaded reference images in the tab,
  reloading resets them to defaults — offer manual widget paste as the alternative.
- Changing the system prompt alone is enough to switch output language (e.g. the
  original Chinese director prompt had rule "默认使用中文" = default Chinese;
  an English system prompt with "ALWAYS respond in English" overrides input language).

## 3. MiniMax H3 native-crash ladder (12 GB VRAM / 32 GB RAM)

All three are `Windows fatal exception: access violation` (native, not catchable;
kills the whole server; exit 2816 observed). Read the innermost frame to place them:

| Stage reached | Innermost frame | Cause | Fix |
|---|---|---|---|
| VAE construction | `comfy/ldm/minimax/vae.py` (torch `nn.Linear __init__`) | ~10 GB Q8 LLM still resident on GPU when fp32 video VAE (~10 GB) builds | `force_offload=true` on `llama_cpp_instruct_adv` |
| CLIP/text-encoder load | `torch/storage.py __getitem__` → `utils.py load_torch_file` → `sd.py load_clip` | `--disable-dynamic-vram` → legacy `safe_open.get_tensor` reads 15 GB TE fully into RAM while VAE+LLM resident | Remove `--disable-dynamic-vram` (DynamicVRAM lazy mmap); if streaming `hostbuf` errors appear instead, Defender exclusion / free RAM |
| Sampling | `hostbuf_file_reader_read failed` (aimdo) | file→pinned-RAM streaming read failed (Defender, tight RAM) | See dynamic-vram-errors.md playbook |

Verification commands used: `curl system_stats` for `system.argv` (confirm flags
actually took effect — flags are launch-scoped), `safetensors_check.py` on the
15 GB TE (proved healthy → loader/memory, not corruption), grep of ComfyUI source
(`main.py` aimdo gate, `cli_args.py enables_dynamic_vram`, `utils.py load_torch_file`
branches) to confirm which loader path executed.
