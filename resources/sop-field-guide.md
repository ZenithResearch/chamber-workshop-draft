# SOP worksheet: source and field guide

This worksheet helps participants describe a recurring task in the Hub's Markdown process format. It is a planning document, not an executable process or an access grant. The facilitator translates and checks the completed worksheet before use in the Hub.

## Source

Based on ZenithResearch/hub at commit `17796093f6bbf766d0a642709d553ae121eb7181`:

- [Process schema and authoring rules](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/base/ops/processes/index.md).
- [Process contract compiler](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/services/cases/contract.py).
- [Contract tests](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/tests/test_process_contract.py).

The compiler and explicit Variables/step rules take precedence over the short introductory example in the process index. This worksheet follows that Hub contract; it does not substitute the separate Process Runtime publication schema.

## Participant use

Complete the process name, purpose, and information table on page 1. Use pages 2-4 for three steps. Leave unused step pages blank. For longer processes, use additional copies with continued step numbers; when completing digitally, keep additional copies as separate files so repeated form-field names do not overwrite each other. Use extra paper or a separate file if the information table needs more rows.

Use the same short name for an information item everywhere. Record all inputs and outputs in the information table, including information supplied at the start. A newly created value has one producing step; if a later step changes it, give the changed value a new name. Write missing-data handling, approval points, and checks directly in the step's instructions.

Downloading and opening the PDF in a form-capable reader allows typed answers to be saved. It can also be printed blank or with completed answers. The PDF sends no information to the workshop site.

## Field mapping

| Worksheet prompt | Hub representation | Review needed |
| --- | --- | --- |
| Process name | Top-level `#` title | Use a specific task name. |
| What does this process do? | `## What this process does` | State the purpose, trigger, and intended result in prose. |
| Item name, type, meaning | `## Variables` table: Variable, Type, Description | Include every step input/output. Use unique names in backticks. |
| Source | Facilitation note; root inputs and producer links are derived | Check that each item is available at the start or produced by one earlier step. Do not add a fourth column to the Hub contract. |
| Step number and name | `### Step N -- Title` | Use consecutive, unique step numbers. |
| Who does the work? | `**Assignee:**` | Translate a role description to the intended assignment. |
| Skill needed | `**Skills:**` | Map a plain description to an existing skill/worker capability; do not treat a description as a registered identifier. |
| Inputs | `**Input:**` | Reference declared information names only. |
| What happens in this step? | `**Processing:**` | Required for every step. Include writes, checks, approvals, and failure handling. |
| Outputs | `**Output (process state):**` | Translate named values to JSON keys matching the Variables table; omit if there are no new values. |
| Required resources | `**Required Resources:**` | Declare systems, workspaces, or other non-slot capabilities on the step that uses them. |
| Suggested resources | `**Suggested Resources:**` | Optional; the step must be able to run without them. |
| Executor | `**Executor:**` | Optional setup field, separate from the assignee. Do not infer an executor from a skill name. |
| Tools | `**Tools:**` | Use exact registry-backed tool names, one entry per line. |
| Toolsets | `**Toolsets:**` | Optional named tool groups. |

Types can be written in ordinary language on the worksheet: text -> `string`, number -> `number`, yes/no -> `boolean`, list -> `array`, record -> `object`. Preserve any needed format detail, such as a path or date, during review. These are authoring conventions, not a claim that this compiler enforces every type or business rule.

## Review before use

- Every named input and output appears once in Variables with a type and meaning.
- Each new value has one producer. Inputs are available before their consuming step.
- Every step has explicit Processing instructions.
- Resources and tools are declared on their steps, not as Variables or a global capability block. An application is a resource; an actual file path can be a named information value.
- Writes to a system are described in Processing and use a required resource. Do not use deprecated labels such as `Output (vault)`.
- Skills, tools, assignments, and executors are resolved against the intended environment. Documenting a resource does not authorize access to it.
- The finished Markdown is compiled and reviewed in the target Hub environment before execution. A successful compile does not prove that the work meets business needs.

The [worked example](sop-example.md) shows a small quote-review process using the same fields. It is illustrative and is not a deployed integration.
