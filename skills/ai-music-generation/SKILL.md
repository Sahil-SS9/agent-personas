---
name: ai-music-generation
description: "Research, evaluate, set up, and use AI music generation tools — both cloud (Suno) and self-hosted open-source (ACE-Step, YuE, MusicGen). Covers licensing, hardware requirements, commercial use rights, and creating an 'artist' persona for distribution."
version: 1.0.0
license: MIT
---
# AI Music Generation — Research & Setup

## Overview

AI music generation has two main paths:
1. **Cloud services** (Suno, Udio) — highest quality, subscription cost, commercial tiers
2. **Self-hosted open-source** (ACE-Step 1.5, YuE) — free, unlimited, full ownership, but lower quality than latest Suno

## Cloud: Suno

### Current State (v5.5, March 2026 ToS)
- **Explore page** (suno.com/explore): Staff Picks, Best of v5.5, trending creators, remix culture
- **Key features**: Text-to-Music, Studio (multi-track), Hooks (short clips), Labs (experimental), Voice Model (your own voice), Covers, Suno Chat (AI assistant in UI)
- **Models**: currently on v5.5

### Commercial Rights
From help.suno.com (article 2410177):
- **Free plan**: Non-commercial only — cannot monetize, no retroactive licensing
- **Pro (~$10/mo)**: Full commercial rights — distribute to Spotify, Apple Music, YouTube, TikTok, X
- **Premier (~$30/mo)**: Full commercial rights — higher monthly song limit
- **Attribution**: NOT required (but appreciated)
- **Critical**: You must own 100% of the material (lyrics, samples). Cannot monetize others' IP.

### Artist Workflow (Cloud)
```
Suno Pro ($10/mo) → Generate songs → DistroKid ($23/yr) → Spotify/X/Apple Music
```

## Self-Hosted: ACE-Step 1.5 (PRIMARY — MIT License)

### Overview
- **11.3k ⭐ GitHub**, MIT license, actively maintained (last commit: April 2026)
- **Architecture**: Hybrid LM (Qwen3-based planner) + DiT (audio decoder)
- **Models**: 2B DiT or 4B XL DiT + 0.6B/1.7B/4B LM options
- **Quality**: Between Suno v4.5 and v5 — commercial-grade
- **Speed**: <10s per song on RTX 3090, <2s on A100

### Hardware Requirements
| VRAM | Config | Backend |
|---|---|---|
| ≤6GB | 2B turbo, DiT only, INT8+CPU offload | — |
| 6-8GB | 2B turbo + 0.6B LM | PyTorch |
| 8-16GB | 2B sft/turbo + 0.6B/1.7B LM | vllm |
| 16-20GB | XL turbo + 1.7B LM (CPU offload) | vllm |
| 20-24GB | XL sft/turbo + 1.7B LM | vllm |
| ≥24GB | XL sft + 4B LM (best quality) | vllm |

**Confirmed on RTX 4070 Ti (12GB):** `acestep-v15-sft` + `acestep-5Hz-lm-1.7B` uses ~9.5GB VRAM during idle, leaving ~2.5GB headroom. sft config (50 steps) works; turbo (8 steps) for faster iteration.

### Key Features
- Text-to-music, cover generation, repaint/edit, stem separation
- Vocal-to-BGM conversion, multi-track layering
- LoRA training (one-click in Gradio, ~1 hour on 3090, 8 songs)
- REST API (port 8001), Gradio UI (port 7860), VST3 plugin
- 10 seconds to 10-minute song generation
- Multi-language lyrics (50+ languages)

### Practical Setup — Windows

#### Install
```bash
cd ~/Suno   # or your preferred directory
git clone https://github.com/ACE-Step/ACE-Step-1.5.git
cd ACE-Step-1.5
uv sync      # ~54s resolve, ~4s install, 125 packages incl PyTorch 2.7.1+cu128
```

#### Configure for Quality
```bash
cp .env.example .env
```
Edit `.env` to set:
```
ACESTEP_CONFIG_PATH=acestep-v15-sft
ACESTEP_LM_MODEL_PATH=acestep-5Hz-lm-1.7B
```

#### First Launch — Model Download
Models auto-download on first run with `ACESTEP_NO_INIT=false`:
```bash
ACESTEP_NO_INIT=false uv run acestep-api
# Downloads ~6GB total:
#   - DiT: 4.79 GB (model.safetensors)
#   - LM planner: 3.71 GB (model.safetensors)
#   - VAE/tokenizer: 1.33 GB
# Takes several minutes at ~100-130 MB/s
```

After download, server initializes LM tokenizer (~11s), loads DiT into VRAM (~9.5GB/12GB used on 4070 Ti), then serves on `localhost:8001`.

