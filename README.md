# Chamber workshop draft

Plain HTML and CSS, with the original Times-and-navy agenda and native activity drawers. No browser JavaScript or build step. Run `python3 -B -u server.py` and visit http://127.0.0.1:8767.

For a phone on the same Wi-Fi, run `python3 -B -u server.py --host YOUR_LOCAL_IP` and open `http://YOUR_LOCAL_IP:8767`. The server still serves only the explicitly listed workshop files.

- `index.html`: agenda and concise activity outlines.
- `plans/activity-NN.html`: activity summary and outline linking directly to each slide.
- `slides/activity-NN.html`: first slide of an activity; additional slides use `activity-NN-slide-NN.html`. Each page shows only the slide and simple navigation.
- `notes/activity-NN.html`: readable facilitator notes and citations, separate from the slides.
- `resources.html`: shared supporting works.

Welcome and Foundations each have seven populated draft slides. Demo has its agreed summary and notes. Exercise has a short outline linking to six slides, including SOP creation; its SOP template and prepared example remain proposed materials to prepare. Timing is to determine; Looking Forward and Questions have their agreed outlines and proposed resources. The OECD report remains a proposed source, with detailed citation passages pending.

The old `../workshop-agenda` repository is unchanged. Reference notes remain outside this site at `../Workshop_Reference_Notes_2026-11-04.md`.

The agenda contains six activities: Welcome, Foundations, Demo, Exercise, Looking Forward and Questions. Unused placeholder slide and notes pages still exist for some of these activities, but are not linked from the agenda.
