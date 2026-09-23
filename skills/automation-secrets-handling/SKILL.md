---
name: "automation-secrets-handling"
description: "Handle credentials in automations safely: no plaintext, least privilege, rotation."
license: "MIT"
---

# Automation Secrets Handling

Automations run unattended; a leaked secret runs unattended too.

## 1. Never in plaintext
- Secrets come from a vault/secret manager at runtime, never hardcoded or committed.
- No secrets in logs, error messages, or command lines.

## 2. Least privilege, scoped
- Each automation gets its own scoped credential with only the access it needs.
- Short-lived tokens over long-lived keys where possible.

## 3. Rotatable and auditable
- Rotation must not require code changes; reference secrets, don't embed them.
- Access is logged; a compromised automation must be revocable fast.

## Voice
Vault-first. Refuse an automation that reads a hardcoded API key from the script.
