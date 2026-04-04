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

## Core-Book

| Chapter path | Highest-value missing illustration | Recommended visual type | Rationale | Difficulty |
|---|---|---|---|---|
| `foundations/gradient-aspect-steepest-descent.qmd` | Show a sloped surface with the gradient vector uphill, steepest descent downhill, and aspect as a compass-facing quantity | Annotated terrain diagram | This is one of the clearest "see it once, understand it faster" chapters in the core book. | Medium |
| `spatial-analysis/watershed-delineation.qmd` | Show the pipeline from DEM to flow direction to accumulation to streams to watershed boundary | Process-flow sequence | The chapter is really an end-to-end terrain transformation chain. | Medium |
| `environmental-systems/net-radiation-and-albedo.qmd` | Show incoming and outgoing shortwave and longwave around one surface | Energy-budget diagram | Radiation balance is much easier with arrows than with prose alone. | Low |
| `environmental-systems/soil-moisture-dynamics.qmd` | Show infiltration, storage, evapotranspiration, drainage, runoff, and plant uptake in one root-zone profile | Cross-section diagram | Soil moisture is a stock-and-flow system that readers grasp spatially. | Low |
| `spatial-analysis/point-in-polygon-testing.qmd` | Show ray casting with edge crossings counted visually | Interactive widget or algorithm diagram | The odd-even rule becomes obvious when crossings are animated or highlighted. | Medium |
| `atmospheric-hazards/fire-weather-ignition.qmd` | Show the causal chain linking weather, fuel moisture, VPD, wind, and ignition potential | Systems diagram | This chapter teaches a dependency chain, not an isolated formula. | Medium |

## Topic-Libraries

| Chapter path | Highest-value missing illustration | Recommended visual type | Rationale | Difficulty |
|---|---|---|---|---|
| `advanced-remote-sensing/sar-fundamentals.qmd` | Show side-looking radar geometry, repeated pulse positions, synthetic aperture formation, and the range/azimuth distinction | Conceptual geometry diagram | SAR is one of the least intuitive sensing modes; geometry carries the intuition better than algebra. | High |
| `advanced-remote-sensing/hyperspectral-imaging.qmd` | Show a hyperspectral cube plus representative spectra from different materials | Cube diagram plus annotated spectra | Readers need to see the object they are compressing before the later analytics make sense. | Medium |
| `machine-learning/dimensionality-reduction-pca-tsne-umap.qmd` | Show the same dataset under PCA, t-SNE, and UMAP with labeled preservation goals | Comparison figure | The important distinction is what structure each method preserves, not just the method names. | Medium |
| `cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd` | Show start zone, track, runout, terrain trap, and safer route alternatives on one mountain slope | Annotated terrain illustration | This chapter is strongly geometric and hazard-oriented, so a visual route-and-hazard frame would materially improve retention. | Medium |
| `atmospheric-hazards/fire-emissions-smoke.qmd` | Show the chain from fuel consumed to emissions to plume rise to transport to surface concentration | Process-flow diagram | Smoke modeling is a linked process pipeline and benefits from a single visual overview. | Medium |
| `economic-systems/alberta-pipeline-integrated-network.qmd` | Show the integrated network geographically with commodity toggles and bottleneck emphasis | Interactive map | The existing chapter already has strong charts; the next gain is spatial legibility. | High |

## Cross-Volume Priority Order

1. `advanced-remote-sensing/sar-fundamentals.qmd`
2. `spatial-analysis/watershed-delineation.qmd`
3. `foundations/gradient-aspect-steepest-descent.qmd`
4. `cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd`
5. `environmental-systems/net-radiation-and-albedo.qmd`
6. `machine-learning/dimensionality-reduction-pca-tsne-umap.qmd`

## Cross-Volume Priority Cards

### Card 7: SAR Side-Looking Geometry

- Chapter path: `advanced-remote-sensing/sar-fundamentals.qmd`
- Goal: Make side-looking radar geometry legible before readers encounter synthetic aperture and speckle mathematics.
- Deliverable: One concept graphic showing slant range, ground range, azimuth, layover, foreshortening, and shadow on a simple terrain profile.
- Recommended visual type: Conceptual geometry diagram.
- Visual brief:
  - Draw a side-looking radar platform with pulses traveling obliquely to the ground.
  - Label platform track, slant range, ground range, and azimuth direction.
  - Include one sloped terrain feature to show layover, foreshortening, and radar shadow.
  - Add a small inset connecting this geometry to why SAR imagery looks unlike optical imagery.
- Why this matters: This is the gateway intuition for the whole SAR family. Without it, later chapters inherit avoidable cognitive load.
- Acceptance criteria:
  - A reader can point to slant range and azimuth correctly.
  - Terrain distortion mechanisms are visually distinct.
  - The figure prepares readers for later SAR and InSAR chapters.
- Difficulty: High

### Card 8: Watershed Delineation Pipeline

