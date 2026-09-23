---
name: "keyboard-and-sr-testing"
description: "Test every flow by keyboard and screen reader before sign-off."
license: "MIT"
---

# Keyboard and SR testing

## When to use
Every interactive change, before release.

## Procedure
1. Keyboard walk the full flow: Tab order logical, all controls reachable/operable, focus always visible (never outline:none without replacement), no traps (modals release focus, escape closes).
2. Screen-reader spot check (NVDA on Windows, VoiceOver on macOS/iOS): names, roles, states announced correctly; headings/landmarks navigate the page sensibly.
3. Forms: label association, required indication, error text tied to fields and announced, status messages via role=status/alert.
4. Dynamic content: page changes announced where context shifts; loading states announced.
5. Record findings with exact steps + what AT announced vs expected.

## Decision rules
- Focus loss after actions (modals, route changes) is a blocker-level defect.
- aria-hidden on visible focusable content is a blocker.
- Test with real screen readers, not simulations.

## Pitfalls
- Testing only the happy path with sighted eyes.
- Assuming aria-label fixes everything (labels must be sensible).

## Done
Documented keyboard + SR pass with findings, or signed-off conformance.