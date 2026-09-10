---
name: comfyui-runtime-observability
description: "Use when monitoring intermittent local ComfyUI runs."
version: 1.0.0
license: MIT
---
# ComfyUI Runtime Observability

Provide grounded diagnosis for local ComfyUI jobs whose behavior varies between successful and failed runs, especially large Krea/Krea2, Flux, video, or other DynamicVRAM workflows.

## Operating procedure

1. Check server health before queueing with `GET http://127.0.0.1:8188/system_stats`. Record ComfyUI version, free system RAM, free VRAM, device name, and `system.argv`.
2. Identify the active log. For a Windows portable install, use `ComfyUI/user/comfyui.log`.
3. Start monitoring before the user queues the job. Follow from the current end so historical failures are not attributed to the new run.
4. Capture `Requested to load`, `prepared for dynamic VRAM loading`, `MemoryError`, `HostBuffer.read_file_slice failed`, `hostbuf_file_reader_read failed`, `execution_error`, and `Windows fatal exception: access violation`.
5. Verify success through ComfyUI history plus a corresponding output file. A loaded model or preview alone is insufficient.

## Intermittent DynamicVRAM runs

A workflow that sometimes succeeds is not automatically corrupt. Large models may load correctly and fail later when DynamicVRAM streams another weight block through pinned host memory. Repeated model preparation lines can indicate swapping and elevated pressure rather than a missing model. Preserve DynamicVRAM by default unless the observed signature specifically warrants another loader strategy.

For Krea2-style workloads, reduce one variable at a time: batch size, resolution, LoRAs/patches, or concurrent model branches. A fresh process is a useful control because it removes resident model state. Avoid rapid repeated queue submissions while the first model is staging.

## Reporting

Report the health snapshot, exact active log path, whether monitoring began before the run, new relevant timestamps, classification, confidence, and output verification. Never infer a current failure from `comfyui.prev.log`; use previous logs only as recurrence evidence.

## References

- `references/krea2-dynamic-vram-session.md` — verified Krea2 signatures, environment snapshot, and live-watch recipe.
