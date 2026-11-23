---
name: "update-and-drift-revetting"
description: "Use when an installed skill, plugin or MCP server changes version, its tool definitions change, or you need to check whether what is running still matches what was approved."
license: "MIT"
---

# Update and drift re-vetting

An update is a new acquisition. A server that changes its tools after approval (a rug pull) is the attack this skill stops.

## Use when
- A new version is offered, auto-update is pending, or a lockfile hash changed.
- An MCP server's tool list or tool definitions differ from the approved record.
- A routine drift check is due (date in the gate record).

## Do NOT use when
- The component has never been vetted. Run the full vetting sequence (see the persona).

## Procedure (in order)
1. **Load the approved record** (gate record): approved version, artefact hash and, for MCP servers, the hash of every complete tool definition (name, description, `inputSchema`, `outputSchema`, annotations).
2. **Detect drift.** Re-hash the installed artefact and, for MCP, re-list tools and hash each complete definition. Any mismatch with no approved update = **drift incident**: disable the component, then continue at step 3. Hash the whole definition, not just the description: a flipped `readOnlyHint` changes approval behaviour with no visible text change.
3. **Diff the texts, not the release notes.** Compare old and new:
   - every instruction file;
   - tool names, descriptions, parameter names, descriptions and defaults;
   - prompts and resources.
   Run the prescan script from `prescan-and-inventory` on both versions and diff the findings.
4. **Diff the capability surface.** Look for:
   - new tools;
   - new permissions or OAuth scopes;
   - new network hosts;
   - new file paths;
   - new env or credential reads;
   - new install hooks;
   - triggers widened.
   Privilege expansion, trigger change and parameter change are the three rug-pull signals; any one is a finding.
5. **Diff the dependency tree.** Look for:
   - added packages;
   - version moves;
   - source or registry changes;
   - new advisories;
   - removed pins.
6. **Check who changed it.** Look for new maintainers, a transferred repo or package ownership, or an unusual release path (no tag, no CI, a different signer). Ownership change plus a capability change = treat as a new component.
7. **Classify the diff and act.**
   - No behaviour change (docs or typos only): record and approve the new hash.
   - Behaviour change inside the approved capability set: re-run prescan-and-inventory, instruction-layer-review and code-and-capability-review on the changed files.
   - Any capability expansion, new remote fetch, or ownership change: the full vetting sequence.
   - Unexplained change or a confirmed payload: BLOCK, keep the previous approved version pinned, and trigger revocation.
8. **Update the gate record** with the new hashes, or record why the old version stays.

## Tools
- `python3 scripts/tooldef_hash.py snapshot tools.json` creates the per-tool hashes to store in the gate record at approval.
- `python3 scripts/tooldef_hash.py diff approved.json current.json` reports added, removed and changed tools, which fields changed, new or removed parameters, and annotation flips. It exits 1 on any change.
- Get `current.json` from the server's `tools/list` result, captured in the sandbox.

## Worked example
`tooldef_hash.py diff v1.json v2.json` reports:
- `added: ["export_all"]`;
- `send_email` changed: `fields: [description, inputSchema]`, `params_added: ["cc"]`.

The new description says "cc the archive address for compliance". That is a new destination for user data, added in an update, so it is a rug-pull signal. Keep v1 pinned, BLOCK v2, and record the quoted text.

## Checklist
- [ ] Old and new hashes recorded
- [ ] Tool-definition diff run (MCP)
- [ ] Prescan diff run
- [ ] Capability and dependency diffs done
- [ ] Ownership change checked
- [ ] Classification and action recorded
- [ ] Gate record updated

## Checks
- Old and new hashes are both written down.
- Every changed file is either reviewed or listed as not reviewed (which blocks approval).
- The running version equals the approved version when you finish.

## Avoid
- Approving because the changelog says "minor fixes".
- Letting auto-update run before the diff is reviewed. Pin first, review, then move the pin.
