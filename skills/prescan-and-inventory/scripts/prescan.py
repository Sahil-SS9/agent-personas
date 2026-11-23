#!/usr/bin/env python3
"""Deterministic pre-scan of a third-party agent skill or MCP server package.

Stdlib only. Read-only: never imports, executes or installs anything from the package.
Usage: python3 prescan.py <package_dir> [--json]

Reports byte-level and pattern-level signals that a reading model tends to miss.
Every finding is a LEAD for the auditor to confirm by reading the cited file and
line. It is not a verdict: a clean pre-scan does not mean safe, and the manual
stages still run.
"""
from __future__ import annotations

import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".py", ".js", ".mjs", ".cjs", ".ts", ".sh", ".bash", ".zsh",
            ".json", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".html", ".svg", ".ps1",
            ".rb", ".go", ".rs", ".env", ".npmrc", ".pypirc", ""}
BINARY_EXT = {".pyc", ".pyo", ".so", ".dll", ".dylib", ".exe", ".bin", ".class", ".jar",
              ".whl", ".node", ".wasm"}
ARCHIVE_EXT = {".zip", ".tar", ".gz", ".tgz", ".7z", ".rar", ".xz", ".bz2"}
MAX_BYTES = 2_000_000

INVISIBLE = {
    "tag_block": lambda c: 0xE0000 <= ord(c) <= 0xE007F,
    "zero_width": lambda c: c in "\u200b\u200c\u200d\u2060\ufeff\u180e",
    "bidi_control": lambda c: c in "\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069\u200e\u200f",
    "variation_selector": lambda c: 0xFE00 <= ord(c) <= 0xFE0E or 0xE0100 <= ord(c) <= 0xE01EF,
}
# U+FE0F (emoji presentation) is excluded: it follows most emoji in normal text.
OFFICIAL_HOSTS = {"pypi.org", "files.pythonhosted.org", "registry.npmjs.org", "registry.yarnpkg.com",
                  "download.pytorch.org", "crates.io", "static.crates.io", "proxy.golang.org",
                  "rubygems.org", "repo.maven.apache.org", "github.com", "objects.githubusercontent.com"}
SKIP_DIRS = {".git", ".hg", ".svn", "node_modules", ".venv", "venv"}

