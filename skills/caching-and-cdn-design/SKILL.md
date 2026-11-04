---
name: "caching-and-cdn-design"
description: "Design caches and CDNs that cut latency and load without becoming the outage: placement, keys, TTLs, invalidation, stampede control, cold starts and cache-failure behaviour."
license: "MIT"
---

# Caching and CDN design

## 1. Decide whether to cache
Cache when data is read far more than written, a dependency is slow or rate-limited, or users are far away. Write down what staleness is acceptable per data item; if none, do not cache it (or cache with strict invalidation).

## 2. Know which kind of cache you are building
- **Latency cache**: the system meets its load with an empty cache, just slower.
- **Capacity cache**: the backing store cannot survive without it. Then the cache is a critical dependency: replicate it, warm it, and plan the cold start (a deploy, a flush or a failover that empties it can take the backend down).

## 3. Placement and patterns
- Client and CDN for static and public content; set cache headers and versioned asset names.
- Application-local in-memory caches: fastest, but each instance warms separately and is inconsistent with the others.
- Shared external cache: one copy, but a network hop and a new dependency.
- Cache-aside (read-through on miss) is the default; write-through or write-behind only with a reason.

## 4. Keys, TTLs, eviction
- Key on everything that changes the result (tenant, locale, version, permissions).
- Set TTLs deliberately and revisit them with measured hit rate, size and downstream calls.
- Soft and hard TTLs: refresh after the soft TTL; keep serving the last good value until the hard TTL if the source is failing.
- Cache "not found" results briefly (negative caching).
- LRU or LFU eviction; size the cache from the hot set in the estimate.

## 5. Invalidation and consistency
Prefer short TTLs plus explicit invalidation on writes; update the store first, then delete the cache entry. Beware races that put stale data back; version values or use leases where it matters. Treat cached formats as persistent data: new code must read old entries.

## 6. Protecting the source
- Request coalescing (single flight) so one miss triggers one fetch.
- Jittered TTLs so keys do not expire together.
- On cache failure, do not stampede the source: limit concurrent fetches, shed, or serve stale.
- Ramp traffic slowly into cold caches.

## Output
Per cache: what, where, key, TTL (soft/hard), invalidation, size, expected hit rate, behaviour when the cache is down, metrics (hits, misses, evictions, downstream calls).

## Pitfalls
- Caching personalised or permissioned data under a shared key (data leak).
- A cache added for latency silently becoming a capacity cache as traffic grows.
- Untuned TTLs chosen once and never revisited.
