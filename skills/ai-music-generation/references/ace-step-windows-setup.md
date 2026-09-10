# ACE-Step 1.5 — Windows Setup & Generation Walkthrough

System: Windows 10, RTX 4070 Ti (12GB VRAM), 32GB RAM, git-bash shell, Python 3.11 via uv.

## Full Setup Sequence

```bash
# 1. Clone
cd ~/Suno
git clone https://github.com/ACE-Step/ACE-Step-1.5.git
cd ACE-Step-1.5

# 2. Install deps (125 packages, includes PyTorch 2.7.1+cu128, flash-attn for Windows)
uv sync

# 3. Configure for quality
cp .env.example .env
# Edit .env to set:
#   ACESTEP_CONFIG_PATH=acestep-v15-sft
#   ACESTEP_LM_MODEL_PATH=acestep-5Hz-lm-1.7B
```

## First Launch — Model Download

Run with `ACESTEP_NO_INIT=false` to force model preloading at startup:

```bash
ACESTEP_NO_INIT=false uv run acestep-api
```

### Model Download Order & Sizes
| Model | Size | Type |
|-------|------|------|
| DiT (sft) | 4.79 GB | model.safetensors |
| LM planner (1.7B) | 3.71 GB | model.safetensors |
| VAE / tokenizer | 1.33 GB | model.safetensors |
| **Total** | **~9.8 GB** | |

Download speed: ~100-130 MB/s on typical connection. Takes 2-4 minutes total.

Cached at: `~/.cache/huggingface/hub/` on subsequent runs.

### Initialization Sequence (after download completes)
1. `5Hz LM tokenizer loaded successfully in 11.42 seconds`
2. `Initializing constrained decoding processor...`
3. `Setting constrained decoding max_duration to 480s based on GPU config (tier: tier4)`
4. DiT model loads into VRAM → ~9.5 GB / 12 GB used on RTX 4070 Ti

### Server Ready (lazy-load mode)
Without `ACESTEP_NO_INIT=false`, the server starts immediately but logs:
```
[API Server] Models will be lazy-loaded on first request
[API Server] Set ACESTEP_NO_INIT=false to load models at startup
INFO: Application startup complete.
```

## Port Conflict Resolution

Port 8001 often stays LISTENING after a failed or killed process. Symptom:
```
ERROR: [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8001)
```

### Kill on Windows
```powershell
# Find the offender
netstat -ano | findstr :8001

# Try taskkill first
taskkill /PID <PID> /F

# If that hangs/times out, use PowerShell
powershell -Command "Stop-Process -Id <PID> -Force"

# Wait for TIME_WAIT to clear
Start-Sleep -Seconds 2

# Verify
netstat -ano | findstr :8001
```

## Verify the API

```bash
# Health check
curl -s http://localhost:8001/health
# {"data":{"status":"ok","models_initialized":true,"llm_initialized":true,"loaded_model":"acestep-v15-sft","loaded_lm_model":"acestep-5Hz-lm-1.7B"},...}

# List models
curl -s http://localhost:8001/v1/models
# Lists "acestep/acestep-v15-sft" with pricing 0 (free), input/output modalities: text + audio
```

## Generate a Song

The API uses an OpenRouter-compatible `/v1/chat/completions` endpoint. The `content` field = music caption.

### Python Example
```python
import requests, base64, json

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [
        {"role": "user", "content": "trap soul, dark and intimate, raspy male vocals, 808 sub-bass, atmospheric pads, 72 BPM, D minor"}
    ],
    "max_tokens": 240   # controls duration (~0.53s per token → ~128s)
})

data = response.json()
choice = data['choices'][0]

# Text metadata
print(choice['message']['content'])
# Returns markdown with Caption, BPM, Duration, Key, Time Signature

# Audio — base64 in audio[0].audio_url.url
audio_url = choice['message']['audio'][0]['audio_url']['url']
# Format: data:audio/mpeg;base64,SUQzBAAAA...

b64 = audio_url.split(',', 1)[1]
audio_bytes = base64.b64decode(b64)

with open("output.mp3", 'wb') as f:
    f.write(audio_bytes)
```

