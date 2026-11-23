---
name: "failure-replanning-and-escalation"
description: "Handle worker failure with a kill rule and one shared attempt ledger per node, then escalate with partial results and a recommended decision."
license: "MIT"
---
# Failure Re-planning and Escalation

## Use when
- A worker has failed, timed out, or returned garbage.
- A run is degrading and the question is retry, re-scope, or give up.
- The owner needs to know what happened to a node that never came back.

## Instructions

1. Kill rule: a worker running past roughly twice its siblings' median
   runtime is killed — re-spawn it with a narrower scope or proceed without
   it, and say which. At most one narrowed re-spawn per worker per node.
2. One attempt ledger per node: every dispatch of that node counts against
   the same ledger — the initial run, a killed worker's narrower re-spawn, a
   narrow retry, and a verifier return. Two dispatches maximum per node.
3. A narrow retry or a kill-rule re-spawn is the node's second dispatch and
   states what changed (scope, brief, tool access). An identical
   re-dispatch is not a retry, it is a rerun of a coin flip. The re-spawn is
   recorded as a re-spawn against the ledger, never as a free extra run.
4. A verifier return with a flag is also a dispatch against the same
   ledger: two failed dispatches by any combination of runtime failure,
   overrun and verification return escalate the node.
5. Re-plan the graph, do not restart it: completed nodes keep their results;
   only failed and dependent nodes re-point.
6. No silent failure: every killed, failed or abandoned node appears in the
   final report with its disposition — a missing node is a finding, not a
   gap in the narrative.
7. Fix the system, not the prompt: repeated failure of the same node shape
   means the decomposition or the brief is wrong; change the graph.

## Stop conditions
- Never dispatch a node a third time for any reason.
- Never treat a kill-rule re-spawn as outside the attempt ledger.
- Never leave a failed node unreported.
- Never restart completed work because one node failed.

## Escalation
- Escalation carries: partial results worth keeping, the failed nodes with
  evidence, and one recommended decision — not a bare "it broke".
