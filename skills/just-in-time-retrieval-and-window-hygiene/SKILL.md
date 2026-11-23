---
name: "just-in-time-retrieval-and-window-hygiene"
description: "Retrieve relevant context without flooding the window."
license: "MIT"
---
# Just-in-Time Retrieval and Window Hygiene

## Use when
- The agent pre-loads "everything it might need".
- Tool results accumulate and dominate the window.
- A long session is drifting or repeating itself.

## Instructions

1. Retrieve just in time: keep lightweight identifiers in the window (file
   paths, stored queries, links) and load the material with tools when it is
   actually needed. Pre-loading trades a fixed token cost every turn for a
   guessed-at convenience.
2. Disclose tools progressively: an agent does not need every tool schema in
   every turn. Surface what the current stage needs; the rest stays
   loadable.
3. Clear the re-fetchable: tool results that can be re-derived (file reads,
   API responses, search dumps) are the cheapest thing to clear from the
   window — clearing them early is the safest win in context engineering,
   but may invalidate prefix reuse on some providers. Preserve needed evidence,
   timestamps and durable pointers before clearing mutable results.
4. Externalise durable state: what the model must not re-derive — plans,
   decisions, established facts — goes to files or a memory store a human
   can read, not to the end of a long conversation.
5. Isolate exploration: noisy searches and dead-end reasoning run in a
   separate window or subagent; only the distilled result crosses back.
   One task's noise must not contaminate another task's context.
6. Keep it informative yet tight: every block in the window earns its place
   by supporting the current task; the test is signal density, not volume.

## Preferences
- Prefer measured hybrid retrieval when small stable upfront context is useful.

## Stop conditions
- Never let re-fetchable tool results sit uncleared once consumed, except where
  the provider's prefix reuse makes retained results cheaper — then keep the
  smallest evidence slice that preserves them.
- Never let exploration noise ride in the main window.

## Escalation
- Workloads whose live context genuinely exceeds the budget escalate to
  compaction or isolation decisions (the other members of this bundle) with
  the measured line items attached.
