---
name: "cleanup-cadence-and-new-debris-monitoring"
description: "Run hygiene as a recurring service with alerting on new debris, not as an occasional rescue when the disk fills."
license: "MIT"
---

# Cleanup cadence and new debris monitoring

## When to use
After the first cleanup, to stop the second rescue being necessary.

## Procedure
1. Set a cadence by risk: weekly for agent-heavy workstations, monthly for stable trees, quarterly for archives.
2. Track a small set of signals: free space, growth rate by directory, count of unattributed items, quarantine age.
3. Alert on rate of change rather than absolute threshold, so you are warned before the disk is full.
4. Review the register's unknown items each cycle rather than only the new ones.
5. Report progress in reclaimed space and items retired, with what remains.

## Decision rules
- Alert on growth rate; an absolute threshold fires too late.
- A sweep that leaves the register's unknowns untouched is maintenance, not hygiene.
- Cadence must match how fast the tree decays; a monthly sweep on a daily-changing tree is theatre.
- Every cycle should end with fewer unknowns or an explicit decision to keep them.

## Pitfalls
- Only cleaning when something breaks.
- Monitoring total disk use and missing one directory growing steadily.
- Letting quarantine grow without bound because nothing expires.

## Done
A cadence is scheduled with rate-based alerts, and each cycle reduces unknowns or records a decision to retain them.
