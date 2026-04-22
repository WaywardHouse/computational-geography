#!/usr/bin/env python3
"""
Add pathway-prerequisites, next-steps, and methods-anchor frontmatter to core pathway chapters.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATHWAYS = {
    "A": [
        "foundations/what-is-remote-sensing.qmd",
        "foundations/spatial-spectral-temporal-and-radiometric-resolution.qmd",
        "foundations/atmospheric-effects-and-surface-reflectance.qmd",
        "environmental-systems/multispectral-imagery-and-band-interpretation.qmd",
        "environmental-systems/vegetation-indices-and-remote-sensing.qmd",
        "spatial-analysis/raster-resampling-interpolation.qmd",
        "spatial-analysis/raster-classification.qmd",
        "spatial-analysis/change-detection.qmd"
    ],
    "B": [
        "foundations/digital-elevation-models-as-functions.qmd",
        "foundations/gradient-aspect-steepest-descent.qmd",
        "environmental-systems/net-radiation-and-albedo.qmd",
        "environmental-systems/sensible-and-latent-heat-fluxes.qmd",
        "environmental-systems/soil-heat-diffusion.qmd",
        "environmental-systems/photosynthesis-light-response.qmd",
        "environmental-systems/soil-moisture-dynamics.qmd",
        "environmental-systems/wind-profiles-and-turbulence.qmd",
        "environmental-systems/temperature-moisture-gradients.qmd",
        "foundations/hydrological-flow-as-optimization.qmd",
        "spatial-analysis/watershed-delineation.qmd",
        "environmental-systems/phenology-and-growing-season.qmd"
    ],
    "C": [
        "atmospheric-hazards/fire-weather-ignition.qmd",
        "atmospheric-hazards/fire-spread-modeling.qmd",
        "atmospheric-hazards/rainfall-intensity-duration.qmd",
        "atmospheric-hazards/flood-frequency-analysis.qmd",
        "atmospheric-hazards/urban-flood-modeling.qmd",
        "economic-systems/canada-trade-gravity-model.qmd",
        "economic-systems/urban-bid-rent-model.qmd",
        "economic-systems/urban-agglomeration-economies.qmd",
        "economic-systems/markets-spatial-arbitrage.qmd"
    ]
}

METHODS_ANCHORS = {
    "atmospheric-effects-and-surface-reflectance": "uncertainty",
    "multispectral-imagery-and-band-interpretation": "model-choice",
    "raster-classification": "validation",
    "soil-moisture-dynamics": "validation",
    "soil-heat-diffusion": "numerical-methods",
    "net-radiation-and-albedo": "sensitivity",
    "photosynthesis-light-response": "parameter-fitting",
    "fire-spread-modeling": "model-choice", # and validation
    "canada-trade-gravity-model": "statistical-testing",
    "urban-agglomeration-economies": "causal-inference",
}

LAB_LINKS = {
    "vegetation-indices-and-remote-sensing": [
        "Laboratory: Passive Microwave Radiometry (Problem Set A)",
        "Laboratory: Photosynthesis and Gross Primary Production (Problem Set F)"
    ],
    "raster-classification": [
        "Laboratory: SAR Fundamentals (Problem Set A)",
        "Laboratory: Regression for Continuous Spatial Variables (Problem Set E)",
        "Laboratory: Land Use Change Modeling (Problem Set D)"
    ],
    "change-detection": [
        "Laboratory: Land Use Change Modeling (Problem Set D)",
        "Laboratory: Land Use Change & Deforestation (Problem Set F)"
    ],
    "watershed-delineation": [
        "Laboratory: Reservoir Operations (Problem Set B)",
        "Laboratory: Stochastic Streamflow (Problem Set B)",
        "Laboratory: Sediment and Contaminant Transport (Problem Set B)",
        "Laboratory: Soil Erosion and the RUSLE (Problem Set C)",
        "Laboratory: Sediment Transport in Rivers (Problem Set C)",
        "Laboratory: Channel Morphology (Problem Set C)"
    ],
    "soil-moisture-dynamics": [
        "Laboratory: Dissolved Oxygen Dynamics (Problem Set B)",
        "Laboratory: Nutrient Dynamics and Lake Eutrophication (Problem Set B)",
        "Laboratory: Groundwater Contaminant Plumes (Problem Set B)",
        "Laboratory: Pump and Treat Remediation (Problem Set B)",
        "Laboratory: Soil Erosion and the RUSLE (Problem Set C)",
        "Laboratory: Shallow Landslides (Problem Set C)",
        "Laboratory: Soil Carbon Storage (Problem Set F)",
        "Laboratory: Methanogenesis (Problem Set F)"
    ],
    "net-radiation-and-albedo": [
        "Laboratory: Rock Weathering (Problem Set C)",
        "Laboratory: Urban Heat Island Dynamics (Problem Set D)"
    ],
    "sensible-and-latent-heat-fluxes": [
        "Laboratory: Urban Heat Island Dynamics (Problem Set D)"
    ],
    "soil-heat-diffusion": [
        "Laboratory: Groundwater Contaminant Plumes (Problem Set B)",
        "Laboratory: Soil Carbon Storage (Problem Set F)"
    ],
    "wind-profiles-and-turbulence": [
        "Laboratory: Sediment Transport in Rivers (Problem Set B)",
        "Laboratory: Wave Dynamics & Nearshore Transformation (Problem Set C)",
        "Laboratory: Longshore Sediment Transport (Problem Set C)",
        "Laboratory: Sea Level & Coastal Morphodynamics (Problem Set C)",
        "Laboratory: Urban Ventilation (Problem Set D)"
    ],
    "temperature-moisture-gradients": [
        "Laboratory: Wave Dynamics & Nearshore Transformation (Problem Set C)",
        "Laboratory: Sea Level & Coastal Morphodynamics (Problem Set C)",
        "Laboratory: Ocean Carbon Uptake (Problem Set F)"
    ],
    "photosynthesis-light-response": [
        "Laboratory: Nutrient Dynamics and Lake Eutrophication (Problem Set B)",
        "Laboratory: Biomass Burning (Problem Set F)",
        "Laboratory: Land Use Change and Deforestation (Problem Set F)",
        "Laboratory: Photosynthesis and GPP (Problem Set F)",
        "Laboratory: Soil Carbon Storage (Problem Set F)"
    ],
    "fire-spread-modeling": [
        "Laboratory: Biomass Burning (Problem Set F)"
    ],
    "urban-bid-rent-model": [
        "Laboratory: Transportation Network Analysis (Problem Set D)",
        "Laboratory: Land Use Change Modeling (Problem Set D)",
        "Laboratory: Demographic & Spatial Dynamics (Problem Set D)"
    ],
    "urban-agglomeration-economies": [
        "Laboratory: Accessibility & Travel Demand (Problem Set D)",
        "Laboratory: Urban Scaling Laws (Problem Set D)"
    ],
    "multispectral-imagery-and-band-interpretation": [
        "Laboratory: Dimensionality Reduction for Geographic Data (Problem Set E)"
    ]
}

def get_title(filepath):
    """Extract the title from a qmd file's frontmatter."""
    if not os.path.exists(filepath):
        return os.path.basename(filepath).replace('.qmd', '').replace('-', ' ').title()
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^title:\s*["\']?(.*?)["\']?$', content, re.MULTILINE)
    if match:
        return match.group(1)
    return os.path.basename(filepath).replace('.qmd', '').replace('-', ' ').title()

