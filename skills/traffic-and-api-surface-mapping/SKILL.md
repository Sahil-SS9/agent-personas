---
name: traffic-and-api-surface-mapping
description: "Map authorised traffic to code and requests."
version: 0.1.0
author: Hermes
license: MIT
---

# Traffic and API surface mapping

Map application behaviour to its network and IPC surfaces using only owner-authorised sessions. This skill does not provide credential theft, interception of third-party traffic or bypass instructions.

## Procedure
1. Define scope, accounts, hosts, test data, retention and stop conditions before capture.
2. Capture a baseline session in an isolated environment. Record timestamps, binary/version hashes, request method, host, path, status, timing, direction and correlation identifiers.
3. Redact tokens, cookies, personal data and payload secrets at capture time; preserve a hash and schema summary where the raw value is unnecessary.
4. Group endpoints by feature and correlate calls with static references, UI actions or controlled runtime traces.
5. Document authentication, signing, retries, pagination, compression, framing and failure responses without turning secrets into fixtures.
6. Re-run the same action with a negative control and a changed input. Separate observed protocol facts from inferred server behaviour.
7. Produce a replay-safe contract fixture containing synthetic values and explicit limitations.

## Verification
A mapping is complete only when every claimed endpoint has capture evidence, a feature correlation, redaction status and a reproducible synthetic request/response fixture.
