---
name: "reviewer-delegation-and-codeowners"
description: "Delegate review authority with CODEOWNERS and reviewer expectations, so the maintainer stops being the bottleneck on every path."
license: "MIT"
---

# Reviewer delegation and codeowners

## When to use
Review latency is dominated by one person, or review ownership is unclear.

## Procedure
1. Write CODEOWNERS using the narrowest glob that covers the area, in one of the valid locations.
2. Verify every pattern actually matches files; a rule that matches nothing is a silent hole.
3. Remember the last matching pattern wins, and use one line per pattern.
4. Record reviewer expectations: what a reviewer is trusted to decide alone and what must escalate.
5. Rotate and retire reviewers who stop reviewing.

## Decision rules
- Widening a path is a governance change, not a convenience.
- Every critical path needs exactly one accountable owner, not a crowd.
- A CODEOWNER who never reviews is removed, not ignored.
- Tooling files that must live in .github (for example funding configuration) are not general-purpose ownership targets.

## Pitfalls
- A CODEOWNERS path that silently matches nothing, giving false confidence.
- Adding five reviewers so nobody feels individually responsible.
- Delegating review authority without delegating the corresponding trust or context.

## Done
Every critical path has an owner who knows it, and measured review latency is lower than before the change.
