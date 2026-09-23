---
name: "c4-architecture-modelling"
description: "Model and communicate system structure top-down with the C4 ladder."
license: "MIT"
---

# C4 architecture modelling

Communicate structure at increasing zoom before committing to it.

## When to use
Once driving characteristics exist and you need to describe or agree the structure.

## The ladder
1. System Context — the system as one box, its users and external systems. Always produce this.
2. Container — the separately deployable/runnable units (services, apps, datastores) and how they talk. Always produce this.
3. Component — the major building blocks inside one container. Produce only where risk or disagreement warrants.
4. Code — class/detail level. Usually redundant; skip unless a single tricky mechanism needs it.

## Supporting views (only to answer a real question)
- Deployment: how containers map to infrastructure/nodes.
- Dynamic: one concrete runtime flow across containers.
- Landscape: a system-of-systems overview.

## Decision rules
- Default deliverable = Context + Container. Go deeper only where a real question is unanswered.
- Notation- and tooling-independent: ship an explicit legend rather than relying on house style.
- One abstraction level per diagram; do not mix containers and code in the same view.

## Pitfalls
- Big-ball-of-boxes diagrams with no defined element meaning.
- Producing Component/Code diagrams that no decision depends on.

## Done
Context + Container (plus any justified deeper/supporting view), each with a legend and a stated purpose.
