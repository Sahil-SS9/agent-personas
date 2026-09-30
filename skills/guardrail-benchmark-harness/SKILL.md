---
name: "guardrail-benchmark-harness"
description: "Build the benchmark that can fail a rail: adversarial surfaces, trajectory-level checks, and claim discipline that penalises fabricated coverage."
license: "MIT"
---

# Guardrail benchmark harness

## When to use
Comparing rails, validating a rail before promotion, or re-validating after a change.

## Procedure
1. Build fixtures per surface, including at least one harm that only exists compositionally across steps.
2. Trace whether the harm reaches execution, not just whether a rail fired.
3. Score: placement accuracy, trajectory-level detection, over-triggering rate, and claim discipline.
4. Include a deliberate over-trigger fixture so a rail that blocks everything fails.
5. Record results as a versioned tuple: rail, model, threshold, fixture set, verdict.

## Decision rules
- A benchmark that cannot fail a rail is decoration. Include the reject-everything case.
- Rails asserted without a mechanism score as fabricated coverage, not as untested.
- Verdicts are bound to a tuple; re-test when any element changes.
- Under a recall harness, a rail that never rejects can post perfect recall while filtering nothing. Always pair recall with a utility or over-trigger measure.

## Decision-output clarification
Separate expected policy from observed exam behaviour. A block-everything control should fail a zero-benign-block-budget exam. If the saved verdict nevertheless passes it, over-trigger detection has not been demonstrated: report the recorded pass and the harness defect separately. Reasoning that it should fail is not evidence that the exam actually rejected it.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Scoring firing instead of preventing.
- Single-turn fixtures that miss cross-step violations.
- Publishing a pass rate with no fixture version.

## Done
The harness can reject a bad rail and validate a good one, and the result records the full tuple that produced it.
