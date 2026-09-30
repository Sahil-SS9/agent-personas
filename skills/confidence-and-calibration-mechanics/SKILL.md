---
name: "confidence-and-calibration-mechanics"
description: "Read a model is confidence distribution correctly, and tell a genuinely discriminative model from one that scores everything the same."
license: "MIT"
---

# Confidence and calibration mechanics

## When to use
A candidate passes a recall gate but you suspect it is not discriminating, or thresholds must be set.

## Procedure
1. Inspect the score distribution across inputs, not just the argmax.
2. Check spread: a flat distribution across options means the model has no opinion.
3. Check separability between the classes you care about, not the accuracy of the top option.
4. Test proper scoring: a calibrated model should be penalised for confident errors.
5. Fix the operating point deliberately, then re-examine the distribution at that point.

## Decision rules
- A model that never rejects can post perfect recall while filtering nothing. Always pair recall with the rejection or noise-reduction figure.
- Flat distributions are genuine uncertainty, not a threshold artefact. Re-tuning will not rescue them.
- Check upstream serving bugs before concluding a model is weak, but be sceptical: after correcting one, our verdict did not change.
- Calibration and discrimination are different properties; a well-calibrated uninformative model is still useless here.

## Pitfalls
- Judging on accuracy of the top option alone.
- Blaming thresholds for what is a model capability limit.
- Reading a score as a probability of correctness without checking calibration.

## Done
The distribution is characterised, discrimination is measured separately from calibration, and the operating point is recorded with its dataset.
