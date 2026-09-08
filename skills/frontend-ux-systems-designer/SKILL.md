---
name: "frontend-ux-systems-designer"
description: "Discover design intent, compare visual directions, and build coherent accessible frontends."
license: "MIT"
---
# Frontend UX Systems Designer

Own design discovery, creative direction, user selection and implementation. Components serve the design; they do not determine it. Cover marketing, editorial, commerce and product interfaces with task-appropriate methods. This experimental candidate is not a benchmarked design system or a guarantee of originality.

## When to Use
- A user wants a new frontend or a meaningful redesign but has not selected its visual direction.
- A product needs several genuinely distinct design choices, not colour-swapped templates.
- A selected direction needs component sourcing, implementation and visual/functional verification.

## Prerequisites
Identify audience, primary task, project type, existing stack/brand, content, assets, budget and change permissions. Inspect existing material before asking. Preserve established brand and interaction patterns unless an overhaul is approved. Do not force exploration for a small bug fix or an already approved design.

## Procedure
1. Discover intent through a short adaptive interview, one question at a time. Ask only unresolved questions: desired impression, references and what specifically appeals, disliked examples, density, motion appetite and constraints. Offer concrete contrasts when the user lacks design vocabulary. Stop once differences that would change the design are resolved; do not make the user complete a questionnaire.
2. State a concise design brief and separate fixed constraints from preferences. For product UI, define key workflows and information hierarchy; do not apply landing-page hero conventions to dashboards or forms.
3. Research visual references before selecting libraries. Include independent sites/editorial/brand sources and a broad component search including 21st.dev. Search outside the shadcn ecosystem and respect non-React stacks. Review current primary docs, compatibility and licence evidence; popularity is discovery evidence, not quality proof.
4. Develop three distinct directions by default, or five when the user requests broader exploration. Begin each with an experience concept: what users should feel, what they can do differently, and which visual/interaction idea unifies it. Give each a distinct typographic voice, spatial composition, background art direction and motion/interaction language. Keep representative content and user outcomes equivalent, not the widget structure. Research and realise the concept before choosing a library; do not merely recolour, restyle or rearrange the same template.
5. Produce lightweight rendered previews of each direction at desktop and mobile sizes. Include the primary task, representative supporting content and the signature live interaction. Make the behaviour that differentiates a concept real, even when the final transaction is explicitly a demo. Use licensed font/art assets where needed; a system-font-only static scaffold cannot prove broad creative range. Supply actual preview URLs and normal-motion evidence alongside a separately checked reduced-motion alternative. If rendering is unavailable, disclose the blocker; descriptions or moodboards are not equivalent delivered previews.
6. Review directions for distinctiveness, coherence and brief fidelity using the comparison reference. Reject superficial variants and redesign them before presentation. Keep accessibility and functional correctness firm; aesthetic conventions are contextual. No blanket bans on gradients, serif fonts, centred layouts, familiar libraries or conventional product patterns.
7. Present the three or five previews with rationale, source combinations, main trade-off and a recommendation. Ask which direction to develop and which specific elements to retain/change. Allow bounded recombination, then re-check coherence and confirm the revised direction. Do not proceed to full implementation without selection or explicit user authority to choose.
8. Select implementation foundations after direction approval. Compare reuse, adaptation and native CSS/custom construction. Mix compatible source material only under a common token, semantics and interaction model; do not stack competing full design systems. Unknown licence blocks importing that component, not continuing design exploration with lawful alternatives.
9. Implement the approved direction with semantic tokens, responsive layouts and applicable idle/loading/empty/error/partial/success/cancel/retry states. Preserve approval boundaries for consequential AI actions. Use real supplied content or clearly labelled examples; never invent testimonials, customers or product evidence to make a design convincing.
10. Render and inspect the actual implementation against the chosen previews. Observe normal-motion choreography and the reduced-motion fallback separately, including custom canvas/shader work. Test keyboard/focus, contrast, mobile reflow, key task completion and performance. Provide pause controls for continuous decorative motion; stop offscreen work. Review typography, background treatments and visual rhythm across the whole experience. Feed measured defects back into a bounded repair pass and recheck all affected contexts. Screenshots alone do not establish motion, accessibility or working interactions.

## Stop Rules
No production edits, paid assets, external publication or dependency migration beyond authorisation. Do not claim preview rendering, visual review or behavioural testing that did not occur. Never trade usability for novelty. An inherited aesthetic rule that conflicts with the approved brief must be challenged, not silently enforced.

## Output Contract
Only report fields relevant to the current phase; do not dump empty downstream checklists for a simple question or blocker.

Supply when applicable: design_brief; interview_decisions; constraints; reference_sources; direction_count (3 or 5 for exploration); directions with composition/type/imagery/density/motion choices; desktop_mobile_preview_handles; pairwise_difference_review; tradeoffs; selected_direction and approval; component_provenance; token_mapping; state_matrix; rendered_implementation_evidence; functional_accessibility_checks; unresolved_risks.

For bounded fixes or an already approved direction, record exploration_not_needed and its reason instead of manufacturing alternatives.

## Verification
Separate gates: brief completeness; real preview delivery; distinctiveness/coherence/brief fidelity; user selection; component rights/compatibility; actual build and interactions; final visual fidelity. Creative acceptance is separate from technical acceptance: functioning but generic work remains creatively unaccepted. Evaluate concepts in live interaction as well as stills; do not substitute an effect count or novelty claim for human judgement. Static tests can check contracts and missing evidence, not prove taste or eradicate generic design. Behavioural and visual evaluations remain required for promotion.

## References
- [Design discovery and comparison](references/design-discovery-comparison.md): load for interviews, directions and user selection.
- [Source landscape](references/source-landscape.md): load before reference/component discovery.
- [Inherited taste-rule audit](references/taste-rule-audit.md): load before reusing anti-slop instructions.
- [Component selection](references/component-selection.md): load before importing or adapting components.
- [Interaction acceptance](references/interaction-acceptance.md): load for modals, motion, asynchronous work or AI approvals.
