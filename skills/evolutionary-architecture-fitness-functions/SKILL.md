---
name: "evolutionary-architecture-fitness-functions"
description: "Keep architecture honest over time with fitness functions and guided change."
license: "MIT"
---

# Evolutionary Architecture & Fitness Functions

Architecture is not a one-time drawing; it must be defended as the system changes.

## 1. Make the quality attributes testable
- Turn each key characteristic into a fitness function: an automated check that guards it.
- Examples: latency budgets, dependency-direction rules, coupling limits, security scans.

## 2. Guard in the pipeline
- Run fitness functions in CI so architectural erosion fails the build, not a later review.
- A characteristic with no fitness function will silently rot.

## 3. Enable guided change
- Design for incremental, reversible change; big-bang re-architecture is the smell.
- Let the architecture evolve within guardrails, not freeze or drift.

## Voice
Guard-what-you-value. Refuse an architecture "principle" that nothing automatically enforces.
