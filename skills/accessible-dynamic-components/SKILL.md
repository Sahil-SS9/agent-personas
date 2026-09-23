---
name: "accessible-dynamic-components"
description: "Make dynamic and JS-driven UI accessible: focus, live regions, and state."
license: "MIT"
---

# Accessible Dynamic Components

The hard part of a11y is what changes after load.

## 1. Manage focus on change
- Move focus deliberately on route change, modal open/close and content injection.
- Trap focus inside modals; return it to the trigger on close.
- Never leave focus on a removed element.

## 2. Announce what changed
- Use live regions (polite/assertive) for async updates, toasts and validation.
- Don't over-announce: only changes the user needs to know.

## 3. Reflect state in the accessibility tree
- Expanded, selected, busy, invalid must update as ARIA state, not just visually.
- Loading and error states are announced, not only spinner-shown.

## Voice
Post-load first. Refuse a modal that opens without moving or trapping focus.
