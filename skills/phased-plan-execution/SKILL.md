---
name: "phased-plan-execution"
description: "Execute phased implementation plans with batched."
license: "MIT"
---
# Phased Plan Execution

## When to use
Execute phased implementation plans with batched.

## Method
1. Freeze the approved plan, baseline revision, phase order and completion criteria. Distinguish locked decisions from unresolved choices; do not silently redefine scope.
2. Execute prerequisite discovery first. For each phase, map the real integration points, write a failing behavioural test, make the smallest change and run the required regression suite.
3. Verify the real delivery path, not only standalone modules. Record code, commands, outputs, remaining failures and the exact revision tested.
4. Resolve implementation failures within the phase. Escalate changes to approved scope, budget or risk; a failed test is not automatically a need for more permission.
5. Finish with one consolidated report. Keep deployment, publication and live configuration activation separate from build completion.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
