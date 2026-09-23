---
name: "attack-path-modelling"
description: "Model plausible attack paths across the kill chain and map coverage gaps."
license: "MIT"
---

# Attack path modelling

## When to use
Any offensive assessment: before scanning, and again after findings emerge.

## Procedure
1. Establish written scope and rules of engagement first: targets, methods, windows, escalation contacts, out-of-bounds. No scope, no engagement.
2. Enumerate the attack surface: what is reachable, authenticated, trusted, or supply-chain adjacent. Map assets the way an adversary would.
3. Model candidate attack paths across the kill-chain stages (recon → initial access → execution → persistence → privilege escalation → credential access → lateral movement → exfiltration → impact); name the ATT&CK technique each step uses.
4. Rank paths by feasibility and impact; a finding matters in proportion to the path it unlocks.
5. Work the web-app checklist systematically (attack surface, authentication, session handling, access control, input handling, business logic) — logic flaws and access-control failures are the perennial leaders.

## Decision rules
- Anything not in scope does not get touched, however tempting.
- Prioritise common failure classes before exotic paths; they recur because they are easy to get wrong.
- Every path must be testable within scope — theoretical-only paths are reported as hypotheses, not findings.

## Pitfalls
- Scanning before scoping.
- Chasing exotic exploits while missing broken access control.

## Done
Scope- authorised ATT&CK-mapped path model with ranked candidates ready for testing.