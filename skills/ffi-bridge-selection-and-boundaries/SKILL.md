---
name: "ffi-bridge-selection-and-boundaries"
description: "Choose the right bridge per language, keep callers' API unchanged, and record why every unported export stays behind."
license: "MIT"
---
# FFI Bridge Selection and Boundaries

## Use when
- Rust must be callable from an existing TypeScript, Python, Go, Ruby, Java
  or C codebase without changing callers.
- Deciding what can cross the bridge at all.
- Throughput matters and per-call ports keep losing.

## Instructions

1. Match the bridge to the host, not to fashion: Node-hosted code gets the
   Node binding layer; Python gets the Python binding (stable ABI where
   possible) with typed exceptions; Go goes through typed cgo calls; Ruby
   through its extension layer under the original modules; Java through
   typed JNI in wrapper classes with the original method names; C through
   plain extern declarations with the original names and a header.
2. Callers keep their API: the Rust lands behind a wrapper with the original
   signatures; the rest of the code changes nothing.
3. What cannot cross stays behind, WITH THE REASON RECORDED: values holding
   or typed as functions, generators and iterators, host regex objects,
   identity checks, unresolvable generics, code leaning on platform data
   (e.g. locale). The shadow module re-exports the original for those.
4. Structure crosses on a real wire, not loose JSON: generate the binary
   wire from the host types (aliases resolved through imports, parameter
   types inferred from defaults); JSON is the fallback only for shapes the
   wire cannot model.
5. For throughput, port the LOOP: generate a batch class that takes the
   items once, holds them in Rust, and runs the work over all of them on all
   cores per call. A per-call port of a small function usually loses to a
   JIT; the batch usually wins by a wide margin.
6. Batch crates should measure allocator choice: a different allocator can
   matter more than kernel tuning on multi-core batches.

## Stop conditions
- Never change caller signatures to suit the bridge.
- Never leave an unported export without its recorded reason.
- Never claim a per-call port is faster without the bench.

## Escalation
- Exports the owner wants ported but the bridge cannot carry are listed with
  their reasons and the options (restructure host-side, keep behind bridge,
  drop from scope) — the owner decides.
