---
name: codebase-simplification-campaign
description: Use when refactoring a module or codebase while preserving behaviour.
version: 0.2.1
author: Sahil Saghir
license: MIT
---

# Codebase Simplification Campaign

Operational method; evidence is limited to the scenarios actually exercised.

## Preparation gate
Applies to module-level refactors as well as campaigns. BEFORE the first structural source edit, follow [refactor preparation](references/refactor-preparation.md): inspect and execute relevant coverage; add and run missing boundary characterization against unchanged source. A smoke pass alone does not cover absent edge assertions. Reuse adequate existing coverage without duplicate tests.
For structural-plus-feature work, verify a behaviour-preserving structural slice before adding the feature; separate edits/test receipts suffice, not mandatory separate commits. If a small test seam is necessary first, disclose and verify that prerequisite instead of pretending the source was untouched.
For trivial local work, use the short path in the guide; the repository-wide LOC census and campaign machinery below apply only when a repository-wide campaign or numerical reduction is requested.


1. Freeze baseline revision, tracked file universe, language-aware LOC tool/version and exclusions before changes. Report overall repository and production-source counts separately, with tests/docs/generated/vendor categories. Include new and moved files consistently.

2. A requested 30% reduction is an aggressive target, not a licence to remove features, tests, security guards, observability or compatibility. Never minify, reclassify or move code outside the denominator to claim success. Report target shortfalls honestly.

3. Map entrypoints, dependencies, high-churn modules, large files and duplicate behaviours. Read callers and history before declaring code dead; reflection, registration and import side effects can evade text search.

4. First add characterisation tests at observable boundaries, including error paths, ordering and side effects. Keep existing defects distinguishable from intended fixes; behaviour-changing repairs are separate scope, not disguised refactoring.

5. Rank seams by measured duplication, change coupling and verification cost. Break god files along coherent responsibilities and ownership, not line thresholds. Consolidate helpers only when semantics and reasons for change match; keep accidental similarity separate.

6. Flatten routing only after recording precedence, fallthrough, defaults and failure semantics. Compare guard clauses, explicit state transitions and table dispatch; reject clever indirection that makes the caller harder to understand.

7. Apply small reversible slices; after each slice run focused and integration tests. Use simplify-swarm-candidate for local improvements and hermaguard-candidate for adversarial verification. Reviewer agreement never lowers change risk.

8. Prefer independently green stacked PRs. When changing published interfaces or independently deployed consumers, apply [expand/migrate/contract gates](references/parallel-evolution.md), including mixed-state and retirement evidence. Use one atomic PR only where splitting creates broken intermediate states. Continue routine approved choices without asking, but do not invent missing authority or conceal blockers.

9. Report baseline/current counts, reduction, duplication/coupling changes, remaining hotspots, tests and actual PR handles if authorised. Only undo owned changes; preserve unrelated dirty work. A smaller tree is not enough: prove unchanged contracts and explain representative execution paths.

## Provenance and limits
Read [source synthesis](SOURCE-SYNTHESIS.md) when assessing origin, conflicting guidance or evidence maturity.

## Source-grounded decision rules

Separate mechanism, specialised action and policy when they have different change reasons. A god-file split is successful only if callers need less knowledge and dependencies decrease; never extract solely to meet a function-length threshold (Ousterhout, chapters 6 and section 9.8).

Reduce special cases through representations only after proving distinctions are irrelevant: empty and absent are not interchangeable when callers observe them. Compare explicit branches, data dispatch and polymorphism; preserve unknown-type defaults and error semantics (Ousterhout chapter 6; Fowler catalogue).

Migration ledger: enumerate every consumer, compatibility state, owner, verification and retirement condition. Use independently green shards, prevent new old-API uses, and do not call the migration finished while consumers or temporary adapters remain (Software Engineering at Google, chapter 22).

Branch by abstraction: place current behaviour behind a narrow boundary, migrate callers, introduce and compare the replacement, switch only with authority, then retire old implementation and temporary boundary when no longer needed. Test mixed-version states; do not shadow-write side effects (Fowler, Branch By Abstraction; side-effect prohibition is our safety synthesis).

Freeze the dependency index revision and confirm runtime registration, configuration and dynamic callers separately. Treat graph absence as an investigation lead, never proof of dead code (wiki codeindex plus upstream README).
