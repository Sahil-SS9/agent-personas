# H3 Prompting — Evidence, Sources, and Health Warning

This package exists so that a reader can tell what is **known** from what is **guessed**. That
distinction is the whole value. Read this file before trusting anything in the others.

---

## 1. The four evidence grades

Every claim in this package carries one of four tags.

| Tag | Means | What it licenses you to do |
|---|---|---|
| `[OFFICIAL]` | Stated in MiniMax's own prompt-writing guides, model card, or repository documentation | Treat as the specification. If output contradicts it, suspect your prompt, not the rule. |
| `[OBSERVED]` | Someone ran a generation and reported what came back | Treat as a working hypothesis. Check the reporter count — most are n=1. |
| `[INFERRED]` | Derived from official structure, or measured across a corpus of working prompts | Reasonable default. Nobody has demonstrated that violating it degrades output. |
| `[ASSERTED]` | A community kit states it as fact with no evidence of any kind | Someone's taste, written in the voice of a specification. Ignore freely. |

**When two grades conflict, the higher grade wins** — except where an `[OBSERVED]` finding is
corroborated by several independent people and the `[OFFICIAL]` text is merely permissive rather
than prescriptive. The one documented case of this is `N/A` in the audio fields: the guide allows
it, several practitioners report it provokes invented audio, and the affirmative-silence phrasing
satisfies both.

---

## 2. Source register

### Primary — MiniMax's own documentation

| Source | What it is | Weight |
|---|---|---|
| `docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md` | The prompt format for T2VA / I2VA / FL2VA / L2VA. Field schema, camera vocabulary, dialogue syntax, alignment lines, worked cases. | Highest. This is the specification. |
| `docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md` | The prompt format for full-reference mode. Label types, task-type prefixes, retention markers, the 350–500 word target. | Highest. |
| MiniMax-H3 model card (HuggingFace) | Architecture, input limits, durations, resolutions, aspect ratios, the `<d>` token, the three-field IR schema. | High. |
| MiniMax H3 open-source announcement | Release specs. | High, but marketing register — prefer the guides for anything operational. |

Both guides live under `docs/` in the `MiniMaxAI/MiniMax-H3` repository on HuggingFace.

**The most important thing these documents establish:** the field schema is not a community
convention. `integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music` is the
native output format of the model's own prompt-compiler stage. Writing in it means writing in the
model's intermediate representation directly.

### Secondary — model-adjacent tooling

| Source | What it is | Weight |
|---|---|---|
| `lightx2v` `MiniMax-H3-Prompt-Rewriter-LoRA` template | The prompt template a rewriter LoRA was trained to emit. | High for format questions. It shows what the model expects to receive. |
| Third-party prompt-builder plugins for local runtimes | Independent implementations of the schema as software. | Useful as **corroboration**: where an independent implementer reproduces the field order, task-type prefixes and retention enums exactly, that is real confirmation the schema is stable. Not useful as authority: at least one such tool extends the camera and cut vocabularies well beyond the official lists while describing them as "from the spec". Read the code, not the claims. |

### Tertiary — community practice

| Source | What it is | Weight |
|---|---|---|
| Banodoco Hivemind Discord corpus | ~1.08M messages; the `minimax_h3_chatter` / `_resources` / `_gens` / `_training` channels are the relevant ones. Practitioners reporting real runs. | Medium. Named observers, real outputs, but almost never controlled. |
| `Banodoco/discord-archive` (HuggingFace dataset) | The same corpus as a dataset. | Same. |
| Two community "Custom GPT" knowledge kits | Compiled prompting guidance, checklists, gold examples, a research ledger. | Mixed. The parts that quote the official guides are reliable. The craft layer is invented — see the health warning. |

---

## 3. Health warning

Read this before citing anything from this package as established fact.

**The model had been public for roughly twelve days when this was compiled.** Every community
finding here comes from that window. Nothing has been re-tested after the model's first updates.

**Most `[OBSERVED]` entries rest on a single unrepeated run by a single observer.** Of the observed
findings in the failure catalogue, roughly two-thirds are n=1. They are recorded because a real
observation beats a guess, not because they are settled.

