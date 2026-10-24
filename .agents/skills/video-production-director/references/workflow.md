# Stage checklist

1. **Brief** — audience, premise, intended effect, format, resources, deadline and budget. Use `assets/BRIEF.md`.
2. **Script/treatment** — beginning, change, ending; measured reading time or visual beats; sources and adaptation labels. Use `assets/SCRIPT.md`.
3. **Boards and look** — load [art direction](art-direction.md); inspect a small relevant reference set, turn observations into original story-specific rules, and compare style frames. Use `assets/STYLE_BIBLE.md`.
4. **Animatic** — full-length low-cost timing preview with temporary audio. Check comprehension and pacing before polish.
5. **Risk trials** — one or two hardest short shots, including target-resolution typography/material check. Use `assets/SHOT_CONTRACT.json`.
6. **Production** — freeze accepted inputs; make shot-level versions; log controlled experiments in `assets/DECISION_LOG.csv`.
7. **QA/delivery** — content, aesthetic, audio, technical and actual remote delivery. Use `assets/QA_AND_DELIVERY.md` and `assets/ART_REVIEW.md`; do not equate metadata checks with aesthetic approval.

Final duration is selected from the script and timed animatic, not a universal 30–40 second limit. Leave `format.duration_s=null` during unresolved development, then set the selected positive duration and matching shot timeline before production. As planning examples only: a single visual beat may fit 20–40 seconds, a focused story 45–75 seconds, and a more involved explanation 90 seconds or longer. These are not platform-optimal benchmarks. Do not pad holds or rush narration to fit them; record the actual timing basis. 60fps final output remains required unless the user changes it.

When generated images help the look or shot assets, read [image assets](image-assets.md), inspect actual model access and reference controls, lock accepted images, and test a motion route. Image generation is separate from animation, composition and final video verification.

Review points follow the user's authorization. Preserve approvals already given. A delegated decision can be recorded as delegated; don't fabricate an approval from an absent user reply. Research and reversible drafts can proceed independently of a pending decision.

Failure routing: unclear meaning → script; inconsistent identity → references/look; deformation in motion → smaller action or different production method; bad pacing → animatic; text collisions → compositing; failed download → delivery channel. Two failed controlled candidates are a diagnostic signal, not a reason to keep changing random seeds indefinitely.
