# Chapter Inventory

## Purpose

This document is the working editorial inventory for the `Learn` book.

It now also supports a broader series decision:

- what remains in the flagship `Computational Geography` book
- what stays as optional depth inside that flagship experience for now
- what is a likely future companion-book candidate

Each chapter is assigned one of three editorial labels:

- `core`: belongs in the beginner-safe main path for smart Grade 10 readers and up
- `extension`: valuable and retained, but better as second-pass or optional depth
- `laboratory`: advanced investigations, project-style chapters, or companion material

This inventory is not a judgment on quality.

It is a judgment about:

- where a chapter belongs in the reader journey
- how much prior confidence it assumes
- whether it should be mandatory on a first pass

## Current Proposed Counts

- `34` core chapters
- `72` extension chapters
- `39` laboratory chapters

## Editorial Notes

- Part index pages are not classified here; this inventory covers chapter pages only.
- The strongest current spine remains:
  - Foundations
  - Environmental Systems
  - Spatial Analysis
- Hazards and Economic Systems contribute selected core chapters.
- Cryosphere, Advanced Remote Sensing, and Machine Learning are currently better positioned as extension material.
- The Laboratory section should be framed as advanced investigations rather than as a required staircase.
- Some current `extension` material is not merely optional depth. It is better understood as future companion-book material, especially in remote sensing, cryosphere, machine learning, and deeper economic systems.
- See [`planning/series-architecture.md`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/planning/series-architecture.md) for the proposed flagship-plus-companions model.

## Proposed Core Path

This is the recommended beginner-safe reading path in rough order.

| Order | Chapter | Path |
|---|---|---|
| 1 | What Is a Spatial Model? | `learn/foundations/what-is-a-spatial-model.qmd` |
| 2 | Linear Change and Rate | `learn/foundations/linear-change-and-rate.qmd` |
| 3 | Exponential Growth and Logarithms | `learn/foundations/exponential-growth-and-logarithms.qmd` |
| 4 | Logistic Growth and Equilibrium | `learn/foundations/logistic-growth-and-equilibrium.qmd` |
| 5 | Digital Elevation Models as Functions | `learn/foundations/digital-elevation-models-as-functions.qmd` |
| 6 | Gradient, Aspect, and Direction of Steepest Descent | `learn/foundations/gradient-aspect-steepest-descent.qmd` |
| 7 | Gravity Models of Trade and Migration | `learn/foundations/gravity-models-trade-migration.qmd` |
| 8 | Spatial Diffusion of Innovation | `learn/foundations/spatial-diffusion-of-innovation.qmd` |
| 9 | Net Radiation and Albedo | `learn/environmental-systems/net-radiation-and-albedo.qmd` |
| 10 | Sensible and Latent Heat Fluxes | `learn/environmental-systems/sensible-and-latent-heat-fluxes.qmd` |
| 11 | Soil Heat Diffusion | `learn/environmental-systems/soil-heat-diffusion.qmd` |
| 12 | Photosynthesis and Light Response | `learn/environmental-systems/photosynthesis-light-response.qmd` |
| 13 | Soil Moisture Dynamics | `learn/environmental-systems/soil-moisture-dynamics.qmd` |
| 14 | Wind Profiles and Atmospheric Turbulence | `learn/environmental-systems/wind-profiles-and-turbulence.qmd` |
| 15 | Temperature and Moisture Gradients | `learn/environmental-systems/temperature-moisture-gradients.qmd` |
| 16 | Vegetation Indices and Remote Sensing | `learn/environmental-systems/vegetation-indices-and-remote-sensing.qmd` |
| 17 | Point-in-Polygon Testing | `learn/spatial-analysis/point-in-polygon-testing.qmd` |
| 18 | Buffer Operations and Distance Fields | `learn/spatial-analysis/buffer-operations.qmd` |
| 19 | Polygon Overlay and Clipping | `learn/spatial-analysis/polygon-overlay-operations.qmd` |
| 20 | Spatial Joins and Proximity Queries | `learn/spatial-analysis/spatial-joins.qmd` |
| 21 | Raster Resampling and Interpolation | `learn/spatial-analysis/raster-resampling-interpolation.qmd` |
| 22 | Map Algebra and Focal Operations | `learn/spatial-analysis/map-algebra-focal-operations.qmd` |
| 23 | Raster Classification and Reclassification | `learn/spatial-analysis/raster-classification.qmd` |
| 24 | Viewshed and Line-of-Sight Analysis | `learn/spatial-analysis/viewshed-line-of-sight.qmd` |
| 25 | Watershed Delineation and Flow Networks | `learn/spatial-analysis/watershed-delineation.qmd` |
| 26 | Fire Weather and Ignition Potential | `learn/atmospheric-hazards/fire-weather-ignition.qmd` |
| 27 | Fire Spread modelling | `learn/atmospheric-hazards/fire-spread-modeling.qmd` |
| 28 | Rainfall Intensity-Duration-Frequency | `learn/atmospheric-hazards/rainfall-intensity-duration.qmd` |
| 29 | Flood Frequency Analysis | `learn/atmospheric-hazards/flood-frequency-analysis.qmd` |
| 30 | Urban Flood modelling and Green Infrastructure | `learn/atmospheric-hazards/urban-flood-modeling.qmd` |
| 31 | The Gravity Model of Trade | `learn/economic-systems/canada-trade-gravity-model.qmd` |
| 32 | The Bid-Rent Model | `learn/economic-systems/urban-bid-rent-model.qmd` |
| 33 | Agglomeration Economies | `learn/economic-systems/urban-agglomeration-economies.qmd` |
| 34 | Spatial Arbitrage and the Law of One Price | `learn/economic-systems/markets-spatial-arbitrage.qmd` |

