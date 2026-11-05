# Workshop content structure

This records the logical objects supplied by Gabriel. They can share HTML pages; they do not require a database or browser JavaScript.

| Object | Definition | Relationship |
|---|---|---|
| Workshop | Event, audience, purpose and intended outcomes | Has an agenda and a shared resource collection |
| Agenda | Ordered overview | Presents an entry for each activity |
| Activity | A coherent part of the workshop | Has a name, time, summary and plan |
| Plan | The activity’s ordered outline | Organizes talking points, slide references and facilitator notes |
| Slide | One presentation unit | Has a title and content notes; belongs to an activity; several slides can belong to one activity |
| Facilitator notes | Guidance associated with a slide | What it needs to show; what the audience should take from it; citations and contextual notes |
| Resource | A complete supporting publication, guide, repository, tool, documentation set or worked example | Recorded once; can support several activities, slides and citations |
| Citation | A particular use of a resource to support a point | Records the point, source location, relevant notes, qualifications and limits |
| Attachment | An optional branch from a slide | Links to supporting material and provides a return to the referring slide |

An agenda entry is the compact presentation of an activity’s name, time and summary. Attendee resources are the attendee-facing selection from the workshop’s shared collection.

## Page mapping

| Page | Records |
|---|---|
| `index.html` | Agenda entries, concise activity outlines and navigation |
| `plans/activity-NN.html` | Activity name/time/summary and ordered outline with slide references |
| `slides/activity-NN.html` | Multiple slide records, each with its content notes, facilitator notes, citations and attachment links |
| `resources.html` | Shared resource index and full resource records |

## Record fields

**Slide:** activity, title, content to include, what it needs to show, what the audience should take from it, linked resources, citations and relevant notes, attachments.

**Resource:** title, type, source/publisher, link, date/version, description, audience, supported activities/slides and status.

**Citation:** supported point, linked resource, section/page/passage, contextual notes, qualifications and limits. Its location is the associated slide or talking point.

The resource is the complete supporting work. A citation records a particular use of it; creating a citation does not create another copy of the resource record.
