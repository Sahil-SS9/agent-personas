---
name: "controlled-runtime-investigation"
description: "Observe program behaviour under authorised, isolated control: sandboxing, dynamic analysis, emulation and evidence capture."
license: "MIT"
---

# Controlled runtime investigation

Behaviour is evidence. Run artefacts only where containment is proven, and record what happened, not what you assume happened.

## When to use
Static analysis left a question only execution can answer — a decryption key, a network payload, a launch mechanism, a crash cause — and the owner has authorised runtime work.

## Procedure
1. Verify isolation before any run: dedicated disposable VM/container, snapshot restore proven this session, no host mounts, egress control with a logged/inspected channel, time limits. NAT and host-only settings are not proof of isolation; prove the path.
2. Write the run plan first: the question the run answers, the instrumentation (API monitoring, network capture, memory snapshot, file/registry diffing), trigger conditions and abort criteria. A run without a question is contamination risk for nothing.
3. Instrument passively before actively: observe first-run behaviour, then escalate to targeted tracing. Expect anti-analysis: long sleeps, environment checks, breakpoint detection — record their presence as findings.
4. Capture comprehensively once: process trees with provenance, memory images (hashed), packet captures, dropped artefacts. Analysis happens on the capture, not by re-running repeatedly.
5. Emulate before executing when suspicion is high: instruction-level emulation of the specific code path rehearses behaviour without a live run; initialise state deliberately, expect unimplemented-operation stubs, and treat emulator results as strong hypotheses pending live confirmation where authorised.
6. Correlate static and dynamic: every observed behaviour maps back to the code path that caused it; unexplained behaviour goes back to the static loop, not into speculation.

## Decision rules
- Unproven containment = no execution, whatever the deadline.
- A crash is an observation, not an explanation; root-cause it (which input reached which defect) before reporting impact.
- If behaviour changed between runs, suspect environment sensitivity (or anti-analysis) and record both runs rather than averaging them.
- Runtime evidence outranks static inference; static evidence outranks plausible narrative.

## Pitfalls
- Interfering monitors that alter behaviour, then reporting the altered behaviour as native.
- Forgetting the sandbox clock, locale and user-agent fingerprint are part of the experiment.
- Re-running repeatedly instead of analysing the first full capture.

## Done
A run record with proven isolation proof, the captured evidence set, correlated static-dynamic findings and explicitly unanswered questions.