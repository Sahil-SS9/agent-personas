---
name: parity-and-differential-verification
description: "Measure behavioural parity with safe fixtures."
version: 0.1.0
author: Hermes
license: MIT
---

# Parity and differential verification

Compare a candidate implementation with an authorised reference through a deterministic, redacted harness. This skill does not require access to or redistribution of the reference implementation.

## Procedure
1. Freeze input fixtures, environment metadata, reference version and candidate version.
2. Run both sides in separate disposable environments and capture structured outputs, errors, state changes and resource limits.
3. Normalise only documented nondeterminism; never hide a mismatch by broad string cleaning.
4. Score exact, semantic and tolerated fields separately. Classify mismatches as contract, platform, timing, unknown or candidate defect.
5. Include malformed, boundary, repeated and rollback cases. Preserve failing fixtures and a minimal reproduction.
6. Re-run the full matrix after every change and publish limitations alongside the score.

## Verification
Report fixture count, exact/semantic match rates, mismatch severity, excluded fields and a reproducible command.
