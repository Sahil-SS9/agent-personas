---
name: "decomposition-tradeoff-analysis"
description: "Earn every split by naming its driver and the tax it imposes."
license: "MIT"
---

# Decomposition tradeoff analysis

Decide monolith vs modules vs distributed services on evidence, not fashion.

## When to use
Whenever choosing how coarse or fine to split a system or a service.

## Procedure
1. Start from the simplest structure that can meet the driving characteristics — often a well-modularised monolith.
2. Distribute a piece ONLY when a concrete driver demands it: independent scaling, independent deploy cadence, fault isolation, team autonomy, or genuinely divergent technology.
3. For each proposed split, name the tax accepted: network failure, weakened consistency, distributed transactions, added operational surface, latency. If you cannot name the driver, do not split.
4. Set service granularity by balancing disintegrators (change cadence, data ownership, fault isolation, scaling) against integrators (shared data, transactions, chatty workflows). Not "one service per noun", not lines of code.

## Decision rules
- No driver, no split. "Microservices by default" is rejected.
- Every boundary you introduce must pay for its tax with a stated benefit.
- Data ownership follows the service boundary; shared mutable databases re-couple what the split paid to separate.

## Pitfalls
- Distributing to look modern, then paying the distributed-systems tax with no benefit.
- Nano-services that turn one call into ten network hops.

## Done
A decomposition where each boundary lists its driver and accepted tax, with data ownership assigned.
