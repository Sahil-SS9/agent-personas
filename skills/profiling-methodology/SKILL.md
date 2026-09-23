---
name: "profiling-methodology"
description: "Diagnose performance from measurement, not guesswork: profile, attribute, verify."
license: "MIT"
---

# Profiling Methodology

Measure the real bottleneck before touching code.

## 1. Reproduce and measure first
- Reproduce on representative hardware/network; devs' machines lie.
- Profile before optimising; the bottleneck is rarely where you guessed.

## 2. Attribute to the real cost
- Find the dominant cost (the flame-graph wide bar), not a random slow line.
- Optimise the thing on the critical path; off-path speedups don't move the metric.

## 3. Verify the change
- Re-measure after each change; keep or revert on evidence.
- Guard the win with a budget so it doesn't regress.

## Voice
Measure-first. Refuse speculative optimisation with no profile behind it.
