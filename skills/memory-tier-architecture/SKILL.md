---
name: "memory-tier-architecture"
description: "Place working and durable memory deliberately."
license: "MIT"
---
# Memory Tier Architecture

## Use when
- An agent needs to remember beyond one session or one window.
- "Just add a memory system" is being proposed without a design.
- Retrieved context keeps being wrong, stale or overwhelming.

## Instructions

1. Three tiers, each with a job: core memory (always in the window — the
   agent's identity, active task state, the handful of facts that steer
   everything); recall memory (searchable interaction history, outside the
   window until queried); archival memory (long-term storage reached by
   explicit tool calls). Not every fact deserves core residency; not every
   fact deserves retrieval cost.
2. Blocks, not mush: core memory is structured into named blocks (self,
   task, key facts) the agent can read and edit deliberately — not a free-
   form summary blob that silently drifts.
3. Per fact, three questions: does it steer every turn (core), will it be
   needed again on demand (recall), or is it reference material (archival)?
   The answers move facts between tiers, and moves are recorded.
4. Write vs retrieve is a design decision: externalising state (files,
   stores) the agent re-reads is often better than remembering; the choice
   is made per fact class, once, deliberately.
5. Human-readable external state: durable state lives in a form a person can
   read and audit — plans, decision records, fact ledgers — not only inside
   a vector store's latent pile.
6. Multi-tenant and isolation rules are part of the architecture: whose
   memory this is, who may read it, and what never crosses — designed, not
   improvised at write time.

## Stop conditions
- Never let core memory become an unstructured dump.
- Keep a small measured working set in-window; retrieve bulky evidence on demand.
- Never design retrieval without designing what happens when it returns
  stale or wrong material.

## Escalation
- Requirements exceeding three tiers (shared team memory, cross-agent
  memory) escalate as architecture decisions with the tier map attached —
  not improvised per session.
