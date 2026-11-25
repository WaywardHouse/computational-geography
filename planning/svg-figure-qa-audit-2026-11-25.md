# SVG figure QA audit (2026-11-25)

Scope: all 77 inline `<svg>` figures in `.qmd` sources (61 chapters). Each was rendered in headless Firefox (Arial stand-in for Barlow, so slightly pessimistic on width) and measured.

**Result: 54 of 77 have at least one automatically detected defect; 23 are clean on these checks.** Visual review of a sample confirms the defects are real and often severe.

Checks: CLIP = text extends past the viewBox (cut off); T/T = text bbox overlaps other text; T/L = text sits on a stroked line/path. The audit does **not** catch oversized arrowheads or text over filled shapes, so clean does not mean good.

## Fix pass (same day): 54 flagged -> 1

Re-run of the same audit after fixes: **1 of 77 figures still flagged** (soil-heat-diffusion, an intentional pair of stacked two-line labels). Every figure that was flagged was also re-rendered and checked by eye.

What was done (all repeatable from the repo root):
- `scripts/fix-svg-markers-and-halos.py`: arrowheads no longer scale with stroke width (27 figures); 97 labels that sat on lines got a background-colour outline.
- `scripts/svg-qa/apply-wraps.py`: 44 over-long labels wrapped into `<tspan>` lines or shifted to fit the frame (measured in the browser).
- `scripts/svg-qa/hand-fixes.py`: ~40 per-figure layout edits (moved labels, widened frames/caption pills, taller canvases, fixed z-order of a translucent overlay, relocated captions).
- `scripts/svg-qa/run-audit.sh`: re-render and re-measure all figures (Firefox headless). `audit-baseline.txt` is the original "before" result.
- Click-to-zoom lightbox for these figures added to the theme extension (`include-after-body.html` + `theme.scss`).

Not covered by the automated checks: text over filled shapes and general aesthetics. The photosynthesis y-axis label was a false positive of the checker (rotated text) but was genuinely clipped and was fixed anyway.

---

## Systemic causes

1. **Labels are single `<text>` strings longer than the canvas**, e.g. "bottom position depends on speed, angle," cut off at the right edge. Needs wrapping into `<tspan>` lines or shorter copy.

2. **Arrow markers scale with stroke width** (`markerUnits` default `strokeWidth` with 6px strokes), so arrowheads are huge and cover labels and boxes (compound-hazards, thermal-infrared, prospect). Set `markerUnits="userSpaceOnUse"` or shrink marker size.

3. **Labels placed on top of their own leader lines/curves** with no halo. Add `paint-order="stroke"` with a light stroke on text, or move labels off the lines.

4. **Labels pinned to other labels** (e.g. sar-fundamentals "platform motion" under "physical antenna"; prospect-leaf "high NIR reflectance" over "palisade mesophyll").

5. Many figures are not sized for the frame: content is left-heavy with right-side labels falling off.

## Per-figure results (worst first)

