---
name: "workspace-convention-and-gitignore-hygiene"
description: "Close the source of the mess: define where things belong, make the ignore rules match reality, and stop untracked chatter reaching the index."
license: "MIT"
---

# Workspace convention and gitignore hygiene

## When to use
Debris keeps reappearing after each cleanup.

## Procedure
1. Define the intended layout: source, generated output, scratch, artefacts, secrets, vendored dependencies.
2. Update ignore rules to cover everything generated, with the widest correct pattern.
3. Verify the rules with a check that respects tracked files, since ignore rules do not apply to already-tracked paths.
4. Ensure secret-bearing paths are ignored before they are ever created.
5. Add a pre-commit check for the paths that keep slipping in.

## Decision rules
- Recursive patterns have surprising semantics; test the pattern rather than reasoning about it.
- Ignore rules are documented as having no effect on tracked files — verify, do not assume.
- Untrack rather than delete when the item should exist locally but not in history.
- A convention nobody enforces is a suggestion; add the check or accept the drift.

## Decision-output clarification
An added ignore pattern leaves an already-tracked path tracked until an approved index change occurs. A proposal to untrack is not an executed fix. A saved matcher result of not ignored means the source is not hidden; do not reverse the boolean because generated output elsewhere is ignored.

Before returning a structured result, check that each field answers the requested proposition, uses the requested types and vocabulary, and agrees with the explanation. Saved evidence is not an action performed by you; a recommended next step is not an executed action.

## Pitfalls
- Adding an ignore rule for a file that is already tracked and concluding it is fixed.
- Over-broad patterns that hide real sources.
- Ignoring a directory that contains files someone does need to track.

## Done
The layout is written down, the rules match practice, and a check prevents the specific recurrence.
