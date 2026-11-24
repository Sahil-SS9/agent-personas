---
name: "port-plan-and-decision-records"
description: "Use when a Rust rewrite or port covers more than one function or file, or when asked to plan a migration to Rust: scope, equivalence bar, compatibility promises, crate map, waves, checkpoints and recorded decisions."
license: "MIT"
---

# Port plan and decision records

Step 2. A port without a written equivalence bar and scope ends in arguments about whether a difference is a bug.

## Use when
- After choosing the unit (step 1), before any Rust is written. Also for whole-app ports.

## DO NOT use when
- The plan exists and is approved; go to recorded-behaviour-equivalence.

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Inventory the unit:** exported functions and their signatures, the types that cross, error behaviour (every `raise`/`throw`/error return), I/O and side effects, global state, and its dependencies.
2. **Set the equivalence bar with the owner:** byte-for-byte output (default), or equal after normalising named things (key order, float tolerance with a stated value, timestamps). Never pick a tolerance yourself.
3. **List compatibility surfaces that must not change:** function signatures callers use, config/on-disk/wire formats, CLI flags and exit codes, environment variables, error types callers catch.
4. **Map each dependency to a Rust crate,** or mark it "unknown" for the owner. Never silently hand-roll a library. In offline settings, std only unless a vendored crate is listed.
5. **Order the work in waves:** leaves first, so Rust never calls back into the original; units in a dependency cycle move together.
6. **Set checkpoints** (default: stop for the owner after the plan, then after each wave) and the cutover style (shadow first, then switch).
7. **Write decision records** (ADR: context, decision, consequences) for each choice above.

## Worked example
Porting `pricing.py` (3 functions). Equivalence bar: identical results; floats compared exactly because prices are integer cents. Compatibility: the `Quote` dict keys and `PricingError` type must stay. Dependency: `decimal` -> none needed (cents as i64). Wave 1: `round_cents`, `tax_for`; wave 2: `quote` (calls both). Checkpoint after wave 1. ADR-001: "integer cents, not f64".

## Checklist
- [ ] Inventory (exports, types, errors, side effects, state, deps)
- [ ] Equivalence bar agreed (no self-chosen tolerance)
- [ ] Compatibility surfaces listed
- [ ] Dependency-to-crate map, unknowns flagged
- [ ] Waves, checkpoints and cutover style
- [ ] ADRs written

## Output
PLAN.md with the items above and the ADRs.

## Avoid
- Starting to write Rust before the equivalence bar is set.
- Replacing a library with hand-written code without saying so.
