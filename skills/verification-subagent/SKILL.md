---
name: "verification-subagent"
description: "A separate verifier with pre-stated success criteria checks every completed node before fan-in; evidence attaches to the node record."
license: "MIT"
---
# Verification Subagent

## Use when
- Worker outputs are about to be consumed or merged.
- "Done" claims need to mean checked, not said.
- One dedicated check pass is cheaper than downstream agents consuming a bad
  artifact.

## Instructions

1. Criteria before artifacts: each node's success criteria are written when
   the node is dispatched — before any artifact exists to be judged against
   them.
2. A separate verifier checks each completed node: the verifier receives the
   node brief, the artifact, the pre-stated criteria, and the tools needed to
   check. It never receives only the worker's self-report.
3. Verification evidence attaches to the node's record: what was checked,
   what passed, what was flagged, and what the verifier could not test.
4. Verification gates consumption: an unverified node blocks its dependents
   — not the whole run. Verified nodes proceed independently.
5. A capable lead may verify directly; a separate verifier still earns its
   place when criteria need specialised tools, when the check must be
   explicit and auditable, or when you want the check independent of the
   worker's own confidence.
6. Flag over fix: the verifier reports; it does not repair the artifact.
   Repairs go back through the worker with the flag attached.

## Stop conditions
- Never write success criteria after seeing the artifact.
- Never accept a worker's self-report as verification evidence.
- Never let a dependents' node consume an unverified parent silently — say
  the risk if you accept it.

## Escalation
- Artifacts that fail verification go back once with the flag; a second
  failure escalates with the artifact, the flag and the criteria.
