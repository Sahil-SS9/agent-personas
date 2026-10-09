---
name: "generative-asset-production"
description: "Plan, route and verify generated image and video assets for a design, matched to the generation tools the user can actually access."
license: "MIT"
---

# Generative asset production

Ambitious web design is carried by its media: commissioned-looking imagery, illustration, lettering, texture and motion footage. Hand-drawing subject matter in CSS or SVG to stand in for that media produces clip art next to anything real. This skill turns an art direction into a media plan, routes every asset to the best generation capability the user has, and verifies the results before they reach the build.

## When to use
Any surface whose direction calls for imagery, illustration, lettering, texture, ambient video or state-transition footage. Skip for UI inside an established world whose asset library already covers the need.

## Procedure
1. **Discover access before planning.** Inventory what the user can use, by capability class rather than brand: local model servers (installed checkpoints and workflows), hosted APIs with working credentials, built-in agent tools, and licensed stock libraries. For each, record: classes covered, cost model (free/local, metered, subscription), and the user's spending permission. Paid or metered tools are used only with explicit approval for this job; otherwise they are listed as unused upgrades. Probe, do not assume: a key that exists may not work, and a model that is installed may not have a workflow.
2. **Write the media plan from the thesis.** Before any build, list every asset the direction needs, each with: role (hero plate, layered element, texture, lettering, room/product view, ambient loop, state-transition clip, poster frame), exact pixel size and aspect, whether it needs transparency or layer separation, its motion behaviour, and its fallback. The plan names the signature media moment, the one asset the page is remembered for, and spends most of the effort there.
3. **Route each asset to a capability class.**
   - Style-consistent sets and layered pieces: reference-conditioned or instruction-edit image models (generate the master once, derive the parts from it).
   - Lettering, signage, posters, any legible text inside an image: text-rendering image models; never trust a general model's text.
   - Photoreal stills: the strongest photographic model available.
   - Harmonising a set (horizon, palette, grain, light direction): an image-edit pass over all members against one reference.
   - Ambient loops: image-to-video from the approved still, short (4-8 s), with the first and last frames matched for a seamless loop.
   - Interaction states (closed to open, day to night, before to after): first-and-last-frame video models, keyframed from the two approved stills.
   - Resolution: dedicated upscalers after approval, never before.
   Use the best available tool per class. When a class has no tool, use the fallback ladder.
4. **Lock a style bible before volume.** Fix the medium (for example film stock, print process, illustration technique), palette, light, lens or mark-making, and the recurring motifs. Generate one master asset, inspect it, then condition every later asset on it (reference image, same model, fixed seeds where supported). Mixed models in one set are allowed only when a harmonising pass follows.
5. **Generate for compositing.** Produce elements the page can layer and animate: separate plates, cut-outs with clean alpha (matte them if the model cannot), and states with identical framing. The DOM composes and animates; the generator supplies the material. Code-drawn shapes are for UI, diagrams and deliberate graphic styles, never imitations of painted, photographed or crafted objects.
6. **Verify every asset at full size.** Check against the plan: real output dimensions and aspect (tools often ignore the request; crop or regenerate), anatomy and hands, perspective and geometry, text spelling, repeated-pattern artefacts, set consistency, loop seams, and that nothing implies false facts about the client (invented people presented as real staff, places that do not exist). Reject and regenerate; do not hide defects with overlays.
7. **Prepare for the web.** Encode stills as AVIF/WebP with explicit dimensions and responsive sources. Encode video as WebM with an MP4 fallback, muted, inline, looped where ambient, each with a poster frame. Give every video a reduced-motion path (show the poster, or play only on explicit request). Lazy-load everything below the fold. Hold the page to an asset budget and record the totals.
8. **Record provenance.** Keep a manifest per asset: capability class, tool and model, prompt, seed or reference, edits applied, licence or terms, and generated-or-real status. Generated imagery that stands in for the client's real photography is flagged as a placeholder until the owner replaces or approves it.

## Fallback ladder
When a class has no generation access: (1) the next-best available class with an edit pass; (2) licensed stock with attribution, art-directed by crop, grade and treatment into the style bible; (3) a deliberately graphic direction (type-led, pattern, diagrammatic, procedural canvas or shader art) chosen as a style, not as a stand-in for photography or painting; (4) a clearly labelled placeholder plus the asset brief, so the owner can commission it. Tell the owner which tier each asset landed on and what access would raise it.

## Decision rules
- Never write model or vendor names into skills, personas or plans meant to outlive the job. Route by capability class and rediscover the tools on every job: models are replaced fast, and the best currently available tool in each class wins, judged by testing it on the master asset, not by reputation.
- No asset without a role in the media plan; no plan item without a fallback.
- The thesis selects the medium; the available tools select the route. A weak tool never quietly downgrades the direction: report the gap instead.
- Spending follows explicit permission per job, never inferred from a key existing.
- One style bible per page; every asset is judged against the master, not on its own.
- Motion footage must earn its weight: one signature clip beats many ambient ones.

## Pitfalls
- CSS or SVG drawings of buildings, people, food or objects next to real photographs.
- Generating each image from scratch with unrelated prompts, so the set does not look like one world.
- Trusting the requested aspect ratio or the model's lettering without checking.
- Autoplaying heavy video with no poster, no reduced-motion path and no size budget.
- Presenting generated people, rooms or products as the client's real ones.

## Done
A media plan, a style bible with its master asset, every asset verified at full size and encoded for the web, a provenance manifest, and a short note of the access tier each asset used and what better access would change.
