---
name: pressure-aware-inference-policy
description: "Shed inference load within explicit user limits."
license: "MIT"
---
# Pressure-Aware Inference Policy

## When to Use
A shared GPU machine needs bounded inference residency and graceful degradation.

## Procedure
1. Set user constraints first: minimum useful context, permitted substitute models/endpoints, latency floor, privacy limits and permission to unload/reload. A product's hard-coded 64K floor is not a universal requirement.
2. Treat other applications as untouchable. Build a measured fit ladder of allowed context/model/residency lanes; pressure may lower a verified ceiling, never justify exceeding it.
3. Choose the degradation order explicitly. Context-first is appropriate only above the required floor. Otherwise queue, switch only to authorised alternatives, or release own residency with a clear unavailable response. Never silently truncate, change models or route to cloud.
4. Separate observation, policy decision, reconciliation and publication. A stale probe or failed reconcile cannot be reported as the engaged lane. Verify actual backing and one completion before announcing ready.
5. Add hysteresis, cooldown and bounded retries to avoid flapping. Heal upward only after stable capacity and confirmation that the selected lane still fits. Preserve in-flight requests or report cancellation explicitly.
6. Default proposed endpoints to loopback. Do not copy recipe auto-publication, tailnet sharing, credentials or lifecycle commands without owner approval. Service restarts and live configuration changes belong to the service owner.

## Verification
Fixture tests cover contention, below-floor capacity, stale probes, failed reconcile, recovery and forbidden fallback. Live soak and failure injection remain separate gated checks.
