---
name: "systematic-debugging"
description: "Find and prove root causes before applying one verified fix."
license: "MIT"
---
# Systematic Debugging

## Core rule

Do not change production code until evidence identifies a root cause.

A plausible explanation is not a root cause. A root cause is supported when a controlled test changes only the suspected cause and the failure changes as predicted.

Use this process for bugs, failed tests, build failures, performance problems, integration faults and unexpected runtime behaviour.

## Decision states

- **PASS** — the requested closure is supported by a complete operational resolution or a verified root-cause fix.
- **PARTIAL** — useful investigation or repair evidence exists, but a required later gate remains.
- **BLOCKED** — safe progress cannot continue until a reproducible signal, missing artefact, access or architectural decision exists.
- **INVALID** — the proposed cause, fix or proof is contradicted, guesses without evidence, or tests the wrong seam.

## 1. Build a trusted feedback loop

Before proposing a fix, create the fastest reliable signal that exercises the symptom:

- focused failing test;
- repeatable CLI or HTTP request;
- captured trace replay;
- headless UI assertion;
- throwaway harness;
- old-versus-new differential;
- bisection or seeded stress loop.

The loop must report the actual symptom, not merely “did not crash”. Record the exact command, input, output and exit state.

### Intermittent failures

Increase the reproduction rate before guessing:

- repeat the trigger;
- pin time and randomness;
- add controlled concurrency or delay;
- capture a real payload or trace;
- isolate filesystem, network and shared state.

A one-per-cent anecdote is not a safe repair signal. If a useful loop cannot be built, stop and request a log, trace, dump, recording, reproduction environment or permission for temporary instrumentation.

## 2. Trace the failure

Read the full error and stack trace. Do not work from a copied last line.

Then inspect:

1. exact reproduction steps;
2. recent code, dependency and configuration changes;
3. process start time versus source and config modification times;
4. input and output at every component boundary;
5. the origin and transformation of the first bad value;
6. a similar working path in the same system.

In a multi-component path, trace end to end. A healthy API response does not prove the adapter or rendered UI is healthy.

### Stale processes

If the running process predates the relevant source or configuration change, test staleness directly:

1. record process and source identity;
2. restart only the proven stale process within existing authority;
3. rerun the exact reproduction repeatedly;
4. verify the process loaded the expected source and config.

If that alone resolves the incident and repeated checks pass, record an operational stale-process resolution. Do not invent a code fix.

## 3. Test ranked hypotheses

Write three to five specific, falsifiable hypotheses. Rank them by evidence and likelihood.

For each hypothesis:

1. state the predicted observation;
2. change or bypass one variable in an isolated environment;
3. rerun the same feedback loop;
4. record whether the prediction held;
5. discard disproved hypotheses instead of patching them.

Do not bundle several speculative changes. A failed hypothesis is new evidence, not permission to layer another fix on top.

## 4. Confirm the root cause

A root cause is confirmed only when evidence shows:

- where the failure enters the system;
- why the current behaviour follows;
- one controlled cause change alters the symptom as predicted;
- competing explanations are weaker or disproved.

At this point the investigation can advance to repair. It is not yet a proven fix.

## 5. Repair at the correct seam

Before production changes, write a regression test or replay at the seam where the real defect occurs.

The proof must:

- reproduce the actual input and state;
- fail before the fix for the reported reason;
- exercise the real call path;
- avoid live user or system state.

A helper unit test that passes before and after an integration failure is not proof. If no correct seam exists, stop and create one or record the architectural gap.

Then:

1. make one root-cause change;
2. rerun the focused regression proof;
3. rerun the required wider suite;
4. rerun the original reproduction;
5. inspect the final diff and residue.

Do not weaken the test to match the accidental implementation. Do not mix refactoring or unrelated cleanup into the fix.

## 6. Rule of three

Count attempted fixes.

After three failed fixes:

- stop applying patches;
- preserve the new evidence;
- review the architecture, hidden state and missing seams;
- ask for a decision before a fourth implementation attempt.

A fourth conditional on top of unexplained coupling is not systematic debugging.

## 7. Clean up and record

Tag temporary instrumentation with a unique marker such as `[DEBUG-a4f2]`.

Before closure:

- remove temporary logs, probes and feature flags;
- run the required full suite;
- rerun the original reproduction;
- record the root cause, rejected hypotheses and exact fix;
- state any untested environment or remaining limitation.

A focused green test with debug probes still present is **PARTIAL**, not complete.

## Stop rules

Stop and correct course when:

- no reliable feedback loop exists;
- the error has not been read fully;
- a fix is proposed before the failing boundary is known;
- a hypothesis was disproved but its fix is still proposed;
- several variables change at once;
- the regression test does not exercise the real defect seam;
- three fixes have already failed;
- temporary debugging changes remain.

## Report

```text
State: INVESTIGATING | ROOT_CAUSE_CONFIRMED | REPAIRING | VERIFIED | BLOCKED
Symptom: <exact observed failure>
Feedback loop: <command or replay and result>
Root cause: <supported explanation or not yet known>
Disproved: <rejected hypotheses>
Proof: <failing-before and passing-after evidence>
Next action: <one smallest safe step>
```

## Done

Close an incident only when either:

- a proven operational cause was resolved and the exact reproduction repeatedly passes; or
- the root cause was confirmed, a correct-seam regression proof failed first and passed after one fix, the required wider suite passed, the original reproduction passed, and temporary instrumentation was removed.

Missing evidence stays missing. Do not turn confidence into proof.
