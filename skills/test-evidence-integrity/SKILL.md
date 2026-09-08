---
name: "test-evidence-integrity"
description: "Produce trustworthy test and release evidence without hidden gaps."
license: "MIT"
---
# Test Evidence Integrity

## Purpose

Use this skill when test results decide whether a defect is fixed, a candidate can merge, or a release gate passed.

The goal is simple: make the claim no stronger than the proof.

## First decide the risk

Use the full gate for:

- merge or release decisions;
- production or destructive changes;
- cross-repository convergence;
- migrations and live activation.

For a bounded repair on an isolated branch, keep it light:

1. run the focused test;
2. make the repair;
3. run the full required suite once;
4. inspect the worktree;
5. report plainly.

Do not turn a small repair into repeated ceremony.

## Evidence states

Use these words precisely:

- **PASS** — every required proof ran and passed against the exact candidate.
- **BLOCKED** — a required proof is missing or contradicted by current evidence.
- **PARTIAL** — some planned proof ran, but the complete gate did not.
- **INVALID** — the command, runtime, output or artefact cannot support the claim.

A partial or invalid run never becomes a pass by omission.

## Core gate

### 1. Bind the exact candidate

Record:

- base and candidate commit or exact dirty patch identity;
- candidate path and branch;
- clean or fully classified pre-run Git status;
- required test command and runtime.

A commit hash does not identify uncommitted changes.

### 2. Run direct proof

Prefer the direct test command.

Never use `pytest | tail`, `grep`, `tee`, or a later successful command as the pass/fail result unless every gate's exit code is captured separately. A consumer's zero exit code does not repair a failed test command.

If output must be redirected:

1. run the test command;
2. capture its exit code immediately;
3. inspect the saved output afterwards;
4. gate on the captured test exit code.

### 3. Separate collection from execution

Collection proves discovery and imports. Execution proves behaviour.

For a full gate, record both separately. Do not report a suite green from `--collect-only`.

### 4. Prove runtime identity

Use the repository's canonical interpreter and runner.

Record child-side evidence such as `sys.executable` and key dependency versions. Parent environment variables and wrapper banners show intent, not the runtime that actually executed tests.

When candidate and baseline use different runtimes, classify the result as an environment mismatch. Repeat in the same canonical runtime before assigning a source regression.

### 5. Verify independently

An implementer or reviewer summary is a claim. The controller reruns the required proof before accepting a merge, release or fixed-defect claim.

If the controller result conflicts with approval, stop. Preserve the mismatch, repair narrowly, and rerun the proof.

### 6. Inspect post-test residue

Compare Git status before and after tests, including untracked files.

If a lockfile, manifest, cache or generated file changed:

1. preserve it;
2. inspect and classify it;
3. do not clean, stage or commit it merely to make the tree look tidy;
4. establish a stable candidate snapshot;
5. rerun the required proof if the candidate changed.

### 7. Reconcile the gate

A merge or release gate passes only when:

- candidate identity is exact;
- required collection and execution passed;
- the canonical runtime is proven;
- the controller independently verified the result;
- required lanes ran or were explicitly classified;
- the worktree has no unexplained residue.

Passing the local evidence gate does not publish, install or activate anything.

## Special cases

### Stopped or long-running matrices

Before starting, state the lane count, repetitions, time limit and likely cost.

If stopped:

- preserve completed checkpoints;
- state the exact completed and missing lanes;
- label the result **PARTIAL** or **CANCELLED / PARTIAL**;
- block formal selection, promotion or activation.

Completed lanes may support a directional finding. They cannot satisfy an incomplete formal matrix.

### Optional integrations

A clean base skip proves only that the base environment handles absence correctly.

To prove the integration works, run a supported environment with the optional dependency present and execute the real product seam. Until then, report **PARTIAL**.

### Isolated or sharded suites

Treat child exits separately:

- `0`: passed;
- `1`: test failure;
- `2`: collection or import error;
- `5`: no tests collected;
- timeout, signal or another code: runner failure.

A zero exit with a missing or malformed required report is an evidence failure, not a passing shard.

### Baseline attribution

Do not call a failure pre-existing without replaying the same failing set on the immutable base using the same runtime, runner, home and flags.

Compare failing test identities, not unstable traceback text or timing.

## Stop rules

Do not approve the gate when:

- a pipeline masks the test exit code;
- only collection ran;
- the runtime is different or unknown;
- the candidate identity is stale or dirty but unrecorded;
- required lanes are missing;
- the controller did not verify a gating claim;
- test-created residue is unexplained;
- a required report is missing or malformed.

Do not silently retry, repair or restamp historical evidence. Preserve the first result and label later proof separately.

## Report

Lead with the decision:

```text
Verdict: PASS | BLOCKED | PARTIAL | INVALID
Candidate: <exact identity>
Proven: <what directly ran and passed>
Missing or conflicting: <what prevents a stronger claim>
Next action: <smallest proof or repair>
Release state: local only | tagged | published | installed | activated
```

Keep hashes and paths after the plain result.

## Done

The result is complete when another reviewer can tell:

- what candidate was tested;
- what commands ran;
- which runtime ran them;
- every command's real exit status;
- what was skipped or blocked;
- whether tests changed the worktree;
- the strongest claim the evidence supports.
