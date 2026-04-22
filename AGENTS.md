# AGENTS.md — Computational Geography Project

> Shared instructions for all AI agents (Claude Code, Codex, Gemini, etc.).
> Claude Code: also read `CLAUDE.md` (this file is the authoritative project spec).

---

## What this project is

A multi-book computational geography platform built in Quarto. Not a linear textbook — a **modular learning platform** with explicit prerequisite chains. Serves three roles simultaneously:

1. **Essays** — falsifiable geographic theses and analytical context
2. **Systems digest** — current-event hooks connected to models
3. **Structured library** — learning the computational machinery

The core book is being restructured from a flat 53-chapter shovel-to-the-face into **three parallel learning pathways** with math-only Foundations as a shared prerequisite. A companion Laboratory of 39 project-based investigations is organized into **6 thematic problem sets**.

---

## Repository structure

```
waywardhouse-computational-geography/
├── AGENTS.md                        ← this file
├── CLAUDE.md                        ← Claude Code addendum
├── README.md
├── _quarto.yml                      ← default Quarto config (main site)
├── _quarto-core-book.yml            ← Core Book (3 pathways)
├── _quarto-laboratory.yml           ← Laboratory (6 problem sets)
├── _quarto-topic-libraries.yml      ← Topic Libraries (companions)
│
├── getting-started/                 ← Part 1: orientation (7 chapters)
├── foundations/                     ← Part 1: math-only (7–10 chapters)
├── scientific-computing/            ← Part 1: Python setup (10 chapters, PLANNED)
│
├── remote-sensing/                  ← Pathway A chapters
├── environmental-systems/           ← Pathway B chapters
├── applications/                    ← Pathway C chapters
│
├── laboratory/                      ← 39 investigations; 6 problem sets
│   ├── index.qmd                    ← Problem set overview
│   ├── laboratory-navigation.qmd    ← How to choose your path
│   └── *.qmd                        ← Investigation chapters
│
├── methods-and-tools/               ← 7 chapters → being split (see Phase 2)
├── cryosphere-and-mountain-systems/ ← Future Companion 2
├── advanced-remote-sensing/         ← Future Companion 1
├── machine-learning/                ← Future Companion 4
├── economic-systems/                ← Future Companion 3
│
├── planning/                        ← Architecture decisions (read before acting)
│   ├── phase-2-methods-tools-bifurcation.md
│   ├── phase-3-topic-libraries.md
│   ├── phase-3-geographic-gaps.md
│   ├── phase-4-laboratory.md
│   ├── laboratory-index.csv         ← All 39 investigations: metadata
│   ├── scientific-computing-foundations-outline.md
│   └── ucl-curriculum-alignment.md
│
├── scripts/
│   └── add-lab-metadata.py          ← Bulk metadata insertion (idempotent)
│
└── assets/
```

---

## Active branch

**Always work on:** `restructure/pathways-v1`

```bash
git checkout restructure/pathways-v1
```

Do **not** push to `main` without explicit user approval.

---

## Build system

Four separate Quarto book configs:

| Config | Output | Purpose |
|---|---|---|
| `_quarto-core-book.yml` | `_book-core/` | Main learning platform |
| `_quarto-laboratory.yml` | `_book-lab/` | 39 investigations, 6 problem sets |
| `_quarto-topic-libraries.yml` | `_book-topic/` | Topic library chapters |
| `_quarto.yml` | `_book/` | Default full render |

**To render a specific book:**
```bash
quarto render --profile core      # or: quarto render _quarto-core-book.yml
quarto render --profile lab       # or: quarto render _quarto-laboratory.yml
```

**Do not** run `quarto render` (default) without a specific profile unless explicitly requested — it renders everything and takes a long time.

---

## Chapter frontmatter conventions

### Core book chapters (pathway/foundations)
```yaml
---
title: "Chapter Title"
type: chapter
book-part: "pathway-b"           # pathway-a | pathway-b | pathway-c | foundations | getting-started
pathway-prerequisites:
  - "Foundations: Linear Change and Rate"
next-steps:
  - "Pathway B, Chapter 6: Soil Heat Diffusion"
methods-anchor: "validation"     # Optional: which methods snippet to embed
---
```

### Laboratory investigation chapters

