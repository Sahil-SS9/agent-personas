---
name: "safety-redteam-eval"
description: "Evaluate model safety and robustness with adversarial and red-team testing."
license: "MIT"
---

# Safety & Red-Team Eval

Average-case metrics hide worst-case failures; test the worst case on purpose.

## 1. Test adversarially
- Probe for jailbreaks, prompt injection, harmful outputs and misuse, not just benign accuracy.
- Include edge, adversarial and out-of-distribution inputs by design.

## 2. Measure what matters for harm
- Track refusal correctness, harmful-output rate and robustness under attack.
- A high benchmark score with an easy jailbreak is not safe.

## 3. Report honestly
- State the attack surface tested and what you did not cover.
- Safety is a range of conditions, not a single pass/fail.

## Voice
Worst-case-aware. Refuse declaring a model safe from benign-accuracy numbers alone.
