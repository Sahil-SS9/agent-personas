# Refactor preparation: establish evidence before restructuring

## Scope and provenance
Original synthesis for the observed gap: richer compatibility tests were added only after a structural-plus-feature edit. Fresh source read: Martin Fowler, An example of preparatory refactoring, https://martinfowler.com/articles/preparatory-refactoring-example.html . Reused previously ingested analytical notes from Michael Feathers, Working Effectively with Legacy Code, chapter 4 (publisher sample): https://www.informit.com/content/images/0131177052/samplechapter/0131177052_ch04.pdf . No new whole-book reading is claimed. Source copyrights remain with their authors; no source code reproduced.

Fowler supplies a concrete sequence: preserve observable behaviour while creating a place for a feature, keep existing tests passing through that preparation, then change behaviour. Feathers supplies the escape route when safe observation needs a seam. Our adaptation makes the preparation an evidence gate and adds a proportionality rule; these details are our synthesis, not quotations or proof of universal benefit.

## Trigger and scope
Use for a module-level or repository-wide structural change: extracting shared logic, changing representations/routing, or combining simplification with a feature. Do not reserve this for large campaigns. A cosmetic or truly local change with adequate existing tests takes the short path below; do not invent a migration programme or mandatory LOC census.

## Preparation gate — before the first structural source edit
1. Inspect the affected observable boundary and its relevant callers. Identify which existing contracts are exposed by the intended change, not every imaginable edge case.
2. Inspect and execute existing relevant tests. A green smoke suite is not evidence for untested contracts. Identify the specific gaps: e.g. errors, ordering, missing/empty distinctions, consumed iterators, serialization or side effects, only where relevant.
3. If coverage is missing, add the smallest boundary-level characterization tests and RUN THEM against untouched production source. Expect these preservation tests to pass; do not confuse this with a new-feature test that should fail. Record what ran and its result. Added tests that have never run on the original implementation have not cleared this gate.
4. If the boundary cannot be exercised safely, use a pre-existing injection/recording seam where possible. If a small seam-introducing production change is unavoidable, identify it explicitly as the prerequisite exception, preserve delegation to the real dependency, verify it, and only then resume the broader structural work. Never mock away the contract or pretend no source changed.
5. If existing tests already cover the relevant contract, run and reuse them. State the evidence briefly; do not add duplicates merely to satisfy the gate. If tests cannot run, preserve that limitation and do not report the refactor as verified.

## Separate preparation from changed behaviour
Make a small behaviour-preserving structural slice, then run the characterization and affected caller tests while the feature is still absent. Only then implement the feature and its own tests. Separately observable edits and test receipts are sufficient; multiple commits or PRs are not mandatory. Avoid skipped/xfail tests as a way to claim a green completed deliverable. Fowler's temporary skipped new-feature test is an optional development tactic, not permission to suppress existing failures; prefer separate targeted execution or add the feature test at the feature phase.

## Short path and stop rule
For a local rename/cosmetic edit or a structural edit whose affected behaviour is already meaningfully tested: inspect callers, execute that coverage, perform the minimal edit, rerun it. No duplicate tests, speculative abstractions, new dependency, mandatory micro-commits or repository-wide LOC inventory. Stop when relevant existing behaviour and requested changes are verified on final bytes. Do not discover extra work solely to prolong the process.

## Conflicting requirements
Preserve legacy behaviour unless a separate approved change calls for a fix. Characterization records what happens; it does not certify that every observed behaviour is desirable. Safety-critical discovered defects are surfaced, not silently preserved or silently repaired under a refactor label.

## What counts as evidence
Actual test runs before and after the structural slice, with discovered tests and observed results. Checklist prose is not proof. Equal final correctness may still hide the useful difference between establishing a safety net before versus after editing. One fixture cannot establish repeatability or general efficiency.
