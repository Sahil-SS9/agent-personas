---
name: "ringed-technology-recommendation"
description: "Output Adopt/Trial/Assess/Caution rings with rationale, expiry and re-assessment triggers."
license: "MIT"
---

# Ringed technology recommendation

## When to use
Any tool/technology recommendation, before adoption.

## Procedure
1. Frame the decision: name the capability gap, constraints (licensing, budget, platform, security), success measure, and decision type (one-off vs sustained adoption). A decision made before the gap is named is a fashion decision.
2. Evaluate the producer, not just the product: age vs maintenance, release cadence, bus factor, issue responsiveness, license health, who funds continued investment. A weeks-old single-maintainer tool is a different risk class than governed multi-year projects.
3. Trial in OUR context, not the vendor demo: check 12-factor fit (config in environment, backing services attachable, dev/prod parity), security posture (data boundaries, permission footprint, exit costs), operating fit (who runs/who is paged).
4. Output a ring: Adopt (seriously consider), Trial (prove on low-risk work), Assess (look closely, not yet), Caution (negative experience / high risk — prefer alternatives).
5. State rationale, expiry (when to re-assess), and what evidence would move the ring.

## Decision rules
- No ring, no recommendation. A bare "yes it's good" is not a verdict.
- Ring must match decision type: never a full adoption trial for a one-off script; never Adopt without a trial in our context.
- Cognitive debt counts: adopting what you cannot understand makes the system harder to debug/evolve — factor comprehension cost in.
- Exit cost before entry cost: export paths, portability, replacement cost. A tool you cannot leave is a dependency.

## Pitfalls
- Recommending from vendor demo settings rather than an honest-context trial.
- Treating legacy-vendor momentum as a quality signal.
- Adopting what is fashionable without naming what problem it solves.

## Done
Ringed recommendation with rationale, expiry, re-assessment triggers, producer health, security posture and exit cost stated and recorded.