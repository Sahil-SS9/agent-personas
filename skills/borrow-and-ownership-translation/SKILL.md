---
name: "borrow-and-ownership-translation"
description: "Turn garbage-collected idioms into ownership designs: lifetimes over clones, Send/Sync decided deliberately, async mapped to the Rust model."
license: "MIT"
---
# Borrow and Ownership Translation

## Use when
- Translating code from a GC or scripting language into Rust.
- The borrow checker is fighting a structure that was natural in the
  original.
- Async, shared state or callback-heavy code is crossing the port.

## Instructions

1. Redesign for ownership, don't transliterate: in the original everything
   was shared; in the port decide who owns each value. Borrowing beats
   cloning; clones are chosen, not defaulted to.
2. Shared mutable state from the original (globals, long-lived caches,
  cross-object mutation) becomes an explicit choice: message passing, or an
  interior-mutability container — with the reasoning stated at the site.
3. Decide Send/Sync deliberately: a value crossing a thread boundary in the
  original (thread pools, background workers) must be Send in the port; a
  value that must not cross gets its boundary enforced by the type, not a
  comment.
4. Map async honestly: callback and promise idioms translate to Rust async
  only where the underlying work is actually concurrent; where the original
  was sequential with a callback sugar, a synchronous port is simpler and
  faster — say which and why.
5. Error handling translates, not disappears: the original's exception
  surface becomes a Rust error type with the same variants; a port that
  turns exceptions into panics changed the behaviour.
6. Cycles from reference-heavy originals get broken with ids or arena
  structures; Arc cycles leak, and "it compiles" is not a memory model.

## Stop conditions
- Never silence the borrow checker with clone loops or unsafe.
- Never let a panic path exist where the original returned an error.
- Never leave a Send decision implicit.

## Escalation
- Structures that cannot be expressed safely (self-referential originals,
  host-callback lifetimes) escalate: keep that unit behind the bridge, or
  restructure the host side — owner decides with the options priced.
