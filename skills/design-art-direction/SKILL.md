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
5. Lock direction with a preview: a mockup or wireframe the owner approves before implementation (owner gate). Never implement first and justify later.
6. Commit: the chosen thesis owns every surface decision until replaced. Within an established world, extension inherits; only a redesign replaces the world — a refinement never splits the difference between two looks.
7. Implementation compares itself to the thesis at review: render-fidelity checks against the approved direction, plus the floor checks (contrast, states, browser-default theming, real content at real breakpoints).
8. "Bolder" requests amplify the existing system's strongest moves in the system's own vocabulary — reuse its motif and scale at full strength, increase conviction, quiet what competes. If everything got louder, nothing did.

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

## Done
An approved thesis and locked direction, implemented output that passes render-fidelity comparison against it, with the candidate list and ranking retained as part of the record.