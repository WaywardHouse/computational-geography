#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SPLIT_BOOK_DIRS=(
  "$ROOT_DIR/_book-core"
  "$ROOT_DIR/_book-topics"
  "$ROOT_DIR/_book-lab"
)

EXISTING_BOOK_DIRS=()
for dir in "${SPLIT_BOOK_DIRS[@]}"; do
  if [[ -d "$dir" ]]; then
    EXISTING_BOOK_DIRS+=("$dir")
  fi
done

if [[ ${#EXISTING_BOOK_DIRS[@]} -eq 0 && -d "$ROOT_DIR/_book" ]]; then
  EXISTING_BOOK_DIRS+=("$ROOT_DIR/_book")
fi

if [[ ${#EXISTING_BOOK_DIRS[@]} -eq 0 ]]; then
  echo "No rendered book output found. Render the book first." >&2
  exit 1
fi

echo "Checking rendered HTML for flattened pseudo-lists..."

TMP_FILE="$(mktemp)"
trap 'rm -f "$TMP_FILE"' EXIT

rg -n '<p><strong>[^<]+:</strong> ?- (?:<|[A-Za-z])' "${EXISTING_BOOK_DIRS[@]}" > "$TMP_FILE" || true

if [[ -s "$TMP_FILE" ]]; then
  echo "Found flattened pseudo-lists in rendered output:"
  cat "$TMP_FILE"
  exit 1
fi

echo "Render QA passed."
