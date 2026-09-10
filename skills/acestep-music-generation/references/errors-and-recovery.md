# ACE-Step Error Patterns & Recovery (RTX 4070 Ti, 12GB VRAM, Windows 10)

## SIGSEGV (Exit Code 139) on Generation

**Symptom:** Server crashes with segmentation fault during or after first generation request.

**Root cause:** VRAM exhaustion. The sft model + 1.7B LM preloaded uses ~9.5GB of 12GB. Generation pushes past the limit.

**Fix:** Switch `.env` to `acestep-5Hz-lm-0.6B` instead of 1.7B. Saves ~1.1GB VRAM.

**Detection:**
```bash
nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader
# If >10500 MiB before generation, you're at risk
```

## ConnectionResetError (WinError 10054)

**Symptom:** `urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(10054, ...))`

**Root cause:** Response is too large for the Hermes agent's `requests` session (~2.7MB base64 audio). The server closes the connection mid-stream.

**Fix:** Run generation scripts from inside the ACE-Step venv, not from Hermes:
```bash
cd ~/Suno/ACE-Step-1.5
python -c "
import requests, base64
resp = requests.post('http://localhost:8001/v1/chat/completions', json={...}, timeout=180)
b64 = resp.json()['choices'][0]['message']['audio'][0]['audio_url']['url'].split(',',1)[1]
with open('output.mp3', 'wb') as f: f.write(base64.b64decode(b64))
"
```

## 503 Model Not Initialized

**Symptom:** `{"detail":"Model not initialized. init_error=None"}`

**Root cause:** Server started in lazy-load mode (default). First request triggers model init, but if VRAM is tight it fails silently.

**Fix:** Start with `ACESTEP_NO_INIT=false` to force preload at startup, or wait for lazy-init to complete (first request may take 30-60s).

## Port 8001 Zombie Process

**Symptom:** `[Errno 10048] error while attempting to bind on address ('127.0.0.1', 8001)`

**Quick fix:** Double-click `close_api_server.bat` in the ACE-Step directory.

**Manual fix:** Kill the orphaned process. `netstat` shows an owner PID but `taskkill` can fail on Windows 10. Use PowerShell:
```powershell
# Find the PID
netstat -ano | findstr :8001

# Force terminate
powershell -Command "Stop-Process -Id <PID_HERE> -Force"

# Verify
netstat -ano | findstr :8001
# Should return only TIME_WAIT entries, not LISTENING
```

## First-Run Model Download Timing

| Model | Size | Time @ ~100MB/s |
|-------|------|------------------|
| DiT sft | 4.79 GB | ~50s |
| VAE | 1.33 GB | ~13s |
| LM 1.7B | 3.71 GB | ~38s |
| LM 0.6B | ~1.2 GB | ~12s |
| Total | ~6-10 GB | ~5-7 min |

Models cache to `checkpoints/` in the repo directory — not re-downloaded on subsequent starts.
