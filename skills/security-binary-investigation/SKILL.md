---
name: "security-binary-investigation"
description: "Investigate binaries for security-relevant behaviour: launch chains, injection, persistence, obfuscation and qualified impact."
license: "MIT"
---

# Security-focused binary investigation

Determine what a binary does to the systems that run it, with mechanism-level evidence — and say precisely how far the evidence reaches.

## When to use
Triage-to-verdict investigation of suspicious artefacts: suspected malware, an unexplained crash with security potential, a supply-chain artefact review, or security assessment of a binary within authorised scope.

## Procedure
1. Frame the question in security terms: what is the suspected behaviour (launch, injection, persistence, credential access, egress, stealth), and what answer would change the owner's decision?
2. Investigate the mechanism chain, not the API name list: for a suspected launch/injection mechanism, separate payload storage from the execution mechanism; trace process/thread/target identity and handle ownership; record memory destination, data provenance, sizes and protection changes; relate allocation+write evidence to the subsequent thread/hook/queue operation. Name a recovered mechanism against the ATT&CK process-injection sub-technique taxonomy only when mechanism evidence, not a matching import, supports it.
3. Recover configuration, payloads and command channels as data: decoding embedded config keys, C2 formats or resource payloads; store decoded artefacts with hashes alongside the code paths that produce them.
4. Characterise obfuscation rather than admiring it: packers, string encoding, control-flow flattening, anti-debug/anti-VM. For each layer, record the mechanism and the unpacked/decoded result — and state every remaining blind spot the layer creates.
5. Escalate to fuzzing and symbolic analysis by evidence need (a parser whose crash conditions matter, a decoding routine too complex to read), with explicit budgets and coverage honesty: solver completion is not coverage proof.
6. Qualify impact with witness-first discipline: reproduce a witness (input → defect → effect) before claiming exploitability; a crash is not a vulnerability; a mechanism existing statically is not proof it executes.
7. Apply negative controls: benign software uses the same APIs (instrumentation tools, debuggers, accessibility software, ordinary installers). A finding must explain why the hostile interpretation is the right one.
8. Report with the evidence boundary: what was observed, what was inferred, what is unknown, and what environment limits applied. Separately flag detection-relevant observables for handoff.

## Decision rules
- Attribution beyond the artefact (actor, campaign) requires corroboration this investigation actually has; usually the honest answer is "consistent with", not "is".
- No offensive capability development: describing a mechanism is the deliverable; writing working exploit/injection/persistence code is out of role and refused without a separate, explicit owner authorisation.
- If the investigation cannot answer the framing question, deliver the partial answer with the boundary stated — never a confident-sounding guess.

## Pitfalls
- Strings/imports/capability-rule hits reported as behaviour.
- Trusted-looking executable paths treated as proof of mapped bytes' identity.
- Reporting "T1055" without the mechanism evidence that distinguishes it from benign API use.

## Done
An investigation report: mechanism-level findings with per-claim evidence, negative controls, qualified impact, ATT&CK-mapped behaviours where justified, decoded artefacts with hashes, and explicit unknowns — plus the detection-observables handoff note.