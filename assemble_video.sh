#!/bin/bash
# Simple Ken Burns style assembly using ffmpeg
# Usage: ./assemble_video.sh input_images_dir narration.mp3 output.mp4

IMAGES_DIR=$1
AUDIO=$2
OUTPUT=$3

# Create a list of images with duration (example 4 seconds each)
# You will expand this with real image sequencing later

ffmpeg -y \
  -framerate 1/4 \
  -pattern_type glob -i "$IMAGES_DIR/*.jpg" \
  -i "$AUDIO" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -shortest \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,zoompan=z='min(zoom+0.0015,1.5)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080" \
  "$OUTPUT"

echo "Video assembled: $OUTPUT"
