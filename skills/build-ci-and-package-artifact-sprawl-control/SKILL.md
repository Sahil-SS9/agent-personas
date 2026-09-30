---
name: "build-ci-and-package-artifact-sprawl-control"
description: "Control generated artifacts from builds, CI runs and package managers — the largest and fastest-growing source of reclaimable space."
license: "MIT"
---

# Build ci and package artifact sprawl control

## When to use
Storage is disappearing without human activity, or CI artifacts are accumulating.

## Procedure
1. Attribute space to artifact classes: build outputs, caches, package stores, CI logs and artifacts, container layers, model weights, worktrees.
2. Identify which are regenerable and at what cost to regenerate.
3. Set retention per class rather than one global rule.
4. Trim the regenerable classes with the cheapest-to-rebuild first.
5. Add cache cleanup to the same cadence rather than as a manual rescue.

## Decision rules
- Regenerable is not free: a cache that takes an hour to rebuild has a cost, and the eviction policy must account for it.
- CI artifacts are usually the easiest large win and the least examined.
- Never clear a package store that a pinned build depends on without checking the pin.
- Run caches hold state that makes the next run fast; treat them as an asset with a retention policy.

## Decision-output clarification
Separate the observed artifact type and proposed policy from the eligible cleanup candidate and recommended policy. A pinned package store with no passed dependency check is not eligible for removal; reject a global cache-age rule in favour of per-class retention. Cheap regeneration and expiry do not grant removal authority: analysis-only work still needs a separate approved removal decision.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Deleting a shared build cache and slowing every subsequent job.
- Assuming a container layer set reclaims what the tool advertises.
- Clearing the store that serves the offline rebuild you will need.

## Done
Space is attributed by class, retention is set per class, and the largest reclaim came from the cheapest-to-regenerate class.
