# yt-faceless-agent

Zero-budget autonomous YouTube faceless channel agent powered by Grok.

## Locked Configuration
- **Voice**: aurora (female)
- **Cadence**: 1 long-form + 7 Shorts per week
- **Primary niches**: History explainers / narrow documentaries + Science & space explainers
- **Secondary**: Business / company rise-and-fall stories
- **Style**: AI-generated images + Ken Burns (slow pan/zoom) + Aurora narration + burned-in captions
- **Budget**: $0 monthly software cost

## Folder Structure
```
yt-faceless-agent/
├── README.md
├── state/
│   ├── config.json
│   ├── performance.json
│   └── current_cycle.json
├── scripts/
│   ├── assemble_video.sh
│   └── upload_helper.py
├── ready_to_upload/
├── assets/
└── production_logs/
```

## How it works
1. Grok Automations run on schedule.
2. Grok researches, picks topics, writes original scripts, generates narration (Voice), generates images, assembles video with ffmpeg, writes metadata.
3. Finished packages land in `ready_to_upload/YYYY-MM-DD/`.
4. You (or a free GitHub Action / local script) run the upload helper using your YouTube OAuth token.

## One-time remaining setup
1. Google Cloud project → enable YouTube Data API v3 → create OAuth Desktop client → authorize your channel → get refresh token.
2. Store client_secrets.json + token securely.
3. Test upload with scripts/upload_helper.py.

## Current Status
Initialized 2026-11-24. Ready for first production cycle.
