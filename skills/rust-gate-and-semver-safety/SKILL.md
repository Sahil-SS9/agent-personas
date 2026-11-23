---
name: "rust-gate-and-semver-safety"
description: "Gate every port on the full Rust hygiene gate — fmt, clippy, tests, unsafe audit, error paths — and prove the crate's API did not break semver."
license: "MIT"
---
# Rust Gate and Semver Safety

## Use when
- A port or crate change claims to be done.
- Anything might leave the crate's consumers.
- An edition migration or dependency bump is planned.

## Instructions

1. The gate is fixed and non-negotiable: formatting, clippy with warnings
   denied, the full test suite, an unsafe audit, and nothing unported left
   behind without a recorded reason. A port passes the gate or it is not
   done.
2. Error paths are part of behaviour: the original's every error path gets a
   recorded failing case, and the port never panics where the original
   returned an error. Only genuinely infallible sites are marked as such —
   and the mark is a justification, not a suppression.
3. unsafe is audited, not just counted: each block states why it exists, the
   invariant it relies on, and why safe Rust cannot do it. Undefined
   behaviour checks (Miri or equivalent) run on code that can take untrusted
   input before the gate passes.
4. Semver is proven, not felt: linter-based breaking-change detection runs
   against the previous published crate version before release; a change
   that breaks the public API is a major bump or a compatibility shim, and
   that decision is recorded.
5. Edition migrations are their own change: never mix an edition move with
   a behaviour change; the migration compiles and passes the gate alone
   first.
6. Public API naming follows the Rust API guidelines (naming, Result vs
   Option, getter conventions); internal style never leaks into the public
   surface.

## Stop conditions
- Never merge with the gate red; the gate has no exceptions.
- Never mark infallible to make the gate pass.
- Never ship an API change without the semver check result recorded.

## Escalation
- Gate failures that reveal a design problem (the port needs unsafe the
  design cannot justify) go back to the plan — the unit may need to stay
  behind the bridge.
