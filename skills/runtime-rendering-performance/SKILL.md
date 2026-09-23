---
name: "runtime-rendering-performance"
description: "Fix runtime performance: rendering, main-thread work, and memory."
license: "MIT"
---

# Runtime & Rendering Performance

Load speed is half the story; runtime jank is the other half.

## 1. Protect the main thread
- Long tasks block input; break work up, defer, or move to a worker.
- Measure INP and long-tasks, not just load metrics.

## 2. Render only what changed
- Avoid needless re-renders; memoise the expensive, not everything.
- Virtualise long lists; don't mount thousands of nodes.

## 3. Watch memory
- Leaks come from unremoved listeners, timers and retained closures.
- Profile heap over a session, not a single snapshot.

## Voice
Main-thread-first. Refuse "add more memoisation everywhere" without a profile.
