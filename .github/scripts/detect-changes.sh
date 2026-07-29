#!/usr/bin/env bash
set -euo pipefail

subprojects='[
  {"path":"01-arithmetic-formatter"},
  {"path":"02-time-calculator"},
  {"path":"03-budget-app"},
  {"path":"04-polygon-area-calculator"},
  {"path":"05-probability-calculator"}
]'

if [ "${GITHUB_EVENT_NAME:-}" = "workflow_dispatch" ]; then
  paths=$(jq -r '.[].path' <<<"$subprojects")
else
  paths=$(git diff --name-only "${GITHUB_EVENT_BEFORE:-}" "${GITHUB_SHA:-}" 2>/dev/null || true)
fi

projects='[]'

while read -r entry; do
  path=$(jq -r '.path' <<<"$entry")
  if printf '%s\n' "$paths" | grep -qE "^${path}/"; then
    projects=$(jq -c --argjson entry "$entry" '. + [$entry]' <<<"$projects")
  fi
done < <(jq -c '.[]' <<<"$subprojects")

echo "projects=$projects" >> "$GITHUB_OUTPUT"
