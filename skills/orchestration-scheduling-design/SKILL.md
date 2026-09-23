---
name: "orchestration-scheduling-design"
description: "Orchestrate multi-step workflows with dependencies, retries and idempotency."
license: "MIT"
---

# Orchestration & Scheduling

Chained jobs need a graph, not a pile of crons hoping to line up.

## 1. Model the dependency graph
- Express order and dependencies explicitly (a DAG), not implicit timing luck.
- A downstream step runs when its inputs are ready, not at a guessed clock time.

## 2. Idempotent, retryable steps
- Each step is idempotent so retries are safe; failures retry with backoff and a cap.
- Partial failure resumes from the failed step, not the whole run.

## 3. Observe and bound
- Every run is traceable: what ran, when, with what result.
- Bound runtime and concurrency; a stuck run must time out and alert.

## Voice
Graph-first. Refuse chaining jobs by hardcoded schedule offsets and hope.
