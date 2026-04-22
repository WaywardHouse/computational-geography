# Phase 4: Laboratory Reorganization

## Goal
Restructure 42 project-based investigations from linear sequential → thematic problem sets with explicit prerequisites and backward links to core pathways.

**Philosophy:** Lab is not a textbook to read cover-to-cover, but a collection of projects readers pick based on:
- What they learned in their chosen pathway
- What problem they want to investigate
- What methods they want to practice

---

## Current Laboratory (42 chapters)

Current organization is mostly sequential by domain, but lacks:
- Explicit prerequisites (what do you need to know before starting this?)
- Backward links (which pathway/core chapter enables this?)
- Problem set organization (grouping related investigations)

### Current Thematic Groups

**Remote Sensing Applications (4)**
- SAR fundamentals and applications
- InSAR deformation monitoring
- GRACE gravity remote sensing
- Passive microwave radiometry

**Geomorphology & Hazards (10)**
- Rock weathering & soil formation
- Soil erosion & RUSLE
- Shallow landslides & slope stability
- Sediment transport in rivers (2)
- Channel morphology & hydraulic geometry
- Wave dynamics & nearshore transformation
- Longshore sediment transport & coastal budgets
- Sea level, storm surge & coastal morphodynamics

**Urban Systems (6)**
- Urban heat island dynamics
- Urban ventilation & pollutant dispersion
- Transportation network analysis
- Accessibility & travel demand modeling
- Land-use change modeling
- Urban scaling laws & city structure
- Demographic spatial dynamics

**Water Systems (8)**
- Reservoir operations & mass balance
- Stochastic streamflow & drought risk
- Dissolved oxygen dynamics (Streeter-Phelps)
- Nutrient dynamics & lake eutrophication
- Sediment & contaminant transport
- Groundwater contaminant plumes
- Pump-and-treat & in situ remediation

**Inference Methods (6)**
- Bayesian inference for environmental models
- Regression for continuous spatial variables
- Dimensionality reduction
- Ensemble forecasting & uncertainty quantification
- Kalman filter & sequential data assimilation
- Satellite data assimilation in environmental models

**Biogeochemical Cycles (7)**
- Fossil fuel combustion chemistry
- Biomass burning & pyrogenic carbon
- Land-use change & deforestation
- Photosynthesis & gross primary production
- Ocean carbon uptake & air-sea exchange
- Soil carbon storage & decomposition
- Methanogenesis in anaerobic environments

---

## Phase 4 Reorganization Strategy

### Principle 1: Thematic Problem Sets (Not Sequential)

**Reorganize into 6 problem set groups:**

#### **Problem Set A: Observation & Remote Sensing Advanced Applications**
(Builds on: Pathway A + Companion 1: Remote Sensing)

1. SAR Fundamentals & Deformation Monitoring
   - Prerequisites: Pathway A (what-is-remote-sensing, atmospheric effects)
   - Backward link: Pathway A, Chapter 6 (Raster Classification) → "See Lab for SAR"

2. Gravity Remote Sensing (GRACE)
   - Prerequisites: Pathway A, Companion 1 (orbital mechanics)
   - Backward link: Pathway A, Chapter 2 (Spectral/Temporal Resolution) → "GRACE extends temporal monitoring"

3. Passive Microwave Radiometry
   - Prerequisites: Pathway A, Companion 1 (thermal/microwave RS)
   - Backward link: Pathway A, Chapter 5 (Vegetation Indices) → "Microwave offers all-weather alternative"

---

#### **Problem Set B: Water Systems & Hydrology**
(Builds on: Pathway B + Vol II.A + Vol II.B hydrology spine)

1. Reservoir Operations & Mass Balance
   - Prerequisites: Pathway B (Water Balance + Watershed), Scientific Computing (Python scripts)
   - Backward link: Pathway B, Chapter 11 (Watershed Delineation) → "Apply to real reservoir system"

2. Streamflow Forecasting (Stochastic & Ensemble)
   - Prerequisites: Pathway B (Environmental Systems), Vol II.B (ensemble methods), Methods Reference (uncertainty)
   - Backward link: Vol II.B, Chapter B.1 (Time-Series Mechanics) → "Practice with real USGS data"

