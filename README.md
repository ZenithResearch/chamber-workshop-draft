# Chamber workshop draft

Plain HTML and CSS, with the original Times-and-navy agenda and native activity drawers. No browser JavaScript. Local serving needs no build step. Run `python3 -B -u server.py` and visit http://127.0.0.1:8767.

For a phone on the same Wi-Fi, run `python3 -B -u server.py --host YOUR_LOCAL_IP` and open `http://YOUR_LOCAL_IP:8767`. The server still serves only the explicitly listed workshop files.

- `index.html`: agenda and concise activity outlines.
- `plans/activity-NN.html`: activity summary and outline linking directly to each slide.
- `slides/activity-NN.html`: first slide of an activity; additional slides use `activity-NN-slide-NN.html`. Each page shows only the slide and simple navigation.
- `notes/activity-NN.html`: readable facilitator notes and citations, separate from the slides.
- `resources.html`: shared supporting works.

Welcome and Foundations each have seven populated draft slides. Demo has its agreed summary and notes. Exercise has a short outline linking to six slides, including SOP creation; its SOP template and prepared example remain proposed materials to prepare. Timing is to determine; Looking Forward has six draft slides; Questions has five. Both retain their agreed outlines and proposed resources. The OECD report remains a proposed source, with detailed citation passages pending.

The old `../workshop-agenda` repository is unchanged. Reference notes remain outside this site at `../Workshop_Reference_Notes_2026-11-04.md`.

The agenda contains six activities: Welcome, Foundations, Demo, Exercise, Looking Forward and Questions. Unused placeholder slide and notes pages still exist for some of these activities, but are not linked from the agenda.

Navigation is checked with python3 -B check_navigation.py. Every served detail page has one sticky “Back to agenda” link; slide Previous/Next, outline and resource links stay available. External readings open in another tab so the workshop remains open.

## Hosting

Live site: https://chamber-workshop-draft.vercel.app

Hosted on Vercel under ZenithResearch, project chamber-workshop-draft. The GitHub repository remains private; the deployed workshop pages are public.

To publish an update from this repository:

    vercel link --yes --project chamber-workshop-draft --scope zenith-research
    python3 -B build_static.py
    vercel deploy --prebuilt --prod --yes --scope zenith-research

The packager runs the navigation check and copies only server.py's allowlisted HTML and CSS into the ignored .vercel/output/static directory. Python source, repository documentation and reference notes are excluded. Deployment preserves the no-script content security policy and direct .html links.

Deployments are manual. Vercel could not connect the private GitHub repository during setup, so pushing to GitHub alone does not publish changes.
