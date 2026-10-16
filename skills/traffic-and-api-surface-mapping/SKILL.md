---
name: traffic-and-api-surface-mapping
description: "Map authorised traffic to code and requests."
version: 0.2.0
author: Hermes
license: MIT
---

# Traffic and API surface mapping

Map application behaviour to network and IPC surfaces using owner-authorised sessions. No credential theft, third-party interception, replay against live services or pinning bypass instructions.

## Procedure
1. Define scope: account, hosts, synthetic data, session duration, retention, redaction and authority. Use an isolated test account and local endpoint where possible.
2. Capture the smallest useful HAR/pcap/trace. Record app/build, proxy/tool version, clock and certificate setup; never retain private keys or secrets.
3. Build an endpoint inventory: method, host/path, status, headers, body schema, auth/signing presence, retry/cache semantics and redaction status.
4. Join requests to static call sites or documented SDK routes, marking confidence and unresolved indirection. Do not equate a request with server-side implementation.
5. Replay only against a local/mock or explicitly authorised staging endpoint. Test malformed/expired responses safely and bound rate/volume.
6. Publish sanitised evidence with hashes, exclusions and retention expiry; quarantine raw captures.

## Verification
The report includes scope proof, redaction scan, complete capture metadata, endpoint inventory, static joins, replay target and limitations. Certificate pinning is documented as a boundary/escalation, not silently bypassed.
