# Golden Paths Framework

## Purpose

This document proposes a new cross-cutting framework for the `Computational Geography` series:

- not a new book line
- not a replacement for the current site architecture
- not a claim that there is only one correct workflow for a research question

It is a proposal for a workflow layer.

The project already has strong discrete models, chapters, topic libraries, and laboratory investigations.

What it does not yet have is a consistent way to help a reader move from:

- a role or function
- a practical motivation
- a recurring research question
- a reasonable default sequence of data collection and modelling choices
- an interpretable outcome

That is the role of `golden paths`.

## Working Definition

A `golden path` is a curated research workflow for a recurring class of problem.

It should connect:

- who is asking
- why they are asking
- what question they need to answer
- what minimum data they need
- what conceptual and modelling sequence is usually dependable
- what kind of output or decision product should result

A golden path is:

- opinionated enough to be useful
- explicit about assumptions
- modular enough to branch
- framed as a dependable default, not an absolute best practice for every context

This distinction matters.

Many research questions can be answered through multiple defensible modelling routes.

The value of a golden path is not that it proves one true method.

The value is that it gives readers a strong starting grammar for assembling the material already present in the project.

## Why This Adds Value

The current planning model already separates the project into:

- `Start Here`
- `Core Book`
- `Topic Libraries`
- `Laboratory`
- `Methods and Tools`

That architecture clarifies what kind of material the reader is looking at.

But many readers will not begin by asking:

- which volume should I read?
- which chapter should I open first?

They will begin by asking:

- how would I investigate flood risk in a city?
- how would I monitor vegetation stress over time?
- how would I reason from snowpack and terrain to avalanche exposure?
- how would I identify trade or infrastructure bottlenecks?

Those are workflow questions.

Golden paths would add value because they translate a rich but distributed body of content into practical research routes.

They would help the project serve at least four reader needs better:

1. problem-first readers who begin with a use case rather than a topic
2. practitioners who need a dependable default workflow before they need specialist depth
3. learners who want to understand how individual models connect into a larger analysis
4. future curriculum or companion-book design that needs a reusable workflow grammar

## What Golden Paths Are Not

To keep the framework coherent, golden paths should not become:

- a new parallel taxonomy that competes with the main book structure
- an exhaustive map of every possible modelling workflow
- a rigid "best practice" claim that hides uncertainty or context dependence
- a substitute for topic libraries or laboratory investigations

They should remain:

- a synthesis layer
- a reader-intent layer
- a research-design layer

## Relationship To The Existing Architecture

Golden paths should sit across the current architecture, not inside only one cluster.

They would use the existing content this way:

- `Core Book` supplies the conceptual and methodological backbone
- `Topic Libraries` supply specialist branch depth
- `Laboratory` supplies integrated and advanced applications
- `Methods and Tools` supplies reusable practical supports

In other words:

- the current architecture tells readers where content lives
- golden paths would tell readers how to combine it for a recurring purpose

This means golden paths are best understood as an overlay.

They are closer to a workflow index or applied research framework than to a new volume.

## Design Principles

If the framework is developed, each path should follow a small set of editorial rules.

### 1. Start From The Question

The path should begin with a practical research question, not with a tool, platform, or technique.

### 2. Keep The Default Path Teachable

Each path should have a minimum viable route that can be explained clearly without requiring the reader to absorb every specialist branch.

### 3. Make Branching Explicit

Paths should show where optional specialist depth becomes useful:

- remote sensing
- cryosphere
- machine learning
- uncertainty quantification
- advanced laboratory methods

### 4. Make Scale Visible

Every path should state its typical:

- spatial scale
- temporal scale
- resolution limits
- interpretive limits

### 5. Make Failure Modes Visible

Each path should name common reasons it fails or misleads:

- poor proxy choice
- mismatched scales
- insufficient calibration
- weak causal interpretation
- overconfident classification

### 6. Preserve Reader Trust

Golden paths should be framed as:

- dependable defaults
- transparent about assumptions
- open to alternative routes

This matters especially because the project spans both physical and human systems, where methods may differ significantly by context.

## Canonical Path Template

Each golden path should use the same core template.

This consistency would make the framework teachable, navigable, and eventually machine-readable if the project later uses metadata-driven pages.

Recommended fields:

