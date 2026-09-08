---
name: "scheduled-job-audit"
description: "Audit scheduled jobs from intent through verified delivery."
license: "MIT"
---
# Scheduled Job Audit

## When to use
Audit scheduled jobs from intent through verified delivery.

## Method
1. Inventory enabled schedules, timezones, overlap policies, inputs, credentials, output destinations and the reason each job exists.
2. Trace schedule to invocation, result, delivery and acknowledgement. A scheduler success does not establish useful output or successful delivery.
3. Correlate logs over one explicit time window using run identifiers. Distinguish historical failures, current unresolved failures, retries and duplicate notifications.
4. Test cancellation, timeout, missed runs, overlapping executions and output suppression with isolated fixtures rather than live schedules.
5. Propose the smallest repair and preserve prior records. Activation or schedule changes require approval and a verified rollback path.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
