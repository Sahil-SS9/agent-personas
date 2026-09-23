---
name: "wcag-conformance-audit"
description: "Audit interfaces against WCAG 2.2 AA with POUR structure and named techniques."
license: "MIT"
---

# WCAG conformance audit

## When to use
Auditing or signing off any interface.

## Procedure
1. Audit by POUR: Perceivable (text alternatives, contrast ≥4.5:1, captions), Operable (keyboard-complete, visible focus, targets ≥24px, no traps), Understandable (labels, consistent navigation, error clarity), Robust (valid semantics, name/role/value on custom controls).
2. For each criterion: cite technique or failure (e.g. G94 for alternatives), record evidence per element, not per page-average.
3. Classify level: A (blocker), AA (default target), AAA (selective).
4. Automated scan for the floor; manual keyboard + screen-reader pass for the real ceiling; document both.
5. Report as defect list with severity mapped to user impact (screen-reader blocker > inconvenience).

## Decision rules
- Automated-only signoff is a failure: automated tools catch roughly a third of issues.
- Wrong ARIA is worse than no ARIA: prefer native semantics first.

## Pitfalls
- Auditing the desktop viewport only.
- Trusting contrast on gradients without sampling both ends.

## Done
A criterion-level audit with techniques cited, both automated and manual evidence, severity-ranked defects.