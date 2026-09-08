---
name: "release-readiness-manager"
description: "Run pre-release checks, release-day execution and post-release verification end to end."
license: "MIT"
---
# Release Readiness Manager

## Use when
- A release candidate is approaching its ship date
- Post-release health is unclear or nobody owns stabilisation
- Rollback has never been rehearsed for this service

## Instructions

1. PRE-RELEASE gate: reviews+QA green, regression/performance passed,
   docs and release notes current, security scans done, stakeholder sign-off
   recorded, and ROLLBACK REHEARSED — an untested rollback is no rollback.
2. Release DAY: verify environment parity, DB backup + migration with reverse
   scripts, live monitoring on logs/metrics, comms plan sent, feature flags /
   canary configured. Build binaries once, promote through environments.
3. Progressive delivery preference order: flags > canary > blue-green;
   gradual exposure with metrics segmented by cohort.
4. POST-RELEASE: production smoke tests on critical flows, error rates vs
   baseline, KPI tracking (crash rate, latency, uptime), feedback channels
   open, retrospective scheduled with owners for actions.
5. POST-RELEASE MONITORING owns release success measurement — software and
   product lens together:
   - Delivery health (DORA): lead time for changes, deployment frequency,
     change failure rate, failed-deployment recovery time. Watch tension
     pairs; never game one metric (Goodhart).
   - Error budget & stability: error rates vs baseline, SLO burn, crash
     rate, p95/p99 latency vs pre-release.
   - Product adoption funnel per feature: exposure -> activation ->
     retained use; cohort-segmented via feature flags.
   - User/stakeholder feedback: support ticket deltas by class, NPS/CSAT
     movement, qualitative themes from feedback channels.
   - Outcome metrics from the PRD: the success metrics committed BEFORE
     build, checked at agreed intervals (7/30/90 days) against targets;
     misses feed the Project Strategist as evidence, not blame.
6. Keep the checklist versioned per service; every release updates it with
   what was missed.

## Stop conditions
- Never ship without a rehearsed rollback path and a named owner for it.
- Never mark a release complete before post-release verification ran.

## Escalation
- Failed smoke tests in production trigger the rollback decision immediately
  with evidence — not after further monitoring debate.
