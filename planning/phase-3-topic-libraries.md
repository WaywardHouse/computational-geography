# Phase 3: Reorganize Topic Libraries into 4 Companion Books

## Goal
Split the sprawling topic libraries (~68 chapters) into 4 coherent companion volumes, each with:
- Clear learning arc
- Distinct audience/purpose
- Cross-links to core pathways
- Self-contained but builds on core book

---

## Current Topic Libraries (68 chapters)

```
Cryosphere and Mountain Systems (11)
Advanced Remote Sensing (9)
Machine Learning (3)
Environmental Systems extensions (8: orbital + carbon + nitrogen + phenology)
Atmospheric Hazards extensions (6: thunderstorms, tornadoes, hail, wind, compound)
Economic Systems (30+: pipelines, trade, ports, markets, resources, renewable)
```

---

## Proposed 4 Companion Books

### **Companion 1: Remote Sensing for Environmental Modelling**

**Purpose:** Deep specialization for readers who choose Pathway A and want to go advanced.

**Chapters (~18-20 total):**

From current Advanced Remote Sensing:
- PROSPECT (leaf optical properties)
- SAIL (canopy reflectance)
- Hyperspectral imaging
- Thermal infrared remote sensing
- LiDAR and point clouds
- Bathymetric LiDAR & sonar
- SAR fundamentals
- Gravity remote sensing

From current Environmental Systems (orbital mechanics):
- Circular orbits & Kepler's third law
- Ground tracks & orbital geometry
- Satellite overpasses & visibility
- How GPS works

New synthetic chapters:
- Satellite image time-series analysis
- Sensor fusion (combining multiple sensors)
- Change detection at scale
- Real-world data workflows (APIs, cloud processing)

**Position:** After Pathway A (Remote Sensing & Observation); natural deepening for readers who want advanced RS skills.

**Rationale:** Pathway A covers observation *mechanics*; Companion 1 covers *advanced techniques & real-world workflows*.

---

### **Companion 2: Cryosphere & Mountain Systems**

**Purpose:** Specialized systems book for high-altitude, snow-dominated environments.

**Chapters (~16-18 total):**

From current Cryosphere:
- Snowpack energy balance
- Snow accumulation-melt modeling
- SWE estimation methods
- Avalanche terrain analysis
- Glacier mass balance
- Glacial meltwater chemistry
- Glacial lake outburst floods
- Slope stability analysis
- Debris-flow modeling
- Permafrost thaw geohazards

New synthetic chapters:
- Mountain hydrology (how cryosphere feeds water cycle)
- Elevation gradients (temperature, precipitation lapse rates)
- Alpine hazards integration (avalanche + GLOF + debris flow cascades)
- Climate change in mountains (glacier retreat, permafrost thaw implications)

**Position:** After Pathway B (Environmental Systems & Processes); extends water/hazard thinking to mountains.

**Rationale:** Cryosphere is a *complete system* (energy, water, hazards coupled); coherent to treat as specialized volume.

---

### **Companion 3: Economic Geography & Infrastructure Systems**

**Purpose:** Deep dive into spatial economics, trade networks, resource systems, and infrastructure.

**Chapters (~35-40 total):**

**Trade & Economic Networks (~10 chapters):**
- Canada trade gravity model (KEEP in core, reference here)
- Canada trade corridors
- Canada port economics
- Canada freight modal split
- Canada integrated trade network
- Urban city-size Zipf's law
- Urban economic base
- Urban integrated system
- Commodity price formation
- Futures & geographic instruments
- Price volatility & integration

**Resource Systems (~12 chapters):**
- Hotelling's rule (resource depletion economics)
- Supply curves & cost curves
- Royalty regimes
- Resource curse
- Integrated resource systems
- Alberta crude oil pipelines (5 chapters: crude, NGL, gas, products, integrated)
- Crude oil pipeline systems
- NGL & condensate systems
- Natural gas transmission
- Refined products distribution
- Integrated pipeline network

**Renewable Energy & Transitions (~8 chapters):**
- Alberta renewable resource geography
- Alberta renewable economics
- Alberta renewable policy & demand
- Energy transitions & stranded assets
- Storage & grid integration
- Market design for renewables
- Just transition frameworks
- Urban renewable systems

**Position:** After Pathway C (Applications & Implications); extends economic models to complex systems.

**Rationale:** Economics is a *complete domain* with its own modeling tradition (trade, resources, energy); deserves a dedicated companion.

---

### **Companion 4: Geographic Machine Learning & Inference**

**Purpose:** Statistical & computational methods for spatial prediction and inference.

**Chapters (~15-18 total):**

From current Machine Learning:
- Regression for continuous variables
- Dimensionality reduction (PCA, t-SNE, UMAP)

From Methods Reference (expanded for ML audience):
- Bayesian inference for spatial data
- Causal inference for observational geographies
- Feature engineering for spatial data
- Model selection & cross-validation

New synthetic chapters:
- Time-series forecasting (ARIMA, state-space)
- Spatial interpolation methods comparison (kriging, neural networks, ensemble)
- Deep learning for imagery (CNNs for classification)
- Uncertainty quantification in predictions
- Operationalizing machine learning (training → deployment pipeline)

**Position:** Can enter from:
- Pathway A (satellite imagery classification → deep learning)
- Pathway B (parameter estimation → Bayesian inference)
- Pathway C (prediction → model selection & validation)
- Vol II.B (ensemble forecasting → advanced methods)

**Rationale:** Machine learning is a *cross-cutting methodology*; readers approach it from different pathways.

---

## Mapping Current → New Structure

