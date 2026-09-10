---
name: acestep-riven
description: "RIVEN-style music generation — trap soul, dark noir, 72 BPM, D minor, sung-rap male vocals"
version: 1.0.0
license: MIT
---
# ACE-Step — RIVEN Style Generation

Generate RIVEN songs locally via ACE-Step. Artist preset: dark trap soul / R&B with sung-rap delivery.

**Prerequisites:** `acestep-music-generation` skill loaded (for API basics).

## RIVEN Default Parameters

| Parameter | Value |
|-----------|-------|
| **BPM** | 72 |
| **Key** | D minor |
| **Genre** | trap soul, dark R&B, sung-rap |
| **Vocal** | raspy male vocal, sung-rap delivery |
| **Instruments** | 808 sub-bass, atmospheric pads, tight hi-hats, pitched snare rolls |
| **Vibe** | late-night introspection, dark, intimate, nocturnal |
| **Duration** | ~128s (max_tokens=240) |

## RIVEN Caption Template

```
trap soul, dark and intimate, raspy male vocal with sung-rap delivery, 
heavy 808 sub-bass, atmospheric synth pads, tight hi-hats, pitched snare rolls, 
72 BPM, D minor, late-night introspective, raw and vulnerable
```

## RIVEN Lyric Structure

```
[Intro - atmospheric, spoken]
[Verse 1 - sung-rap flow]
[Pre-Chorus - building tension]
[Chorus - melodic hook]
[Verse 2 - more intense delivery]
[Bridge - vulnerable, stripped back]
[Chorus]
[Outro - fading, whispered]
```

## Example API Call

```python
import requests, base64

caption = """trap soul, dark and intimate, raspy male vocal with sung-rap delivery, 
heavy 808 sub-bass, atmospheric synth pads, tight hi-hats, 72 BPM, D minor"""

lyrics = """[Verse 1]
City never sleeps but I ain't been asleep in weeks
Shadows on the wall talkin' secrets that I keep
[Chorus]
I'm still wearing black for you
Ain't nothing new, just the same old shade of blue"""

prompt = f"{caption}\n\n{lyrics}"

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 240
})

# Save output
audio = response.json()['choices'][0]['message']['audio'][0]
b64 = audio['audio_url']['url'].split(',', 1)[1]
with open("riven-output.mp3", 'wb') as f:
    f.write(base64.b64decode(b64))
print("RIVEN track saved!")
```

## Output Naming Convention

Save to `~/RIVSOL/outputs/` with pattern: `riven-{song-name}-{date}.mp3`

## Energy Arc (ACE-Step Caption)

Unlike Suno DSL, ACE-Step captions use natural language. Translate energy arc into emotion words:
- **Intro:** atmospheric, sparse, whispered
- **Verse 1:** intimate, building
- **Chorus:** full, anthemic, emotional peak
- **Bridge:** stripped back, vulnerable
- **Outro:** fading, dissolving
