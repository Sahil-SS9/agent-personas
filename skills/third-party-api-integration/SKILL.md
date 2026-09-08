---
name: "third-party-api-integration"
description: "Integrate external APIs handling auth lifecycles, webhook verification and environment parity."
license: "MIT"
---
# Third-Party API Integration

## Use when
- Wiring any external API (payment, CRM, messaging, data providers)
- A webhook signature check silently fails or works inconsistently
- Test and production environments behave differently for the same code

## Instructions

1. Auth first: identify the vendor's scheme precisely — OAuth token
   lifecycle vs static keys vs non-Bearer headers vs mandatory version
   headers. Token refresh races are their own failure class; refresh under
   a lock.
2. Webhooks: verification canonicalisation differs per vendor (HMAC-SHA256
   over raw body vs RSA over joined fields vs certificates fetched from
   vendor domains). Implement per vendor doc, verify domain first, and
   treat ANY deviation as silent rejection — log verification failures
   explicitly.
3. Idempotency: every write endpoint gets an idempotency key strategy;
   retries without idempotency create duplicate side effects.
4. Environment parity: maintain an explicit divergence register (base URLs,
   prefixes, feature availability). Some vendors silently route to test env
   on wrong prefixes — document or suffer mystery behaviour.
5. Rate limits & pagination: respect documented budgets with backoff;
   paginate to exhaustion, never to 'looked like the end'.

## Stop conditions
- Never deploy an integration whose webhook path has not received a real
  vendor-signed event in staging.
- Never share secrets across test/live environments.

## Escalation
- Vendor-side breakages (silent API changes) get reported upstream AND
  worked around locally with the workaround recorded in the divergence
  register.
