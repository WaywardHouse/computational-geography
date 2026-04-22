#!/usr/bin/env python3
"""
Add problem-set metadata frontmatter to all laboratory chapter .qmd files.
Inserts problem-set, pathway-prerequisites, backward-link, and est-hours fields.
Updates section-code and section-title to reflect the new A-F problem set structure.
"""

import re
import os

LAB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "laboratory")

# ── Metadata map: filename → problem set metadata ─────────────────────────────
CHAPTER_META = {
    # ── Problem Set A: Observation & Remote Sensing ──────────────────────────
    "sar-fundamentals-and-applications": {
        "problem-set": "A",
        "section-code": "A",
        "section-title": "Problem Set A: Observation & Remote Sensing Advanced Applications",
        "pathway-prerequisites": [
            "Pathway A: Remote Sensing fundamentals",
            "Pathway A: Atmospheric Effects & Surface Reflectance",
            "Pathway A: Raster Classification",
        ],
        "backward-link": "Pathway A, Raster Classification — SAR is an all-weather alternative",
        "est-hours": 10,
        "lab-level": "Advanced",
    },
    "insar-deformation-monitoring": {
        "problem-set": "A",
        "section-code": "A",
        "section-title": "Problem Set A: Observation & Remote Sensing Advanced Applications",
        "pathway-prerequisites": [
            "Pathway A: SAR Fundamentals (Problem Set A, Investigation 1)",
            "Pathway A: Spectral & Temporal Resolution",
        ],
        "backward-link": "Pathway A, Raster Classification — extends SAR to surface deformation",
        "est-hours": 12,
        "lab-level": "Advanced",
    },
    "gravity-remote-sensing-grace": {
        "problem-set": "A",
        "section-code": "A",
        "section-title": "Problem Set A: Observation & Remote Sensing Advanced Applications",
        "pathway-prerequisites": [
            "Pathway A: Orbital Mechanics (Companion 1)",
            "Pathway A: Spectral & Temporal Resolution",
        ],
        "backward-link": "Pathway A, Spectral & Temporal Resolution — GRACE extends temporal monitoring",
        "est-hours": 11,
        "lab-level": "Advanced",
    },
    "passive-microwave-radiometry": {
        "problem-set": "A",
        "section-code": "A",
        "section-title": "Problem Set A: Observation & Remote Sensing Advanced Applications",
        "pathway-prerequisites": [
            "Pathway A: Thermal Infrared Remote Sensing",
            "Pathway A: Vegetation Indices & Remote Sensing",
        ],
        "backward-link": "Pathway A, Vegetation Indices — microwave offers all-weather alternative",
        "est-hours": 10,
        "lab-level": "Advanced",
    },

    # ── Problem Set B: Water Systems & Hydrology ─────────────────────────────
    "reservoir-operations-and-mass-balance": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Watershed Delineation",
            "Scientific Computing Foundations: Python scripting",
        ],
        "backward-link": "Pathway B, Watershed Delineation — apply mass balance to a real reservoir system",
        "est-hours": 12,
        "lab-level": "Advanced",
    },
    "stochastic-streamflow-and-drought-risk": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Watershed Delineation",
            "Vol II.B: Ensemble Methods",
            "Methods Reference: Uncertainty Propagation",
        ],
        "backward-link": "Vol II.B, Time-Series Mechanics — practice with real USGS data",
        "est-hours": 15,
        "lab-level": "Advanced",
    },
    "dissolved-oxygen-dynamics-and-the-streeter-phelps-model": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Soil Moisture Dynamics",
            "Methods Reference: Differential Equations",
        ],
        "backward-link": "Pathway B, Soil Moisture — extend to coupled water-quality dynamics",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "nutrient-dynamics-and-lake-eutrophication": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Soil Moisture Dynamics",
            "Pathway B: Photosynthesis & Light Response",
            "Methods Reference: Differential Equations",
        ],
        "backward-link": "Pathway B, Soil Moisture — extend to coupled nutrient-water dynamics",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "sediment-and-contaminant-transport-in-rivers": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Watershed Delineation",
            "Pathway B: Wind Profiles & Turbulence",
            "Methods Reference: Dynamics",
        ],
        "backward-link": "Pathway B, Watershed Delineation — model sediment in your basin",
        "est-hours": 13,
        "lab-level": "Advanced",
    },
    "groundwater-contaminant-plumes": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Soil Heat Diffusion",
            "Pathway B: Soil Moisture Dynamics",
            "Methods Reference: PDEs & Numerical Methods",
        ],
        "backward-link": "Pathway B, Soil Heat Diffusion — apply diffusion physics to contaminants",
        "est-hours": 14,
        "lab-level": "Advanced",
    },
    "pump-and-treat-and-in-situ-remediation": {
        "problem-set": "B",
        "section-code": "B",
        "section-title": "Problem Set B: Water Systems & Hydrology",
        "pathway-prerequisites": [
            "Pathway B: Soil Moisture Dynamics",
            "Laboratory: Groundwater Contaminant Plumes",
        ],
        "backward-link": "Laboratory: Groundwater Contaminant Plumes — extends to remediation design",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },

    # ── Problem Set C: Geomorphology & Hazards ───────────────────────────────
    "rock-weathering-and-soil-formation": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Net Radiation & Albedo",
        ],
        "backward-link": "Pathway B, Net Radiation & Albedo — heat drives weathering",
        "est-hours": 9,
        "lab-level": "Intermediate",
    },
    "soil-erosion-and-the-rusle": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Soil Moisture Dynamics",
            "Pathway B: Watershed Delineation",
            "Pathway C: Rainfall Intensity-Duration-Frequency",
        ],
        "backward-link": "Pathway B, Watershed Delineation — predict erosion in your watershed",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "shallow-landslides-and-slope-stability": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Digital Elevation Models",
            "Pathway B: Soil Moisture Dynamics",
            "Pathway C: Rainfall Intensity-Duration-Frequency",
        ],
        "backward-link": "Pathway B, Gradient/Aspect — use terrain derivatives for hazard mapping",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "sediment-transport-in-rivers": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Watershed Delineation",
            "Methods Reference: Dynamics",
        ],
        "backward-link": "Pathway B, Watershed Delineation — model sediment in your basin",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "channel-morphology-and-hydraulic-geometry": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Watershed Delineation",
            "Methods Reference: Numerical Methods",
        ],
        "backward-link": "Pathway B, Watershed Delineation — channel form as a product of process",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "wave-dynamics-and-nearshore-transformation": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Wind Profiles & Turbulence",
            "Pathway B: Temperature-Moisture Gradients",
            "Methods Reference: Numerical Methods",
        ],
        "backward-link": "Pathway B, Wind Profiles — wave generation and propagation",
        "est-hours": 13,
        "lab-level": "Advanced",
    },
    "longshore-sediment-transport-and-coastal-budgets": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Wind Profiles & Turbulence",
            "Laboratory: Wave Dynamics & Nearshore Transformation",
        ],
        "backward-link": "Pathway B, Wind Profiles — coastal sediment budgets driven by wave energy",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "sea-level-storm-surge-and-coastal-morphodynamics": {
        "problem-set": "C",
        "section-code": "C",
        "section-title": "Problem Set C: Geomorphology & Hazards",
        "pathway-prerequisites": [
            "Pathway B: Wind Profiles & Turbulence",
            "Pathway B: Temperature-Moisture Gradients",
            "Methods Reference: Numerical Methods",
        ],
        "backward-link": "Pathway B, Wind Profiles — surge modeling from atmospheric forcing",
        "est-hours": 14,
        "lab-level": "Advanced",
    },

    # ── Problem Set D: Urban Systems & Infrastructure ────────────────────────
    "urban-heat-island-dynamics": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway B: Net Radiation & Albedo",
            "Pathway B: Sensible & Latent Heat Fluxes",
            "Pathway A: Thermal Infrared Remote Sensing",
        ],
        "backward-link": "Pathway B, Sensible/Latent Heat — apply energy balance to cities",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "urban-ventilation-and-pollutant-dispersion": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway B: Wind Profiles & Turbulence",
            "Pathway C: Urban Applications",
        ],
        "backward-link": "Pathway B, Wind Profiles — apply turbulence physics to urban canyons",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "transportation-network-analysis": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway C: Gravity Models — Trade & Migration",
            "Pathway C: Urban Bid-Rent Models",
        ],
        "backward-link": "Pathway C, Gravity Models — model travel demand in your city",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "accessibility-and-travel-demand-modeling": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway C: Gravity Models — Trade & Migration",
            "Pathway C: Urban Agglomeration Economies",
        ],
        "backward-link": "Pathway C, Gravity Models — spatial accessibility and transport equity",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "land-use-change-modeling": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway A: Raster Classification",
            "Pathway A: Change Detection",
            "Pathway C: Urban Bid-Rent Models",
        ],
        "backward-link": "Pathway A, Change Detection — predict future land use from past change",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "urban-scaling-laws-and-city-structure": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway C: Urban Agglomeration Economies",
            "Pathway C: Gravity Models — Trade & Migration",
        ],
        "backward-link": "Pathway C, Urban Agglomeration — investigate scaling in your region",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "demographic-spatial-dynamics": {
        "problem-set": "D",
        "section-code": "D",
        "section-title": "Problem Set D: Urban Systems & Infrastructure",
        "pathway-prerequisites": [
            "Pathway C: Urban Bid-Rent Models",
            "Methods Reference: Spatial Statistics",
        ],
        "backward-link": "Pathway C, Urban Bid-Rent — model population change in space",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },

    # ── Problem Set E: Inference & Methods ───────────────────────────────────
    "bayesian-inference-for-environmental-models": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Methods Reference: Bayesian Updating",
            "Any applied chapter (fire, flood, etc.)",
        ],
        "backward-link": "Vol II.B, Data Assimilation — deep dive into Bayesian methods",
        "est-hours": 12,
        "lab-level": "Advanced",
    },
    "regression-for-continuous-spatial-variables": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Pathway A: Raster Classification",
            "Methods Reference: How to Choose a Model",
        ],
        "backward-link": "Pathway A, Classification — advanced statistical validation",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "dimensionality-reduction-for-high-dimensional-geographic-data": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Pathway A: Multispectral Imagery & Band Interpretation",
            "Methods Reference: How to Choose a Model",
        ],
        "backward-link": "Pathway A, Vegetation Indices — extract features from high-dimensional imagery",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "ensemble-forecasting-and-uncertainty-quantification": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Vol II.B: Ensemble Methods",
            "Methods Reference: Uncertainty Propagation",
        ],
        "backward-link": "Vol II.B, Time-Series Mechanics — practice ensemble thinking with real data",
        "est-hours": 12,
        "lab-level": "Advanced",
    },
    "the-kalman-filter-and-sequential-data-assimilation": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Vol II.B: Data Assimilation",
            "Methods Reference: Bayesian Updating",
        ],
        "backward-link": "Vol II.B, Data Assimilation — operational forecasting implementation",
        "est-hours": 13,
        "lab-level": "Advanced",
    },
    "satellite-data-assimilation-in-environmental-models": {
        "problem-set": "E",
        "section-code": "E",
        "section-title": "Problem Set E: Inference & Methods",
        "pathway-prerequisites": [
            "Pathway A: Remote Sensing fundamentals",
            "Vol II.B: Data Assimilation",
        ],
        "backward-link": "Vol II.B, Data Assimilation — assimilate real satellite observations",
        "est-hours": 12,
        "lab-level": "Advanced",
    },

    # ── Problem Set F: Biogeochemical Cycles ─────────────────────────────────
    "Fossil-Fuel-Combustion-Chemistry": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway C: Markets & Spatial Arbitrage",
        ],
        "backward-link": "Companion 3: Energy Systems — understand emissions from sources",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "Biomass-Burning-and-Pyrogenic-Carbon": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway C: Fire Spread Modeling",
            "Pathway B: Photosynthesis & Light Response",
        ],
        "backward-link": "Pathway C, Fire Spread — calculate carbon emissions from fire",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "Land-Use-Change-and-Deforestation": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway A: Change Detection",
            "Pathway B: Photosynthesis & Light Response",
        ],
        "backward-link": "Pathway A, Change Detection — quantify carbon loss from deforestation",
        "est-hours": 12,
        "lab-level": "Intermediate",
    },
    "Photosynthesis-and-Gross-Primary-Production": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway B: Photosynthesis & Light Response",
            "Pathway A: Vegetation Indices",
        ],
        "backward-link": "Pathway B, Photosynthesis — validate GPP with field measurements",
        "est-hours": 10,
        "lab-level": "Intermediate",
    },
    "Ocean-Carbon-Uptake-and-Air-Sea-Exchange": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway B: Temperature-Moisture Gradients",
            "Pathway A: Water Optics (Companion 1)",
        ],
        "backward-link": "Pathway B, Temperature-Moisture Gradients — ocean carbon in global cycles",
        "est-hours": 11,
        "lab-level": "Intermediate",
    },
    "Soil-Carbon-Storage-and-Decomposition": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway B: Soil Heat Diffusion",
            "Pathway B: Soil Moisture Dynamics",
            "Pathway B: Photosynthesis & Light Response",
        ],
        "backward-link": "Pathway B, Soil Heat — model soil carbon under climate change",
        "est-hours": 9,
        "lab-level": "Intermediate",
    },
    "Methanogenesis-in-Anaerobic-Environments": {
        "problem-set": "F",
        "section-code": "F",
        "section-title": "Problem Set F: Biogeochemical Cycles",
        "pathway-prerequisites": [
            "Pathway B: Soil Moisture Dynamics",
        ],
        "backward-link": "Pathway B, Soil Moisture — model methane from wetlands",
        "est-hours": 8,
        "lab-level": "Intermediate",
    },
}


