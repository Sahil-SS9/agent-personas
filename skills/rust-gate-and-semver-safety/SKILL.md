---
name: "rust-gate-and-semver-safety"
description: "Use before saying a Rust port or rewrite is done or ready: build, fmt, clippy with porting lints, real tests in debug, no stubs or todo!, Err instead of panic or unwrap, unsafe documented, public API unchanged."
license: "MIT"
---

# Rust gate and semver safety

Step 7. "It compiles and the tests pass" is not done. The gate makes every port meet the same bar.

## Use when
- Before reporting a port as finished, and in CI for every change to it.

## DO NOT use when
- Measuring speed (rust-benchmarking-with-controls).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Run `scripts/port_gate.py <crate> --offline`** and fix every FAIL in order:
   - build; `cargo fmt --check`;
   - `cargo clippy -- -D warnings` plus porting lints `cast_possible_truncation`, `cast_sign_loss`, `cast_possible_wrap`, `arithmetic_side_effects` (each flags an integer trap from step 4);
   - at least one real test (passing with zero tests proves nothing) and `cargo test` passing;
   - no `todo!`/`unimplemented!`;
   - no `unwrap`/`expect`/`panic!` inside a function that returns `Result` (return `Err`; for a truly impossible state add `// INFALLIBLE: why`);
   - every `unsafe` with a `// SAFETY:` comment.
2. **Run the equivalence replay** (step 3): recorded N/N and held-out M/M. The gate does not replace it.
3. **Silence a lint only with `#[expect(lint, reason = "...")]`**, never a blanket `#[allow]`.
4. **Check debug AND release behaviour** where integers are involved (overflow checks differ).
5. **Published crates:** run `cargo semver-checks` before each release so the Rust API does not break callers.

## Tools
`scripts/port_gate.py [CRATE] [--offline] [--no-clippy]`: PASS/FAIL per check with the fix; exit 1 until all pass.

## Worked example
Porting `parse_size("10MB") -> Result<u64, String>`. First gate run: FAIL tests_exist, FAIL err_not_panic (`num.parse::<u64>().unwrap()` inside the Result function), FAIL clippy `cast_possible_truncation` (`kib as u32`). Fixes: tests for "", "10", "10XB" and "99999999999999999999MB"; `map_err` to `Err("ValueError: ...")`; `u32::try_from(kib)` returning an error. Second run: all PASS; replay 42/42; held-out 60/60.

## Checklist
- [ ] port_gate.py all PASS
- [ ] Equivalence replay and held-out pass
- [ ] Lints silenced only with #[expect(..., reason)]
- [ ] Debug and release checked for integer code
- [ ] semver-checks for published crates

## Output
The gate output and the replay counts.

## Avoid
- Declaring done because `cargo build` succeeded.
