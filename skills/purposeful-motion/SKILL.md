---
name: "purposeful-motion"
description: "Use motion to orient, explain and confirm — within reduced-motion constraints."
license: "MIT"
---

# Purposeful motion

## When to use
Any animation or transition.

## Procedure
1. Motion must communicate: orient (where did this come from), explain (relationship/cause), confirm (action received). No decoration-only motion.
2. Timing: entrances ≤200ms, exits ≤150ms, standard transitions 200-300ms; ease-out for entrances, ease-in for exits; nothing linear.
3. Choreograph: staggered lists (20-40ms stagger), spatial continuity (elements move from where they were, not teleport).
4. Respect prefers-reduced-motion: cross-fade or instant where motion is reduced; nothing essential depends on animation.
5. Interruptibility: users can cancel/interact mid-animation; no animation locks the UI.

## Decision rules
- Fast > pretty: animation that delays the task is a defect.
- One motion language per product: consistent easing/duration tokens, not per-screen inventions.

## Pitfalls
- Spinners on fast operations (flash of spinner).
- Parallax/scroll-jacking that hijacks control.

## Done
Motion that communicates within the shared timing tokens and reduced-motion constraints.