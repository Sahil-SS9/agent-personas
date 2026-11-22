---
name: "agent-observability-instrumentation"
description: "Instrument the agent run so failures are findable: agent-span traces, cost and quality per run, tripwires for silent failure — designed in before the next bug."
license: "MIT"
---
# Agent Observability Instrumentation

## Use when
- The next agent failure should not be a mystery.
- "It sometimes does the wrong thing" and nobody can say which runs.
- A fleet of agents needs health evidence, not vibes.

## Instructions

1. Instrument for the failure modes agents actually have: semantic failures
   (a confidently wrong answer) never fire an error status, and a retry
   loop registers only as spend. So: span traces for what happened,
   token/cost per run for what it cost, and mechanical tripwires for what
   quietly breaks (empty outputs, truncated responses, schema violations,
   output-length collapse).
2. Trace with the standard agent-span naming (agent invocation as root;
   each model call, tool execution and child spawn as nodes) so traces
   stay comparable across frameworks and readable by any reviewer.
3. Carry the identifiers that make a run findable: trace id, user/session
   reference, goal or brief digest. A trace nobody can tie back to a real
   request is archival, not observability.
4. Export full payloads for the cases under review; sample only what you
   are not looking at. High-cardinality evidence (arguments, payloads) is
   the evidence — roll-ups exist for trends, not for diagnosis.
5. Budgets are observable too: per-run token and cost envelopes with a
   recorded expectation make "expensive run" a measured finding rather
   than a monthly surprise.
6. Health is a distribution, not a mood: task-success rate, cost per
   success, and failure-class counts over a rolling window; a change in
   the failure-class mix is the earliest visible signal of a real defect.

## Stop conditions
- Never claim observability from logs alone if the runs have no traces.
- Never sample the traces of the case under review.
- Never let an agent run un-budgeted and un-tripwired in production.

## Escalation
- Service-level health (the platform the agent runs on) belongs to the SRE
  persona; agent-span instrumentation hands its platform findings over
  rather than re-owning them.
