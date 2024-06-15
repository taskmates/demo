#!/usr/bin/env bash


cat "$MARKDOWN_CHAT_PATH" | taskmates-complete \
    --template-params='{"repository": "${{ github.repository }}", "event_name": "${{ github.event_name }}"}' \
    --template-params="{ \"event\": $GITHUB_EVENT  }"  \
    --format text \
    "Hey @progress please report this"
