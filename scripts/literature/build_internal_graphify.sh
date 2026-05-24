#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH="${1:-04_templates/literature_config.example.yaml}"
OUTPUT_DIR="${2:-graphify-out/internal_literature}"

if [ ! -f "$CONFIG_PATH" ]; then
  echo "Config not found: $CONFIG_PATH" >&2
  exit 1
fi

SECOND_BRAIN_PATH="$(python3 - "$CONFIG_PATH" <<'PY'
import sys, re
path=sys.argv[1]
text=open(path, encoding='utf-8').read()
match=re.search(r'^second_brain_literature_path:\s*["']?([^"'
]+)', text, re.M)
print(match.group(1).strip() if match else '')
PY
)"

if [ -z "$SECOND_BRAIN_PATH" ] || [ "$SECOND_BRAIN_PATH" = "<second_brain_literature_path>" ]; then
  echo "second_brain_literature_path is not configured. Copy the example config and replace placeholders." >&2
  exit 2
fi

if [ ! -d "$SECOND_BRAIN_PATH" ]; then
  echo "second_brain_literature_path is not a directory: $SECOND_BRAIN_PATH" >&2
  exit 3
fi

mkdir -p "$OUTPUT_DIR"
if ! command -v graphify >/dev/null 2>&1; then
  echo "graphify command not found. Install or activate graphify before running this script." >&2
  exit 4
fi

echo "Building bounded internal graphify corpus"
echo "Input: $SECOND_BRAIN_PATH"
echo "Output: $OUTPUT_DIR"

graphify "$SECOND_BRAIN_PATH" --no-viz

if [ -d "$SECOND_BRAIN_PATH/graphify-out" ]; then
  rsync -a "$SECOND_BRAIN_PATH/graphify-out/" "$OUTPUT_DIR/"
fi

echo "Internal graphify output ready: $OUTPUT_DIR"
