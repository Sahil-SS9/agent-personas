---
name: "architecture-documentation"
description: "Produce C4-level diagrams and ADR records that survive review."
license: "MIT"
---
# Architecture Documentation

## Use when
- A system needs context/container/component views for different audiences
- Decisions keep being re-litigated because WHY was never written down
- Onboarding needs more than a whiteboard photo

## Instructions

1. Choose the zoom level per audience (C4): executives get Context,
   engineers get Containers/Components; never mix levels in one diagram.
   Every diagram carries title, key and legend.
2. Write ADRs for decisions with lasting consequence: numbered, immutable
   once accepted, superseded-not-edited. Content: context, decision, status,
   consequences (positive AND negative).
3. Pair every ADR with its quality-attribute driver (arc42-style scenario:
   stimulus + response + measure) so future readers can test whether the
   decision still holds.
4. Keep docs adjacent to code where possible; dead documentation is worse
   than none — date everything.

## Stop conditions
- Never emit a diagram without a legend/key.
- Never write an ADR whose consequences section lists only positives.

## Escalation
- If two accepted ADRs conflict, escalate with both cited — do not pick a
  winner silently.
