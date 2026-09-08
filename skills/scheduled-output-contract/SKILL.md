---
name: "scheduled-output-contract"
description: "Produce concise, verifiable output from scheduled tasks."
license: "MIT"
---
# Scheduled Output Contract

## When to use
Produce concise, verifiable output from scheduled tasks.

## Method
1. Define output mode and recipient before running a scheduled task: silent bookkeeping, actionable alert or human-facing digest.
2. Produce one concise summary with a decision or next action; link necessary artefacts rather than flooding recipients with intermediate checks.
3. Distinguish an empty valid result from a failed collection. Never label missing evidence as no news and never turn internal reasoning into a notification.
4. Validate artefacts exist and are readable before delivery. Read back the exact destination where possible; preserve unverified delivery as an explicit state.
5. Use idempotency keys or run identifiers to prevent duplicate sends. Do not send a second message merely to repeat a successful verification.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