# (rule, severity, regex, note)
PATTERNS = [
    ("remote_script_pipe", "HIGH", r"(curl|wget)[^\n|]{0,200}\|\s*(sudo\s+)?(ba|z)?sh\b",
     "downloads and executes a remote script"),
    ("registry_redirect", "HIGH",
     r"(--index-url|--extra-index-url|PIP_INDEX_URL|PIP_EXTRA_INDEX_URL|npm_config_registry|"
     r"npm\s+config\s+set\s+registry|--registry[ =]|registry\s*=\s*https?://|index-url\s*=)",
     "package source redirected; confirm the host is the official registry"),
    ("exec_eval", "MEDIUM", r"\b(eval|exec)\s*\(|new\s+Function\s*\(|shell\s*=\s*True|os\.system\s*\(|"
     r"child_process|subprocess\.(Popen|run|call|check_output)\s*\(", "dynamic code or shell execution"),
    ("decode_then_exec", "HIGH",
     r"(b64decode|base64\s+-d|atob\(|fromCharCode|bytes\.fromhex|codecs\.decode)[^\n]{0,160}"
     r"(exec|eval|system|Popen|\|\s*(ba|z)?sh\b)", "decodes data and executes it"),
    ("env_dump", "HIGH", r"(os\.environ\b(?!\s*(\.get|\[|\.setdefault|\.copy\(\)\s*$))|dict\(os\.environ\)|"
     r"process\.env\b(?![.\[])|\bprintenv\b|(^|[;&|]\s*)env\s*($|[|>]))",
     "reads the whole environment (credentials live there)"),
    ("sensitive_path", "HIGH",
     r"(~|\$HOME|home/[^/\s]+)/\.(ssh|aws|gnupg|kube|docker|netrc|npmrc|pypirc|git-credentials)\b|"
     r"\bid_rsa\b|\bid_ed25519\b|(open|cat|read|load_dotenv)[^\n]{0,20}['\"\s/]\.env\b|Login Data|Cookies\.sqlite|"
     r"security\s+find-(generic|internet)-password",
     "touches credential or key material"),
    ("network_send", "MEDIUM",
     r"(requests\.(post|put)|urllib\.request\.urlopen|http\.client|fetch\(|axios\.(post|put)|"
     r"curl\s+[^\n]*(-d|--data|-F|-T)|socket\.connect|XMLHttpRequest|websocket)",
     "sends data over the network"),
    ("instruction_override", "HIGH",
     r"(ignore|disregard|forget)\s+(all\s+|any\s+)?(previous|prior|above|earlier|other)\s+"
     r"(instructions|rules|guidance|messages)|you\s+are\s+now\s+in\s+\w+\s+mode|"
     r"(do\s+not|don't|never)\s+(tell|inform|mention|reveal|show)\s+(this\s+to\s+)?(the\s+)?user|"
     r"without\s+(telling|informing|asking)\s+the\s+user|"
     r"(reveal|print|output|repeat|show|send)\s+(me\s+)?(your|the)\s+(full\s+)?system\s+prompt",
     "instruction aimed at the agent, not the user"),
    ("hidden_markup", "MEDIUM", r"<!--[\s\S]{0,2000}?-->|\[//\]:\s*#|<\s*(div|span|p)[^>]*display\s*:\s*none",
     "comment or hidden markup: read its contents"),
    ("data_uri", "MEDIUM", r"data:[a-z]+/[a-z0-9.+-]+;base64,", "inline data URI"),
    ("long_base64", "MEDIUM", r"[A-Za-z0-9+/]{200,}={0,2}", "long base64-like blob"),
    ("long_hex", "MEDIUM", r"(\\x[0-9a-fA-F]{2}){40,}|\b[0-9a-fA-F]{240,}\b", "long hex blob"),
    ("fetch_and_follow", "HIGH",
     r"(fetch|download|read|load|retrieve|get)\s+[^\n]{0,80}(instructions|rules|prompt|guidance)\s+"
     r"(from|at)\s+https?://", "tells the agent to fetch and follow remote instructions"),
    ("persistence_write", "HIGH",
     r"((?:^|\s)>>?\s*|\btee\b|\bcp\b|\bmv\b|\.write\(|\bappend|open\([^)]*['\"][wa]|crontab\s+-|systemctl\s+enable|launchctl\s+load)"
     r"[^\n]{0,80}(crontab|\.bashrc|\.zshrc|\.profile|authorized_keys|MEMORY\.md|USER\.md|SOUL\.md|AGENTS\.md|memories/|SKILL\.md|systemd)|"
     r"crontab\s+-|systemctl\s+enable|launchctl\s+load|"
     r"open\(\s*['\"][^'\"]*(\.bashrc|\.zshrc|\.profile|authorized_keys|MEMORY\.md|USER\.md|SOUL\.md|AGENTS\.md|memories/|SKILL\.md)[^'\"]*['\"]\s*,\s*['\"][wa]",
     "writes to persistence or agent memory"),
    ("privilege", "HIGH", r"chmod\s+(u?\+s|[0-7]?[4-7]755|[0-7]?777)|\bsetuid\(|chown\s+root", "privilege change"),
    ("sudo", "MEDIUM", r"(^|[;&|`$(]\s*|\s)sudo\s+\S", "runs a command as root"),
    ("unsafe_yaml_tag", "HIGH", r"!!python/(object|apply|name|module)|yaml\.load\((?![^)]*Loader\s*=\s*yaml\.SafeLoader)|\bpickle\.loads?\(",
     "unsafe deserialisation"),
    ("destructive", "HIGH", r"rm\s+-rf?\s+(/|~/?|\$HOME/?|/\*|~/\*)(\s|$|;|&)|\bmkfs\b|\bdd\s+if=[^\n]*of=/dev/|git\s+push\s+(-f\b|--force(?!-with-lease))",
     "destructive command"),
]
URL_RE = re.compile(r"https?://([A-Za-z0-9.-]+)")
UNPINNED = [
    (re.compile(r"^\s*([A-Za-z0-9_.\-\[\]]+)\s*(>=|>|~=|\*)?\s*$"), "requirements"),
]
NEGATION = re.compile(r"\b(never|do not|don't|must not|avoid|forbidden|no)\b[^\n]{0,40}$", re.I)


def _rel(p: Path, root: Path) -> str:
    return str(p.relative_to(root))


