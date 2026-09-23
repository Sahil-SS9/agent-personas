---
name: "component-library-contracts"
description: "Specify components with states, accessibility contracts and documented APIs."
license: "MIT"
---

# Component library contracts

## When to use
Adding or changing any shared component.

## Procedure
1. Every component owns a written contract: purpose, when-to-use/when-not, props/slots API, and full state coverage (default/hover/focus/disabled/error/loading/empty).
2. Accessibility is part of the contract: name/role/value semantics, keyboard interaction pattern, focus management, minimum target size.
3. Composition over configuration: split components when props multiply; a 30-prop component is a failed decomposition.
4. Version with semver; breaking changes carry migration guides and deprecation timelines.
5. Live documented examples with copy-paste code; undocumented components don't exist.

## Decision rules
- Duplicates get consolidated: two similar components is a pending decision, not a pattern.
- Component changes need visual regression evidence (before/after across states).
- New components serve ≥2 real use cases before entering the library.

## Pitfalls
- Copy-paste fork instead of extending the library.
- State coverage discovered by consumers at integration time.

## Done
Documented, versioned, state-complete components with a11y contracts and live examples.