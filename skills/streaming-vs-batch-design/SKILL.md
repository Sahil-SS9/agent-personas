---
name: "streaming-vs-batch-design"
description: "Choose streaming or batch by latency need, and design each correctly."
license: "MIT"
---

# Streaming vs Batch

Match processing model to the latency the decision actually needs.

## 1. Latency need drives the choice
- Batch is simpler, cheaper and easier to reason about; use it unless latency demands otherwise.
- Streaming earns its complexity only when minutes-old data changes a decision.

## 2. Design for the model's hazards
- Streaming: handle late/out-of-order events, watermarks, and exactly-once vs at-least-once explicitly.
- Batch: idempotent reruns, clear windows, and backfill that doesn't double-count.

## 3. Don't split-brain the semantics
- If both exist, one source of truth for definitions; avoid batch and stream disagreeing.

## Voice
Batch by default. Refuse streaming complexity when nobody consumes sub-hour data.
