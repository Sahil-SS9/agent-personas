---
name: "frida-tracing-adapter"
description: "Use Frida for authorised dynamic instrumentation: hooking, tracing and memory inspection under containment and anti-analysis awareness."
license: "Apache-2.0"
---

# Frida tracing adapter

Frida instruments running processes: API hooks, memory inspection, behaviour tracing. Powerful, invasive, and fingerprintable. (Adapter structure original; Frida is third-party tooling referenced, not embedded.)

## When to use
Authorised runtime investigation where in-process observation answers the written question better than external monitoring. Requires: containment proven, owner authorisation for dynamic analysis, Frida available in the analysis environment.

## Procedure
1. Plan hooks from the static analysis: which functions, which stages (crypto, network, file, process APIs), what to record (args, buffers with sizes, return values, call stacks). Avoid hooking everything — noise is its own anti-forensic problem.
2. Expect detection: sleeps, ptrace checks, anti-debug heuristics. Record detection-attempted observations as findings; prefer early instrumentation over late attachment where the plan allows.
3. Capture payloads and decoded data with hashes at the hook point; a captured decrypted buffer outranks a static guess about the cipher.
4. Trace the injection/launch chain specifically when the question is security-behavioural: module loads, memory protection changes, thread starts — correlated with the static mechanism map.
5. Save scripts and captures as evidence with versions; report what instrumentation may have altered (timing, anti-analysis triggers).

## Decision rules
- If instrumentation disturbs execution (anti-analysis fired), report the observation with both instrumented and uninstrumented evidence where they conflict.
- Hooking belongs to the runtime investigation member's containment rules; the adapter never relaxes them.

## Pitfalls
- Reporting hook-induced artefacts (stubs, trampolines) as sample behaviour.
- Over-hooking until the sample times out or behaves differently.

## Done
Hook plan + captures with hashes + anti-analysis notes, all correlated to static findings, tool version recorded.