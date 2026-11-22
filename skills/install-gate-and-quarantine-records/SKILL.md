---
name: "install-gate-and-quarantine-records"
description: "Every trust decision is a recorded artefact: install gates, quarantine with reasons, revocation triggers — no silent installs, no silent blocks."
license: "MIT"
---
# Install Gate and Quarantine Records

## Use when
- Codifying the vetting verdict into a fleet gate.
- A component needs blocking or removal.
- Someone asks "why is this blocked?" weeks later.

## Instructions

1. The gate record IS the decision: for every component the fleet could
   load, the record holds the vetted version, evidence examined, risk
   tier, decision (allowed / blocked / quarantined / revoked), the deciding
   party, and the date.
2. Quarantine is a first-class state: blocked-with-reason, with the quoted
   evidence and the exact condition that would lift it. A silent block and a
   silent install are the same failure in opposite directions.
3. Revocation triggers are written at install time: what future event would
   invalidate this trust (an update, a dependency change, a behaviour
   report, an advisory) — so the gate knows before it happens.
4. Proportionality is recorded, not implied: the tier says how much scrutiny
  was applied, so a later reader knows what the verdict did and did not
   cover.
5. The record survives the component: when a component is removed, the
   record stays, so re-acquisition starts with history rather than amnesia.
6. Audit shape: a gate record answers in one read — what is installed, at
   which version, trusted to do what, decided by whom, revocable by what.

## Stop conditions
- Never install, block or revoke without the record entry.
- Never quarantine without the reason and the lift condition.
- Never record a decision as "owner approved" without the owner's explicit
  approval trace.

## Escalation
- Behaviour reports from the fleet (an agent doing something a component's
  instructions should not cause) trigger a re-vet of the suspect component
  with the report attached.
