---
name: "storyboard-to-shots"
description: "Convert a story or script into sequential storyboard panels with generation-ready prompts."
license: "MIT"
---
# Storyboard to Shots

## Use when
- Turning a narrative, script or beat sheet into sequential images/video shots
- Panels drift off-model between frames
- Planning a comic strip, explainer sequence or short film

## Instructions

1. Break the story into beats first (goal, obstacle, turn, resolution per
   scene); each beat becomes one or more panels. Number them.
2. For every panel define: shot size (wide/medium/close), camera angle,
   subject pose/action, emotional beat, and continuity anchors (props,
   clothing, time of day carried from the previous panel).
3. Generate panels IN ORDER using the canonical character sheets as identity
   references; carry forward the previous accepted panel as an additional
   reference where continuity is critical.
4. Maintain a continuity ledger alongside the storyboard: what each panel
   must inherit from the last (position of objects, lighting direction,
   damage/state changes).
5. Review as a SEQUENCE before polishing individual panels — story clarity
   beats per-panel beauty.

## Stop conditions
- Never polish panel N+1 while panel N still breaks continuity.
- Never introduce a new prop/outfit mid-sequence without a ledger entry.

## Escalation
- Story beats that cannot be visualised cleanly go back to the writer with
  the specific ambiguity named.
