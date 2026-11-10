# Working notes — dispatching and harness evolution

Archived exploratory draft, 10 November 2026. This is the research notebook supporting the final workshop study, not the final publication. Its measurements remain a synthetic microbenchmark; prose and proposed next steps are working material.

ZENITH

# Dispatching and harness evolution

Evidence review and reproducible synthetic experiment · 10 November 2026

## Finding

In a deliberately narrow allocation task, shared fields and indexed retrieval reduced the data packaged for execution while preserving the correct disposition on every tested request. This supports reducing unnecessary work through explicit data and tool design. It does not establish that all administration can be automated, that an LLM learns this improvement, or that a business will achieve a particular saving.

**Status:** literature review plus an executed, offline Python microbenchmark. No LLM inference, token bills or production business processes were measured. The previous $10 → $4 → $2 teaching bars have been withdrawn as a basis for claims. No new chart images are included.

## Research questions

- Can a defined service request be dispatched correctly using explicit records, rules and permission checks?

- Can evaluated changes reduce the records inspected and data passed forward without changing the required outcome?

- Which measurements would justify a later claim about token consumption and system cost per correctly completed task?

## Published evidence and its limits

**τ-bench: evaluate outcomes, not plausible responses**

The original benchmark checks resulting database state against the intended state and tests reliability across repeated trials. Its airline and retail simulations motivate outcome checks and repeated evaluation. Its reported 2024 model scores are not acceptance probabilities for our task. [Yao et al., 2024.](https://arxiv.org/abs/2406.12045)

**GEPA: propose, evaluate and retain changes**

GEPA reflects on execution traces to propose and test prompt revisions. Across six tasks, the authors report quality improvements and up to 35 times fewer optimization rollouts than their GRPO comparison. That is an optimization-efficiency result, not a 35-fold reduction in production tokens or a universal learning curve. Our experiment uses manually authored candidates, not GEPA. [Agrawal et al., 2026 revision.](https://arxiv.org/abs/2507.19457v2)

**Hermes: a mechanism for retaining procedures**

Hermes documents on-demand skills, progressive disclosure and editable procedural documents. This is a practical mechanism for reusing instructions and controlling context. Documentation alone does not quantify savings, prove reliability or establish autonomous improvement on our task. [Hermes skills documentation.](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

**Hyper-tau-bench: construction needs its own evaluation**

This 2026 benchmark evaluates building customer-service agents from records, requirements, APIs and an existing codebase under serving constraints, then testing them against held-out simulated users. It reinforces the need to evaluate the resulting system separately from the process that builds it. We do not transfer its scores to this workshop. [Shi et al., 2026.](https://arxiv.org/abs/2609.04611v1)

These sources support the study design. They do not calibrate our synthetic workload or supply a measured business saving.

## Executed experiment

**Task:** Given a service request and a roster, choose an available worker with the requested skill and region. Break ties by lowest workload, then worker ID. Unauthorized or incomplete requests go to review; requests with no eligible worker also go to review. The result is a case-status record, not an externally executed appointment.

**Data:** Four roster sizes (32, 128, 512 and 2,048), three independently seeded rosters per size, and 240 held-out requests per roster: 2,880 unique test cases. The constructed mix is 60% routine, 20% absent skill, 10% missing field and 10% unauthorized. This is a coverage design, not an estimate of business frequencies. Roster records use four skills and eight regions; each worker has one of each. Tasks use independent snapshots, so there is no concurrent booking or state-changing workload.

**Variants:** (A) scan the roster and package full records; (B) scan the same roster and package only decision fields; (C) retrieve the matching skill/region bucket, then scan and package its decision fields. All implement the same selection rule. The full-record baseline deliberately includes verbose irrelevant descriptions; it is not an optimized production baseline.

**Evaluation before retention:** A separate 96-request development set selects among manually authored candidates by minimum mean payload bytes, subject to perfect development correctness. The indexed projection is selected before held-out evaluation. A controlled candidate that ignores availability is rejected by a counterexample. This demonstrates evaluated retention; it is not a measured autonomous evolution trajectory.

**Checks:** An independently implemented filtering-and-sorting oracle supplies the expected case record. Every variant must match it. “Correct” includes appropriate review; it does not mean every service request was assigned. At 2,048 workers, each variant assigns 432 of 720 requests and correctly sends 288 to review.

**Measures:** records visited; serialized UTF-8 JSON payload bytes; local runtime including projection, serialization and decision. Bytes are not tokens. Each variant is timed three times per request after warm-up, in deterministically shuffled order; the per-request median is retained. The table averages these medians. Index construction is excluded from per-request timings and recorded separately; comparisons in the raw results include one build per 240-request batch. Generation and oracle time are excluded equally.

## Measured results

All three variants matched the oracle on 2,880 of 2,880 main test cases each. These finite deterministic tests establish no general LLM success rate or production reliability guarantee.

| Workers | Implementation | Records visited | Payload bytes | Runtime (ms) |
| --- | --- | --- | --- | --- |
| 32 | Full records + scan | 25.6 | 13,690 | 0.0335 |
| 32 | Relevant fields + scan | 25.6 | 1,530 | 0.0138 |
| 32 | Relevant fields + index | 0.6 | 107 | 0.0021 |
| 128 | Full records + scan | 102.4 | 54,586 | 0.1251 |
| 128 | Relevant fields + scan | 102.4 | 5,946 | 0.0503 |
| 128 | Relevant fields + index | 2.5 | 216 | 0.0032 |
| 512 | Full records + scan | 409.6 | 218,401 | 0.4787 |
| 512 | Relevant fields + scan | 409.6 | 23,841 | 0.1971 |
| 512 | Relevant fields + index | 9.6 | 626 | 0.0072 |
| 2,048 | Full records + scan | 1,638.4 | 874,498 | 1.8853 |
| 2,048 | Relevant fields + scan | 1,638.4 | 96,258 | 0.7702 |
| 2,048 | Relevant fields + index | 38.2 | 2,317 | 0.0218 |

The full-record baseline makes the apparent gain large because it repeatedly packages irrelevant descriptions. Comparing projected scan with indexed projection separates the effect of field selection from candidate retrieval. These runtimes measure local Python work, not model latency or elapsed service time.

### Sensitivity checks

At 2,048 workers, remove the descriptions, then concentrate all workers in one skill/region bucket. Each sensitivity uses 80 additional requests; all three variants still match the oracle.

| Condition | Implementation | Records visited | Payload bytes |
| --- | --- | --- | --- |
| No descriptions | Full records + scan | 1,638.4 | 114,290 |
| No descriptions | Relevant fields + scan | 1,638.4 | 96,267 |
| No descriptions | Relevant fields + index | 36.8 | 2,234 |
| One shared bucket | Full records + scan | 2,048.0 | 142,845 |
| One shared bucket | Relevant fields + scan | 2,048.0 | 120,317 |
| One shared bucket | Relevant fields + index | 2,048.0 | 120,317 |

When all workers share the queried bucket, indexed retrieval visits every worker and has the same payload as the projected scan. The benefit depends on selectivity. This negative result prevents a universal “lookup solves the task” claim.

## Complexity: what the experiment does and does not change

Let n be roster size, N the number of requests on an unchanged roster, and k the number of candidates returned for a request. Fixed-size fields and descriptions are assumed here.

- A full scan is Θ(n) per complete request. Removing irrelevant fields reduces serialization work and payload size but does not change this class.

- Building the index takes Θ(n) time and Θ(n) references. A hash lookup is expected O(1) under ordinary hash-table assumptions, followed by Θ(k) candidate work. Including construction, N queries cost expected O(n + N + Σkᵢ). The candidate scan remains O(n) in the worst case.

- With a fixed number of uniformly populated categories, expected k grows proportionally with n. The synthetic improvement therefore reduces constants; it does not demonstrate O(log n) task execution.

- A changed roster needs index maintenance or rebuilding. Rebuilding for every request can erase the query-time advantage. Our static snapshots do not test maintenance, concurrent assignment or stale data.

Nor does a finite process DAG alone bound work within a node. Five human reviews or a compression cap can bound one configured session, but unrestricted redefinition or takeover adds further work. This experiment has no such retry loop; it cannot estimate its probabilities or costs.

## The system-cost model for the next empirical phase

**Comparison assumption:** human cost is a common component across scenarios, held equal at each workload size, including any shared growth with volume. The comparison below isolates computational work and system costs.

**System cost per correctly completed task = counted system costs for the batch ÷ correctly completed tasks.** The numerator includes model calls, tools and infrastructure, plus the compute consumed by evaluation, development and maintenance, each counted once. Include failed attempts and retries. Report completion, correct escalation and incorrect acceptance separately. If no task is correctly completed, the ratio is undefined. A correct escalation must not be silently counted as delivered service.

Price uncached input, cached input and output tokens separately from actual usage records. Record elapsed runtime separately. Compute spent on evolution must be included in cumulative system cost and amortized over a declared volume. Lower bytes do not establish lower billed tokens, fewer calls or lower total system cost.

Track absolute token consumption and its share of system cost separately. A larger token-cost share does not by itself mean more tokens were consumed; this experiment measures neither.

## What a stronger follow-up must measure

- Use the same business outcome, data access and permissions for each workflow, a fixed harness and frozen revised versions. A one-shot model output is comparable only if it achieves the same required result.

- Keep development and final evaluation requests separate. Freeze versions before final evaluation; include exceptions, distribution shifts and changed business rules.

- Log model/version, prompt and tool versions, input/cached/output tokens, latency, tool actions, retries, compression and takeover events, and final state. Count development experiments that fail as well as those retained.

- Use paired requests, repeated model runs and independent outcome checks. Report uncertainty across requests and environments; choose the sample size from pilot variation and the smallest useful effect. Three synthetic roster seeds are not a broad confidence interval.

- Accept an efficiency claim only at comparable quality and coverage. A cheaper harness that misses constraints or escalates more often may not be an improvement.

## Implication for the workshop

The defensible message is: explicit data and tools make a bounded administrative procedure executable; evaluation can show which changes preserve its result while reducing work. The experiment supports those mechanisms in one synthetic task. It does not justify “all admin work is automated,” the withdrawn dollar bars or a guaranteed reduction in tokens per task.

Future visuals should show measured payload and record counts as such, distinguish runtime from cost, and include the concentrated-roster counterexample. Token and system-cost charts must wait for the corresponding measurements.

## Reproduce and inspect

From the workshop repository, run `python3 research/dispatch-study/run.py`. Python standard library only; no credentials, network or paid inference. Deterministic data and operation counts should reproduce; timings will vary with hardware and load. A rerun overwrites the result files; retain a copy before comparing runs.

[Source](dispatch-study/run.py) · [Protocol](dispatch-study/protocol.json) · [Development selection](dispatch-study/selection.json) · [Raw trials](dispatch-study/trials.csv) · [Results and environment](dispatch-study/results.json)

Source SHA-256: `cb99d9efd89b4f86974ffa769be8a3002ab45d46f19bc8fd243950b6dc973fe3`. The result JSON records software, hardware platform, individual index-build timings and sensitivity checks.