## Full Inventory By Part

## Foundations

Keep most of this part visible, but reserve the more physics-heavy observation chapters for a second pass.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | What Is a Spatial Model? | `core` |
| 2 | Linear Change and Rate | `core` |
| 3 | Exponential Growth and Logarithms | `core` |
| 4 | Logistic Growth and Equilibrium | `core` |
| 5 | Light Attenuation in a Canopy | `extension` |
| 6 | Spectral Mixing and Sensor Response | `extension` |
| 7 | Solar Geometry and Projection | `extension` |
| 8 | Digital Elevation Models as Functions | `core` |
| 9 | Gradient, Aspect, and Direction of Steepest Descent | `core` |
| 10 | Hydrological Flow as Optimization | `extension` |
| 11 | Gravity Models of Trade and Migration | `core` |
| 12 | Spatial Diffusion of Innovation | `core` |
| 13 | Earth as a Rotating Sphere | `extension` |

## Environmental Systems

Treat orbital and GPS chapters as extension material for the first edition of the beginner path; the process chapters are stronger entry points.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Circular Orbits and Kepler's Third Law | `extension` |
| 2 | Ground Tracks and Orbital Geometry | `extension` |
| 3 | Satellite Overpasses and Visibility | `extension` |
| 4 | How GPS Works | `extension` |
| 5 | Net Radiation and Albedo | `core` |
| 6 | Sensible and Latent Heat Fluxes | `core` |
| 7 | Soil Heat Diffusion | `core` |
| 8 | Photosynthesis and Light Response | `core` |
| 9 | Soil Moisture Dynamics | `core` |
| 10 | Carbon Allocation and Net Primary Productivity | `extension` |
| 11 | Wind Profiles and Atmospheric Turbulence | `core` |
| 12 | Temperature and Moisture Gradients | `core` |
| 13 | Vegetation Indices and Remote Sensing | `core` |
| 14 | Decomposition and Soil Carbon Turnover | `extension` |
| 15 | Nitrogen Cycling and Limitation | `extension` |
| 16 | Phenology and Growing Season Dynamics | `extension` |

## Spatial Analysis

This is one of the strongest beginner-to-intermediate sections and should stay near the center of the core path.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Point-in-Polygon Testing | `core` |
| 2 | Buffer Operations and Distance Fields | `core` |
| 3 | Polygon Overlay and Clipping | `core` |
| 4 | Spatial Joins and Proximity Queries | `core` |
| 5 | Raster Resampling and Interpolation | `core` |
| 6 | Map Algebra and Focal Operations | `core` |
| 7 | Raster Classification and Reclassification | `core` |
| 8 | Viewshed and Line-of-Sight Analysis | `core` |
| 9 | Cost-Distance and Least-Cost Paths | `extension` |
| 10 | Watershed Delineation and Flow Networks | `core` |
| 11 | Supervised Image Classification | `extension` |
| 12 | Change Detection in Satellite Imagery | `extension` |
| 13 | Time Series Analysis of Satellite Data | `extension` |

