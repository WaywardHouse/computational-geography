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

## Laboratory Priority Cards

### Card 1: SAR Aperture Synthesis Geometry

- Chapter path: `laboratory/sar-fundamentals-and-applications.qmd`
- Goal: Make synthetic aperture formation visually obvious before readers meet the resolution math.
- Deliverable: One annotated concept graphic showing a moving platform, successive pulse positions, overlapping returns, and the resulting synthetic aperture length versus physical antenna length.
- Recommended visual type: Annotated process diagram.
- Visual brief:
  - Draw the satellite track with several pulse positions.
  - Show one target patch on the ground being observed from multiple positions.
  - Label physical antenna length, synthetic aperture length, range direction, and azimuth direction.
  - Include a small before/after inset comparing coarse physical-aperture azimuth resolution versus sharpened SAR azimuth resolution.
- Why this matters: The hardest conceptual leap in SAR is geometric. If that leap is visualized well, the later algebra reads as explanation instead of mystery.
- Acceptance criteria:
  - A first-time reader can point to azimuth and range directions correctly.
  - The diagram makes clear why motion improves azimuth resolution.
  - The figure is interpretable without reading the full derivation first.
- Difficulty: Medium

### Card 2: InSAR Phase and Unwrapping Sequence

- Chapter path: `laboratory/insar-deformation-monitoring.qmd`
- Goal: Reduce cognitive load in the phase-displacement sections.
- Deliverable: One four-panel explainer showing acquisition geometry, path-length difference, wrapped fringes, and phase unwrapping to displacement.
- Recommended visual type: Four-panel conceptual explainer.
- Visual brief:
  - Panel 1: Two SAR acquisitions from slightly different positions/times over the same ground target.
  - Panel 2: Range difference translated into phase difference.
  - Panel 3: Wrapped phase shown as repeating color cycles.
  - Panel 4: Unwrapped phase converted to a smooth displacement field.
  - Keep line-of-sight displacement explicit.
- Why this matters: InSAR is teachable when readers can see fringe logic in sequence. Without that, the notation feels abstract too early.
- Acceptance criteria:
  - The reader can explain what one fringe cycle means.
  - The distinction between wrapped and unwrapped phase is visually obvious.
  - The line-of-sight measurement limitation is visible in the figure.
- Difficulty: Medium

### Card 3: GRACE Pull-Gap Measurement Concept

- Chapter path: `laboratory/gravity-remote-sensing-grace.qmd`
- Goal: Make the measurement principle legible at a glance.
- Deliverable: One orbital schematic showing leading and trailing satellites crossing a mass anomaly and the inter-satellite gap changing.
- Recommended visual type: Conceptual orbital diagram.
- Visual brief:
  - Show two satellites on the same track with a labeled separation distance.
  - Show a groundwater/ice mass anomaly below.
  - Indicate slight acceleration of the lead satellite first, then the trailing satellite.
  - Add a small callout for range-rate measurement and how repeated passes become monthly mass-change maps.
- Why this matters: GRACE feels magical until the geometry is seen. This is a high-payoff low-complexity illustration.
- Acceptance criteria:
  - A reader can describe why the gap first grows and then shrinks.
  - The link between mass anomaly and range-rate change is explicit.
  - The figure supports, rather than duplicates, the chapter text.
- Difficulty: Low

### Card 4: Infinite Slope Force Balance

- Chapter path: `laboratory/shallow-landslides-and-slope-stability.qmd`
- Goal: Support the derivation with a physical picture of forces and effective stress.
- Deliverable: One slope cross-section showing soil depth, failure plane, driving force, resisting force, pore pressure, and root reinforcement.
- Recommended visual type: Force-balance slope diagram.
- Visual brief:
  - Show a planar hillslope and shallow soil slab over a failure plane.
  - Label slab thickness `z`, slope angle `beta`, groundwater height, and root zone.
  - Use arrows for downslope shear stress, normal force, pore-pressure effect, and root reinforcement.
  - Include a dry-versus-wet inset or side-by-side mini comparison.
- Why this matters: This chapter is a classic case where one diagram can carry a large share of the intuition.
- Acceptance criteria:
  - The reader can map each major term in the factor-of-safety expression to a visible part of the figure.
  - The effect of increasing pore pressure is visually immediate.
  - The role of root reinforcement is explicit rather than implied.
- Difficulty: Low

### Card 5: Nearshore Wave Transformation Profile

- Chapter path: `laboratory/wave-dynamics-and-nearshore-transformation.qmd`
- Goal: Show the spatial sequence from deep water to surf zone before the equations are asked to do all the work.
- Deliverable: One shore-normal profile illustration showing wavelength shortening, shoaling, steepening, breaking, and setup.
- Recommended visual type: Cross-shore transformation diagram.
- Visual brief:
  - Draw offshore deep water, intermediate depth, shoaling zone, breaker zone, and swash zone.
  - Show one incoming wave train changing form as depth decreases.
  - Label wave height increase, wavelength decrease, celerity decrease, and breaking point.
  - Add a subtle water-level setup indication nearshore.
- Why this matters: The chapter is fundamentally a process sequence in space. A spatial figure should anchor the entire model.
- Acceptance criteria:
  - A reader can trace the wave from deep water to breaking without relying on equations.
  - The connection between depth change and wave transformation is explicit.
  - The figure prepares the reader for shoaling and breaking calculations.
- Difficulty: Low

### Card 6: Kalman Filter Update Loop

- Chapter path: `laboratory/the-kalman-filter-and-sequential-data-assimilation.qmd`
- Goal: Give readers a durable mental model for sequential state estimation.
- Deliverable: One loop diagram showing forecast state, observation, innovation/residual, Kalman gain, and updated analysis state.
- Recommended visual type: Algorithm flow diagram.
- Visual brief:
  - Show the cycle `predict -> compare -> update -> predict`.
  - Include state estimate, uncertainty, observation, and model forecast as distinct boxes.
  - Label the innovation as "observation minus forecast".
  - Include a small note that high observation uncertainty means smaller correction, and vice versa.
- Why this matters: The Kalman filter is often easy mathematically once the loop is understood, but opaque without that loop.
- Acceptance criteria:
  - The reader can state what the innovation is.
  - The direction of information flow between model and observation is obvious.
  - The diagram makes uncertainty an active part of the update, not a side note.
- Difficulty: Low

## Notes

- Most laboratory chapters already have charts.
- The bigger opportunity is conceptual illustration rather than additional charting.
- A separate audit for `core-book` and `topic-libraries` is in progress and should be appended here when ready.