| Figure | Source | Clipped | Text/text | Text/line |
|---|---|---|---|---|
| atmospheric-hazards__boundary-layer-turbulence__1 | atmospheric-hazards/boundary-layer-turbulence.qmd:178 | 3 | 1 | 3 |
| foundations__earth-as-rotating-sphere__1 | foundations/earth-as-rotating-sphere.qmd:57 | 4 | 0 | 1 |
| atmospheric-hazards__thunderstorm-dynamics__1 | atmospheric-hazards/thunderstorm-dynamics.qmd:190 | 1 | 2 | 2 |
| advanced-remote-sensing__sar-fundamentals__1 | advanced-remote-sensing/sar-fundamentals.qmd:174 | 0 | 1 | 5 |
| atmospheric-hazards__fire-weather-ignition__1 | atmospheric-hazards/fire-weather-ignition.qmd:111 | 2 | 0 | 3 |
| environmental-systems__net-radiation-and-albedo__1 | environmental-systems/net-radiation-and-albedo.qmd:130 | 1 | 1 | 3 |
| environmental-systems__soil-heat-diffusion__1 | environmental-systems/soil-heat-diffusion.qmd:123 | 2 | 0 | 3 |
| advanced-remote-sensing__prospect-leaf-optical-properties__1 | advanced-remote-sensing/prospect-leaf-optical-properties.qmd:123 | 1 | 1 | 2 |
| atmospheric-hazards__hail-formation-forecasting__1 | atmospheric-hazards/hail-formation-forecasting.qmd:192 | 1 | 0 | 4 |
| cryosphere-and-mountain-systems__avalanche-terrain-analysis__1 | cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd:153 | 1 | 0 | 4 |
| cryosphere-and-mountain-systems__glacial-lake-outburst-floods__1 | cryosphere-and-mountain-systems/glacial-lake-outburst-floods.qmd:190 | 1 | 0 | 4 |
| cryosphere-and-mountain-systems__glacial-meltwater-chemistry__1 | cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd:167 | 1 | 1 | 2 |
| economic-systems__canada-trade-corridors__1 | economic-systems/canada-trade-corridors.qmd:151 | 3 | 0 | 0 |
| environmental-systems__decomposition-and-soil-carbon__1 | environmental-systems/decomposition-and-soil-carbon.qmd:160 | 1 | 2 | 0 |
| environmental-systems__land-atmosphere-coupling-and-feedbacks__1 | environmental-systems/land-atmosphere-coupling-and-feedbacks.qmd:121 | 0 | 0 | 6 |
| atmospheric-hazards__tornado-formation-intensity__1 | atmospheric-hazards/tornado-formation-intensity.qmd:194 | 2 | 0 | 1 |
| cryosphere-and-mountain-systems__debris-flow-modeling__1 | cryosphere-and-mountain-systems/debris-flow-modeling.qmd:160 | 0 | 0 | 5 |
| environmental-systems__photosynthesis-light-response__1 | environmental-systems/photosynthesis-light-response.qmd:139 | 1 | 0 | 3 |
| environmental-systems__soil-moisture-dynamics__1 | environmental-systems/soil-moisture-dynamics.qmd:158 | 0 | 2 | 1 |
| environmental-systems__temperature-moisture-gradients__1 | environmental-systems/temperature-moisture-gradients.qmd:147 | 1 | 0 | 3 |
| environmental-systems__wind-profiles-and-turbulence__1 | environmental-systems/wind-profiles-and-turbulence.qmd:158 | 0 | 1 | 3 |
| advanced-remote-sensing__bathymetric-lidar-sonar__1 | advanced-remote-sensing/bathymetric-lidar-sonar.qmd:190 | 1 | 0 | 2 |
| advanced-remote-sensing__gravity-remote-sensing__1 | advanced-remote-sensing/gravity-remote-sensing.qmd:185 | 1 | 0 | 2 |
| advanced-remote-sensing__hyperspectral-imaging__1 | advanced-remote-sensing/hyperspectral-imaging.qmd:162 | 2 | 0 | 0 |
| advanced-remote-sensing__thermal-infrared-remote-sensing__1 | advanced-remote-sensing/thermal-infrared-remote-sensing.qmd:177 | 1 | 0 | 2 |
| atmospheric-hazards__compound-hazards-and-cascading-risk__1 | atmospheric-hazards/compound-hazards-and-cascading-risk.qmd:106 | 2 | 0 | 0 |
| atmospheric-hazards__fire-emissions-smoke__1 | atmospheric-hazards/fire-emissions-smoke.qmd:233 | 1 | 0 | 2 |
| cryosphere-and-mountain-systems__permafrost-thaw-geohazards__1 | cryosphere-and-mountain-systems/permafrost-thaw-geohazards.qmd:173 | 1 | 1 | 0 |
| environmental-systems__multispectral-imagery-and-band-interpretation__1 | environmental-systems/multispectral-imagery-and-band-interpretation.qmd:137 | 1 | 1 | 0 |
| foundations__spatial-diffusion-of-innovation__1 | foundations/spatial-diffusion-of-innovation.qmd:112 | 0 | 0 | 4 |
| foundations__spatial-spectral-temporal-and-radiometric-resolution__2 | foundations/spatial-spectral-temporal-and-radiometric-resolution.qmd:96 | 1 | 1 | 0 |
| foundations__spectral-mixing-and-sensor-response__1 | foundations/spectral-mixing-and-sensor-response.qmd:60 | 0 | 2 | 0 |
| environmental-systems__carbon-allocation-and-npp__1 | environmental-systems/carbon-allocation-and-npp.qmd:140 | 1 | 0 | 1 |
| environmental-systems__nitrogen-cycling__1 | environmental-systems/nitrogen-cycling.qmd:135 | 0 | 1 | 1 |
| foundations__atmospheric-effects-and-surface-reflectance__1 | foundations/atmospheric-effects-and-surface-reflectance.qmd:72 | 0 | 0 | 3 |
| foundations__exponential-growth-and-logarithms__1 | foundations/exponential-growth-and-logarithms.qmd:107 | 0 | 0 | 3 |
| foundations__gravity-models-trade-migration__1 | foundations/gravity-models-trade-migration.qmd:122 | 0 | 1 | 1 |
| foundations__logistic-growth-and-equilibrium__1 | foundations/logistic-growth-and-equilibrium.qmd:114 | 1 | 0 | 1 |
| advanced-remote-sensing__sail-canopy-reflectance__1 | advanced-remote-sensing/sail-canopy-reflectance.qmd:139 | 1 | 0 | 0 |
| cryosphere-and-mountain-systems__slope-stability-analysis__1 | cryosphere-and-mountain-systems/slope-stability-analysis.qmd:146 | 1 | 0 | 0 |
| cryosphere-and-mountain-systems__snow-accumulation-melt-modeling__1 | cryosphere-and-mountain-systems/snow-accumulation-melt-modeling.qmd:152 | 0 | 0 | 2 |
| environmental-systems__sensible-and-latent-heat-fluxes__1 | environmental-systems/sensible-and-latent-heat-fluxes.qmd:132 | 0 | 0 | 2 |
| foundations__digital-elevation-models-as-functions__1 | foundations/digital-elevation-models-as-functions.qmd:134 | 1 | 0 | 0 |
| foundations__gradient-aspect-steepest-descent__1 | foundations/gradient-aspect-steepest-descent.qmd:131 | 0 | 0 | 2 |
| foundations__hydrological-flow-as-optimization__1 | foundations/hydrological-flow-as-optimization.qmd:61 | 0 | 0 | 2 |
| foundations__light-attenuation-in-canopy__2 | foundations/light-attenuation-in-canopy.qmd:76 | 1 | 0 | 0 |
| foundations__linear-change-and-rate__1 | foundations/linear-change-and-rate.qmd:98 | 0 | 0 | 2 |
| foundations__solar-geometry-and-projection__2 | foundations/solar-geometry-and-projection.qmd:78 | 0 | 0 | 2 |
| machine-learning__dimensionality-reduction-pca-tsne-umap__3 | machine-learning/dimensionality-reduction-pca-tsne-umap.qmd:271 | 1 | 0 | 0 |
| economic-systems__canada-trade-gravity-model__1 | economic-systems/canada-trade-gravity-model.qmd:80 | 0 | 0 | 1 |
| economic-systems__markets-spatial-arbitrage__1 | economic-systems/markets-spatial-arbitrage.qmd:54 | 0 | 0 | 1 |
| environmental-systems__vegetation-indices-and-remote-sensing__1 | environmental-systems/vegetation-indices-and-remote-sensing.qmd:134 | 0 | 0 | 1 |
| foundations__what-is-remote-sensing__1 | foundations/what-is-remote-sensing.qmd:126 | 0 | 0 | 1 |
| spatial-analysis__time-series-analysis__1 | spatial-analysis/time-series-analysis.qmd:139 | 0 | 0 | 1 |

