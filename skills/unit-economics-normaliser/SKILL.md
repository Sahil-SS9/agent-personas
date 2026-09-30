---
name: "unit-economics-normaliser"
description: "Normalise every price onto one comparable basis, so token, seat, credit and subscription pricing can be compared honestly."
license: "MIT"
---

# Unit economics normaliser

## When to use
Comparing options, or checking a price claim before recommending it.

## Procedure
1. Convert each offer to a cost per unit of work you can measure: per million input and output tokens, per seat per month, per credit.
2. Include the costs that hide: minimum spend, overage rates, cache pricing, batch discounts, egress, and subscription seats you must buy to unlock the rate.
3. Model your own workload: expected volume, input-to-output ratio, and burst behaviour.
4. Compute break-even between the options.
5. State the assumptions, because the comparison is only as good as them.

## Decision rules
- Seat and subscription pricing converts to per-token only through your utilisation; state the utilisation you assumed.
- A discount you cannot reach is not a price.
- Cache and batch pricing changes the ranking for some workloads; test whether yours is one.
- Publish the comparison basis, not just the winner.

## Pitfalls
- Comparing an input-token rate against an all-in rate.
- Ignoring that the cheap tier caps context or throughput.
- Assuming steady-state volume when your workload is bursty.

## Done
Every option is expressed on one basis with stated assumptions, and break-even points are shown.
