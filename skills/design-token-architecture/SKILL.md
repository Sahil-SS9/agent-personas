---
name: "design-token-architecture"
description: "Define and govern semantic tokens layered over primitives."
license: "MIT"
---

# Design token architecture

## When to use
Building or evolving any design system.

## Procedure
1. Layer tokens: primitives (hex/px values) → semantic tokens (intent: colour-surface-primary, space-md, radius-card) → component tokens where needed. Consumers use semantics only.
2. Name by purpose, not appearance (danger-red not #ff0000-dark): names survive rebrands and theming.
3. Document every token: name, value, usage rule, do-not-use-with. A token without governance rots into two.
4. Theme support from day one: light/dark/high-contrast mapped at the semantic layer; primitives untouched.
5. Version and publish token sets like code: changelog, semver, breaking-change policy.

## Decision rules
- One value, one token: duplicated values get consolidated before they diverge.
- Raw values in components are lint failures, not style opinions.
- Token changes go through the governance process with visual regression evidence.

## Pitfalls
- Tokens that mirror implementation instead of intent.
- Token sprawl: 300 tokens for a 40-component system is drift, not richness.

## Done
A layered, documented, versioned token system with theming support and governance.