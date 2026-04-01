#!/bin/bash
set -euo pipefail

OUTDIR="${1:-_book}"

mkdir -p "$OUTDIR/assets"

rm -rf "$OUTDIR/assets/dist" "$OUTDIR/assets/js" "$OUTDIR/assets/css" "$OUTDIR/assets/images"

cp -R assets/dist "$OUTDIR/assets/"
cp -R assets/js "$OUTDIR/assets/"
cp -R assets/css "$OUTDIR/assets/"
cp -R assets/images "$OUTDIR/assets/"
