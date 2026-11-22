---
name: "agent-context-and-state-forensics"
description: "Forensically account for what the agent actually saw: full context reconstruction, truncation checks, and stale-state detection before blaming the model."
license: "MIT"
---
# Agent Context and State Forensics

## Use when
- The agent "ignored" an instruction, or answered from the wrong past.
- Output quality changed with no code change.
- Suspicion falls on context, memory or session state.

## Instructions

1. Reconstruct what the agent ACTUALLY saw: dump the full prompt/context
   window as served — not what was intended, what was delivered. The gap
   between the two is where most "model ignored it" findings die.
2. Check for the quiet killers, in order: truncation (did the tail of the
   window get cut?), silent compression (did a summariser drop the exact
   detail that mattered?), ordering (did a stale instruction outrank a
   fresh one by position?), and pollution (did unrelated turns ride along
   in the window and steer behaviour?).
3. Trace state to its source: for every fact the agent acted on, find where
   it came from — live session, retrieved memory, or invented. Stale state
   serving an outdated version of a fact is a state-pipeline defect, not a
   model defect.
4. Diff across the change window: when behaviour changed without a code
   change, diff what entered the context (retrieval results, memory writes,
   upstream payloads) before and after. The change is usually in the diff.
5. Measure the overflow boundary: record window size, content size and the
   fill order; a run that overflows at a certain conversation length will
   fail deterministically at that length — make the number known.
6. Attribute before fixing: context failures are fixed in the context
   architecture (what gets loaded, when, in what order, with what budget) —
   not by pleading harder in the prompt.

## Stop conditions
- Never conclude "the model ignored the instruction" without the delivered
  context in hand.
- Never treat silent truncation as acceptable behaviour.
- Never fix a state pipeline defect inside the prompt text.

## Escalation
- Memory- and retrieval-sourced staleness escalates with its diff to the
  state owner (memory or knowledge system) — the fix lands there.
