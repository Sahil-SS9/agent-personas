---
name: "project-health-and-maintainer-load-review"
description: "Run a recurring health and load review: backlog age, attention distribution, community-health files, open-source health scorecard, and maintainer capacity."
license: "MIT"
---

# Project health and maintainer load review

## When to use
On a recurring cadence — monthly for an active project, quarterly for a quiet one — or when the maintainer is burning out.

## Procedure
1. Measure the backlog and, more importantly, its age distribution.
2. Measure where attention went and what is waiting on whom.
3. Audit the community-health file set: contribution policy, code of conduct, security policy, ownership, support, governance and funding configuration, checking each is present and correctly located.
4. Run an open-source project health scorecard and read it by severity tier rather than as a single number.
5. Review maintainer load: hours, interruptions, and burnout signals.
6. Decide what to stop doing.

## Decision rules
- An unowned queue is the failure mode; ownership matters more than count.
- Measure response latency and age, not just volume.
- A single aggregate score is not health; use the severity tiers and the failing checks.
- Reducing scope deliberately is a legitimate outcome. Record it, so the next review does not re-litigate it.
- Health work is scheduled, not done opportunistically between fires.

## Pitfalls
- Treating a green badge as health.
- Adding process that increases load rather than reducing it.
- Ignoring maintainer capacity because the queue looks acceptable.
- Placing project files in locations their tooling does not read.

## Done
The review names the largest load source, one thing to stop, one thing to fix, and the date of the next review.
