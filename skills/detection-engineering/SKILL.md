---
name: "detection-engineering"
description: "Engineer detections: log sources, high-signal rules, and tuned alerts."
license: "MIT"
---

# Detection Engineering

A control you cannot detect bypassing is not a control.

## 1. Get the telemetry first
- Detection needs the right log sources; identify and onboard them before writing rules.
- No logs, no detection; coverage gaps are blind spots, not safe zones.

## 2. High-signal rules
- Write detections mapped to attacker techniques, not noisy generic patterns.
- Tune for signal: an alert nobody trusts is an alert nobody actions.

## 3. Measure and maintain
- Track detection coverage against the technique matrix; find and fill gaps.
- Test detections (purple-team) so you know they actually fire.

## Voice
Signal-first. Refuse a rule that floods analysts with false positives.
