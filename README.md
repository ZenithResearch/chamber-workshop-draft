# README.md

A guide to the Victoria Chamber Workshop draft for reviewers, facilitators and participants.

The workshop explores manageable AI adoption, data strategy, operational efficiency, competitive advantage and control over software dependencies. Self-sovereignty, efficiency and verifiability guide the discussion. The intended outcome is practical experience, a useful business decision and a next experiment.

## Start with the agenda

Open the agenda using Back to agenda and expand an activity to see its outline and resources. The current order is Welcome, Foundations, Demo, Exercise, Looking Forward and Questions.

- **Plan / Outline:** read what the activity is intended to cover.
- **Slides:** open the first slide, or select a topic directly from the outline. Previous and Next move through the activity.
- **Facilitator notes:** read the separate delivery notes where provided. Welcome and Foundations have populated notes.
- **Activity resources:** find supporting materials for preparation and delivery, including relevant repositories.
- **Attendee resources:** find materials intended for participants.
- **Back to agenda:** return to the overview from any detail page. External resources open in a new tab so the workshop stays open.

For an overview of supporting materials, use [Resources](resources.html). Agents can use [AGENTS.md](agents.html) for object definitions, page relationships and editing rules.

## What is ready to review

Welcome and Foundations each have seven populated draft slides and separate notes. Demo has an outline for a shared-screen demonstration. Exercise has an outline and six draft slides. Looking Forward has an outline and six draft slides; Questions has an outline and five draft slides.

The whole package remains a draft. Timings are To determine. Materials marked To prepare are not yet available, including the SOP template and Five Activities worksheet. The OECD reading is proposed; detailed citation passages remain to be selected. Repository links provide source references without establishing that installation or integration has been verified.

Use the agenda links to review the intended package. Some unlinked slide and notes files remain as placeholders.

## For maintainers

This repository uses plain HTML and CSS, the Times-and-navy design and native activity drawers. No browser JavaScript or Sites tools. See [AGENTS.md](agents.html) before editing.

Run locally:

    python3 -B render_guides.py
    python3 -B -u server.py

Open http://127.0.0.1:8767. For a phone on the same Wi-Fi, add --host YOUR_LOCAL_IP to the server command and open that address on port 8767.

README.md and AGENTS.md are the guide sources. render_guides.py generates their readable HTML pages; build_static.py refreshes those pages and runs the navigation check before packaging the public site.

Live site: [Victoria Chamber Workshop](https://chamber-workshop-draft.vercel.app) (new tab). Hosted on Vercel under ZenithResearch, project chamber-workshop-draft. The source repository is private; the deployed pages are public.

Publish an update:

    vercel link --yes --project chamber-workshop-draft --scope zenith-research
    python3 -B build_static.py
    vercel deploy --prebuilt --prod --yes --scope zenith-research

Deployments are manual; pushing to GitHub alone does not publish changes. The packager includes only the server's allowlisted public files, including these two guides. Other repository documentation, Python source and separate reference notes are excluded.

Check navigation with python3 -B check_navigation.py. The older workshop-agenda repository remains separate.
