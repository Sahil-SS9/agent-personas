Source: https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html
Author: OWASP Cheat Sheet Series
Read scope: Full page read; selected server-side lifecycle principles distilled
Captured: 2026-09-08T19:32:09.332981+00:00
Rights: original distillation; source rights retained; no source text redistribution.
Target: hermaguard-candidate

# Temporal transaction authorization review

Load only for sensitive operations that have a transaction-authorization policy; do not require a second factor for every ordinary operation.

## Model before hunting
Record actor/tenant, transaction identity, significant approved fields, policy/method, authorization credential, transaction state/version, validity window and the mutation that constitutes execution. Distinguish session authentication from approval for this particular transaction.

## Procedure
1. Trace server-side enforcement: client flags, omitted fields, legacy endpoints and downgraded authorization methods must not bypass the configured policy. Locate the actual execution entrypoint, not merely the UI gate.
2. Define permitted state transitions from proposal through authorization to execution. Identify whether callers can skip steps, replay an earlier transition or replace transaction data between approval and use.
3. Bind authorization to significant transaction data. When those fields change, invalidate or restart approval according to policy; verify that the execution gate evaluates the current approved state rather than a stale authorization boolean.
4. Verify transaction-specific credential validity and expiry at the execution boundary. Replay resistance and single-use consumption must be considered together with the effect. For a race claim, construct a deterministic two-request interleaving; without it label the claim unverified. Atomic check/consume is our implementation-level synthesis of the source's execution-gate requirement.
5. Read alternative entrypoints and error paths. Confirm rejection leaves the sensitive effect unperformed, including after stale approval, method downgrade or token reuse.
6. Report a finding with trusted/untrusted inputs, reachable transition, violated policy, trigger, expected/observed state and reproducible evidence. A missing comment, grep hit or imagined second-factor policy is not evidence of bypass.

## Acceptance scenarios (not executed by these notes)
- Approve amount A, mutate to B, then execute: reject or require renewed approval.
- Two workers consume the same one-use authorization: at most one contracted effect.
- Expired token, another tenant's token or token bound to another transaction: reject.
- Direct execution endpoint and legacy authorization route cannot skip the server-side gate.

## Negative control and limits
An immutable signed transaction with execution-bound verification and documented reusable authorizations must be judged against that actual policy, not an invented blanket single-use rule. Single-use recommendations apply where transaction-specific credentials are part of the contract/threat model. Do not copy numerical ASVS section identifiers without checking the relevant version. Do not reproduce source exploit instructions or run tests on real services.
