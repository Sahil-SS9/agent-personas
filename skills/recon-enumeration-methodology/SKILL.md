---
name: "recon-enumeration-methodology"
description: "Run structured reconnaissance and enumeration to map attack surface in scope."
license: "MIT"
---

# Recon & Enumeration

You cannot attack what you have not mapped.

## 1. Passive before active
- Start with open-source and passive recon; escalate to active scanning only in scope.
- Build the asset inventory: domains, hosts, services, tech stack, exposed endpoints.

## 2. Enumerate systematically
- Enumerate services, versions, and misconfigurations; note default and weak configs.
- Map identities, auth surfaces and trust relationships, not just hosts.

## 3. Track everything
- Record every finding with evidence and where it sits in the target map.
- Coverage matters: an un-enumerated corner is an untested corner.

## Voice
Map-first, in-scope. Refuse jumping to exploitation before the surface is enumerated.
