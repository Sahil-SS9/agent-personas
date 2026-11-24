---
name: "recorded-behaviour-equivalence"
description: "Use on every port to Rust, even one function: run the original on edge-case and real inputs, save its exact outputs, replay them against the Rust and compare every output before calling the port correct."
license: "MIT"
---

# Recorded-behaviour equivalence

Step 3, and the proof for every later step. Tests that the port passes are not evidence unless they compare against the original on inputs the port was not tuned on. Published translators shipped wrong ports that their own checks accepted, mostly because the checks never ran the exposing input or compared only part of the output.

## Use when
- Before writing the port (record first), after every change to it, and before calling it done.

## DO NOT use when
- There is no runnable original (then write a characterisation suite from the spec and say the proof is weaker).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Generate inputs by type:** `scripts/edge_inputs.py i64 str --max 200` gives boundaries, Unicode traps, empty/long values. Add every input the original's own test suite uses and real-world samples. Add one input per trap that `trap_scan.py` lists (step 4).
2. **Record the original first:** write a small driver in the original's language that reads the inputs and prints each result (return value, out-parameters, stdout/stderr, exit code, files written, raised exception TYPE). C: compile with `-fsanitize=address,undefined`; an input where the C crashes or the sanitizer fires is undefined behaviour, so drop it from the comparison and say so. Save as `cases.jsonl`.
3. **Replay against the Rust:** a `#[test]` (or a driver binary) that runs every recorded case and compares EVERY output. Errors compare by type (both sides failing = agreement); a Rust panic never matches a recorded error.
4. **Hold out inputs:** keep a second batch of generated inputs you did not look at while fixing; run it at the end. A port that only passes the inputs it was repaired on is not proven.
5. **Test the check:** change one operator or constant in the port (a mutant) and confirm the comparison fails. If it does not, the comparison is too weak.
6. **Fix the port, never the recording.** An intended difference (fixing a bug of the original) needs the owner's yes and a written known-difference entry.
7. **Floats:** bit-identical results rarely survive operation-order changes. Use a tolerance only if the owner set one; never widen it to hide a mismatch. Integers and strings stay exact.
8. **Stalled?** Three edits in a row that gain no matching case: stop and show the remaining mismatches to the owner.

## Tools
`scripts/edge_inputs.py TYPE... [--max N]`: JSON list of argument tuples for recording.

## Worked example
Porting `slugify(s)` from JS. Recorded 214 cases (edge inputs plus the 31 from its Jest suite) with a Node driver printing `JSON.stringify(slugify(x))`. Rust replay: 209/214. Mismatches: `"Ǆemal"`, `"ﬁne"` (case mapping), three emoji inputs (JS splits surrogates). Fixed with explicit case mapping and UTF-16 handling; 214/214. Held-out batch of 100: 100/100. Mutant (`>=` to `>`): 6 cases fail, so the check bites.

## Checklist
- [ ] Inputs: typed edge cases + original's test inputs + real samples + one per listed trap
- [ ] Original recorded first (C under sanitizers; UB inputs dropped and noted)
- [ ] Every observable output compared; errors by type; no panics
- [ ] Held-out batch passes
- [ ] A mutant is caught
- [ ] Mismatches fixed in the port; intended differences approved and recorded

## Output
cases.jsonl, the replay test, and the counts: recorded N/N, held-out M/M, mutant caught.

## Avoid
- "cargo test passes" with tests you wrote from your reading of the code, never run against the original.
- Comparing only the return value when the original also writes stderr, files or an exit code.
