---
name: "service-blueprinting"
description: "Map a customer journey onto the service system behind it: frontstage, backstage, support, owners and wait points."
license: "MIT"
---

# Service Blueprinting

A journey map shows what the customer does and feels. A service blueprint shows the
service system that produces that experience — who does what behind the scenes, where
the customer waits, and who owns the next handoff. Use it when the question is "why does
the experience stall, and who is responsible for the next step?", not "how does the
customer feel?".

## 1. Decide a blueprint is the right artefact
- Blueprint when you must connect customer-facing steps to the staff, product and support
  work that delivers them, and expose ownership and wait points.
- If the request is only about customer actions, feelings or pain points, hand back to
  journey mapping (`journey-map-persona-artefacts`). Do not draw a blueprint to answer a
  sentiment question.
- If the request is an editable process model (BPMN, Lucidchart), hand the operating steps
  to the Business Process Analyst. A blueprint complements a process map; it does not
  replace an editable one.

## 2. Lay out the lanes and the lines
Use horizontal lanes, one row per stage of the journey, ordered left to right in time:
- **Physical evidence** — what the customer sees or touches at each step (receipt, screen,
  email, queue ticket).
- **Customer actions** — the steps the customer takes.
- **Frontstage / onstage contact** — what staff or the product show the customer.
- **Backstage contact** — staff or system work the customer does not see.
- **Support processes** — the internal systems and teams that make the backstage work possible.

Draw three boundary lines and label them:
- **Line of interaction** between customer actions and frontstage contact.
- **Line of visibility** between frontstage and backstage. Everything below it is hidden
  from the customer; everything above is seen. This line is the defining feature of a
  blueprint — without it you have a flowchart, not a blueprint.
- **Line of internal interaction** between backstage contact and support processes.

## 3. Fill each stage from source notes, not imagination
For every stage record, from the supplied notes:
- the customer action and the physical evidence;
- the frontstage touchpoint (what the customer is shown or told);
- the backstage action and the support process behind it;
- **who owns the next handoff** — the named team, role or system responsible for moving the
  case forward;
- **what the customer is told** at that point, and **where the customer waits** (a wait
  point is any stage where the customer has acted but the next visible response depends on
  hidden work).

## 4. Mark unknowns explicitly
- If the notes name no owner for a handoff, write `owner: unknown` and flag it as a gap to
  resolve. Never invent a team or role to fill the cell.
- If an explanation for a delay is not supported by the notes, write `cause: unverified`.
  Do not present a guess as the reason.
- A blueprint with honest gaps is useful; a blueprint with invented owners is a lie that
  will misdirect remediation.

## 5. Read it back as a diagnostic
The finished blueprint must let a reader answer three questions without extra prose:
1. Where does the customer wait, and on which hidden work?
2. Who owns the next action at each wait point?
3. What is the customer told while they wait?
If any answer is "unknown", that is a finding to surface, not a cell to fabricate.

## Voice
Visibility-line first. Name the owner of every handoff or mark it unknown. Refuse to invent
owners or causes, and refuse to draw a blueprint when a journey map or an editable process
map is what was actually asked for.
