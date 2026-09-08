Source ledger: ../../../sources.json
Retrieved: 2026-09-07T18:04:01.820110+00:00
Sharpens: component-compatibility-review, ui-integration-acceptance
Rights: original distillation; source-specific restrictions retained in ledger; no full-book or source-code reproduction.

# Component selection and provenance

Sources: S03, F01, F04–F08 in ../../../sources.json. Original synthesis, not copied code.

## Catalogue roles
- Beautiful UI: agent-native patterns, including approval cards, tool/task displays, contexts and diff tables. Explicit MIT licence verified on its own licence page. A code import still requires notice preservation and revision capture.
- beUI: animated React/Next.js components using Motion and Tailwind; inspected catalogue advertised React 19/Tailwind 4. Verify the chosen component against the target rather than copying catalogue-level version claims blindly.
- Rare UI: animated React components delivered through shadcn. Exact licence not checked in this pass; do not import until verified.
- Transitions.dev: product-state transitions and a free/Pro split. Paid demos or availability do not establish redistribution rights.
- shadcn: a distribution mechanism for editable code. Its registry can distribute multiple kinds of files across frameworks; that says nothing about compatibility of an individual React component.

## Selection record
Capture user need, current solution, candidate URL/revision, source files, licence/notice, dependency delta, rendering boundary, keyboard model, token changes and rejection reason.

Use a small shortlist rather than downloading entire catalogues. Compare against doing nothing or extending an existing component. A candidate that requires a styling-system migration to improve one button normally loses to local adaptation; this is a design judgement, not an empirical law.

## Integration sequence
1. Read the component and all registry-declared file/dependency changes.
2. Resolve licence scope, including fonts, icons and third-party dependencies.
3. Stage only reviewed files; record upstream provenance and local changes.
4. Map tokens without introducing a second unrelated palette or spacing system.
5. Preserve semantic behaviours during visual edits.
6. Verify build and interactions; preserve a reversible change set.

## Rejected shortcuts
No arbitrary global CSS resets, framework upgrades, unknown install scripts, copied paid source, screenshot-only sign-off or unverified 'accessible by default' claims.

## Remaining evidence
These catalogues were researched, not installed or benchmarked. Individual maintenance, licence and performance assessments are per-component work for a future implementation task.
