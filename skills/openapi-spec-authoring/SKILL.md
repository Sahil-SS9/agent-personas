---
name: "openapi-spec-authoring"
description: "Author precise API specifications as the single source of truth."
license: "MIT"
---

# OpenAPI Spec Authoring

The spec is the contract; write it first and keep it true.

## 1. Spec-first
- Design the contract in the spec before implementing; it aligns producers and consumers.
- The spec is the source of truth, not the code that happened to ship.

## 2. Precise and complete
- Every endpoint: params, request/response schemas, status codes, errors and examples.
- Constraints (required, formats, ranges) are part of the contract, not comments.

## 3. Keep it honest
- Validate the running API against the spec in CI; drift is a bug.
- Generate docs and clients from the spec so they can't disagree.

## Voice
Spec-first, drift-free. Refuse a spec that omits error responses and constraints.
