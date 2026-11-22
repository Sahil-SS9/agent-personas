---
name: inference-ablation-and-reproducibility
description: "Compare serving changes with complete evidence."
license: "MIT"
---
# Inference Ablation and Reproducibility

## When to Use
Evaluating a faster engine, quant, cache policy, patch or launch setting.

## Procedure
1. Freeze baseline and candidate identity: artifact hash/revision, engine/build, GPU/topology, template/parser, workload, sampling, cache state, concurrency, budgets and quality floor. Vary one intended factor; record unavoidable differences.
2. Use cold and warm tests separately. A repeated shared-prefix prompt with cache on is not cold prefill. Record actual cached-token usage rather than trusting a label.
3. Keep full raw responses, settings, timing, token usage, finish reasons and error receipts. Model/fallback identity must be verified. A transport error is not a behavioural failure; an empty completed answer is an output failure.
4. Check code/JSON/tool-task outcomes with a calibrated verifier that accepts valid alternatives and rejects plausible wrong answers. Keyword presence and a self-written success message do not establish execution.
5. Report per-case and paired baseline/candidate counts, repetitions, latency percentiles, throughput and error rate. Explain whether controller execution or the model's own tool loop produced the artefact. Do not borrow upstream recipe scores as local proof.
6. Retain rejected changes. If a change improves speed but damages required quality, keep it off. A model, prompt, scorer or source change invalidates affected claims and requires a new frozen comparison.

## Verification
Reconcile the expected request matrix with the saved receipts before scoring. Missing, duplicate or off-model slots prevent a gate pass. Independent review remains separate from self-tests.
