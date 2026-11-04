---
name: "process-architecture-levels"
description: "Organise process knowledge into a Level 1 to 4 hierarchy, decide which levels the evidence supports, and keep every child map traceable to its parent with consistent naming and numbering."
license: "MIT"
---

# Process architecture levels (L1 to L4)

Organisations number process levels differently. Before mapping, find out whether the organisation already has a level scheme or framework, and use it. Otherwise use the default below and put it in the legend of every deliverable.

## Default level model
| Level | Answers | Content | Typical notation | Size guide |
|---|---|---|---|---|
| **L1 Process landscape / value chain** | What does the organisation do end to end? | Process areas such as "Procure to pay" or "Hire to retire", grouped into core, management and support | Value-chain chevrons or block landscape | 5 to 12 areas |
| **L2 Process groups / sub-process map** | What are the main stages of one L1 area? | Ordered stages, owner, SIPOC per stage (suppliers, inputs, outputs, customers), key measures | Linear block flow, SIPOC table, BPMN collapsed sub-processes in one pool | 4 to 10 stages |
| **L3 Process flow** | How does one L2 stage run across roles? | Swimlanes per role, team or system; activities, decisions, events, handoffs, main exceptions, key documents and systems | BPMN 2.0 collaboration, or a cross-functional swimlane flowchart | 8 to 30 activities |
| **L4 Procedure / task detail** | How exactly is one L3 activity done? | Steps, screens and fields, business rules, decision tables, controls, SLAs, work instructions | BPMN sub-process, detailed flowchart, numbered SOP table, decision table | One activity per map |

Crosswalk: APQC's framework uses Category, Process Group, Process, Activity, Task (five levels). Its rules (verb-noun naming, mutually exclusive and collectively exhaustive children, each child serving its parent's outcome) apply at every level here. Flow and sequence start at L3. The framework itself deliberately excludes order and dependency. Some organisations add an L0 enterprise view or call task detail L5. State the mapping instead of arguing about it.

## Level-fit assessment: what the evidence supports
Classify each ledger fact by its granularity signal:
- **L1/L2 signals**: process-area or stage names, outcomes, owners, "then it goes to fulfilment".
- **L3 signals**: a role plus an action plus a handoff or decision ("AP checks the PO match; if it fails the budget holder reviews it").
- **L4 signals**: screens, fields, clicks, exact thresholds, checklists, system transactions ("I paste the PO number into the reference field; over GBP 10k needs a second approver").

Then produce a **coverage matrix**: rows are process areas or stages, columns are L1 to L4, and each cell is `supported` (n facts), `partial`, `inferred only` or `missing`. Recommend:
1. which maps can be drawn now and at which level;
2. which levels need more elicitation, and who to ask;
3. where a transcript supports deep L4 for one activity but only thin L2 context. Map the L4 and flag the context gap rather than padding the L2.

Never manufacture L4 detail from L2-grade talk. Never collapse rich L4 evidence into an L3 box and lose it: park it as an L4 candidate.

## Decomposition rules
- **One parent each**: every L(n+1) map decomposes exactly one L(n) element. Its title repeats the parent's number and name.
- **Numbering**: hierarchical, such as 2 > 2.3 > 2.3.1 > 2.3.1.4. Numbers are an index, not an execution order, unless the map shows flow.
- **Naming**: verb plus noun, descriptive rather than prescriptive ("Approve supplier invoices", not "Invoice approval process").
- **MECE children**: no two children overlap, and together they cover the parent's scope. Report a gap rather than stretching a child to hide it.
- **Consistent boundaries**: the trigger and end states of an L3 map match the inputs and outputs of its L2 stage. The end states of an L4 map match the outgoing branches its L3 parent depends on.
- **Split when too large**: if an L3 exceeds about 30 activities or 6 lanes, split it into sub-processes and make each one its own L4 or L3 page.

## Deliverable skeleton
1. Level scheme and legend.
2. Coverage matrix with recommendations.
3. Hierarchy register: number, name, level, parent, owner, status (draft / validated / approved), as-is or to-be, map file or page, and supporting fact ids.
4. The maps, produced with the notation skills and labelled with their level in the title ("L3 2.3 Approve supplier invoices (as-is, draft v0.2)").
