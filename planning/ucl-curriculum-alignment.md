# Computational Geography Vol I–II Alignment with UCL Remote Sensing & Environmental Mapping MSc

## Strategy: Hydrology as Vol II Spine

Vol II uses **hydrology** as the connective thread across both Vol II.A (standstill) and Vol II.B (dynamics):
- Integrates multiple Vol I systems (terrain, soil, vegetation, atmosphere, energy balance)
- Has strong remote sensing footprint (precipitation, snow, soil moisture, ET, land cover)
- Bridges mechanics → observation → real-time forecasting (natural validation arc)
- Aligns with Mat's optional "Surface Water Modelling" module
- Supports data assimilation pedagogy (streamflow assimilation is standard DA testbed)

This keeps the Barnsley spirit: deep understanding of process mechanics, then validation against observations, then prediction forward in time.

---

## Vol I → Mat's Program Mapping

### Direct Coverage (Vol I chapters → UCL compulsory modules)

| Vol I Chapter | UCL Module Alignment |
|---|---|
| Getting Started (all) | **Analytical & Numerical Methods** + **Scientific Computing** foundations |
| Foundations: spatial models, CRS, DEM, gradient | **Geospatial Science** + **Principles & Practice of Remote Sensing** (observation geometry) |
| Foundations: remote sensing basics, resolution, atmospheric effects | **Principles & Practice of Remote Sensing** (core) |
| Spatial Analysis (all chapters) | **Geospatial Science** + **Environmental GIS** (optional) |
| Environmental Systems (radiation, heat, moisture, vegetation indices) | **Principles & Practice of Remote Sensing** + practical data interpretation |
| Atmospheric Hazards (fire, flood) | Applied case studies bridging mechanics → observation |
| Economic Systems | Advanced spatial analysis (gravity, agglomeration patterns from data) |

### Vol I Strengths Relative to UCL
- **Mechanistic foundation first**: Students understand *why* a vegetation index works before applying it
- **Equation-to-code clarity**: Direct path from differential equations to spatial operations
- **Spatial analysis rigor**: Vector/raster operations are taught as mathematical operations, not just GIS buttons
- **Applied hazard modeling**: Fire spread and flood routing show coupled-process thinking

---

## Gaps: UCL Topics Not Covered in Vol I

