---
name: quantisation-engine-and-quality-contract
description: "Choose quants by kernel support and task quality."
license: "MIT"
---
# Quantisation, Engine and Quality Contract

## When to Use
Selecting or producing a quantised model for a known serving engine and GPU.

## Procedure
1. Record the exact model revision, tokenizer, chat template, quantisation method/format, group size, activation precision and engine/build. Check actual kernel support for the target GPU architecture before downloading or claiming speed.
2. Quantised weight size does not describe the whole service. Account for scales, zero points, packing, nonquantised layers, activations, KV and draft weights. Separate weight, activation and KV quantisation effects.
3. For calibration-based methods, record dataset/version, samples and sequence length; keep held-out tasks separate. Compare full/higher precision and the existing usable quant when feasible. If the reference cannot run, explicitly limit quality claims.
4. Set acceptable loss before comparing. Test code execution, exact tool name/typed arguments, abstention, stop behaviour, long-context use and required safety decisions, not just perplexity or fluent prose.
5. Examine sensitivity: protected tensors/mixed precision may preserve quality but require compatible packing and kernels. AWQ's activation-aware scaling is a studied method, not a universal best quant. Do not infer a private method from an announcement.
6. Publish the supported lane and rejected lanes with reasons. A Blackwell-only format is not an Ampere fast path. No bit width or format is universally lossless.

## Boundaries
Quantisation calibration is not task fine-tuning. Dataset creation, adapter training and preference optimisation are outside this persona; any adapter merge/re-quantisation needs separate held-out quality checks and authority.

## Verification
The artifact actually loads in the pinned engine and passes the frozen quality floor through its real parser/template. A metadata match alone is insufficient; unavailable execution is UNTESTED.
