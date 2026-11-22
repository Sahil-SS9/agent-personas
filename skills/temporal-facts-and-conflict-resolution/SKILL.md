---
name: "temporal-facts-and-conflict-resolution"
description: "Resolve changing facts with time and provenance."
license: "MIT"
---
# Temporal Facts and Conflict Resolution

## Use when
- Facts change over time (roles, prices, addresses, preferences, versions).
- Two memories disagree and the agent must answer anyway.
- "How good is your memory" turns out to mean "how does it handle change".

## Instructions

1. Facts are time-bounded: store when a fact became true and (when known)
   when it stopped being true. A fact without time bounds answers today's
   question with whatever was last written.
2. Supersede, don't duplicate: a new fact that contradicts an old one
   supersedes it — the old value stays in history with its validity window
   closed, and retrieval serves the current truth. Duplicate contradictory
   facts co-existing is the failure mode, not the design.
3. When the resolution is uncertain, surface it: state both values with
   their times and sources rather than silently picking one. A wrong
   confident answer is worse than an honest conflict.
4. First match subject, predicate, scope and real-world validity: two claims
   may both be true. Ingestion recency alone is not truth. Apply a documented
   source-authority policy; absent decisive evidence, preserve the conflict.
5. Bi-temporal where it matters: record both when the fact was true in the
   world and when the system learned it — "the system knew on Tuesday" and
   "it was true on Tuesday" are different questions, and audits ask both.
6. Test contradictions deliberately: a memory system that has never been
   tested against conflicting facts has not been tested — contradiction
   handling is one important test alongside retrieval, abstention, isolation,
   deletion, latency and cost; no universal strongest discriminator is claimed.

## Stop conditions
- Never write a contradiction that leaves both facts equally live.
- Never answer confidently from a superseded or conflicted fact.
- Never invent a validity window you do not know — unknown is stored as
  unknown.

## Escalation
- Conflicts that cannot be resolved from stored data escalate to the
  source (re-ask, re-read, re-verify) — memory answers from what it holds,
  and says when that is not enough.
