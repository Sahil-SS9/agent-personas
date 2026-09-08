---
name: "flaky-test-manager"
description: "Detect, quarantine and fix flaky tests using root-cause taxonomy."
license: "MIT"
---
# Flaky Test Manager

## Use when
- CI fails intermittently on unchanged code
- A suite's red build is routinely dismissed as "probably a flake"
- Retry/re-run rates are climbing

## Instructions

1. Confirm flakiness first: a test that passes and fails on the SAME commit.
   Re-run in isolation before classifying. Real regressions fail consistently
   after a specific change.
2. Classify by root cause (Luo et al. taxonomy, with modern additions):
   - Async wait (~45%): hard-coded sleeps; replace with explicit state polls
     or event waits — never lengthen the sleep.
   - Concurrency/races (~20%): shared fixtures, parallel data writes;
     serialise the conflicting resource or scope fixtures per-worker.
   - Order dependency (~12%; ~59% of Python flakes): randomise order with a
     RECORDED seed; fix leakage via proper setup/teardown, not run-order.
   - Resource leaks (~8%): connections/files/threads not torn down.
   - Network/external (~5%): stub at the boundary; never depend on third-
     party uptime for correctness signals.
   - Time/randomness/other (~10%): freeze clocks, seed RNGs explicitly.
   - Modern E2E additions: selector drift (hashed classes) — prefer
     role/text/test-id selectors; cluster analysis — 75% of flakes co-occur,
     fix the cluster cause not each symptom.
3. Quarantine discipline: move confirmed-flaky tests to a quarantine lane
   that CANNOT block merges, with a visible budget (count + age). A quarantined
   test older than its budget is either fixed or deleted — never ignored.
4. Retry rules: retries allowed only with an automatic root-cause label on
   every retry; uncapped blind retries destroy CI signal (59% of devs ignore
   CI when flaky history accumulates).
5. Size discipline (SE@Google): classify tests small (no I/O), medium
   (localhost only), large; flakes concentrate in oversized tests — shrink
   the test before hardening it.
6. Report the signal cost, not just the count: "N flaky failures this week
   means M real regressions we could have missed."

## Stop conditions
- Never mark a failing test as flaky without same-commit evidence.
- Never fix flakiness by increasing timeouts alone.

## Escalation
- Flakes originating in production code (concurrency bugs) go to the owning
  team as defects, not test chores.
