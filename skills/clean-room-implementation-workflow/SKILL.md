---
name: clean-room-implementation-workflow
description: "Build compatibility slices from a reviewed specification."
version: 0.1.0
author: Hermes
license: MIT
---

# Clean-room implementation workflow

Build a compatible implementation in small vertical slices from a reviewed behaviour specification. This skill does not author a clone from copied source or promise feature completeness without measured coverage.

## Procedure
1. Select one contract slice with an oracle and a stopping rule.
2. Write a failing contract test against the empty candidate; keep the reference call outside the candidate package.
3. Implement the smallest clean change, then run focused and wider parity tests.
4. Preserve a decision log: requirement, implementation choice, evidence, alternatives and unresolved risk.
5. Add compatibility fixtures for errors, ordering, version negotiation, persistence and resource limits.
6. Review dependency licences, generated code, bundled assets and distribution obligations before packaging.
7. Stop at the measured boundary; do not fill unknowns with guessed behaviour.

## Verification
Each released slice has a contract test, provenance entry, parity result, licence review and rollback path.
