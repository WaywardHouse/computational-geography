#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

PAGES=(
  "foundations/what-is-a-spatial-model.qmd"
  "laboratory/sar-fundamentals-and-applications.qmd"
  "advanced-remote-sensing/prospect-leaf-optical-properties.qmd"
)

HTML_OUTPUTS=(
  "_book/foundations/what-is-a-spatial-model.html"
  "_book/laboratory/sar-fundamentals-and-applications.html"
  "_book/advanced-remote-sensing/prospect-leaf-optical-properties.html"
)

for page in "${PAGES[@]}"; do
  echo "Rendering $page"
  (cd "$ROOT_DIR" && quarto render "$page")
done

for html in "${HTML_OUTPUTS[@]}"; do
  echo "Checking $html"
  test -f "$ROOT_DIR/$html"
  grep -q '/assets/js/core.js' "$ROOT_DIR/$html"
done

echo "Wayfinding check passed."
