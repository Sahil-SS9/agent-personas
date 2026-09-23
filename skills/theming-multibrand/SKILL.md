---
name: "theming-multibrand"
description: "Support theming, dark mode and multi-brand from one token architecture."
license: "MIT"
---

# Theming & Multi-Brand

One system, many skins — driven by tokens, not forks.

## 1. Theme is a token layer
- Themes swap semantic token values, never component code.
- Reference tokens (brand.primary) map to system tokens (color.action) map to component use.
- Dark mode is a theme, not a special case bolted on.

## 2. Multi-brand without forking
- Brands are alternate token sets over shared components; forking components is the failure.
- Contrast and accessibility must hold in every theme, checked per theme.

## 3. Runtime and build
- Decide runtime switching (CSS variables) vs build-time; document the trade-off.
- Avoid theme-specific conditionals leaking into component logic.

## Voice
Token-driven. Refuse a per-brand component fork when a token set would do it.
