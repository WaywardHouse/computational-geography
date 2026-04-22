#!/usr/bin/env python3
"""
Generate the 4 Quarto companion book configurations.
"""

import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_config(filename, output_dir, title, subtitle, parts):
    content = f"""project:
  type: book
  output-dir: {output_dir}
  pre-render:
    - ./scripts/prepare-book-output.sh {output_dir}
  post-render:
    - ./scripts/sync-book-assets.sh {output_dir}

book:
  title: "{title}"
  subtitle: "{subtitle}"
  author: "Paul Hobson"
  search: true
  chapters:
"""
    for part in parts:
        if isinstance(part, str):
            content += f"    - {part}\n"
        elif isinstance(part, dict):
            part_title = part['part']
            content += f"    - part: \"{part_title}\"\n      chapters:\n"
            for chap in part['chapters']:
                content += f"        - {chap}\n"
                
    content += """
format:
  html:
    theme: none
    css:
      - assets/css/quarto-wayward.css
    html-math-method: katex
    toc: true
    number-sections: false
    include-in-header:
      - assets/includes/quarto-head.html
    include-after-body:
      - assets/includes/quarto-body.html

execute:
  freeze: auto
"""
    
    with open(os.path.join(ROOT_DIR, filename), "w") as f:
        f.write(content)


companion1 = [
    "index.qmd",
    "advanced-remote-sensing/index.qmd",
    {
        "part": "Advanced Remote Sensing",
        "chapters": [
            "advanced-remote-sensing/prospect-leaf-optical-properties.qmd",
            "advanced-remote-sensing/sail-canopy-reflectance.qmd",
            "advanced-remote-sensing/hyperspectral-imaging.qmd",
            "advanced-remote-sensing/thermal-infrared-remote-sensing.qmd",
            "advanced-remote-sensing/lidar-point-clouds.qmd",
            "advanced-remote-sensing/bathymetric-lidar-sonar.qmd",
            "advanced-remote-sensing/sar-fundamentals.qmd",
            "advanced-remote-sensing/gravity-remote-sensing.qmd",
        ]
    },
    {
        "part": "Orbital Mechanics",
        "chapters": [
            "environmental-systems/circular-orbits-and-keplers-third-law.qmd",
            "environmental-systems/ground-tracks-and-orbital-geometry.qmd",
            "environmental-systems/satellite-overpasses-and-visibility.qmd",
            "environmental-systems/how-gps-works.qmd",
        ]
    }
]

companion2 = [
    "index.qmd",
    "cryosphere-and-mountain-systems/index.qmd",
    {
        "part": "Cryosphere & Mountain Systems",
        "chapters": [
            "cryosphere-and-mountain-systems/snowpack-energy-balance.qmd",
            "cryosphere-and-mountain-systems/snow-accumulation-melt-modeling.qmd",
            "cryosphere-and-mountain-systems/swe-estimation-methods.qmd",
            "cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd",
            "cryosphere-and-mountain-systems/glacier-mass-balance.qmd",
            "cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd",
            "cryosphere-and-mountain-systems/glacial-lake-outburst-floods.qmd",
            "cryosphere-and-mountain-systems/slope-stability-analysis.qmd",
            "cryosphere-and-mountain-systems/debris-flow-modeling.qmd",
            "cryosphere-and-mountain-systems/permafrost-thaw-geohazards.qmd",
        ]
    }
]

companion3 = [
    "index.qmd",
    "economic-systems/index.qmd",
    {
        "part": "Trade & Economic Networks",
        "chapters": [
            "economic-systems/canada-trade-gravity-model.qmd", # Reference here
            "economic-systems/canada-trade-corridors.qmd",
            "economic-systems/canada-port-economics.qmd",
            "economic-systems/canada-freight-modal-split.qmd",
            "economic-systems/canada-integrated-trade-network.qmd",
            "economic-systems/urban-city-size-zipf.qmd",
            "economic-systems/urban-economic-base.qmd",
            "economic-systems/urban-integrated-system.qmd",
            "economic-systems/markets-commodity-price-formation.qmd",
            "economic-systems/markets-futures-geographic-instruments.qmd",
            "economic-systems/markets-price-volatility.qmd",
            "economic-systems/markets-integrated-price-system.qmd" # Might not exactly match
        ]
    },
    {
        "part": "Resource Systems",
        "chapters": [
            "economic-systems/resource-hotelling-rule.qmd",
            "economic-systems/resource-supply-cost-curves.qmd",
            "economic-systems/resource-royalty-regimes.qmd",
            "economic-systems/resource-curse.qmd",
            "economic-systems/resource-integrated-system.qmd",
            "economic-systems/alberta-pipeline-crude-oil.qmd",
            "economic-systems/alberta-pipeline-ngl-condensate.qmd",
            "economic-systems/alberta-pipeline-natural-gas.qmd",
            "economic-systems/alberta-pipeline-refined-products.qmd",
            "economic-systems/alberta-pipeline-integrated-network.qmd",
            "economic-systems/crude-oil-pipelines.qmd",
            "economic-systems/ngl-condensate-systems.qmd",
            "economic-systems/natural-gas-transmission.qmd",
            "economic-systems/refined-products-distribution.qmd",
            "economic-systems/integrated-network.qmd",
        ]
    },
    {
        "part": "Renewable Energy & Transitions",
        "chapters": [
            "economic-systems/alberta-renewable-resource-geography.qmd",
            "economic-systems/alberta-renewable-economics.qmd",
            "economic-systems/alberta-renewable-policy-demand.qmd"
        ]
    }
]

companion4 = [
    "index.qmd",
    "machine-learning/index.qmd",
    {
        "part": "Geographic Machine Learning & Inference",
        "chapters": [
            "machine-learning/regression-continuous-variables.qmd",
            "machine-learning/dimensionality-reduction-pca-tsne-umap.qmd",
            "methods-and-tools/bayesian-updating-and-geographic-inference.qmd",
            "methods-and-tools/causal-inference-for-geographic-questions.qmd"
        ]
    }
]

def main():
    write_config("_quarto-companion-1-remote-sensing.yml", 
                "_book-companion-base-1",
                "Computational Geography", 
                "Companion 1: Remote Sensing for Environmental Modelling", 
                companion1)
                
    write_config("_quarto-companion-2-cryosphere.yml", 
                "_book-companion-base-2",
                "Computational Geography", 
                "Companion 2: Cryosphere & Mountain Systems", 
                companion2)
                
    write_config("_quarto-companion-3-economics.yml", 
                "_book-companion-base-3",
                "Computational Geography", 
                "Companion 3: Economic Geography & Infrastructure Systems", 
                companion3)
                
    write_config("_quarto-companion-4-ml-inference.yml", 
                "_book-companion-base-4",
                "Computational Geography", 
                "Companion 4: Geographic Machine Learning & Inference", 
                companion4)
                
    # Also create the missing directories or chapters if mentioned but not present? I've verified most of the files are present.
    print("Configs generated.")

if __name__ == "__main__":
    main()
