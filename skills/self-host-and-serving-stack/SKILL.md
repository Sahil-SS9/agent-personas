---
name: "self-host-and-serving-stack"
description: "Stand a decision model up locally and prove the deployment matches the benchmark, including which conversion path puts the decision head where."
license: "MIT"
---

# Self host and serving stack

## When to use
Latency, cost, retention or determinism requires local serving.

## Procedure
1. Choose the runtime for the family: a dedicated compiler for typed-decision models, an encoder server with a classification route, or a general inference server with a classify mode.
2. Establish which serving path the conversion uses and where the decision head lives. Some conversions keep the backbone as a standard encoder and read the head from a sibling weights file outside the runtime. Others compile the whole model, baking the decision recipe into the artefact itself.
3. Verify the artefact carries what the runtime expects before serving.
4. Measure end-to-end latency per decision on your hardware, not per token.
5. Confirm outputs match the hosted reference for identical inputs.

## Decision rules
- Do not assume a GGUF built for one runtime loads in another. Compiler-produced artefacts are their own format.
- Publish end-to-end per-decision latency, since that is the falsifiable claim users care about.
- A local model that agrees with the reference but takes 40x the budget has not solved the problem.
- Keep the serving path identical to the benchmarked path, or re-benchmark.

## Pitfalls
- Assuming every GGUF is loadable by the standard runtime.
- Missing a required sibling head file and concluding the model is broken.
- Measuring model time and reporting it as end-to-end time.

## Done
The model serves locally, the decision head is located and documented for that path, and measured latency and agreement with the reference are recorded.
