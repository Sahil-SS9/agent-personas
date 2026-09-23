---
name: "workflow-incident-readiness"
description: "Design automations to be operable during incidents: ownership, runbooks, drills."
license: "MIT"
---

# Workflow incident readiness

## When to use
Any automation that production depends on, before it is declared done.

## Procedure
1. Assign ownership and on-call expectations explicitly: who is paged, at what severity, with what escalation path. An automation without an owner is an unexploded device.
2. Write the runbook as part of the deliverable: purpose, inputs, normal output, failure signatures, diagnosis steps, kill switch. The kill switch must be tested.
3. Apply the 3Cs to failures: coordinate (clear line of command), communicate (declared early, updates as you go), control (working record of debugging while it happens).
4. Declare incidents early: a silently failing automation is worse than a loudly broken one; alert on the automation itself, not just its outputs.
5. Feed failures back: blameless postmortem after every automation-caused incident; the recurring-manual-failure fix is usually another stabilised, automatable path.
6. Drills: periodically rehearse failure with real tools at low stakes; each drill ends with a what-broke-in-the-process report.

## Decision rules
- Kill switches are part of done, not a nice-to-have: untested kill switch = unfinished automation.
- Alert fatigue is a design defect: every alert must be actionable and unique.

## Pitfalls
- Runbooks written after the first incident, from memory.
- Automations only their author can operate.

## Done
Owned, runbooked, drilled automation with tested kill switch and a feedback loop from failures into design.