---
name: "cross-language-semantics-traps"
description: "START HERE for any 'port/rewrite/translate this C, Python or JavaScript to Rust' task, before writing Rust: list every construct whose meaning changes in Rust (integer width and overflow, shifts, parsing, strings, Unicode, empty input, NULL) and cover each with a test case."
license: "MIT"
---

# Cross-language semantics traps

Step 4. The defects real ports ship are rarely algorithmic. They are integer widths and overflow, lenient parsers, string indexing units, Unicode rules and empty-input loops.

## Use when
- Reading the original before writing each function, and when a recorded case mismatches.

## DO NOT use when
- Designing the bridge (ffi-bridge-selection-and-boundaries) or ownership (borrow-and-ownership-translation).

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **Scan the original:** `scripts/trap_scan.py original.c` (or .py/.js). Read every listed line.
2. **For each trap, decide the Rust idiom and add a recorded case that exercises it:**
   - **Integer width and overflow:** match the C type width (long is 64-bit on LP64 Linux). C unsigned arithmetic wraps; Rust debug builds panic: use `wrapping_*` where C wraps. Shifts: widen BEFORE shifting (`u32::from(b) << 24`); a shift by the full width is UB in C and a panic in Rust: guard it, or use `rotate_left`.
   - **Division:** Python `//` and `%` floor toward negative infinity; Rust truncates toward zero. Python ints never overflow: use i128 or checked maths at the edges.
   - **Parsing:** C `atoi/strtol/scanf` and Python `int()` skip leading whitespace, accept signs, and C stops at the first bad character; Rust `str::parse` rejects all of that. Write the scanner the original implies. C `isspace` in the C locale is ASCII only.
   - **Strings:** C strings are bytes (maybe not UTF-8): use `&[u8]`. JS `length`/`indexOf`/`slice` count UTF-16 code units: use `encode_utf16`. Python `str.split()` also splits on `\x1c`-`\x1f`. Python `capitalize`/`title` use titlecase (`ß` -> `Ss`, `ǆ` -> `ǅ`). Python regex `\d` and `int()` accept every Unicode decimal digit.
   - **Formatting:** Python `str(float)` prints `1.0`, `1e+16`, `1e-05`, `inf`, `nan`; Rust `{}` prints `1`, `10000000000000000`, `0.00001`, `inf`, `NaN`.
   - **Empty and boundary input:** a do-while runs once on empty input; end markers are written even when there is no data; caps (e.g. run length 255) split long runs; NULL is not an empty slice (`Option<&[T]>`).
   - **Ordering:** hash map iteration and key order reaching output -> ordered map.
3. **Keep a trap table** in your notes: trap, line, Rust idiom, recorded case id.

## Tools
`scripts/trap_scan.py FILE...`: JSON list of trap sites with the reason and the Rust idiom. It lists places to read; it is not a verdict.

## Worked example
`trap_scan.py sum16.c` lists line 6 `sum += buf[i];` on a `uint16_t sum` (unsigned_wrap) and line 9 `return (sum << 3) | (sum >> 13);` (shift_by_variable: constant here, fine). The port uses `sum = sum.wrapping_add(u16::from(b))` and `sum.rotate_left(3)`. A recorded case of 600 bytes of `0xff`, which wraps the sum several times, passes in both debug and release builds; the first draft with `+=` panicked in debug only.

## Checklist
- [ ] trap_scan.py run on every original file
- [ ] Each trap has a Rust idiom and a recorded case
- [ ] Debug-build behaviour checked (overflow panics show only there)
- [ ] Trap table kept

## Output
The trap table and the extra recorded cases.

## Avoid
- `s.trim().parse().unwrap_or(0)` for a C or Python parser.
- `s.len()` or `chars().count()` for a JS length.
