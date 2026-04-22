import os
import glob
import re
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subdirs = ["foundations", "environmental-systems", "spatial-analysis", 
           "atmospheric-hazards", "economic-systems", "machine-learning",
           "advanced-remote-sensing", "cryosphere-and-mountain-systems", 
           "laboratory", "scientific-computing", "methods-and-tools"]

ALIASES = {
    "pathway a: remote sensing fundamentals": "foundations/what-is-remote-sensing.qmd",
    "pathway a: atmospheric effects & surface reflectance": "foundations/atmospheric-effects-and-surface-reflectance.qmd",
    "pathway a: spectral & temporal resolution": "foundations/spatial-spectral-temporal-and-radiometric-resolution.qmd",
    "pathway a: vegetation indices & remote sensing": "environmental-systems/vegetation-indices-and-remote-sensing.qmd",
    "pathway a: vegetation indices": "environmental-systems/vegetation-indices-and-remote-sensing.qmd",
    "pathway a: multispectral imagery & band interpretation": "environmental-systems/multispectral-imagery-and-band-interpretation.qmd",
    "pathway a: sar fundamentals (problem set a, investigation 1)": "laboratory/sar-fundamentals-and-applications.qmd",
    "pathway a: orbital mechanics (companion 1)": "advanced-remote-sensing/orbital-mechanics.qmd",
    "pathway a: water optics (companion 1)": "advanced-remote-sensing/water-optics.qmd",
    
    "pathway b: net radiation & albedo": "environmental-systems/net-radiation-and-albedo.qmd",
    "pathway b: sensible & latent heat fluxes": "environmental-systems/sensible-and-latent-heat-fluxes.qmd",
    "pathway b: photosynthesis & light response": "environmental-systems/photosynthesis-light-response.qmd",
    "pathway b: wind profiles & turbulence": "environmental-systems/wind-profiles-and-turbulence.qmd",
    "pathway b: temperature-moisture gradients": "environmental-systems/temperature-moisture-gradients.qmd",

    "pathway c: urban bid-rent models": "economic-systems/urban-bid-rent-model.qmd",
    "pathway c: gravity models — trade & migration": "economic-systems/canada-trade-gravity-model.qmd",
    "pathway c: markets & spatial arbitrage": "economic-systems/markets-spatial-arbitrage.qmd",
    "pathway c: fire spread modeling": "atmospheric-hazards/fire-spread-modeling.qmd",
    "pathway c: urban applications": "economic-systems/urban-agglomeration-economies.qmd",
    
    "laboratory: wave dynamics & nearshore transformation": "laboratory/wave-dynamics-and-nearshore-transformation.qmd",
    
    "methods reference: differential equations": "methods-and-tools/simulation-paradigms.qmd",
    "methods reference: numerical methods": "methods-and-tools/simulation-paradigms.qmd",
    "methods reference: pdes & numerical methods": "methods-and-tools/simulation-paradigms.qmd",
    "methods reference: spatial statistics": "methods-and-tools/how-to-validate-a-model.qmd",
    "methods reference: dynamics": "methods-and-tools/simulation-paradigms.qmd",
    
    "vol ii.b: ensemble methods": "methods-and-tools/uncertainty-propagation-and-ensembles.qmd",
    "vol ii.b: data assimilation": "methods-and-tools/the-kalman-filter-and-sequential-data-assimilation.qmd",
    "vol ii.b: time-series mechanics": "methods-and-tools/uncertainty-propagation-and-ensembles.qmd",
    
    "scientific computing foundations: python scripting": "scientific-computing/your-first-python-script.qmd",
    "any applied chapter (fire, flood, etc.)": "atmospheric-hazards/flood-frequency-analysis.qmd"
}

def get_title(filepath):
    if not os.path.exists(filepath): return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^title:\s*["\']?(.*?)["\']?$', content, re.MULTILINE)
    if match: return match.group(1).strip()
    return os.path.basename(filepath).replace('.qmd', '').replace('-', ' ').title()

def process():
    nodes = {}
    edges = []
    
    for d in subdirs:
        for fpath in glob.glob(os.path.join(ROOT_DIR, d, "*.qmd")):
            if os.path.basename(fpath).startswith("index"): continue
            
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if not m: continue
            fm = m.group(1)
            
            title = get_title(fpath)
            book_part = None
            m_part = re.search(r'^book-part:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
            if m_part: book_part = m_part.group(1).strip()
            
            prereqs = []
            m_req = re.search(r'^pathway-prerequisites:\n((?:\s+-\s+[^\n]+(?:\n|$))+)', fm, re.MULTILINE)
            if m_req:
                for line in m_req.group(1).split('\n'):
                    if '-' in line:
                        val = re.sub(r'^\s+-\s+"?(.*?)"?$', r'\1', line).strip()
                        if val: prereqs.append(val)
                        
            rel_path = os.path.relpath(fpath, ROOT_DIR)
            nodes[rel_path] = {
                "id": rel_path,
                "title": title,
                "part": book_part,
                "prerequisites_raw": prereqs,
                "status": "ready"
            }

    title_index = {}
    for node_id, data in nodes.items():
        title_index[data["title"].lower()] = node_id

    def resolve_target(req):
        raw = req.lower()
        if raw in ALIASES:
            return ALIASES[raw]
            
        stripped = re.sub(r'^[^:]+:\s*', '', raw).strip()
        if stripped in title_index:
            return title_index[stripped]
            
        for t in title_index:
            if stripped in t or t in stripped:
                return title_index[t]
        return None

    unresolved = []
    node_items = list(nodes.items()) # Snapshot for iteration
    
    for node_id, data in node_items:
        for req in data["prerequisites_raw"]:
            target_id = resolve_target(req)
            if target_id:
                edges.append({"source": target_id, "target": node_id, "type": "prerequisite"})
                if target_id not in nodes:
                    nodes[target_id] = {
                        "id": target_id,
                        "title": target_id.split('/')[-1].replace('.qmd','').replace('-',' ').title(),
                        "part": "Planned",
                        "prerequisites_raw": [],
                        "status": "planned"
                    }
            else:
                unresolved.append({'node': node_id, 'req': req})
                
    graph = {
        "nodes": list(nodes.values()),
        "edges": edges,
        "metadata": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "unresolved_count": len(unresolved)
        }
    }
    
    if unresolved:
        print("WARNING: There are unresolved edges:")
        for r in unresolved:
            print(f"  {r['node']} missing -> {r['req']}")
            
    out_dir = os.path.join(ROOT_DIR, "assets", "data")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "dependency-graph.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2)
        
    print(f"Graph written to {out_file} with {len(nodes)} nodes and {len(edges)} edges.")

if __name__ == "__main__":
    process()
