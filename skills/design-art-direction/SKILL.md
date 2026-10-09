---
name: "design-art-direction"
description: "Form a content-specific visual thesis and maintain committed art direction from brief through implementation."
license: "MIT"
---

# Design art direction

Adapted in original words from Apache-2.0 sources, notably Impeccable (Paul Bakaus) new-work and bolder playbooks; see THIRD-PARTY-NOTICES.md.

Every ambitious surface gets a visual thesis: one sentence about what this brief looks like and why. Direction is chosen before build; build honours the thesis.

## When to use
Any new surface, redesign, or work flagged as ambitious/expressive. Not required for a one-off component inside an established world.

## Procedure
1. Write the thesis before pixels: name the subject's unique mechanism in a sentence, the audience's real scene, and the cultural world the brief summons (its places, rituals, artefacts). The thesis predicts what a stranger should feel in the first five seconds.
2. Derive composition candidates from the content, not the template shelf: at least three materially different structures, each joining a distinct composition to the same thesis. Recolouring one layout is not a candidate. Candidates are ranked by fit to the brief, and the ranking is shown, not hidden.
3. For whole new visual worlds, go wider: list concrete visual systems the audience knows from its world (publications, notation, interfaces, physical artefacts), spanning at least three material families; convert two or three into full directions with ground colours, type voices and one signature device. Name the category's predictable default and exclude it unless the content specifically earns it.
4. Write the media plan with generative-asset-production: every image, illustration, lettering piece and video the direction needs, its role, and the tool class it routes to given the user's access. A direction whose signature depends on media it cannot get is revised now, not discovered at build.
5. Set the system before devices: a layout grid, a type scale with at most two families plus one utility face, spacing steps, and one signature interaction for the page. Further devices must reuse the signature's vocabulary; a new gimmick per section is noise, not ambition.
6. Lock direction with a preview: a mockup or wireframe the owner approves before implementation (owner gate). Never implement first and justify later.
7. Commit: the chosen thesis owns every surface decision until replaced. Within an established world, extension inherits; only a redesign replaces the world — a refinement never splits the difference between two looks.
8. Implementation compares itself to the thesis at review: render-fidelity checks against the approved direction, plus the floor checks (contrast, states, browser-default theming, real content at real breakpoints).
10. Render gate before anyone sees it. Render in a real browser at 1440, 1024 and 390 wide, after load and after scrolling each section into view, and inspect every section at full size. Fail on any of: clipped or cut-off elements, unintended overlaps, labels off their targets, broken kerning or letter-spacing in display type, awkward wraps (orphaned arrows, one-word button lines), dead empty bands, AI artefacts or fake lettering, inconsistent subjects between images, copy contradictions, and placeholders (dummy numbers, example domains, draft notes). Write the list with a pass or fix for each item. Self-ratings and model or vision-tool scores are not evidence; if no full-size inspection happened, the work is not ready to show.
9. "Bolder" requests amplify the existing system's strongest moves in the system's own vocabulary — reuse its motif and scale at full strength, increase conviction, quiet what competes. If everything got louder, nothing did.

## Decision rules
- The brief wins over personal taste; redirecting a clear brief toward one's own preferred look is failure.
- An ambitious directive ("really bold", "expressive") expands the candidate range, never the template adherence.
- If the skeleton (structure minus copy) does not communicate, the boldness is decoration, not design.
- One world per page: borrowed disciplines transfer as ambition and rigour, never as pasted costumes.

## Pitfalls
- Seven variations of one grid presented as seven directions.
- Hand-drawing in CSS what should be a photograph, painting or crafted object.
- Treating ambition as adding effects rather than committing to a premise.
- Mockup approved, implementation quietly drifted (re-theming, swapped fonts, dropped signature) — drift is a defect.
- Expression that breaks core interaction paradigms without cause.
- Judging the page from shrunken full-page screenshots or one width; defects live at full size and on mobile.
- Shipping draft copy or placeholders marked as drafts instead of holding the page back.

## Done
An approved thesis and locked direction, implemented output that passes render-fidelity comparison against it, a render-gate list with every item passed at all three widths, and the candidate list and ranking retained as part of the record.