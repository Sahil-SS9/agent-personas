---
name: "process-map-validation-and-signoff"
description: "Prove process maps before sign-off: trace every element to evidence, run structural and cross-level consistency checks, walk paths with the people who do the work, and record versions, approvals and open questions."
license: "MIT"
---

# Process map validation and sign-off

A map is draft until the people who do the work recognise it and an owner accepts it. Validation has three layers: evidence, structure and people.

## 1. Evidence traceability
- Each element (activity, decision, event, lane, rule annotation) lists one or more fact ids, or is marked `assumed` or `inferred` with the reason.
- Report the assumed share per map. If more than about a fifth of a map's elements are assumed, it is not ready for walkthrough; go back to elicitation.
- Each conflict from the register is either resolved, with a source, or shown as an open question on the map.

## 1b. Three kinds of quality
- **Syntactic**: the map follows the notation (no dead ends, deadlocks or orphans). Checked by tools.
- **Semantic**: the map is true and complete. Checked with the people who do the work.
- **Pragmatic**: readers understand it. Checked by layout, labels and the visual standard, and by asking a reader to explain the map back.
A map passing only the first is not validated.

## 2. Structural checks per map
- BPMN files: the full validation ladder in `bpmn-xml-authoring-and-validation`.
- Any notation: one clear start; a named terminator per end state; every decision has labelled exits; no dead ends or orphans; every handoff has a receiver; every lane has at least one step; names are verb plus object; the legend is present.

## 3. Cross-level consistency
- Every L(n+1) map names its parent, and the parent element links to it.
- The child's trigger and end states match the parent element's inputs and the outcomes its next decision tests.
- Roles in L3 lanes exist in the actor list; L4 steps are performed by the lane that owns the parent L3 activity, or the handoff is shown.
- Numbering and names are identical across the register, map titles and links.
- No L2 stage silently missing an L3 when the coverage matrix said it was supported.

## 3b. Readability review
- Run the 7PMG review: few elements, low connector counts, structured blocks, few start and end events, no OR, verb-object labels, decompose past 50 elements. At equal size, dense and highly connected maps are harder to read; simplify those first.
- Run the style checks (`check_bpmn.py`, `check_visual_standard.py`) and clear or justify every warning.
- Readers who know the notation understand maps better than experienced readers who do not, so give business reviewers the legend and a one-page notation primer before the walkthrough.

## 4. Walkthrough with the people who do the work
- Walk each path end to end, one token at a time: the happy path, then each exception. Ask "what happens next, who does it, and what do they need?"
- Use the gap questions from elicitation. Capture each correction as a new fact, with source `validation session <date>, <role>`.
- Separate "this is wrong" (fix it) from "this should be different" (an opportunity for the to-be).
- Walk with practitioners as well as managers; their versions differ, and both matter.

## 5. Versioning and sign-off record
- Each map carries a version, date, status (draft / validated / approved / superseded), owner and as-is or to-be.
- Change log: what changed, why, and the fact ids.
- Sign-off record: who approved which maps and scope, on what date, and with which open questions accepted.
- Keep the open-question list with the maps, not in someone's inbox.

## Done when
The maps, the hierarchy register, the fact ledger, the conflict and open-question lists and the sign-off record are consistent with each other. Every check that was run is reported, and so is every check that was not run, with the reason.
