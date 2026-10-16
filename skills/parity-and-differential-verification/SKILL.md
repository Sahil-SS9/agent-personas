---
name: parity-and-differential-verification
description: "Measure behavioural parity with safe fixtures."
version: 0.2.0
author: Hermes
license: MIT
---

# Parity and differential verification

Compare a candidate with an authorised reference through a deterministic, redacted harness. This does not require access to or redistribution of the reference implementation.

## Procedure
1. Freeze inputs, environment, versions, seeds and reference/candidate command lines. Hash fixtures and outputs.
2. Use a balanced suite: normal, boundary, malformed and safe negative controls. Include repeated runs for nondeterminism.
3. Choose byte comparison for canonical serialisation and semantic comparison for permitted representation differences; declare tolerances before running.
4. Normalise only documented nondeterminism. Never erase a mismatch by broadening the normaliser after seeing the result.
5. Classify mismatches as cosmetic, behavioural, compatibility-critical or harness error; retain minimal reproducers and both raw outputs in private evidence.
6. Report coverage, pass rate, mismatch categories, unsupported features and resource/time budgets.

## Verification
A result is valid only if the harness itself passes controls, the reference is versioned, negative controls remain distinguishable and all claimed metrics can be regenerated from the fixture manifest. A compile or sample-match is not parity.