3. Water Quality & Nutrient Dynamics
   - Prerequisites: Pathway B (Soil Moisture, Wind, Temperature), Methods Reference (differential equations)
   - Backward link: Pathway B, Chapter 8 (Soil Moisture) → "Extend to coupled nutrient-water dynamics"

4. Groundwater & Contaminant Transport
   - Prerequisites: Pathway B (Soil Heat, Soil Moisture), Methods Reference (PDEs, numerical methods)
   - Backward link: Pathway B, Chapter 6 (Soil Heat Diffusion) → "Apply diffusion physics to contaminants"

---

#### **Problem Set C: Geomorphology & Hazards**
(Builds on: Pathway B + Pathway C: Hazards)

1. Soil Formation & Weathering
   - Prerequisites: Pathway B (basics), Companion 2 (if mountain context)
   - Backward link: Pathway B, Chapter 4 (Radiation & Heat) → "Heat drives weathering"

2. Soil Erosion (RUSLE)
   - Prerequisites: Pathway B (Soil Moisture, Watershed), Pathway C (Rainfall)
   - Backward link: Pathway B, Chapter 11 (Watershed) → "Predict erosion in your watershed"

3. Slope Stability & Landslides
   - Prerequisites: Pathway B (DEM, Soil Moisture), Pathway C (Rainfall)
   - Backward link: Pathway B, Chapter 2 (Gradient/Aspect) → "Use terrain derivatives for hazard mapping"

4. River Sediment Transport & Channel Morphology
   - Prerequisites: Pathway B (Watershed, Wind Profiles), Methods Reference (dynamics)
   - Backward link: Pathway B, Chapter 11 (Watershed) → "Model sediment in your basin"

5. Coastal Dynamics (Waves, Sediment, Storm Surge)
   - Prerequisites: Pathway B (Wind, Temperature Gradients), Methods Reference (numerical methods)
   - Backward link: Pathway B, Chapter 9 (Wind Profiles) → "Wave and surge modeling"

---

#### **Problem Set D: Urban Systems & Infrastructure**
(Builds on: Pathway C: Economics + Urban Systems)

1. Urban Heat Island Dynamics
   - Prerequisites: Pathway B (Radiation, Sensible Heat), Pathway A (Thermal RS)
   - Backward link: Pathway B, Chapter 5 (Sensible/Latent Heat) → "Apply to cities"

2. Urban Ventilation & Air Quality
   - Prerequisites: Pathway B (Wind Profiles), Pathway C (Urban applications)
   - Backward link: Pathway B, Chapter 9 (Wind Profiles) → "Apply to urban canyons"

3. Transportation Networks & Accessibility
   - Prerequisites: Foundations (Gravity Models, Spatial Diffusion), Pathway C (Economic Systems)
   - Backward link: Pathway C, Chapter 1 (Gravity Models) → "Model travel demand in your city"

4. Land-Use Change Modeling
   - Prerequisites: Pathway A (Classification, Change Detection), Pathway C (Economic/Urban)
   - Backward link: Pathway A, Chapter 8 (Change Detection) → "Predict future land use"

5. Urban Scaling Laws & City Structure
   - Prerequisites: Pathway C (Urban Economics, Agglomeration)
   - Backward link: Pathway C, Chapter 3 (Urban Agglomeration) → "Investigate scaling in your region"

6. Demographic Spatial Dynamics
   - Prerequisites: Pathway C (Migration/Social Systems), Methods Reference (spatial statistics)
   - Backward link: Pathway C, Chapter 2 (Urban Bid-Rent) → "Model population change"

---

#### **Problem Set E: Inference & Methods (Cross-Cutting)**
(Builds on: All Pathways + Methods Reference + Vol II.A/B)

1. Bayesian Inference for Environmental Models
   - Prerequisites: Methods Reference (Bayesian), any applied chapter (fire, flood, etc.)
   - Backward link: Vol II.B, Chapter B.3 (Data Assimilation) → "Deep dive into Bayesian methods"

2. Regression for Spatial Variables
   - Prerequisites: Pathway A (Classification), Methods Reference (regression basics)
   - Backward link: Pathway A, Chapter 7 (Classification) → "Advanced statistical validation"

