---
name: "cost-modelling-for-system-design"
description: "Model what a design costs to run and to change: unit cost per request, user or tenant, dominant drivers such as compute, storage, egress, third-party and model calls, and the first levers, without letting cost become the only goal."
license: "MIT"
---

# Cost modelling for system design

Cost is a design constraint and a guardrail, not the design goal. Model it early enough to change the design.

## 1. Unit economics
From the estimate, compute cost per meaningful unit: per request, per active user per month, per tenant, per GB stored, per order. Compare with what the unit earns or is worth.

## 2. Drivers to model
- Compute: nodes at peak with failure-domain headroom; idle cost of over-provisioning.
- Storage: raw x replication x retention, plus indexes, backups, snapshots.
- Network: cross-zone and cross-region traffic and internet egress are often the surprise line.
- Managed services and third parties: per-call or per-message pricing (email, SMS, maps, payments).
- AI: tokens in and out per request x price, embeddings, vector storage, GPU hours for self-hosting.
- People: on-call and operational load of every extra component.
State the largest two drivers; most decisions only need those.

## 3. Reliability costs money
Each extra nine roughly multiplies cost (more replicas, regions, engineering). Tie availability targets to business impact rather than maximising them.

## 4. Levers, in order of usual payoff
Remove work (cache, batch, avoid recomputation); right-size and use cheaper tiers (storage classes, smaller models for simple requests); shape traffic (async, off-peak batch); reduce data movement (co-locate, compress); commit or reserve only for proven steady load.

## 5. Guardrails
Budgets and alerts per environment and per tenant; hard spend caps for external APIs and model calls; cost per unit on the dashboard.

## Output
Cost section: unit cost, top drivers with figures, assumptions, sensitivity (what doubles the cost), first levers, guardrails.

## Pitfalls
- Ignoring egress and cross-zone traffic.
- Per-call third-party pricing multiplied by retries.
- Optimising cost before the design meets its SLOs.
