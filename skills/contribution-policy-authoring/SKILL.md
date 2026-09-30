---
name: "contribution-policy-authoring"
description: "Write or repair CONTRIBUTING so a stranger can get from I-found-a-bug to here-is-my-PR without asking a question the file does not answer."
license: "MIT"
---

# Contribution policy authoring

## When to use
The project has no contribution policy, or practice has drifted from the written one.

## Procedure
1. Cover: how to report, how to propose, what is in scope, the review promise, the licence and DCO/CLA position, the AI-assistance disclosure, and the enforcement ladder.
2. Place it at .github/CONTRIBUTING.md or the repository root, respecting path precedence.
3. State the review latency you actually achieve, not the one you aspire to.
4. State the enforcement ladder so a code of conduct has teeth.

## Decision rules
- Policy must describe what you actually do. A policy the maintainer violates is worse than none.
- Do not require a CLA you cannot administer; prefer DCO when in doubt.
- The AI-assistance disclosure must be explicit and non-punitive: disclose, do not detect.
- Keep it short enough that a contributor reads it.

## Pitfalls
- Aspirational policy that the first hard case contradicts.
- A policy nobody can find because it is in the wrong location for precedence.
- Copying a template whose governance model this project is not operating.

## Done
A contributor can follow the file end to end and arrive at a reviewable pull request without asking a question the file does not answer.