3. Dimensionality Reduction
   - Prerequisites: Pathway A (multispectral imagery), Methods Reference (PCA)
   - Backward link: Pathway A, Chapter 5 (Vegetation Indices) → "Extract features from high-dimensional data"

4. Ensemble Forecasting & Uncertainty Quantification
   - Prerequisites: Vol II.B (Ensembles), Methods Reference (Uncertainty)
   - Backward link: Vol II.B, Chapter B.1 (Time-Series Mechanics) → "Practice ensemble thinking"

5. Kalman Filtering & Sequential Data Assimilation
   - Prerequisites: Vol II.B (Data Assimilation), Methods Reference (Bayesian)
   - Backward link: Vol II.B, Chapter B.3 (Data Assimilation) → "Operational forecasting implementation"

6. Satellite Data Assimilation
   - Prerequisites: Pathway A (RS fundamentals), Vol II.B (Assimilation)
   - Backward link: Vol II.B, Chapter B.3 (Data Assimilation) → "Assimilate real satellite observations"

---

#### **Problem Set F: Biogeochemical Cycles**
(Builds on: Pathway B + Companion 2/4)

1. Combustion Chemistry & Energy Systems
   - Prerequisites: Pathway C (Energy/Markets), Methods Reference (chemistry basics)
   - Backward link: Companion 3 (Economics: Energy Systems) → "Understand emissions from sources"

2. Biomass Burning & Pyrogenic Carbon
   - Prerequisites: Pathway C (Fire), Pathway B (Photosynthesis/Carbon)
   - Backward link: Pathway C, Chapter 2 (Fire Spread) → "Calculate carbon emissions from fire"

3. Land-Use Change & Deforestation
   - Prerequisites: Pathway A (Classification, Change Detection), Pathway B (Carbon Cycle)
   - Backward link: Pathway A, Chapter 8 (Change Detection) → "Quantify carbon loss from deforestation"

4. Photosynthesis & Primary Productivity
   - Prerequisites: Pathway B (Photosynthesis, Light Response), Pathway A (Vegetation Indices)
   - Backward link: Pathway B, Chapter 7 (Photosynthesis) → "Validate with field measurements"

5. Ocean Carbon Cycles
   - Prerequisites: Pathway B (Temperature-Moisture Gradients), Pathway A (Water optics from Companion 1)
   - Backward link: Pathway B, Chapter 10 (Temperature-Moisture) → "Ocean carbon in global cycles"

6. Soil Carbon Dynamics
   - Prerequisites: Pathway B (Soil Heat, Soil Moisture, Photosynthesis)
   - Backward link: Pathway B, Chapter 6 (Soil Heat) → "Model soil carbon under climate change"

7. Methanogenesis & Anaerobic Processes
   - Prerequisites: Pathway B (Soil Moisture), Companion 2 (if wetland/permafrost context)
   - Backward link: Pathway B, Chapter 8 (Soil Moisture) → "Model methane from wetlands"

---

## Phase 4 Implementation

### Step 1: Create Metadata for Each Lab Chapter

Each lab chapter gets frontmatter:
```yaml
prerequisites:
  - core-pathway: "B"  # Pathway B
    specific-chapters: ["net-radiation-and-albedo", "soil-heat-diffusion"]
  - methods-reference: "chapter-3"  # Uncertainty Propagation
backward-links:
  - pathway: "B"
    chapter: "soil-heat-diffusion"
    note: "Lab extends soil heat to contaminant transport"
problem-set: "C"  # Geomorphology & Hazards
```

### Step 2: Reorganize _quarto-laboratory.yml

Instead of linear chapters, organize by problem set:

```yaml
book:
  chapters:
    - index.qmd
    - part: "Problem Set A: Observation & Remote Sensing"
      chapters:
        - sar-fundamentals-and-applications.qmd
        - insar-deformation-monitoring.qmd
        - gravity-remote-sensing-grace.qmd
        - passive-microwave-radiometry.qmd
    - part: "Problem Set B: Water Systems & Hydrology"
      chapters: [...]
    # ... etc
```

### Step 3: Add "Prerequisites" Section to Each Lab Chapter

Example opening:

