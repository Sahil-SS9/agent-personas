---
name: "core-web-vitals-optimisation"
description: "Diagnose and fix LCP, INP and CLS against field p75 targets."
license: "MIT"
---

# Core Web Vitals optimisation

## When to use
Any performance work on web properties.

## Procedure
1. Baseline in FIELD data at p75, segmented by mobile/desktop (CrUX/RUM). Lab numbers are diagnostics only.
2. LCP (≤2.5s): trace the critical chain — TTFB (server/edge), render-blocking resources, LCP asset. Cut blockage, preload the LCP resource, edge-cache, optimise images.
3. INP (≤200ms): find long tasks after interactions; break into <50ms slices; defer/debounce expensive handlers; reduce main-thread contention.
4. CLS (≤0.1): reserve space for images/ads/embeds (aspect-ratio, width/height), font-display with size-adjusted fallbacks, no content injected above existing content.
5. Re-measure field p75 after each fix; ship the next biggest lever until all three pass.

## Decision rules
- No optimisation without a field baseline and a re-measurement.
- Fix the median device (mid-range mobile), not the office desktop.

## Pitfalls
- Chasing Lighthouse 100 while field INP fails.
- Optimising the wrong metric (TBT when the field problem is LCP).

## Done
Field p75 within all three thresholds with documented before/after evidence.