## Cryosphere and Mountain Systems

Valuable and motivating, but better as extension material after the reader has confidence with core environmental modelling.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Snowpack Energy Balance | `extension` |
| 2 | Snow Accumulation and Melt modelling | `extension` |
| 3 | Snow Water Equivalent Estimation | `extension` |
| 4 | Avalanche Terrain Analysis | `extension` |
| 5 | Glacier Mass Balance | `extension` |
| 6 | Glacial Meltwater Chemistry | `extension` |
| 7 | Glacial Lake Outburst Floods (GLOFs) | `extension` |
| 8 | Slope Stability Analysis | `extension` |
| 9 | Debris Flow modelling | `extension` |
| 10 | Permafrost Thaw and Geohazards | `extension` |

## Advanced Remote Sensing

Highly worthwhile specialist material, but too technical for the beginner-safe spine.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Leaf Optical Properties — the PROSPECT Model | `extension` |
| 2 | Canopy Reflectance — the SAIL Model | `extension` |
| 3 | Hyperspectral Imaging | `extension` |
| 4 | Thermal Infrared Remote Sensing | `extension` |
| 5 | Terrestrial LiDAR Point Clouds | `extension` |
| 6 | Bathymetric LiDAR and Sonar Mapping | `extension` |
| 7 | SAR Fundamentals and Applications | `extension` |
| 9 | Gravity Remote Sensing (GRACE) | `extension` |

## Atmospheric Hazards and Dynamics

A subset belongs in the core path because hazards are motivating and concrete; the more meteorology-heavy chapters can be extensions.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Fire Weather and Ignition Potential | `core` |
| 2 | Fire Spread modelling | `core` |
| 3 | Fire Emissions and Smoke Dispersion | `extension` |
| 4 | Thunderstorm Dynamics and Severe Weather | `extension` |
| 5 | Tornado Formation and Intensity | `extension` |
| 6 | Hail Formation and Forecasting | `extension` |
| 7 | Boundary Layer Turbulence and Wind Profiles | `extension` |
| 8 | Extreme Wind Events and Downbursts | `extension` |
| 9 | Rainfall Intensity-Duration-Frequency | `core` |
| 10 | Flood Frequency Analysis | `core` |
| 11 | Urban Flood modelling and Green Infrastructure | `core` |

## Economic Systems

Distinctive and important, but should be selective in the core path; note the parallel pipeline chapter families that may need consolidation.

| Chapter Number | Chapter | Label |
|---|---|---|
| 1 | Alberta's Crude Oil Pipeline Network | `extension` |
| 2 | NGL and Condensate Pipeline Systems | `extension` |
| 3 | Natural Gas Transmission from Alberta | `extension` |
| 4 | Refined Products Distribution | `extension` |
| 5 | The Integrated Network | `extension` |
| 6 | The Gravity Model of Trade | `core` |
| 7 | Canadian Trade Corridors | `extension` |
| 8 | Port Economics | `extension` |
| 9 | Modal Split and Freight Economics | `extension` |
| 10 | The Integrated Trade Network | `extension` |
| 11 | The Bid-Rent Model | `core` |
| 12 | Agglomeration Economies | `core` |
| 13 | Zipf's Law and the City Size Distribution | `extension` |
| 14 | The Urban Economic Base | `extension` |
| 15 | The Integrated Urban System | `extension` |
| 16 | The Hotelling Rule | `extension` |
| 17 | Supply Cost Curves and Break-Even Prices | `extension` |
| 18 | Royalty Regimes and Resource Rents | `extension` |
| 19 | The Resource Curse | `extension` |
| 20 | The Integrated Resource System | `extension` |
| 21 | Commodity Price Formation | `extension` |
| 22 | Spatial Arbitrage and the Law of One Price | `core` |
| 23 | Futures Markets as Geographic Instruments | `extension` |
| 24 | Price Volatility and Its Geographic Consequences | `extension` |
| 25 | The Integrated Price System | `extension` |
| 26 | Crude Oil Pipelines | `extension` |
| 27 | NGL and Condensate Systems | `extension` |
| 28 | Natural Gas Transmission | `extension` |
| 29 | Refined Products Distribution | `extension` |
| 30 | The Integrated Network | `extension` |
| 31 | Renewable Resource Geography | `extension` |
| 32 | The Economics of Clean Generation | `extension` |
| 33 | Policy, Capital, and the Grid | `extension` |

