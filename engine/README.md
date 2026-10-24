# Deterministic film engine v2
Four-to-six worker_threads launch isolated Chromium renderers. Each owns a contiguous absolute-frame range and calls seekTo(frameIndex/fps); Canvas JPEG readback avoids slow full-window screenshots. Atomic frame writes, resumable ranges, missing-frame rejection, worker error propagation and FFmpeg CFR assembly are implemented. A passing QA report is mandatory. Actual 1-vs-4-page benchmark is recorded per production; no universal 5x guarantee.

Modules: parallel-render.js, qa-watchdog.js, tts-timeline.js, fx-components.js, audio-studio.js. Browser components are original UMD and Node-testable. CPU-only runtime supported. Browser page contract: filmReady, filmTimeline, seekTo(t), getSceneState(), captionBoxes. Motion telemetry must describe actual rendered transforms, not fake counters.

QA: .5s core-region pixel samples (2s overview retained), every rolling 3s window requires composition motion or a real subshot AND visible pixel change. Grain/subtitle/particle jitter alone does not pass. Exactly 16 target-size keyframes are emitted; visual inspection remains mandatory. This is a heuristic gate, not proof of artistic value or absence of every sub-.5s defect.

TTS: 14 generated segments at 1.18; FFmpeg trims leading/trailing silence, ffprobe measures milliseconds; rejects narration longer than the chosen 85s. Timeline has explicit visual pause budget. Per-word timestamps are initially labelled estimated; a provider/ASR refinement must preserve uncertainty when not force-aligned. Kinetic captions scale highlighted nouns/verbs 135%, no white backing box.

Audio: independent speech, original procedural score, original SFX; actual two-input FFmpeg sidechain compression; 3-act instrumentation and BPM progression. Audio meters and transcription do not establish a subjective listening pass.

Tests: npm test. No third-party video/music, model credentials or weights in Git. Existing historical project remains archived. This v2 is the default path for the new production; no claim of every “industrial” feature (distributed farm, GUI, cloud job service) being built.
