---
name: "fail-open-gate-and-band-policy"
description: "Integrate a decision model as a fail-open pre-filter with explicit threshold bands, telemetry and a single rollback switch."
license: "MIT"
---

# Fail open gate and band policy

## When to use
Putting a qualifying model in front of a larger, more expensive process.

## Procedure
1. Define the bands: below the low threshold, drop with confidence; above the high threshold, keep; between them, defer to the incumbent path.
2. Make the gate fail open on every failure: no model, no key, disabled flag, timeout, or exception.
3. Emit telemetry per decision: verdict, band, score, latency, and what happened next.
4. Provide a single environment switch to disable the filter without a deploy.
5. Verify the disabled path is identical to the pre-filter behaviour.

## Decision rules
- Fail open, always. A filter that fails closed can halt the pipeline it was added to protect.
- The middle band is where the savings and the risk both live; tune it against the exam, not by intuition.
- Every gate needs a rollback that has been exercised, not merely declared.
- Record the cost per decision so the savings claim is checkable.

## Pitfalls
- A crash path that silently drops inputs instead of passing them through.
- Tuning the middle band on production traffic without an exam.
- No telemetry on the deferred band, so its size is unknown.

## Done
The gate fails open on every failure mode, the bands are set from the exam, telemetry covers all three bands, and rollback has been exercised.
