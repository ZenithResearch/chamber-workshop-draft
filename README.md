# Chamber workshop draft

Plain HTML and CSS, with the original Times-and-navy agenda and native activity drawers. No browser JavaScript or build step. Run `python3 -B -u server.py` and visit http://127.0.0.1:8767.

For a phone on the same Wi-Fi, run `python3 -B -u server.py --host YOUR_LOCAL_IP` and open `http://YOUR_LOCAL_IP:8767`. The server still serves only the explicitly listed workshop files.

- `index.html`: agenda and concise activity outlines.
- `plans/activity-NN.html`: activity summary and outline linking directly to each slide.
- `slides/activity-NN.html`: first slide of an activity; additional slides use `activity-NN-slide-NN.html`. Each page shows only the slide and simple navigation.
- `notes/activity-NN.html`: readable facilitator notes and citations, separate from the slides.
- `resources.html`: shared supporting works.

Welcome and Foundations each have seven populated draft slides, including the Foundations closing summary. Foundations slide text mirrors its facilitator notes; Welcome slides expand the supplied outline, with separate notes retained. Timing is to determine; other activity slots remain blank. The OECD report remains a proposed source, with detailed citation passages pending.

The old `../workshop-agenda` repository is unchanged. Reference notes remain outside this site at `../Workshop_Reference_Notes_2026-11-04.md`.
