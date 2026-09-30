---
name: "zdr-retention-verification"
description: "Verify zero-data-retention and training-use claims against the actual terms, and hunt the carve-outs that quietly defeat them."
license: "MIT"
---

# Zdr retention verification

## When to use
Any route carrying sensitive or client data, and whenever a provider changes terms.

## Procedure
1. Read the privacy policy, the terms of service, and the data-processing addendum as three separate documents.
2. Find the retention statement, its scope and its exceptions.
3. Hunt carve-outs: abuse monitoring, safety review, legal process, sub-processor lists, opt-in-by-default settings, and enterprise-versus-individual tier differences.
4. Check whether the claim applies to your tier and your product, not just to an enterprise plan.
5. Record each claim with the exact clause and retrieval date.

## Decision rules
- ZDR is a term, not a feature badge. Cite the clause or do not claim it.
- Retention for abuse monitoring is still retention; state the period.
- Tier matters: enterprise terms frequently do not bind the consumer product you are using.
- No operational coverage for ZDR exists in most tooling; verify manually rather than assuming a dashboard.

## Pitfalls
- Accepting a marketing page as the policy.
- Missing that sub-processors have their own retention.
- Assuming a self-hosted or gateway route inherits the upstream's ZDR.

## Done
Each retention claim is recorded with its clause, tier, carve-outs and retrieval date.
