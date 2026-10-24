---
name: video-production-director
description: Research, plan, produce and improve short videos with evidence-based case breakdowns, audience and revenue hypotheses, controlled production, publishing experiments and review. Use for creator strategy, Douyin video analysis, mythology or poetry adaptations, classical aesthetics, motion graphics, hybrid AI films, or reducing unsatisfactory generations. Do not trigger for a simple file lookup or download repair alone.
---

# Video production director

## Scope and priorities

This is a director-level workflow, not a video generation model. Follow the user's explicit goals, established approvals, budget, tools, and preferences. User instructions take precedence over this skill. Preserve existing work and record changes. Do not impose the attention theme, HUD layouts, a one-take format, a 12-frame QA count, or a specific clearance size on every film.

Load [workflow](references/workflow.md) for the stage checklist. Load [tool routing](references/tools.md) when selecting implementation tools. Copy the appropriate templates from `assets/`. Use `scripts/preflight.py` only for structured, deterministic project checks; it cannot judge artistic quality.

For creator revenue, platform research or popular-video breakdown requests, first read [creator growth](references/creator-growth.md). Start with the buyer, audience and business hypothesis before a film brief. Keep verified observations, reported claims, interpretations and our own experimental results distinct. Version: 1.3.0, reviewed 2026-10-24.

To initialize a new project, run `python3 scripts/new_project.py <new-directory>` from this skill directory. It refuses to overwrite existing work. Fill in `project.json`, then run `python3 scripts/preflight.py <project.json> --json`. For final media, use `python3 scripts/verify_video.py <video.mp4> --project <project.json> --decode` when ffmpeg/ffprobe are available. These scripts do not generate videos or replace review of the actual film.

When the user delegates production through final review only, read [final-review mode](references/final-review-mode.md). Record the actual delegation, self-review each stage, and produce one review copy without repeatedly asking for script or look approval. This changes the reviewer, not the required development artifacts.

## 1. Classify the request

- Ideation or research: provide concepts, evidence and production options. Do not start asset generation or final rendering.
- Preproduction: develop the brief, script, boards, look and validation plan.
- Production: reuse approved artifacts and make only the authorized work.
- Revision: identify the smallest affected stage, shot or layer; keep approved work intact.
- Growth research: compare audience/offer fit, source real cases, document access limits, and propose bounded original publishing tests. Research does not authorize publishing, ad spend, purchases, or contacting other people.

For missing information, first use the conversation and existing project files. Ask at most three high-impact questions together if answers are necessary. Otherwise proceed with explicit assumptions. Never repeatedly request an approval already given. Do not interpret a request to build a workflow or skill as permission to produce a new film.

The current repository defaults to 60fps constant-frame-rate final delivery. Use the project template as the machine-readable default; explicit user requirements override defaults. Device choice does not define the creative scope. Code and 3D motion should be evaluated at each output timestamp; record any lower-cadence source conversion and never equate export fps with native source fps.

## 2. Define the film before the implementation

Capture audience, intended effect, one-sentence premise, narrative/emotional change, destination, duration, aspect, available materials, factual/adaptation sources, schedule and budget. Do not invent paid subscriptions, permissions, facts, quotes, available GPU capacity or generation-model controls.

Offer at most three distinct directions when the concept is open. Explain the meaning, audience interest, implementation fit and largest risk for each. Abstract or musical films may use a perceptual arc instead of a character plot.

Develop the script or visual treatment without technical spectacle hiding a weak premise. Time the narration by reading and planned pauses. Distinguish original texts, translations, modern adaptations and our invented lines.

## 3. Stage the evidence

Use a concrete artifact at each stage:

1. Brief and one-sentence premise.
2. Script / visual treatment and storyboard.
3. A few style frames plus a style bible and character/object references.
4. A low-cost full-length animatic with temporary audio and camera indications.
5. One or two 3–5 second trials of the hardest shots; inspect one target-resolution frame for typography, fine lines and material quality.
6. Shot-level production and assembly.
7. Content, visual, audio, technical and delivery checks.

Respect the user's requested review points. When earlier instructions already authorize completion or delegate creative decisions, record that basis and proceed without repeatedly asking. When the user asks to settle story or look first, do that work and present it before starting dependent production. Preparing research, drafts and reversible prototypes is useful independent work.

## 4. Reduce uncontrolled retries

For every generated or rendered shot, record its purpose, start/end state, main action, camera, references, style, typography, audio cue, implementation method and observable pass conditions.