**Verify it's running:**
```bash
curl -s http://localhost:8001/health
# Expected: {"data":{"status":"ok","models_initialized":true,"llm_initialized":true}}
curl -s http://localhost:8001/v1/models
# Lists loaded model: "acestep/acestep-v15-sft"
```

#### Port Conflict Troubleshooting
Port 8001 may be held by a zombie process (common on Windows after failed starts):
```bash
# Find the offending PID
netstat -ano | grep :8001

# Kill it — try in order:
taskkill /PID <PID> /F
powershell -Command "Stop-Process -Id <PID> -Force"
# Wait 2 seconds, then verify:
netstat -ano | grep :8001
# If still LISTENING, the process may need a full reboot
```

### Generation Workflow

#### Via REST API (OpenRouter-compatible)
The API uses a chat-completions-style endpoint. The `content` field is the caption describing the music:

```python
import requests, base64

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [
        {"role": "user", "content": "trap soul, dark and intimate, raspy male vocals, 808 sub-bass, atmospheric pads, 72 BPM, D minor"}
    ],
    "max_tokens": 240  # controls generation duration
})

data = response.json()
meta = data['choices'][0]['message']['content']  # text metadata
audio_list = data['choices'][0]['message']['audio']  # list of audio URLs

# Audio comes as base64 data URL: data:audio/mpeg;base64,XXXX
audio_url = audio_list[0]['audio_url']['url']
b64_data = audio_url.split(',', 1)[1]
audio_bytes = base64.b64decode(b64_data)

with open("output.mp3", 'wb') as f:
    f.write(audio_bytes)
```

#### Caption Format Best Practices
Cover these dimensions:
- **Genre**: trap soul, lo-fi, synthwave, indie folk, etc.
- **Emotion**: dark, melancholic, uplifting, dreamy, intimate
- **Instruments**: 808 sub-bass, atmospheric pads, fingerpicked guitar, strings
- **Vocal style**: raspy male vocal, breathy female vocal, falsetto, spoken word
- **BPM**: 72, 128, 140 etc. (note: LM may reinterpret BPM)
- **Key**: D minor, F minor, C major, etc.

The LM planner handles lyrics automatically in Simple Mode. For lyrical control, pass lyrics in section-tag format:
```
[Verse 1]
Walking down the street today

[Chorus]
I'm moving on, I'm staying strong
```

#### LM BPM Interpretation Note
The 1.7B LM sometimes reinterprets the requested BPM. For example, "72 BPM" in the caption may result in a different BPM in the generated metadata (tested: returned 190-300 BPM). The key (e.g. D minor) and mood are reliably preserved. The audio duration matches `max_tokens` × ~0.53 seconds/token.

### Artist Workflow (Self-Hosted)
```
ACE-Step local (MIT, free) → REST API → Python script posts to X
   ↓
LoRA train on 8 songs → consistent "artist" style
```

For structured style-to-song pipelines, create per-artist skills (e.g. `acestep-riven`, `acestep-sola`) that encapsulate the DSL→caption conversion and preset parameters.

## Self-Hosted: YuE (SECONDARY — Non-Commercial License)

- **License**: CC BY-NC 4.0 (cannot monetize)
- **Architecture**: 7B Stage 1 + 1B Stage 2
- **VRAM**: 12-16GB minimum
- **Speed**: ~4 min for 30s on RTX 4090 (slow)
- **Strengths**: Lyrics-to-full-song with vocals, In-Context Learning with audio prompts
- **Weaknesses**: Non-commercial license, much slower than ACE-Step

## Other Models (Lower Priority)

### MusicGen (Facebook AudioCraft)
- MIT licensed, instrumental only, stale (last commit 2024)
- Well below Suno quality, slow inference

## General Workflow: Creating an "Artist" Persona

1. **Define the sound**: Genre, instruments, mood, vocal style, gender
2. **Generate a batch**: Minimum 10-20 songs to establish consistency
3. **Train a LoRA** (ACE-Step only): 8 songs, ~1 hour, creates a consistent voice/style
4. **Distribute**: Use DistroKid / TuneCore / CD Baby to get on Spotify, Apple Music
5. **Promote on X**: Post clips with audio, link to full song
6. **Automate**: ACE-Step REST API + X API = cron-driven music bot

## Pitfalls
- **Free Suno songs CANNOT be retroactively licensed** — subscribe BEFORE generating commercial songs
- **YuE is CC BY-NC** — cannot monetize; verify license before using in any commercial workflow
- **ACE-Step quality vs Suno**: ACE-Step is between v4.5-v5, NOT at v5.5 level yet
- **Multiple llama-server instances** exhaust RAM — don't run ACE-Step alongside heavy LLM inference on the same GPU

## References
See `references/` directory in this skill for detailed model specs, benchmarks, and session research.

## Related Skills
- `local-llm-management` — for GPU memory management when running alongside LLMs
