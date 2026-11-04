---
name: "ai-systems-evaluation-and-operations"
description: "AI and LLM systems: make AI components measurable and operable: evaluation sets before launch, online quality signals, tracing of model calls, versioned prompts and models, staged rollout of model changes, drift and feedback-loop monitoring."
license: "MIT"
---

# AI systems: evaluation and operations

Sub-category: AI and LLM systems. Deep evaluation methodology (judges, contamination, statistics) belongs to the ML Eval Engineer; this skill puts evaluation into the system design.

## 1. Define quality before launch
For each AI component: what "good" means (correct, grounded, safe, right format, helpful), how it is measured (exact checks, reference answers, rubric with a judge model, human review), and the launch bar. Build an evaluation set from real or realistic inputs, including hard and adversarial cases; keep it versioned.

## 2. Evaluate the parts, not just the whole
Retrieval (did the right documents come back?), generation (faithful to context?), tools and plans (valid tool, valid arguments, goal reached, constraints respected), and efficiency (steps, latency, cost per task).

## 3. Versioning and change control
Prompts, model versions, retrieval settings and tool definitions live in a versioned catalogue. Any change runs the evaluation set and ships through staged rollout (shadow, canary, wider) with rollback, like code. Changing anything changes everything: re-evaluate end to end.

## 4. Online signals
Trace every model call (inputs, retrieved ids, outputs, tokens, latency, cost) with privacy controls; user feedback; automatic checks on output format and policy; sampled human review; dashboards for quality proxies, refusal and failure rates, TTFT, cost per request.

## 5. Drift and feedback loops
Monitor input distribution, retrieval hit rates and answer quality over time; provider model updates; corpus changes. Watch for hidden feedback loops where model outputs shape future inputs or training data, and for undeclared consumers relying on output formats.

## 6. Incidents
Runbooks for bad outputs at scale: disable the feature or tool, roll back the prompt or model, purge caches of bad answers, notify affected users where needed.

## Output
Evaluation plan with launch bar, component-level metrics, versioning and rollout process, online monitoring, drift checks, AI incident runbook.

## Pitfalls
- Shipping on vibes from a few demos.
- Silent provider model changes with no regression run.
- Logging prompts that contain personal data without controls.
