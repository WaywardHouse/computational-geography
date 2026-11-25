#!/usr/bin/env python3
"""Bulk SVG QA fixes (idempotent). Run from repo root.
1. Arrow markers: stop scaling with stroke width (markerUnits=userSpaceOnUse).
2. Text halo: labels listed in scripts/svg-qa/audit-baseline.txt as TEXT/LINE get a
   paint-order stroke in the figure's background colour so lines don't cut through them.
"""
import re, subprocess, sys, html
files = subprocess.check_output(["git","ls-files","*.qmd"],text=True).split("\n")
files=[f for f in files if f and not f.startswith("_book") and " " not in f]
# labels flagged text-on-line, keyed by figure
flag = {}; cur=None
for l in open("scripts/svg-qa/audit-baseline.txt",encoding="utf8"):
    m=re.match(r"(\S+)\s+CLIP=",l)
    if m: cur=m[1]; continue
    m=re.match(r'\s+TEXT/LINE "(.*)" crossed',l)
    if m and cur: flag.setdefault(cur,set()).add(m[1])
def marker(m):
    tag=m.group(0)
    if "markerUnits" in tag: return tag
    w=int(m[1]); 
    return re.sub(r'markerWidth="\d+" markerHeight="\d+"',
        f'markerUnits="userSpaceOnUse" viewBox="0 0 {w} {w}" markerWidth="{w+4}" markerHeight="{w+4}"',tag)
nm=nt=0
for p in files:
    try: t=open(p,encoding="utf8").read()
    except: continue
    if "<svg" not in t: continue
    base=p.replace("/","__").replace(".qmd","")
    idx=[0]
    def fig(m):
        global nm,nt
        idx[0]+=1; s=m.group(0)
        s2=re.sub(r'<marker\b[^>]*markerWidth="(\d+)"[^>]*>',marker,s)
        nm+= s2!=s; s=s2
        labels=flag.get(f"{base}__{idx[0]}",set())
        bg=re.search(r'<rect[^>]*fill="(#[0-9a-fA-F]{3,6})"',s)
        bg=bg[1] if bg else "#ffffff"
        def txt(m2):
            global nt
            tag,body=m2[1],m2[2]
            if "paint-order" in tag: return m2[0]
            plain=html.unescape(re.sub(r"<[^>]+>","",body)).strip()[:32]
            if plain in labels:
                nt+=1
                return tag[:-1]+f' paint-order="stroke" stroke="{bg}" stroke-width="5" stroke-linejoin="round">'+body+"</text>"
            return m2[0]
        return re.sub(r"(<text\b[^>]*>)(.*?)</text>",txt,s,flags=re.S)
    t2=re.sub(r"<svg\b.*?</svg>",fig,t,flags=re.S)
    if t2!=t: open(p,"w",encoding="utf8").write(t2)
print("figures with markers fixed:",nm,"text halos:",nt)
