#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$REPO_ROOT"
PROJECT_PATH=projects/2026-10-24-coffee-ring-85
VIDEO_PYTHON="${VIDEO_PYTHON:-$REPO_ROOT/.venv/bin/python}"
# Reuses accepted TTS files; remove only explicitly selected raw files when revising voice.
node engine/tts-timeline.js --script "$PROJECT_PATH/script.json" --out "$PROJECT_PATH/audio/voice" --timeline "$PROJECT_PATH/timeline.json" --python "$VIDEO_PYTHON" --provider engine/providers/kokoro_cpu.py --speed 1.18 --duration 85
"$VIDEO_PYTHON" engine/providers/align_words.py "$PROJECT_PATH/timeline.json"
node engine/audio-studio.js --timeline "$PROJECT_PATH/timeline.json" --out "$PROJECT_PATH/audio/mix"
node engine/qa-watchdog.js --root . --page "$PROJECT_PATH/source/film.html" --out "$PROJECT_PATH/qa/watchdog-samples" --report "$PROJECT_PATH/qa/watchdog.json" --duration 85 --sourceFiles "engine/fx-components.js,$PROJECT_PATH/source/film.js,$PROJECT_PATH/timeline.json"
# Review actual keyframes and pilot before running final renderer. The CLI gate binds source hashes.
node engine/parallel-render.js --root . --page "$PROJECT_PATH/source/film.html" --frames "$PROJECT_PATH/frames/master" --duration 85 --fps 60 --workers 4 --qa "$PROJECT_PATH/qa/watchdog.json" --output "$PROJECT_PATH/renders/picture-master.mp4" --report "$PROJECT_PATH/qa/final-render.json" --resume
bash "$PROJECT_PATH/source/assemble.sh"
