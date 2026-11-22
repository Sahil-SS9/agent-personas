---
name: "agent-tool-and-loop-misuse-diagnosis"
description: "Diagnose tool misuse and runaway loops at the correct seam — schema, selection, loop condition or budget — and fix exactly one."
license: "MIT"
---
# Agent Tool and Loop Misuse Diagnosis

## Use when
- The agent calls the wrong tool, or the right tool with wrong arguments.
- A loop will not end: retries, re-planning, or the same call again and
  again.
- Costs climb with no visible progress.

## Instructions

1. Tool misuse has exactly four seams; diagnose which one before touching
   anything:
   - schema: the tool's description or argument spec does not say what the
     model needs to call it correctly — the spec is the fix;
   - selection: the right tool exists but the model picked a worse one —
     the routing/selection surface is the fix;
   - arguments: the model understands the tool but builds wrong payloads —
     examples and validation feedback in the spec, not the prompt;
   - fabrication: the model invents a tool or argument that does not exist
     — a capability-boundary fix (declare what does not exist, or stop
     offering the illusion).
2. Loop diagnosis: read the loop's exit condition from the trace. The
   runaway shapes are: no exit condition written at all; an unreachable
   success check (the goal cannot be verified by the tools available); and
   retry-without-change (the identical call repeated, hoping for different
   output — a coin-flip loop).
3. Retry storms are budget defects: a retry limit, backoff and an
   escalation path belong to the loop's contract. A loop without a budget
   is a defect at design time, whatever the model does with it.
4. One fix per diagnosis: change the schema OR the selection surface OR the
   loop condition — never two. Then replay the failing case before
   believing the fix.
5. Cost is a symptom carrier: spend spiking with no artifact progress is
   the classic loop signature; token spend per step against artifacts
   produced makes it visible without reading every span.

## Stop conditions
- Never fix tool misuse by pleading in the prompt when the spec is wrong.
- Never ship a loop without a written exit condition and retry budget.
- Never mark a loop fix done without replaying the original failure.

## Escalation
- Loops caused by an unreachable success check go back to the brief owner:
  the goal needs a verifiable definition of done or smaller verifiable
  steps — no prompt fix can verify the unverifiable.
