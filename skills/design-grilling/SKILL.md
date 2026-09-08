---
name: "design-grilling"
description: "Interview a design to surface trade-offs and failure modes before commitment."
license: "MIT"
---
# Design Grilling

## Use when
- A design, RFC or architecture will be committed to soon
- A proposal reads well but nobody has named its costs
- Pre-mortem time before build starts

## Instructions

1. Make the presenter restate the problem before the solution; designs that
   skip problem statements get sent back.
2. Force trade-offs explicit for every claimed benefit: "what does this make
   worse?" One-sided benefits are red flags (Ousterhout: every structure has
   costs).
3. Walk failure modes before happy paths: what breaks under load, partial
   failure, rollback, schema change, key-person loss.
4. Ask the Release It questions for every external dependency: what
   happens when it HANGS (not just fails)? timeout/bulkhead/circuit
   breaker/load-shed named or the design isn't done.
5. Probe data-model consequences: storage engine behaviour, consistency
   model under replication, migration path (Kleppmann lens).
5. Record each resolved question as an ADR candidate (context -> decision ->
   consequences); park unresolved ones visibly with owners and deadlines.
6. End with a verdict menu: proceed / proceed with changes / reshape — never
   a silent pass.

## Stop conditions
- Never accept "it depends" without naming what it depends on.
- Never let the interview end without at least one named cost per benefit.

## Escalation
- Cross-domain conflicts (data vs security vs product) go to the owning
  leads with the grilling transcript attached.
