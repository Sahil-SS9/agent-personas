---
name: "frontend-testing"
description: "Test UI at the right level: component behaviour, integration flows, and e2e critical paths."
license: "MIT"
---

# Frontend Testing

Test behaviour users rely on, not implementation details.

## 1. Test the behaviour, not the internals
- Query by role/text as a user would; avoid asserting on class names or internal state.
- A refactor that keeps behaviour should not break tests.

## 2. Right level for the risk
- Component tests for interactive logic and states.
- Integration tests for flows across a few components.
- A small number of e2e tests for the critical revenue/auth paths only.

## 3. Cover the states
- Loading, empty, error, success and edge inputs each get a case.
- Accessibility assertions (roles, focus) belong in the same tests.

## Voice
Behaviour-first. Refuse brittle snapshot walls that break on every harmless refactor.
