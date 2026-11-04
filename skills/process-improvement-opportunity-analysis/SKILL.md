---
name: "process-improvement-opportunity-analysis"
description: "Analyse as-is maps for handoffs, rework, waits, duplicate entry, control gaps and policy-practice deviations, then build an evidence-linked opportunity register and to-be options without inventing benefits."
license: "MIT"
---

# Process improvement opportunity analysis

An as-is map is a diagnosis tool. Analyse it systematically, tie every opportunity to evidence, and keep the as-is honest: a to-be is never presented as the current process.

## 1. Structural scan of the map
Count and list each of these, with element ids:
- **Handoffs**: lane crossings. Each one is a delay and an error risk.
- **Rework loops**: flows back to an earlier step; record the loop trigger and its frequency, if evidenced.
- **Waits and queues**: timers, "waits for", batch runs, inbox steps.
- **Duplicate or re-keyed data**: the same data entered in two systems, swivel-chair transfers, spreadsheets in the middle.
- **Approvals**: who approves, what they check, whether rejection ever happens (a rubber stamp), and thresholds.
- **Controls**: preventive or detective, where they sit, and gaps against the documented policy.
- **Single points of failure**: one named person, or a manual step with no cover.
- **Policy versus practice**: every conflict in the register is a candidate finding.
- **Unclear ownership**: steps with no clear lane, or shared lanes. Draft a RACI where it helps.

## 1b. Look beyond the flow: six enablers
Process performance also depends on technology and information systems, motivation and measurement, people and organisation, policies and rules, and facilities, not only on the flow design. Tag each finding with the enabler it sits in; many "process problems" are measurement or policy problems.
- Gateway cascades usually hide a business rule; extracting it into a decision table is often a quick win.
- Improving one phase can make the whole worse. Check every opportunity against the end-to-end result.

## 2. Value and waste lens
Classify activities as value-adding (the customer would pay for it), business-necessary (regulatory or control) or waste. Tag waste type: waiting, rework/defects, over-processing, motion/transport of information, inventory/backlog, unused skills, over-production. Apply it to evidenced activities only.

## 3. Opportunity register
| Field | Rule |
|---|---|
| id | O01... |
| map elements | ids from the as-is map |
| observation | what happens, with fact or conflict ids |
| likely cause | labelled as a hypothesis until validated |
| type | eliminate, simplify, standardise, automate (workflow, integration, RPA, rules), add control, policy change, training, data fix |
| benefit | qualitative always; quantified only from evidenced volumes and times, showing the arithmetic, as a range if the inputs are ranges |
| effort and risk | low, medium or high, with the reason |
| dependencies | systems, policy owners, other opportunities |
| owner to validate | role |

Prioritise with an impact versus effort grid and say which inputs are assumptions.

## 4. Automation suitability
Good candidates are rule-based, have structured digital inputs, run at high volume, have stable rules and a low exception rate. Simplify or standardise first: automating a broken process makes it fail faster. Flag where an automation would remove a control or hide an exception path.

## 5. To-be options
- Keep the same level structure and numbering. Mark changed, new and removed elements against the as-is.
- State what changes for each role, system, control and measure.
- Offer more than one option when trade-offs are real: quick win versus structural change.
- To-be maps go through the same validation as as-is maps, with the people who will run them.

## Stop rules
- No benefit figure without its inputs. No "saves 40%" from intuition.
- No root cause stated as fact before validation.
- Requirements, solution design and build go to the right role; this skill identifies and frames.
