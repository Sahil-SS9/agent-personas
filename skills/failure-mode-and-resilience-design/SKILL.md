---
name: "failure-mode-and-resilience-design"
description: "Find every way the design can fail and design containment: failure-mode table per component and dependency, redundancy across failure domains, bulkheads and cells, static stability, degradation and tested recovery."
license: "MIT"
---

# Failure-mode and resilience design

Expect failure, keep things simple, automate recovery. Every integration point (socket, RPC, database call, feed) will eventually hang, fail or flood you.

## 1. Failure-mode table (mandatory)
For every component and every external dependency:
| Component | Failure | Detection | Impact | Mitigation |
|---|---|---|---|---|
Failures to consider: crash, hang or slow response (worse than a fast failure), overload, bad deploy or config, data corruption, dependency outage or brownout, zone or region loss, network partition, clock problems, quota exhaustion, poison input. Impact is stated in user terms and against the SLOs.

## 2. Redundancy and failure domains
- No single points of failure on the critical path; N+1 at least, sized so the system meets the SLO after losing one failure domain (with three zones, run each at most two-thirds utilised).
- Static stability: keep working on the last known good state when a dependency or control plane is impaired; do not need to launch or reconfigure anything during the failure to survive it. Pre-provision instead of scaling up during an outage.
- Keep requests within one zone where possible to limit cross-zone blast radius; deploy one zone or cell at a time.

## 3. Contain the blast radius
- Bulkheads: separate pools (threads, connections, queues, workers) per dependency or workload so one cannot exhaust the rest.
- Cells or shards: independent copies of the stack serving subsets of customers.
- Shuffle sharding: give each customer a random combination of workers so one bad customer affects almost nobody else.
- Canary requests or limited first fan-out before sending a new request type to every node.

## 4. Degrade, do not collapse
Define degraded modes in advance (serve cached or partial results, disable non-critical features, good-enough answers from most shards) and keep them simple. The code path you never run usually does not work, so exercise degraded modes and fallbacks regularly or prefer designs that need none: fail fast and let the caller retry, push data to where it is needed, make the primary path more available.

## 5. Tail latency
Fan-out turns rare slowness into common slowness. Use hedged requests (send a second copy after the 95th-percentile delay, cancel the loser), micro-partitions for fine-grained rebalancing, and selective replication of hot items.

## 6. Recovery
Define recovery time and recovery point per component; backups that are restore-tested; replay from logs; runbooks; and automated recovery where humans are slow. Test by injecting failures (kill nodes, blackhole dependencies, drop a zone) before production does it for you.

## Output
Failure-mode table covering every component in the design, failure-domain plan and capacity after loss, degraded modes, recovery objectives and the tests that prove them.

## Pitfalls
- Redundant instances that share one hidden dependency (same config service, same zone, same certificate).
- Fallback paths that were never exercised.
- Health checks that only test that the process is up, not that it can do useful work.
