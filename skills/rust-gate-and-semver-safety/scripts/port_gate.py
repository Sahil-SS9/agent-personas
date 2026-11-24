#!/usr/bin/env python3
"""Done-means-gate for a ported Rust crate. Runs from the crate directory (or pass it).

  port_gate.py [CRATE_DIR] [--offline] [--no-clippy]
Checks (each PASS/FAIL with a fix):
  build        cargo build succeeds
  fmt          cargo fmt --check
  clippy       cargo clippy -- -D warnings, plus porting lints: cast_possible_truncation,
               cast_sign_loss, cast_possible_wrap, arithmetic_side_effects (warn -> error)
  tests_exist  at least one #[test] in src/ or tests/ (passing with zero tests proves nothing)
  tests        cargo test passes
  no_stubs     no todo!/unimplemented!
  err_not_panic  no unwrap()/expect()/panic! inside a function that returns Result (or an // INFALLIBLE: note)
  unsafe_documented  every `unsafe` has a // SAFETY: comment on the line above
Exit 0 only if every check passes. Recorded-behaviour equivalence is checked separately (diff step).
"""
import re, subprocess, sys
from pathlib import Path

PORT_LINTS = ["-D", "warnings", "-D", "clippy::cast_possible_truncation", "-D", "clippy::cast_sign_loss",
              "-D", "clippy::cast_possible_wrap", "-D", "clippy::arithmetic_side_effects"]


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr)[-1200:]


def rust_files(crate: Path):
    return [p for d in ("src", "tests") for p in (crate / d).rglob("*.rs")] if crate.exists() else []


def static_checks(crate: Path):
    res = {}
    src = {p: p.read_text(errors="replace") for p in rust_files(crate)}
    res["tests_exist"] = (any("#[test]" in t for t in src.values()), "add #[test] functions for the edge cases you reasoned about")
    stubs = [f"{p.name}:{i}" for p, t in src.items() for i, l in enumerate(t.splitlines(), 1) if re.search(r"\b(todo|unimplemented)!", l)]
    res["no_stubs"] = (not stubs, f"replace stubs: {stubs[:5]}")
    bad = []
    for p, t in src.items():
        if "/tests/" in str(p):
            continue
        for m in re.finditer(r"fn\s+\w+[^{;]*->\s*Result<[^{]*\{", t):
            body, depth, i = "", 1, m.end()
            while i < len(t) and depth:
                depth += {"{": 1, "}": -1}.get(t[i], 0); body += t[i]; i += 1
            for l in body.splitlines():
                if re.search(r"\.unwrap\(\)|\.expect\(|panic!\(", l) and "INFALLIBLE:" not in l and "#[test]" not in body:
                    bad.append(f"{p.name}: {l.strip()[:80]}")
    res["err_not_panic"] = (not bad, f"return Err instead of panicking: {bad[:3]}")
    undoc = []
    for p, t in src.items():
        lines = t.splitlines()
        for i, l in enumerate(lines):
            if re.search(r"\bunsafe\s*(\{|fn|impl)", l) and not (i and "SAFETY:" in lines[i - 1]) and "SAFETY:" not in l:
                undoc.append(f"{p.name}:{i + 1}")
    res["unsafe_documented"] = (not undoc, f"add // SAFETY: above {undoc[:5]}")
    return res


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    flags = [a for a in argv if a.startswith("--")]
    args = [a for a in argv if not a.startswith("--")]
    crate = Path(args[0] if args else ".").resolve()
    if not (crate / "Cargo.toml").exists():
        print(f"no Cargo.toml in {crate}"); return 2
    off = ["--offline"] if "--offline" in flags else []
    results = {}
    results["build"] = run(["cargo", "build", "-q", *off], crate) + ("fix the compile errors",)
    results["fmt"] = run(["cargo", "fmt", "--check"], crate) + ("run cargo fmt",)
    if "--no-clippy" not in flags:
        results["clippy"] = run(["cargo", "clippy", "-q", *off, "--all-targets", "--", *PORT_LINTS], crate) + ("fix lints; silence only with #[expect(lint, reason = \"...\")]",)
    results["tests"] = run(["cargo", "test", "-q", *off], crate) + ("make the tests pass",)
    for k, (ok, fix) in static_checks(crate).items():
        results[k] = (ok, "", fix)
    allok = True
    for k, (ok, out, fix) in results.items():
        allok &= ok
        print(f"{'PASS' if ok else 'FAIL'} {k}" + ("" if ok else f"  -> {fix}"))
        if not ok and out:
            print("   " + out.strip().splitlines()[-1][:200])
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
