#!/usr/bin/env python3
"""List the constructs in an original C, Python or JavaScript file whose meaning changes
when written the "obvious" way in Rust.

  trap_scan.py FILE [FILE...]        language from the extension (.c .h .py .js .mjs .ts)
Prints JSON: [{"file", "line", "trap", "code", "rust"}]. Each entry is a place to read and
to cover with a recorded edge case; it is not a bug report. Exit 0 always (2 on unreadable input).
"""
import json, re, sys
from pathlib import Path

RULES = {
    "c": [
        ("unsigned_wrap", r"\b(uint\d+_t|unsigned)\b[^;]*[*+-]=|\bh\s*\*=", "C unsigned arithmetic wraps; Rust debug builds panic on overflow", "wrapping_mul/wrapping_add (or Wrapping<T>)"),
        ("narrow_shift", r"\(\s*(uint8_t|uint16_t|char|unsigned char)\s*\)[^;]*<<|\b\w+\[\w+\]\s*<<", "integer promotion: C widens before shifting; a Rust u8 shifted by 8+ overflows", "cast to the wide type BEFORE shifting (u32::from(b) << 24) or from_be_bytes"),
        ("shift_by_variable", r"<<\s*\(?\s*[a-z_]\w*|>>\s*\(?\s*\(?\s*\d+\s*-\s*\w+", "shift amount may reach the type width: UB/masked in C, panic in Rust debug", "checked_shl/rotate_left or explicit width guard"),
        ("libc_parse", r"\b(atoi|atol|strtol|strtoul|strtod|sscanf|scanf)\s*\(", "C parsers skip leading whitespace, accept trailing junk, stop at first bad char; str::parse rejects all of these", "hand-written byte scanner matching the C rules"),
        ("ctype", r"\b(isspace|isalpha|isdigit|isalnum|toupper|tolower)\s*\(", "C ctype is ASCII in the C locale; Rust char::is_whitespace/is_alphanumeric are Unicode", "u8::is_ascii_* on bytes"),
        ("c_string", r"\bconst\s+char\s*\*|\bchar\s*\*", "C strings are bytes, may be non-UTF-8 and NUL-terminated", "&[u8] / CStr, not &str"),
        ("null_vs_empty", r"\bNULL\b", "NULL and empty are different C values; a Rust slice cannot express NULL", "Option<&[T]>"),
        ("loop_on_empty", r"\bdo\s*\{", "a do-while runs once even on empty input", "explicit first iteration; record the empty input"),
        ("int_width", r"\b(long|size_t|int64_t|uint64_t|int)\b\s+\w+\s*\(", "return/argument width: long is 64-bit on LP64 Linux, int is 32-bit", "match the C type width exactly (i64/u64/i32)"),
    ],
    "python": [
        ("floor_div_mod", r"//|%|\bdivmod\s*\(", "Python // and % floor toward -inf; Rust / and % truncate toward 0; Python ints never overflow", "div_euclid/rem_euclid adjusted for negative divisors, or i128; record negative operands"),
        ("str_split", r"\.split\(\s*\)", "str.split() splits on Unicode whitespace incl. \\x1c-\\x1f and drops empties", "custom predicate: char::is_whitespace || '\\x1c'..='\\x1f'"),
        ("case_mapping", r"\.(capitalize|title|upper|lower|casefold|swapcase)\(", "Python case mapping uses titlecase and special cases (ß -> Ss, ligatures)", "explicit titlecase handling; record non-ASCII words"),
        ("float_str", r"\bstr\s*\(|\brepr\s*\(|f\"[^\"]*\{[^}]*\}", "Python float str: '1.0', 'inf', 'nan', exponent below 1e-4 and from 1e16 ('1e+16')", "format shortest digits, then apply Python's exponent rules"),
        ("unicode_digits", r"\\d|\.isdigit\(|\.isdecimal\(|\bint\s*\(", "re \\d and int() accept all Unicode decimal digits ('\\u0661' == 1)", "char::to_digit is ASCII-only: map Unicode Nd digits explicitly"),
        ("regex_fullmatch", r"\b(re\.(match|search|fullmatch)|\.fullmatch\(|\.match\()", "match anchors at start only; $ matches before a final newline; fullmatch anchors both", "anchor exactly as the original; record a trailing-newline input"),
        ("exceptions", r"\braise\b", "each raise is an error path the port must return as Err, never panic", "Result<_, String> with the exception type name"),
        ("int_unbounded", r"\bint\b", "Python int has no overflow", "i128 or checked arithmetic at the boundaries"),
    ],
    "js": [
        ("utf16_length", r"\.length\b", "JS string length counts UTF-16 code units; Rust len() counts UTF-8 bytes", "s.encode_utf16().count()"),
        ("utf16_index", r"\.(indexOf|lastIndexOf|slice|substring|substr|charAt|charCodeAt|at)\(", "JS indices are UTF-16 code units and slice can split surrogate pairs", "convert byte offsets to UTF-16 offsets; record emoji and combining marks"),
        ("number_f64", r"\b(parseInt|parseFloat|Number|Math\.\w+)\(", "JS numbers are f64; parseInt stops at junk; -0 and NaN exist", "f64 semantics and a lenient parser"),
        ("string_compare", r"[<>]=?\s*['\"]|localeCompare", "JS < compares UTF-16 code units, not code points", "compare encode_utf16 sequences"),
        ("object_order", r"Object\.(keys|entries|values)|for\s*\(\s*const\s+\w+\s+in\b", "JS object key order is insertion order (integer-like keys first)", "indexmap / ordered map"),
    ],
}
EXT = {".c": "c", ".h": "c", ".py": "python", ".js": "js", ".mjs": "js", ".ts": "js"}


def scan(path: Path):
    lang = EXT.get(path.suffix)
    if not lang:
        return []
    out = []
    for n, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        code = line.strip()
        if not code or code.startswith(("#", "//")) and lang != "c":
            continue
        for trap, pat, why, rust in RULES[lang]:
            if re.search(pat, line):
                out.append({"file": str(path), "line": n, "trap": trap, "code": code[:160], "why": why, "rust": rust})
    return out


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print(__doc__); return 2
    res = []
    for a in argv:
        p = Path(a)
        if not p.is_file():
            print(f"cannot read {a}", file=sys.stderr); return 2
        res += scan(p)
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
