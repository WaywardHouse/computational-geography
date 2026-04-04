# Golden Path Pilot: Urban Flood Screening and Green Infrastructure Prioritization

## Path Snapshot

- `Path type`: `Applied`
- `Path family`: `Hazards and Early Warning`
- `Primary roles`: municipal planner, stormwater engineer, resilience analyst
- `Typical spatial scale`: neighbourhood to municipality
- `Typical temporal scale`: event-scale screening with seasonal or annual planning use

## Use Case

This path exists for readers who need a dependable first workflow for thinking about urban flood risk without beginning from a full hydraulic simulation.

It is designed for questions such as:

- where is runoff likely to accumulate?
- which assets or neighbourhoods are most exposed?
- where might green infrastructure or drainage intervention matter most?

This is a screening and prioritization path.

It is not a substitute for detailed engineering design or calibrated floodplain modelling.

## Why This Path Exists

Urban flood questions are one of the clearest examples of why the project would benefit from golden paths.

The relevant material already exists in different parts of the series:

- rainfall and extreme-event framing in `atmospheric-hazards`
- terrain and flow logic in `spatial-analysis`
- practical overlays and exposure screening in GIS workflows
- advanced hydrologic and systems material in the laboratory

The path adds value by combining those pieces into a practical default route.

## Research Question

How can we screen a city or neighbourhood to identify likely runoff concentration zones, exposed assets, and promising intervention areas for flood resilience?

## Minimum Data Inputs

At a minimum, the path assumes access to:

- a DEM or comparable surface model
- rainfall intensity information or a design-storm proxy
- drainage network or flow-path context
- land cover, imperviousness, or surface-type indicators
- exposed assets such as roads, buildings, schools, substations, or vulnerable populations

If the reader has only partial data, the path can still function as a coarse screening workflow, but confidence should be correspondingly reduced.

## Core Concepts

The conceptual backbone of this path is:

- runoff is shaped by rainfall intensity, infiltration limits, and topography
- flow concentrates through structure rather than distributing evenly across space
- exposure depends on both hazard location and the geography of people and assets
- useful first-pass planning can be done before full dynamic simulation

## Recommended Modelling Sequence

### 1. Define The Planning Question Clearly

Decide whether the immediate need is:

- hotspot screening
- infrastructure prioritization
- neighbourhood comparison
- intervention siting

This matters because the output map should be designed for the decision, not only for the model.

### 2. Establish A Rainfall Severity Frame

Use a design-storm or intensity-duration-frequency context to define what kind of event the screening is meant to represent.

This gives the rest of the workflow a shared severity assumption.

### 3. Derive Terrain And Flow Structure

Use elevation data to identify:

- local depressions
- downslope flow directions
- likely concentration corridors
- contributing areas

At this stage the workflow is trying to understand urban terrain as a routing structure.

### 4. Add Surface Response Information

Overlay imperviousness, land cover, or drainage limitations to distinguish places that shed water quickly from places that can absorb or delay it.

### 5. Build A Hazard Screening Surface

Combine rainfall framing, terrain concentration, and surface response into a first-pass surface showing where runoff pressure is likely to be highest.

This does not need to claim exact water depth.

Its purpose is to show relative concentration and likely concern areas.

### 6. Add Exposure Layers

Overlay buildings, roads, utilities, public facilities, and social vulnerability indicators to identify where hydrologic pressure and consequence intersect.

### 7. Prioritize Intervention Zones

Identify places where:

- runoff pressure is high
- exposure is meaningful
- intervention is plausible

This is where the path becomes useful for green infrastructure, drainage upgrades, detention, or corridor redesign.

## Suggested Chapter Path

The minimum chapter sequence for this path is:

1. [`rainfall-intensity-duration.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/atmospheric-hazards/rainfall-intensity-duration.qmd)
2. [`flood-frequency-analysis.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/atmospheric-hazards/flood-frequency-analysis.qmd)
3. [`watershed-delineation.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/spatial-analysis/watershed-delineation.qmd)
4. [`polygon-overlay-operations.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/spatial-analysis/polygon-overlay-operations.qmd)
5. [`urban-flood-modeling.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/atmospheric-hazards/urban-flood-modeling.qmd)

Useful supporting chapters:

- [`buffer-operations.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/spatial-analysis/buffer-operations.qmd)
- [`spatial-joins.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/spatial-analysis/spatial-joins.qmd)
- [`map-algebra-focal-operations.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/spatial-analysis/map-algebra-focal-operations.qmd)

Advanced branches:

- [`reservoir-operations-and-mass-balance.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/laboratory/reservoir-operations-and-mass-balance.qmd)
- [`satellite-data-assimilation-in-environmental-models.qmd`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/laboratory/satellite-data-assimilation-in-environmental-models.qmd)

## Minimum Viable Outputs

The path should usually produce:

- a runoff concentration screening map
- an asset exposure overlay
- a ranked set of intervention or investigation zones

If the path is being used in a municipal context, a short decision memo would likely matter as much as the map outputs themselves.

## Interpretation Cautions

This path should be framed carefully.

It is strongest when used for:

- comparative screening
- prioritization
- identifying where deeper work is warranted

It is weaker when asked to provide:

- exact inundation depths
- parcel-level engineering decisions
- high-confidence flood extents without calibration

## Common Failure Modes

The most likely ways this path can mislead are:

- using elevation data that is too coarse for urban drainage structure
- assuming runoff behaviour without representing impervious surfaces or stormwater constraints
- treating a relative hazard surface as a calibrated flood model
- overlaying assets without distinguishing consequence severity
- ignoring the temporal assumptions built into the chosen rainfall frame

## Adjacent Golden Paths

This pilot path naturally connects to:

- wildfire risk screening, where exposure overlays and prioritization logic are similar
- watershed condition and downstream risk, where upstream routing and transport logic become more important
- urban accessibility and service allocation, where the same municipal audience may be making competing infrastructure decisions

## Editorial Note

This path is a strong pilot candidate because it combines:

- clear public relevance
- existing chapter strength
- a practical decision context
- a manageable distinction between minimum workflow and advanced modelling

If the golden-paths framework works here, it is likely to work in other hazard and planning contexts.
