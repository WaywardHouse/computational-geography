# Site Architecture

## Purpose

This document translates the editorial series plan into a public-facing information architecture.

The model is inspired by how NASA Earthdata clusters content by user intent instead of forcing one single hierarchy to do every job.

That means the project should let readers enter through different doors:

- they may want the main book
- they may want a topic branch
- they may want practical investigations
- they may want methods or setup help

## Core Principle

Do not make one navigation system carry every meaning at once.

The project needs separate clusters for:

- learning sequence
- topical branches
- advanced practice
- methods and tools

## Recommended Top-Level Structure

The public site should cluster material into five visible areas:

1. `Start Here`
2. `Core Book`
3. `Topic Libraries`
4. `Laboratory`
5. `Methods and Tools`

## 1. Start Here

### Role

The calm on-ramp for first-time readers.

### Contents

- how to use the project
- how to read equations
- units, scale, and estimation
- maps, coordinates, and layers
- uncertainty and approximation
- what makes a model computational
- environment setup

### Current Repo Mapping

- `getting-started/`

## 2. Core Book

### Role

The flagship ENVMOD209-inspired linear reading path.

### Reader Promise

If you want one coherent book, this is it.

### Contents

- `Foundations`
- `Environmental Systems`
- `Spatial Analysis`
- selected `Atmospheric Hazards`
- selected `Economic Systems`

### Current Repo Mapping

- `foundations/`
- `environmental-systems/`
- `spatial-analysis/`
- selected chapters from `atmospheric-hazards/`
- selected chapters from `economic-systems/`

## 3. Topic Libraries

### Role

The place for coherent specialist branches that are better browsed by subject than forced into the main staircase.

### Reader Promise

Open these by interest, region, or subfield.

### Initial Library Clusters

- `Remote Sensing Library`
- `Cryosphere and Mountain Systems`
- `Economic Geography and Infrastructure`
- `Machine Learning and Inference`

### Current Repo Mapping

- `advanced-remote-sensing/`
- remote-sensing-adjacent extension chapters from `environmental-systems/`
- `cryosphere-and-mountain-systems/`
- extension-heavy parts of `economic-systems/`
- `machine-learning/`

## 4. Laboratory

### Role

Project-style investigations, advanced applications, and practicum material.

### Reader Promise

This is where readers go to work on harder integrated problems.

### Current Repo Mapping

- `advanced-investigations/`
- `laboratory/`

## 5. Methods and Tools

### Role

Cross-cutting practical resources that support the whole series rather than one branch.

### Possible Contents

- GIS resources
- modelling workflow primers
- remote sensing method guides
- data handling patterns
- statistical method primers
- software setup and environment notes

### Current Repo Mapping

This cluster is currently distributed across:

- `getting-started/`
- `spatial-analysis/`
- `machine-learning/`
- parts of `advanced-remote-sensing/`
- scripts or future resource pages

It may begin as a tagging or navigation layer before it becomes a separate section with its own pages.

## Navigation Model

The homepage should answer five questions quickly:

1. Where do I start?
2. What is the main book?
3. What topics can I browse independently?
4. Where are the advanced projects?
5. Where are the practical methods resources?

## Naming Guidance

Use labels that describe function, not internal editorial history.

Prefer:

- `Start Here`
- `Core Book`
- `Topic Libraries`
- `Laboratory`
- `Methods and Tools`

Avoid making first-time readers decode terms like:

- `Explore More`
- `Extensions`
- `Part 6`

unless they are immediately explained in plain language.

## Repo Implication

The current Quarto book can still contain all material during transition.

But the landing pages and planning documents should already teach readers the new clustered model:

- linear book path for the flagship experience
- subject libraries for branch topics
- laboratory for advanced investigations
- methods and tools as a cross-cutting support layer

## Immediate Next Steps

1. update the homepage to use the five-cluster model
2. rename or reframe `Explore More` as `Topic Libraries`
3. treat `Advanced Investigations` as the front door to the laboratory
4. decide whether `Methods and Tools` should be a dedicated page or a tagged navigation layer first
5. revise the Quarto TOC only after the public language is stable

## Build Model

The repo now supports a practical intermediate step between one giant book and multiple repositories:

- full build in `_book/`
- core book build in `_book-core/`
- topic libraries build in `_book-topics/`
- laboratory build in `_book-lab/`

This allows the public architecture to separate by reader intent without forcing an immediate repo split.
