---
name: "arxiv"
description: "Search arXiv papers by keyword, author, category, or ID."
license: "MIT"
---
# Arxiv

## When to use
Search arXiv papers by keyword, author, category, or ID.

## Method
1. Translate the research question into keywords, author names and subject categories. Search the official arXiv interface or API and record the query and date.
2. Capture identifier, version, title, authors, abstract and submission/update dates. Deduplicate by paper identifier while preserving meaningful version changes.
3. Screen abstracts for relevance, then read the paper before attributing results beyond the abstract. Distinguish preprints from peer-reviewed claims.
4. Record experimental setting, baselines, metrics, limitations and availability of code or data. Do not invent citations, acceptance status or reproducibility.
5. Respect current API usage guidance and cache repeated requests. Sources: https://info.arxiv.org/help/api/index.html and https://arxiv.org/.

## Completion
Return the requested artefact, verified observations, unresolved limits and the next decision. Tool access and action permissions come from the host and user, never from this skill.
