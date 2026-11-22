---
name: "goal-decomposition-and-specialist-routing"
description: "Break a goal into a routed task graph: per-node objective, output format, tools and boundary, with a named specialist and a recorded routing reason."
license: "MIT"
---
# Goal Decomposition and Specialist Routing

## Use when
- A goal needs more than one agent or specialist to finish.
- The brief says what, but nobody has said who does which part.
- Work has been landing with whoever was free, and the wrong specialist keeps getting the wrong slice.

## Instructions

1. Decompose broad-then-narrow: split the goal into independent facets first;
   go deep only where the broad pass says depth is warranted.
2. Write four things per node before it exists as a dispatch:
   - objective: one sentence, checkable;
   - output format: what the returning artifact looks like;
   - tools and sources the node may use;
   - boundary: what the node must NOT touch or decide.
3. Route by domain fit, never by availability: each node names its specialist
   and a one-line routing reason. Availability is a schedule fact, not a
   qualification.
4. No orphan nodes: every node either feeds the goal or feeds another node;
   dangling work is cut, not carried.
5. Task descriptions are contracts: a worker receives its node brief plus
   the shared context slice it needs — never the whole conversation history
   as its working context.
6. Reuse over re-derive: if two nodes would collect the same reference
   material, make one node produce it as a shared input and mark the
   dependency.

## Stop conditions
- Never dispatch a node missing objective, output format or boundary.
- Never route without a recorded reason; "default" is not a reason.
- Never decompose a single-agent task into fan-out to look coordinated.

## Escalation
- Facets that cannot be split honestly go back as single-agent work with a
  note; forcing a split invents seams that will fail at integration.
