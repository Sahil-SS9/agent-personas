---
name: kv-cache-and-per-rank-capacity-planning
description: "Budget weights, KV and headroom for every rank."
license: "MIT"
---
# KV Cache and Per-Rank Capacity Planning

## When to Use
A model must fit a particular machine, context size and concurrency without claiming total VRAM as usable memory.

## Procedure
1. Inventory each device and topology, free/available memory, existing workloads and the engine allocator's accounting. Keep GB and GiB explicit; do not add unified memory to itself or assume all ranks share one pool.
2. Per rank budget resident weights including metadata, KV, activations/workspace, graph capture, draft model, fragmentation and reserve. Multi-GPU fit requires every rank to fit, not just aggregate bytes.
3. For ordinary MHA/GQA only, estimate KV bytes as 2 * layers * KV_heads * head_dimension * live_tokens * bytes_per_element. Live tokens sum current/reserved sequence occupancy according to the engine policy. Then add layout/page/scale overhead.
4. For MLA, sliding-window, recurrent or hybrid attention, obtain the engine's actual cache layout rather than misuse the ordinary formula. Shared prefix blocks and copy-on-write change physical occupancy.
5. Use the bundled capacity_plan.py through terminal on an explicit JSON fixture to check simple MHA/GQA estimates and per-rank arithmetic. It is an estimator, not a hardware probe or model-specific admission guarantee. Profile real peak usage before calling a lane safe.
6. Test maximum required context under intended concurrency and mixed prefill/decode. Record peak observed memory, queueing and failures. Refuse a lane below required context; never silently truncate or substitute a model.

## How to Run
From this skill's directory, invoke through `terminal`:
`python3 scripts/capacity_plan.py templates/gqa-capacity.json`
Exit 0 means the estimate fits, 1 means it does not, and 2 means invalid input.
The template is synthetic, not a measurement of your machine. Replace every
field from evidence; budgets are bytes and KV heads are resident per rank.

## Verification
Run `python3 scripts/test_capacity_plan.py` for provider-free calculator controls.
Every rank still needs measured headroom at required service load. Unknown
architecture/layout prevents a confirmed-fit claim. Calculator tests do not
establish actual GPU fit.
