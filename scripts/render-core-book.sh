#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BASE_CONFIG="$ROOT_DIR/_quarto.yml"
TARGET_CONFIG="$ROOT_DIR/_quarto-core-book.yml"
BACKUP_CONFIG="$ROOT_DIR/_quarto.yml.render-backup"
BASE_INDEX="$ROOT_DIR/index.qmd"
TARGET_INDEX="$ROOT_DIR/core-book/index.qmd"
BACKUP_INDEX="$ROOT_DIR/index.qmd.render-backup"
STASH_DIR="$(mktemp -d "${TMPDIR:-/tmp}/codex-render-stash.XXXXXX")"

cleanup() {
  if [[ -d "$STASH_DIR" ]]; then
    cp -R "$STASH_DIR"/. "$ROOT_DIR"/ 2>/dev/null || true
    rm -rf "$STASH_DIR"
  fi
  if [[ -f "$BACKUP_CONFIG" ]]; then
    mv "$BACKUP_CONFIG" "$BASE_CONFIG"
  fi
  if [[ -f "$BACKUP_INDEX" ]]; then
    mv "$BACKUP_INDEX" "$BASE_INDEX"
  fi
}

trap cleanup EXIT

while IFS= read -r file_path; do
  [[ -e "$file_path" ]] || continue
  rel="${file_path#$ROOT_DIR/}"
  mkdir -p "$STASH_DIR/$(dirname "$rel")"
  if [[ -d "$file_path" ]]; then
    cp -R "$file_path" "$STASH_DIR/$rel"
    rm -rf "$file_path"
  else
    cp "$file_path" "$STASH_DIR/$rel"
    rm -f "$file_path"
  fi
done < <(find "$ROOT_DIR" -maxdepth 2 \
  \( -name '*.html' -o -name '*_files' \) \
  -not -path "$ROOT_DIR/_book*" \
  -not -path "$ROOT_DIR/index.html" \
  -not -path "$ROOT_DIR/.git/*")

cp "$BASE_CONFIG" "$BACKUP_CONFIG"
cp "$TARGET_CONFIG" "$BASE_CONFIG"
cp "$BASE_INDEX" "$BACKUP_INDEX"
cp "$TARGET_INDEX" "$BASE_INDEX"

rm -rf "$ROOT_DIR/.quarto/idx"

"$ROOT_DIR/scripts/prepare-book-output.sh" "$ROOT_DIR/_book-core"
mkdir -p "$ROOT_DIR/_book-core"

quarto render
