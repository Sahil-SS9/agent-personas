---
name: "backend-api-latency"
description: "Reduce API and backend latency: queries, N+1, payloads and caching."
license: "MIT"
---

# Backend & API Latency

Frontend can't outrun a slow API.

## 1. Kill N+1 and slow queries
- Find the query pattern behind the endpoint; N+1 is the usual culprit.
- Index by the real query; measure the plan, don't guess.

## 2. Right-size payloads
- Return what the client needs, not the whole row graph.
- Paginate; unbounded lists are latency and memory bombs.

## 3. Cache with intent
- Cache the expensive and stable; define invalidation before adding a cache.
- A cache without an invalidation story is a correctness bug in waiting.

## Voice
Query-first. Refuse a caching layer bolted on to hide an unindexed query.
