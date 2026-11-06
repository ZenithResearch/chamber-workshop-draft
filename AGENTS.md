# AGENTS.md

Guide for agents reading or maintaining the Victoria Chamber Workshop site. For a human introduction, see [README.md](readme.html).

## Purpose and scope

This site is a draft workshop package: an agenda, activity outlines, presentation drafts, facilitator notes and supporting resources. Its audience is Chamber members exploring manageable AI adoption, data strategy, operational efficiency, competitive advantage and control over software dependencies.

The guiding domains are self-sovereignty, efficiency and verifiability. Intended participant outcomes are hands-on experience, a useful business decision and a practical next experiment. These describe the workshop's intent; they are not evidence of delivery or measured results.

## Objects and relationships

- **Workshop:** the overall learning event, defined by its audience, purpose and intended outcomes. It has one agenda and a shared collection of resources.
- **Agenda:** the ordered view of the workshop's activities. The main table presents activity summaries, time allocations and attendee resources.
- **Activity:** one coherent part of the workshop. The current sequence is Welcome, Foundations, Demo, Exercise, Looking Forward and Questions. Each activity has an agenda entry and an activity plan; it may have slides and facilitator notes.
- **Agenda entry:** the compact view of an activity in the table. Its drawer exposes the outline and activity resources. It represents the activity; it is not a separate activity.
- **Activity plan / outline:** the description of what an activity is intended to cover. Depending on the activity, it includes summary, business relevance, intended outcome, bulleted plan, evidence of success, time and resources. Demo uses the agreed shorter summary and notes. An outline is not an execution record.
- **Slide:** one presentation unit belonging to an activity, with a title, supplied content and navigation. A slide is a separate HTML page; Previous and Next express presentation order. Demo is delivered through a shared screen rather than a demo link.
- **Facilitator notes:** a separate readable page for delivery guidance, context and supporting citations, organized around an activity's slides or topics. Notes are distinct from the audience-facing slides.
- **Resource:** a supporting work or material, such as a repository, publication, guide, template or worksheet. One resource may support several activities or slides. Activity resources support preparation and delivery; attendee resources are the selection intended for participants.
- **Repository:** a resource containing source code, specifications or documentation. A link identifies the source project; it does not establish installation readiness, integration compatibility or the scope of demonstrated capabilities.
- **Citation:** a specific use of a resource to support a claim. It should identify the claim and the relevant source location, with qualifications where needed. A general resource link or proposed reading is not a completed citation.
- **Attachment:** optional supporting context branched from a slide, with a return to that slide. This is a retained content concept; the current site has no attachment pages.
- **Evidence of success:** the observation or participant result proposed for assessing an activity. A success criterion is not a claim that the result has occurred.
- **Status:** the maturity of content or supporting material. Draft, To prepare and To determine describe unfinished work; an existing file may still be a placeholder.

## Where to read

- Agenda: activity order, summaries and drawers.
- Activity plans: plans/activity-01.html through plans/activity-06.html. Follow each activity's Outline or Plan link.
- Slides: slides/activity-NN.html is the first slide; subsequent pages use slides/activity-NN-slide-SS.html. Use the links in the outline to select a topic.
- Facilitator notes: notes/activity-NN.html. Welcome and Foundations have populated notes; other unlinked notes files are placeholders.
- [Resources](resources.html): shared materials, repository links and preparation status.
- [Readable human guide](readme.html): navigation and current content status.

Use the agenda as the entry point. Do not infer inclusion from a filename alone: some unlinked placeholder files remain. Every detail page must keep a direct Back to agenda link. External resources open in a separate tab.

## Editing rules

- This is a fresh workshop draft. Develop its content with the user step by step.
- Preserve the original Times-and-navy agenda design and native activity drawers.
- Keep unspecified agenda names, times, activities and resources blank.
- Keep reference notes, personal statements, research hypotheses and planning commentary outside the website unless the user explicitly asks to include selected content.
- Use plain HTML and CSS. No browser JavaScript at this stage.
- Do not use the Sites skill or Sites plugin.
- The older `../workshop-agenda` repository is separate; do not change it while working here.
- Preserve the distinction between proposed content, implemented source and verified installed behavior. Do not promote status without evidence.
- Keep README.md and this guide current when the site's contents or navigation change. Their HTML views are generated by render_guides.py.
