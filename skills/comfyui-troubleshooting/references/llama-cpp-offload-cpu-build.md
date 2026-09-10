# llama-cpp in ComfyUI: CPU-only wheel vs native CUDA build (worked case)

Date: 2026-08 · ComfyUI v0.30.0 portable · RTX 4070 Ti (12 GB) · Windows

## Symptom
MiniMax H3 "All-in-One" workflow (`minimaxH3AllInOne_v10`): the prompt-director stage
(`llama_cpp_model_loader` + `llama_cpp_instruct_adv` from the ComfyUI-llama-cpp_vlm
custom node pack) loaded the LLM entirely onto CPU. User expected GPU offload with the
remainder on CPU. (User's "Qwen 3.59B" = Qwen3.5-9B-Q8_0.gguf.)

## Machine topology (verified 2026-08)
- Native llama.cpp C++ build at `C:\Users\Hermes\llama.cpp\` — `GGML_CUDA:BOOL=ON` in
  `build/CMakeCache.txt`, nvcc from CUDA v13.3 toolkit; binaries in `build/bin/`
  (`llama-server.exe`, `llama-cli.exe`, `llama-quantize.exe`, `ggml-cuda.dll`).
  Used by the user's local agent / local models. NOT used by ComfyUI nodes.
- ComfyUI portable `python_embeded` (Python 3.13.14) has its OWN `llama-cpp-python`
  wheel at `Lib/site-packages/llama_cpp/` — this is what the custom node imports.
  At diagnosis it was a CPU-only build: `llama_supports_gpu_offload() = False`.

## Why everything loaded on CPU
The loader node defaults `vram_limit = -1` -> `n_gpu_layers = -1` ("offload all").
A CPU-only llama-cpp-python build ignores `n_gpu_layers` entirely. A smaller model
does NOT fix this — it just runs less slowly on CPU.

## Diagnosis (commands)
1. Binding build check:
   `python_embeded\python.exe -c "import llama_cpp; from llama_cpp import llama_cpp as lc; print(llama_cpp.__version__, lc.llama_supports_gpu_offload())"`
2. Version + source: `python_embeded\python.exe -m pip show llama-cpp-python`
3. Node pack: `custom_nodes/ComfyUI-llama-cpp_vlm/nodes.py` — loader computes
   n_gpu_layers from vram_limit (approx lines 223-278): -1 = all-GPU; otherwise
   `max(1, int((vram_limit - mmproj_size) / gguf_layer_size))`.
4. Saved workflow: check the loader node's widgets (model, vram_limit, n_ctx,
   chat_handler).

## Fix
Prebuilt CUDA wheel from https://github.com/JamePeng/llama-cpp-python/releases —
match version AND Python cp tag exactly. Worked case: release `v0.3.46-cu131-win-20260808`
-> `llama_cpp_python-0.3.46+cu131-cp313-cp313-win_amd64.whl`.
Install: `python_embeded\python.exe -m pip install --force-reinstall --no-deps <wheel-url>`
Restart ComfyUI, re-verify `llama_supports_gpu_offload() == True`.
Rollback: `python_embeded\python.exe -m pip install --force-reinstall llama-cpp-python==0.3.46`
(PyPI CPU wheel). The CUDA wheel bundles its own runtime; pip never touches the NVIDIA
driver or the CUDA 13.3 toolkit, and `~/llama.cpp/build` is untouched by pip.

## VRAM fit (12 GB card)
- Qwen3.5-9B-Q8_0.gguf ~9.5 GB + mmproj-Q8_0.gguf ~0.6 GB ~= 10.1 GB weights + KV cache.
  Fully offloads, tight. If OOM/spill: set loader `vram_limit` ~10-11 GB (offload what
  fits, rest on CPU), or use Q5_K_M (~6.5 GB) / Q4_K_M (~5.5 GB) of the same model.
- Smaller VLM swap is possible (Qwen3-VL-8B/4B/2B, MiniCPM-v4.5+, Gemma3, GLM-4.6V)
  but the family MUST be in the node's chat_handler list AND ship an mmproj GGUF;
  prompt-quality drops below ~8B. Not worth it once the build is fixed.

## Do NOT confuse the two "Qwen" models in the H3 workflow
- Swappable: the director LLM (Qwen3.5-9B GGUF via llama_cpp nodes).
- Fixed: `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` (~15 GB) is the official MiniMax
  H3 text encoder (CLIPLoader type=minimax) — already the smallest quant, NOT replaceable
  with a smaller model.

## Lesson
When asked "can I use a smaller model instead" for an LLM stage that runs on CPU, check
the binding's GPU support FIRST — the model was never the bottleneck.
