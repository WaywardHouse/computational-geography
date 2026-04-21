# Phase 2: Methods & Tools Bifurcation

## Goal
Split Methods & Tools into two components:
1. **In-situ pedagogy** — Short, focused methods snippets woven into pathway chapters
2. **Methods Reference companion volume** — Full chapters for deeper dives

## Methods & Tools Chapters (Current)
- how-to-validate-a-model.qmd
- how-to-choose-a-model.qmd
- uncertainty-propagation-and-ensembles.qmd
- simulation-paradigms.qmd
- decision-models-and-optimization.qmd
- bayesian-updating-and-geographic-inference.qmd
- causal-inference-for-geographic-questions.qmd

---

## Where Methods Concepts Naturally Appear

### Pathway A: Remote Sensing & Observation
- Validation: How do we know a classification works? (accuracy assessment)
- Model choice: Which bands to use? Supervised vs. unsupervised?
- Uncertainty: Measurement error in atmospheric correction

### Pathway B: Environmental Systems & Processes
- Validation: Does this model match field measurements?
- Numerical methods: Time-stepping stability and accuracy
- Sensitivity: How does changing inputs affect outputs?
- Parameter fitting: Calibration to observations

### Pathway C: Applications & Implications
- Validation: Fire model vs. observed burn perimeters
- Model choice: Rothermel vs. CFD for fire spread
- Statistical testing: Do observed patterns match predictions?
- Causal inference: What actually drives agglomeration?

---

## In-Situ Teaching Points (Snippets)

### Pattern 1: "Does This Model Work?"
After deriving a model, add 200-400 word subsection:
- Short explanation of validation concept
- Link to Methods Reference Chapter 2 (How to Validate)
- Concrete example from that chapter

### Pattern 2: "Which Model Should We Use?"
When multiple approaches exist, add 300-500 word subsection:
- Trade-offs table (simple vs. complex, empirical vs. physical)
- Link to Methods Reference Chapter 1 (How to Choose)
- Example from pathways

### Pattern 3: "Where Does Uncertainty Come From?"
When inputs have error, add 150-300 word callout:
- Sources (measurement, parameterization, model structure)
- Link to Methods Reference Chapter 3 (Uncertainty Propagation)
- Why this matters for Vol II

**Frequency:** ~20-30 snippets total across all pathways

---

## Methods Reference Companion Volume

**New config:** `_quarto-methods-reference.yml`

### Chapters (Reorganized):

1. **How to Choose a Model** — Empirical vs. mechanistic, simple vs. complex
2. **How to Validate a Model** — Independent data, metrics, residual analysis
3. **Uncertainty Propagation & Ensembles** — Sources, ensemble methods, interpretation
4. **Simulation Paradigms** — Time-stepping, stochastic vs. deterministic, stability
5. **Bayesian Updating & Inference** — Prior/likelihood/posterior, parameter estimation
6. **Causal Inference** — Confounding, causal graphs, observational data
7. **Decision Models & Optimization** — Objectives, constraints, algorithms

**Total:** 7 chapters, ~25-30K words
**Linking:** Each reference chapter has case studies pointing to pathway examples

---

## Implementation Questions

1. **In-situ snippet format:**
   - Subsections within chapters?
   - Callout boxes (visual separation)?
   - Sidebars/footnotes?

2. **Methods Reference publication:**
   - Separate book (published independently)?
   - Part of website but not core book flow?
   - Topic library material?

3. **Vol II assumptions:**
   - Readers have read Methods Reference?
   - Readers know only in-situ foundations?
   - Some concepts repeated with citations?

---

## Critical Files to Modify

1. **_quarto-core-book.yml** — Remove Methods & Tools section
2. **Create _quarto-methods-reference.yml** — New companion config
3. **All Pathway chapters** — Add 20-30 in-situ snippets
4. **methods-and-tools/*.qmd** — Reorganize for reference (not linear)

