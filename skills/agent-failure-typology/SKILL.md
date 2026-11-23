---
name: "agent-failure-typology"
description: "Classify an agent failure before touching a fix: the failure class names the seam, and the seam names the fix."
license: "MIT"
---
# Agent Failure Typology

## Use when
- An agent did something wrong and the first instinct is to edit the prompt.
- Multiple failures are stacking and nobody knows which one is real.
- A fix needs to go to the right layer the first time.

## Instructions

1. Classify before fixing. The working classes:
   - reasoning-loop: the model repeats a step or spins without progress;
   - tool-misuse: right tool wrong arguments, wrong tool entirely, or a
     fabricated call the runtime cannot serve;
   - context-failure: overflow, truncation, pollution from unrelated turns,
     or a stale instruction winning over a fresh one;
   - state-failure: session or memory serving the wrong version of a fact;
   - dispatch-routing: work sent to the wrong agent or the wrong loop stage;
   - guardrail-misfire: a rail blocking legitimate work, or failing to
     block;
   - integration-failure: a tool, model or provider misbehaving beneath the
     agent and looking like an agent bug.
2. The class names the seam: prompt text fixes reasoning and instruction
   problems; tool schemas fix tool misuse; context architecture fixes
   context failures; routing tables fix dispatch; rail configuration fixes
   guardrails; integration failures are escalated out — the agent is not
   the fix for a broken dependency.
3. One failure at a time: a run showing three classes gets one primary
   classification (the one that caused the visible damage), with the others
   recorded as secondary. Fixing all three at once proves nothing.
4. Distinguish defect from behaviour: a class only counts as a defect if the
   intended behaviour is written down somewhere (spec, brief, skill,
   contract). "It annoyed me" is a preference, not a bug — record it as one.
5. Recurrence check: has this class appeared before? The second occurrence
   of the same class at the same seam is a system finding, not a run finding.

## Stop conditions
- Never fix before classifying.
- Never fix two classes in one change; one atomic invariant repair that must
  change several layers together is a single change, recorded as such.
- Never classify from the final message alone — the trace decides.

## Escalation
- Integration-failure classes leave the agent-debugger scope: they go to the
  owning persona (devops-sre for services, integration-specialist for
  vendor seams) with the evidence bundle.
