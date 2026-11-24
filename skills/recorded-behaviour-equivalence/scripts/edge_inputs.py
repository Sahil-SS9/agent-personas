#!/usr/bin/env python3
"""Generate edge-case inputs for recording an original's behaviour, by parameter type.

  edge_inputs.py TYPE [TYPE...] [--max N]
TYPE: i8 i16 i32 i64 u8 u16 u32 u64 int (unbounded, Python) f64 str bytes bool
Prints one JSON array of argument lists (the cartesian product, capped at --max, default 200).
The lists are a start: add real-world inputs and every input the original's own tests use.
"""
import itertools, json, sys

def ints(bits, signed):
    lo, hi = (-(1 << (bits - 1)), (1 << (bits - 1)) - 1) if signed else (0, (1 << bits) - 1)
    v = {lo, lo + 1, -1, 0, 1, 2, hi - 1, hi, 7, 8, 31, 32, 33, 63, 64, 65, 255, 256}
    v |= {1 << k for k in (7, 8, 15, 16, 31, 32, 62, 63) if (1 << k) <= hi}
    return sorted(x for x in v if lo <= x <= hi)

STR = ["", " ", "a", "  lead and trail  ", "multiple   spaces", "tab\tnew\nline", "\x0b\x0c", "\x1cfs\x1dgs",
       "\u00a0nbsp", "\u2003em space", "ß straße", "İstanbul", "ǆ", "ﬁ ligature", "e\u0301 combining", "😀", "a😀b",
       "👍🏽", "中文", "\u0661\u0662 arabic digits", "١h", "-0", "+7", " 12", "12abc", "3.14", "1_000", "1e3",
       "NaN", "inf", "\\", "\"quoted\"", "x" * 300]
BYTES = [b"", b"\x00", b"\x00\x00\x01", b"\xff", b"\x80", b"\xc3\x28", b"a" * 255, b"a" * 256, b"a" * 300, bytes(range(256))]
F64 = [0.0, -0.0, 1.0, -1.5, 0.1 + 0.2, 1e-5, 1e-4, 1e15, 1e16, 1e22, 5e-324, 1.7976931348623157e308,
       float("inf"), float("-inf"), float("nan"), 2.5, 0.5, 123456789012345.6]

def values(t):
    if t in ("i8", "i16", "i32", "i64"): return ints(int(t[1:]), True)
    if t in ("u8", "u16", "u32", "u64"): return ints(int(t[1:]), False)
    if t == "int": return ints(64, True) + [-(1 << 70), 1 << 70]
    if t == "f64": return [repr(x) if x != x or x in (float("inf"), float("-inf")) else x for x in F64]
    if t == "str": return STR
    if t == "bytes": return [b.hex() for b in BYTES]
    if t == "bool": return [False, True]
    raise SystemExit(f"unknown type {t}")

def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    cap = 200
    if "--max" in argv:
        i = argv.index("--max"); cap = int(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
    if not argv:
        print(__doc__); return 2
    combos = list(itertools.islice(itertools.product(*(values(t) for t in argv)), cap))
    print(json.dumps([list(c) for c in combos], ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
