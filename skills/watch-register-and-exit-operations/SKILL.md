---
name: "watch-register-and-exit-operations"
description: "Run the watch register and execute clean exits: track every route, spot decay early, and leave without losing data or breaking a dependency."
license: "MIT"
---

# Watch register and exit operations

## When to use
Continuously for live routes; immediately when a route degrades, changes terms, or must be abandoned.

## Procedure
1. Keep one register row per route: verdict, expiry, owner, exposure, dependencies, last re-test.
2. Watch decay signals: price changes, rate-limit tightening, quality drift, latency, support responsiveness, ownership changes.
3. On a downgrade, decide re-verify, restrict, or exit.
4. For an exit: identify data that lives only there, export it, verify the export, then revoke keys and cancel.
5. Record the exit so the same route is not silently re-adopted later.

## Decision rules
- Every live route needs an owner and an expiry; an unowned route decays unnoticed.
- Verify the export before revoking access. Closing the account first is the classic way to lose data.
- Remove the route from configuration and credentials, not just from the document.
- An exit that leaves a dependency behind is not an exit.

## Pitfalls
- Discovering a downgrade from a production incident.
- Cancelling before confirming the export.
- Leaving an old key active after abandoning a provider.

## Done
The register shows every live route with verdict, expiry and owner, and any exit is evidenced by a verified export and revoked credentials.
