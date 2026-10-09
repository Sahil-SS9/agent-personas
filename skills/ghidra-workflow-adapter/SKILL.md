---
name: "ghidra-workflow-adapter"
description: "Drive Ghidra (GUI/headless/version tracking) as the reverse engineering specialist's static-analysis workbench, with an analysis-quality correction loop."
license: "Apache-2.0"
---

# Ghidra workflow adapter

Ghidra is the static workbench: disassembly, decompilation, differential matching and scriptable automation. The adapter structures its use; the specialist still owns the evidence. (Workflow structure adapted from Apache-2.0 material: NSA Ghidra's GhidraClass courses; notices carried in the repo.)

## When to use
When Ghidra is installed and in scope for the artefact. Requires: Ghidra present (version recorded), owner scope permitting the analysis environment.

## Procedure
1. Import and analyse as configured: headless (`analyzeHeadless … -import/-process [-preScript/-postScript -scriptPath -readOnly -max-cpu]`) for scripted triage; GUI for interactive correction. Record tool version and analysis options with the evidence.
2. Run the analysis-quality loop: entropy/overview sidebar → error bookmarks → fix non-returning/inline/signature/class-structure/vftable assumptions → re-decompile → diagnostic scripts for what still resists. Every manual correction is recorded where it was made.
3. Use version tracking for lineage: correlators (exact/similar data, symbol, function; reference-based) with the accept-only-with-semantic-corroboration rule; export the match table as evidence.
4. Emulation path (with the debugger integration): program-image emulation for rehearsal of specific paths without live execution; initialise state deliberately; unimplemented userops are recorded as limits, not hidden.
5. Script the repeated loop in Java/Jython; scripts versioned and deterministic; their outputs cite the script version.

## Decision rules
- Decompiler output is never quoted as fact without the correction loop having run.
- A signature override is evidence: record before/after.
- If Ghidra is unavailable or the artefact needs a different loader, say so and fall back to format-level tools, not to pretending.

## Pitfalls
- Believing auto-analysis: packed regions, opaque predicates and unknown non-returning functions silently corrupt nearby decoding.
- Unversioned scripts making conclusions unreproducible.

## Done
A scripted or recorded Ghidra pass with corrections logged, match tables exported where used, tool version recorded and residual blind spots stated.