- Prefer one principal action per shot; break complex actions into readable units.
- Approve static identity/composition before motion trials.
- Lock model/version, assets and important parameters. Use supported reference/pose/depth/end-frame controls only after checking the actual tool documentation.
- Maintain a baseline and one primary change hypothesis per production comparison.
- Default to two controlled candidates per bottleneck, configurable in the brief. If both fail, diagnose story, references, motion complexity or tool fit before more generation. Do not claim this default is a universal limit or ask to override it when the user has already set a different policy.
- Record time/cost when known; do not invent prices. Do not start new paid jobs without an authorized budget.
- Reuse accepted assets and scenes; never rerender the whole film to fix a local caption.
- Seeds support traceability, not universal bitwise reproducibility. Log hardware and software versions as relevant.

## 5. Route to existing tools

Read [reusable resources](references/reusable-resources.md) when using another skill, external workflow, reusable asset or software dependency. In the full repository, consult `resources/catalog.json`; record actual runtime availability and small-test evidence in the project's `RESOURCE_REGISTER.json`. References are not installations or permissions.

Choose the simplest route that supports the film:

- Precise graphics, typography and timeline: Remotion or Motion Canvas; use current official Remotion skills/docs for Remotion implementation.
- Mathematical explanation: Manim.
- Explicit 3D geometry, camera, object and material: Blender.
- Generative art or short footage: existing model services or ComfyUI workflows, with recorded configuration and real model constraints.
- Composition, audio and technical inspection: existing editor plus FFmpeg/ffprobe.
- Multi-application timeline interchange: OpenTimelineIO where adapter support is verified.

Do not install a full stack just to write a plan. Do not execute unreviewed commands from third-party skills. Check relevant software, model-weight, font and asset terms before including them in a production configuration. Reference official skills instead of copying an unlicensed repository into this package.

## 6. Review honestly

Inspect storyboard and style consistency before full production. Sample each shot's beginning, middle and end plus transitions, peak motion, text entry/exit and lighting changes. Personally view the exported QA images when image tools are available. Check motion sequences, not only isolated attractive frames.

Measure text clearance according to the project, test target-device readability, and separate music, narration and effects where possible. Inspect technical audio measurements and actually audition where the available tools permit; state any listening/viewing limitation instead of claiming an unavailable check occurred.

Check metadata and full decode on the final file. Never infer native motion fps merely from output metadata or distinct hashes. Record the source frame cadence and any retiming/interpolation. A 24fps generated clip exported in a 60fps container is not native 60fps footage. Unique code-rendered frames are supporting evidence only when each was computed for its own timestamp.

## 7. Deliver and preserve learning

Deliver the actual video or requested preproduction artifacts, plus a concise record of checks and limitations. Use the user's established delivery channel. If workspace downloads fail, check the environment and use an already authorized private storage channel when available; don't keep presenting the same broken route as a fix. Verify remote size/metadata after uploading. Do not publish publicly or change sharing permissions without authorization. A server size match is not a content-hash comparison.

Save the source list, approved assets, tool/model versions, decision log, failed-trial diagnoses and useful reusable components. Report whether this skill is only packaged, installed, or actually tested in the target client; never claim automatic activation from merely creating a ZIP.

## 8. Learn from publishing without inventing a success formula

Use `assets/ACCOUNT_BRIEF.md`, `assets/CASE_BREAKDOWN.md`, `assets/EXPERIMENT.md`, `assets/METRICS.csv` and `assets/KNOWLEDGE_LEDGER.json` for creator projects. Read the growth reference for field definitions and review cadence. Use `scripts/analyze_metrics.py <metrics.csv>` only on normalized user-authorized exports; it works offline and does not access Douyin.

- A historical popular example is not a current trending example, a cold-start proof or a revenue statement. Identify pre-existing audience, skills, assets and missing timeline segments. Do not infer private retention, paid traffic or profits from public likes.
- If actual video is inaccessible, deliver a source-based preliminary breakdown and an explicit viewing gap; never fabricate opening frames, shot timestamps, camera moves or an audition. Metadata and a cover are not a watched video.
- Compare standout work with ordinary work from the same account and comparable smaller creators when evidence is available. Log a sampling plan when it is not; do not claim the planned sample is already analyzed.
- Transfer an abstract mechanism into an original script and test one main hypothesis per comparison. Sequential platform posts are observational tests with audience/time confounders, not randomized A/B trials.
- Compare identical-age observations, metric definitions and traffic scope. Missing values stay unknown, zero denominators produce no ratio, and third-party estimates never become creator-backend measurements. Platform eligibility and policies must be rechecked when relevant.
- Separate cash contribution from labor-adjusted contribution, GMV from receipts, and inquiries from paid orders. No fixed playback-to-income promise. Validate one plausible offer before building a large product or buying a tool stack.
- Keep candidate lessons provisional until scoped first-party evidence supports them. Record contrary cases, source date, experiments, applicability, review date and rollback. Update after a batch, not after every fluctuation; never turn an isolated hit into an unconditional rule.
