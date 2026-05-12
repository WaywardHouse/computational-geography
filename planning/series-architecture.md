# Series Architecture

## Purpose

This document reframes the project as a coherent publishing program instead of a single endlessly expanding book.

The original intent was to rebuild the spirit of Mikr Barnsley's `ENVMOD209 Environmental Modelling` book from CRC Press in a Wayward House form:

- concept-first
- model-centered
- readable by self-directed learners
- computational when computation genuinely clarifies the system

That original goal is still strong.

What drifted was the container.

The project now holds several different kinds of material:

- a beginner-safe modelling textbook spine
- specialist extensions
- advanced laboratory investigations
- domain-specific branches that are substantial enough to stand on their own

The problem is not that there is too much good material.

The problem is that too much of it is still being asked to behave like one book.

## Editorial Thesis

The cleanest structure is:

1. one main book that carries the ENVMOD209 reconstruction goal
2. a small set of companion books or field guides for major specialist branches
3. one laboratory or workbook line for advanced investigations

This keeps the original pedagogical promise intact while giving the larger body of work room to grow without confusing first-time readers.

## The Main Book

## Working Role

`Computational Geography` should remain the flagship book.

It should be the closest descendant of the ENVMOD209 ambition:

- a serious introduction to environmental modelling
- broadened through geography, GIS, and human systems
- structured as a guided climb rather than an archive

## What Belongs In It

The main book should include:

- `Getting Started`
- `Foundations`
- `Environmental Systems`
- `Spatial Analysis`
- a selective `Hazards, Change, and Prediction` section
- a selective `Cities, Networks, and Economic Geography` section

This is the core teaching path.

It is the book most readers should be able to begin and finish.

## What It Should Not Try To Be

The main book should not also try to be:

- a full remote sensing methods handbook
- a cryosphere specialist text
- a full economic geography reference
- a machine learning methods survey
- a compendium of advanced environmental modelling case studies

Those are valid projects.

They are just different projects.

## Proposed Series Shape

## Book 1: Computational Geography

### Role

The flagship introductory book.

### Promise

If you want the rebuilt ENVMOD209-style experience, start here.

### Internal Structure

1. `Getting Started`
2. `Maths for Modelling Space`
3. `Earth Systems and Observation`
4. `Part 3: GIS and Spatial Analysis`
5. `Hazards, Change, and Prediction`
6. `Cities, Networks, and Economic Geography`

### Scope Rule

Only keep chapters that strengthen the beginner-to-intermediate modelling staircase.

If a chapter mainly serves specialist depth, it should move to a companion piece even if it is excellent.

## Companion 1: Remote Sensing for Environmental Modelling

### Role

A focused methods companion for sensing, retrieval, and observation systems.

### Likely Inputs

- orbital and sensing geometry chapters currently inside `environmental-systems`
- all of `advanced-remote-sensing`
- selected laboratory chapters such as SAR, InSAR, GRACE, and passive microwave

### Why It Deserves Its Own Container

Remote sensing is coherent enough to read as a technical strand instead of as scattered optional chapters.

It is also one of the clearest bridges from environmental modelling into real observational practice.

## Companion 2: Cryosphere and Mountain Systems

### Role

A field-focused systems book on snow, ice, permafrost, slopes, and alpine hazards.

### Likely Inputs

- all of `cryosphere-and-mountain-systems`
- selected laboratory chapters on slope stability, debris, hydrology, or related hazards when they fit naturally

### Why It Deserves Its Own Container

This material has strong internal coherence, clear regional identity, and a distinct audience.

It reads better as a branch text than as a side hallway off the main beginner book.

## Companion 3: Economic Geography and Infrastructure Systems

### Role

A human-systems companion focused on trade, transport, cities, pricing, energy, and networks.

### Likely Inputs

- the full `economic-systems` collection

### Editorial Rule

Keep four to six chapters in the flagship book as the human-systems gateway:

- gravity
- bid-rent
- agglomeration
- spatial arbitrage

Move the denser pipeline, infrastructure, and integrated-system families into this companion line.

### Why It Deserves Its Own Container

It is one of the project's most distinctive strengths, but it is large enough to overwhelm the environmental-modelling spine if it remains embedded as a near-equal book within the book.

## Companion 4: Geographic Machine Learning and Inference

### Role

A methods companion for regression, dimensionality reduction, Bayesian thinking, ensembles, and data assimilation.

### Likely Inputs

- `machine-learning`
- the statistical and inference-heavy parts of `laboratory`

### Why It Deserves Its Own Container

These chapters work best once readers already understand models, variables, uncertainty, and spatial data structure.

They are advanced methods, not core onboarding.

## Workbook Line: Computational Geography Laboratory

### Role

A laboratory, workbook, or investigations series rather than a conventional linear textbook.

### Likely Inputs

- the current `laboratory` collection

### Framing

This should be presented as:

- advanced investigations
- project-style studies
- worked applications
- optional practicum material

Not every strong chapter needs to migrate out of the lab.

Some topics belong there precisely because they are best encountered as problems to work through rather than chapters to read straight through.

## Decision Rules For Future Placement

When deciding where a chapter belongs, use these questions:

1. Does this chapter help a first-time reader continue the main modelling staircase?
2. Is its main value conceptual foundation, specialist depth, or project application?
3. Would a reader reasonably seek this topic as part of a dedicated subfield?
4. Does it depend on too much prior knowledge to be fair in the flagship book?

Use the answers this way:

- if it advances the main staircase, keep it in the flagship book
- if it is specialist but internally coherent with a branch, move it to a companion
- if it is best learned as an investigation or applied exercise, place it in the laboratory line

## Practical Repo Implication

This repository can still temporarily hold the full material set during restructuring.

But editorially it should now be treated as:

- the home of the flagship book first
- the staging ground for extracting companion volumes second

That means future TOC and landing-page decisions should optimize for the flagship reader journey, not for exposing every available chapter equally.

For the public navigation model that supports this series split, see [`planning/site-architecture.md`](/Users/pauldhobson/src/websites/waywardhouse-computational-geography/planning/site-architecture.md).

## Immediate Next Moves

1. lock the flagship `Computational Geography` TOC to the true core path plus a small number of gateway extension chapters
2. mark companion-bound chapters explicitly in the planning inventory
3. consolidate the duplicate or parallel infrastructure chapter families in `economic-systems`
4. decide whether companion books remain in this repo temporarily or move into sibling repos once stable
5. rename public-facing sections so readers can tell the difference between `main book`, `companions`, and `laboratory`
