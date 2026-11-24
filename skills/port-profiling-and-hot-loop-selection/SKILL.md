---
name: "port-profiling-and-hot-loop-selection"
description: "Use when asked to rewrite or move code to Rust for speed or performance, before choosing what to port: profile the real workload and pick the hot unit worth porting. Skip when the unit to port is already given."
license: "MIT"
---

# Port profiling and hot-loop selection

Step 1. Which code to port is a property of how it is called, not of how it looks. Porting the wrong unit, or a fine-grained leaf behind an expensive bridge, makes callers slower.

## Use when
- The goal is speed, memory or safety for part of an existing program, and the unit to port is not yet chosen.

## DO NOT use when
- The owner already named the unit and the reason (go to port-plan-and-decision-records), or the task is a whole-app rewrite (still profile, but plan waves in step 2).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Run a real workload under the language's own profiler:** Node `node --cpu-prof`, Python `python -m cProfile -o prof.out` then `pstats` sorted by cumulative time, Go `go test -cpuprofile`, C `perf record`/`perf report`. Use production-like inputs, not a toy.
2. **Rank functions by inclusive time, with their callers and call counts.** Note the argument that varies per call: a function called 50,000 times from one loop is a batch candidate, not a per-call port.
3. **Estimate the crossing cost.** Every call across the bridge copies arguments and results. For fine-grained functions this cost dominates; prefer porting a bigger unit (the loop and its callee) or a batch API (items cross once, results come back in one array).
4. **Exclude what should stay:** UI and editor-host code, code with callbacks into the host language, generics/iterators/closures crossing the boundary, and units with no measurable share of time.
5. **Write the selection:** unit, its share of time, call pattern (per-call or batch), expected crossing cost, and what stays in the original.

## Worked example
A Python log analyser spends 71% of run time in `classify(line)`, called once per line from `for line in f`. Each call does 2 µs of work; a PyO3 call costs about the same in conversion. Porting `classify` alone would roughly break even. Port `classify_all(lines) -> list[str]` instead: lines cross once, results return once.

## Checklist
- [ ] Profile from a real workload saved
- [ ] Top functions ranked by inclusive time with callers and call counts
- [ ] Crossing cost considered; batch or larger unit chosen where calls are fine-grained
- [ ] Exclusions listed
- [ ] Selection written down

## Output
The chosen unit, its measured share of time, the call pattern and what stays in the original.

## Avoid
- Choosing by code shape ("it has loops") instead of measurement.
- Porting a leaf called millions of times per request without batching.
