---
name: "seller-verification-protocol"
description: "Verify sellers and listings before money moves; buyer-protected rails only."
license: "MIT"
---

# Seller verification protocol

## When to use
Before any payment or commitment to an unfamiliar seller.

## Procedure
1. Seller history: transaction volume, dispute rate, account age, response quality. Thin history + high price = elevated risk.
2. Listing authenticity: stock photos vs real photos, serial/proof evidence for used goods, condition grading with test evidence, original purchase documentation.
3. Payment rails: buyer protection (escrow, card chargeback, marketplace guarantee) mandatory. Off-rail payments (wires, crypto to strangers) are refused.
4. For used hardware: define the test protocol before buying (what will be verified on arrival, return window).
5. Record the verification in the sourcing ledger.

## Decision rules
- Never pay outside buyer-protected rails.
- If verification cannot be completed in time, the deal waits; urgency is the scammer's tool.
- Prices far below the three-source cross-check median are investigated, not celebrated.

## Pitfalls
- Trusting marketplace rating alone without dispute records.
- Skipping arrival-test planning for used hardware.

## Done
Every candidate verified with recorded evidence and a protected payment route identified.