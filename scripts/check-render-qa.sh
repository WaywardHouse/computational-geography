#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BOOK_DIR="$ROOT_DIR/_book"

if [[ ! -d "$BOOK_DIR" ]]; then
  echo "_book does not exist. Render the book first." >&2
  exit 1
fi

echo "Checking rendered HTML for flattened pseudo-lists..."

TMP_FILE="$(mktemp)"
trap 'rm -f "$TMP_FILE"' EXIT

rg -n '<p><strong>[^<]+:</strong> ?-' "$BOOK_DIR" > "$TMP_FILE" || true

if [[ -s "$TMP_FILE" ]]; then
  echo "Found flattened pseudo-lists in rendered output:"
  cat "$TMP_FILE"
  exit 1
fi

echo "Render QA passed."
