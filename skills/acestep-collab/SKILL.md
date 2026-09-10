---
name: acestep-collab
description: "RIVSOL collab generation — RIVEN × SOLA duet, call-and-response chemistry"
version: 1.0.0
license: MIT
---
# ACE-Step — RIVSOL Collab Generation

Generate RIVSOL duet songs (RIVEN × SOLA) locally via ACE-Step.

**Prerequisites:** `acestep-music-generation` skill loaded (for API basics).

## Collab Default Parameters

| Parameter | Value |
|-----------|-------|
| **BPM** | 73 (compromise between RIVEN's 72 and SOLA's 74) |
| **Key** | E♭ minor (between RIVEN's Dm and SOLA's Fm) |
| **Genre** | trap soul duet, alternative R&B |
| **Concept** | Two perspectives on the same distance — push-pull chemistry |
| **Duration** | ~160s for full duet structure (max_tokens=300) |

## Collab Caption Template

```
trap soul duet, alternative R&B, male and female vocals trading verses, 
call-and-response chorus, 808 sub-bass, atmospheric pads, warm Rhodes piano, 
73 BPM, E-flat minor, push-pull chemistry, two perspectives on the same distance
```

## Collab Lyric Structure (Dual Vocal)

```
[Intro - atmospheric, both voices layered]
[Verse 1 - RIVEN: dark, sung-rap, introspective]
[Verse 2 - SOLA: soft, ethereal, answering]
[Pre-Chorus - both, building tension]
[Chorus - SOLA lead, RIVEN harmony underneath]
[Verse 3 - RIVEN: more vulnerable]
[Bridge - both interweaving, emotional peak]
[Chorus - full duet, biggest moment]
[Outro - fading together]
```

## Example API Call

```python
import requests, base64

caption = """trap soul duet, alternative R&B, male and female vocals trading verses, 
call-and-response chorus, 808 sub-bass, atmospheric pads, warm Rhodes piano, 
73 BPM, E-flat minor, push-pull chemistry"""

lyrics = """[Verse 1 - RIVEN]
Half the distance, I've been running in place
Got your number saved but I never press play
[Verse 2 - SOLA]
Half the distance, I've been waiting right here
Same address, same fears, same mirror
[Chorus - Both]
We're standing at the edge of maybe
Half the distance from saving me"""

prompt = f"{caption}\n\n{lyrics}"

response = requests.post("http://localhost:8001/v1/chat/completions", json={
    "model": "acestep/acestep-v15-sft",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 300
})

# Save all variations
data = response.json()
for i, a in enumerate(data['choices'][0]['message'].get('audio', [])):
    b64 = a['audio_url']['url'].split(',', 1)[1]
    with open(f"rivsol-output-v{i+1}.mp3", 'wb') as f:
        f.write(base64.b64decode(b64))
print("RIVSOL collab track(s) saved!")
```

## Output Naming Convention

Save to `~/RIVSOL/outputs/` with pattern: `rivsol-{song-name}-{variant}-{date}.mp3`

## Dual Vocal Tips for ACE-Step

ACE-Step handles vocal separation via section tags. Label who sings what:
```
[Verse - male vocal]
[Chorus - female vocal]
[Bridge - duet]
```

The caption should describe both vocal styles so the model doesn't blend them into one. Be explicit:
- "male and female vocals trading verses"  
- "call-and-response duet"
- "male verse, female chorus"
