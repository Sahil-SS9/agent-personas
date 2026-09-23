---
name: "automated-a11y-ci"
description: "Wire automated accessibility checks into CI to catch regressions early."
license: "MIT"
---

# Automated Accessibility in CI

Catch the mechanical failures automatically; reserve humans for judgement.

## 1. Automate the catchable
- Run an axe-style engine in CI on key pages and components.
- Fail the build on new violations; treat a11y regressions like test failures.
- Automated tools catch ~30-40%; never claim conformance from a green scan alone.

## 2. Layer the checks
- Lint for missing alt, labels and contrast at author time.
- Component-level a11y assertions in unit tests; page-level scans in integration.

## 3. Keep humans for the rest
- Keyboard, screen-reader and cognitive checks stay manual and scheduled.
- Track the gap: what automation cannot see is still owed a manual pass.

## Voice
Automate the floor, not the ceiling. Refuse "axe is green so we're accessible".
