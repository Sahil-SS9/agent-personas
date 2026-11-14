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

## 4. Worked example: native disclosure

```html
<button type="button" id="opener" aria-expanded="false" aria-controls="delivery">Delivery options</button>
<section id="delivery" hidden> ... </section>
```

Expected accessibility tree and behaviour:

| Check | Expected |
|---|---|
| Role | `button`, native, so nothing to declare |
| Name | "Delivery options", from its own text, not from `aria-label` |
| State | `expanded=false` before, `true` after |
| Tab order | One stop. The panel's contents are not tabbable while `hidden`. |
| Keyboard | `Enter` toggles. `Space` toggles on key-up. One toggle per press, no repeat on key-down. |
| Focus | Stays on the button through the toggle; never moves into the panel unasked. |
| Tree | After opening, the section is present in the tree; before, it is absent, not merely invisible. |

If `<details>`/`<summary>` can carry the same design, use it and stop: that is the native disclosure.

## 5. Worked example: custom disclosure

Build this only when no native element can do the job, and ship all four parts together.

```html
<h3><button type="button" id="faq-1-button" aria-expanded="false" aria-controls="faq-1-panel">Returns policy</button></h3>
<div id="faq-1-panel" role="region" aria-labelledby="faq-1-button" hidden> ... </div>
```

```js
const button = document.getElementById('faq-1-button');
const panel = document.getElementById('faq-1-panel');
button.addEventListener('click', () => {
  const open = button.getAttribute('aria-expanded') === 'true';
  button.setAttribute('aria-expanded', String(!open));
  panel.hidden = open;
});
```

All required: role `button`, name from its text, `aria-expanded` toggling `false`/`true`, `aria-controls` pointing at the panel id, `Enter` and `Space` each toggling exactly once, focus staying on the button, and visibility driven by the `hidden` attribute rather than a CSS class alone so the tree and the pixels agree. The heading keeps the button in the document outline, which is what makes it navigable by heading.

## 6. Rejected control: plausible but wrong

```html
<div class="disclosure" tabindex="0">Returns policy</div>
<div class="panel"> ... </div>
```

Reject it. The tree exposes a container with no role and no name to announce; nothing reports open or closed; `tabindex="0"` adds a tab stop that `Enter` and `Space` cannot operate because no keyboard handler exists; the panel is always present and always announced, so the visual toggle lies to assistive technology.

Adding `role="button"` alone makes it worse: the tree now promises an operable button that keyboard users cannot press, and still reports no expanded state. That is the wrong ARIA this skill exists to prevent.

## 7. Accept or reject

- Accept only when the accessibility tree shows the intended role, name, state and value for every control added, and the keyboard checks above pass for each of them.
- Reject when a native element could have done the job, or when role, name, state and keyboard behaviour are not all present at once.
- Reject "the DOM looks right" as evidence: inspect the tree in a browser's accessibility panel and confirm with a real screen reader. The keyboard-and-sr-testing skill owns the full sign-off pass; this section is the per-widget gate.

## Voice
Native-first. Refuse a div-with-role button when a real button exists.
