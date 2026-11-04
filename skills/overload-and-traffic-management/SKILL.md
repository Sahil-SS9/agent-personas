---
name: "overload-and-traffic-management"
description: "Keep the system useful under load and partial failure: timeouts from latency percentiles, single-layer retries with backoff, jitter and budgets, idempotency, deadlines, rate limits, admission control, load shedding and metastable-failure avoidance."
license: "MIT"
---

# Overload and traffic management

Goodput, not throughput: an overloaded server can be busy 100% of the time and complete nothing useful.

## 1. Timeouts on every remote call
- Set each timeout from the dependency's latency distribution: choose an acceptable false-timeout rate (say 0.1%) and use that percentile, with padding where p99.9 is close to p50.
- Know what the timeout covers (connect, DNS, TLS, whole request). Prefer well-tested client libraries.
- Propagate deadlines downstream (remaining time) and cancellation; never start work whose caller has already given up. Deadlines far above normal latency are harmful.

## 2. Retries, carefully
- Retry only idempotent operations, or make them idempotent with client request tokens (same token returns a semantically equivalent result; same token with different parameters is rejected).
- Retry at one layer only. Five layers each retrying three times multiply load at the bottom by 243.
- Exponential backoff with a cap, plus jitter so clients do not synchronise.
- A retry budget (token bucket: retries allowed while tokens remain, e.g. 10% of requests) stops retries amplifying an outage. Prefer it over circuit breakers, whose open/closed modes are hard to test; use breakers only where that behaviour is tested.
- Never retry client errors or malformed requests; return clear retriable vs permanent error codes.

## 3. Admission control and limits
- Rate limits and quotas per client or tenant, sized from negotiated usage, so global overload returns errors only to the heaviest users.
- Model capacity in the resource consumed (CPU, connections, tokens), not raw QPS: request mix changes.
- Client-side adaptive throttling: clients fail requests locally when the backend is rejecting most of them.
- Priorities (criticality): shed sheddable work first; propagate priority downstream.

## 4. Load shedding
Reject early and cheaply when over capacity (queue length, concurrency, latency signals); bound every queue; drop work whose deadline has passed. Instrument every rejection (who, which operation) and alert when shedding starts. Overload-test past the knee: goodput should stay flat as offered load rises.

## 5. Metastable failures
A trigger (spike, brief outage, cache flush) can push a system into a bad state that persists after the trigger ends, sustained by retries, timeouts that re-queue work, or cold caches. Avoid: retry budgets, load shedding, ramping traffic back slowly after recovery, and testing recovery from overload rather than only tolerance of it.

## Output
Per call: timeout and its basis, retry policy (layer, attempts, backoff, jitter, budget), idempotency mechanism; per service: limits, priorities, shedding signal, overload test plan.

## Pitfalls
- Default library timeouts of minutes.
- Retries in the client, gateway and service at once.
- Autoscaling as the only overload defence (too slow for spikes).
