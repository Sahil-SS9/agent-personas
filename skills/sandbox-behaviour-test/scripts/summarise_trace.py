#!/usr/bin/env python3
"""Summarise a sandbox_trace.sh run into observed behaviour plus findings.

Usage: summarise_trace.py <out_dir>   (reads trace.log, canary-marker.txt,
stdout.txt, stderr.txt, home-writes.txt; writes behaviour.json)
Exit 0 = no findings, 1 = findings, 2 = missing inputs.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CRED_PATHS = re.compile(r"/home/sandbox/(\.ssh/|\.aws/|\.env\b|\.config/gh/|\.netrc|\.npmrc|\.pypirc|\.git-credentials)")
SYSTEM_PREFIXES = ("/usr/", "/lib", "/proc/", "/dev/", "/etc/", "/pkg", "/tmp/", "/sys/")
OPEN_RE = re.compile(r'^(\d+)\s+(openat|open|stat|newfstatat|statx|access|faccessat2?|readlink|lstat)\((?:[^,]*,\s*)?"([^"]+)"')
WRITE_OPEN_RE = re.compile(r'O_WRONLY|O_RDWR|O_CREAT|O_APPEND')
CONNECT_RE = re.compile(r'^(\d+)\s+connect\(\d+,\s*\{sa_family=(AF_INET6?|AF_UNIX)[^}]*?(?:sin6?_port=htons\((\d+)\)[^}]*?(?:inet_addr|inet_pton)\([^"]*"([^"]+)"|sun_path="([^"]+)")')
EXEC_RE = re.compile(r'^(\d+)\s+execve\("([^"]+)",\s*\[([^\]]*)\]')


def summarise(out: Path) -> dict:
    trace = (out / "trace.log").read_text(errors="replace").splitlines()
    mark = (out / "canary-marker.txt").read_text().strip()
    files_read, files_written, cred_touch, connects, execs, leaks = set(), set(), set(), [], [], []
    for line in trace:
        m = OPEN_RE.match(line)
        if m:
            path = m.group(3)
            if CRED_PATHS.search(path):
                cred_touch.add(path)
            if not path.startswith(SYSTEM_PREFIXES):
                (files_written if WRITE_OPEN_RE.search(line) else files_read).add(path)
            elif path.startswith("/pkg") and WRITE_OPEN_RE.search(line):
                files_written.add(path)
        m = CONNECT_RE.match(line)
        if m:
            target = m.group(5) or f"{m.group(4)}:{m.group(3)}"
            connects.append(target)
        m = EXEC_RE.match(line)
        if m:
            execs.append(m.group(2) + " " + m.group(3)[:160])
        if mark in line and re.match(r"^\d+\s+(write|sendto|sendmsg|connect)\(", line):
            leaks.append(line[:240])
    for name in ("stdout.txt", "stderr.txt"):
        p = out / name
        if p.exists() and mark in p.read_text(errors="replace"):
            leaks.append(f"canary value printed to {name}")
    home_writes = [l for l in (out / "home-writes.txt").read_text().splitlines() if l] if (out / "home-writes.txt").exists() else []

    findings = []
    if cred_touch:
        findings.append({"severity": "HIGH", "rule": "credential_access", "detail": sorted(cred_touch)})
    if leaks:
        findings.append({"severity": "HIGH", "rule": "canary_exfiltration", "detail": leaks[:20]})
    if connects:
        findings.append({"severity": "HIGH", "rule": "network_attempt",
                         "detail": sorted(set(connects)),
                         "note": "compare with declared hosts; any undeclared host is a finding"})
    if home_writes or any(p.startswith("/home/sandbox") for p in files_written):
        findings.append({"severity": "HIGH", "rule": "home_write",
                         "detail": sorted(set(home_writes) | {p for p in files_written if p.startswith('/home/sandbox')}),
                         "note": "writes to the user's home (persistence, memory, dotfiles)"})
    if any(p.startswith("/pkg") for p in files_written):
        findings.append({"severity": "MEDIUM", "rule": "self_modification_attempt",
                         "detail": sorted(p for p in files_written if p.startswith("/pkg"))})
    shells = [e for e in execs if re.search(r"/(ba|z|da)?sh\b|curl|wget|nc\b|ncat|python3? -c", e)]
    if len(execs) > 1 and shells:
        findings.append({"severity": "MEDIUM", "rule": "child_process", "detail": shells[:20],
                         "note": "compare with declared capabilities"})
    report = {
        "exit_code": (out / "exit-code.txt").read_text().strip() if (out / "exit-code.txt").exists() else None,
        "processes": execs[:50],
        "files_read_outside_system": sorted(files_read)[:200],
        "files_written": sorted(files_written)[:200],
        "credential_paths_touched": sorted(cred_touch),
        "network_attempts": sorted(set(connects)),
        "findings": findings,
        "reminder": "One clean run does not prove safety: conditional triggers (date, host, CI, first-run) may not fire here.",
    }
    (out / "behaviour.json").write_text(json.dumps(report, indent=2))
    return report


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    out = Path(argv[0])
    if not (out / "trace.log").exists() or not (out / "canary-marker.txt").exists():
        print(f"missing trace.log or canary-marker.txt in {out}", file=sys.stderr)
        return 2
    r = summarise(out)
    for f in r["findings"]:
        print(f"[{f['severity']}] {f['rule']}: {f['detail']}")
    print(f"processes={len(r['processes'])} network_attempts={len(r['network_attempts'])} findings={len(r['findings'])}")
    return 1 if r["findings"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
