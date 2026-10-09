---
name: "design-mixer-prototyping"
description: "Give people live design-token controls on a delivered prototype: faders/knobs that retheme instantly, export cleanly, and remove without residue."
license: "MIT"
---

# Design mixer prototyping

A portable controls layer for delivered prototypes: the recipient adjusts tokens and sees the design retheme instantly — no model call, no tooling, no dependency left behind.

## When to use
A design/prototype is delivered and the recipient should be able to explore variants (density, accent, type, motion). Attachable to any token-driven page; never required for viewing the design.

## Controls (each maps to real properties)
- Typography: scale step, display weight, letter-spacing, line-height.
- Spacing/density: base space value and its scale multiplier; density presets (compact/comfy/editorial).
- Colour: accent hue/chroma (perceptual colour space; derived hover/tint variants recompute automatically), light/dark scheme, surface tint strength.
- Shape/depth: corner-radius scale, shadow strength.
- Motion: intensity (0 = none), one-authored-moment toggle.

Rules: expose only controls the current composition uses, advanced controls tucked away; every control is direct-manipulation plus a keyboard/numeric-entry alternative; a11y (roles, labels, contrast) is re-checked automatically at every change and violations are surfaced, not silently accepted.

## Scope and behaviour
- Select target: whole page (default) or a named component subtree.
- Every fader move applies locally and instantly (CSS custom properties — no inference call); changes are staged until applied.
- Presets: named snapshots; undo/redo stack; reset returns to shipped tokens.
- Export: token values as JSON + stylesheet, schema-validated; import round-trips exactly.
- Bake-in: accepted settings are written into the design's stylesheet as its own tokens; after removal the design is byte-matched to the mixed state. Removal is a deletion, not a toggle: no scripts, no classes, no placeholder markup remain.

## Integrity rules
- The mixer is always removable: it edits tokens; it never edits component structure.
- It never bypasses the accessibility floor: mixing may change tokens, never below contrast minimums (the mixer corrects derived text colours and reports the correction).
- Performance budget: control feedback <50ms, no layout thrash, no scroll jank while open.
- The delivered design loads and looks right with the mixer blocked or absent.

## Done
Mixer attached with stated controls; a11y re-checks pass across the sampled token range; export round-trip verified; removal produces a working design identical to the applied mixed state.