| Current | Goes To | Notes |
|---------|---------|-------|
| Cryosphere & Mountain Systems (11) | Companion 2 (16-18) | Stays mostly intact; add synthesis chapters |
| Advanced Remote Sensing (9) | Companion 1 (18-20) | Core + orbital mechanics + new workflows |
| Machine Learning (3) | Companion 4 (15-18) | Expanded with Bayesian, causal, deep learning |
| Environmental Systems extensions (8) | Companion 1 (orbital), Companion 2 (phenology into mountain context) | Orbital stays with RS; phenology distributed |
| Atmospheric Hazards extensions (6) | Companion 2 (avalanche/debris cascades), Companion 3 (policy response) | Organized by domain, not hazard type |
| Economic Systems (30+) | Companion 3 (35-40) | All organized by subsystem (trade, resources, energy) |

---

## Four _quarto Configs

1. **_quarto-companion-1-remote-sensing.yml** — Remote Sensing for Environmental Modelling
2. **_quarto-companion-2-cryosphere.yml** — Cryosphere & Mountain Systems
3. **_quarto-companion-3-economics.yml** — Economic Geography & Infrastructure
4. **_quarto-companion-4-ml-inference.yml** — Geographic Machine Learning & Inference

Each config:
- Self-contained (can be read independently)
- But assumes reader has completed core book (Part 1 + one Pathway)
- Cross-links to related pathways and other companions
- "Before You Start" sections specify core prerequisites

---

## Why This Organization?

1. **By System, Not By Topic**
   - Not "all machine learning" (scattered across pathways)
   - But "machine learning for inference in geography" (coherent)
   - Not "all hazards" (fire + flood + avalanche separate)
   - But "cryosphere as a coupled system" (integrated)

2. **Respects Reader Paths**
   - Pathway A reader naturally progresses: core RS → Advanced RS → ML for imagery
   - Pathway B reader naturally progresses: core systems → Cryosphere/Energy/Carbon (as extensions)
   - Pathway C reader naturally progresses: core apps → Economic geography (detailed)

3. **Defers Specialization**
   - Core book is accessible to all
   - Companions are "pick your specialization"
   - Not trying to be comprehensive; being coherent

4. **Supports Vol II**
   - Vol II.A (validation): References Methods Reference + Companion 4 (inference)
   - Vol II.B (forecasting): References Pathway B + Companion 2 (hydrology) + Companion 4 (ensemble methods)

---

## Synthetic Chapters Needed (Fills Gaps)

| Companion | New Chapters Needed | Purpose |
|-----------|---|---|
| 1 | Sensor fusion, real-world workflows, cloud processing | Bridge theory → operations |
| 2 | Mountain hydrology, elevation gradients, climate change impacts | Complete the system; connect to water cycle |
| 3 | Energy transitions, storage, grid integration, just transition | Modern context; not just static systems |
| 4 | Time-series forecasting, deep learning, uncertainty quantification, operationalization | Complete ML toolkit; bridge to Vol II.B |

---

## Implementation Plan

### Step 1: Create directory structure
- Move existing topic chapters into companion directories
- Create index chapters for each companion

### Step 2: Organize by companion theme
- Cryosphere: straightforward (mostly already organized)
- Remote Sensing: add orbital mechanics + new chapters
- Economics: reorganize by subsystem (currently scattered)
- ML: pull from methods + add new material

### Step 3: Create _quarto configs (4 new configs)
- Each companion as self-contained book
- Cross-links between companions
- "Prerequisites" metadata

### Step 4: Add "Before You Start" sections
- Each companion specifies what core pathways it assumes
- Links to prerequisite material

### Step 5: Write synthetic chapters (20-30 new chapters across companions)

---

## Critical Files to Create/Modify

1. **Create 4 new _quarto configs:**
   - `_quarto-companion-1-remote-sensing.yml`
   - `_quarto-companion-2-cryosphere.yml`
   - `_quarto-companion-3-economics.yml`
   - `_quarto-companion-4-ml-inference.yml`

2. **Reorganize directories:**
   - `cryosphere-and-mountain-systems/` → new structure
   - `advanced-remote-sensing/` → add orbital mechanics + new chapters
   - `machine-learning/` → expand; add inference chapters
   - `economic-systems/` → reorganize by subsystem
   - Create `remote-sensing-workflows/` → new chapters

3. **Create index chapters** for each companion

4. **Create cross-link matrix** (companion A ↔ companion B)

---

## Estimated Scope

| Companion | Existing | New | Total | Est. Words |
|-----------|----------|-----|-------|------------|
| 1: Remote Sensing | 9 + 4 (orbital) | 5-6 (sensor fusion, workflows, deep learning) | 18-20 | 45-50K |
| 2: Cryosphere | 11 | 5-7 (hydrology, elevation, climate change) | 16-18 | 50-60K |
| 3: Economics | 30 | 5-8 (energy transitions, policy) | 35-40 | 100-120K |
| 4: ML & Inference | 3 | 12-15 (Bayesian, causal, forecasting, deep learning, operationalization) | 15-18 | 60-70K |
| **TOTAL** | **57** | **27-36** | **84-112** | **255-300K** |

---

## Questions for Phase 3 Execution

1. **Economics depth:** Should we keep all 30+ economic chapters, or prune to essentials + case studies?
2. **ML focus:** Emphasis on classical (regression, Bayesian) or modern (deep learning)? Or both?
3. **Cross-links:** Should each companion reference others (e.g., "See Cryosphere Companion for mountain hydrology context")?
4. **Publishing:** Should companions be published as:
   - A) Separate books (4 PDFs)?
   - B) Sections of one larger "Companions" book?
   - C) Topic libraries on the website (no separate publication)?

