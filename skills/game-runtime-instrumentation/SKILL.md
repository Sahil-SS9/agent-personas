---
name: game-runtime-instrumentation
description: "Observe game behaviour in authorised local tests."
version: 0.1.0
author: Hermes
license: MIT
---

# Game runtime instrumentation

Observe a game or mod in an authorised offline/local runtime to answer a bounded question. This skill does not provide anti-cheat bypass, multiplayer manipulation or credential access.

## Procedure
1. Snapshot saves and configuration; record build, loader, platform and mod list.
2. Define one observable: load event, asset lookup, script call, state transition, performance cost or crash.
3. Use the least invasive logger, profiler, debug console or documented hook available. Bound duration, output and filesystem/network access.
4. Compare baseline, mod-enabled and no-op-control runs. Separate mod effects from loader and environment effects.
5. Capture logs and traces with secrets and personal data redacted.
6. Remove instrumentation and verify the test environment returns to the snapshot.

## Verification
Provide baseline/control/candidate traces and a statement of what the instrumentation cannot observe.
