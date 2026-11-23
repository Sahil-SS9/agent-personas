#!/usr/bin/env python3
"""Validate a gate record before it is accepted. Validate, fix, repeat until clean.

Usage: gate_record_check.py <record.json>
Exit 0 = valid, 1 = problems listed, 2 = unreadable input.

Rules enforced (each maps to a check in the gate skill):
- required fields present and non-empty
- verdict is BLOCK, CONDITIONAL or APPROVE
- artefact sha256 is 64 hex characters (pinning by content hash)
- MCP servers carry a hash for every tool definition
- APPROVE: every vetting step completed, none skipped, sandbox test done
- CONDITIONAL: at least one exact condition; skipped steps listed with reasons
- APPROVE and CONDITIONAL: at least one revocation trigger, an approver, and
  an install plan shown before any write
- BLOCK: quoted evidence present
- no secret-looking values anywhere in the record
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STEPS = ["intake", "prescan", "instruction_review", "code_review", "dependency_review",
         "sandbox_test", "verdict", "gate_record"]
REQUIRED = ["component", "version", "artefact_sha256", "source_url", "verdict", "vetted_on",
            "vetted_by", "stages_completed", "stages_skipped", "observed_risk_indicators", "evidence"]
SECRETS = re.compile(r"(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[abp]-[A-Za-z0-9-]{10,})")


def check(rec: dict) -> list[str]:
    p = []
    for k in REQUIRED:
        if k not in rec or rec[k] in (None, "", []) and k not in ("stages_skipped", "observed_risk_indicators"):
            p.append(f"missing or empty: {k}")
    v = rec.get("verdict")
    if v not in ("BLOCK", "CONDITIONAL", "APPROVE"):
        p.append(f"verdict must be BLOCK, CONDITIONAL or APPROVE (got {v!r})")
    if not re.fullmatch(r"[0-9a-f]{64}", str(rec.get("artefact_sha256", ""))):
        p.append("artefact_sha256 must be a 64-character lowercase hex sha256")
    if rec.get("kind") == "mcp_server":
        hashes = rec.get("mcp_tool_definition_hashes") or {}
        if not hashes:
            p.append("MCP server record needs mcp_tool_definition_hashes (tooldef_hash.py snapshot)")
        elif not all(re.fullmatch(r"[0-9a-f]{64}", str(h)) for h in hashes.values()):
            p.append("every tool definition hash must be a sha256")
    done = set(rec.get("stages_completed") or [])
    skipped = rec.get("stages_skipped") or []
    unknown = done - set(STEPS)
    if unknown:
        p.append(f"unknown stage names: {sorted(unknown)} (use {STEPS})")
    if v == "APPROVE":
        missing = [s for s in STEPS[:6] if s not in done]
        if missing:
            p.append(f"APPROVE needs every vetting step completed; missing {missing}")
        if skipped:
            p.append("APPROVE cannot have skipped stages")
    if v == "CONDITIONAL":
        if not rec.get("conditions"):
            p.append("CONDITIONAL needs at least one exact condition")
        for s in skipped:
            if not (isinstance(s, dict) and s.get("stage") and s.get("reason")):
                p.append("each skipped stage needs {stage, reason}")
                break
    if v in ("APPROVE", "CONDITIONAL"):
        if not rec.get("revocation_triggers"):
            p.append("needs at least one revocation trigger")
        if not rec.get("approver"):
            p.append("needs the approver (the owner installs, not the auditor)")
        plan = rec.get("pre_install_plan") or {}
        if not plan or plan.get("shown_before_write") is not True:
            p.append("needs pre_install_plan with shown_before_write: true")
        for c in rec.get("conditions") or []:
            if re.search(r"\b(carefully|be careful|monitor closely|as appropriate|if needed)\b", str(c), re.I):
                p.append(f"condition is not checkable: {c!r}")
    if v == "BLOCK":
        ev = rec.get("evidence")
        if not ev or not any(isinstance(e, dict) and e.get("quote") and e.get("file") for e in (ev if isinstance(ev, list) else [])):
            p.append("BLOCK needs at least one evidence item with file and quote")
    if SECRETS.search(json.dumps(rec)):
        p.append("record contains a secret-looking value: redact it")
    return p


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    try:
        rec = json.loads(Path(argv[0]).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    problems = check(rec)
    for x in problems:
        print(f"- {x}")
    print("VALID" if not problems else f"{len(problems)} problem(s): fix and re-run")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
