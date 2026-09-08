---
name: "architecture-layering-review"
description: "Verify layered-architecture boundaries before commit."
license: "MIT"
---
# Architecture Layering Review

## When to use
Verify layered-architecture boundaries before commit.

## Method
1. Map the intended layers and dependency direction from code rather than folder names alone. Record entry points, domain logic, storage contracts and external adapters.
2. Trace representative execution paths for imports crossing layers, business policy in infrastructure, concrete storage leaking through interfaces and hidden cycles.
3. Check contract shape, transaction ownership, lifecycle and failure semantics across boundaries. A wrapper does not create an abstraction if callers still depend on backend details.
4. Prove each suspected violation with call-site evidence and a minimal counterexample. Distinguish structural defects from a documented justified exception.
5. Recommend the smallest change that restores the boundary and test the affected caller paths. Do not require a rewrite solely for aesthetic purity.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
