---
name: "rag-retrieval-design"
description: "Design retrieval-augmented generation: chunking, retrieval quality and grounding."
license: "MIT"
---

# RAG & Retrieval Design

Garbage retrieval in, confident hallucination out.

## 1. Retrieval quality is the lever
- Most RAG failures are retrieval failures, not generation failures; measure retrieval first.
- Chunk by meaning, size for the query, and keep metadata for filtering.

## 2. Ground and cite
- Instruct the model to answer only from retrieved context and to cite it.
- Handle "not in context" explicitly; don't let it fill gaps from parametric memory.

## 3. Evaluate the pipeline
- Measure retrieval hit-rate and answer faithfulness separately.
- Tune chunking/embedding/top-k against a real query set, not vibes.

## Voice
Retrieval-first. Refuse blaming the model when the retriever never surfaced the answer.
