import glob,os,html
files=sorted(glob.glob("svgs/*.svg"))
parts=[]
for f in files:
    n=os.path.basename(f)[:-4]
    parts.append(f'<div class="w" data-n="{n}" style="width:1000px;height:auto">{open(f).read()}</div>')
js='''
const out=[];
function box(e){const b=e.getBBox();return {x:b.x,y:b.y,w:b.width,h:b.height};}
function tbox(t){ // transform-aware: use getBoundingClientRect relative to svg
  const s=t.ownerSVGElement.getBoundingClientRect(), r=t.getBoundingClientRect();
  const vb=t.ownerSVGElement.viewBox.baseVal; const k=vb.width/s.width;
  return {x:(r.left-s.left)*k+vb.x,y:(r.top-s.top)*k+vb.y,w:r.width*k,h:r.height*k};}
function ov(a,b){const w=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),h=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);return (w>2&&h>2)?w*h:0;}
document.querySelectorAll('.w').forEach(d=>{
  const svg=d.querySelector('svg'),vb=svg.viewBox.baseVal,iss=[];
  const ts=[...svg.querySelectorAll('text')].filter(t=>t.textContent.trim());
  const bs=ts.map(t=>({t,b:tbox(t),s:t.textContent.trim().slice(0,32)}));
  let clip=0,tt=0,tl=0;
  bs.forEach(o=>{const b=o.b;
    if(b.x+b.w>vb.x+vb.width+1||b.x<vb.x-1||b.y+b.h>vb.y+vb.height+1||b.y<vb.y-1){clip++;iss.push('CLIP "'+o.s+'" right='+Math.round(b.x+b.w-vb.width)+'px past edge');}
  });
  for(let i=0;i<bs.length;i++)for(let j=i+1;j<bs.length;j++){
    const a=bs[i].b,b=bs[j].b,o=ov(a,b);
    if(o>0.15*Math.min(a.w*a.h,b.w*b.h)){tt++;iss.push('TEXT/TEXT "'+bs[i].s+'" x "'+bs[j].s+'"');}
  }
  // text vs stroked line/path
  const geo=[...svg.querySelectorAll('line,path,polyline')].filter(g=>!g.closest('defs,marker')&&g.getAttribute('stroke')&&g.getAttribute('stroke')!=='none');
  bs.forEach(o=>{if(o.t.getAttribute('paint-order'))return;const b=o.b;let hit=0;
    const pt=svg.createSVGPoint();
    for(const g of geo){ if(g.tagName==='path'&&!/fill="none"/.test(g.outerHTML.slice(0,300))&&g.getAttribute('fill')&&g.getAttribute('fill')!=='none')continue;
      let h=false;
      for(let ix=0;ix<=8&&!h;ix++)for(let iy=0;iy<=2&&!h;iy++){
        const px=b.x+b.w*ix/8, py=b.y+b.h*(0.25+0.5*iy/2);
        const m=g.getScreenCTM().inverse().multiply(svg.getScreenCTM());
        pt.x=px;pt.y=py;const q=pt.matrixTransform(m);
        try{ if(g.isPointInStroke(q))h=true;}catch(e){}
      }
      if(h)hit++;}
    if(hit){tl++;iss.push('TEXT/LINE "'+o.s+'" crossed by '+hit+' stroke(s)');}
  });
  out.push({n:d.dataset.n,clip,tt,tl,iss});
});
let s='';out.forEach(o=>{s+=o.n+'  CLIP='+o.clip+' T/T='+o.tt+' T/L='+o.tl+'\\n'; o.iss.forEach(i=>s+='    '+i+'\\n');});
document.getElementById('r').textContent=s;
document.title='done';
'''
open("audit.html","w").write('<!doctype html><meta charset=utf8><body style="margin:0;font-family:Arial,sans-serif">'+"".join(parts)+'<pre id=r style="font:14px monospace"></pre><script>window.addEventListener("load",()=>{'+js+'})</script>')
