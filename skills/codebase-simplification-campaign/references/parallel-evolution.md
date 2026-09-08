Source: https://martinfowler.com/bliki/ParallelChange.html
Author: Danilo Sato
Read scope: Full article; complement, not repeat, existing chapter-22 and Branch By Abstraction learning
Captured: 2026-09-08T19:32:09.326129+00:00
Rights: original distillation; source rights retained; no source text redistribution.
Target: codebase-simplification-campaign

# Published-interface change: phase gates

Load when a refactor changes a published signature, schema or independently deployed consumer contract. Use ordinary small refactoring when all clients can safely change together.

## Procedure and gates
1. Inventory old and new readers/writers, external clients, persisted data, delayed jobs and rollback binaries. Distinguish source migration from deployed consumer migration; source search cannot prove external clients have stopped.
2. EXPAND: introduce the new interface while old clients still work. Prefer an old-interface shim delegating to one authoritative implementation when semantics permit. Test old writes/new reads and new writes/old reads when they share logical state.
3. If duplicate representations are unavoidable, specify the authoritative representation and synchronisation/backfill rules before allowing mixed use. The article's illustrative separate containers are not a proof of shared-state consistency. Do not blindly translate that example into dual independent production stores.
4. MIGRATE: move consumers in bounded batches; record cohort, active version, compatibility evidence, and rollback position. Gate each batch on contract tests and data parity relevant to that cohort. Deployment is separately authorised.
5. CONTRACT: remove old interfaces only after evidence that supported old readers/writers, delayed jobs and rollback versions no longer need them. A timeout without observed migration is not retirement proof. Track removal of adapters, obsolete data and temporary flags as explicit completion work.
6. Define the rollback frontier: after a lossy transformation or old-schema removal, reverting code alone may not restore compatibility. Establish a restoration or forward-repair path before taking that step. This rollback application is our synthesis beyond the article's basic phase description.

## Structure to deliver
A phase ledger with consumer cohort, old/new version compatibility, authoritative data form, verification command, rollback condition and exit criterion. Keep build-ready, migrated and contracted as separate states.

## Acceptance scenarios (not executed by these notes)
- Old caller writes; new caller must observe the same logical record.
- Mixed old/new consumers and queued old-format jobs remain supported until the retirement gate.
- An unobserved external client blocks an unsupported claim of complete migration.
- A migration adding temporary code may be correct even when the LOC target is temporarily missed.

## Conflicts and negative controls
Do not accept malformed security-sensitive payloads just because the source mentions Postel's Law. Do not implement three release phases for a private helper with one safely migratable caller. Branch by abstraction remains useful when a shared seam reduces a very large consumer surface; parallel change is not its compulsory replacement.
