---
name: "ffi-bridge-selection-and-boundaries"
description: "Use when Rust code will be called from Python, Node/JavaScript or C (PyO3, napi-rs, wasm-bindgen, C ABI): choose the bridge, design the boundary, convert errors, and keep panics and unsafe away from callers."
license: "MIT"
---

# FFI bridge selection and boundaries

Step 6. The bridge is where ports crash processes (a panic unwinding into Node, Python or C aborts) and where per-call conversion costs erase speed-ups.

## Use when
- The port is called from Python, JS/Node, C, Go, Ruby or Java.

## DO NOT use when
- The port replaces the whole program (no callers in the original language).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Choose the bridge by caller:** Python -> PyO3 (abi3 wheel); Node-only code -> napi-rs; code that must also run in browsers -> wasm-bindgen; C callers -> a plain `extern "C"` API with a header.
2. **Split the crate:** `port.rs` holds plain safe Rust (`#![forbid(unsafe_code)]`), testable without the host runtime; `lib.rs` holds the generated or hand-written bindings.
3. **Catch panics at every exported function** (`std::panic::catch_unwind`) and turn them into the host's error (exception, error code). Unwinding across a non-`-unwind` ABI is undefined behaviour.
4. **Map errors to the host's types:** the same exception class the original raised, the same error code or errno.
5. **Types across the boundary:** numbers and strings directly; JS numbers are f64; Python ints that pass through must come back as ints; C `const char *` -> bytes, not `&str`; ownership of any buffer is explicit (who frees it) and documented.
6. **Cost:** measure the per-call crossing cost; batch hot loops (items cross once, results return as one array).
7. **Keep the original's API:** a wrapper with the same names, defaults and keyword arguments, so callers do not change. Test the equivalence cases THROUGH the wrapper, the way callers call it.

## Worked example
A PyO3 port of `tokenise(text: str) -> list[str]`. `port.rs` returns `Result<Vec<String>, TokError>`. The `#[pyfunction]` wrapper catches panics, maps `TokError::Empty` to `ValueError` (as the original raised), and the Python shim keeps the `tokenise(text, lower=True)` keyword default. The recorded cases run from Python through the shim: 512/512.

## Checklist
- [ ] Bridge chosen by caller
- [ ] port.rs safe and runtime-free; bindings separate
- [ ] Panics caught at every export
- [ ] Errors mapped to the original's types
- [ ] Boundary types and buffer ownership documented
- [ ] Equivalence cases run through the wrapper

## Output
The bridge choice, the wrapper and the through-the-wrapper equivalence result.

## Avoid
- Letting `unwrap()` inside the port take down the host process.
- Testing only the Rust side and never the wrapper callers use.
