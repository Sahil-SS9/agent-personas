---
name: "exam-validity-and-robustness-proof"
description: "Prove the exam can be trusted before any model is rejected on it — with oracle and anti-oracle controls and invariance checks."
license: "MIT"
---

# Exam validity and robustness proof

## When to use
Before concluding that any candidate fails, and whenever a benchmark produces a surprising result.

## Procedure
1. Push an oracle through the identical harness: a synthetic model with perfect discrimination. It establishes the achievable ceiling.
2. Push an anti-oracle through: a model that rejects everything. It must fail the gates.
3. If the oracle cannot reach the ceiling or the anti-oracle passes, the exam is broken, not the candidates.
4. Check invariance: option order, surface phrasing, and formatting should not change the verdict.
5. Recompute all threshold and band points offline from saved answers before declaring a discriminating failure.

## Decision rules
- An exam that rejects every model is not evidence that every model is bad.
- An exam that passes reject-everything has no teeth.
- Distinguish a calibration artefact from a genuine ability limit by recomputing the whole grid offline, not by tuning live.
- A ceiling well below 100 percent is legitimate and must be published as the exam's real limit.

## Pitfalls
- Rejecting candidates on a benchmark that was never validated.
- Assuming a low ceiling means the models are weak rather than that the task is hard.
- Comparing scores from two versions of an exam.

## Done
The exam has a published ceiling from an oracle, a demonstrated rejection of an anti-oracle, and recorded invariance results.