- `Path name`
- `Primary roles`
- `Use case`
- `Research question`
- `Why this path exists`
- `Typical spatial scale`
- `Typical temporal scale`
- `Minimum data inputs`
- `Core concepts`
- `Recommended modelling sequence`
- `Suggested chapter path`
- `Minimum viable outputs`
- `Advanced extensions`
- `Common failure modes`
- `Interpretation cautions`
- `Adjacent golden paths`

## Path Grammar

The framework should be expressible through one simple grammar:

`Role -> Motivation -> Question -> Data -> Transformations -> Models -> Outputs -> Interpretation -> Decision`

This grammar is one of the most valuable parts of the proposal.

If it is adopted consistently, it can later support:

- public navigation
- chapter cross-linking
- curriculum planning
- role-based learning paths
- a future use-case library across industries and sectors

## Golden Path Types

To prevent the framework from becoming too flat, it should likely distinguish between three path types.

### Starter Paths

These are mostly built from `Core Book` chapters with minimal branching.

They are suitable for:

- first applied projects
- classroom use
- readers who need a practical entry point

### Applied Paths

These combine `Core Book` and `Topic Libraries` and may include selected laboratory chapters.

They are suitable for:

- realistic professional workflows
- interdisciplinary projects
- readers who need a more complete default route

### Expert Paths

These draw heavily on `Laboratory` and specialist branches and should foreground uncertainty, calibration, and interpretation risks.

They are suitable for:

- advanced projects
- practicum or capstone work
- domain-specialist readers

## Initial Path Families

A first version of the framework should stay broad and legible.

An initial set of path families could be:

- `Hazards and Early Warning`
- `Environmental Monitoring and Change Detection`
- `Water, Terrain, and Watersheds`
- `Networks, Trade, and Infrastructure`
- `Urban Systems and Planning`

These categories are useful because they organize by recurring problem form rather than by the current storage location of chapters.

## Pilot Golden Paths

The framework should begin with a small number of pilot paths rather than a full taxonomy.

The purpose of the pilot set is to prove that the framework adds real value across different parts of the project.

## 1. Wildfire Risk Screening and Spread Interpretation

### Primary Roles

- wildfire analyst
- land manager
- municipal emergency planner

### Use Case

Screen landscapes for ignition risk, likely spread behaviour, and exposed assets.

### Research Question

Where are fire starts and fast-spread conditions most likely, and what areas are most exposed?

### Minimum Data Inputs

- weather or fire weather indicators
- topography
- vegetation or fuels proxy
- settlement, infrastructure, or asset layers

### Likely Chapter Backbone

- `atmospheric-hazards/fire-weather-ignition.qmd`
- `atmospheric-hazards/fire-spread-modeling.qmd`
- `environmental-systems/vegetation-indices-and-remote-sensing.qmd`
- `spatial-analysis/buffer-operations.qmd`
- `spatial-analysis/map-algebra-focal-operations.qmd`

### Minimum Viable Outputs

- ignition-risk surface
- spread-favourability zones
- exposure or priority map

### Likely Extensions

- smoke dispersion
- change detection
- ensemble forecasting

## 2. Urban Flood Screening and Green Infrastructure Prioritization

### Primary Roles

- municipal planner
- stormwater engineer
- resilience analyst

### Use Case

Identify runoff concentration zones, exposed assets, and promising intervention sites.

### Research Question

Where is runoff likely to concentrate, what is exposed, and where will interventions matter most?

### Minimum Data Inputs

- rainfall design information
- DEM
- drainage or watershed network
- land cover or imperviousness
- exposed assets or population layers

### Likely Chapter Backbone

- `atmospheric-hazards/rainfall-intensity-duration.qmd`
- `atmospheric-hazards/flood-frequency-analysis.qmd`
- `atmospheric-hazards/urban-flood-modeling.qmd`
- `spatial-analysis/watershed-delineation.qmd`
- `spatial-analysis/polygon-overlay-operations.qmd`

### Minimum Viable Outputs

- runoff concentration map
- flood-exposure screening map
- intervention priority map

### Likely Extensions

- reservoir operations
- data assimilation
- uncertainty ranges

## 3. Vegetation Stress and Drought Monitoring

### Primary Roles

- environmental scientist
- watershed analyst
- agricultural monitor
- conservation planner

### Use Case

Track vegetation response to heat and moisture stress through time.

