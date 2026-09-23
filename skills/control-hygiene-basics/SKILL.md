---
name: "control-hygiene-basics"
description: "Enforce the boring fundamentals that stop most real attacks."
license: "MIT"
---

# Control hygiene basics

## When to use
Continuous baseline hygiene for any estate; before any advanced security investment.

## Procedure
1. Patch discipline: criticals on a defined SLA; exceptions documented with compensating controls.
2. Least privilege everywhere: identities, service accounts, keys. Rotate; remove standing access; no shared credentials.
3. MFA on all human access; phishing-resistant factors for privileged roles.
4. Network segmentation: blast-radius boundaries between zones; no flat networks.
5. Backups: automated, offsite/immutable copies for ransomware scenarios, and TESTED restores on a schedule (a backup never restored is a hope, not a control).
6. Asset inventory and change management: every change reviewable, every asset owned.

## Decision rules
- A control that is not tested is not a control.
- Exception registries with expiry, or exceptions become the norm.
- Security tooling decisions follow the same evaluator rigour as any tool adoption.

## Pitfalls
- Shiny-tool purchases while MFA is missing somewhere.
- Backup policies without restore drills.

## Done
Documented, evidenced fundamentals with an exception registry and tested restores.