```
## Before You Start This Investigation

**You should have completed:**
- Pathway B, Chapter 11: Watershed Delineation
- Vol II.B, Chapter B.1: Time-Series Mechanics
- Methods Reference, Chapter 3: Uncertainty Propagation

**You will learn:**
- Ensemble streamflow forecasting with real USGS data
- Handling forecast uncertainty in operations
- Connecting observations to runoff predictions

**See also:** [This lab builds on watershed concepts from Pathway B](...)
```

### Step 4: Add "Where This Leads" Section

Example closing:

```
## Where This Investigation Leads

**In Vol II.B:** This project prepares you for operational hydrologic forecasting
covered in Chapter B.5 (Operational Forecasting).

**Related labs:** 
- Reservoir Operations (Problem Set B)
- Groundwater Contaminant Transport (Problem Set B)

**In the field:** NOAA/USGS operational streamflow forecasts use these methods.
```

---

## Laboratory as Workbook, Not Textbook

### Key Design Change

**Before:** Linear chapters 1-42, read in order  
**After:** Problem sets organized by domain; choose entry point based on pathway + interest

**Navigation:**
- Readers pick problem set matching their pathway
- Metadata shows prerequisites and backward links
- "Related investigations" section connects to other problem sets

### Example Reader Journey

Reader completes:
- Pathway B (Environmental Systems)
- Vol II.B (Dynamics & Forecasting)

Can now choose:
- **Problem Set B:** All water investigations (streamflow, reservoirs, water quality)
- **Problem Set C:** Geomorphology (use watershed skills for erosion/landslides)
- **Problem Set F:** Biogeochemical (soil carbon, methane from wetlands)

Each investigation has clear prerequisites + backward links.

---

## Laboratory Metadata (CSV Index)

Create `planning/laboratory-index.csv`:

| Investigation | Problem Set | Prerequisites | Backward Link | Est. Hours | Level |
|---|---|---|---|---|---|
| SAR Fundamentals | A | PathwayA-Ch6 | PathwayA-Ch6 | 10 | Advanced |
| Streamflow Forecasting | B | PathwayB-All, VolII-B1 | VolII-B1 | 15 | Advanced |
| Slope Stability | C | PathwayB-Ch2/8, PathwayC-Ch3 | PathwayB-Ch2 | 12 | Intermediate |
| Urban Heat Island | D | PathwayB-Ch5, PathwayA-Ch5 | PathwayB-Ch5 | 10 | Intermediate |
| Bayesian Inference | E | MethodsRef-Ch6, Any applied | VolII-B3 | 12 | Advanced |
| Soil Carbon | F | PathwayB-Ch6/7/8 | PathwayB-Ch6 | 8 | Intermediate |

---

## Critical Files to Modify

1. **Create _quarto-laboratory.yml (reorganized)**
   - Structure by problem sets, not linear
   - Add metadata to chapters

2. **Create planning/laboratory-index.csv**
   - All chapters with prerequisites, backward links, difficulty

3. **Update each lab chapter frontmatter**
   - Add prerequisites metadata
   - Add backward-links
   - Update opening/closing to reference them

4. **Create laboratory-navigation.qmd**
   - Overview of problem sets
   - How to choose entry point
   - Prerequisite checker

---

## Estimated Scope

| Problem Set | Chapters | Avg Hours Each | Total Hours | Level |
|---|---|---|---|---|
| A: Remote Sensing | 4 | 10 | 40 | Advanced |
| B: Water Systems | 4 | 12 | 48 | Advanced |
| C: Geomorphology | 5 | 11 | 55 | Intermediate |
| D: Urban Systems | 6 | 10 | 60 | Intermediate |
| E: Inference Methods | 6 | 12 | 72 | Advanced |
| F: Biogeochemical | 7 | 9 | 63 | Intermediate |
| **TOTAL** | **42** | **~11** | **~438 hrs** | Mixed |

Roughly: 40-50 hours per problem set; reader picks 1-2 sets based on interests.

---

## Questions for Phase 4 Execution

1. **Difficulty levels:** Should we formally mark chapters as Beginner/Intermediate/Advanced, or just through prerequisites?
2. **Reading order within problem sets:** Are problem sets sequential (do investigation 1, then 2)? Or can they be done in any order?
3. **Size of investigations:** Should we combine some (SAR fundamentals + InSAR = one big SAR project) or keep separate?
4. **Estimated time:** Should we add "approximately X hours" to each investigation?