| Topic | UCL Module(s) | Why Matters | Vol II Opportunity |
|---|---|---|---|
| **Carbon cycle & monitoring** | Terrestrial Carbon: Modelling and Monitoring | Core to climate/land-use research; MODIS/Sentinel carbon products | Vol II.A: Static carbon stocks from imagery; Vol II.B: Time-series disturbance recovery |
| **Climate system dynamics** | Climate Modelling | Large-scale feedbacks (not in Vol I's local focus) | Out of scope for Vol II (needs Vol III?); reference in Vol II climate-hazards sections |
| **Data visualization & cartography** | Cartography and Data Visualisation | Communication layer missing | Vol II.A: Validation visualization; Vol II.B: Uncertainty/ensemble mapping |
| **Spatio-temporal statistics** | Spatial-Temporal Data Analysis and Data Mining | Formal frameworks for time-series validation | Vol II.B: Cross-validation, autocorrelation, change detection |
| **Advanced sensors** | Reality Capture, Sensors and Location, Precision 3D Sensing | LiDAR, UAV, 3D reality capture workflows | Vol II.A: LiDAR DEM validation; Vol II.B: Multi-temporal point clouds |
| **Coastal processes** | Coastal Geohazards (optional) | Wave/tide/surge modeling at boundaries | Defer (requires boundary condition complexity not in Vol I) |
| **Surface hydrology** | Surface Water Modelling (optional) | River routing, flow accumulation operational workflows | Vol II.A: Static watersheds & DEM hydrology; Vol II.B: Time-series runoff forecasting |
| **Data assimilation** | Implicit in all UCL modules | Feeding observations back into running models | **Vol II.B core**: Ensemble Kalman filter concepts; particle filters for state correction |

---

## Proposed Vol II Structure

**Connective spine**: Hydrology (water balance, infiltration, runoff) runs through both Vol II.A and Vol II.B, integrating multiple Vol I systems (terrain, soil, vegetation, atmosphere).

### Volume II.A: Standstill Observation & Validation
**Goal**: Validate Vol I mechanics against static observations (synthetic → real data)

#### A.1 Data & Uncertainty (2–3 chapters)
- Synthetic data generation (add noise to equations from Vol I)
- Field measurement networks and sampling design (weather stations, soil moisture sensors, stream gauges)
- Accuracy assessment, confusion matrices, cross-validation frameworks
- **Hydrology anchor**: Design a watershed observation network; validate soil moisture equation against sensors

#### A.2 Static Remote Sensing Interpretation (3–4 chapters)
- Single-date image classification (supervised, unsupervised)
- Accuracy of vegetation indices (NDVI, EVI, NDMI) against field plots
- Terrain analysis: DEM accuracy, slope/aspect from LiDAR vs. photogrammetry
- Atmospheric correction and surface reflectance validation
- **Hydrology anchor**: Classify land cover from Sentinel-2; use it to estimate infiltration rates by type

#### A.3 Spatial Interpolation & Gap-Filling (2–3 chapters) [**Core hydrology**]
- Kriging as Bayesian estimation (bridge to Vol II.B uncertainty)
- Inverse distance weighting vs. mechanistic models (when does each win?)
- Spatial validation: leave-one-out cross-validation of interpolated fields
- **Hydrology focus**: Interpolate precipitation, temperature, soil moisture from point stations; validate against independent field data
- **Secondary**: Snow-covered area from Landsat TM; compare to field snow courses

#### A.4 Watershed Analysis & Static Runoff (2–3 chapters) [**Major hydrology section**]
- Refining Vol I watershed delineation with real DEMs (handling sinks, flat areas)
- Flow direction, flow accumulation, contributing area patterns
- Soil properties from soil surveys or pedotransfer functions
- Static infiltration-excess and saturation-excess runoff estimation
- **Case study**: Delineate a real watershed; estimate runoff from a single precipitation event using field soil data

#### A.5 Evapotranspiration & Water Availability (2 chapters) [**Hydrology + ecology**]
- Potential vs. actual ET (bridging Vol I photosynthesis + sensible/latent heat)
- Estimating ET from vegetation indices (NDVI/EVI → LAI → canopy resistance)
- Spatial water balance: precipitation − ET − runoff = change in storage
- **Case study**: Estimate water availability across a basin using Sentinel ET and soil moisture

#### A.6 Carbon & Disturbance Basics (2 chapters) [**Gap coverage**]
- Forest carbon stocks from optical + LiDAR (bridging Vol I vegetation indices)
- Burn scar detection (bridge fire Vol I → satellite observations)
- Change detection fundamentals (differencing, thresholding)
- **Case study**: Map a recent fire perimeter; validate against field GPS data; estimate carbon loss

#### A.7 Cartography & Communication (1–2 chapters) [**Gap coverage**]
- Designing maps for different audiences (scientific vs. operational vs. policy)
- Color ramps, symbolization, legend design
- Static uncertainty visualization (confidence intervals on maps)
- **Case study**: Design a water-stress or runoff hazard map communicating both prediction + uncertainty

---

### Volume II.B: Dynamic Time-Series & Forecasting
**Goal**: Extend standstill validation to temporal dimension; introduce data assimilation

#### B.1 Time-Series Mechanics & Hydrology (2–3 chapters)
- Discrete time-stepping (Euler methods from Vol I, but now with observations)
- Autoregressive & moving-average models (ARIMA) as baseline competitors
- Seasonal decomposition (climate, phenology, hydrology cycles)
- **Hydrology focus**: Time-stepping a bucket water-balance model (input: precipitation; output: runoff, ET, storage change)
- **Case study**: Model monthly streamflow; compare mechanistic water-balance model vs. ARIMA

#### B.2 Multi-Temporal Remote Sensing & Hydrology (3–4 chapters)
- Landsat/Sentinel time-series: atmospheric correction, harmonization
- Phenology extraction (greenup, maturity, senescence dates; impacts on ET)
- Snow-covered area tracking (melt contribution to runoff)
- Soil moisture time-series from microwave (SMAP, Sentinel-1)
- Disturbance detection: fire progression, post-fire infiltration changes
- **Case study**: Time-series analysis of MODIS/Sentinel phenology + snow cover; infer runoff generation timing

#### B.3 Data Assimilation (2–3 chapters) [**Major gap coverage, hydrology-focused**]
- Ensemble Kalman filter (ensemble forecasting + observation update)
- Particle filters (state correction without linearity assumption)
- Uncertainty propagation (process error + observation error + model structural error)
- **Hydrology focus**: Assimilate SMAP soil moisture, streamflow observations, precipitation into a runoff model; improve forecast
- **Secondary**: Fire spread data assimilation (as comparison to hydrologic assimilation)

#### B.4 Coupled Hydro-Ecological Systems & Time-Series (2–3 chapters)
- Coupling water + carbon cycles (photosynthesis is water-limited; water use drives ET)
- Coupling energy + water (radiation determines ET; ET affects temperature)
- Spatio-temporal coherence (Moran's I over time; autocorrelation in streamflow, soil moisture)
- Scaling from point observations to gridded watersheds
- **Case study**: Time-evolving water-balance + phenology; forecast seasonal runoff and vegetation stress

#### B.5 Operational Hydrologic Forecasting (2–3 chapters) [**Bridge to Mat's advanced modules**]
- Real-time APIs: NOAA/USGS streamflow, precipitation radar, MODIS/Sentinel data pipelines
- Latency & product delays (Sentinel is 5 days; precipitation radar is 6 hours; streamflow is 1–7 days)
- Ensemble streamflow prediction (ESP): use ensemble of historical meteorology + current model
- Drought early warning using soil moisture time-series + precipitation deficits
- **Case study**: Build an operational drought or flood forecast for a real watershed using NOAA/USGS data

#### B.6 Time-Series Uncertainty & Visualization (1–2 chapters)
- Ensemble spread as forecast confidence (spaghetti plots → quantile bands)
- Communicating ensemble hydrology to water managers and public
- Skill assessment (RMSE, correlation, lead time vs. accuracy tradeoffs)
- **Case study**: Design a probabilistic streamflow forecast product

---

## Synthetic → Real Data Progression

### Vol II.A: Data Realism Arc (Hydrology focus)
1. **Chapters A.1–A.2**: Synthetic perfect watershed data + known noise; field station networks
2. **Chapters A.3–A.4**: Point measurements (precipitation, soil moisture, soil properties) + static DEM runoff estimation
3. **Chapters A.5–A.7**: Satellite-derived ET, land cover, snow cover (larger scale, atmospheric errors, gaps)

### Vol II.B: Temporal Realism Arc (Hydrology focus)
1. **Chapters B.1**: Perfect monthly streamflow time-series (seasonal cycle from bucket model)
2. **Chapters B.2–B.3**: Real satellite + gauge data (clouds, product delays, asynchronous observations); assimilation
3. **Chapters B.4–B.6**: Multi-source fusion (weather API + satellite + streamflow in real time; operational forecasting)

---

## Coverage of UCL Optional Modules

| UCL Module | Vol II Coverage |
|---|---|
| Environmental GIS | Vol I (with expansion in II.A spatial interpolation) |
| Terrestrial Carbon | II.A.4 + II.B.4 (stocks & time-series) |
| Climate Modelling | II.B.4 (coupled systems); defer large-scale climate to Vol III |
| Cartography & Data Vis | II.A.5 + II.B.5 (uncertainty visualization) |
| Spatial-Temporal Data Analysis | II.B.1–B.3 (ARIMA, phenology, assimilation) |
| Reality Capture / 3D Sensing | II.A (LiDAR validation of terrain) |
| Coastal Geohazards | Out of scope (requires boundary processes) |
| Surface Water Modelling | II.B.4 (runoff time-series forecasting) |
| Sensors & Location | II.A–B (implicit in sensor error budgeting) |

---

## Scope Notes

- **What stays out**: Large-scale atmospheric circulation (Vol III?), full GCM physics, supply-chain logistics
- **What's new**: Data assimilation, operational forecasting, multi-source fusion workflows, uncertainty visualization
- **Continuity principle**: Every Vol II chapter references Vol I equations; validates or extends them with observations

