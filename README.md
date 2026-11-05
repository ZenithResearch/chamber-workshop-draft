# Chamber workshop draft

A fresh, independent repository for developing the workshop step by step.

| Page | Content to fill |
|---|---|
| `index.html` | Agenda names, times, descriptions, activity bullets and material links |
| `plans/activity-NN.html` | Activity name, time, summary and ordered outline with slide references |
| `slides/activity-NN.html` | Individual slide records: content notes, facilitator notes, citations and attachments |
| `resources.html` | Shared resource index and full records |

The agenda uses the original nine-row table and native activity drawers. Its rows are placeholders; no activities or times have been selected. The agenda design is retained from the earlier stylesheet at commit `b01e197`; detail-page styles support the record fields.

Plain HTML and CSS; no browser JavaScript, framework, dependencies or build step. Run `python3 -B -u server.py` and visit http://127.0.0.1:8767.

The previous repository remains at `../workshop-agenda`. Reference notes are kept outside this repository at `../Workshop_Reference_Notes_2026-11-04.md`. Neither those notes nor previous workshop content is included in this website. The preview server exposes only the agenda, activity plan/slide pages, shared resources and stylesheet. `STRUCTURE.md` records the logical objects and relationships; it is not served.

An activity can contain multiple slides on its slides page. Activity 1 begins with two empty slide records; the remaining activities each have one empty record to duplicate as needed. These are structural placeholders, not selected workshop content. Each slide has its own facilitator notes and citation fields. Complete resources are recorded once in `resources.html`; citations connect a specific point to a resource and source location, with notes and limits. Attachments remain optional branches with a return to their referring slide.
