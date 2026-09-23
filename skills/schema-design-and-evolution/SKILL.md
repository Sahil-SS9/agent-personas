---
name: "schema-design-and-evolution"
description: "Design schemas from access patterns; evolve them without breaking consumers."
license: "MIT"
---

# Schema design and evolution

## When to use
Designing tables/models or changing existing ones.

## Procedure
1. State the access patterns first: the questions this data must answer and their frequency. Schema follows access, not aesthetics.
2. Model the grain explicitly: one row = one what? Document it; grain violations are the root of most modelling pain.
3. For analytics: dimensional modelling (facts/dimensions, star schemas); for transactional: normalise to protect integrity; denormalise only with measured read justification.
4. Document columns: meaning, units, nullability, source. Undocumented schema is undocumented system.
5. Evolve additively: nullable columns, new tables; expand → migrate → contract for renames/restructures; consumers never break between deploys.

## Decision rules
- Every index costs write throughput: each must be justified by a measured query.
- Backward compatibility is a property: old readers keep working across the change.
- Test migrations on production-shaped data, with a tested rollback.

## Pitfalls
- EAV/JSON-blob schemas hiding structure that queries need.
- Grain drift as requirements creep (mixing daily and event rows).

## Done
Documented, grain-explicit schemas evolved compatibly with tested migrations.