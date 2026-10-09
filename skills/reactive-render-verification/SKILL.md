---
name: "reactive-render-verification"
description: "Verify the built interface against the approved design direction: rendered fidelity, content honesty and live interaction evidence."
license: "MIT"
---

# Reactive render verification

The approved direction is the contract; the render is what gets audited. Fidelity of the real page, not similarity of code.

## When to use
After implementing an approved thesis/mockup (or any redesign), before delivery; also on every fix round that could shift the render.

## Procedure
1. Render at the same viewports the direction was approved at; compare structurally, not pixel-slavishly: element presence (nothing missing, nothing invented), hierarchy reading the same way, signature devices intact (the thesis's type voice, motif, grid breaks).
2. Check content honesty: real copy in real slots; no placeholder claims; every brief requirement present and findable within seconds.
3. Verify composition separately from polish: fidelity failures are classified — missing element, invented element, hierarchy drift, signature drift, breakpoint breakage — before any restyling begins.
4. Test interaction as evidence, not as a screenshot: keyboard walk, focus visibility, hover/press states, loading/error/empty states, reduced-motion fallback. A visually perfect page with a dead call-to-action fails delivery outright.
5. Similarity tooling (screenshot metrics) is diagnostic support only; the verdict is named checks against the direction, not a score.
6. Log the comparison: direction reference, render captures per breakpoint, discrepancy list with severity and disposition.

## Decision rules
- Copying the approved mockup accurately is fidelity; redesigning mid-build without re-approval is drift — a defect even when the result looks better.
- Overall visual similarity never excuses missing or invented content.
- Interaction evidence is gathered from the running interface, never from static screenshots.

## Pitfalls
- Judging fidelity from one desktop screenshot.
- "Improving" the direction silently during build and presenting the result for the first time at review.

## Done
A fidelity verdict per breakpoint with classified discrepancies (all resolved or owner-approved), plus live interaction evidence across the states that matter.