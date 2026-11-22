---
name: "memory-write-and-curation-discipline"
description: "Curate scoped memories and honour deletion policy."
license: "MIT"
---
# Memory Write and Curation Discipline

## Use when
- Deciding what a memory system stores (and what it must not).
- Memory is growing fast and nobody is deleting anything.
- Retrieved memories repeat, contradict or leak private material.

## Instructions

1. Curation happens at WRITE time, not at read time: deduplicate, supersede
   and classify when the memory arrives. A store curated later is a store
   that serves noise until someone pays for cleanup.
2. Provenance rides every memory: who said it, when, from what source.
   A memory without provenance cannot be trusted, superseded or audited.
3. Forgetting is a first-class operation: transient detail (session
   scaffolding, tool chatter, one-off scratch) is never stored; superseded
   values close their window subject to retention policy. Authorised erasure
   must also address derived facts, indexes, caches and backups under policy;
   hiding a fact from current retrieval is not deletion. Opinions and facts age
   on an explicit schedule.
   A store that only grows is a store that eventually answers wrongly.
4. Never store secrets: credentials and keys stay out. Persist personal data only with
   appropriate purpose, authority, minimisation, scope and retention; anything
   the user did not mean to persist stays out — write-time policy, not a
   hope about later filtering.
5. Write what is true, not what was said: extract the fact from the
   phrasing, with the speaker's certainty attached. "Maybe X" stored as
   "X" is corruption with good intentions.
6. Periodic review with a readable ledger: curation decisions are recorded
   (what was merged, superseded, forgotten, and why) so a human can audit
   the store's history — the same way code review audits a branch.
7. Dream/consolidation passes are auditable and reversible: bulk merges or
   summaries run against a copy first, report what they would change, and
   are applied only after review — memory rewrites are changes to user
   data, and get change discipline.

## Stop conditions
- Never write without dedup/supersede checks against existing memory.
- Never store transient scaffolding or secrets.
- Never bulk-rewrite memory without a reviewable, reversible plan.

## Escalation
- Curation passes that would merge or discard memories of consequence
  escalate with their preview — the owner decides, the ledger records.
