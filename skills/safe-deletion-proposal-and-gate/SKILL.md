---
name: "safe-deletion-proposal-and-gate"
description: "Propose deletions behind an explicit human gate, with confidence, reason and a restore reference for anything destructive."
license: "MIT"
---

# Safe deletion proposal and gate

## When to use
Producing cleanup proposals from a register.

## Procedure
1. Assign each item a status, a confidence, a proposed action and a reason.
2. Before proposing a move, quarantine, archive or deletion, verify provenance, whether the item is in use, and a tested restore path. A snapshot label or backup's mere existence is not restore proof. Until those checks pass, report and hold the item; do not propose moving or deleting it, even behind an approval gate.
3. Group eligible proposals by reversibility: trash-move, quarantine-move, archive, delete.
4. Present the smallest set that achieves the goal, with the residual-uncertainty appendix attached.
5. Never execute. The register proposes; the human disposes.

## Decision rules
- Low confidence or unverified provenance, use, or restore means report and hold each affected item; do not propose quarantine, archive or deletion. Urgent space pressure does not waive this rule, including for apparent logs, caches or model files. A move to quarantine is still a move proposal even if labelled reversible; do not list it as the current action or a ready-to-approve fallback until all checks pass.
- A report may name an untested snapshot as a candidate restore source if it explicitly requires checking relevance, coverage, suitability and a test restore before treating it as viable. A restore reference counts for a move proposal only after those checks pass. No tested restore, no move or destructive proposal.
- A report needs no file-move approval. Human approval is required before any later move, quarantine, archive or deletion; approval alone never replaces the evidence checks.
- The register never executes anything, including via a helper it wrote.
- Residual uncertainty is mandatory, not optional, and must name what you could not check.

## Pitfalls
- Batching a risky item inside a batch of obvious junk.
- Reporting only the deletable items and hiding the uncertain ones.
- Leaving the gate as a formality by making approval trivial.

## Done
Every destructive proposal has a restore reference and a confidence, and the uncertain items are listed rather than omitted.