def update_chapter(filepath, pathway_code, prev_title, next_title):
    """Update frontmatter for a single chapter."""
    if not os.path.exists(filepath):
        print(f"  MISSING: {filepath}")
        # Create a dummy file if it doesn't exist for the sake of completeness (we shouldn't hit this normally)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\ntitle: \"{os.path.basename(filepath).title()}\"\n---\n")
            
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "pathway-prerequisites:" in content:
        print(f"  SKIP (already has frontmatter): {filepath}")
        return

    stem = os.path.basename(filepath).replace('.qmd', '')
    
    # Build payload
    lines = []
    lines.append("pathway-prerequisites:")
    if prev_title:
        lines.append(f"  - \"{prev_title}\"")
    else:
        lines.append(f"  - \"Foundations: Linear Change and Rate\"")
        
    lines.append("next-steps:")
    if next_title:
        lines.append(f"  - \"Pathway {pathway_code}: {next_title}\"")
    
    if stem in LAB_LINKS:
        for lab in LAB_LINKS[stem]:
            lines.append(f"  - \"{lab}\"")
            
    if stem in METHODS_ANCHORS:
        lines.append(f"methods-anchor: \"{METHODS_ANCHORS[stem]}\"")
        
    payload = "\n".join(lines) + "\n"
    
    # insert before the closing --- of frontmatter, or at the end of frontmatter
    # assuming standard format:
    # ---
    # title: ...
    # ---
    
    parts = content.split("---", 2)
    if len(parts) >= 3: # valid frontmatter
        new_frontmatter = parts[1].rstrip() + "\n" + payload
        new_content = "---" + new_frontmatter + "---" + parts[2]
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  OK: {filepath}")
    else:
        print(f"  WARN: Could not parse frontmatter in {filepath}")

def main():
    for pw_code, chapters in PATHWAYS.items():
        print(f"Processing Pathway {pw_code}...")
        for i, rel_path in enumerate(chapters):
            full_path = os.path.join(ROOT_DIR, rel_path)
            
            # Figure out prev/next titles
            if i > 0:
                prev_path = os.path.join(ROOT_DIR, chapters[i-1])
                prev_title = f"Pathway {pw_code}: {get_title(prev_path)}"
            else:
                prev_title = None
                
            if i < len(chapters) - 1:
                next_path = os.path.join(ROOT_DIR, chapters[i+1])
                next_title = get_title(next_path)
            else:
                next_title = None
                
            update_chapter(full_path, pw_code, prev_title, next_title)
            
if __name__ == "__main__":
    main()
