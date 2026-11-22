---
name: "trajectory-and-tool-call-eval"
description: "Evaluate agents from their trajectories: task success measured from tool calls, artifacts and side effects — not from the final answer's tone."
license: "MIT"
---
# Trajectory and Tool-Call Eval

## Use when
- The thing being evaluated is an agent run (tools, steps, artifacts), not a
  model answer.
- An agent "finished" and the question is whether the run actually achieved
  the task.
- Production traces need a quality check.

## Instructions

1. Judge the trajectory, not the prose: task success is measured from what
  the run DID — tool calls made and their arguments, artifacts produced or
  modified, side effects, and final state — never from how confident the
  final message sounds.
2. Define success as checkable claims before scoring: which calls should
   have happened, which files should exist, which invariants should hold.
   A run whose evidence is distributed across calls, logs and artifacts
   needs an inspection plan, not a single glance at the output.
3. Score the process failures separately from outcome failures: a right
   answer reached through a retry loop that burned extra calls is a cost
   finding; a wrong answer stated confidently is a correctness finding.
   Semantic failures fire no error status — only the trace shows them.
4. Reward-verified beats reward-guessed: prefer a grounded, verifiable
   reward (tests ran, file exists, state changed) over a judge's opinion of
   the transcript; use judges only for what cannot be checked mechanically,
   and calibrate them (see the judge skill).
5. High-cardinality payloads rule out sampling: a sampled trace deletes the
   evidence for the exact failure you are hunting; export full traces for
   the cases under review.
6. Aggregate honestly: report task-success rate, cost per success, and the
   distribution of failure classes — a single blended score hides the
   failure you most need to see.

## Stop conditions
- Never accept an agent's self-report of success as the measurement.
- Never score only the final message when tool evidence exists.
- Never sample the traces under review.

## Escalation
- Failure classes that dominate (one tool misused across cases) escalate as
  a capability defect with the trace bundle — the skill or tool changes, not
  the eval.
