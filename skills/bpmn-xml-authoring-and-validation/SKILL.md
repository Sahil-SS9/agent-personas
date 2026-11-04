---
name: "bpmn-xml-authoring-and-validation"
description: "Write BPMN 2.0 XML with diagram interchange that imports into modelling tools and Lucidchart, then prove it with a structural checker, bpmnlint and a reference parser before handing it over."
license: "MIT"
---

# BPMN XML authoring and validation

A `.bpmn` file is the most portable BPMN deliverable. Camunda Modeler, bpmn.io, Signavio, Bizagi and Lucidchart all import it, and Lucidchart can export it again. It only travels if it is structurally sound **and** carries diagram interchange (DI). Without DI most tools show an empty canvas or an auto-layout nobody can review.

## 1. File skeleton
- Root `definitions` in namespace `http://www.omg.org/spec/BPMN/20100524/MODEL`, with `bpmndi` (`.../BPMN/20100524/DI`), `dc` (`http://www.omg.org/spec/DD/20100524/DC`) and `di` (`http://www.omg.org/spec/DD/20100524/DI`), plus a `targetNamespace`.
- `collaboration` with one `participant` per pool (`processRef` for pools you model; none for black boxes) and the `messageFlow`s.
- One `process` per modelled pool: a `laneSet` whose lanes list `flowNodeRef`s, then flow nodes, then `sequenceFlow`s with `sourceRef`/`targetRef`. Repeat them as `incoming`/`outgoing` on the nodes.
- `BPMNDiagram` > `BPMNPlane` (on the collaboration) with a `BPMNShape` + `dc:Bounds` for **every** participant, lane and flow node, and a `BPMNEdge` with at least 2 `di:waypoint`s for every sequence and message flow.
- `isExecutable="false"` unless engine execution is in scope.
- Default sizes: task 110x80, event 36x36, gateway 50x50. Lanes tile their pool exactly.

Start from `templates/l3-swimlane-template.bpmn` (two pools, three lanes, labelled gateways, merge, two named end states, message flows).

## 2. Ids and traceability
- Use stable, readable ids derived from the hierarchy (`Task_RegisterInvoice`, `Gw_Matches`, `Proc_L3_2_3`), never random ones, so revisions diff cleanly.
- Put supporting fact ids and the parent reference in `documentation` elements.
- Keep the process `name` equal to the map title ("2.3 Approve supplier invoices").

## 3. Validation ladder (run all that are available; report each separately)
1. **Well-formed XML** (any XML parser).
2. **Structural check**: `python3 scripts/check_bpmn.py file.bpmn`. Dependency-free. It checks reference integrity, single lane membership, sequence flows staying inside one pool, message flows crossing pools, named activities, start/end connectivity, gateway branch labels and full DI coverage. Errors fail; warnings (unnamed end states, implicit joins, unlabelled branches) must be fixed or justified.
3. **bpmnlint**: `npx bpmnlint file.bpmn` with `.bpmnlintrc` `{"extends": "bpmnlint:recommended"}`. It covers label-required, no-disconnected, fake-join, no-implicit-split, superfluous-gateway, start/end-event-required and others. It does **not** check lane membership or pool boundaries, which is why step 2 exists.
4. **Reference parse**: load it with `bpmn-moddle` (the parser behind bpmn.io). Unresolved references show up as warnings.
5. **Open it** in the target tool, if you have access, and look at it. Say which steps actually ran; a passing lint is not proof that a tool renders it.

Installing linters needs network access and the user's agreement. If unavailable, run step 2 and report the rest as not run.

## 4. Lucidchart round trip
- Import: Lucidchart > New > Import documents accepts `.bpmn` and `.xpdl`. Only BPMN 2.0 standard content survives; styling and vendor extensions are dropped.
- Export: File > Export > BPMN 2.0 (.bpmn) includes only shapes from Lucid's BPMN 2.0 library. Flowchart-library shapes are silently excluded. Build in the BPMN library if a round trip is needed.

## 5. Common defects
- Sequence flow between pools (use message flow), or message flow inside one pool.
- A node missing from every lane, or listed in two.
- DI missing for lanes or message flows: the file imports but looks broken.
- Flows pointing at a gateway's id after it was renamed: run the checker after every edit.
- Hand-edited coordinates that leave a shape outside its lane; keep bounds inside the lane box.
