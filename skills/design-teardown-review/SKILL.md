---
name: "design-teardown-review"
description: "Review UI against hierarchy, system, a11y and CWV before and after build."
license: "MIT"
---

# Design teardown review

## When to use
Self-review gate for every screen/PR.

## Procedure
1. Teardown pass: what is this page for? What is the primary action? What is noise? Remove noise; if the answers are unclear, the hierarchy failed.
2. System pass: every value from tokens? Components from the library? Off-system drift flagged.
3. Accessibility pass: keyboard walk, focus visible, contrast checked, labels present (deep pass by accessibility persona).
4. Performance pass: LCP asset preloaded, below-fold lazy, bundle impact known (deep pass by performance persona).
5. Motion pass: purposeful, interruptible, reduced-motion respected.
6. Diff review: does this change move the product toward or away from the system? One-off hacks need a reason and an exit.

## Decision rules
- "It looks fine" is not a review: each pass produces named checks.
- Regressions against the previous design must be justified, not absorbed.

## Pitfalls
- Reviewing in only one viewport.
- Reviewing screenshots instead of the running interface.

## Done
A reviewed screen with named checks across hierarchy, system, a11y, performance and motion.