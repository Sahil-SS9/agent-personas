# Worked case: recurring DynamicVRAM failures from resident VRAM (RTX 4070 Ti)

Concrete incident that established the "systemic trigger" guidance in the
DynamicVRAM playbook. Session on a 12.8 GB RTX 4070 Ti, ComfyUI 0.30.0
portable with comfy-aimdo.

## Symptom
Two consecutive generations failed (`status_str: error`) after a batch that
had succeeded (14 images out). `last_error.py` on the latest run reported:

```
node      : 546:82 (KSampler)
exception : RuntimeError: HostBuffer.read_file_slice failed
traceback top: comfy/ops.py cast_bias_weight → handle_pin →
               comfy_aimdo/host_buffer.py:109  raise RuntimeError("HostBuffer.read_file_slice failed")
```

The traceback showed LoRA weight casting (`cast_bias_weight`) — a LoRA being
applied at sampling was what forced the streaming read.

## Evidence chain
- `/history?max_items=5`: two of the three most recent error entries carried
  the DynamicVRAM signature; a successful 14-image batch sat between them.
- `system_stats` with **0 running / 0 pending** in the queue still showed
  `vram_free ~ 2.2 / 12.88 GB` → a model stack was resident.
- `POST /free` (`{"unload_models":true,"free_memory":true}`) returned 200 but
  `vram_free` stayed ~2.3 GB → the resident model was NOT released by `/free`.
- Free system RAM was also tight (`ram_free ~ 12 GB` of 34 GB), matching the
  skill's "low RAM + multi-GB checkpoint = streaming-error risk" warning.

## Fix sequence (both verified via live output)
1. **Windows Defender exclusion** for `C:\Users\Hermes\ComfyUI\ComfyUI_windows_portable\`
   via elevated PowerShell (UAC prompt appears). Confirmed present in
   `Get-MpPreference` ExclusionPath afterwards.
2. **Kill + relaunch the portable server** — the only thing that cleared the
   resident ~10 GB VRAM. Identify the main process first:
   ```
   powershell "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object {$_.CommandLine -match 'main.py'}"
   taskkill /PID <pid> /F      # single slash; //PID mangles in git-bash
   ```
   Relaunch from the portable root:
   ```
   cd /c/Users/Hermes/ComfyUI/ComfyUI_windows_portable
   ./python_embeded/python.exe -s ComfyUI/main.py --windows-standalone-build --disable-dynamic-vram
   ```
3. **Verify** via `system_stats`:
   - `system.argv` contains `--disable-dynamic-vram`
   - `vram_free` rose to ~11.6 / 12.88 GB on the fresh boot.

## Key takeaways (encoded into SKILL.md)
- `HostBuffer.read_file_slice failed` is the co-equal signature with
  `hostbuf_file_reader_read failed`.
- `/free` does NOT clear a resident model; only process kill + relaunch does.
- `--disable-dynamic-vram` is launch-scoped and vanishes on any relaunch.
- Defender exclusion add/view both require elevation (UAC).
