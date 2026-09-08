---
name: "story-slicing"
description: "Split features into thin, vertical, INVEST-shaped stories that deliver value."
license: "MIT"
---
# Story Slicing

## Use when
- A story resists estimation ("that's a quarter's work")
- Slices came out as technical layers (frontend/backend/database)
- Acceptance criteria are unwritable because scope is too fat

## Instructions

1. Slice vertically: each story walks through the whole stack for a thin
   user-visible capability — never split by architectural layer.
2. Use slicing patterns when stuck: workflow steps, business rules,
   data variations, interface variations, spike-then-build.
3. Run INVERTED-INVEST triage: valuable (user-visible outcome?) and
   testable (writable acceptance criteria?) catch most bad slices;
   independent/negotiable/estimable/small complete the check.
4. Name the OUTCOME per slice: which user behaviour should change and how
   you'd observe it (Perri/Seiden outcome-over-output rule). A slice with
   no observable behaviour change is a layer in disguise.
5. Write acceptance criteria as examples where shared understanding
   matters (Specification-by-example habit).

## Stop conditions
- Never mark 'ready' a slice without acceptance criteria.
- Never accept a horizontal-layer story as done-value.

## Escalation
- Features that cannot be sliced after honest attempts go back to the PM
  persona — the problem may be the scope, not the slicing.
