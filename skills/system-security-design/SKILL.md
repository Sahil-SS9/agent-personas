---
name: "system-security-design"
description: "Build security into the system design: trust boundaries, identities, authorisation model, secrets, encryption, tenant isolation, abuse limits and personal data handling, with threats tied to concrete controls."
license: "MIT"
---

# System security design

Security is a property of the architecture, not a review at the end. This skill covers design-time choices; deep threat modelling, testing and detection belong to the security personas.

## 1. Trust boundaries
Draw them on the container diagram: internet to edge, edge to services, service to service, service to data, your system to third parties and model providers. Every crossing gets: authentication, authorisation, input validation, encryption in transit, logging.

## 2. Identity and authorisation
- Users: a central identity provider (federated identity); short-lived tokens; MFA for privileged roles.
- Services: workload identities (mTLS or signed tokens), never shared static keys.
- Authorisation model chosen explicitly (roles, attributes, relationship-based) and enforced server-side at the resource, including in caches, search indexes and vector stores.
- Least privilege for every component; separate read and write credentials where possible.

## 3. Data protection
- Classify data (public, internal, confidential, personal, special category). Minimise what you collect; keep personal data out of logs, analytics and model prompts unless needed.
- Encrypt at rest and in transit; manage keys in a key service; plan rotation.
- Secrets in a secrets manager, never in code, images or config files; rotate them.
- Retention and deletion that reach replicas, backups, caches and derived indexes.
- Data residency requirements decide region placement.

## 4. Multi-tenancy
Tenant id on every request and every row; enforce isolation in queries, caches, queues, object paths and indexes; per-tenant limits; consider cells for large or regulated tenants.

## 5. Abuse and availability
Rate limits and quotas, bot and fraud signals, request size limits, validation of uploads, protection of expensive endpoints (search, exports, AI calls) against denial of wallet.

## 6. Threat-to-control table
| Threat | Where | Control | Owner | How tested |
|---|---|---|---|---|
Use STRIDE-style prompts (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) at each boundary. Controls must live in code or infrastructure, not in documentation or prompts.

## Output
Trust-boundary diagram notes, identity and authorisation model, data classification and handling, tenant isolation, abuse limits, threat-to-control table.

## Pitfalls
- Authorisation checked in the UI or gateway only.
- Derived stores (search, cache, vectors) that bypass access control.
- Logging tokens, secrets or personal data.