### Editorial Direction

This part is the strongest candidate for partial extraction into a companion volume.

For the flagship book, keep the gateway human-systems chapters that teach transferable modelling ideas.

For the wider series, treat the larger infrastructure, pricing, and integrated-network families as the backbone of a future economic geography companion.

## Computational Geography Laboratory

This entire part should be framed as advanced investigations, projects, and companion material.

| Chapter Number | Chapter | Label |
|---|---|---|
| 56 | SAR Fundamentals and Applications | `laboratory` |
| 57 | InSAR Deformation Monitoring | `laboratory` |
| 58 | Gravity Remote Sensing (GRACE) | `laboratory` |
| 59 | Passive Microwave Radiometry | `laboratory` |
| 71 | Rock Weathering and Soil Formation | `laboratory` |
| 72 | Soil Erosion and the RUSLE | `laboratory` |
| 73 | Shallow Landslides and Slope Stability | `laboratory` |
| 74 | Sediment Transport in Rivers | `laboratory` |
| 75 | Channel Morphology and Hydraulic Geometry | `laboratory` |
| 76 | Wave Dynamics and Nearshore Transformation | `laboratory` |
| 77 | Longshore Sediment Transport and Coastal Budgets | `laboratory` |
| 78 | Sea Level, Storm Surge, and Coastal Morphodynamics | `laboratory` |
| 95 | Urban Heat Island Dynamics | `laboratory` |
| 96 | Urban Ventilation and Pollutant Dispersion | `laboratory` |
| 97 | Transportation Network Analysis | `laboratory` |
| 98 | Accessibility and Travel Demand modelling | `laboratory` |
| 99 | Land Use Change modelling | `laboratory` |
| 100 | Urban Scaling Laws and City Structure | `laboratory` |
| 101 | Demographic Spatial Dynamics | `laboratory` |
| 102 | Reservoir Operations and Mass Balance | `laboratory` |
| 103 | Stochastic Streamflow and Drought Risk | `laboratory` |
| 104 | Dissolved Oxygen Dynamics and the Streeter-Phelps Model | `laboratory` |
| 105 | Nutrient Dynamics and Lake Eutrophication | `laboratory` |
| 106 | Sediment and Contaminant Transport in Rivers | `laboratory` |
| 107 | Groundwater Contaminant Plumes | `laboratory` |
| 108 | Pump-and-Treat and In-Situ Remediation | `laboratory` |
| 109 | Bayesian Inference for Environmental Models | `laboratory` |
| 110 | Regression for Continuous Spatial Variables | `laboratory` |
| 111 | Dimensionality Reduction for High-Dimensional Geographic Data | `laboratory` |
| 112 | Ensemble Forecasting and Uncertainty Quantification | `laboratory` |
| 113 | The Kalman Filter and Sequential Data Assimilation | `laboratory` |
| 114 | Satellite Data Assimilation in Environmental Models | `laboratory` |
| 115 | Fossil Fuel Combustion Chemistry | `laboratory` |
| 116 | Biomass Burning and Pyrogenic Carbon | `laboratory` |
| 117 | Land Use Change and Deforestation | `laboratory` |
| 118 | Photosynthesis and Gross Primary Production | `laboratory` |
| 119 | Ocean Carbon Uptake and Air-Sea Exchange | `laboratory` |
| 120 | Soil Carbon Storage and Decomposition | `laboratory` |
| 121 | Methanogenesis in Anaerobic Environments | `laboratory` |

## Machine Learning for Geographic Data

Useful later-on material, but not yet substantial enough to function as a full main-sequence part.

| Chapter Number | Chapter | Label |
|---|---|---|
| 2 | Regression for Continuous Variables | `extension` |
| 3 | Dimensionality Reduction: PCA, t-SNE, and UMAP | `extension` |
