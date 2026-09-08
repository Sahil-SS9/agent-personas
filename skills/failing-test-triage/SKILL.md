---
name: "failing-test-triage"
description: "Decide if a red test is a real bug or a stale test."
license: "MIT"
---
# Failing Test Triage

## When to use
Decide if a red test is a real bug or a stale test.

## Method
1. Reproduce the exact failure on the actual revision with the correct interpreter and documented command. Capture the failing assertion and environment.
2. Trace the assertion to the current behavioural contract. Distinguish a code defect, stale expectation, broken fixture, dependency failure and test-order leak.
3. If the contract changed legitimately, update the test with evidence of that decision; otherwise repair production behaviour. Never weaken an assertion just to obtain green output.
4. For a bug, preserve a witnessed failing regression test, make the smallest fix and rerun the focused test and relevant wider suite.
5. Keep unrelated baseline failures visible. Report classification and evidence, not a blanket claim that the tests are wrong.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
