---
name: "rust-benchmarking-with-controls"
description: "Use when asked whether a Rust port is faster, or to benchmark Rust against the original: same inputs, bridge cost included, warm-up, repeated runs and a ship / keep original / port more verdict."
license: "MIT"
---

# Rust benchmarking with controls

Step 8. Speed is not correctness and is measured separately, after the gate passes. Many correct ports are slower per call.

## Use when
- After the gate, when the reason for the port is speed or memory.

## DO NOT use when
- The port is not yet equivalent (benchmarks of wrong code are meaningless).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Benchmark what callers experience:** call through the bridge from the original's process, with the same inputs for both sides; decode inputs once outside the timed region.
2. **Control the run:** warm-up, many samples, the same machine and build profile (`--release`), nothing else running. Rust side alone: criterion.rs (warm-up, statistical comparison against a saved baseline).
3. **Report per-call and per-batch times** with spread, for the original and the port.
4. **Verdict:** ship if the port is clearly faster for callers; keep slower functions in the original; or port a bigger unit / batch when per-call crossing dominates. Never ship a port that makes callers slower without saying so.
5. **Memory:** if memory was the goal, measure peak RSS for the same workload.

## Worked example
`fuzzy_score` via napi: original 0.9 µs/call, port 1.4 µs/call (crossing dominates): slower. Batch API over 50,000 items: original 45 ms, port 6 ms on 8 cores. Verdict: keep per-call function in JS, ship the batch API, and change the search loop to use it.

## Checklist
- [ ] Gate passed first
- [ ] Measured through the bridge, same inputs, decode outside timing
- [ ] Warm-up, repeated samples, release build
- [ ] Per-call and batch numbers with spread
- [ ] Verdict written

## Output
Benchmark table and verdict.

## Avoid
- Timing only the Rust function and claiming the caller gets that speed.
