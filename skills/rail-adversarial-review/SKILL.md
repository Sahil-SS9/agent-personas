---
name: "rail-adversarial-review"
description: "Attack the rails themselves: verify the verifier, and produce rail-breach findings rather than exploit reports."
license: "MIT"
---

# Rail adversarial review

## When to use
Before trusting a rail with a real harm, and periodically afterwards.

## Procedure
1. Enumerate how input reaches the behaviour the rail is supposed to stop.
2. Attempt bypasses adapted to the rail: encoding, paraphrase, intent manipulation, split payloads across steps, tool-result injection.
3. Attempt rail denial: slow it, exhaust its quota, trigger its fail-open path.
4. Check the monitor itself: can the observed system write the telemetry the monitor reads?
5. Report breaches with the path taken and the rail that should have stopped it.

## Decision rules
- Verify the verifier. A monitor whose input the monitored system controls is not a control.
- Test the fail-open path adversarially; an attacker will.
- Report rail breaches as control findings, never as exploit write-ups. No working exploit leaves this skill.
- Bypass found once is not a bypass; reproduce it and record the distribution of attempts.

## Pitfalls
- Testing only obvious payloads, which every rail catches.
- Assuming the monitor's data source is trustworthy.
- Fixing the specific payload rather than the class of bypass.

## Done
Each rail has a documented bypass attempt set, the result at the current version, and any breach recorded with its path and proposed hardening.
