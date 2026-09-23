---
name: "api-security-design"
description: "Design API security: authentication, authorization, rate limiting and abuse controls."
license: "MIT"
---

# API Security Design

An API contract without a security model is an open door.

## 1. AuthN and AuthZ are separate
- Authenticate who is calling (tokens/OAuth) and authorize what they may do (scopes/roles) — both, distinctly.
- Enforce authorization server-side per resource; never trust the client to self-limit.

## 2. Least privilege by default
- Scope tokens narrowly; deny by default and grant explicitly.
- Sensitive actions need explicit, auditable permission.

## 3. Protect against abuse
- Rate-limit and throttle per client; validate and bound all input.
- Never leak internals in errors; log security events for audit.

## Voice
Deny-by-default. Refuse an endpoint that authenticates but never checks authorization.
