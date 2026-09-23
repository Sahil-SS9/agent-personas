---
name: "progressive-delivery-and-rollback"
description: "Ship with canaries, abort criteria, and rollback proven before it is needed."
license: "MIT"
---

# Progressive delivery and rollback

## When to use
Every production change.

## Procedure
1. Separate build/release/run (12factor): one artifact promoted through stages; config in environment; dev/prod parity.
2. Roll out progressively: canary → partial → full, with automatic abort criteria defined BEFORE the rollout (error rate, latency, business metric).
3. Prove rollback before you need it: previous artifact retained, rollback rehearsed, feature flags for risky paths. Reversibility by design.
4. Blast-radius control: risky changes go behind flags; database changes ship expand→migrate→contract, never big-bang.
5. Record every release: what shipped, to whom, with what observed effect.

## Decision rules
- Deploy ≠ release: decouple code deployment from feature exposure.
- An un-rollbackable change is a stopped change until it becomes rollbackable.
- Failed canary aborts automatically; humans are for judgement, not polling.

## Pitfalls
- Rollback scripts that have never run.
- Schema changes coupled to code deploys without compatibility windows.

## Done
Every release progressive, abortable, and reversible with rehearsed rollback evidence.