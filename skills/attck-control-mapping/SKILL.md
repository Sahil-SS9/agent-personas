---
name: "attck-control-mapping"
description: "Map every plausible attack tactic to a detection and a response; gaps are the work plan."
license: "MIT"
---

# ATT&CK control mapping

## When to use
Designing or auditing defensive coverage for an estate.

## Procedure
1. Inventory the estate: assets, data flows, trust relationships, identities. Unknown assets cannot be defended; inventory is a living control.
2. For each plausible ATT&CK tactic against this estate (initial access → impact), name: prevention control, detection (which log source, which alert), and response action.
3. Mark tactics with neither detection nor response as coverage gaps — the gap list is the work plan, ranked by likelihood and impact.
4. For each detection, verify the log source actually supports it: no log, no detection.
5. Layer defences: prevention reduces likelihood, detection reduces dwell time, response reduces impact. Single-control reliance is a finding.

## Decision rules
- Fundamentals before tooling: patching, least privilege, MFA, segmentation, tested backups stop the majority of real attacks.
- Every alert must map to a technique and an action; orphans get deleted.

## Pitfalls
- Copying a generic control framework without mapping to the actual estate.
- Buying detection that no one has time to tune.

## Done
An ATT&CK-mapped coverage matrix with named, ranked gaps and layered controls.