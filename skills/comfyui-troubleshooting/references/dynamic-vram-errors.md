# DynamicVRAM (comfy-aimdo) streaming errors — ComfyUI ≥0.30

## What DynamicVRAM is
ComfyUI 0.30 ships `comfy-aimdo`, a DynamicVRAM manager. Instead of loading an
entire multi-GB checkpoint into system RAM first, it streams weight slices
directly from the model file on disk to the GPU, staging through a pinned
(page-locked) host buffer:

```
model.safetensors (disk)
   │ read_file_to_device(file, offset, size, stream_ptr, ...)   ← failure point
   ▼
pinned host buffer (comfy_aimdo.host_buffer.HostBuffer)
   │ async copy / gather
   ▼
GPU weights → forward pass
```

Code path: `comfy/memory_management.py:read_tensor_file_slice_into` →
`comfy_aimdo.host_buffer.read_file_to_device` (native extension) → raises
`RuntimeError("hostbuf_file_reader_read failed")` when the disk→pinned-RAM read
fails. `comfy_aimdo.control.init()` wires it up in `main.py`; if aimdo is
absent ComfyUI falls back to legacy ModelPatcher with a log warning.

## Signature
- `exception_message: hostbuf_file_reader_read failed`
- `exception_type: RuntimeError`
- Traceback tail: `comfy/ops.py cast_bias_weight` → `model_management.cast_to_gathered`
  → `memory_management.read_tensor_file_slice_into` → `comfy_aimdo/host_buffer.py`.
- Surfacing node is typically a KSampler (where weights get gathered), NOT the
  checkpoint loader.

## Environmental causes (in practice order)
1. **System RAM pressure** — pinned memory can't be paged; tight free RAM makes
   the OS refuse/stall page-locking. Watch `ram_free` in /system_stats.
2. **Windows Defender** — real-time scan of a multi-GB .safetensors on first
   access holds/throttles the read. Classic "fails once, works on retry".
3. **VRAM contention** — little free VRAM when the transfer is set up.

## Worked case (2026-08-04, RTX 4070 Ti / 32 GB RAM / Win10)
- Failed run: KSampler crashed with `hostbuf_file_reader_read failed`,
  checkpoint `plantMilkModelSuite_hempII.safetensors` (7.1 GB). Only ~8 GB of
  32 GB RAM free at the time; two 7 GB checkpoints in the graph.
- Verification: safetensors header parse OK (2515 tensors, offsets match size);
  minimal 4-step smoke test through the SAME checkpoint succeeded and saved an
  image. → transient, not corruption.
- Resolution: retry. Permanent escape hatches if it recurs:
  - Launch flag `--disable-dynamic-vram` (legacy estimate-based loading).
  - Defender exclusion for the ComfyUI models directory.
  - `POST /free` (`{"unload_models": true, "free_memory": true}`) before runs.
  - Related flags: `--cache-classic`, `--disable-pinned-memory`,
    `--fast-disk` (prefer disk-backed loading on NVMe), `--vram-headroom`.

## Discrimination protocol before re-downloading
1. Header-validate the file (scripts/safetensors_check.py).
2. Smoke-test the exact checkpoint through a minimal workflow.
3. Both pass → transient/environmental; retry or apply escape hatches.