def build_new_fields(meta: dict) -> str:
    """Build YAML block for new metadata fields."""
    ps = meta["problem-set"]
    level = meta["lab-level"]
    hours = meta["est-hours"]
    backward = meta["backward-link"]
    prereqs = meta["pathway-prerequisites"]

    prereq_lines = "\n".join(f"  - \"{p}\"" for p in prereqs)
    return (
        f"problem-set: \"{ps}\"\n"
        f"lab-level: \"{level}\"\n"
        f"est-hours: {hours}\n"
        f"pathway-prerequisites:\n{prereq_lines}\n"
        f"backward-link: \"{backward}\"\n"
    )


def update_chapter(filepath: str, stem: str) -> None:
    """Insert new metadata fields into the chapter frontmatter."""
    meta = CHAPTER_META.get(stem)
    if meta is None:
        print(f"  SKIP (no metadata): {stem}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Bail if already updated
    if "problem-set:" in content:
        print(f"  SKIP (already has problem-set): {stem}")
        return

    # Build new fields block
    new_fields = build_new_fields(meta)

    # Insert after the line that has 'book-part: laboratory'
    # Find that line, insert new_fields immediately after
    pattern = r"(book-part: laboratory\n)"
    replacement = r"\1" + new_fields

    new_content, count = re.subn(pattern, replacement, content)
    if count == 0:
        # Try inserting before closing --- of frontmatter
        pattern2 = r"(\ndifficulty:)"
        replacement2 = "\n" + new_fields.rstrip("\n") + r"\1"
        new_content, count2 = re.subn(pattern2, replacement2, content)
        if count2 == 0:
            print(f"  WARN (insertion point not found): {stem}")
            return

    # Also update section-code and section-title
    new_content = re.sub(
        r"section-code: .*",
        f"section-code: {meta['section-code']}",
        new_content
    )
    new_content = re.sub(
        r"section-title: .*",
        f"section-title: {meta['section-title']}",
        new_content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  OK: {stem} → Problem Set {meta['problem-set']}")


def main():
    updated = 0
    skipped = 0
    for stem in CHAPTER_META:
        fname = stem + ".qmd"
        fpath = os.path.join(LAB_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  MISSING file: {fpath}")
            skipped += 1
            continue
        update_chapter(fpath, stem)
        updated += 1

    print(f"\nDone. Processed {updated} chapters, skipped {skipped}.")


if __name__ == "__main__":
    main()
