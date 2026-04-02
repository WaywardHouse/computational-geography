#!/bin/bash
set -euo pipefail

OUTDIR="${1:-_book}"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

while IFS= read -r file_path; do
  perl "$ROOT_DIR/scripts/normalize-interactive-html.pl" "$file_path"
done < <(find "$ROOT_DIR" -type f -name '*.qmd' \
  -not -path "$ROOT_DIR/_book/*" \
  -not -path "$ROOT_DIR/_book-core/*" \
  -not -path "$ROOT_DIR/_book-lab/*" \
  -not -path "$ROOT_DIR/_book-topics/*")

mkdir -p \
  "$OUTDIR/getting-started" \
  "$OUTDIR/methods-and-tools" \
  "$OUTDIR/foundations" \
  "$OUTDIR/environmental-systems" \
  "$OUTDIR/spatial-analysis" \
  "$OUTDIR/atmospheric-hazards" \
  "$OUTDIR/economic-systems" \
  "$OUTDIR/explore-more" \
  "$OUTDIR/cryosphere-and-mountain-systems" \
  "$OUTDIR/advanced-remote-sensing" \
  "$OUTDIR/advanced-investigations" \
  "$OUTDIR/laboratory" \
  "$OUTDIR/machine-learning"
