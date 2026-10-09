---
name: "binary-structure-assembly"
description: "Read binary structure and assembly fluently: formats, disassembly quality loops and decompiler-correction technique."
license: "MIT"
---

# Binary structure and assembly

Understand what a binary is made of and read it the way its compiler wrote it. Static craft is the backbone of every later stage.

## When to use
Any static analysis of executable artefacts: understanding file formats, disassembly, decompilation, data, and code lineage.

## Procedure
1. Map the format first: headers, sections/segments, symbols, relocations, imports, resources, certificates. Know what each part claims and verify the claims against bytes (entry point reachable? sizes consistent? overlays present?).
2. Establish the build: architecture, ABI, calling convention, compiler fingerprint, linkage (static/dynamic), presence of RTTI or symbols. Every later judgement is conditional on this step.
3. Disassemble with intent: functions are found by pattern and call-graph; find the boundary-missing regions and understand why (non-returning functions, opaque predicates, jumptables, data-in-code) before trusting surrounding code.
4. Maintain an analysis-quality loop: entropy/overview scan → error bookmarks → correct signatures (including non-returning marks, variadic overrides, custom conventions) → define structures/classes incl. vftables → re-decompile → re-check. Decompiler output is evidence to correct, never truth; `in_`/`unaff_`/`extraout_` variables, p-code leaking into views and addresses assigned to locals are standard defect signatures with standard fixes.
5. Data before code: type the memory (strings, constants, structures) the code touches; retyping data usually explains more than re-reading code.
6. Track lineage: when a family relation is suspected, run differential comparison (function-level matching by exact/similar signatures and reference structure, accepted only where semantics agree, not where scores merely look high).
7. Automate deliberately: headless, scriptable workflows repeat the loop over many artefacts; keep scripts deterministic, versioned and logged so their conclusions are reproducible.

## Decision rules
- A decompiled function you cannot explain in one sentence is not understood; dig or declare.
- Analysis assumptions (calling convention, return type, mutability) are recorded where they were changed, so corrections are auditable.
- Timeboxed rabbit-holing: when a region resists, note the resistance and move on; the call graph often explains it later.
- Prefer correcting the analysis over forcing the conclusion: if the decompiler disagrees with your reading, check the assumption before overriding output.

## Pitfalls
- Trusting decompiler output verbatim, especially around undefined behaviour and compiler corner cases.
- Reading x86-64 disassembly without the ABI: sizes, caller/callee-saved registers and flag semantics are where misreads begin.
- Treating packed/encrypted regions as if they were code.

## Done
A structural map of the artefact with a corrected, explained decompilation of the regions relevant to the question, documented assumptions, and stated residual blind spots.