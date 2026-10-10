---
name: "analysis-capability-ladder"
description: "Pick the strongest analysis level actually available (tool-less to decompiler to integration layer to runtime), state it, and finish the report within budget."
license: "MIT"
---

# Analysis capability ladder

The specialist's judgement is the same at every level; what changes is how much of the artefact it can see. Detect the level, use the best one in scope, say which one, and let the level set the confidence ceiling. Tools named below are current examples, not requirements; any tool that does the same job counts.

## When to use
At the start of every investigation, and again whenever a question needs evidence the current level cannot reach.

## Procedure
1. Detect what is installed and in scope; do not assume. Record name and version of anything used.
2. Choose the highest level the question needs and the scope allows:
   - Level 0, format tools (always available): strings, symbol/section listing, raw disassembly, hex view, a contained run. Reaches small binaries and confirms facts; on large or optimised code it cannot see structure. Confidence ceiling: claims about control flow are inferred unless byte-verified.
   - Level 1, decompiler (for example Ghidra headless, rizin/radare2 with a decompiler plugin, IDA, Binary Ninja): readable pseudocode, functions, references. The default workhorse once installed. Pseudocode is decompiler output, not source; types and names are guesses until corrected.
   - Level 2, integration layer (for example REA): wraps a decompiler and adds evidence records, callers/callees, explicit limitations, and app/web/.NET coverage. Use when present; it adds bookkeeping, not new truth.
   - Level 3, runtime (for example gdb, Frida, process capture): observed behaviour. Only inside owner-authorised isolation.
3. Read at the level's natural unit: functions at Level 1-2, not whole-binary dumps. Ask for one function or one region at a time.
4. Promote a finding only with corroboration from a second view (decompiler claim + bytes, or static claim + a contained run).

## Finishing discipline
- Keep working notes short; do not hand-decode long instruction runs when a higher level can show the same thing, and do not narrate arithmetic.
- Budget: by the time about two-thirds of the tool budget is spent, stop exploring and write the report. Unanswered questions go under unknowns.
- The final message is always the report. Never end on a tool request, never write or imitate tool output yourself.

## Decision rules
- The report states the level used and what that level could not show.
- A missing tool lowers confidence; it never licenses guessing.
- If only Level 0 is available on a large or optimised binary, say the result is partial instead of over-reading.

## Pitfalls
- Treating Level 2 bookkeeping as extra evidence: it is the same decompiler underneath.
- Escalating to runtime when static evidence already answers the question.

## Done
A report that names its level and tools, reaches a verdict within budget, and lists what a higher level would add.
