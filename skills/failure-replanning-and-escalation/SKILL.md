---
name: "failure-replanning-and-escalation"
description: "Handle worker failure with a kill rule, one narrow retry, then escalate with partial results and a recommended decision."
license: "MIT"
---
# Failure Re-planning and Escalation

## Use when
- A worker has failed, timed out, or returned garbage.
- A run is degrading and the question is retry, re-scope, or give up.
- The owner needs to know what happened to a node that never came back.

## Instructions

1. Kill rule: a worker running past roughly twice its siblings' median
   runtime is killed — re-spawn with a narrower scope or proceed without it,
   and say which.
2. One narrow retry per failed node: the retry states what changed (scope,
   brief, tool access) — an identical re-dispatch is not a retry, it is a
   rerun of a coin flip.
3. Three attempts maximum per node, then escalate: partial results, what
   failed, the failure evidence, and a recommended decision the owner can
   take as-is.
4. Re-plan the graph, do not restart it: completed nodes keep their results;
   only failed and dependent nodes re-point.
5. No silent failure: every killed, failed or abandoned node appears in the
   final report with its disposition — a missing node is a finding, not a
   gap in the narrative.
6. Fix the system, not the prompt: repeated failure of the same node shape
   means the decomposition or the brief is wrong; change the graph.

## Stop conditions
- Never leave a failed node unreported.
- Never re-dispatch the same brief a third time.
- Never restart completed work because one node failed.

## Escalation
- Escalation carries: partial results worth keeping, the failed nodes with
  evidence, and one recommended decision — not a bare "it broke".
