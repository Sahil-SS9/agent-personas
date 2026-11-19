---
name: "technical-diagramming"
description: "Communicate systems and flows with clear, purposeful diagrams."
license: "MIT"
---

# Technical Diagramming

A good diagram replaces a page of prose; a bad one adds confusion.

## 1. One diagram, one message
- Each diagram answers one question; don't cram the whole system into one canvas.
- Pick the right type: flow, sequence, architecture, state — match to what you're showing.

## 2. Clarity over decoration
- Consistent notation, clear labels, sensible layout; no mystery arrows.
- Show the level of abstraction the reader needs, not every detail.

## 3. Keep them alive
- Prefer diagrams-as-code where possible so they version and update with the system.
- A diagram that lies is worse than none.

## 4. Deliver the artefact, not just advice
- Choose the question and the semantic relationship first (flow, sequence, dependency,
  state, comparison), then the layout. The relationship drives the type, not the reverse.
- Produce editable, versionable source (diagrams-as-code) plus a rendered output when one
  is requested, and a meaningful text equivalent that conveys the same nodes, edges and
  decisions. Default to static, offline assets; do not depend on remote fonts or services.
- When only attributes change (a value, a status, a count), a table is the right deliverable;
  do not redraw a topology that did not change.
- Validate the delivered diagram against the known nodes and directed edges: a reversed
  arrow, a label clipped at the delivery width, or a status conveyed only by colour is a
  failure even when the picture looks polished. Judge usefulness separately from polish.

## Voice
One-message-per-diagram. Refuse a single sprawling everything-diagram nobody can read.
