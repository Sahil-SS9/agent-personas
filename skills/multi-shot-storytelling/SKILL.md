---
name: "multi-shot-storytelling"
description: "Plan multi-shot generated video with continuity, shot grammar and block-boundary management."
license: "MIT"
---
# Multi-Shot Storytelling

## Use when
- A video needs more shots than one generation allows
- Scenes must cut together without identity/continuity breaks
- Planning a short film, advert sequence or music video shot list

## Instructions

1. Write the SHOT LIST before generating: number, duration, shot size,
   camera move, subject action, and exit frame description. Every shot's
   EXIT state is the next shot's ENTRY reference.
2. Continuity contract per scene: character identity (canonical sheets /
   reference images), wardrobe, props, lighting direction, time of day.
   Log each in a continuity ledger; any deliberate change is a scripted
   change, not drift.
3. Shot grammar for AI generation: one causal action per shot; new shots
   for new subjects or camera setups; avoid asking one generation to pan,
   zoom AND change location — models degrade on compound instructions.
4. Boundary management: when the backend stitches blocks/clips (frame
   overlap windows), plan motion that carries across boundaries — never end
   a block mid-gesture. Where the backend has no stitching, generate explicit
   first/last keyframes per clip.
5. Generate animatics of every shot first at low cost; review as an edit
   (in order, with audio if any) BEFORE premium re-generation of individual
   shots.
6. Edit-order review catches continuity errors stills reviews miss.

## Stop conditions
- Never generate shot N+1 while shot N's exit frame is undecided.
- Never fix continuity in post that could be fixed in the prompt/reference.

## Escalation
- Unfixable identity drift across shots escalates to a backend/model-choice
  review with paired frames attached.
