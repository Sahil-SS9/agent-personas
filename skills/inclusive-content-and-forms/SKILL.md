---
name: "inclusive-content-and-forms"
description: "Make content and forms work for cognitive, motor and situational limits."
license: "MIT"
---

# Inclusive content and forms

## When to use
Writing or reviewing any UI content and forms.

## Procedure
1. Plain language: short sentences, common words, expand acronyms on first use; reading level matched to audience.
2. Forms: visible labels (placeholders are not labels), one topic per step for long forms, autocomplete attributes, errors in text at the field with fix guidance, no timeout traps without extension.
3. Non-colour semantics: errors/states carry icons AND text; links look like links (underline in body text).
4. Instructions in text, not inside placeholder or tooltips that vanish.
5. Motion/time: prefers-reduced-motion honoured; time limits extendable; nothing flashes >3/s.

## Decision rules
- Content is accessible when the most-constrained user can complete the task, not when tools pass.
- Icons need text names; abbreviation-dependent content fails Understandable.

## Pitfalls
- Placeholder-as-label disappearing on input.
- "Click here" links with no destination context.

## Done
Plain-language, form-correct, motion-safe content verified against constrained-user paths.