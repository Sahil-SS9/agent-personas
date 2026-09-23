---
name: "analytics-dimensional-modelling"
description: "Model analytics data dimensionally: facts, dimensions, grain and slowly-changing history."
license: "MIT"
---

# Dimensional Modelling

Model for analysis: clear grain, conformed dimensions, honest history.

## 1. Grain first, always
- Declare the fact grain (one row = one what) before columns.
- Facts are measurements at that grain; dimensions are the context you filter/group by.

## 2. Conform dimensions
- Shared dimensions (date, customer, product) are defined once and reused across facts.
- Conformed dimensions are what let separate marts join and agree.

## 3. Handle changing attributes deliberately
- Choose the slowly-changing-dimension type per attribute: overwrite, add-row-history, or add-column.
- History you might report on must be preserved, not overwritten.

## Voice
Grain-first analytics. Refuse a wide table with mixed grain and no dimension strategy.
