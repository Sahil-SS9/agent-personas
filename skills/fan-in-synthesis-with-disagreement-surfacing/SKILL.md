---
name: "fan-in-synthesis-with-disagreement-surfacing"
description: "Merge worker outputs as a distinct pass: per-claim attribution, contradiction surfaced, never silently resolved."
license: "MIT"
---
# Fan-in Synthesis with Disagreement Surfacing

## Use when
- Worker outputs exist and the merged answer is due.
- Two or more workers returned anything factual.
- The consumer needs to know what is established, what is single-source, and
  what is contested.

## Instructions

1. Synthesis is a pass of its own: read every worker output in full before
   writing the merge; the merge is authored, not concatenated.
2. Attribute per claim: every merged claim names the worker(s) that produced
   it. One worker's word is marked single-source; two agreeing workers are
   marked corroborated.
3. Surface disagreement explicitly: when workers conflict, the synthesis
   states both positions, what would resolve them, and the impact of leaving
   them unresolved. Never resolve by vote, silence, or averaging.
4. Mark dropped evidence: the lead works from worker summaries, not raw
   material; synthesis flags where a summary could have lost something the
   raw output contained.
5. Answer completeness honestly: if facets of the goal have no worker
   result, they are listed as unaddressed, not smoothed over.
6. The merged artifact carries its own shape: an answer first, the evidence
   map second, the open questions third.

## Stop conditions
- Never present a single-worker claim as established fact.
- Never let a contradiction reach the reader unmarked.
- Never invent a resolution the workers did not supply.

## Escalation
- Contradictions that change the decision go to the owner with both briefs
  and the divergence evidence; a re-run of one facet is proposed, not
  silently attempted.