### Research Question

Where is vegetation under stress, how is that changing, and what environmental conditions help explain it?

### Minimum Data Inputs

- multispectral imagery
- temperature and precipitation or moisture proxies
- land cover context

### Likely Chapter Backbone

- `environmental-systems/soil-moisture-dynamics.qmd`
- `environmental-systems/temperature-moisture-gradients.qmd`
- `environmental-systems/vegetation-indices-and-remote-sensing.qmd`
- `spatial-analysis/change-detection.qmd`
- `spatial-analysis/time-series-analysis.qmd`

### Minimum Viable Outputs

- vegetation condition anomaly map
- stress hotspot map
- trend summary through time

### Likely Extensions

- phenology
- hyperspectral indicators
- data assimilation

## 4. Snowpack, Terrain, and Avalanche Exposure

### Primary Roles

- avalanche forecaster
- mountain guide
- transportation corridor analyst
- alpine planner

### Use Case

Relate terrain structure and snow conditions to avalanche exposure for routes, recreation, or infrastructure.

### Research Question

Where are avalanche start, track, and runout zones likely, and what routes or assets are exposed?

### Minimum Data Inputs

- DEM
- snow and weather observations
- slope and aspect derivatives
- route, corridor, or asset layers

### Likely Chapter Backbone

- `cryosphere-and-mountain-systems/snowpack-energy-balance.qmd`
- `cryosphere-and-mountain-systems/snow-accumulation-melt-modeling.qmd`
- `cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd`
- `foundations/gradient-aspect-steepest-descent.qmd`
- `spatial-analysis/viewshed-line-of-sight.qmd`

### Minimum Viable Outputs

- terrain hazard classes
- route exposure map
- monitoring priority areas

### Likely Extensions

- debris flow
- permafrost
- high-resolution remote sensing

## 5. Trade Corridor Bottlenecks and Network Exposure

### Primary Roles

- transportation strategist
- economic geographer
- port analyst
- policy advisor

### Use Case

Identify infrastructure chokepoints, dominant routes, and system dependencies.

### Research Question

Which routes or nodes dominate movement, where are the bottlenecks, and what disruptions matter most?

### Minimum Data Inputs

- network topology
- flow or movement volumes
- node capacities
- corridor geography
- disruption scenarios

### Likely Chapter Backbone

- `economic-systems/canada-trade-gravity-model.qmd`
- `economic-systems/canada-trade-corridors.qmd`
- `economic-systems/canada-port-economics.qmd`
- `economic-systems/integrated-network.qmd`
- `laboratory/transportation-network-analysis.qmd`

### Minimum Viable Outputs

- bottleneck ranking
- corridor dependency map
- disruption screening scenarios

### Likely Extensions

- modal substitution
- price impacts
- throughput modelling

## 6. Urban Structure, Accessibility, and Service Allocation

### Primary Roles

- planner
- economic development analyst
- transit strategist
- public-service analyst

### Use Case

Understand access patterns, concentration effects, and service mismatches.

### Research Question

Where are people and services mismatched, and how do accessibility and urban structure shape demand?

### Minimum Data Inputs

- population distribution
- service locations
- network or travel-time structure
- land-use or land-value context

### Likely Chapter Backbone

- `economic-systems/urban-bid-rent-model.qmd`
- `economic-systems/urban-agglomeration-economies.qmd`
- `spatial-analysis/spatial-joins.qmd`
- `spatial-analysis/cost-distance-least-cost-paths.qmd`
- `laboratory/accessibility-and-travel-demand-modeling.qmd`

### Minimum Viable Outputs

- accessibility surface
- underserved-area map
- service allocation options

### Likely Extensions

- demographic change
- network optimization
- equity weighting

## 7. Watershed Condition, Sediment, and Downstream Risk

### Primary Roles

- watershed scientist
- river engineer
- land-use regulator
- restoration planner

### Use Case

Connect upland disturbance, transport pathways, and downstream exposure.

### Research Question

How do terrain, runoff, and land disturbance combine to shape erosion, sediment transport, and downstream risk?

### Minimum Data Inputs

- DEM
- runoff or hydrologic context
- soils and land cover
- channel network
- disturbance or source layers

### Likely Chapter Backbone

