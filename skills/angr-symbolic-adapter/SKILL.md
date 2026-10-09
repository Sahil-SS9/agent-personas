---
name: "angr-symbolic-adapter"
description: "Use angr for symbolic analysis when evidence needs justify it: constraint solving on parsers, decoders and guarded paths, with coverage honesty."
license: "BSD-2-Clause"
---

# angr symbolic adapter

angr turns guarded code paths into constraint problems: recover decoders, enumerate reachable states, find inputs that reach a target. A scalpel, not a default ritual. (Adapter structure original; angr is third-party tooling referenced, not embedded.)

## When to use
When a written question justifies it — e.g. what input reaches a forbidden branch, or what a transformation routine decodes — and static reading alone stalls. Requires: angr available, artefact arch supported, explicit budget agreed.

## Procedure
1. Frame the symbolic question before scripting: the target (address/state), the constraints that matter, the budget (time/steps). Record both; a solver run without them is noise.
2. Prepare the state deliberately: correct base address, initialised registers/memory, avoided paths (e.g. anti-analysis or abort branches) chosen from static reading — the avoidance choices are assumptions and are recorded.
3. Read results as evidence with limits: solver "not found" is not coverage proof; timeout is not safety; a found input is a witness to be verified by execution/emulation, not a conclusion.
4. Prefer symbolic execution of small, well-understood routines (decoders, checksums, guards) over whole-program exploration; whole-program runs get explicit timeboxes and coverage accounting.
5. Feed findings back to the static loop: recovered transformations become retypeable data or callable signatures.

## Decision rules
- Solver completion time or status never substitutes for coverage measurement; report both.
- Found inputs are verified before becoming findings (the verification member owns that step).

## Pitfalls
- Fighting path explosion in loops/parsers with bigger budgets instead of better boundaries.
- Presenting "no input found" as "input cannot exist".

## Done
A scripted run with recorded question/budget/assumptions, witnesses or bounded negative results, and coverage notes.