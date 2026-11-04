---
name: "lucidchart-diagram-delivery"
description: "Get process maps into Lucidchart by the right route: BPMN file import, CSV process-diagram import, Standard Import JSON via the API, or a connected Lucid integration. Includes page structure for L1 to L4 and drill-down links."
license: "MIT"
---

# Lucidchart diagram delivery

Lucidchart is where many business stakeholders review process maps. Pick the import route by what the map needs. Never upload, create or share a document without the user's authorisation, and never write API tokens into files.

## 1. Choose the route
| Need | Route | Fidelity |
|---|---|---|
| BPMN map, editable in Lucid | Validated `.bpmn` file, then New > Import documents | BPMN 2.0 content only; styling dropped |
| Simple flowchart or swimlane (L2/L3, not BPMN), fast | CSV process-diagram import (Lucid marks it experimental) | Auto-layout; no styling; horizontal swimlanes only |
| Full control: layout, styling, multi-page L1 to L4, drill-down links, custom data | Standard Import `.lucid` file via the REST API | Highest; needs the user's API access |
| The user has connected the Lucid MCP server or uses Lucid AI | Let that integration create or edit; you supply the content | Still validate the content and read it back |
| Diagram exists only as an image | Lucid AI can rebuild an uploaded PNG or JPEG as shapes; check every label afterwards | Variable |

Draw.io import only accepts files exported from draw.io itself. Hand-generated draw.io XML may be refused, so do not promise it.

## 2. CSV process-diagram import
Required columns: `ID`, `Name`, `Shape Library`, `Page ID`, `Contained By`, `Text Area 1`. Optional: `Line Source`, `Line Destination`, `Source Arrow`, `Destination Arrow`, `Text Area 2`...
- One row per page, shape and line. Ids are unique; numbering from 1 works.
- `Name` is the object type: `Page`, `Line`, or a supported shape from the `Flowchart Shapes` library: Swim Lane, Process, Decision, Terminator, Document, Preparation, Data (I/O), Database, Delay, Connector, Or, Display, Note. Spelling and capitals must match exactly.
- `Contained By` places a shape in a lane as `<swimlaneId>:<laneNumber>` (for example `2:1`).
- Lines: `Line Source`/`Line Destination` hold shape ids; arrows are None, Arrow, Open Arrow or Hollow Arrow. Decision branch labels go in the line's `Text Area 1`.
- Expect overlaps on complex maps. Keep each CSV to one L3 page and tidy it on the canvas.

## 3. Standard Import (`.lucid`)
- A ZIP named `*.lucid` containing `document.json` (2 MB limit), with optional `/data` CSVs (1 MB) and `/images` (50 MB total ZIP).
- `document.json`: `{"version": 1, "pages": [{"id", "title", "shapes", "lines", "groups", "layers"}]}`. Every item needs a unique `id`; shapes need `type` and `boundingBox {x, y, w, h}`.
- BPMN shapes: `bpmnPool` (`title`, `lanes[{title, width, laneFill}]`, lane widths summing to the pool size, `vertical`), `bpmnActivity` (`activityType` task / transaction / eventSubProcess / callActivity; `taskType` none, user, service, manual, send, receive, businessRule, script; markers such as subProcess and loop), `bpmnEvent` (`eventGroup` start / intermediate / end; `eventType` none, message, timer, error, escalation, signal, terminate...), `bpmnGateway` (`gatewayType` exclusive, parallel, inclusive, eventBased...), `bpmnDataObject`, `bpmnDataStore`, `bpmnTextAnnotation`, `bpmnGroup`, `bpmnBlackBoxPool`.
- Non-BPMN maps: the flowchart library, plus `swimLanes` from the container library (`vertical`, `titleBar`, `lanes`).
- Lines: `lineType` elbow is best for process maps. `endpoint1`/`endpoint2` are `shapeEndpoint`s with `shapeId` and `style` (none / arrow). Labels go in `text[{text, position, side}]`.
- Drill-down: give an L2 or L3 shape an `actions` entry `{"type": "gotoPage", "pageId": "<child page>"}`. Use `customData` for fact ids, owner and status.
- Create it with `POST https://api.lucid.co/v1/documents` (multipart: `file` typed `x-application/vnd.lucid.standardImport`, `title`, `product=lucidchart`), using the user's OAuth token. Lucid notes that the same file can render differently over time, so open the result and check it.
- Check the current developer docs for exact property names before a large generation. The format evolves.

## 3b. Make the house style stick in Lucid
Lucid styles are easy to drift. Theme edits are saved per document only, so they do not standardise a team. Instead:
- Keep one **master template document** built from `process-map-visual-standard` (title block, legend, breadcrumb, lane set-up, styled shapes) and create every map from it.
- Put the styled shapes in a shared **custom shape library** and pin it; documents made from a template carry its libraries.
- Use **conditional formatting** to assign theme styles by shape type and to add marker icons from shape data, rather than colouring by hand.
- Use **layers** for overlays (Issues, Controls, Changes, Metrics) above a clean base map. Layers are per page, so set them up in the template page.
- Page settings: fixed landscape page size, no infinite canvas, page tiling on, so maps print and export as designed.
- Lines: Elbow is the default shape; turn on jumps where lines must cross. Standard Import stroke widths are whole pixels.
- Text in Standard Import: set the font size explicitly with an HTML style (`<span style="font-size: 11pt">`); without it Lucid auto-scales and sizes drift across shapes.
- Check generated files with `scripts/check_visual_standard.py` (in `process-map-visual-standard`) before import.

## 4. Document structure in Lucid
- One document per L1 area, or per engagement. Pages titled `L1 Landscape`, `L2 2 Procure to pay`, `L3 2.3 Approve supplier invoices`, `L4 2.3.1 Register invoice`.
- A legend on every page: level scheme, notation, lane convention, version, status, as-is or to-be.
- Parent shapes link to child pages, and child pages link back.
- Use data linking (Sheets, Excel, CSV) for volumes and timings only with the user's data and permission.

## 5. Verification
- Before upload: run the validation ladder for `.bpmn`, check CSVs for unique ids, valid shape names and resolvable line ends, and check JSON for unique ids and lane widths that sum to the pool.
- After upload, where you have access: read the document back (page list, shape count, any import warnings) and compare it with the source model. Without access, hand over the file with the exact import steps and say it was not imported.