def scan(root: Path) -> dict:
    findings: list[dict] = []
    inventory: list[dict] = []
    doc_hosts: set[str] = set()
    code_hosts: dict[str, list[str]] = {}

    def add(rule, sev, path, line, note, excerpt=""):
        findings.append({"rule": rule, "severity": sev, "file": path, "line": line,
                         "note": note, "excerpt": excerpt[:160]})

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        d = Path(dirpath)
        for name in list(dirnames):
            p = d / name
            if name in SKIP_DIRS:
                add("vendored_or_vcs_dir", "LOW", _rel(p, root), 0,
                    f"{name}/ not scanned; packages should not ship it - inspect or rebuild from source")
                dirnames.remove(name)
                continue
            if p.is_symlink():
                add("symlink", "HIGH", _rel(p, root), 0, f"directory symlink -> {os.readlink(p)}")
                dirnames.remove(name)
            elif name == "__pycache__":
                add("shipped_bytecode", "HIGH", _rel(p, root), 0,
                    "compiled bytecode shipped; often skipped by scanners")
        for name in filenames:
            p = d / name
            rel = _rel(p, root)
            st = p.lstat()
            ext = p.suffix.lower()
            entry = {"file": rel, "bytes": st.st_size,
                     "executable": bool(st.st_mode & stat.S_IXUSR), "hidden": name.startswith(".")}
            inventory.append(entry)
            if stat.S_ISLNK(st.st_mode):
                add("symlink", "HIGH", rel, 0, f"file symlink -> {os.readlink(p)}")
                continue
            if name.startswith(".") and name not in {".gitignore", ".gitattributes"}:
                add("hidden_file", "MEDIUM", rel, 0, "hidden file: read it")
            if ext in BINARY_EXT:
                add("unanalysable_binary", "HIGH", rel, 0, "binary or bytecode: cannot be reviewed as text; fail closed")
                continue
            if ext in ARCHIVE_EXT:
                add("nested_archive", "HIGH", rel, 0, "archive inside the package: unpack in the sandbox and rescan")
                if ext == ".zip":
                    head = p.read_bytes()[:64]
                    if head[:4] == b"PK\x03\x04" and head[6] & 0x01:
                        add("encrypted_archive", "HIGH", rel, 0, "password-protected zip: unreadable, fail closed")
                continue
            low = rel.replace(os.sep, "/").lower()
            if (low.startswith((".claude/", ".cursor/", ".vscode/", ".github/hooks", "hooks/", ".husky/", ".git-hooks/"))
                    or low.endswith(("settings.json", ".envrc", "lefthook.yml", ".pre-commit-config.yaml"))):
                add("config_as_code", "MEDIUM", rel, 0, "config or hook file that can execute on clone/open/install: review as code")
            if st.st_size > MAX_BYTES:
                add("oversized_file", "MEDIUM", rel, 0, "file too large for full pre-scan; review manually")
                continue
            raw = p.read_bytes()
            if b"\x00" in raw[:8192]:
                add("unanalysable_binary", "HIGH", rel, 0, "binary content")
                continue
            if raw[:4] == b"\x7fELF" or raw[:2] == b"MZ":
                add("unanalysable_binary", "HIGH", rel, 0, "executable binary disguised by its extension")
                continue
            text = raw.decode("utf-8", errors="replace")
            if "evals/" in rel.replace(os.sep, "/") or rel.startswith(("eval/", "tests/fixtures")):
                entry["note"] = "eval/test data: some scanners skip it; scanned here"
            is_doc = ext in {".md", ".txt", ""} or name.upper().startswith(("SKILL", "README"))
            for ln, line in enumerate(text.splitlines(), 1):
                for kind, pred in INVISIBLE.items():
                    hits = [c for c in line if pred(c)]
                    if kind == "variation_selector" and hits and not re.search(
                            r"[\x21-\x7e][\ufe00-\ufe0e\U000e0100-\U000e01ef]|[\ufe00-\ufe0e\U000e0100-\U000e01ef]{2,}", line):
                        hits = []
                    if hits:
                        decoded = ""
                        if kind == "tag_block":
                            decoded = "".join(chr(ord(c) - 0xE0000) for c in hits if 0x20 <= ord(c) - 0xE0000 < 0x7F)
                        add(f"invisible_{kind}", "HIGH", rel, ln,
                            f"{len(hits)} invisible character(s)" + (f"; decodes to: {decoded!r}" if decoded else ""))
                for tok in re.findall(r"\w{3,}", line):
                    if re.search(r"[A-Za-z]", tok):
                        scripts = {unicodedata.name(c, "").split(" ")[0] for c in tok if c.isalpha() and ord(c) > 0x7F}
                        if scripts & {"CYRILLIC", "GREEK", "ARMENIAN"}:
                            add("mixed_script_identifier", "HIGH", rel, ln,
                                f"token {tok!r} mixes Latin with a look-alike script (homoglyph spoofing)", line)
                            break
                for rule, sev, rx, note in PATTERNS:
                    for m in re.finditer(rx, line, re.I):
                        prefix = line[: m.start()]
                        if rule == "registry_redirect":
                            hosts = {h.lower() for h in URL_RE.findall(line)}
                            if hosts and hosts <= OFFICIAL_HOSTS:
                                add(rule, "LOW", rel, ln, note + " (official host)", line)
                                break
                        if rule in {"sensitive_path", "network_send", "env_dump", "destructive"} and NEGATION.search(prefix):
                            add(rule, "INFO", rel, ln, note + " (inside a prohibition; confirm it is guidance, not action)", line)
                        else:
                            add(rule, sev, rel, ln, note, line)
                        break
                for host in URL_RE.findall(line):
                    host = host.lower().rstrip(".")
                    if is_doc:
                        doc_hosts.add(host)
                    else:
                        code_hosts.setdefault(host, []).append(f"{rel}:{ln}")
                if re.search(r"(^|/)(requirements[^/]*\.txt)$", rel) and line.strip() and not line.startswith(("#", "-")):
                    if "==" not in line and "@" not in line:
                        add("unpinned_dependency", "LOW", rel, ln, "dependency without an exact pin", line)
            if name == "package.json":
                try:
                    pj = json.loads(text)
                    for hook in ("preinstall", "install", "postinstall", "prepare"):
                        if hook in pj.get("scripts", {}):
                            add("install_hook", "HIGH", rel, 0, f"npm {hook} script runs on install: {pj['scripts'][hook]}")
                    for sect in ("dependencies", "devDependencies"):
                        for dep, ver in pj.get(sect, {}).items():
                            if isinstance(ver, str) and (ver[:1] in "^~*>" or ver in {"latest", ""} or ver.startswith(("http", "git"))):
                                add("unpinned_dependency", "LOW", rel, 0, f"{dep}@{ver} not exactly pinned")
                except ValueError:
                    add("malformed_manifest", "MEDIUM", rel, 0, "package.json does not parse")
            if name in {"setup.py"} and re.search(r"cmdclass|install\s*\(", text):
                add("install_hook", "HIGH", rel, 0, "setup.py customises install: code runs at install time")

    def covered(h: str) -> bool:
        return any(h == d or h.endswith("." + d) for d in doc_hosts)

    for host, where in sorted(code_hosts.items()):
        if not covered(host):
            add("undeclared_destination", "MEDIUM", where[0].split(":")[0], int(where[0].split(":")[1]),
                f"code references {host} which the docs never name ({len(where)} place(s))")

    has_skill = any(e["file"].upper().endswith("SKILL.MD") for e in inventory)
    sev_rank = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "INFO": 0}
    findings.sort(key=lambda f: (-sev_rank[f["severity"]], f["file"], f["line"]))
    return {
        "package": str(root),
        "files": len(inventory),
        "has_skill_md": has_skill,
        "doc_hosts": sorted(doc_hosts),
        "code_hosts": sorted(code_hosts),
        "counts": {s: sum(1 for f in findings if f["severity"] == s) for s in sev_rank},
        "findings": findings,
        "inventory": inventory,
        "reminder": "Leads, not a verdict. Confirm each finding in the file. A clean pre-scan does not mean safe.",
    }


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {"-h", "--help"}:
        print(__doc__)
        return 2
    root = Path(argv[0]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    report = scan(root)
    if "--json" in argv:
        print(json.dumps(report, indent=2))
    else:
        print(f"{report['package']}: {report['files']} files, SKILL.md={report['has_skill_md']}, counts={report['counts']}")
        for f in report["findings"]:
            print(f"[{f['severity']}] {f['rule']} {f['file']}:{f['line']} - {f['note']}")
        print(report["reminder"])
    return 1 if report["counts"]["HIGH"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
