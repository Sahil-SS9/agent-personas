---
name: "bpmn-modelling-method"
description: "Model business processes in BPMN 2.0 that business readers and tools both understand: right palette per level, pools versus lanes, labelled gateways and end states, exceptions and drill-down sub-processes."
license: "MIT"
---

# BPMN modelling method

BPMN 2.0.2 (OMG) is the standard notation. A diagram is only useful if it is valid and readable: valid so tools import it, readable so the people who do the work recognise their process.

## 1. Choose the palette for the level and audience
- **Descriptive** (business-facing L2/L3): pools, lanes, tasks, collapsed or expanded sub-processes, none/message/timer start events, none/message end events, exclusive and parallel gateways, sequence and message flows, data objects and stores, text annotations.
- **Analytic** (detailed L3/L4): adds boundary events (timer, error, message, escalation), event-based gateways, more event types, and task types where they add meaning (user, service, manual, send, receive, business rule, script).
- **Executable** detail (process-engine attributes) only when the target is a process engine and the user asks for it.
Use the smallest palette that tells the truth. Mixing in flowchart symbols makes it not BPMN.

## 2. Participants: pools and lanes
- A **pool** is an independent participant, such as your organisation, a customer, a supplier or an external system you do not control. Show external parties as black-box pools unless their internals matter.
- A **lane** is a role, team or system inside one pool. Pick one convention per diagram (roles, or teams, plus systems as lanes) and say so in the legend.
- **Sequence flow** stays inside one pool. Between pools, only **message flow**. Most structural mistakes are this.

## 3. Naming and labels
- Activities: imperative verb plus object, "Approve invoice". No nouns-only ("Approval") and no role names inside the box.
- Start events name the trigger: "Invoice received".
- End events name the **end state**, one per distinct outcome: "Invoice rejected", "Invoice scheduled for payment".
- Exclusive gateways are questions ("Invoice matches PO?"). Every outgoing flow is labelled with an answer. The work that produces the answer is a task **before** the gateway; a gateway decides, it does not do work.
- Sub-process names match the child map's title exactly.

## 4. Flow logic
- Pair splits and joins of the same type. A parallel split needs a parallel join, or the tokens never synchronise.
- Merge alternative paths with an exclusive gateway, not by pointing several flows at one task (an implicit join).
- Avoid conditional flows straight out of tasks (implicit splits). Use a gateway.
- Use inclusive and complex gateways only when the evidence really says "one or more of" or something stranger. Most business branching is exclusive.
- Loops (rework) go back through a gateway, with the loop condition labelled.

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
- Left to right, with the happy path on one straight line where possible.
- About 30 flow elements per page at most; past that, split by sub-process.
- No crossing lines where a re-route avoids them; consistent spacing; lanes ordered by flow, starting with the trigger.
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
