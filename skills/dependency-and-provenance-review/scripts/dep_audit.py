#!/usr/bin/env python3
"""Audit the dependencies a third-party agent component ships with.

Usage: dep_audit.py <package_dir> [--osv] [--popular names.txt] [--json]

Reads requirements*.txt, pyproject.toml ([project] dependencies), package.json
and package-lock.json. For every dependency it reports:
  - pin status (exact pin, hash pin, range, unpinned, URL/git source)
  - non-default package sources (index-url, extra-index-url, registry, git, URL)
  - possible typosquats: one edit, or a separator/character swap, away from a
    popular name. PyPI names are compared with the bundled top-1000 list
    (top-pypi-1000.json, with its source and date inside). npm needs --popular.
  - known vulnerabilities via the OSV.dev batch API (only with --osv; needs
    network; exact pins only, because OSV needs a version)
Exit 0 = no HIGH finding, 1 = HIGH finding, 2 = usage error.
Read-only: it never installs or imports anything from the package.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OFFICIAL = {"pypi.org", "files.pythonhosted.org", "registry.npmjs.org", "registry.yarnpkg.com"}
# Vendor-run indexes that are legitimate but still replace or extend the default source:
# reported MEDIUM so the auditor confirms the host is the vendor's real one.
KNOWN_VENDOR = {"download.pytorch.org", "wheels.vllm.ai", "pypi.nvidia.com"}
OSV_URL = "https://api.osv.dev/v1/querybatch"


def norm(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def edit1(a: str, b: str) -> bool:
    """True when a and b differ by exactly one insert, delete, substitute or adjacent swap."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        return len(diff) == 1 or (len(diff) == 2 and diff[1] == diff[0] + 1
                                  and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]])
    s, l = (a, b) if len(a) < len(b) else (b, a)
    return any(l[:i] + l[i + 1:] == s for i in range(len(l)))


def typosquat_of(name: str, popular: set[str]) -> str | None:
    n = norm(name)
    if n in popular:
        return None
    squashed = n.replace("-", "")
    for p in popular:
        if edit1(n, p) or (squashed == p.replace("-", "") and n != p):
            return p
    return None


def parse_requirements(path: Path) -> tuple[list[dict], list[dict]]:
    deps, sources = [], []
    for ln, raw in enumerate(path.read_text(errors="replace").splitlines(), 1):
        line = raw.split(" #")[0].strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"(--index-url|-i|--extra-index-url|--find-links|-f)\s*=?\s*(\S+)", line)
        if m:
            host = re.sub(r"^https?://([^/:]+).*", r"\1", m.group(2)).lower()
            sources.append({"file": path.name, "line": ln, "kind": m.group(1), "url": m.group(2),
                            "official": host in OFFICIAL})
            continue
        if line.startswith("-"):
            continue
        name = re.split(r"[\s\[<>=!~;@]", line, maxsplit=1)[0]
        if "@" in line and re.search(r"@\s*(git\+|https?://|file:)", line):
            pin = "url-or-git"
        elif "--hash=" in raw:
            pin = "hash"
        elif re.search(r"===?\s*[\w.]+", line) and not re.search(r"[<>~*]", line):
            pin = "exact"
        elif re.search(r"[<>=~!]", line):
            pin = "range"
        else:
            pin = "unpinned"
        ver = re.search(r"===?\s*([\w.]+)", line)
        deps.append({"ecosystem": "PyPI", "name": name, "version": ver.group(1) if ver and pin in ("exact", "hash") else None,
                     "pin": pin, "file": path.name, "line": ln})
    return deps, sources


def parse_pyproject(path: Path) -> list[dict]:
    try:
        import tomllib
    except ModuleNotFoundError:  # Python < 3.11
        return []
    data = tomllib.loads(path.read_text())
    out = []
    for spec in data.get("project", {}).get("dependencies", []):
        name = re.split(r"[\s\[<>=!~;@]", spec, maxsplit=1)[0]
        exact = re.search(r"==\s*([\w.]+)", spec)
        pin = "exact" if exact and not re.search(r"[<>~*]", spec) else ("range" if re.search(r"[<>=~]", spec) else "unpinned")
        out.append({"ecosystem": "PyPI", "name": name, "version": exact.group(1) if pin == "exact" else None,
                    "pin": pin, "file": path.name, "line": 0})
    return out


def parse_package_json(path: Path, lock: dict | None) -> tuple[list[dict], list[dict]]:
    pj = json.loads(path.read_text())
    deps, hooks = [], []
    locked = (lock or {}).get("packages", {})
    for sect in ("dependencies", "optionalDependencies", "peerDependencies"):
        for name, spec in pj.get(sect, {}).items():
            if not isinstance(spec, str):
                continue
            if re.match(r"^(git|https?|file|github:)", spec) or "/" in spec and not spec.startswith("@"):
                pin = "url-or-git"
            elif re.match(r"^\d+\.\d+\.\d+([-+][\w.]+)?$", spec):
                pin = "exact"
            elif spec in ("*", "latest", ""):
                pin = "unpinned"
            else:
                pin = "range"
            lv = locked.get(f"node_modules/{name}", {})
            deps.append({"ecosystem": "npm", "name": name,
                         "version": spec if pin == "exact" else lv.get("version"),
                         "pin": pin, "locked": bool(lv), "integrity": bool(lv.get("integrity")),
                         "file": path.name, "line": 0})
    for hook in ("preinstall", "install", "postinstall", "prepare"):
        if hook in pj.get("scripts", {}):
            hooks.append({"file": path.name, "hook": hook, "command": pj["scripts"][hook]})
    return deps, hooks