### Generation Stats (from test run)
- **Requested**: 72 BPM, D minor, trap soul, male vocals
- **Generated**: 239s metadata duration, 128s actual audio file (3.6 MB MP3)
- **Key**: D minor ✓
- **BPM note**: LM returned 300 BPM — the 1.7B planner sometimes reinterprets BPM values. The audio itself matched the mood/genre well despite metadata discrepancy.

## GPU Memory (RTX 4070 Ti)

| State | VRAM Used | % of 12GB |
|-------|-----------|-----------|
| Idle (no models) | ~1 GB | ~8% |
| After loading sft + 1.7B LM | ~9,577 MiB | ~78% |
| Headroom available | ~2,705 MiB | ~22% |

Suitable for generation at 50-step sft quality. Turbo config would use less VRAM but generate faster. XL models would require CPU offload.

## .env Config Notes

The `.env` file at `~/Suno/ACE-Step-1.5/.env`:

```ini
# ACE-Step Configuration for High Quality
# Using sft (50 steps) + 1.7B LM for best quality

ACESTEP_CONFIG_PATH=acestep-v15-sft
ACESTEP_LM_MODEL_PATH=acestep-5Hz-lm-1.7B
```

Available configs (from docs):
- `acestep-v15-sft` — 50 steps, high quality, ~4.7GB VRAM
- `acestep-v15-turbo` — 8 steps, faster, slightly lower quality
- `acestep-v15-base` — 50 steps, no fine-tuning, medium quality
- `acestep-v15-xl-sft` — 4B XL, ~9GB VRAM (needs CPU offload on 12GB)

Available LM models:
- `acestep-5Hz-lm-0.6B` — smallest, fastest
- `acestep-5Hz-lm-1.7B` — good balance for complex lyrics
- `acestep-5Hz-lm-4B` — strongest, composition and melody (needs >16GB VRAM)

## Caption Writing Best Practices

Based on ACE-Step's official guide and practical testing:

| Dimension | Examples |
|-----------|----------|
| Genre | trap soul, lo-fi hip hop, synthwave, indie folk, dark cinematic orchestral |
| Emotion | melancholic, dark, intimate, dreamy, uplifting, euphoric |
| Instruments | 808 sub-bass, atmospheric pads, fingerpicked acoustic guitar, strings |
| Timbre | warm, bright, airy, punchy, lush, raw |
| Vocal | raspy male vocal, breathy female vocal, falsetto, choir, spoken word |
| Era/Reference | 80s synth-pop, modern trap, reminiscent of Bon Iver |

**Bad:** "a sad song"
**Good:** "dark trap soul with raspy male vocals, heavy 808 sub-bass, atmospheric pads, intimate"

The LM planner generates lyrics automatically from the caption. For lyrical control, include section-tagged lyrics (see ACE-Step docs for [Verse], [Chorus] format).

## Integration with RIVSOL Music Project

For the RIVSOL project (RIVEN + SOLA artist profiles), the workflow is:

1. DSL notation → natural language caption (ACE-Step doesn't use Suno DSL)
2. Artist parameters (BPM, key, vocal style) embedded in caption text
3. API call with `max_tokens=240` for ~2min songs
4. Save output to `~/RIVSOL/outputs/`
5. Post-generation: LoRA training for consistent artist voice (requires 8+ songs per artist)

RIVEN preset caption template:
```
trap soul, dark and intimate, raspy male vocals with sung-rap delivery, heavy 808 sub-bass heartbeat, atmospheric pads, distorted 808 slides, 72 BPM, D minor
```

SOLA preset caption template:
```
alternative R&B, warm and ethereal, silky breathy female vocals, Rhodes/Wurlitzer piano, warm bass, soft drums, 74 BPM, F minor
```
