#!/bin/bash
set -euo pipefail

OUTDIR="${1:-_book}"

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
