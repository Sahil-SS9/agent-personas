---
name: "ui-component-composition"
description: "Build UI from the design system's tokens and components; compose, don't invent."
license: "MIT"
---

# UI component composition

## When to use
Building any interface.

## Procedure
1. Check the design system first: existing component? Use it. Near-miss? Propose extension to the design-system persona before inventing.
2. Consume semantic tokens only (colour-surface, space-md, radius-card): no raw hex/pixel values in component code; off-system values fail the lint gate.
3. Respect component contracts: states (default/hover/focus/disabled/error/loading), slots/props per the documented API.
4. Compose atoms → molecules → organisms; keep components single-purpose; duplication beats a wrong abstraction.
5. New patterns go through the system: propose → review → versioned component → reuse.

## Decision rules
- A one-off style value is a debt: route it through tokens or drop it.
- State coverage is part of done: an unstyled error state is a defect.
- Responsive by default: components work at 320px and 200% zoom or they are not done.

## Pitfalls
- Copy-paste styling that bypasses tokens.
- Prop-explosion mega-components.

## Done
UI built from documented, token-consuming components with all states covered.