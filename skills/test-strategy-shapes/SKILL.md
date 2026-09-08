---
name: "test-strategy-shapes"
description: "Choose test distribution and advanced techniques by architecture."
license: "MIT"
---
# Test Strategy Shapes

## Use when
- Planning test coverage for a new service, UI or migration
- A suite feels expensive but keeps missing real bugs
- Deciding whether property/mutation/contract testing pays off

## Instructions

1. Pick the shape from the ARCHITECTURE (never from fashion):
   - Monolith with thick service layer -> pyramid (many unit, some
     integration, few E2E)
   - Component-driven frontend -> testing trophy (static analysis base,
     integration widest — implementation-detached tests at module
     boundaries; unit/integration boundary is blurry in component UIs)
   - Microservices -> honeycomb/diamond (wide collaborative integration:
     contract tests + stubbed dependencies; narrow E2E across services)
   - Mixed estate -> per-service shapes; one shape never fits all.
2. Enforce F.I.R.S.T. qualities on every member: fast, isolated,
   repeatable, self-validating, timely.
   Balance Khorikov's four pillars when judging any test: protection
   against regressions and resistance to refactoring outrank speed and
   maintainability. Mock only at application boundaries you don't own;
   internal mocks couple tests to implementation.
   Performance claims get statistical treatment: multiple runs,
   significance testing — most 'faster' implementations are not (wiki:
   arXiv 2607.07619 found 6.11% significant).
3. Coverage discipline: coverage % measures execution, not fault detection.
   Where a suite must PROVE it catches bugs, add mutation testing
   (mutmut/PIT): kill score <80% = undertested, >90% good, 95%+ for
   critical paths. Cost is O(mutants x suite) -> run weekly or on release
   for critical modules only (authz, pricing, parsers).
4. Route advanced techniques to risky boundaries chosen by defect history:
   - Property-based (Hypothesis): invariants over examples — round-trip
     parse/serialize, order-insensitivity, idempotence; auto-shrinking
     gives minimal reproducers.
   - Schema fuzzing (Schemathesis): reads OpenAPI/GraphQL, generates valid
     AND intentionally-invalid inputs against declared constraints.
   - Contract testing (Pact): consumer-defined contracts verified against
     provider CI without co-running services; pays off when services deploy
     independently.
   Adoption rule: one technique on one painful boundary; expand only when
   it catches bugs the existing suite missed.
5. Exploratory testing is charter-based and time-boxed (session-based):
   charter, timebox, debrief with session sheet — not random clicking.

## Stop conditions
- Never prescribe a shape without knowing the architecture first.
- Never adopt an advanced technique as a maturity badge; require a target
  boundary and a defect-history justification.

## References
See the persona's edge-case-inventory knowledge base for domain-specific
checklists (unicode/DST/a11y/i18n/perf/security/migration/AI systems).
