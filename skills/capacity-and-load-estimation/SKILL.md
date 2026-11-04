---
name: "capacity-and-load-estimation"
description: "Size a design with back-of-the-envelope numbers: QPS, peak, storage, bandwidth, IOPS, memory, nodes and LLM tokens, from stated assumptions, with a bundled deterministic calculator."
license: "MIT"
---

# Capacity and load estimation

Estimates decide the design: they show which resource binds (IOPS, memory, network, CPU, provider limits, GPU memory) and whether you need to distribute at all. Rough but honest beats precise but invented.

## 1. Method
1. List assumptions with units, each traced to the assumptions register.
2. Derive per operation: average QPS = DAU x actions per user per day / 86,400; peak = average x peak factor (2 to 3 unless measured; spiky products more).
3. Storage per day = writes per day x bytes per write (by object type); over retention; x replication factor; plus indexes and overhead (round up).
4. Bandwidth = QPS x payload x 8 bits, in and out separately, at peak.
5. Compare each figure with what one machine does (disk IOPS, RAM, NIC, CPU) and with external limits (provider quotas). Name the binding constraint.
6. Nodes = peak load / (per-node capacity x target utilisation), then add headroom to survive losing one failure domain (with 3 zones, x 3/2).
7. Iterate: if the design changes, recompute.

Use scientific notation for long chains (5e5/s x 8.64e4 s x 2e3 B = 8.64e13 B = 86.4 TB/day). Round assumptions up early so limits are not discovered late.

## 2. Reference magnitudes
- 1 day ~ 1e5 s; 1M requests/day ~ 12 req/s average.
- Memory reference ~100 ns; 1 MB from memory ~250 us; datacentre round trip ~0.5 ms; HDD seek ~10 ms; 1 MB from HDD ~30 ms; cross-continent round trip ~150 ms. SSDs reach tens of thousands of IOPS; HDDs a few hundred.
- Fan-out multiplies tail latency: if each server is slow 1% of the time, a request touching 100 servers is slow 63% of the time.
- Downtime: 99.9% ~ 8.8 h/year; 99.99% ~ 53 min/year.

## 3. Start with one machine
Estimate the single-machine design first. Many workloads fit; a competent single-node design often beats a distributed one until the numbers say otherwise. Distribute for a named reason (binding resource, availability, latency to users), never by default.

## 4. LLM workloads
Plan in tokens, not requests: input and output tokens per request, requests per second at peak, time to first token and time per output token targets. Throughput is bounded by accelerator memory for the KV cache (grows with context length x concurrency), so long contexts cut concurrency. Cost per request = input tokens x input price + output tokens x output price; cost per day at average load.

## 5. Calculator
`python3 scripts/capacity_estimate.py assumptions.json [--markdown]` derives QPS, peak, storage, bandwidth, nodes with failure-domain headroom, and LLM tokens, replicas and cost from a JSON of assumptions (example in `templates/estimate-input.example.json`). Every output row shows its formula. It refuses missing or invalid assumptions and warns on peak factors below 1.5, single-copy storage, no failure-domain headroom and very long contexts. Known-answer tests: `python3 -m unittest scripts/test_capacity_estimate.py`.

## Pitfalls
- Using average QPS for capacity; forgetting replication and indexes; mixing bits and bytes; daily vs per-second slips.
- Quoting QPS when the cost driver is something else (bytes scanned, fan-out, tokens).
- Presenting estimates as facts: label them and the assumptions they rest on.
