---
name: "frontend-architecture"
description: "Structure frontend code: state ownership, data fetching, and component boundaries."
license: "MIT"
---

# Frontend Architecture

Decide where state lives and how data flows before writing components.

## 1. Own state at the right level
- Local state for local concerns; lift only when two siblings must agree.
- Server state (fetched) is not UI state: cache it, revalidate it, don't copy it into local state.
- Global store only for genuinely cross-cutting state (auth, theme); most state is not global.

## 2. Data fetching is a contract
- Fetch at the boundary that owns the data; pass down, don't re-fetch in leaves.
- Model loading, empty, error and success as explicit states, never just "no data yet".
- Colocate the query with the component that needs it; avoid waterfall fetches.

## 3. Component boundaries by responsibility
- Split by responsibility and reuse, not by line count.
- Container (data/logic) vs presentational (props in, markup out) keeps testability high.
- Props are an API: minimal, typed, no leaking internal shape.

## Voice
Structure-first. Refuse "just add another useState" when the real fix is moving state ownership.
