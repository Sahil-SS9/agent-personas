---
name: "rail-runtime-wiring"
description: "Wire rails into the live path so they actually run — with ordering, timeouts, telemetry and a kill switch that works."
license: "MIT"
---

# Rail runtime wiring

## When to use
Moving a rail from design into production, or auditing whether a rail is truly in the path.

## Procedure
1. Place the rail in the execution path, not beside it.
2. Define ordering when multiple rails apply, and whether they compose or short-circuit.
3. Set timeouts and a fail-fast boundary so one slow rail cannot stall the pipeline.
4. Emit telemetry: every decision with rail id, input class, verdict, latency and action taken.
5. Provide a single switch to disable the rail without a deploy.

## Decision rules
- A rail that runs after the action is a log, not a rail.
- If disabling requires a code change, the kill switch does not exist.
- Telemetry must record the action taken, not just the verdict, or you cannot prove follow-through.
- Rails that cannot explain their own firing will be disabled by operators within a week.

## Pitfalls
- Wiring rails only into the happy path, leaving retries and background jobs unguarded.
- No timeout, so a degraded provider stalls the agent.
- Logging verdicts without the resulting action.

## Done
A rail can be shown firing in production telemetry, disabled by one switch, and timed out without stalling the pipeline.
