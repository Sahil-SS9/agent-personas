---
name: "test-driven-development"
description: "Build production behaviour through witnessed RED, minimal GREEN and safe refactoring."
license: "MIT"
---
# Test-Driven Development

## Core rule

For production behaviour:

1. write one behavioural test first;
2. run it and observe the expected failure;
3. add the smallest production change;
4. run the focused test;
5. run the required wider suite;
6. refactor only while green.

A test that never failed for the intended reason does not prove the change.

## Scope

Use TDD for:

- new production behaviour;
- bug fixes;
- behaviour-changing refactors;
- changed error or boundary handling.

Ask before skipping it for:

- a throwaway spike;
- generated code;
- configuration-only work.

An approved spike must stay isolated and must be discarded. Start the production build again from a failing test.

## RED — prove the test can fail

Write one small test against public behaviour.

A valid RED run must:

- execute the intended path;
- fail because the behaviour is missing or wrong;
- show the expected assertion or outcome;
- use the actual defect state for a bug fix.

These are not valid RED evidence:

- import errors, syntax errors or fixture setup errors;
- a test that passes on its first run;
- a test added only after the implementation;
- a happy-path fixture that never reproduces the defect;
- a test that only checks a mock or comment.

If setup fails, fix the test setup and run RED again. Do not touch production code yet.

## If code was written first

Do not destroy unreviewed work blindly.

1. preserve the diff as non-gating reference;
2. remove or isolate it from the code under test;
3. write the wished-for behavioural test;
4. run the test against the pre-implementation state;
5. confirm the expected RED result;
6. implement from the test.

The preserved code-first diff is not evidence and must not shape the test contract.

## GREEN — make the smallest change

After valid RED evidence:

1. change only enough production code to satisfy the test;
2. run the focused test;
3. fix production code rather than weakening a valid test;
4. run the repository's required wider suite.

Focused GREEN without the required wider suite is **PARTIAL**, not complete.

Do not add unrelated features, abstractions or cleanup during GREEN.

## REFACTOR — stay green

Refactor only after focused and required wider tests pass.

During refactoring:

- keep behaviour unchanged;
- take one small step;
- rerun the focused test after each risky step;
- run the required wider suite before completion.

If a test fails, revert the last refactor or take a smaller step. Do not continue on a broken baseline.

## Bug-fix witness

A bug-fix test must contain the actual failing input or state.

Before changing source:

1. reproduce the defect;
2. make the test fail on that defect;
3. confirm the failure message matches it;
4. apply the fix;
5. confirm the same test passes;
6. run the wider suite.

A test that passes before and after the change is a placebo. Replace it with a real defect witness.

## Test quality

Prefer:

- public results over private implementation details;
- real code over broad mocks;
- one behaviour per test;
- stable fixtures over live system state;
- exact failure and side-effect assertions.

When a side effect is external, inject or sandbox its boundary. Never let a test mutate a real crontab, service, user config, live database or account.

## Decision states

- **PASS** — the complete requested cycle has valid RED, focused GREEN, wider-suite proof and a stable final diff.
- **PARTIAL** — a valid phase completed, but later required proof has not.
- **BLOCKED** — the next TDD step cannot proceed safely from the present state.
- **INVALID** — the claimed evidence does not exercise or prove the intended behaviour.

## Stop rules

Stop and correct course when:

- production code exists without a witnessed RED test;
- RED is a setup or collection error;
- a bug test does not reproduce the bug;
- focused GREEN is presented as complete without required wider tests;
- refactoring continues while tests fail;
- a test reaches live system state.

Do not rewrite a test merely to match an accidental implementation. Resolve the intended behaviour first.

## Report

```text
State: RED | GREEN | REFACTOR | COMPLETE | INVALID
Behaviour: <one sentence>
Observed proof: <exact test and result>
Missing proof: <next unmet gate>
Next action: <one smallest step>
```

## Done

A production change is complete when:

- the behavioural test existed first;
- the expected RED result was observed;
- minimal code produced focused GREEN;
- required wider tests passed;
- refactoring, if any, stayed green;
- no test touched live state;
- the final diff contains only intended source and test changes.
