---
name: "verification-subagent"
description: "A separate verifier with pre-stated success criteria checks completed nodes before fan-in; evidence attaches to the node record."
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
2. Verification depth follows the node's risk tier, set at dispatch.
   Anything that feeds a merge, a release or an external action gets a
   separate verifier: it receives the node brief, the artifact, the
   pre-stated criteria and the tools needed to check, never only the
   worker's self-report. A low-risk node may be spot-checked by a capable
   lead, who records what was checked. A check that needs specialised
   tools, must be auditable, or must be independent of the worker's own
   confidence always goes to a separate verifier.
3. Verification evidence attaches to the node's record: what was checked,
   what passed, what was flagged, and what the verifier could not test.
4. Verification gates consumption: an unverified node blocks its dependents
   — not the whole run. Verified nodes proceed independently. Only the
   owner may accept an unverified parent into a dependent, and the
   acceptance, its reason and its risk are recorded on both node records.
5. Flag over fix: the verifier reports; it does not repair the artifact.
   Repairs go back through the worker with the flag attached.
6. A verifier return is a dispatch of the node under the shared attempt
   ledger in failure-replanning-and-escalation: the flag goes back once,
   and a second failure escalates with the artifact, the flag and the
   criteria.

## Stop conditions
- Never write success criteria after seeing the artifact.
- Never accept a worker's self-report as verification evidence.
- Never let a dependent consume an unverified parent without the owner's
  recorded acceptance.

## Escalation
- Artifacts that fail verification go back once with the flag; a second
  failure escalates with the artifact, the flag and the criteria.
