#!/usr/bin/env python3
"""Apply browser-measured label wraps (wrap.json) to inline SVG figures in .qmd files.
usage: python3 -I scripts/svg-qa/apply-wraps.py wrap.json   (run from repo root)
Each entry: figure id (<dir>__<chapter>__<n>), index of <text> within the figure, new x, wrapped lines.
"""
import json,re,sys,html
data=json.load(open(sys.argv[1]))
by={}
for r in data:
    if r["x"]<0: continue
    by.setdefault(r["n"],[]).append(r)
files={}
for n in by:
    d,c,i=n.rsplit("__",2); files.setdefault(f"{d}/{c}.qmd".replace("__","/",0),[]).append((int(i),by[n]))
for path,figs in files.items():
    t=open(path,encoding="utf8").read(); figs=dict(figs)
    k=[0]
    def fig(m):
        k[0]+=1
        if k[0] not in figs: return m.group(0)
        rs={r["idx"]:r for r in figs[k[0]]}; j=[-1]
        def txt(m2):
            j[0]+=1
            r=rs.get(j[0])
            if not r or "<tspan" in m2[2]: return m2[0]
            tag=re.sub(r'\sx="[^"]*"',f' x="{r["x"]}"',m2[1],1)
            body="".join(
                f'<tspan x="{r["x"]}"'+(f' dy="{1.2 if i else 0}em"' if i else "")+f'>{html.escape(l,quote=False)}</tspan>'
                for i,l in enumerate(r["lines"])) if len(r["lines"])>1 else html.escape(r["lines"][0],quote=False)
            return tag+body+"</text>"
        return re.sub(r"(<text\b[^>]*>)(.*?)</text>",txt,m.group(0),flags=re.S)
    t2=re.sub(r"<svg\b.*?</svg>",fig,t,flags=re.S)
    if t2!=t: open(path,"w",encoding="utf8").write(t2); print("updated",path)
