---
name: "llm-as-judge-design"
description: "Design LLM-as-judge evaluations with calibration, bias controls and human anchoring."
license: "MIT"
---

# LLM-as-Judge Design

A model grading models is powerful and biased; design against the bias.

## 1. Anchor to humans first
- Calibrate the judge against human labels on a sample; report agreement before trusting it.
- The judge is a proxy, not ground truth; know its error rate.

## 2. Control the known biases
- Counter position, verbosity and self-preference bias: randomise order, control length, avoid a model judging itself.
- Use a clear rubric with explicit criteria, not a vague "which is better".

## 3. Strengthen the verdict
- Multi-judge deliberation (panel/jury) beats a single judge for contested calls; record dissent.
- Reserve escalation for close or high-stakes cases; log the reasoning.

## Voice
Calibrated, bias-aware. Refuse trusting a single uncalibrated judge on high-stakes evals.
