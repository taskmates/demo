#!/usr/bin/env bash

MARKDOWN_CHAT_PATH=/private/var/demos/taskmates-demo/coding.md
RUNNER_TEMP=/tmp

#poetry shell /Users/ralphus/Development/taskmates/taskmates

taskmates-complete --model claude-3-haiku-20240307 --format completion "@guard report true if source code has been modified" <"$MARKDOWN_CHAT_PATH" |
  tee "$RUNNER_TEMP/guard-pr.md" &&
  taskmates-complete --format full "Hey @gh please create a feature branch, commit the modified files, and open a PR" <"$MARKDOWN_CHAT_PATH" |
  tee "$RUNNER_TEMP/create-pr.md"

cp "$RUNNER_TEMP/create-pr.md" "$MARKDOWN_CHAT_PATH"
