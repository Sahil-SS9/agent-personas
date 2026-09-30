---
name: "pr-disposition-and-salvage"
description: "Choose and record what happens to a reviewed pull request — accept, accept with changes, take over, supersede or decline — with accurate credit."
license: "MIT"
---

# Pr disposition and salvage

## When to use
The review is complete and the outcome must be decided and recorded.

## Procedure
1. Choose one disposition: accept, accept-with-changes, take-over, supersede, decline.
2. For take-over or salvage, decide whether to fix on the author's branch or cherry-pick the useful part.
3. Preserve accurate attribution: credit the author in the commit, the changelog or both.
4. If superseding, link to the replacement and explain what changed.
5. If declining, state the reason and, where possible, what would be accepted.

## Decision rules
- Prefer salvage over decline whenever the intent is right and the implementation is fixable.
- Never force-push or rewrite a contributor's branch without telling them.
- If you rewrite substantially, say so plainly; keeping the author's name on code you wrote is a credit lie.
- A merge that will be reverted later should not be merged now.

## Pitfalls
- Silent rewrites that leave the original author looking responsible for the result.
- Closing without a reason, which reads as arbitrary and suppresses future contributions.

## Done
One disposition is recorded, attribution matches who actually wrote what, and the reason survives in the thread.
