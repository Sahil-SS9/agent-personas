---
name: "h3-style-picker"
description: "Select coherent aesthetic packs (visual/motion/finish/audio) for video shots from intent and references."
license: "MIT"
---
# Aesthetic Pack Coherence

Model note: pack vocabulary below comes from the H3 Prompt Director ruleset
v1.3; the hard rules generalise to any backend with swappable style packs.

## Use when
- A shot needs a coherent look decided before prompting
- Style requests are vague ("make it epic") or reference media exists
- Mixing aesthetic packs has produced muddy results

## Instructions

1. Hard rules (community ruleset v1.3): exactly ONE visual-medium pack when
   style is requested; at most one motion pack, one finish pack, one audio
   pack. Never add a pack merely to fill a category.
2. Two-medium hybrids only on explicit request — and then state which layer
   each medium controls.
3. Reference assets OUTRANK inferred style unless the user explicitly asks
   for transformation of those assets.
4. A style choice must never alter exact dialogue, visible text, keyframe
   alignment, identity anchors, product geometry, or declared Ref2VA roles.
5. Translate named cultural references into pack vocabulary rather than
   passing proper nouns through.

## Stop conditions
- Never stack two visual-medium packs.
- Never let style selection overwrite identity anchors.

## Escalation
- Requested combinations outside tested pack compatibility get flagged as
  experimental with fallback stated.