- Chapter path: `spatial-analysis/watershed-delineation.qmd`
- Goal: Show the full DEM-to-basin workflow as a single sequence instead of leaving readers to mentally stitch together processing steps.
- Deliverable: One six-step figure showing DEM, sink filling, flow direction, flow accumulation, stream extraction, and final watershed boundary.
- Recommended visual type: Process-flow sequence.
- Visual brief:
  - Use one stylized terrain example carried through each stage.
  - Keep color treatment consistent so the same ridge, valley, and outlet are recognizable throughout.
  - Label where each algorithmic step changes the data model.
  - End with a clearly highlighted catchment outlet and boundary polygon.
- Why this matters: This chapter is algorithmically straightforward but conceptually multi-step. A process sequence would materially improve retention.
- Acceptance criteria:
  - A reader can explain how flow direction leads to accumulation and then to stream extraction.
  - The visual distinguishes raster transformation from final polygon output.
  - The outlet-to-boundary logic is obvious.
- Difficulty: Medium

### Card 9: Gradient, Aspect, and Steepest Descent

- Chapter path: `foundations/gradient-aspect-steepest-descent.qmd`
- Goal: Anchor the vector calculus ideas in a terrain picture that readers can return to mentally.
- Deliverable: One annotated hillslope illustration showing contour lines, gradient vector, aspect direction, and steepest descent path.
- Recommended visual type: Annotated terrain diagram.
- Visual brief:
  - Show a small hill with contours and a raster-cell inset.
  - Draw the gradient perpendicular to contours and aspect as compass-facing downhill direction.
  - Include a labeled path for steepest descent.
  - Add a tiny “common confusion” inset showing aspect is not the same as gradient magnitude.
- Why this matters: This chapter sits at an important conceptual bridge between maps, DEMs, and spatial analysis workflows.
- Acceptance criteria:
  - A reader can explain why the gradient is perpendicular to contours.
  - Aspect is clearly a direction rather than a magnitude.
  - The steepest-descent connection to later hydrology work is visible.
- Difficulty: Medium

### Card 10: Avalanche Terrain Structure

- Chapter path: `cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd`
- Goal: Make terrain-hazard structure visible at a glance before readers parse slope thresholds and exposure logic.
- Deliverable: One annotated mountain-slope figure showing start zone, track, runout, terrain trap, ridgeline, and safer alternatives.
- Recommended visual type: Annotated terrain illustration.
- Visual brief:
  - Draw a mountain face with one avalanche path from crown to runout.
  - Mark slope-angle bands, convexities, gullies, and terrain traps.
  - Overlay one safer route and one high-exposure route.
  - Use labels that match the chapter's hazard vocabulary.
- Why this matters: The chapter is highly geometric and safety-relevant, so visual terrain literacy is essential rather than optional.
- Acceptance criteria:
  - A reader can identify the three main avalanche-path zones.
  - Terrain traps are visually obvious.
  - The route-choice contrast is immediately legible.
- Difficulty: Medium

### Card 11: Surface Radiation Budget

- Chapter path: `environmental-systems/net-radiation-and-albedo.qmd`
- Goal: Turn the net-radiation equation into a physically intuitive arrow diagram.
- Deliverable: One surface-energy schematic showing incoming and outgoing shortwave and longwave fluxes over contrasting surfaces.
- Recommended visual type: Energy-budget diagram.
- Visual brief:
  - Show sun, atmosphere, and ground or snow surface.
  - Use distinct arrow colors for shortwave and longwave.
  - Label reflected fraction as albedo and show how a darker versus brighter surface changes the balance.
  - Add a small snow-versus-forest comparison inset.
- Why this matters: This chapter's core idea is an accounting balance best learned spatially, not only algebraically.
- Acceptance criteria:
  - A reader can distinguish shortwave from longwave visually.
  - Albedo changes are shown as changes in reflected energy rather than only described.
  - The diagram supports the equation rather than duplicating it.
- Difficulty: Low

### Card 12: PCA vs t-SNE vs UMAP

- Chapter path: `machine-learning/dimensionality-reduction-pca-tsne-umap.qmd`
- Goal: Clarify what each method preserves so readers stop treating them as interchangeable dimensionality-reduction buttons.
- Deliverable: One comparison figure using the same toy dataset under PCA, t-SNE, and UMAP with preservation goals labeled.
- Recommended visual type: Comparison figure.
- Visual brief:
  - Start from one simple high-dimensional-toy-data concept panel.
  - Show three side-by-side 2D embeddings.
  - Label PCA with global variance preservation, t-SNE with local neighborhood preservation, and UMAP with local structure plus better global organization.
  - Include a small “do not over-interpret distance” note under t-SNE.
- Why this matters: The chapter is conceptually comparative. A side-by-side figure would dramatically improve fast comprehension.
- Acceptance criteria:
  - A reader can state one preservation strength and one limitation for each method.
  - The same dataset is visibly used across all three panels.
  - The figure reduces method confusion rather than adding decorative complexity.
- Difficulty: Medium

## Next Queue

- `advanced-remote-sensing/sar-fundamentals.qmd`
- `spatial-analysis/watershed-delineation.qmd`
- `foundations/gradient-aspect-steepest-descent.qmd`
- `cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd`
- `environmental-systems/net-radiation-and-albedo.qmd`
- `machine-learning/dimensionality-reduction-pca-tsne-umap.qmd`
