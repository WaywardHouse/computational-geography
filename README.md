# Wayward House Computational Geography

This repository is the standalone Quarto scaffold for the current computational geography and environmental modelling program.

Its main editorial job is to hold the flagship `Computational Geography` book, which is the closest Wayward House descendant of the original goal to rebuild the spirit of Mikr Barnsley's `ENVMOD209 Environmental Modelling` text from CRC Press.

The repository currently also contains extension and laboratory material that may later be split into companion volumes.

This repository is intended to be consumed by the main Wayward House site as a git submodule. It is not the deployment surface by itself.

## What is included

- the full book source formerly embedded under `learn/`
- the shared Wayward House theme/runtime files needed for standalone rendering
- the current shared bibliography used by the book
- the current public-facing TOC and chapter inventory planning docs
- the working series architecture for splitting the material into a flagship book plus companion pieces
- the working site architecture for clustering readers by intent: start here, core book, topic libraries, laboratory, and methods

## Local render

```bash
quarto render
```

Output is written to:

- `_book/`

## Split builds

The repo can now also render three clustered outputs without splitting into separate repositories:

- `./scripts/render-core-book.sh` -> `_book-core/`
- `./scripts/render-topic-libraries.sh` -> `_book-topics/`
- `./scripts/render-laboratory.sh` -> `_book-lab/`

These targets support the Earthdata-like clustered publishing model while keeping one source repository.

## Submodule workflow

The intended workflow is:

1. Make editorial and theme changes in this repository.
2. Render locally here for QA.
3. Commit and push this repository.
4. Update the submodule pointer in the main Wayward House site repository.
5. Build and deploy from the main site repository.

This repo should not directly publish rendered output to `waywardhouse.github.io` via its own GitHub Actions workflow.

## Current status

This repo scaffold was extracted locally from the shell site so the book can become its own repository and submodule source.

Editorially, the project is being reshaped away from one oversized continuous textbook and toward:

- one flagship book
- a set of companion books or field guides
- a laboratory line for advanced investigations

Before the main site consumes a new version of this book, the next steps are:

1. run full render and QA inside this repo
2. push the updated book repository
3. update the submodule pointer in the main site
4. build and deploy from the main site repository
# waywardhouse-computational-geography