**One frequently-cited batch of twenty animation tests is single-seed and self-rated** on an
undefined scale ("strong", "excellent"), by one author, with no blind evaluation and no control.
Several rules in circulation trace back to it alone. One practitioner in the same corpus states the
methodological objection explicitly — that many prompts and seeds are needed rather than a single
sample — and that objection was never applied to the batch.

**The community kits' craft vocabulary is invented and carries no evidence.** Specifically: the
lettered "pack" identifiers (V01–V24, M01–M08, F01–F08, A01–A08), the thirty named style anchors,
the "exactly one pack per category" budget, "one action beat per 1–3 seconds", "bind 1–3 sound
events", the routing tables, and the 0–25 scoring rubric. None of these appear in any MiniMax or
runtime document. They are decent craft vocabulary presented in the register of a specification.
Nothing in this package depends on them.

**Nobody has measured how H3 handles negation.** The one pure-negation experiment in the corpus has
no reported outcome at all. Chapter 9 of the failure catalogue is therefore the least trustworthy
chapter in this package, and its rules should be read as `[INFERRED]` even where they read
confidently.

**Several widely-reported "prompt failures" are engine bugs.** The most consequential: in one
runtime, attaching any reference silently overwrites every keyframe, so start frames stop working.
People spent days rewording prompts against that. The appendix to the failure catalogue lists the
known cases so you stop trying to fix them with language.

---

## 4. Open questions — what would change this

These are the questions whose answers would most improve the package. Each is genuinely open.

| Question | Why it matters | What would settle it |
|---|---|---|
| Does raw prompt length degrade reference adherence, or only conflicting instruction? | Determines whether the length guidance in `05` is a real constraint or a proxy for something else. | Fixed reference set and fixed scene; generate at 500 / 1500 / 3000 / 6000 characters where the added text is purely elaborative and introduces no new or conflicting instruction. Score reference adherence blind. |
| What is the real character limit, per regime? | The commonly cited 7,000 is uncited and appears to describe the **hosted** service only; locally nothing is enforced and a 30,000-character prompt is reported to have run. Most length advice in circulation silently merges the two regimes. | Binary search the hosted API for the refusal point. Separately, on local weights, hold the scene and references fixed and step length up while scoring adherence blind — the question there is where the gradient becomes costly, not where the gate is. |
| How is negation handled? | An entire chapter rests on inference. | Matched pairs: prohibition-phrased versus positively-phrased end state, same seed, n≥10. |
| Can two distinct voice references bind to two subjects? | Currently blocks any two-hander with referenced voices. | Systematic variation of audio-label binding syntax, dialogue length per speaker, and separation of the two audio files. |
| Do the amplitude/speed modifiers scale, or switch? | Determines whether "small amplitude" is a dial or a mode. | Same shot, same seed, cycling all four combinations. |
| Does shot count itself degrade a clip, or only shot *duration*? | Decides whether the two-shot ceiling is real or an artefact of the example corpus. | Constant total duration, varying cut count from 1 to 5. |
| Does the affirmative-silence phrasing beat `N/A`? | One of the most-repeated pieces of advice, never controlled. | Matched pairs, n≥20, count clips containing unrequested audio. |

---

## 5. Maintenance

**Adding an entry.** Give it an ID in the chapter's existing series, fill all five columns, and
date-stamp it. An entry without a fix written as copyable prompt language is not finished.

**Promoting `[INFERRED]` to `[OBSERVED]`** requires a reported run: what was generated, what came
back, and who ran it. One run is enough to promote, but record `n=1` in the entry.

**Promoting `[OBSERVED]` to a rule you would stake work on** requires either independent
corroboration by a second person, or a controlled comparison with the variable isolated. Record
which.

**Demote freely.** If a finding fails to reproduce, say so in the entry rather than deleting it —
a documented non-reproduction is more useful than a gap.

**Date-stamp everything new.** This model is moving. A finding without a date is unusable in six
months.
