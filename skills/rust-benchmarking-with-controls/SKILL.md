---
name: "rust-benchmarking-with-controls"
description: "Bench the port against the original with the bridge included and controls on both sides; ship only on the measured verdict, and report losses honestly."
license: "MIT"
---
# Rust Benchmarking with Controls

## Use when
- Deciding whether a port ships, stays in shadow, or is reverted.
- Comparing per-call ports against batch ports.
- Any Rust performance claim needs to be made.

## Instructions

1. Bench against the original, bridge included: the caller's reality is the
   number that matters, not the Rust-side microbenchmark. Time the recorded
   cases on both sides, called the way the original's callers call.
2. Control, candidate, control: change exactly one thing between runs;
   keep the change only if both controls agree it is a win.
3. Compare all shapes before concluding: per-call port, batch port, and the
   original doing equivalent narrowing work. A batch port can win 20x where
   the same port per-call loses 3x — and a plain conversion loop on the
   results can cost more than the search itself. The verdict table shows
   every shape.
4. Report losses: ports that pass every gate and still lose on the bench
   (bridge cost exceeds the work) are a real outcome with a name — keep the
   unit behind the bridge or revert, and say why. A benchmark that never
   kills a port is not measuring.
5. Regression gates: the bench runs in CI for ported units; a perf change
   beyond tolerance fails the build like a behaviour change would.
6. State hardware and parallelism with every number: cores, allocator and
   thread count move these results more than most code changes.

## Stop conditions
- Never quote a Rust-side benchmark as the shipped speedup.
- Never ship a port the bench did not bless.
- Never report a win without the original's number beside it.

## Escalation
- A port that passes behaviour gates but loses the bench goes to the owner
  with the verdict table: revert, keep behind the bridge, or restructure to
  a batch port — each with its cost.
