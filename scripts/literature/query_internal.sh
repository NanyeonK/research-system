#!/usr/bin/env bash
set -euo pipefail

GRAPHIFY_PATH="${1:-}"
QUERY="${2:-}"
BUDGET="${3:-2000}"

if [ -z "$GRAPHIFY_PATH" ] || [ -z "$QUERY" ]; then
  echo "Usage: $0 <graphify_output_path_or_project_path> <query> [budget]" >&2
  exit 1
fi

if ! command -v graphify >/dev/null 2>&1; then
  echo "graphify command not found. Install or activate graphify before querying." >&2
  exit 2
fi

if [ -f "$GRAPHIFY_PATH/graph.json" ]; then
  WORKDIR="$(dirname "$GRAPHIFY_PATH")"
elif [ -f "$GRAPHIFY_PATH/graphify-out/graph.json" ]; then
  WORKDIR="$GRAPHIFY_PATH"
else
  echo "No graphify graph found at $GRAPHIFY_PATH" >&2
  exit 3
fi

cd "$WORKDIR"
graphify query "$QUERY" --budget "$BUDGET"
