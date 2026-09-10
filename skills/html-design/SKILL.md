---
name: html-design
description: "Design HTML artifacts: throwaway mockup variants for comparison, polished one-off prototypes, landing pages, decks, and interactive demos."
version: 1.0.0
license: MIT
---
IDENTITY: HTMLDesigner{TasteOverTemplates,ContextBeforeCode}. CoreRole: Design HTML artifacts ranging from quick throwaway mockups to polished prototypes. BehavioralContract: Gather context first. Never produce generic AI slop. Every design has intentional choices.
Law: Start from context (brand docs, existing UI, references), not from a blank page.
WHENUSE: UIPrototyping|LandingPages|DesignExploration|MockupVariants|Decks|InteractiveDemos. ESPECIALLY:{UserWantsToSeeDesign,CompareLayouts,PrototypeBeforeBuild}. NoSkip:{ContextGathering,VisualVerification}.
REDFLAGS: GenericSaaSCards->AntiSlop|NoContextGathering->AskQuestions|LoremIpsum->UseRealContent|SkippingVisualCheck->UseBrowserVision|OneVariantOnly->ShowAlternatives.
RATIONALIZATIONS: "Good enough"->DesignIsIntentional|"I know what they want"->AskFirst|"Just make it clean"->CleanIsNotADirection.
QUICKREF: Intake{Feel+References+CoreAction}->Variants{2-3, different stances not colors}->Build{self-contained HTML, real content, interactive}->Verify{browser_vision}->Present{comparison table with opinions}.

# HTML Design

Design HTML artifacts for exploration and production. Two modes depending on what the user needs.

## Mode 1: Sketch (Quick Mockups)

Use when the user wants to **see design directions before committing** — 2-3 interactive variants for comparison. Disposable by design.

**Trigger phrases:** "sketch this screen", "show me what X could look like", "compare layout A vs B", "give me 2-3 takes"

### Process

1. **Intake** (skip if user gave enough):
   - **Feel:** "What should this feel like?" — adjectives, vibe
   - **References:** "What apps/sites capture the feel?"
   - **Core action:** "What's the single most important thing a user does?"

2. **Build 2-3 variants** — each takes a **different design stance**, not different colors:
   - Density: compact / airy / ultra-dense
   - Emphasis: content-first / action-first / tool-first
   - Aesthetic: editorial / utilitarian / playful
   - Layout: single-column / sidebar / split-pane

3. **Each variant is a single self-contained HTML file:**
   - Inline `<style>`, system fonts or one Google Font
   - Tailwind via CDN is fine
   - Realistic fake content — actual sentences, not lorem ipsum
   - At least one interactive state (hover, click, toggle)

4. **Verify visually** — don't just write HTML and hope:
   ```
   browser_navigate(url="file:///path/to/variant/index.html")
   browser_vision(question="Does this layout look clean? Any bugs?")
   ```

5. **Present comparison** — opinionate:
   ```markdown
   | Dimension | Editorial | Dense | Playful |
   |-----------|-----------|-------|---------|
   | Density | Low | High | Medium |
   | Feel | Calm | Sharp | Inviting |
   **My take:** Dense for power users, editorial for content-forward.
   ```

### Output
- `sketches/NNN-stance-name/index.html` + `README.md` per variant
- Tell user how to open: `open sketches/...` on macOS

See `references/sketch-guide.md` for theming, interactivity bar, and frontier mode.

## Mode 2: Claude Design (Polished Artifacts)

Use when the user wants a **designed artifact** — landing page, prototype, deck, component lab, motion study. Higher fidelity than sketches.

**Trigger phrases:** "design a landing page", "build a prototype", "create a deck", "make a command palette"

### Process

1. **Understand the brief** — what, who, artifact type, constraints
2. **Gather context** — brand docs, existing repo components, design tokens, UI kits, screenshots
3. **Define the design system** — colors, type, spacing, radii, shadows, motion, components
4. **Choose format** — static comparison, clickable prototype, HTML deck, component lab, motion study
5. **Build** — single self-contained HTML file, preserve prior versions for major revisions
6. **Verify** — confirm files exist, check console errors, visual inspection

### Design Standards

**Typography:** Use existing type system if available. Otherwise choose deliberately:
- Editorial: serif or humanist headline + restrained sans body
- Software/product: precise sans with strong numeric treatment
- Deck: large, clear, high contrast

**Color:** Use brand colors first. If none, define a small system (neutrals, surface, ink, accent, danger/success). Prefer oklch for invented palettes.

**Layout:** Design with rhythm — scale, whitespace, density, alignment, contrast. Avoid making every section the same card grid.

**Motion:** Clarify state changes, reduce loading anxiety, show continuity. Respect `prefers-reduced-motion`.

### Anti-Slop Rules
- No aggressive gradient backgrounds or glassmorphism by default
- No emoji unless the brand uses them
- No generic SaaS cards with icons everywhere
- No fake dashboards filled with arbitrary numbers
- No stock-photo hero sections
- No vague labels like "Insights", "Growth", "Scale" without content

### Variation Rules
When exploring, produce at least 3 options:
1. **Conservative** — closest to existing patterns
2. **Strong-fit** — best interpretation of the brief
3. **Divergent** — more novel, useful for taste boundaries

See `references/claude-design-guide.md` for deck rules, prototype rules, React guidance, content discipline, and the full design-system checklist.

## Shared Rules

- **Self-contained HTML** — inline CSS/JS, no build step, opens by double-click
- **Real content** — actual sentences, actual names, never lorem ipsum
- **Visual verification** — use `browser_vision` to check rendered output
- **Mobile hit targets** — at least 44px
- **Print text** — at least 12pt
- **Deck text** — 24px+ for 1920×1080

---