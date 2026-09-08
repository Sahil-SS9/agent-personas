---
name: "h3-audio-dialogue-syntax"
description: "Place audio content correctly in H3 prompts; master dialogue syntax and the quote rule."
license: "MIT"
---
# H3 Audio & Dialogue Syntax

## Use when
- Prompts involve speech, singing or sound design
- Burned-in subtitles appear when they shouldn't (or should)
- Ambient/score layers are missing or misplaced

## General principle

Wherever a video model generates audio, sound content splits into the same
three homes: shot-synced events live WITH the shot description, ambience
lives in a dedicated soundscape field, and audience-only score lives in its
own field. Misplacement is a silent failure on any such model.

Model note — MiniMax H3 concrete syntax:

## Instructions

1. Three-layer placement rule ([OFFICIAL]):
   - Dialogue/singing/shot-synced sound events -> main description field
   - Ambience/room tone/physical sounds (footsteps, rain) -> overall_soundscape (1-4 sentences)
   - Audience-only music -> non_diegetic_music (1-3 sentences)
   Wrong home = silent failure.
2. Dialogue syntax: <speaker description> (S1) says, <delivery description>,
   <d>[English] The spoken words.</d> — stable speaker IDs across shots.
3. THE QUOTE RULE [OBSERVED, independently confirmed]: quotation marks
   inside <d> tags render BURNED-IN SUBTITLES — quotes mean "print this text
   in the picture". For spoken-only lines use no quotes inside the tag;
   to force on-screen text, deliberately quote it.
4. Silence is an instruction: no music wanted means non_diegetic_music: N/A,
   not an empty field.

## Stop conditions
- Never leave soundscape empty on shots with physical action.
- Never mix score into soundscape or vice versa.

## Escalation
- Persistent subtitle ghosting despite correct syntax escalates with prompt
  + output pairs as a candidate model issue.
