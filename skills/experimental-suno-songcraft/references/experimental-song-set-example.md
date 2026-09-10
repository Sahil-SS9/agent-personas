# Experimental Song Set — 5-Song Worked Example

Generated from user-provided Suno style descriptions. No artist brand profiles used. Demonstrates the full workflow: extract sonic DNA → discuss themes → build DSL → write lyrics → present as package.

## Song Profiles

| # | Title | Style | BPM | Key | Perspective |
|---|---|---|---|---|---|
| 1 | Still In It | Murky trap-soul | 132 | — | Male, trying to be himself with her |
| 2 | Float | Bass house / shadow trap | 150 | A Minor | Male, atmospheric vibe, euphoric float |
| 3 | Too Much (Or Not Enough) | Dark trap soul | 95 | — | Female, loving him so hard it peaks and collapses |
| 4 | Close Quarters | Late-night alt R&B | 84 | — | Male, intimate wordplay, J. Cole storytelling style |
| 5 | Made It | Trap soul → hype hip hop | 145 | — | Male, freedom/peace/triumph, three-verse arc |

## Structure Pattern

Songs 1-4 use different DSL arcs matched to their emotional shape:
- **Still In It** — `$b(x)=0$` throughout (sustained float, no drop — anxiety without release)
- **Float** — stutter-drop (percussive, sudden silence returns)
- **Too Much** — one-way crescendo to collapse (build→peak→fade)
- **Close Quarters** — `$dE/dx≈0$` (minimal movement, just presence)
- **Made It** — one-way `$dE/dx>0$` full runtime (V1 trap soul → V3 hype)

## Key Lyric Techniques Used

### Song 1 — "I just wanna be myself around you"
- The hook is repeated but context shifts each time (deeper meaning after each verse)
- Specific details over vague statements ("counting the floorboards" not "I'm nervous")
- Bridge pivots to future tense (hope/release)

### Song 2 — "Float"
- Minimalist lyrics, serves the pocket
- Repeated one-word hook anchors the track
- Imagery: wet streets, chrome, penthouse, blue screens (sensory, specific)

### Song 3 — "Too Much (Or Not Enough)"
- Female perspective, conversational intimate tone
- Builds from observation to confession
- Climax switches from "what if" fear to "I want to try" — the turning point

### Song 4 — "Close Quarters"
- Wordplay through physical description ("forget where you end and I begin")
- Specificity (t-shirt, streetlight stripes, tracing patterns)
- Playful but grounded — "Wet Dreamz" energy with "KOD" reflection

### Song 5 — "Made It"
- Three verses tell a chronological story (struggle → rise → arrival)
- Vocal delivery escalates with verse energy (DSL tracks the arc)
- Chorus is simple, anthemic, repeatable — the "crown" metaphor threads through

## Common DSL Patterns

For songs without a branded artist DNA profile, the DSL block needs to be **self-describing**. Everything the model needs to know about texture, mood, and dynamics must be in the block. Key dimensions to cover:

1. **Energy arc** — dE/dx direction, b-switch timing, E values at key points
2. **Per-layer production** — instrumentation, vocal processing, space, density
3. **Vocal persona** — gender, delivery style, processing (filtered, close-mic, etc.)
4. **Structural markers** — which layers correspond to which sections
5. **Genre anchor** — final line with genre blend, BPM, key, mood

See the individual song files in this directory for full output.