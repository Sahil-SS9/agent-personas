---
name: "port-profiling-and-hot-loop-selection"
description: "Profile the real workload before porting anything: find the hot loops, check the port is worth it, and pick the loop over the function."
license: "MIT"
---
# Port Profiling and Hot-Loop Selection

## Use when
- Anyone proposes "rewrite it in Rust" for speed.
- A workload is slow and the fix is not yet chosen.
- You need to decide WHAT to port, in which order, before any code moves.

## Instructions

1. Profile the real workload first — the language's own profiler over the
   actual bench or production path, not a synthetic loop. Output: hot
   functions by inclusive time, their callers, and which loops batch well.
2. Check what the hot code already is: code that is already compiled or
   JIT-shaped (Cython, numba, JAX, long-running JIT hot paths) gains little
   from a per-item port — say so and stop there, unless the batch plan in
   step 3 shows the win; then the port is the batch, judged on measured
   throughput.
3. Prefer the loop over the function: a Rust function called once per item
   pays the bridge once per item and routinely LOSES to a JIT. What wins is
   moving the whole loop — items cross once, all the work stays in Rust, and
   it can use all cores.
4. Rank candidates by measured inclusive time and batchability; port the
   hot-and-batchable first. A small hot inner loop beats a large cold module.
5. State the expected win before porting: from the profile (share of runtime
   the candidate owns) and the batch plan (items per call, cores). The
   estimate is a hypothesis the final bench confirms or kills.
6. Compiled originals (Go, Java): the default is to stop, because the
   per-item work is already fast; a batch port is justified only when the
   measured plan from step 5 shows the win by core count, and that plan is
   recorded before the port starts.

## Stop conditions
- Never start a port without a profile of the real workload.
- Never promise a speedup before the bench; per-call ports can be slower
  than the original.
- Never port cold code because it is easy to port.

## Escalation
- When the profile shows no hot loop worth moving, report that the original
  should stay, with the profile attached — a declined port is a result.
