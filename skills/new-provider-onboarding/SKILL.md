---
name: "new-provider-onboarding"
description: "Bring a new route into use safely: limit exposure, verify behaviour in place, and confirm the terms you graded still hold once you are a customer."
license: "MIT"
---

# New provider onboarding

## When to use
A provisional provider has been admitted and you are about to route real work to it.

## Procedure
1. Start with non-sensitive traffic and a capped spend.
2. Verify in production what you graded in the dossier: model attestation, latency, quota honesty, error behaviour.
3. Confirm that the terms you read are the terms you accepted, and keep the copy you agreed to.
4. Set up key hygiene: scoped keys, rotation, and a revocation path.
5. Record the promotion criteria that would move this route from provisional to trusted.

## Decision rules
- The dossier is a hypothesis until production confirms it.
- Any mismatch between graded terms and accepted terms is a stop condition, not a note.
- Cap the exposure until the route has earned confidence; the cap is a number, not an intention.
- Keep an exit path ready before onboarding completes.

## Pitfalls
- Sending sensitive workloads during the provisional period.
- Accepting a click-through agreement that differs from the published terms.
- No revocation plan for keys already in use.

## Done
The route carries real traffic within its exposure cap, production behaviour matches the dossier or the mismatch is recorded, and promotion criteria are written.
