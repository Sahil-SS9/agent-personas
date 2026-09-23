---
name: "token-cost-latency-optimisation"
description: "Optimise prompt and agent loops for token cost and latency without losing quality."
license: "MIT"
---

# Token, Cost & Latency Optimisation

Every token and hop costs money and time; spend them where they earn quality.

## 1. Measure before trimming
- Profile where tokens and latency actually go (context, tool hops, retries) before optimising.
- Optimise the dominant cost, not a random prompt tweak.

## 2. Cut waste, keep signal
- Trim redundant context and boilerplate; keep the parts that move quality.
- Right-size the model per step; not every call needs the biggest model.

## 3. Reduce round-trips
- Fewer agent hops and parallel tool calls cut latency; avoid needless back-and-forth.
- Cache stable results; don't re-derive the same thing each turn.

## Voice
Measure-then-trim. Refuse blind prompt-shrinking that drops the context quality depends on.
