---
name: "ai-systems-rag-architecture"
description: "AI and LLM systems: design retrieval-augmented generation as a system: ingestion and indexing pipeline, permission-aware retrieval, hybrid search and reranking, context assembly, freshness, and the seven RAG failure points."
license: "MIT"
---

# AI systems: RAG architecture

Sub-category: AI and LLM systems. Prompt-level retrieval tuning belongs to the Prompt/Agent Engineer; this skill designs the system around it.

## 1. Ingestion and indexing pipeline
Sources -> extraction (text, tables, scans) -> cleaning -> chunking (by structure and meaning, sized for the queries) -> metadata (source, owner, date, permissions, version) -> embeddings and keyword index -> store. Design it like any data pipeline: incremental updates, deletes that reach the index, re-embedding when the model changes, lineage back to the source document, and a freshness SLO ("changes searchable within 15 minutes").

## 2. Permission-aware retrieval
The index is a copy of protected data. Filter by the caller's permissions at query time (or partition indexes per tenant); never rely on the prompt to hide documents. Keep tenants' vectors isolated; treat retrieved text as untrusted input (it can carry injected instructions).

## 3. Retrieval quality
Hybrid retrieval (keyword plus embeddings) beats either alone for many corpora; add a reranker for precision; query rewriting for conversational follow-ups; structured data via SQL or APIs rather than embeddings.

## 4. Context assembly
Fewer, better passages beat many: models use the start and end of long contexts better than the middle, and more documents do not steadily help. Put the strongest evidence first, dedupe, keep within a token budget, and carry citations through to the answer.

## 5. Design against the seven failure points
| Failure point | Design response |
|---|---|
| Missing content (answer not in corpus) | Detect low retrieval scores; answer "not found" and log the gap |
| Missed top-ranked documents | Hybrid retrieval, reranking, tuned top-k |
| Not in context (dropped during assembly) | Context budget and ordering rules |
| Not extracted (in context, model misses it) | Less noise, contradiction handling, extraction prompts |
| Wrong format | Structured output with validation |
| Incorrect specificity | Clarifying questions, audience-aware prompts |
| Incomplete answers | Multi-part question decomposition |
RAG can only be fully validated in operation with real questions: plan logging of queries, retrieved ids and outcomes, and a feedback loop to fix gaps.

## 6. Capacity and cost
Index size (chunks x embedding dimension x bytes), embedding cost for initial load and updates, query latency budget split across rewrite, retrieval, rerank and generation.

## Output
RAG design: pipeline, store choice, permission model, retrieval stack, context rules, freshness SLO, failure-point table, evaluation and monitoring plan.

## Pitfalls
- Embedding everything once and never handling updates or deletes.
- Shared indexes that leak documents across tenants or roles.
- Blaming the model when retrieval never surfaced the answer.
