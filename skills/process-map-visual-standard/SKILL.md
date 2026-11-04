---
name: "process-map-visual-standard"
description: "Apply one visual standard to every process map: shape sizes, grid and spacing, lines and connectors, lanes, fonts, a small accessible colour palette, icons, legend and title blocks, enforced in Lucidchart and checked by script."
license: "MIT"
---

# Process map visual standard

Maps from different people, projects and tools should look like one family. The standard below is the house default; if the organisation already has a modelling standard, load its values into `templates/house-style.json` and keep the structure, so the checker still works.

The guiding rules: keep the notation's own meaning intact (BPMN fixes some styles), say everything with shape and text first, and use colour only as a declared, redundant extra.

## 1. What BPMN already fixes (never override)
- Sequence flow is solid, message flow dashed, association dotted. Do not reuse dashed or dotted for anything else, including shape borders.
- Intermediate events keep their double ring; throwing-event markers stay dark-filled.
- Everything else (fill, line colour, size, label position) is a style choice, so it must be standardised by us.

## 2. Shapes, sizes and grid
- One size per element type on every map: activity 110 x 80, event 36 x 36, gateway 50 x 50, data object 36 x 50, data store 50 x 50, annotation 160 wide. A bigger box reads as more important.
- Grid 10 px; snap everything. At least 40 px between shapes horizontally and 30 px vertically. Centre-align shapes on the happy path.
- Lanes: at least 120 px high, header on the left, all lanes the full pool width; at most 6 lanes per pool and 3 nesting levels; order lanes by first involvement so flow runs down and right.
- Collapsed sub-processes show the + marker and link to their child page.

## 3. Lines and connectors
- Orthogonal (elbow) lines only; no diagonals or curves.
- Flows leave shapes on the right or bottom and enter on the left or top, never against the reading direction.
- Line jumps on where crossings cannot be removed; first try reordering lanes or paths.
- Sequence flow 1 px dark grey, solid, filled arrowhead. Message flow per BPMN, at right angles to the sequence flow.
- Branch labels sit next to the gateway on the outgoing line; no labels on unconditional flows.

## 4. Text
- One sans-serif family (Lucid default Liberation Sans or the organisation's font).
- Activity 11 pt, event and gateway labels 10 pt, flow labels 10 pt, lane titles 12 pt, page title 18 pt, legend 10 pt; nothing below 9 pt. Set sizes explicitly, never auto-scale.
- Sentence case. No bold, italics, underline or manual line breaks inside element labels. Keep labels short: verb plus object, up to about five words.

## 5. Colour (monochrome first)
Base: black-ish text (#1A1A1A) on white, dark grey lines (#333333), light grey headers (#F2F2F2). A map must make complete sense in black and white.

Semantic markers, at most three per page, each with three redundant cues (border colour, 3 px border and a text tag), drawn from the colour-blind-safe Okabe-Ito family:
| Meaning | Border | Fill | Tag |
|---|---|---|---|
| Evidenced issue or pain point | #D55E00 vermillion | #FDE8DC | [ISSUE] + register id |
| Internal control | #0072B2 blue | #DCEBF7 | [CONTROL] |
| New or changed in to-be | #007A5A green | #D9F2EA | [CHANGE] |
| Happy path (optional) | normal | #FFF4D6 weak tint | none; legend entry |

- Colour is never the only cue (WCAG 1.4.1): every coloured shape carries its tag in the label or in a linked annotation.
- Text contrast at least 4.5:1 against its fill; borders, lines and icons at least 3:1 (WCAG 1.4.3, 1.4.11). All palette pairs above pass.
- Never colour by department, lane or personal taste. Colour that encodes nothing makes readers hunt for a meaning. Tinting sub-process regions did not help comprehension in studies, and colour preferences differ by culture.
- Highlighting matching gateway pairs can help novice readers in training material; keep it out of published maps.

## 6. Icons
- BPMN maps: only BPMN's own markers (task types, event triggers, sub-process and loop markers).
- Other maps: an optional set of at most 6 icons (for example system, document, customer, decision rule, manual work, external party). Each icon is in the legend, 16 px, top-left of the shape and always paired with text. No decorative icons or clip art.
- Test new icons with real readers; icon meanings that are not tested get misread.
- Lucid conditional formatting can add icons from shape data; use it only for meanings in the legend.

## 7. Page furniture (every page)
- **Title block**: `L3 2.3 Approve supplier invoices | As-is | v0.2 | Draft | Owner: AP lead | 04/11/2026` (level, number, name, as-is/to-be, version, status, owner, date).
- **Breadcrumb**: `Parent: L2 2 Procure to pay`, linked back to the parent page (not needed on L1).
- **Legend**: every symbol, colour, icon and line style used beyond the basics, and the lane convention.
- Page: landscape; A4 for L1/L2, A3 for L3/L4; fixed page size, never an infinite canvas. Fit the map on one page or screen; wrap or split rather than scroll.

## 8. Size limits
- Aim for 9 to 15 activities per page; split above that.
- Never more than 50 flow elements on a page.
- Use at most 3 semantic colours and at most 6 icons per page.

## 9. Enforce it
- Lucid: build maps from the master template (`templates/process-map-template.lucid`, three linked pages: L1 landscape, L2 stage chain, L3 swimlane with issue and control markers), keep styled shapes in a shared custom shape library, and use conditional formatting and layers as described in `lucidchart-diagram-delivery`. Theme edits alone stay inside one document.
- Check every generated Lucid file before import: `python3 scripts/check_visual_standard.py map.lucid [--style house-style.json]`. Errors cover palette, contrast, colour-only meaning, reserved dashed or dotted styles, line shape and style per connection, mixed sizes, lane widths, missing title, legend or breadcrumb, dangling lines, duplicate ids and the 50-element limit. Warnings cover auto-scaled fonts, formatting in labels, more than 15 activities, unlabelled branches and off-standard sizes.
- BPMN files: `check_bpmn.py` (in `bpmn-xml-authoring-and-validation`) flags mixed sizes per element type.
- Neither check sees a rendered page. Open the imported map, look at it, and print it once in black and white.