## Clean on automated checks (still check by eye)

advanced-remote-sensing__lidar-point-clouds__1, cryosphere-and-mountain-systems__glacier-mass-balance__1, foundations__earth-as-rotating-sphere__2, foundations__hydrological-flow-as-optimization__2, foundations__light-attenuation-in-canopy__1, foundations__map-projections-and-coordinate-reference-systems__1, foundations__map-projections-and-coordinate-reference-systems__2, foundations__map-projections-and-coordinate-reference-systems__3, foundations__map-projections-and-coordinate-reference-systems__4, foundations__map-projections-and-coordinate-reference-systems__5, foundations__map-projections-and-coordinate-reference-systems__6, foundations__map-projections-and-coordinate-reference-systems__7, foundations__solar-geometry-and-projection__1, foundations__spatial-spectral-temporal-and-radiometric-resolution__1, foundations__spatial-spectral-temporal-and-radiometric-resolution__3, foundations__spatial-spectral-temporal-and-radiometric-resolution__4, foundations__spectral-mixing-and-sensor-response__2, machine-learning__dimensionality-reduction-pca-tsne-umap__1, machine-learning__dimensionality-reduction-pca-tsne-umap__2, methods-and-tools__causal-inference-for-geographic-questions__1, spatial-analysis__cost-distance-least-cost-paths__1, spatial-analysis__raster-resampling-interpolation__1, spatial-analysis__watershed-delineation__1