def osv_lookup(deps: list[dict]) -> dict[int, list[str]]:
    queries, idx = [], []
    for i, d in enumerate(deps):
        if d.get("version"):
            queries.append({"package": {"name": d["name"], "ecosystem": d["ecosystem"]}, "version": d["version"]})
            idx.append(i)
    if not queries:
        return {}
    req = urllib.request.Request(OSV_URL, data=json.dumps({"queries": queries}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        results = json.loads(r.read()).get("results", [])
    return {idx[k]: [v["id"] for v in res.get("vulns", [])] for k, res in enumerate(results) if res.get("vulns")}


def audit(root: Path, use_osv: bool = False, popular_extra: set[str] | None = None) -> dict:
    deps, sources, hooks = [], [], []
    for p in sorted(root.rglob("requirements*.txt")):
        d, s = parse_requirements(p)
        deps += d
        sources += s
    for p in sorted(root.rglob("pyproject.toml")):
        deps += parse_pyproject(p)
    for p in sorted(root.rglob("package.json")):
        if "node_modules" in p.parts:
            continue
        lockp = p.with_name("package-lock.json")
        lock = json.loads(lockp.read_text()) if lockp.exists() else None
        d, h = parse_package_json(p, lock)
        deps += d
        hooks += h
    for p in list(root.rglob(".npmrc")) + list(root.rglob("pip.conf")):
        for ln, line in enumerate(p.read_text(errors="replace").splitlines(), 1):
            m = re.search(r"(registry|index-url|extra-index-url)\s*=\s*(\S+)", line)
            if m:
                host = re.sub(r"^https?://([^/:]+).*", r"\1", m.group(2)).lower()
                sources.append({"file": p.name, "line": ln, "kind": m.group(1), "url": m.group(2), "official": host in OFFICIAL})

    pypi_pop = {norm(n) for n in json.loads((HERE / "top-pypi-1000.json").read_text())["projects"]}
    findings = []
    for d in deps:
        pop = pypi_pop | (popular_extra or set()) if d["ecosystem"] == "PyPI" else (popular_extra or set())
        t = typosquat_of(d["name"], pop) if pop else None
        if t:
            findings.append({"severity": "HIGH", "rule": "possible_typosquat", "dep": d["name"], "looks_like": t, "file": d["file"]})
        if d["pin"] in ("unpinned", "range"):
            findings.append({"severity": "MEDIUM", "rule": "not_exactly_pinned", "dep": d["name"], "pin": d["pin"], "file": d["file"]})
        if d["pin"] == "url-or-git":
            findings.append({"severity": "HIGH", "rule": "url_or_git_source", "dep": d["name"], "file": d["file"]})
    for s in sources:
        if not s["official"]:
            host = re.sub(r"^https?://([^/:]+).*", r"\1", s["url"]).lower()
            sev = "MEDIUM" if host in KNOWN_VENDOR else "HIGH"
            findings.append({"severity": sev, "rule": "non_default_registry", **s})
    for h in hooks:
        findings.append({"severity": "HIGH", "rule": "install_hook", **h})
    osv_error = None
    if use_osv:
        try:
            for i, ids in osv_lookup(deps).items():
                findings.append({"severity": "HIGH", "rule": "known_vulnerability", "dep": deps[i]["name"],
                                 "version": deps[i]["version"], "advisories": ids})
        except OSError as e:
            osv_error = f"OSV lookup failed: {e}. Vulnerability status is UNKNOWN, not clean."
    return {"dependencies": deps, "sources": sources, "install_hooks": hooks, "findings": findings,
            "osv_checked": use_osv and osv_error is None, "osv_error": osv_error,
            "unversioned_for_osv": [d["name"] for d in deps if not d.get("version")]}


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    root = Path(argv[0])
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    extra = None
    if "--popular" in argv:
        extra = {norm(x) for x in Path(argv[argv.index("--popular") + 1]).read_text().split() if x}
    r = audit(root, "--osv" in argv, extra)
    if "--json" in argv:
        print(json.dumps(r, indent=2))
    else:
        print(f"{len(r['dependencies'])} dependencies; osv_checked={r['osv_checked']}")
        for f in r["findings"]:
            print(f"[{f['severity']}] {f['rule']}: " + ", ".join(f"{k}={v}" for k, v in f.items() if k not in ('severity', 'rule')))
        if r["osv_error"]:
            print(r["osv_error"])
        if r["unversioned_for_osv"]:
            print("No exact version, so OSV cannot check: " + ", ".join(r["unversioned_for_osv"]))
    return 1 if any(f["severity"] == "HIGH" for f in r["findings"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
