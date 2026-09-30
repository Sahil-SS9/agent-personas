---
name: "constraint-compliance-audit"
description: "Prove compliance from what the system actually did — tool-call logs and side effects — because text-level compliance is undetectable and meaningless."
license: "MIT"
---

# Constraint compliance audit

## When to use
Someone asserts the agent followed the process, or an audit needs evidence of constraint adherence.

## Procedure
1. Define the constraints as observable properties over the run record.
2. Derive compliance from tool calls and side effects, not from the transcript's narration.
3. Compute exposure: for each violation, how long it existed and how many runs it affected.
4. Report detection lag, not detection count.
5. Where a constraint cannot be derived from logs, say so rather than approximating it from prose.

## Decision rules
- An agent narrating compliance is not evidence of compliance. Process compliance measured from text is provably undetectable.
- Detection counts are a vanity metric. Detection lag and exposure are the real ones.
- A rule count is not coverage; a large rule set with low effectiveness is the Forensics Trap.
- Prefer a small number of log-derived invariants over a large number of prose checks.

## Pitfalls
- Auditing the transcript instead of the run record.
- Reporting alerts fired as if they were violations caught.
- Claiming coverage for constraints that only exist in instructions.

## Done
Each constraint is expressed as a log-derived property, with measured exposure and detection lag, or is explicitly marked underivable.
