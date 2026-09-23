---
name: "asset-and-bundle-budgets"
description: "Enforce asset, bundle and delivery budgets; ship less by default."
license: "MIT"
---

# Asset and bundle budgets

## When to use
Every change that ships bytes.

## Procedure
1. Set budgets per route: JS KB, CSS KB, image weight, request count — informed by what p75 performance requires.
2. Bundle-analyse per route: every dependency earns its bytes; prefer platform features to polyfills; tree-shake and code-split.
3. Images: AVIF/WebP with fallbacks, responsive srcset, lazy-load below fold, preload the hero image only.
4. Delivery: brotli/gzip, immutable cache headers on versioned assets, HTML not cached long, edge/CDN for static.
5. Fonts: subset, font-display swap with metric-compatible fallback, preload only critical weights.

## Decision rules
- Budget breaches fail the build, like test failures.
- Third-party scripts are quarantined: measured, deferred, or rejected.
- The platform first: native lazy-loading, native dialog, CSS features over JS.

## Pitfalls
- Global budgets that hide a bloated route.
- Preloading everything (which is preloading nothing).

## Done
Enforced budgets per route with CI failure on breach and delivery optimised.