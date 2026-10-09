---
name: "expressive-craft-floor"
description: "Verify built interfaces against the expressive quality floor: hierarchy, craft signals, browser-default theming and contextual refusal list."
license: "MIT"
---

# Expressive craft floor

The floor is verified on the built result, in batched inspection rounds — not on intentions. It raises ambition; it never picks direction. (Method adapted in original words from Apache-2.0 sources, notably Impeccable's craft floor; credit carried in the repo notices.)

## When to use
Before any delivered screen, and after each build/fix round. Batched: one inspection round gathers all checks at once; at most one follow-up round to confirm fixes; then stop polishing.

## Verify (each a real check on the render)
1. Contrast: body ≥4.5:1, large text ≥3:1; secondary text tinted from its surface hue, never generic grey.
2. Hierarchy: a five-second glance answers what the page is for and finds the primary action; the emphasised elements are exactly the ones users must find.
3. Type: real copy at every breakpoint; display scale makes the hierarchy obvious; measure in the 45–90 character band; tracking not below −0.04em; numerals in tabular data set as real numerals.
4. Space: tight groups, generous separation, more space above a heading than below; spacing from a coherent scale (fluid endpoints rather than per-breakpoint nudges).
5. Motion: one authored moment per view with exponential ease-out from an already-visible default; blur/clip-path/mask/shadow join the palette where smooth; nothing essential depends on animation; reduced-motion honoured.
6. States: hover, focus, disabled, loading, error, empty — all real, all themed.
7. Browser-default surfaces: text selection, caret, scrollbars, focus rings, underline offset, tabular numerals themed from the palette. This is the cheapest built-not-assembled signal and the check most often skipped.
8. Coverage: every brief requirement present and findable within seconds.

## Refuse (contextual defaults — the brief's own words can earn any back)
- Same-size icon+heading+text card arrays as page structure; nested cards.
- Hero-metric template (big number, small label, accent).
- Kickers/eyebrows above headings: banned outright; the heading carries its own weight.
- Section numbers unless the sequence informs; modals without cause.
- Gradient text; blur/glass as decoration; coloured border-left >1px on cards; hard offset shadows outside an actually neobrutalist world; sparkles/rings standing in for content; monospace as "technical" costume; a system display face as the display voice of an own-world page; emoji/unicode as icon systems; geometric masks over photographic edges; light/dark chosen by category; elevation declared twice (border under wide shadow); sketch-style SVG illustrations; stripe/grid backgrounds with no real canvas under them.

## Decision rules
- Reaching for a refuse-list default when the axis is free means the element was not decided; rewrite it rather than soften it.
- The floor holds mechanics; the thesis (art direction) owns direction; when torn, commit to the thesis.
- Distinctive, coherent and appropriate to this brief is the gate — avoiding patterns is the floor, not the goal.

## Done
One inspection round covering every check above with named results, fixes applied in one batch, confirmed in at most one further round.