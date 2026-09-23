---
name: "automation-cost-budgeting"
description: "Keep automations within cost and rate-limit budgets so they don't run away."
license: "MIT"
---

# Automation Cost & Rate Budgeting

An unbounded automation is an unbounded bill.

## 1. Budget before scale
- Estimate per-run cost and API calls; multiply by frequency before enabling.
- Respect provider rate limits with backoff; don't hammer and get throttled or banned.

## 2. Cap and alarm
- Hard caps on spend, calls and iterations; a runaway loop must stop itself.
- Alert on budget breach before it becomes a surprise invoice.

## 3. Right-size the trigger
- Run on real change, not a tight poll; event-driven beats busy-waiting.
- Batch where possible to cut per-call overhead.

## Voice
Bounded-by-default. Refuse an automation with no spend cap and a tight polling loop.
