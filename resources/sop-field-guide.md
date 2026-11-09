# SOP worksheet: source and field guide

This worksheet helps participants describe a recurring task in the Hub's Markdown process format. It is a planning document, not an executable process or an access grant. The facilitator translates and checks the completed worksheet before use in the Hub.

## Source

Based on ZenithResearch/hub at commit `17796093f6bbf766d0a642709d553ae121eb7181`:

- [Process schema and authoring rules](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/base/ops/processes/index.md).
- [Process contract compiler](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/services/cases/contract.py).
- [Contract tests](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/tests/test_process_contract.py).

The compiler and explicit Variables/step rules take precedence over the short introductory example in the process index. This worksheet follows that Hub contract; it does not substitute the separate Process Runtime publication schema.

## Participant use

The worksheet is two landscape pages. Complete the process name, purpose, and information table on page 1. Write up to three steps side by side on page 2, then use the work map on page 1 to plan one run. Leave unused steps and tasks blank. Keep answers short enough to remain visible when printed. For longer processes, use additional copies with continued step and task numbers; when completing digitally, keep additional copies as separate files so repeated form-field names do not overwrite each other. Use extra paper or a separate file if the information table needs more rows. Print at actual size on landscape Letter paper; for duplex printing, flip on the short edge.

Use the same short name for an information item everywhere. Record all inputs and outputs in the information table, including information supplied at the start. A newly created value has one producing step; if a later step changes it, give the changed value a new name. Write missing-data handling, approval points, and checks directly in the step's instructions.

Downloading and opening the PDF in a form-capable reader allows typed answers to be saved. It can also be printed blank or with completed answers. The PDF sends no information to the workshop site.

## Field mapping

| Worksheet prompt | Hub representation | Review needed |
| --- | --- | --- |
| Process name | Top-level `#` title | Use a specific task name. |
| When is it used, and what should it produce? | `## What this process does` | State the purpose, trigger, and intended result in prose. |
| Item name, type, meaning | `## Variables` table: Variable, Type, Description | Include every step input/output. Use unique names in backticks. |
| Source | Facilitation note; root inputs and producer links are derived | Check that each item is available at the start or produced by one earlier step. Do not add a fourth column to the Hub contract. |
| Step number and name | `### Step N -- Title` | Use consecutive, unique step numbers. |
| Person or role | `**Assignee:**` | Translate a role description to the intended assignment. |
| Skill needed | `**Skills:**` | Map a plain description to an existing skill/worker capability; do not treat a description as a registered identifier. |
| Inputs | `**Input:**` | Reference declared information names only. |
| What happens? | `**Processing:**` | Required for every step. Include writes, checks, approvals, and failure handling. |
| Outputs | `**Output (process state):**` | Translate named values to JSON keys matching the Variables table; omit if there are no new values. |
| Required systems or workspaces | `**Required Resources:**` | Declare systems, workspaces, or other non-slot capabilities on the step that uses them. |
| Helpful resources / Optional | `**Suggested Resources:**` | Optional; the step must be able to run without them. |

Types can be written in ordinary language on the worksheet: text -> `string`, number -> `number`, yes/no -> `boolean`, list -> `array`, record -> `object`. Preserve any needed format detail, such as a path or date, during review. These are authoring conventions, not a claim that this compiler enforces every type or business rule.

## DevGraph work map

The right half of page 1 is a planning exercise for one run of the SOP. It uses the [DevGraph workflow contract](https://github.com/ZenithResearch/devgraph/blob/6789e9e754c00339db34801a9c4615fa9276a740/ontology/workflows.md) and [versioned workflow definitions](https://github.com/ZenithResearch/devgraph/blob/6789e9e754c00339db34801a9c4615fa9276a740/ontology/workflows.json), pinned to `6789e9e754c00339db34801a9c4615fa9276a740`. This is a source mapping, not verification of an installed DevGraph service.

| Worksheet box | DevGraph meaning | Facilitation note |
| --- | --- | --- |
| Issue / result | One operational outcome to deliver | Describe this run, such as reviewing today's customer quote. The reusable SOP remains a separate document. |
| Task 1-3 / step 1-3 | Concrete work belonging to the Issue | The connecting tree shows parentage, not execution order. One Task per step is an exercise convention, not a schema requirement. |
| Needs task no. / none | A task dependency | If Task 2 needs Task 1, the dependency points Task 2 -> Task 1. Avoid self-dependencies and cycles. Tasks may run independently. |
| Done when... | Acceptance criterion for that Task | Write an observable check, such as a recorded approval or rejection with a reason. |
| Review / evidence | Supporting Artifact or ExternalLink, and later review evidence | Identify the actual result or check for each Task. A planned check is not evidence that it has passed. |
| Handoff / checker and recipient | Review and handoff planning | The receiving person must be able to use the result. Writing a name does not record a workflow approval. |

For the quote example: the Issue is “Review and record this customer quote.” Task 1 prepares the draft and needs no other task; Task 2 reviews it and needs Task 1; Task 3 saves the draft and decision and needs Tasks 1 and 2. Suitable checks are a draft with scope and price, a decision with a reason, and a saved record that can be opened. Evidence includes the draft, decision, and saved-record path. The manager reviews the result and the office coordinator receives the record.

In the pinned source, Issues and Tasks use `execution.v1`: intake and requirements, baseline, implementation, review, and verified handoff before Done. The worksheet collects planning inputs for that flow; it does not implement the full stage sequence or clear its gates. Workflow stage, progress, parentage, and dependency are separate concepts. Do not mark work Done merely because these boxes are filled. Actual completion requires the applicable approvals, evidence, requirement review, technical clearance, and handoff in DevGraph. These work-map fields do not become Hub Variables or extra process headings.

## Facilitator setup

To keep the participant pages compact, resolve technical setup separately during review: `**Executor:**` is optional and separate from the assignee; `**Tools:**` contains exact registry-backed actions, one per line; `**Toolsets:**` contains optional named groups. Do not infer an executor from a skill name or invent registered identifiers. Retain these declarations on the appropriate Hub step when required by the process.

## Review before use

- Every named input and output appears once in Variables with a type and meaning.
- Each new value has one producer. Inputs are available before their consuming step.
- Every step has explicit Processing instructions.
- Resources and tools are declared on their steps, not as Variables or a global capability block. An application is a resource; an actual file path can be a named information value.
- Writes to a system are described in Processing and use a required resource. Do not use deprecated labels such as `Output (vault)`.
- Skills, tools, assignments, and executors are resolved against the intended environment. Documenting a resource does not authorize access to it.
- The finished Markdown is compiled and reviewed in the target Hub environment before execution. A successful compile does not prove that the work meets business needs.

The [worked example](sop-example.md) shows a small quote-review process using the same fields. It is illustrative and is not a deployed integration.
