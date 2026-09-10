---
name: acestep-music-generation
description: "ACE-Step local music generation via REST API — DSL/caption prompts → generate → save audio"
version: 1.0.0
license: MIT
---
# ACE-Step Music Generation

Generate music locally using ACE-Step's REST API (`http://localhost:8001`). Supports text-to-audio generation with full caption/lyrics control, cover mode, and fix/repaint.

## Prerequisites

- ACE-Step 1.5 installed at `~/Suno/ACE-Step-1.5/`
- API server running on `localhost:8001`
- Your RTX 4070 Ti (12GB VRAM) handles the sft config with headroom

## Starting the API Server

### Option A: Double-click (Recommended)
Double-click `start_api_server.bat` in `~/Suno/ACE-Step-1.5/`

### Option B: Terminal
```bash
cd ~/Suno/ACE-Step-1.5
uv run acestep-api
```

Wait for "Server is ready to accept requests" — then go to `http://localhost:8001/docs` for Swagger UI.

**Verify the server is running:**
```bash
curl http://127.0.0.1:8001/health
```
Returns `{"data":{"status":"ok","service":"ACE-Step API"}}` when healthy. Models show `"models_initialized":false` until first request triggers lazy-load.

**Preload models at startup** (models lazy-load on first request by default):
```bash
ACESTEP_NO_INIT=false uv run acestep-api
```

## Closing the Server

### Option A: Double-click `close_api_server.bat`
Added companion script at `~/Suno/ACE-Step-1.5/close_api_server.bat`. Tries graceful shutdown first, force-kills if needed.

### Option B: Clean close (server running in its own terminal window)
Press **`Ctrl+C`** in that window — graceful shutdown.

### Option C: Force kill a zombie (orphaned process holding the port)
```powershell
netstat -ano | findstr :8001          # find the LISTENING PID
powershell -Command "Stop-Process -Id <PID> -Force"   # kill it
netstat -ano | findstr :8001          # verify port is free
```

### One-liner (kill whatever is on port 8001)
```powershell
netstat -ano | findstr :8001 && for /f "tokens=5" %p in ('netstat -ano ^| findstr :8001') do powershell -Command "Stop-Process -Id %p -Force" && echo Port freed || echo Port already free
```

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/chat/completions` | POST | Generate music (OpenRouter-compatible) |
| `/v1/models` | GET | List available models |
| `/health` | GET | Health check / model load status |

## Generation Workflow

### Step 1: Write your prompt

**Caption** = overall vibe. Cover: genre, emotion, instruments, timbre, vocal style, BPM.

**Lyrics** = structure with section tags:
```
[Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Bridge]
[Outro]
```

### Step 2: Call the API

```python
import requests, json, base64

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [
        {"role": "user", "content": "your caption and/or lyrics here"}
    ],
    "max_tokens": 240  # ~120s output
})
data = response.json()
```

### Step 3: Save the audio

```python
audio_list = data['choices'][0]['message'].get('audio', [])
for i, a in enumerate(audio_list):
    b64 = a['audio_url']['url'].split(',', 1)[1]
    audio_bytes = base64.b64decode(b64)
    with open(f"output_{i}.mp3", 'wb') as f:
        f.write(audio_bytes)
