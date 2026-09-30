---
name: "defence-surface-coverage-and-rail-placement"
description: "Map defences against every surface an agent touches and place each rail where the harm actually occurs, not where it is easiest to add."
license: "MIT"
---

# Defence surface coverage and rail placement

## When to use
Designing a guardrail estate, or reviewing whether existing rails sit in the right place.

## Procedure
1. Build the matrix: harms down one axis, surfaces across the other (input, retrieval, tool args, tool results, outbound, execution, egress).
2. Mark each cell covered, partially covered, or not covered. Not-covered cells are the work plan.
3. Trace a canary through the pipeline: exposed, persisted, relayed, executed. Record which step your rail actually stops.
4. For each rail, state the surface it reads, the surface it blocks, and the failure action.
5. Re-check composition: does a rail that is correct at each step still hold across steps?

## Decision rules
- Placement is a claim that must be falsifiable. If you cannot state which step a rail stops, it is not placed.
- Step-scoped monitors cannot detect violations that only exist compositionally across steps. Test for this explicitly.
- Prefer the earliest point that can decide correctly; a rail after the side effect is an audit log.
- A cell you mark covered needs execution evidence, not a configuration screenshot.

## Pitfalls
- Guardrailing the prompt while the retrieval path is unguarded.
- Claiming tool-call coverage from a text-only rail.
- Assuming that because every step is checked, the sequence is safe.

## Done
The map shows no silently-empty cells, and every rail names its read surface, block surface, failure action, and the canary step it stops.
