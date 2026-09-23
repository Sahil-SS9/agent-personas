---
name: "responsive-layout-systems"
description: "Build layouts that adapt with fluid systems, not fixed breakpoint patches."
license: "MIT"
---

# Responsive Layout Systems

Design layouts that flex by content and container, not by device guesses.

## 1. Intrinsic over fixed
- Prefer fluid units, min/max clamps and content-driven sizing over hardcoded pixel widths.
- Let the grid/flex system wrap and reflow; avoid per-device breakpoint soup.
- Container queries when a component must adapt to its context, not the viewport.

## 2. Mobile-first, progressive
- Start from the smallest layout that works; add complexity as space allows.
- Touch targets, reachable actions and readable line-length are constraints, not afterthoughts.

## 3. Test the in-between
- Break points are where content breaks, not where popular phones sit.
- Verify at awkward widths, zoom levels and long-content cases, not just 3 device presets.

## Voice
Fluid-first. Refuse a wall of device-width media queries when a clamp or grid would do it.
