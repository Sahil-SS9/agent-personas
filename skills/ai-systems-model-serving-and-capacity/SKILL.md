---
name: "ai-systems-model-serving-and-capacity"
description: "AI and LLM systems: plan model access and serving: hosted API versus self-hosted, token-based capacity and latency (time to first token, per-token time), GPU memory and batching, rate limits, provider failover, caching and cost per request."
license: "MIT"
---

# AI systems: model serving and capacity

Sub-category: AI and LLM systems. Operating a self-hosted stack in detail belongs to infrastructure roles; this skill makes the design decisions.

## 1. Hosted API or self-hosted
| Factor | Hosted API | Self-hosted |
|---|---|---|
| Time to start | Minutes | Weeks |
| Capacity | Provider rate limits and quotas | Your GPUs |
| Cost shape | Per token; no idle cost | Per GPU hour; cheap only at high, steady utilisation |
| Data control | Provider terms, residency options | Full |
| Model choice | Provider catalogue | Open-weight models |
| Ops burden | Low | High (drivers, serving engine, scaling, upgrades) |
Decide from the estimate (tokens per day, peak tokens per second), data constraints and team capacity. Many systems mix: hosted frontier models for hard requests, small or self-hosted models for bulk.

## 2. Capacity in tokens
- Inputs: requests per second (average, peak), input and output tokens per request, latency targets as time to first token (TTFT) and time per output token (TPOT), or end-to-end for non-streaming.
- Self-hosted throughput is bound by accelerator memory for the KV cache, which grows with context length and concurrency; long contexts cut the batch size. Paged KV-cache memory and continuous batching raise throughput several-fold at the same latency; prefill (input) and decode (output) load the hardware differently.
- Replicas = peak output tokens per second / (per-replica output tokens per second x target utilisation); plus failure-domain headroom. Use `capacity_estimate.py` (llm block).
- Hosted: check rate limits (requests and tokens per minute) and quotas against peak; request increases early.

## 3. Latency budget
Split the end-to-end budget: retrieval, guardrails, model TTFT, generation, post-processing. Stream output to users where possible; set deadlines on model calls; cap output tokens.

## 4. Failure and failover
Model APIs fail and throttle often enough to design for it. Options: retry with backoff inside a budget; route to a second provider or model through the gateway, but only if that path is exercised regularly (send a share of traffic or shadow traffic) and its output quality is evaluated; otherwise degrade (cached or templated answer, queue for later, tell the user). An untested fallback model is a latent outage.

## 5. Caching and cost
Prompt-prefix caching (stable system prompt and documents first), exact caches, batch APIs for offline work, routing simple requests to smaller models, output caps. Cost per request and per day from the estimate; spend caps at the gateway.

## Output
Model access decision, token estimate, latency budget, replica or quota plan, failover behaviour and its test, caching and cost plan.

## Pitfalls
- Sizing by requests per second instead of tokens.
- Self-hosting for cost at low utilisation.
- Fallback to a weaker model that nobody evaluated.
