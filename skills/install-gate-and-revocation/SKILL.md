---
name: "install-gate-and-revocation"
description: "Use to write, read or act on the gate record for a third-party skill or MCP server: the approved version, conditions, revocation triggers and kill-switch steps."
license: "MIT"
---

# Install gate and revocation

The gate record is the decision. If it is not written down, the component is not approved.

## Use when
- A vetting or re-vetting verdict needs recording.
- Someone asks "what is installed and why is it trusted?"
- A revocation trigger fires (advisory, drift, incident, owner change).

## Do NOT use when
- No verdict exists yet. Vet first.

## Gate record (one per component version)
```
component, version/commit, artefact sha256, source URL
mcp_tool_definition_hashes: {tool_name: sha256 of the full definition}
verdict, declared_risk_tier, observed_risk_indicators, vetted_on, vetted_by, approver
stages_completed: from [intake, prescan, instruction_review, code_review, dependency_review, sandbox_test, verdict, gate_record]
stages_skipped: [{stage, reason}]
conditions: exact controls (paths, scopes, network, sandbox, human-approval tools)
revocation_triggers: (see below)
re_vet: on every version change and on any trigger below; plus the periodic cadence the owner has set for this risk level (none is set until the owner sets one)
pre_install_plan: what the install will write or change (skills, config files, hooks, MCP servers, env and network access), shown to the approver before any write
evidence: path to the full report
```
Blocked components get a record too: quarantined, with the reason and the quoted evidence, so nobody re-requests them blind.

## Validate before saving (validate, fix, repeat)
Run `python3 scripts/gate_record_check.py record.json`. Fix every problem it lists and re-run until it prints VALID. It checks:
- required fields and a sha256 pin;
- tool-definition hashes for MCP servers;
- APPROVE needs every vetting step, including the sandbox;
- CONDITIONAL needs exact, checkable conditions;
- triggers, approver and a pre-install plan are present;
- quoted evidence for BLOCK;
- no secrets in the record.

## Worked example
```json
{"component": "md-tidy", "version": "1.0.0", "artefact_sha256": "<64 hex>", "source_url": "https://registry.example/md-tidy",
 "verdict": "CONDITIONAL", "vetted_on": "2026-11-23", "vetted_by": "auditor", "approver": "owner",
 "stages_completed": ["intake", "prescan", "instruction_review", "code_review", "dependency_review", "verdict"],
 "stages_skipped": [{"stage": "sandbox_test", "reason": "no bwrap or docker on the target host"}],
 "observed_risk_indicators": [], "evidence": "reports/md-tidy-1.0.0.md",
 "conditions": ["pin sha256 <64 hex>", "no network egress for this skill"],
 "revocation_triggers": ["hash mismatch", "new advisory on any dependency", "publisher change"],
 "pre_install_plan": {"shown_before_write": true, "writes": ["skills/md-tidy/"]}}
```

## Revocation triggers (write them at approval time)
- A hash mismatch or tool-definition drift with no approved update.
- A new advisory affecting the pinned version or any dependency.
- Ownership or maintainer change, repo transfer, or package takeover.
- A behaviour seen at runtime that is outside the approved capabilities (new host, new file access, credential read).
- The publisher pulls the version, or the registry flags it as malicious.
- A condition can no longer be enforced (for example, sandbox removed).

Subscribe to security advisories for every installed component and its dependencies, so the advisory trigger can actually fire.

## When a trigger fires
1. Recommend disabling the component immediately, and say exactly where it is installed (skills folder, MCP config, server process). Disabling is the owner's action.
2. Re-run `update-and-drift-revetting`, or the full vetting sequence, on the current bytes.
3. Record the trigger, the evidence and the new verdict in the gate record.
4. If a compromise is confirmed or likely, hand over to blue-team-security for incident response: credential rotation, evidence preservation, a search for anything the component wrote, and estate-wide exposure. Runtime defence and incident response are not this persona's job. Pass over the gate record and every finding.

## Checklist
- [ ] Record written with every field
- [ ] Install plan shown before any write
- [ ] Approver named
- [ ] Revocation triggers listed
- [ ] Advisory subscription in place
- [ ] gate_record_check.py prints VALID

## Checks
- Every installed third-party component has a current record. Unknown installs are findings: shadow components.
- Every APPROVE or CONDITIONAL has at least one revocation trigger, and the install plan was shown before anything was written.
- Conditions are checkable, not aspirational ("read-only token with repo:read scope", not "use carefully").

## Avoid
- Approving "for now" without a record.
- Deleting the record when a component is removed: history is how repeat requests get answered.
