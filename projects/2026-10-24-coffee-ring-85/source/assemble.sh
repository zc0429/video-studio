#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ffmpeg -hide_banner -loglevel warning -y -i renders/picture-master.mp4 -i audio/mix/master.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 224k -ar 48000 -ac 2 -t 85 -metadata title='咖啡渍的边界悬案｜85秒三幕审核版' -movflags +faststart delivery/coffee-ring-85-review-1080x1920-60fps.mp4
ffmpeg -hide_banner -loglevel warning -y -i delivery/coffee-ring-85-review-1080x1920-60fps.mp4 -vf scale=540:960 -c:v libx264 -preset veryfast -crf 26 -r 60 -fps_mode cfr -c:a aac -b:a 128k -movflags +faststart delivery/coffee-ring-85-preview-540x960-60fps.mp4
