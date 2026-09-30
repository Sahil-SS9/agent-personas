---
name: "provider-identity-and-payment-integrity"
description: "Establish who you are actually transacting with and how the money moves — because an unknown operator and an undefined payment path are the real risk surface."
license: "MIT"
---

# Provider identity and payment integrity

## When to use
Before any spend, and whenever a provider's ownership or payment route is unclear.

## Procedure
1. Resolve the legal entity: registered name, jurisdiction, corporate filing, and whether the trading name matches.
2. Check domain age and registration history, and where the service is actually hosted.
3. Identify the payment path: which processor, whether the operator ever sees card data, and whether the checkout is hosted or embedded.
4. Verify a reachable support and abuse channel, and whether the operator answers.
5. Check status and incident history, and whether published incidents predate the service's registration.

## Decision rules
- An operator with no resolvable legal entity cannot be a dependency for anything that matters.
- Telegram-only contact is not a support channel for a paid service.
- A status page whose own entries predate the service is evidence of fabrication, not maturity.
- If the payment route is undefined, the transaction is undefined.

## Pitfalls
- Accepting a polished site as identity evidence.
- Missing that the payment processor is a personal account.
- Overlooking that the entity behind the brand is a separate, unfiled trading name.

## Done
Identity, jurisdiction, payment path and contactability are each recorded as verified, partially verified, or unverified.
