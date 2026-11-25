#!/bin/zsh
S=$PWD
FF=/Applications/Firefox.app/Contents/MacOS/firefox
for h in svgs/*.html; do
  b=${h:t:r}
  vb=$(grep -o 'viewBox="[^"]*"' $h | head -1 | sed 's/viewBox="//;s/"//')
  w=$(echo $vb | awk '{print $3}'); ht=$(echo $vb | awk '{print $4}')
  H=$(python3 -c "print(int(1000*$ht/$w)+4)")
  [ -f png/$b.png ] && continue
  $FF --headless --no-remote --profile $S/ffprof --window-size 1000,$H --screenshot $S/png/$b.png file://$S/$h >/dev/null 2>&1
done
