---
name: "bpmn-modelling-method"
description: "Model business processes in BPMN 2.0 that business readers and tools both understand: right palette per level, pools versus lanes, labelled gateways and end states, exceptions and drill-down sub-processes."
license: "MIT"
---

# BPMN modelling method

BPMN 2.0.2 (OMG) is the standard notation. A diagram is only useful if it is valid and readable: valid so tools import it, readable so the people who do the work recognise their process.

## 1. Choose the palette for the level and audience
- **Descriptive** (business-facing L2/L3), as defined by the standard: pools, lanes, none/user/service tasks, collapsed and expanded sub-processes, call activities, exclusive and parallel gateways, sequence and message flows, none/message/timer start events, none/message/terminate end events, data objects and stores, text annotations, groups.
- **Analytic** (detailed L3/L4) adds: send and receive tasks, conditional and default flows, loop and multi-instance markers, inclusive and event-based gateways, link events, and timer, message, error, escalation, signal, compensation and conditional intermediate and boundary events.
- Real models use about 9 different symbols. Publish the house palette (descriptive plus a short, named list of analytic additions) and treat anything outside it as needing a reason and a legend entry.
- **Executable** detail (process-engine attributes) only when the target is a process engine and the user asks for it.
Use the smallest palette that tells the truth. Mixing in flowchart symbols makes it not BPMN.

## 2. Participants: pools and lanes
- A **pool** is an independent participant, such as your organisation, a customer, a supplier or an external system you do not control. Show external parties as black-box pools unless their internals matter.
- A **lane** is a role, team or system inside one pool, named in the singular and never the same as a pool. Pick one convention per diagram (roles, or teams, plus systems as lanes) and say so in the legend. At most three nesting levels.
- **Sequence flow** stays inside one pool. Between pools, only **message flow**, drawn at right angles to the main direction of sequence flow. Most structural mistakes are this.
- Each pool appears once per diagram and holds one complete process. Usually only your own pool is open; external parties are black boxes.
- Lanes suit business-facing maps where responsibility is the question. For executable models, or where participants interact heavily, use a separate pool per participant joined by message flows: lanes there force crossing lines and break the happy path.
- Systems that only store data are data stores; systems that do real work in the process are collapsed pools or lanes.

## 3. Naming and labels
The diagram must stand on its own: if a rule, condition or outcome is only in the XML or a separate document, business readers will not see it.
- Activities: verb plus object in sentence case, "Approve invoice". Verb-object labels are measurably less ambiguous than action-noun ("Invoice approval") or noun-only labels. No role names inside the box, no system or code names, no abbreviations without a glossary, no mushy verbs ("Handle invoice").
- Events: the object plus the state it is in when the process leaves the event, "Invoice received", "Invoice paid". Be specific about the outcome; "Invoice processed" says nothing. (Some teams label message starts "Receive invoice"; pick one convention per repository.)
- Timer events state the time rule ("1st working day of month", "5 days").
- End events: one per distinct end state, named noun plus adjective or past participle ("Invoice rejected"). Never two end events with the same name; merge them if they mean the same outcome. Otherwise prefer a single end (7PMG G3).
- Exclusive gateways test how the preceding activity ended. Every gateway is preceded by the activity that produces the answer; a gateway decides, it does not do work. Label the gates with the end states ("Valid" / "Invalid"), or with two gates, label the gateway as a question and the gates "Yes" / "No".
- Do not label parallel gateways, event-based gateways or any joining gateway.
- Label every boundary event and intermediate event; an error or escalation boundary matches the name of the event thrown inside the sub-process.
- No two activities in a process share a name unless they are the same activity.
- Sub-process names match the child map's title exactly.

## 4. Flow logic (7PMG and house rules)
- As few elements as possible (G1); keep the number of flows in and out of each element low (G2).
- Model structured blocks: every split has a matching join of the same type (G4), drawn symmetrically so the block is visible. A parallel split needs a parallel join.
- Draw split and join gateways as separate symbols, and show the X marker on exclusive gateways.
- Merge alternative paths with an exclusive gateway, not by pointing several flows at one task (an implicit join). Exception: a merge straight after a start event can be left implicit if that reads better.
- Each activity has exactly one outgoing sequence flow; branching happens only at gateways. An activity that checks something is followed by a gateway.
- Avoid inclusive (OR) gateways (G5) unless the evidence really says "one or more of".
- More than two decisions in a row is usually a business rule: move it to a decision table or checklist and replace the cascade with one "Decide ..." activity.
- Loops (rework) go back through a gateway, with the loop condition labelled.
- Decompose any model past 50 elements (G7); aim for 9 to 15 activities per diagram.

## 5. Exceptions, from evidence
Model the happy path first. Then add the exceptions the ledger supports, most frequent first:
- timer boundary event for SLA breaches or chasing;
- message boundary or event sub-process for cancellation or changes mid-flight;
- error end or boundary for hard failures.
Unevidenced "what ifs" go into the gap questions, not onto the diagram.

## 6. Hierarchy across levels
- L2 in BPMN: one pool, a chain of collapsed sub-processes, no lanes needed.
- L3: a collaboration with lanes. Each activity that has its own L4 becomes a collapsed sub-process or call activity marked as drillable.
- L4: the child process. Its end states equal the outcomes the L3 parent's next gateway tests.

## 7. Layout and readability
- Left to right in time order, with the happy path on one straight line through the middle. No flow leaves a shape on its left or enters on its right.
- Fit each map on one screen or page. If it would scroll, split it or wrap it (snake or multi-line layout); scrolling hurts understanding more than a wrapped layout does.
- No crossing lines where reordering lanes or paths avoids them; avoid flows that cross many lanes; use link events only for genuinely distant connections.
- Keep default symbol sizes: a bigger box reads as more important. Colour, size and line rules are in `process-map-visual-standard`.
- Put the legend, level, version, status and as-is/to-be in a text annotation or the page title.
- Annotations carry rules, volumes and pain points, with the fact id.

## 8. Quality checklist
- [ ] At least one start and one named end event per process; nothing disconnected.
- [ ] Every gateway is a question with labelled branches; splits and joins paired.
- [ ] No sequence flow across pools; message flows only between pools.
- [ ] Every activity sits in exactly one lane and is named verb plus object.
- [ ] Every element traces to fact ids or is marked assumed.
- [ ] The palette matches the audience; no flowchart symbols mixed in.
For machine-checkable files, hand over to `bpmn-xml-authoring-and-validation`.
