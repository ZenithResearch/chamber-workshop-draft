# SOP worksheet: source and field guide

This worksheet helps participants describe a recurring task in the Hub's Markdown process format. It is a planning document, not an executable process or an access grant. The facilitator translates and checks the completed worksheet before use in the Hub.

## Source

Based on ZenithResearch/hub at commit `17796093f6bbf766d0a642709d553ae121eb7181`:

- [Process schema and authoring rules](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/base/ops/processes/index.md).
- [Process contract compiler](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/services/cases/contract.py).
- [Contract tests](https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/tests/test_process_contract.py).

The compiler and explicit Variables/step rules take precedence over the short introductory example in the process index. This worksheet follows that Hub contract; it does not substitute the separate Process Runtime publication schema.

## Participant use

Print the single page on landscape Letter paper, or open it in a form-capable PDF reader, type in the boxes, and save a copy. The PDF sends no information to the workshop site.

Choose a familiar recurring task. Write the desired result and what starts the work. Fill in First, Next, and Then with short phrases. Leave unused steps blank. Finish with a result check, a reason to stop and ask for help, and the people who check and receive the result. The arrows make a simple sequence visible. For a branching or longer process, sketch the additional steps on separate paper and review them with the facilitator.

The participant page deliberately omits schema terms, the Variables table, and a second copy of the task plan. It is a starting draft. The facilitator confirms the missing detail and translates it into the Hub contract before use.

## Hub field mapping

| Worksheet prompt | Hub representation | Facilitator follow-up |
| --- | --- | --- |
| A task I do often | Top-level `#` title | Confirm a specific process name. |
| The result I want; When do you start? | `## What this process does` | Combine the purpose, trigger, and intended result. |
| First / Next / Then | `### Step N -- Title` | Derive a short title from each action and confirm the order. |
| Who does it? | `**Assignee:**` | Resolve the intended person or role. Confirm skills separately. |
| What do they do? | `**Processing:**` | Expand short phrases into usable instructions, including writes, decisions, and checks. |
| What do they need? | `**Input:**`, step resources, skills, or tools, depending on the answer | Separate information from systems, workspace access, abilities, and actions. Do not copy this mixed answer into a single schema field. Ask which resources are required and which are merely helpful. |
| What do they pass on? | `**Output (process state):**` for new information | Identify the actual named values and their contents. A system or workspace is a resource, not an output variable. Use no output block if the step produces no new value. |
| Check the result | Checks in the relevant step's Processing | Confirm observable evidence and any approval needed before the next step. |
| If something goes wrong | Failure handling in the relevant step's Processing | Confirm where to stop, who to ask, and how to resume. |
| Hand it over | Review and delivery instructions in the relevant step's Processing | Confirm the reviewer, recipient, and access to the result. |

Build the exhaustive `## Variables` table with the participant after reviewing the steps. Give every input and output a unique name, type, and description; distinguish information available at the start from information produced by a step. Each new value has one producer. If a later step changes it, give the changed value a new name. Use these same names in Input references and Output JSON keys. Never infer an unknown type or missing information without confirmation.

Ordinary type descriptions can be translated as text -> `string`, number -> `number`, yes/no -> `boolean`, list -> `array`, and record -> `object`. Preserve needed format details, such as a path or date. These are authoring conventions, not a claim that the compiler enforces every business rule.

## DevGraph mapping

The connected step boxes preserve a simple work-planning exercise without putting DevGraph vocabulary on the participant page. This mapping uses the pinned [workflow contract](https://github.com/ZenithResearch/devgraph/blob/6789e9e754c00339db34801a9c4615fa9276a740/ontology/workflows.md) and [workflow definitions](https://github.com/ZenithResearch/devgraph/blob/6789e9e754c00339db34801a9c4615fa9276a740/ontology/workflows.json), at commit `6789e9e754c00339db34801a9c4615fa9276a740`. It describes source behavior, not a verified installed service.

- Use the desired result to frame an Issue for one specific run. Keep the reusable SOP as a separate document.
- Each action box can become a Task belonging to that Issue. One Task per step is an exercise convention, not a schema requirement.
- The printed arrows show the order of work and handoffs. They are not literal DevGraph dependency arrows: when Task 2 needs Task 1, the dependency points Task 2 -> Task 1. Confirm each dependency from what a step needs and what an earlier step supplies; do not infer a dependency solely from the layout. Independent work can run in parallel.
- Turn the result check into explicit acceptance criteria for the relevant work. Ask what actual document, result, or check provides evidence. Planned checks do not prove completion.
- Use the final two boxes to discuss blockers, review, and handoff. A written reviewer name does not record approval, and filling the worksheet does not mark a Task Done.

The pinned execution workflow requires requirements and a baseline before implementation, followed by review and verified handoff. The worksheet gathers starting information for this flow; it does not implement its stages or clear its gates. Confirm per-task criteria, applicable approvals, evidence, technical clearance, and handoff in DevGraph before completion. DevGraph planning fields do not become extra Hub headings or Variables.

For the quote example: First prepares a draft using request details and a price list; Next reviews the draft and records a decision; Then saves the draft and decision. The manager checks the decision, and the office coordinator receives the record. Useful evidence is a draft with scope and price, a decision with a reason, and a saved record that opens successfully.

## Facilitator setup and review

- Resolve skill descriptions to existing `**Skills:**` capabilities. Confirm an optional `**Executor:**` separately from the assignee.
- Declare `**Required Resources:**` and optional `**Suggested Resources:**` on the steps that use them. Documenting a resource does not authorize access.
- Use exact registry-backed names for `**Tools:**` and optional `**Toolsets:**`; do not invent identifiers.
- Confirm every named input/output appears once in Variables. Check that all inputs are available before use and each new value has one producer.
- Every step must have explicit Processing instructions. Describe writes there and declare the required resource. Do not use deprecated labels such as `Output (vault)`.
- Compile and review the finished Markdown in the target Hub environment before execution. Successful compilation does not prove that the process meets business needs.

The [worked example](sop-example.md) shows the expanded Hub contract for a quote-review process. It is illustrative and is not a deployed integration.
