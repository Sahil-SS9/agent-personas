---
name: experimental-suno-songcraft
description: "Create experimental/non-branded Suno songs from raw style descriptions — no artist DNA profiles needed. DSL + lyrics production pipeline with character-count verification."
version: 1.0.0
license: MIT
---
# Experimental Suno Songcraft

For creating songs **without** artist branding profiles (RIVEN/SOLA). Pure style-to-DSL pipeline for standalone experimental tracks.

## When to use this

The user shares raw style descriptions (from Suno clips, inspiration boards, or their own writing) and wants a full song built from them — no pre-existing artist brand or persona.

## Workflow

### 1. Extract the sonic DNA
When the user provides style blocks, identify these dimensions across all shared styles:

- **Vocal type** — male/female, sung/rapped, filtered or present, breathy or chest
- **Atmosphere** — nocturnal, neon, intimate, euphoric, cold, warm
- **Foundation** — 808s, sub-bass, percussion type, hats, kick pattern
- **Production FX** — reversed vocals, glitch edits, reverb tails, stereo movement
- **Dynamic pattern** — filtered verse → open chorus, build-drop, sustained float
- **Structural elements** — intro, bridge, breakdown, silence drops

### 2. Discuss themes first
Before writing anything, talk through:
- Subject matter / emotional core
- Perspective (who is singing, to whom)
- Tense (past/present/future — makes a big difference to lyric emotion)
- Whether the song tells a story or creates a vibe

**Key questions to ask before drafting:**
- "Is he still in it or looking back?" (changes tense and emotional weight)
- "Is this storytelling or atmosphere?" (determines lyric density vs sparse repetition)
- "Does the emotional arc match the music arc?" (verse→chorus feeling should align with DSL energy)

### 3. Build the DSL block (≤1,000 chars)
Use the DSL cheatsheet (`skill_view(name='songwriting-and-ai-music', file_path='references/suno-dsl-cheatsheet.md')`) to write the energy arc.

**Character count is a hard limit.** Suno's Style field accepts ≤1,000 characters. Always verify before presenting.

Compression rules when over:
- Merge L0+L1 (extended intro ambient) into one line
- 2-5 texture words per layer, not full sentences
- Front-load notation, back-load plain English
- Condense the final genre tag line — BPM, key, genre, and one mood word is usually enough

### 4. Write lyrics
Load `songwriting-and-ai-music` for craft guidance. Load `humanizer` for wording assistance — especially to avoid AI-isms in natural-language lyrics.

**Metatags:** Reference DSL layers in lyric section headers:
```
[Verse 1 — L1, $b=0$, filtered]
[Chorus — L3, room opens]
```

### 5. Present as a package
Each song gets:

```
**Title**

DSL Style (Paste into Style field):
<dsl block>

Lyrics:
<section tags and lyrics>
```

## Relationship to other skills

- `songwriting-and-ai-music` — provides foundational craft (prosody, rhyme theory, object writing)
- `humanizer` — strips AI-isms from lyric wording
- `acestep-riven` / `acestep-sola` — use those when the user IS writing for a branded artist persona
- This skill fills the gap: non-branded, experimental, vibe-first song creation

## Pitfalls

- **DSL length exceeds 1,000 chars** — always count before presenting. The user will catch it. Compress before their first read.
- **Too many choices too early** — don't present 3+ options for every decision. Ask one question at a time about the thing that matters most (theme > structure > BPM).
- **Lyrics sound AI-generated** — run through humanizer before final presentation. Watch for: excess em dashes, synonym cycling, rule-of-three constructions, "let's dive into," verbless fragments.
- **Over-explaining the DSL** — present the block as-is for Suno copy-paste. Don't paraphrase it unless the user asks what it means.