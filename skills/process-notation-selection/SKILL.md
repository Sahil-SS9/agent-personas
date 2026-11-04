---
name: "process-notation-selection"
description: "Choose and draw the right non-BPMN map for the question: value-chain landscape, SIPOC, flowchart, cross-functional swimlane, value stream map, or diagrams-as-code, without mixing notations."
license: "MIT"
---

# Process notation selection

BPMN is not always the right answer. Choose the notation that answers the reader's question at the level being mapped, and never mix notations on one page.

## 1. Pick by question
| Question | Notation | Level |
|---|---|---|
| What does the organisation do, and how do the areas relate? | Value-chain or landscape map: core, management and support bands | L1 |
| What is in scope: who supplies what to whom? | SIPOC table (suppliers, inputs, process 5 to 7 steps, outputs, customers) | L2 scoping |
| What are the steps and decisions, for one role or a simple flow? | Basic flowchart (terminator, process, decision, document, data, predefined process) | L3/L4 |
| Who does what, and where are the handoffs? | Cross-functional swimlane flowchart, one lane per role or system | L3 |
| Where does time go, and where is the waste? | Value stream map: process boxes with data boxes, wait/inventory between steps, timeline | L2/L3 |
| Precise, tool-portable, exception-aware flow | BPMN (see `bpmn-modelling-method`) | L2 to L4 |
| How does a customer experience it? | Not a process map: a journey map or service blueprint; hand over | n/a |
| How does data move, or how does a record change state? | Data-flow or state diagram; hand over to the systems or data role | n/a |

When the audience is business-only and the organisation has no BPMN standard, a clean swimlane flowchart at L3 is often better received. Offer BPMN when portability, exception handling or automation analysis matters.

Match the dialect to the reader: executives get a landscape or scope model, process owners a summary chart or L2, the people who do the work an L3 swimlane, analysts and engineers BPMN with the analytic palette. Swim lanes help readers answer "who does this?"; when roles do not matter to the question, lanes add search effort.

## 1b. Build up to the swimlane (fast and less wrong)
1. **Scope model**: trigger, results, 5 to 7 phases, main cases (see TRAC in `process-source-elicitation`).
2. **Summary chart**: the phases plus the internal and external participants, to show the process crosses the organisation.
3. **Augmented scope model**: 5 to 10 activities per phase, first the what, then who and with what system.
4. **Swimlane or BPMN L3**: drawn from the augmented model, which makes it quick.
Adding who and how too early locks in today's organisation and systems.

## 2. Swimlane flowchart rules
- Lanes are roles or systems (state the convention). Order lanes so that flow mostly moves downward and to the right.
- Every lane crossing is a handoff. Label what is handed over when it is not obvious.
- Decisions are diamonds phrased as questions, with every exit labelled.
- One start terminator, and one terminator per distinct end state.
- Use a predefined-process shape for anything that has its own child map, and link it.

## 3. Value stream mapping essentials
- Map one product or service family, door to door, from the customer's point of view.
- Each process box gets a data box: cycle time, changeover or setup, uptime, and percentage complete and accurate, only where measured or stated with a source.
- Show queues and waits between boxes. The timeline ladder separates value-added time from lead time.
- Process cycle efficiency = value-added time / total lead time. Compute it only from evidenced numbers and show the inputs.
- A future-state VSM is to-be. Label it, and keep it separate from the current state.

## 4. Diagrams as code (portable drafts)
- **Mermaid** `flowchart LR`, with `subgraph` blocks as pseudo-lanes, for quick review in docs and chat. Say it is an approximation of swimlanes.
- **PlantUML** activity diagrams with `|Lane|` partitions for swimlanes.
- These are review drafts. For Lucidchart use the delivery routes in `lucidchart-diagram-delivery`.

## 5. Every map carries
Title with level and number, as-is or to-be, version and status, a legend for any symbol beyond the basics, the lane convention, the source fact ids (in notes or an appendix), and its open questions.
