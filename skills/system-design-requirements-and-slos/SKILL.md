---
name: "system-design-requirements-and-slos"
description: "Turn a vague system brief into scoped functional requirements, measurable SLOs, constraints and a written assumptions list before any architecture is drawn."
license: "MIT"
---

# System design requirements and SLOs

The most common design failure is solving the wrong problem well. Fix scope and targets first, in writing.

## 1. Questions before boxes
Ask, or state as labelled assumptions when nobody can answer:
- **Who and what**: users and clients (web, mobile, other services), the 3 to 5 core use cases, explicit non-goals.
- **How much**: users now and in 3, 6 and 12 months, actions per user per day, read/write mix, object sizes, retention, peak shape (daily, seasonal, launch spikes).
- **How good**: latency people notice, freshness, durability, availability, consistency needs per operation.
- **Within what**: existing stack and platforms, team skills, budget, regulation and data residency, deadlines.
Never jump to a solution before this list exists; record each answer with its source ("PM, 04/11", "assumed - to confirm").

## 2. Functional requirements
Write them as verbs on things ("post a message", "fetch a timeline", "cancel an order"), with the actor. Mark which are on the critical path for the SLOs and which can be asynchronous.

## 3. SLOs that can be measured
- One SLI per thing users feel: availability (good events / valid events), latency as a percentile with a unit ("p99 < 300 ms"), freshness ("99% of updates visible within 60 s"), durability, correctness.
- State the window (e.g. 28 days) and where it is measured (load balancer, client, pipeline output).
- Never average-only latency and never 100%: every extra nine costs more and slows change. Pick targets from what users need, not from what the current system happens to do. Keep as few SLOs as possible; keep a margin between internal SLOs and any external SLA.
- Translate the target into downtime so stakeholders understand it: 99.9% is about 43 minutes a month, 99.99% about 4.4 minutes.
- Different operations deserve different targets (checkout vs reporting).

## 4. Constraints and assumptions register
| ID | Assumption or constraint | Value | Source | Status |
|---|---|---|---|---|
| A1 | Peak factor | 3x average | assumed | to confirm |
Every number used later in estimates must trace to a row here.

## 5. Output
A requirements section with functional list, SLO table (SLI, target, window, measured at), constraints, assumptions register and open questions addressed to named roles.

## Pitfalls
- Designing for a scale nobody asked for (over-engineering) or ignoring the scale in 12 months.
- "Real-time", "highly available", "scalable" with no number.
- One consistency level assumed for the whole system.
