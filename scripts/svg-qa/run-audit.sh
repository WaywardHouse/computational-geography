#!/bin/zsh
# Re-render and measure every inline SVG figure. Run from repo root: scripts/svg-qa/run-audit.sh [workdir]
# Needs: Firefox (headless), python3. Output: <workdir>/audit.txt (per-figure CLIP / text-text / text-line counts)
# and <workdir>/png/*.png (renders to eyeball). Arial stands in for Barlow, so widths are slightly pessimistic.
ROOT=$PWD; HERE=$ROOT/scripts/svg-qa; W=${1:-${TMPDIR:-/tmp}/svg-qa}; mkdir -p $W/svgs $W/png $W/ffprof
FF=/Applications/Firefox.app/Contents/MacOS/firefox
find $W/svgs $W/png -type f -delete
python3 -I $HERE/extract.py $W >/dev/null
cp $HERE/render.sh $HERE/mkaudit.py $HERE/srv.py $W/; cd $W
./render.sh; python3 -I mkaudit.py
python3 - <<'PY'
s=open("audit.html").read()
s=s.replace('<body style="margin:0;font-family:Arial,sans-serif">','<body style="margin:0;font-family:Arial,sans-serif"><div style="position:absolute;left:-6000px;top:0">',1).replace('<pre id=r','</div><pre id=r',1)
s=s.replace("document.title='done';","fetch('http://127.0.0.1:8765/',{method:'POST',body:s});")
open("audit2.html","w").write(s)
PY
(python3 -I srv.py audit.txt & echo $! > srv.pid); sleep 1
timeout 60 $FF --headless --no-remote --profile $W/ffprof --window-size 1300,800 --screenshot $W/x.png file://$W/audit2.html >/dev/null 2>&1
kill $(cat srv.pid)
grep -E "CLIP=" audit.txt | awk '{split($2,a,"=");split($3,b,"=");split($4,c,"="); if(a[2]+b[2]+c[2]>0){f++;print}} END{print f+0, "figures flagged"}'
