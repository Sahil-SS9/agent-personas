---
name: "trace-replay-diagnosis"
description: "Read the agent run from its trace: walk the span tree call by call, replay the failing step, and let the trace — not the summary — name the failure."
license: "MIT"
---
# Trace-Replay Diagnosis

## Use when
- An agent run failed, silently or loudly, and "why" is the question.
- The final message and the actual behaviour disagree.
- Someone proposes a fix from a description of the run.

## Instructions

1. Get the full trace of the failing run — every model call, tool call,
   retrieval and sub-agent spawn, with arguments and outputs. Semantic
   agent failures fire no error status: a run that "completed" with a wrong
   answer looks clean everywhere except in its trace.
2. Walk the tree: the agent invocation is the root; each model call, tool
   execution and child spawn is a node. Follow the standard agent-span
   naming (agent invocation, tool execution, retrieval, generation) so
   traces stay comparable across runs and frameworks.
3. Replay the failing step in isolation: same inputs, same context slice,
   same tools. A defect that reproduces in isolation is fixable; a defect
   that only reproduces inside the whole run is a context or state failure —
   different seam, different fix.
4. Read the payload, not the status: high-cardinality fields (trace ids,
   tool arguments, user session) carry the actual evidence; rolled-up
   metrics and sampled traces delete exactly the evidence being hunted.
   Export full traces for the cases under review; sample only the ones you
   are not looking at.
5. Find the divergence point: the first node where behaviour left the
   intended path. Everything before it is context; everything after it is
   consequence. The fix lands at the divergence point, not at the symptom.
6. Write the finding as a replayable story: inputs → node-by-node what
   happened → divergence node → why the rest followed. A trace finding that
   another engineer cannot follow is not a finding.

## Stop conditions
- Never diagnose from the final message alone.
- Never fix a sampled or partial trace.
- Never fix downstream of the divergence point.

## Escalation
- Missing instrumentation (no trace, or spans that hide arguments) is itself
  the first finding: fix the instrumentation, reproduce, then diagnose.
