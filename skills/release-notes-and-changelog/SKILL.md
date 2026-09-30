---
name: "release-notes-and-changelog"
description: "Produce release notes a user can act on: what changed for them, breaking changes first, contributors credited beyond code."
license: "MIT"
---

# Release notes and changelog

## When to use
Preparing a release, or catching up a changelog that has fallen behind.

## Procedure
1. Collect every merged change since the last tag.
2. Group by type and lead with breaking changes and migrations.
3. Write user-facing notes that answer "does this affect me", plus a maintainer changelog.
4. Credit contributors, including non-code contributions, using a contribution taxonomy rather than only commits.
5. Verify the tagged tree is the tree that was tested.

## Decision rules
- User notes are not a commit list. A commit subject is rarely a user-facing statement.
- Breaking changes go first, always, even if there is only one.
- Every entry must be actionable by the reader; drop the ones that are not.
- Do not release from a tree that was not the one tested.

## Pitfalls
- Dumping commit subjects and calling it a changelog.
- Burying a breaking change in the middle of a category list.
- Crediting only code, which quietly erases reviewers, documenters and triagers.

## Done
A user can decide whether to upgrade from the notes alone, without reading the diff.
