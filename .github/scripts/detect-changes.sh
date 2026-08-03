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
  paths='*'
else
  paths=$(git diff --name-only "${GITHUB_EVENT_BEFORE:-}" "${GITHUB_SHA:-}" 2>/dev/null || true)
  if printf '%s\n' "$paths" | grep -qE '^\.github/(scripts|workflows)/'; then
    paths='*'
  fi
fi

projects='[]'

while read -r entry; do
  path=$(jq -r '.path' <<<"$entry")
  if [ "$paths" = "*" ] || printf '%s\n' "$paths" | grep -qE "^${path}/"; then
    projects=$(jq -c --argjson entry "$entry" '. + [$entry]' <<<"$projects")
  fi
done < <(jq -c '.[]' <<<"$subprojects")

echo "projects=$projects" >> "$GITHUB_OUTPUT"
