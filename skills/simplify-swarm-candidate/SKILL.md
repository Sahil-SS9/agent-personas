---
name: simplify-swarm-candidate
description: Use when simplifying working changes through hygiene, clarity and correctness analysis.
version: 0.1.0
author: Sahil Saghir
license: MIT
---

# Simplify Swarm Candidate

Experimental operational method; evidence is limited to the scenarios actually exercised.

1. Freeze the exact diff and include explicitly requested new files. Check baseline tests and owned changes before analysis; a clean codebase may correctly yield no changes.

2. Analyse hygiene (dead code and redundancy), clarity (names, duplication, decomposition) and correctness (resources, concurrency and failure semantics) separately and read-only. Parallel workers require permission; sequential passes are controller self-review.

3. Consolidate findings into id, file, line, category, description, confidence, override_risk, evidence and proposed change. Keep SAFE/CAREFUL/RISKY vocabulary consistent. Agreement may prioritise investigation but never promotes a risky change to SAFE.

4. Verify both sides of each call chain before accepting a finding. Text search alone cannot prove dynamic exports, imports with side effects or feature flags are unused. Preserve comments that explain intent and constraints.

5. Apply only pre-authorised scope/tiers. SAFE requires evidence of unchanged semantics, not merely deletion. Resource lifetime, locks, public contracts and error propagation are RISKY regardless of which perspective found them.

6. Apply one coherent slice and run the strongest relevant checks. On failure diagnose first, then undo only owned hunks if needed; never reset the whole tree or discard unrelated work.

7. Do not replace explicit readable logic with terse puzzles. Extract helpers around stable shared meaning, not cosmetic resemblance. Review the combined diff after automated fixes.

8. End with applied/declined/deferred findings, verification receipts and residual risk. State done, blocked or awaiting-authority accurately. Adversarial review remains a separate pass after simplification.

## Provenance and limits
Read [source synthesis](SOURCE-SYNTHESIS.md) when assessing origin, conflicting guidance or evidence maturity.

## Source-grounded decision rules

Keep cohesive code together when extraction creates conjoined helpers that must be read together. Compare interface complexity before and after; shorter functions alone are not a success criterion (Ousterhout section 9.8).

Retain comments that state caller contracts or hidden constraints. Reject consolidation of superficially similar helpers with different ownership, failure or ordering semantics; a general mechanism must simplify current callers rather than shift complexity into them (Ousterhout chapters 6 and section 12.6).
