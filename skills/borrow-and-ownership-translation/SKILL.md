---
name: "borrow-and-ownership-translation"
description: "Use when porting code with shared, mutable or pointer-linked data to Rust, or when fighting the borrow checker: map who owns, who borrows and what mutates, without unsafe shortcuts or needless cloning."
license: "MIT"
---

# Borrow and ownership translation

Step 5. Garbage-collected and pointer-based code hides ownership. Writing it down first avoids clone-everything ports and unsafe shortcuts.

## Use when
- Translating functions that share, mutate or store data; designing structs for state the original kept.

## DO NOT use when
- The function is pure on plain values (most leaf ports): skip with a note.

Follow the persona hard rules: read the original and every given file before writing Rust; the original is the oracle; record its behaviour before porting; a mismatch is fixed in the port, never in the recording; return Err where the original fails, never panic; no network, std only unless the plan names a crate.

## Procedure
1. **For each value, record owner, borrowers and mutators** in the original: who creates it, who reads it, who changes it, how long it lives.
2. **Map the pattern:**
   - read-only parameter -> `&T` / `&str` / `&[T]`;
   - mutated in place -> `&mut T` (one mutator at a time);
   - stored beyond the call -> owned `T` moved in, or `Rc<T>`/`Arc<T>` when genuinely shared;
   - shared and mutated -> restructure first (pass `&mut` down, return new values); `RefCell`/`Mutex` only when restructuring is impossible, and say why;
   - graphs and back-references -> indices into a `Vec` (arena), not reference cycles;
   - C out-parameters -> return values (tuple or struct); C pointer + length -> slice; returned pointer into an argument -> offset.
3. **Functions that mutate their arguments:** keep the same observable result; record the mutated argument as an output in the equivalence cases.
4. **No `unsafe` for convenience.** If truly needed (FFI), isolate it with a `// SAFETY:` comment stating the invariant, and run the tests under Miri (`cargo +nightly miri test`) when available.
5. **Clone only with a reason** written next to it (cheap type, or ownership genuinely split).

## Worked example
A JS `Cache` stores entries in a Map and hands out entry objects that callers mutate (`entry.hits++`). Rust: `Cache { entries: Vec<Entry>, index: HashMap<String, usize> }`; `get_mut(&mut self, key) -> Option<&mut Entry>`; callers increment through the `&mut`. No `Rc<RefCell<_>>` needed. The equivalence cases record `hits` after each call sequence.

## Checklist
- [ ] Owner/borrower/mutator table for shared values
- [ ] Each pattern mapped to a Rust form
- [ ] Mutated arguments recorded as outputs
- [ ] No unsafe without SAFETY note (and Miri where available)
- [ ] Each clone justified

## Output
The ownership table and the struct/function signatures that follow from it.

## Avoid
- `Rc<RefCell<T>>` everywhere to make it compile.
- `.clone()` to silence the borrow checker without a reason.
