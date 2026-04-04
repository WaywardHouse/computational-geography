# Illustration Backlog

This backlog tracks high-value opportunities to improve accessibility for visual learners through diagrams, annotated illustrations, conceptual figures, explainer panels, richer maps, and interactives.

## Priorities

1. Add visuals where the core concept is geometric, sequential, or process-driven.
2. Prefer conceptual diagrams over adding more charts when charts already exist.
3. Prioritize chapters where one strong illustration can significantly reduce cognitive load.

## Laboratory

| Chapter path | Highest-value missing illustration | Recommended visual type | Rationale | Difficulty |
|---|---|---|---|---|
| `laboratory/sar-fundamentals-and-applications.qmd` | Show how a moving antenna synthesizes a long aperture and why azimuth resolution improves | Annotated process diagram | SAR is hard because the key leap is geometric, not algebraic. | Medium |
| `laboratory/insar-deformation-monitoring.qmd` | Show two acquisitions, path-length difference, wrapped fringes, and unwrapping | Four-panel conceptual explainer | InSAR becomes accessible when readers can see acquisition geometry and fringe interpretation before equations. | Medium |
| `laboratory/gravity-remote-sensing-grace.qmd` | Show leading and trailing satellite response over a mass anomaly | Conceptual orbital diagram | GRACE is non-intuitive; a pull-gap diagram would clarify the core measurement idea. | Low |
| `laboratory/passive-microwave-radiometry.qmd` | Show brightness temperature formation from physical temperature plus emissivity, with surface-type comparisons | Layered explainer panel | Visual learners need a "what the sensor sees" frame before dielectric formulas. | Medium |
| `laboratory/rock-weathering-and-soil-formation.qmd` | Show rock to saprolite to soil profile with chemistry, climate, and denudation links | Process cross-section | This chapter spans molecular kinetics to landscape lowering and needs a scale-bridging visual. | Medium |
| `laboratory/soil-erosion-and-the-rusle.qmd` | Show the five RUSLE factors acting on one hillslope | Annotated conceptual illustration | RUSLE is component-based and highly visual in its logic. | Low |
| `laboratory/shallow-landslides-and-slope-stability.qmd` | Show infinite-slope force balance with pore pressure and root reinforcement | Force-balance slope diagram | This is one of the clearest candidates for a visual derivation aid. | Low |
| `laboratory/sediment-transport-in-rivers.qmd` | Show grain entrainment regimes: resting, saltation, suspension | Comparison figure or process strip | Motion regimes are easier to grasp visually than verbally. | Medium |
| `laboratory/channel-morphology-and-hydraulic-geometry.qmd` | Show how width, depth, velocity, and meander wavelength co-scale across channel sizes | Comparative morphology figure | The self-organizing geometry idea is spatial and comparative. | Medium |
| `laboratory/wave-dynamics-and-nearshore-transformation.qmd` | Show deep-water wave to shoaling to breaking to setup across a shore-normal profile | Cross-shore transformation diagram | The chapter's whole logic is a spatial sequence. | Low |
| `laboratory/longshore-sediment-transport-and-coastal-budgets.qmd` | Show wave angle, littoral drift, headland interruption, and sediment budget compartments | Coastal process diagram | Longshore transport is much easier to understand visually. | Low |
| `laboratory/sea-level-storm-surge-and-coastal-morphodynamics.qmd` | Show separate contributions of tide, surge, setup, and sea-level rise on one coast cross-section | Layered hazard diagram | This chapter combines interacting water-level components that benefit from visual stacking. | Medium |
| `laboratory/urban-heat-island-dynamics.qmd` | Show urban canyon energy balance versus rural surface | Annotated comparison section | UHI is easier to understand when buildings, storage, albedo, and turbulent exchange are drawn spatially. | Medium |
| `laboratory/urban-ventilation-and-pollutant-dispersion.qmd` | Show recirculation, channeling, stagnation, and pollutant trapping in street canyons | Flow diagram or annotated section | The intuition is fluid-dynamic and geometric. | Medium |
| `laboratory/transportation-network-analysis.qmd` | Show one real network with shortest path, betweenness choke points, and failure redistribution | Annotated network map | The chapter should show network consequences spatially, not only mathematically. | Medium |
| `laboratory/accessibility-and-travel-demand-modeling.qmd` | Show accessibility surface, impedance decay, and trip-generation linkage | Small multiples or conceptual workflow | Accessibility becomes clearer when origin, impedance, and reachable opportunity are seen together. | Medium |
| `laboratory/land-use-change-modeling.qmd` | Show cell-state transitions, neighborhood effects, and scenario branching | Process flow plus map sequence | Land-use change is dynamic and spatial. | Medium |
| `laboratory/the-kalman-filter-and-sequential-data-assimilation.qmd` | Show prediction, observation, innovation, and update loop | Algorithm flow diagram | A single loop diagram can save pages of explanation. | Low |
| `laboratory/satellite-data-assimilation-in-environmental-models.qmd` | Show model state, satellite retrieval, observation operator, update, and forecast loop | System architecture diagram | Data assimilation becomes concrete when the model-observation relationship is drawn. | Medium |
| `laboratory/reservoir-operations-and-mass-balance.qmd` | Show inflow, storage, release, spill, and demand tradeoffs over one seasonal cycle | Annotated reservoir operation schematic | The chapter is operational and decision-driven. | Low |

## Laboratory Priority Order

1. `laboratory/sar-fundamentals-and-applications.qmd`
2. `laboratory/insar-deformation-monitoring.qmd`
3. `laboratory/gravity-remote-sensing-grace.qmd`
4. `laboratory/shallow-landslides-and-slope-stability.qmd`
5. `laboratory/wave-dynamics-and-nearshore-transformation.qmd`
6. `laboratory/the-kalman-filter-and-sequential-data-assimilation.qmd`

## Notes

- Most laboratory chapters already have charts.
- The bigger opportunity is conceptual illustration rather than additional charting.
- A separate audit for `core-book` and `topic-libraries` is in progress and should be appended here when ready.
