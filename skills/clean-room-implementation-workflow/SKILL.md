---
name: clean-room-implementation-workflow
description: "Build compatibility slices from a reviewed specification."
version: 0.2.0
author: Hermes
license: MIT
---

# Clean-room implementation workflow

Build a compatible implementation in small vertical slices from a frozen behaviour specification. Do not author a clone from copied source or promise completeness without measurements.

## Procedure
1. Select one requirement with a stable oracle and define the smallest useful slice.
2. Create a clean fixture and a failing parity test before implementation; retain the RED result as evidence.
3. Implement the narrowest public behaviour, with explicit error and state semantics. Keep reference observations out of source comments and runtime logs.
4. Run focused parity tests, then normal/boundary/malformed/negative-control cases. Record byte or semantic comparison mode and tolerances.
5. Add a second fixture before generalising. Track unsupported features rather than guessing.
6. Run differential, property and round-trip checks where applicable; minimise failures to a reproducible fixture.
7. Review dependency licences, generated artefacts and provenance before merging a slice.

## Slice record
Requirement IDs; implementation commit; fixture hashes; environment; oracle; pass/fail; known divergence; performance/resource budget; reviewer; next slice.

## Stop rules
Stop on contaminated inputs, unexplained parity failures, non-determinism, legal-scope uncertainty, or three identical failed approaches. Change the experiment, not the oracle. A high test count with weak oracles is not compatibility evidence.
