---
name: inference-workload-and-bottleneck-diagnosis
description: "Diagnose prefill, decode and queueing bottlenecks."
license: "MIT"
---
# Inference Workload and Bottleneck Diagnosis

## When to Use
A local or hosted open-weight model is too slow, expensive or unreliable and an optimisation is proposed.

## Procedure
1. Write the required workload: prompt/output length distributions, concurrency, arrival pattern, reasoning mode, tool schema and minimum quality. Agree user-facing latency and acceptable loss before tuning.
2. Capture a baseline through the actual API. Separate queue delay, time to first visible token, decode/inter-token timing, total latency, failures, peak memory and task success. Include reasoning tokens when relevant; a fast final answer can hide expensive thinking.
3. Identify prefill-heavy, decode-bandwidth-heavy, capacity/fragmentation-bound or queue/interconnect-bound behaviour from traces/profiling, not GPU utilisation alone. Mixed load may change the bottleneck.
4. Form one falsifiable prediction for a change: which measured component should improve, why, and what could regress. Test one mechanism at a time, including a no-change repeat.
5. Report per-request latency and aggregate throughput separately. Saturating a queue can improve total tokens/s while making the user's experience worse. Tail latency and errors are hard constraints.
6. Deliver a baseline ledger, bottleneck evidence, proposed experiment and rollback condition. Do not start downloads, installs or sustained GPU work without authorisation.

## Pitfalls
Short warm prompts are not a long-context workload. Provider timing fields may measure different intervals; name definitions and preserve raw usage. A completion returned is not proof its tool decision is correct.

## Verification
A reviewer can trace every bottleneck claim to retained request settings, timing and output evidence. An unknown component stays unknown, not zero.
