import re,sys,os,glob
S=sys.argv[1]; out=S+"/svgs"
n=0; idx=[]
for p in sorted(glob.glob("**/*.qmd",recursive=True)):
    if p.startswith("_book"): continue
    t=open(p,encoding="utf8").read()
    for i,m in enumerate(re.finditer(r"<svg\b.*?</svg>",t,re.S)):
        line=t[:m.start()].count("\n")+1
        name=p.replace("/","__").replace(".qmd","")+f"__{i+1}"
        svg=m.group(0)
        if 'xmlns=' not in svg.split('>')[0]: svg=svg.replace("<svg","<svg xmlns=\"http://www.w3.org/2000/svg\"",1)
        open(f"{out}/{name}.svg","w").write(svg)
        html=f'<!doctype html><meta charset=utf8><body style="margin:0;background:#fff;font-family:Arial,sans-serif"><div style="width:1000px">{m.group(0)}</div>'
        open(f"{out}/{name}.html","w").write(html)
        idx.append(f"{name}\t{p}:{line}"); n+=1
open(S+"/index.tsv","w").write("\n".join(idx))
print(n)