- `spatial-analysis/watershed-delineation.qmd`
- `laboratory/soil-erosion-and-the-rusle.qmd`
- `laboratory/sediment-transport-in-rivers.qmd`
- `laboratory/sediment-and-contaminant-transport-in-rivers.qmd`
- `laboratory/groundwater-contaminant-plumes.qmd`

### Minimum Viable Outputs

- source-area screening map
- transport pathway map
- downstream risk zones

### Likely Extensions

- reservoir trapping
- contaminant fate
- calibration with observations

## Role / Function / Use-Case Library

One of the strongest long-term reasons to build golden paths is that they create a second organizational layer that is not topic-first.

This could become a role or function library.

For example:

- `Planner`
- `Field Scientist`
- `Hazard Analyst`
- `Infrastructure Strategist`
- `Remote Sensing Analyst`
- `Watershed Manager`
- `Economic Geographer`
- `Emergency Management Officer`

For each role, the site could later show:

- common motivations
- recurring research questions
- recommended starter paths
- specialist extensions
- likely decision products

This would allow the project to support a wider range of entry points without abandoning the series structure already established in the planning documents.

## Metadata Potential

If golden paths become part of the public site, they will likely benefit from consistent metadata.

Possible fields:

- `path_id`
- `path_title`
- `path_type`
- `primary_roles`
- `path_family`
- `difficulty`
- `spatial_scale`
- `temporal_scale`
- `data_types`
- `primary_outputs`
- `linked_chapters`
- `adjacent_paths`

This would support:

- path landing pages
- filtering by role or use case
- cross-linking from chapter pages
- future editorial planning

## How This Could Change The Book

If done well, golden paths could strengthen the book and series in several ways.

### 1. They Add A Workflow Layer

The current project is rich in concepts and chapters.

Golden paths would show how those concepts assemble into real investigations.

### 2. They Improve Reader Entry

Some readers will enter more confidently through:

- `I am a planner`
- `I need to think about flood risk`
- `I want to monitor drought stress`

rather than through:

- `I should begin with this numbered chapter`

### 3. They Create Better Bridges Between Volumes

The existing architecture already separates:

- flagship pathways
- specialist topic libraries
- advanced laboratory work

Golden paths would provide a natural way to connect those layers without flattening them back into one giant book.

### 4. They Provide A Framework For Future Growth

As new chapters are added, the project would have a clearer way to ask:

- which existing golden path does this strengthen?
- does it create a new path family?
- is it a chapter, a method note, or an applied branch?

## Risks And Failure Modes

The framework will only help if it remains disciplined.

Main risks:

- taxonomy sprawl
- role labels that feel too corporate or abstract
- paths that become so generic they stop being useful
- paths that become so prescriptive they overclaim validity
- too many pilot paths before the framework language is stable

The safest approach is to begin with a small pilot set and learn what readers actually find useful.

## Recommended First Version

The first public or semi-public version should likely include six pilot paths:

1. wildfire risk screening
2. urban flood screening
3. vegetation stress monitoring
4. avalanche exposure
5. trade corridor bottlenecks
6. urban accessibility and service allocation

This is a strong initial set because it:

- spans environmental, hazard, cryosphere, infrastructure, and urban domains
- uses some of the project's strongest existing material
- demonstrates that golden paths are genuinely cross-cutting
- avoids trying to map the full project all at once

## Recommended Next Steps

1. refine the framework language until the concept is concise and stable
2. choose six pilot paths and draft them in a uniform template
3. decide whether the first implementation belongs in `planning/` only or also as public-facing prototype pages
4. define a light metadata model for path pages
5. add chapter-to-path cross-references only after the path templates feel editorially sound

## Current Prototype Pages

Initial pilot drafts now live in:

- [`planning/golden-paths/index.md`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/planning/golden-paths/index.md)
- [`planning/golden-paths/urban-flood-screening.md`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/planning/golden-paths/urban-flood-screening.md)
- [`planning/golden-paths/trade-corridor-bottlenecks.md`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/planning/golden-paths/trade-corridor-bottlenecks.md)

## Working Editorial Thesis

The project has already evolved from one large book into a small publishing ecosystem.

Golden paths would be the next coherent step in that evolution.

They would add:

- a workflow grammar
- a reader-intent layer
- a reusable bridge between concept, method, and application

If the current architecture answers:

- where should this material live?

golden paths would answer:

- how does a reader use this material to investigate a real question?
