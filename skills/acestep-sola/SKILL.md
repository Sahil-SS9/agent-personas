---
name: acestep-sola
description: "SOLA-style music generation — alt R&B/neo-soul, warm, 74 BPM, F minor, silky breathy female vocals"
version: 1.0.0
license: MIT
---
# ACE-Step — SOLA Style Generation

Generate SOLA songs locally via ACE-Step. Artist preset: alt R&B / neo-soul with silky breathy female vocals.

**Prerequisites:** `acestep-music-generation` skill loaded (for API basics).

## SOLA Default Parameters

| Parameter | Value |
|-----------|-------|
| **BPM** | 74 |
| **Key** | F minor |
| **Genre** | alt R&B, neo-soul, dreamy pop |
| **Vocal** | silky breathy female vocal, runs, airy upper register |
| **Instruments** | warm Rhodes/Wurlitzer, soft 808s, lush strings, gentle hi-hats |
| **Vibe** | ethereal, warm, self-discovery, emotional arrival |
| **Duration** | ~128s (max_tokens=240) |

## SOLA Caption Template

```
alt R&B, neo-soul, warm and ethereal, silky breathy female vocals with runs, 
Wurlitzer electric piano, soft 808 sub-bass, lush string pads, gentle hi-hats, 
74 BPM, F minor, intimate and radiant, self-discovery theme
```

## SOLA Lyric Structure

```
[Intro - ethereal, wordless vocals]
[Verse 1 - soft, intimate]
[Pre-Chorus - swelling]
[Chorus - radiant, full]
[Verse 2 - more confident]
[Bridge - vulnerable, stripped to piano]
[Chorus - biggest emotional peak]
[Outro - fading into warmth]
```

## Example API Call

```python
import requests, base64

caption = """alt R&B, neo-soul, warm and ethereal, silky breathy female vocals, 
Wurlitzer electric piano, soft 808 sub-bass, lush string pads, 74 BPM, F minor"""

lyrics = """[Verse 1]
Softest place to fall is right here in your arms
Didn't know I needed shelter from my own storms
[Chorus]
I'm learning how to let the light in
Letting go of everything I've been holding"""

prompt = f"{caption}\n\n{lyrics}"

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 240
})

audio = response.json()['choices'][0]['message']['audio'][0]
b64 = audio['audio_url']['url'].split(',', 1)[1]
with open("sola-output.mp3", 'wb') as f:
    f.write(base64.b64decode(b64))
print("SOLA track saved!")
```

## Output Naming Convention

Save to `~/RIVSOL/outputs/` with pattern: `sola-{song-name}-{date}.mp3`

## SOLA Texture Keywords

Use these in captions for specific textures:
- **Warmth:** Wurlitzer, Rhodes, felt piano, tape saturation
- **Space:** reverb tails, delay throws, wide stereo
- **Vocals:** double-tracked, layered harmonies, breathy, head voice
- **Rhythm:** halftime feel, swung hi-hats, soft kick
