---
name: "character-sheet-design"
description: "Build reusable character sheets that keep generated characters on-model across images."
license: "MIT"
---
# Character Sheet Design

## Use when
- A character must appear consistently across multiple generations
- On-model drift ruins a series, storyboard or brand asset
- Starting any illustrated/photographic recurring character

## Instructions

1. Define the identity contract BEFORE generating: name, age-range, build,
   hair (colour/cut/texture), eye colour, skin tone, distinctive marks
   (scars, moles, tattoos), signature outfit + props, palette anchors.
   Write it as a reusable prompt fragment.
2. Generate the canonical sheet: front / 3-quarter / profile turnarounds at
   neutral expression and lighting; then expression range (neutral, joy,
   anger, sorrow, surprise) on the best turnaround.
3. Lock reproducibility: record model version, exact prompt, seed, sampler
   and reference weights per canonical image. Regeneration = same contract
   + recorded parameters, not re-description from memory.
4. For cross-image consistency use the reference pattern (--cref-style):
   pass the canonical sheet as reference with weight tuned high enough to
   hold identity, low enough to allow pose/action variation.
5. Maintain a per-character ledger: every accepted generation logs its seed
   and prompt delta against the contract.

## Stop conditions
- Never accept a 'good enough' face into a series without a canonical sheet.
- Never regenerate identity-critical shots without consulting the ledger.

## Escalation
- Persistent drift that reference weighting cannot fix escalates to a
  model-choice review (different backend may hold identity better).
