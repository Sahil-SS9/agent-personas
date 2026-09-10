# Krea2 DynamicVRAM session reference

## Observed environment

- Windows 11 portable ComfyUI
- RTX 4070 Ti with approximately 12 GB VRAM
- Approximately 32 GB physical RAM
- ComfyUI 0.34.0
- comfy-aimdo 0.4.15
- Launcher: `python_embeded\\python.exe -s ComfyUI\\main.py --windows-standalone-build`

## Verified signatures

Both successful and failed attempts staged Krea2 components. A failed sequence included:

```text
MemoryError
HostBuffer.read_file_slice failed
hostbuf_file_reader_read failed
Windows fatal exception: access violation
```

The traceback surfaced in Krea text encoding after DynamicVRAM staged a roughly 5 GB text encoder and a roughly 12.5 GB Krea2 model. One attempt reported 263 patches attached.

## Live-watch recipe

Follow the active log from EOF. Do not begin with only `comfyui.prev.log`, because it can contain an earlier failure. Watch for model-load lines and the failure markers above. Record `/system_stats` before queueing, then verify history output and the file in `ComfyUI/output/`.

## Interpretation

Intermittent success supports a resource/timing or resident-state explanation more strongly than a conclusively corrupt model. Keep DynamicVRAM enabled initially. Reproduce with a fresh process, batch 1, reduced resolution, and no LoRA; restore variables incrementally. Increasing the Windows pagefile may increase commit headroom but does not substitute for RAM, pinned host buffers, or VRAM bandwidth.
