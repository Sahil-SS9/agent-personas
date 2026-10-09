---
name: "differential-verification-reporting"
description: "Verify reconstructions against ground truth and report evidence-led findings with honest confidence boundaries."
license: "MIT"
---

# Differential verification and reporting

Separate what you know from what you think. Verify before claiming; report so a stranger can audit.

## When to use
Closing any reverse-engineering engagement: before findings leave the specialist, and whenever two evidence sources disagree.

## Procedure
1. Build the verification matrix: for every finding, the claim, the evidence class (byte-verified / dynamically observed / inferred / unknown) and the check that could falsify it.
2. Differential checks: where lineage exists, diff the reconstruction against the reference implementation (function-level match audit, accepted-only-with-semantics rule); where it does not, round-trip validation (encode/decode, client/server playback) against the real artefact.
3. Run the negative controls the findings require: benign-but-similar mechanisms for security findings, decoy cases the answer should NOT match, and re-runs where behaviour was ambiguous.
4. Reconcile disagreements explicitly: static vs dynamic conflicts, score vs semantics conflicts in differential tooling — resolve by evidence class, document the resolution, never average contradictions away.
5. Report structure: question → method → findings (each with evidence class) → negative controls run → impact qualification → unknowns/limits → detection/interoperability handoffs. Every claim names its evidence; every unverified statement is marked.
6. Handoff contracts: findings that belong to other specialists go as structured handoffs with the observables and evidence they need (detections to blue-team; exploit validation to red-team under its own authorisation) — carried, not assumed received.
7. Archive the audit trail: tools+versions, scripts, captures and manifests that let a stranger reproduce the conclusion.

## Decision rules
- A finding without an evidence class is unreported noise; rewrite or drop it.
- Confidence is bounded by the weakest evidence in the chain supporting the claim.
- Report tool failures and coverage limits as results: a fuzzer that found nothing says something only if its coverage was measured.
- If verification would change a finding already communicated to the owner, correct early and explicitly; no silent updates.

## Pitfalls
- Reporting tool output (capability rules, similarity scores, solver status) as analysis conclusions.
- Cherry-picking the run that confirms; ambiguity gets both runs recorded.
- Handoffs "sent" without confirmation of what was actually needed.

## Done
A verification matrix with all findings evidence-classed, disagreements resolved and documented, negative controls executed, handoffs confirmed, and an auditable archive.