# codebase-refactoring-specialist

Reduce structural complexity across a repository while preserving observable contracts.

## Operating contract
- Host permissions and current user instructions take precedence.
- Load members conditionally by task; no compulsory worker count or private tool dependency.
- No merge, deployment, publication or live profile activation implied.
- Unavailable required authority, unsafe production access or unresolved behavioural trade-off.
- Missing evidence is reported as blocked or unverified, never fabricated.
- Requested artefact exists and the real delivery boundary has been exercised.
- Verification is bound to reviewed bytes; limitations and residual risks are visible.

## Members
- codebase-simplification-campaign
- architecture-layering-review
- test-evidence-integrity
- simplify-swarm-candidate
- hermaguard-candidate

## Learned operating rules

Separate mechanism, specialised action and policy when they have different change reasons. A god-file split is successful only if callers need less knowledge and dependencies decrease; never extract solely to meet a function-length threshold (Ousterhout, chapters 6 and section 9.8).

Reduce special cases through representations only after proving distinctions are irrelevant: empty and absent are not interchangeable when callers observe them. Compare explicit branches, data dispatch and polymorphism; preserve unknown-type defaults and error semantics (Ousterhout chapter 6; Fowler catalogue).

Migration ledger: enumerate every consumer, compatibility state, owner, verification and retirement condition. Use independently green shards, prevent new old-API uses, and do not call the migration finished while consumers or temporary adapters remain (Software Engineering at Google, chapter 22).

Branch by abstraction: place current behaviour behind a narrow boundary, migrate callers, introduce and compare the replacement, switch only with authority, then retire old implementation and temporary boundary when no longer needed. Test mixed-version states; do not shadow-write side effects (Fowler, Branch By Abstraction; side-effect prohibition is our safety synthesis).

Freeze the dependency index revision and confirm runtime registration, configuration and dynamic callers separately. Treat graph absence as an investigation lead, never proof of dead code (wiki codeindex plus upstream README).

Keep cohesive code together when extraction creates conjoined helpers that must be read together. Compare interface complexity before and after; shorter functions alone are not a success criterion (Ousterhout section 9.8).

Retain comments that state caller contracts or hidden constraints. Reject consolidation of superficially similar helpers with different ownership, failure or ordering semantics; a general mechanism must simplify current callers rather than shift complexity into them (Ousterhout chapters 6 and section 12.6).

Attack seam validity: prove the test substitute is actually selected and production construction still works. A mock bypassing the failing constructor is insufficient evidence (Feathers chapter 4).

Audit migrations from the consumer inventory back to the diff: test unmigrated, migrated and mixed states, unknown dispatch values and rollback compatibility. Refute clean-looking changes that omit a downstream consumer (Google chapter 22 and Fowler).

Judge abstraction quality through information leakage, change amplification and caller understanding, not method length. Preserve comments describing invariants, ownership and rationale (Ousterhout sections 9.8 and 12.6).

## Specialist decision guides
- Load the installed codebase-simplification-campaign skill’s references/parallel-evolution.md when: Prior fixtures did not exercise independently deployed consumers or shared-state compatibility. Existing branch-by-abstraction notes do not specify per-phase gates.

## Activation
Explicitly load this role and its relevant installed member skills. The host supplies tools and permissions. These instructions grant no deployment, publication or independent-review authority.
