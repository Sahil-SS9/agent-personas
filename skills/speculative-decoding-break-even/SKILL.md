---
name: speculative-decoding-break-even
description: "Verify draft gains without changing target quality."
license: "MIT"
---
# Speculative Decoding Break-Even

## When to Use
Adding checkpoint-native drafting, a small draft model or another speculative path to reduce decode latency.

## Procedure
1. Name the target, drafter, tokenizer mapping, algorithm and exact engine implementation. Verify the algorithm's correctness conditions; a feature called speculative does not automatically preserve the target distribution.
2. Budget drafter weights, KV, workspace, draft/verify time and inter-device communication. Confirm draft artefact licence, particularly commercial-use restrictions, separately from the base model's licence.
3. Run speculation off/on on the same representative prompts, context, concurrency and sampling configuration. Record acceptance length/rate, draft time, verification time, end-to-end latency, tails and quality.
4. Sweep a bounded draft length; more accepted tokens alone do not prove a speedup when drafting costs dominate. Code and prose may have different acceptance; test tool-call structure and stopping too.
5. Distribution-preserving sampling does not promise byte-identical output with the same seed; numerics and random-number consumption can differ. Use task-quality and distributional checks where relevant, not only output hashes.
6. Keep the simpler non-speculative lane when net gain is absent or quality/runtime compatibility fails. Record the no-gain result rather than increasing the tuning budget silently.

## Verification
A reproducible A/B record shows net improvement on the declared workload with all required quality constraints intact. Unsupported algorithm guarantees remain unverified.
