---
name: "rail-failure-mode-and-budget"
description: "Specify how each rail fails, and give it a false-action and latency budget so it cannot silently degrade into either a rubber stamp or a wall."
license: "MIT"
---

# Rail failure mode and budget

## When to use
Before a rail goes live, and when reviewing a rail that is triggering too much or too little.

## Procedure
1. For each rail, state the failure mode: fails open, fails closed, or fails noisy.
2. Define the false-action rate budget and the maximum added latency.
3. State what happens when the rail itself is unavailable (provider down, model missing, quota exhausted).
4. Define the degraded state and who is told.
5. Test the failure path deliberately, not just the happy path.

## Decision rules
- Fails-open is acceptable for filters and unacceptable for destructive actions. Decide per rail, not per system.
- An unavailable rail must have a defined behaviour; undefined means it will fail whichever way surprises you.
- Latency budgets are part of the rail's contract; a rail that adds ten seconds will be disabled by operators.
- Over-triggering is a failure, not conservative safety, once it drives users to work around the rail.

## Pitfalls
- Testing only the passing case.
- A rail that fails closed on an internal error and blocks all traffic.
- No owner for the rail's availability.

## Done
Every rail states its failure direction, its budgets, its unavailability behaviour, and has a witnessed failure-path test.
