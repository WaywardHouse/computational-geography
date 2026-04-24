#!/bin/bash
set -euo pipefail

OUTDIR="${1:-_book}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Pull shared assets from waywardhouse-site.
# Silently skipped if the sibling repo is absent (e.g. CI).
SITE_ROOT="$(cd "$REPO_ROOT/../waywardhouse-site" 2>/dev/null && pwd || echo "")"

if [[ -n "$SITE_ROOT" && -d "$SITE_ROOT" ]]; then
  echo "Syncing shared assets from $SITE_ROOT..."

  # CSS
  cp "$SITE_ROOT/assets/css/quarto-wayward.css" "$REPO_ROOT/assets/css/quarto-wayward.css"

  # Core JS (book-wayfinding.js is book-specific, do not overwrite)
  cp "$SITE_ROOT/assets/js/core.js"             "$REPO_ROOT/assets/js/core.js"

  # Bundled dist
  cp "$SITE_ROOT/assets/dist/main.js"           "$REPO_ROOT/assets/dist/main.js"
  cp "$SITE_ROOT/assets/dist/main.css"          "$REPO_ROOT/assets/dist/main.css"

  # Quarto includes
  cp "$SITE_ROOT/assets/includes/quarto-head.html"        "$REPO_ROOT/assets/includes/quarto-head.html"
  cp "$SITE_ROOT/assets/includes/quarto-body.html"        "$REPO_ROOT/assets/includes/quarto-body.html"
  cp "$SITE_ROOT/assets/includes/quarto-before-body.html" "$REPO_ROOT/assets/includes/quarto-before-body.html"

  if [[ -f "$SITE_ROOT/assets/includes/quarto-book-nav.html" ]]; then
    cp "$SITE_ROOT/assets/includes/quarto-book-nav.html" "$REPO_ROOT/assets/includes/quarto-book-nav.html"
  fi
fi

ASSET_ROOT="$OUTDIR/assets"

rm -rf "$ASSET_ROOT"

mkdir -p \
  "$ASSET_ROOT/dist" \
  "$ASSET_ROOT/js" \
  "$ASSET_ROOT/css" \
  "$ASSET_ROOT/images"

# Copy directory contents; reruns are idempotent.
cp -R "$REPO_ROOT/assets/dist/."    "$ASSET_ROOT/dist/"
cp -R "$REPO_ROOT/assets/js/."      "$ASSET_ROOT/js/"
cp -R "$REPO_ROOT/assets/css/."     "$ASSET_ROOT/css/"
cp -R "$REPO_ROOT/assets/images/."  "$ASSET_ROOT/images/"