```

## Parameters Reference

| Parameter | Type | Notes |
|-----------|------|-------|
| `model` | str | `acestep/acestep-v15-sft` (quality) or `acestep/acestep-v15-turbo` (speed) |
| `messages[0].content` | str | Caption (vibe) + optional lyrics with `[section]` tags |
| `max_tokens` | int | 240 ≈ 128s at 5Hz. Scale: 240 = 128s, 360 = 180s |
| `seed` | int | Reuse seeds for consistent results (omit for random) |

## Prompt Templates

### Simple (no lyrics)
```
"trap soul, dark and intimate, 72 BPM, D minor, male vocals, 808 sub-bass"
```

### With lyrics
```
"[Verse 1]\nCity never sleeps but I ain't been asleep in weeks\n[Chorus]\nI'm still wearing black for you"
```

### Cover mode
The API supports style transfer — pass a source description with different genre/instruments.

## Output

- Audio returns as base64 `data:audio/mpeg;base64,...` in the response
- Duration: `max_tokens * 0.53s` approximately
- API also saves to `gradio_outputs/` in the repo directory

## Configuration

- `.env` controls model config (sft vs turbo, LM model size)
- Quality config: `acestep-v15-sft` (50 steps, ~4.7GB VRAM) + `acestep-5Hz-lm-0.6B` (stable on 12GB)
- High-quality LM (try if VRAM allows): `acestep-5Hz-lm-1.7B` (better lyrics, ~1.1GB more VRAM)
- Turbo: `acestep-v15-turbo` (8 steps) for rapid iteration
- Set `ACESTEP_NO_INIT=false` in `.env` or env var to preload models at startup (default: lazy-load on first request)

## Support Files

- `references/errors-and-recovery.md` — VRAM troubleshooting, port cleanup, error transcripts, ConnectionResetError fix, model download timing
- `references/close-api-server-bat.md` — Companion batch file (`close_api_server.bat`) details, usage, exit codes, and the pitfalls discovered when creating it (batch file line-ending sensitivity, `timeout` vs git-bash, PowerShell quoting).
- `references/ace-step-directory-anatomy.md` — Complete inventory of every file and directory in the ACE-Step 1.5 installation, with what each does and whether you need to care about it.
- `close_api_server.bat` (deployed to ACE-Step directory, not in skill package) — One-double-click tool to kill zombie processes on port 8001.

## Troubleshooting

| Symptom | Fix |
|---------|------|
| Server won't start — `[Errno 10048] address in use` | Zombie process holds port 8001. Diagnose: `netstat -ano \| findstr :8001` → find LISTENING PID → `powershell -Command "Stop-Process -Id <PID> -Force"` → verify free → restart. Use the one-liner in "Closing the Server" for quick cleanup. |
| Port 8001 in use, can't kill with taskkill | `powershell -Command "Stop-Process -Id <PID> -Force"` — more reliable than `taskkill` on Windows 10 |
| SIGSEGV / crash on generation | VRAM pressure. Switch .env to `acestep-5Hz-lm-0.6B` instead of 1.7B. The 0.6B LM saves ~1.1GB VRAM |
| Model not initialized (503 from API) | Start with `ACESTEP_NO_INIT=false` env var or allow lazy-load — first request after startup takes ~30-60s to init |
| Model download / first run | Allow ~5-7 minutes. Downloads ~6GB total at ~100MB/s. Normal |
| ConnectionResetError on generation | Response is large base64 audio (~3MB). Use `python -c` from within ACE-Step dir, not from Hermes agent's venv |
| Low quality | Check `/health` for `models_initialized: true` and `loaded_model: acestep-v15-sft` |

## Pitfalls (RTX 4070 Ti 12GB)

- **sft + 1.7B LM preloaded** uses ~9.5GB VRAM — generation pushes past 12GB → SIGSEGV crash. **Fix:** use 0.6B LM for stable generation.
- **Preloading vs lazy-load:** `ACESTEP_NO_INIT=false` loads everything at startup (convenient but high VRAM). Default (lazy-load) keeps server responsive but first request takes 30-60s to init models.
- **Response too large for curl:** The audio base64 is ~2.7MB. curl saves it fine with `--output`, but Hermes agent's `requests` lib may crash on read. Use ACE-Step's own venv Python for scripting.

### Windows Port Cleanup

When ACE-Step crashes, port 8001 can stay bound to a zombie process.

**Quick fix:** Double-click `close_api_server.bat` in the ACE-Step directory.

**Manual:**
```powershell
# Check who's on port 8001
netstat -ano | findstr :8001

# Force kill (replace PID with the LISTENING pid)
powershell -Command "Stop-Process -Id <PID> -Force"

# Verify free
netstat -ano | findstr :8001
```
