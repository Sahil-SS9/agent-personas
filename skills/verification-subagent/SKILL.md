---
name: "verification-subagent"
description: "Use when reviewing or accepting a worker's or sub-agent's output, or before other tasks depend on it: an independent verifier checks it against the done check, and dependants wait until it passes."
license: "MIT"
---

# Verification subagent

Step 7. A worker's own "done" is a claim. Verification is its own failure category in multi-agent systems.

## Use when
- A worker reports done; before merging, before starting dependents, before reporting to the owner.

## DO NOT use when
- Single-agent trivial lookups with a checkable done_check you run yourself.

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Block dependents** until the output is verified.
2. **Give the verifier a fresh context:** the brief's objective, the done_check, the output artefact. Not the producer's reasoning.
3. **The verifier is a different agent from the producer,** ideally with a different specialism (tester or reviewer for code, fact-checker for research).
4. **Check against the done_check, end state first:** files exist, tests pass, claims match their cited sources, required facets are covered.
5. **Outcome:** pass -> release dependents; fail -> back to failure-replanning-and-escalation with the verifier's findings as the reason.
6. **Record:** verifier, what was checked, result.

## Worked example
The backend worker says "endpoint done". The tester verifier runs the done_check (`pytest tests/test_exports.py`) in a fresh context: 2 failures (CSV header order). Dependents (docs, end-to-end test) stay blocked; the task is re-dispatched with the failing tests attached.

## Checklist
- [ ] Dependents blocked until verified
- [ ] Verifier independent of the producer, fresh context
- [ ] Checked against the done_check (end state)
- [ ] Result recorded; failures fed back as the retry reason

## Output
Verification record per task.

## Avoid
- Starting dependents on a self-reported "done".
