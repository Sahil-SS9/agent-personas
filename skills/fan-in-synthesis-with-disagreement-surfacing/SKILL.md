---
name: "fan-in-synthesis-with-disagreement-surfacing"
description: "Use when merging results from several agents or workers: find conflicts, weigh them on evidence, cover every facet and report disagreements instead of silently picking one answer."
license: "MIT"
---

# Fan-in synthesis with disagreement surfacing

Step 8. Merging is where contradictions disappear. Surface them; resolve them on evidence.

## Use when
- Combining outputs from two or more workers into one answer.

## DO NOT use when
- A single worker's output is the answer (verify it instead).

Follow the persona hard rules: read the goal, roster, limits, policy and every given file first; plan before dispatching; every worker gets a fresh, complete brief; a worker's own "done" is not done; never exceed the agent budget or a worker's context; record every decision.

## Procedure
1. **Lay out claims side by side** per facet of the brief: value, worker, source, source date and type.
2. **Find conflicts:** different values for the same facet.
3. **Resolve on evidence:** prefer primary sources over secondary, newer over older for things that change, and agreement between independent sources. State the rule used. If evidence cannot resolve it, report the conflict as open.
4. **Check coverage:** every facet the brief asked for has at least one supported answer; list unaddressed facets and re-dispatch for them.
5. **Write the merged answer** with the resolution notes and any open conflicts; never present one worker's value as the answer while hiding a contradicting one.

## Worked example
Brief: library X's licence and latest version. W1: MIT, v4.2 (repo LICENSE file, release page this month). W2: Apache-2.0, v3.9 (a 2023 blog). W3: v4.2, licence not covered. Conflict on licence; resolve to MIT (primary file, current) and note W2's claim as outdated. Version agreed by W1 and W3. All facets covered.

## Checklist
- [ ] Claims laid out per facet with sources and dates
- [ ] Conflicts listed
- [ ] Resolution rule stated, or conflict left open
- [ ] Unaddressed facets listed and re-dispatched
- [ ] Merged answer carries the resolution notes

## Output
The merged answer with conflicts, resolutions and coverage.

## Avoid
- Averaging or silently choosing between contradicting values.
