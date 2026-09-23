---
name: "finding-verification-and-chaining"
description: "Verify and chain findings into reproducible, severity-scored, ATT&CK-mapped evidence."
license: "MIT"
---

# Finding verification and chaining

## When to use
After every suspected finding, before it enters the report.

## Procedure
1. Verify each finding with in-scope reproduction: exact steps, minimal proof-of-concept, captured evidence. Unreproducible findings are discarded, not speculated.
2. Map to ATT&CK technique; classify per OWASP-style failure class where web-applicable.
3. Attempt chains: can this finding combine with another to reach credentials, data, or impact? Report the chain and its end-to-end impact, not just the link.
4. Score severity on a consistent rubric (impact × likelihood); state the reasoning, not just the number.
5. Write the remediation the defender can act on: concrete change, not "improve security".
6. Retest after fixes: verify closure with the same reproduction; assumptions do not close findings.

## Decision rules
- No severity without reasoning; no finding without reproduction.
- Report impact honestly: avoid inflating to sound impressive; overstated severity destroys trust in the whole report.
- Out-of-scope discoveries are escalated, not exploited.

## Pitfalls
- Scanner noise reported as verified findings.
- PoCs that damage or destroy data.

## Done
A verified, chained, reproducible finding set with severities, remediations, and retest evidence.