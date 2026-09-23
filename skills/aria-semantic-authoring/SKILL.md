---
name: "aria-semantic-authoring"
description: "Build accessible UI from semantic HTML first, ARIA only where needed."
license: "MIT"
---

# ARIA & Semantic Authoring

Accessible-by-construction: reach for native elements before ARIA.

## 1. Semantic HTML first
- Use the real element (button, nav, label, heading) before any ARIA.
- The first rule of ARIA: don't use ARIA if a native element does the job.
- Headings, landmarks and lists give structure screen readers navigate by.

## 2. ARIA only to fill gaps
- Add roles/states/properties only when no native element exists for the pattern.
- Every custom widget needs name, role, value and keyboard behaviour together.
- No ARIA is better than wrong ARIA: a bad role actively misleads.

## 3. Follow the authoring practices
- Implement custom widgets to the published WAI-ARIA pattern, not invented behaviour.
- Manage focus and announce dynamic changes deliberately.

## Voice
Native-first. Refuse a div-with-role button when a real button exists.
