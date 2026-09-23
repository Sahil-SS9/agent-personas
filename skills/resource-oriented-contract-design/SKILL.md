---
name: "resource-oriented-contract-design"
description: "Design API contracts around resources and standard methods, not internal schemas."
license: "MIT"
---

# Resource-oriented contract design

## When to use
When designing or reviewing any API surface.

## Procedure
1. Model resources (nouns) and their hierarchy first: collections contain same-type resources; every resource is directly addressable without a request sequence (stateless protocol).
2. Map operations to the small standard set (Get/List/Create/Update/Delete) as far as possible; custom methods only where nothing maps, using standard HTTP verbs with the custom verb in the URI.
3. Every resource must support Get (clients verify state after mutations); nearly all support List.
4. Keep resource schemas consistent: if a request/response is or contains a resource, the schema is identical across all methods touching it.
5. Never mirror the database schema in the API — that tightly couples clients to internals. The API is its own design.
6. Keep references acyclic: one canonical parent per resource; no cyclic create/delete ordering traps.

## Decision rules
- Steady-state on completion: after a successful Create/Update/Delete, a Get must reflect final state (or NOT_FOUND / DELETED for soft delete) so clients can chain safely.
- Prefer many resources with few methods over few resources with many verbs.
- Custom methods are design freedom, not a licence to skip modelling.

## Pitfalls
- Verb-first RPC-style surfaces with nouns scattered inside method names.
- Leaking internal storage names/ids as the public contract.

## Done
A resource hierarchy + method map with consistent schemas, Get/List coverage, and acyclic references.