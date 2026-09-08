---
name: "risk-register-manager"
description: "Build and maintain project risk registers with owners, triggers and re-scoring cadence."
license: "MIT"
---
# Risk Register Manager

## Use when
- A project kicks off or crosses a phase boundary
- Someone says "what could go wrong?" without a structured answer
- A near-miss or incident reveals an unmanaged risk class

## Instructions

1. Identify SOFTWARE-DELIVERY risks across the classes that actually kill
   software projects: integration (the #1 schedule killer), data migration,
   third-party dependency/API churn, key-person, technical-debt-driven
   change amplification, release-coupling (big-bang cutovers), and
   requirement volatility. Generic business risks register only when they
   block delivery.
2. Score each on likelihood x impact; for safety/financial exposure add the
   FMEA detection axis. The scoring conversation matters more than the number.
3. Every registered risk carries: owner, mitigation, and a TRIGGER — the
   observable condition that activates contingency ("we act when X"). A risk
   without a trigger is a worry, not managed risk.
4. Re-score at boundaries; retire risks explicitly with rationale. Register
   is visible to the team — hidden registers protect nobody.
5. Near-misses get registered too: they are free evidence about which risks
   are real.

## Stop conditions
- Never accept "we'll handle it if it happens" without naming the trigger
  and the pre-agreed action.
- Never let the register become a one-time kickoff artefact.

## Escalation
- High/High risks with no viable mitigation escalate immediately with
  options attached, not silently accepted.
