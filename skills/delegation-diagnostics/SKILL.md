---
name: "delegation-diagnostics"
description: "Diagnose dispatch routing failures in agent systems."
license: "MIT"
---
# Delegation Diagnostics

## When to use
Diagnose dispatch routing failures in agent systems.

## Method
1. Trace the full route from user request to dispatcher, selected worker, context, tools, execution and return delivery.
2. Capture identifiers and timestamps for the same task. Distinguish wrong routing, incomplete brief, unavailable tools, timeout, worker failure and lost response.
3. Use an isolated representative task to reproduce the earliest failing boundary. Do not blame a model when the worker never received the required input.
4. Repair only the verified defect, then rerun the route end to end and inspect the actual returned artefact.
5. Do not widen permissions, bypass no-delegation instructions or launch repeated fan-out while diagnosing a routing failure.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
