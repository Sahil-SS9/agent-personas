---
name: game-runtime-instrumentation
description: "Observe game behaviour in authorised local tests."
version: 0.2.0
author: Hermes
license: MIT
---

# Game runtime instrumentation

Observe a game or mod in an authorised offline/local runtime to answer a bounded question. Never attach to anti-cheat-protected or online multiplayer processes, bypass protections, access credentials or manipulate a live service.

## Procedure
1. Snapshot saves, configuration and install metadata to a disposable, hashed fixture; verify restore before changing anything.
2. Define one question, observable signal, time/resource budget and stop condition. Use a no-op control with the same loader.
3. Prefer documented loader hooks/logging. Capture only required events; redact usernames, tokens, paths and personal data.
4. Record build, loader, mod list, environment, seed/time and instrumentation version.
5. Compare control and treatment traces, separating causal observations from timing noise. Repeat once before claiming a stable result.
6. Stop on crash, unexpected network access, integrity warning, anti-cheat signal or scope drift; preserve logs and restore the fixture.

## Verification
Evidence includes exact launch context, control/treatment traces, redaction check, replay/minimisation result and restore proof. Runtime observation shows a witnessed path, not exhaustive behaviour.
