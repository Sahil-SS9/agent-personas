---
name: "failure-replanning-and-escalation"
description: "Use when a worker or sub-agent overruns, fails, stalls or drifts, or when deciding whether to retry: stop and re-scope overruns, change the brief or agent after a failure, and escalate at the policy limit with an attempt ledger."
license: "MIT"
---

# Failure replanning and escalation

Step 6 (during execution). Most wasted runs come from steering a runaway worker or resending the same brief.

## Use when
- A worker exceeds its time or token budget, drifts out of scope, fails, or stalls.

## DO NOT use when
- The worker is within budget and scope: let it work.

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Keep an attempt ledger per task:** each dispatch's brief version, specialist, outcome and reason.
2. **Overrun or scope drift:** stop the worker and re-dispatch the task with a narrower brief that names what is already done and what is out of scope. Do not steer it with more messages and do not wait for "almost done". A stop-and-re-scope is not a failed dispatch.
3. **After a failure:** read the reason; change the brief (add the missing input, constraint or template) or route to a different specialist when the reason shows a capability gap. Never resend the same brief.
4. **Policy limit:** when the failed dispatches reach the owner's limit for a task, escalate to the owner with the ledger instead of trying again.
5. **Stalls:** no progress events for longer than the brief's budget counts as an overrun.
6. **Run `scripts/attempt_ledger.py ledger.json --max-dispatches <policy>`** to check the next move against these rules.
7. **Record each decision** as a ruling: what, why, cost if wrong.

## Tools
`scripts/attempt_ledger.py LEDGER.json --max-dispatches N`: next action (kill_and_respawn, wait, retry_new_brief, reroute_specialist, verify, escalate) with the reason. The limit has no default: use the owner's policy.

## Worked example
A summariser's brief allows 15 minutes; at 34 minutes it reports "nearly there, adding two more sources". Stop it; re-dispatch with: "Summarise only sources S1-S4 (S1-S3 drafts attached as out/sum-partial.md); no new sources; 10 minutes." The ledger records the stop as a re-scope, so the task still has its full number of dispatches left.

## Checklist
- [ ] Attempt ledger per task
- [ ] Overruns stopped and re-scoped, not steered
- [ ] Every retry changes the brief or specialist
- [ ] Escalation at the policy limit, with the ledger
- [ ] Rulings recorded

## Output
The ledger and the next action with its reason.

## Avoid
- "Let it finish, it's almost done" after a budget overrun.
- Sending the same brief a second time.