All 39 lab chapters now have these fields (added by `scripts/add-lab-metadata.py`):
```yaml
---
problem-set: "B"                 # A | B | C | D | E | F
lab-level: "Advanced"            # Beginner | Intermediate | Advanced
est-hours: 12
pathway-prerequisites:
  - "Pathway B: Watershed Delineation"
  - "Methods Reference: Uncertainty Propagation"
backward-link: "Pathway B, Watershed Delineation — apply mass balance to a real reservoir system"
section-code: "B"                # matches problem-set letter
section-title: "Problem Set B: Water Systems & Hydrology"
---
```

---

## Completed phases

| Phase | Description | Status |
|---|---|---|
| 1 | Core book restructured: 3 pathways in `_quarto-core-book.yml` | ✅ Done |
| 1.5 | Scientific Computing Foundations outline written | ✅ Done |
| 2 | Methods & Tools bifurcation strategy planned | ✅ Done |
| 3 | Topic Libraries → 4 Companion Books planned | ✅ Done |
| 3b | Geographic gaps documented | ✅ Done |
| 4 | Laboratory problem set planning (42→6 groups) | ✅ Done |
| 5 | `_quarto-laboratory.yml` reorganized; `laboratory-navigation.qmd` written | ✅ Done |
| 6 | All 39 lab chapters updated with problem-set frontmatter metadata | ✅ Done |
| 7 | Core book chapter metadata (`pathway-prerequisites`, `next-steps`) | ✅ Done |
| 8 | Methods Reference companion volume config | ✅ Done |
| 9 | Four Companion Book configs created | ✅ Done |
| 10 | Scientific Computing Foundations (10 chapters written) | ✅ Done |
| 11 | "Before You Start" sections standardized in lab chapters | ✅ Done |
| 12 | Graph/Ontology layer established via JSON/Script | ✅ Done |

---

## Remaining work (priority order)

No planned phases remaining! The structural overhaul is complete.

## Key conventions

### Do
- Keep all changes on branch `restructure/pathways-v1`
- Commit after each phase/subphase with clear commit messages: `"Phase N: Description"`
- Use idempotent scripts for bulk chapter updates (check "already has this field" before inserting)
- Preserve existing frontmatter when adding new fields — do not overwrite existing keys
- Maintain the planning docs in `planning/` as the single source of truth for architecture decisions

### Don't
- Don't touch `_quarto.yml` (default config) unless asked — it's the legacy full-book render
- Don't rename existing chapter files without updating ALL four quarto configs + any cross-references
- Don't add geographic content from underrepresented regions until Phase 12 (geographic gaps) — document in `planning/phase-3-geographic-gaps.md` instead
- Don't merge to `main` without user approval
- Don't `quarto render` the full book without a specific config flag

---

## Planning documents (must read before major changes)

| File | Contents |
|---|---|
| `planning/phase-2-methods-tools-bifurcation.md` | Which methods concepts belong in which chapters; 7-chapter reference structure |
| `planning/phase-3-topic-libraries.md` | 4 companion books: chapter lists, new chapters needed, quarto config names |
| `planning/phase-3-geographic-gaps.md` | Geographic blind spots; priority tiers; NOT to be filled yet |
| `planning/phase-4-laboratory.md` | Problem set structure; prerequisite map; backward link conventions |
| `planning/laboratory-index.csv` | All 39 lab investigations with full metadata |
| `planning/scientific-computing-foundations-outline.md` | 10-chapter outline for Part 1 scientific computing section |

---

## Style guide

- **UK/Canadian English** — "modelling", "colour", "behaviour", "neighbourhood"
- **Prose-first** — derive before you define; intuition before formalism
- **Code cells** use Python 3 with NumPy, SciPy, Matplotlib, xarray as defaults
- **Quarto callouts** for optional depth: `::: {.callout-note}` for pedagogy, `::: {.callout-tip}` for methods links
- **Section numbering** is off (`number-sections: false`)
- **Math** via KaTeX (already configured); use `$$` for display, `$` for inline
- **Chapter length target:** 3,000–5,000 words per pathway chapter; 2,000–4,000 per lab investigation

---

## Repo metadata

- **Owner:** Paul Hobson (p.d.hobson@icloud.com)
- **Branch for this work:** `restructure/pathways-v1`
- **Quarto version:** See `_quarto.yml`
- **Published via:** GitHub Actions (`.github/workflows/`)
- **Consumed by:** Wayward House main site as a git submodule
