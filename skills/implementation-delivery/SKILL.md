---
name: implementation-delivery
description: Use when implementing a feature or bug fix through verified delivery.
version: 0.2.1
author: Sahil Saghir
license: MIT
---

# Implementation Delivery

Operational method; evidence is limited to the scenarios actually exercised.

1. Find the executable entrypoint, real caller, persistence boundary and current tests before choosing an implementation. Record the observed behaviour and required change separately.

2. Define one vertical acceptance slice and failure cases. Prefer an existing capability or standard library over a new dependency; record why reuse does or does not fit. Do not build a framework for hypothetical future variants.

3. For bugs, reproduce the failure first. For features, witness a focused test fail for the missing behaviour, implement minimally, then refactor while green. A missing import or broken harness is not the desired RED.

4. Preserve error semantics, resource ownership, ordering and compatibility. For mutating remote calls, first resolve intent, uncertain outcomes, atomicity and retention using [remote-operation procedure](references/retry-intent.md); do not impose distributed machinery on local-only changes. Test the real integration seam rather than only mocking the implementation you just wrote.

5. Use simplify-swarm-candidate after the slice works. Use hermaguard-candidate on the resulting diff plus its callers; remediate confirmed findings with regression tests and rerun affected checks.

6. Exercise the user-facing entrypoint, build/type checks and relevant regressions. Deliver scoped commits and a PR-ready packet with actual commands, results, unresolved risks and rollback. Creating a PR, merging and deploying require their own authority.

## Provenance and limits
Read [source synthesis](SOURCE-SYNTHESIS.md) when assessing origin, conflicting guidance or evidence maturity.

## Source-grounded decision rules

Legacy seams: name the replaceable dependency and its enabling point before changing legacy code. Prove the test activates that seam; retain a real-boundary integration test so a passing substitute cannot hide broken production wiring (Feathers, chapter 4).

Design two plausible interfaces before a consequential extraction. Prefer the simplest interface covering current needs without leaking UI or vendor policy into the mechanism. Reject speculative options and parameter-heavy generic frameworks (Ousterhout, chapter 6 and 21).

For dependency upgrades, freeze old/new versions and exercise downstream runtime, error and serialization contracts, not installation alone. The wiki motivates this negative scenario; no benchmark success percentage is inherited.
