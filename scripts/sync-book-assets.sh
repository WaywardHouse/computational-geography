#!/bin/bash
set -euo pipefail

OUTDIR="${1:-_book}"

ASSET_ROOT="$OUTDIR/assets"

rm -rf "$ASSET_ROOT"

mkdir -p \
  "$ASSET_ROOT/dist" \
  "$ASSET_ROOT/js" \
  "$ASSET_ROOT/css" \
  "$ASSET_ROOT/images"

# Copy directory contents rather than the directories themselves so reruns stay
# idempotent even when Quarto leaves partial outputs behind.
cp -R assets/dist/. "$ASSET_ROOT/dist/"
cp -R assets/js/. "$ASSET_ROOT/js/"
cp -R assets/css/. "$ASSET_ROOT/css/"
cp -R assets/images/. "$ASSET_ROOT/images/"
