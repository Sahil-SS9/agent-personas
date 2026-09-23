---
name: "docs-lifecycle-ownership"
description: "Own docs as living artefacts: owners, review dates, doc-code co-diffs."
license: "MIT"
---

# Docs lifecycle ownership

## When to use
Managing a documentation set over time.

## Procedure
1. Every doc carries an owner and a review date; the registry of docs is itself maintained.
2. Docs change in the same diff as behaviour; a code change without its doc change is incomplete work.
3. Broken links, stale examples and wrong version notes are defects with the same severity as bugs.
4. Deprecate explicitly: mark superseded docs with a pointer to the current one; do not silently abandon.
5. Measure freshness: sample docs quarterly against reality; fix or delete.

## Decision rules
- Delete beats stale: an obsolete doc is worse than none.
- New feature work includes its doc plan at the start, not after launch.

## Pitfalls
- Documentation written at launch and never revisited.
- Docs-as-status: pages that exist to look complete.

## Done
An owned, dated, fresh doc set where docs move with the code they describe.