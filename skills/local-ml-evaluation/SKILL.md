---
name: "local-ml-evaluation"
description: "Evaluate local ML models on the 3090 rig before adoption."
license: "MIT"
---
# Local Ml Evaluation

## When to use
Evaluate local ML models on the 3090 rig before adoption.

## Method
1. Identify the candidate model, intended task, licence, format and required runtime. Measure the actual hardware and available memory rather than relying on a remembered machine profile.
2. Freeze representative inputs, quality criteria, resource budget and a useful baseline before benchmarking.
3. Run bounded warm-up and measured trials with explicit model/runtime versions, settings and concurrency. Separate cold start, inference latency, throughput and peak memory.
4. Inspect real outputs for the target task, including failure cases. A model that fits in memory is not necessarily useful or stable.
5. Report measured quality and resource trade-offs with uncertainty. Do not change live serving routes, download large assets or expose endpoints without approval.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
