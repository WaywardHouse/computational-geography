# Wayward House Computational Geography

This repository is the standalone Quarto scaffold for the current computational geography and environmental modelling program.

Its main editorial job is to hold the flagship `Computational Geography` book, which is the closest Wayward House descendant of the original goal to rebuild the spirit of Mikr Barnsley's `ENVMOD209 Environmental Modelling` text from CRC Press.

The repository currently also contains extension and laboratory material that may later be split into companion volumes.

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

## Current status

This repo scaffold was extracted locally from the shell site so the book can become its own repository.

Editorially, the project is being reshaped away from one oversized continuous textbook and toward:

- one flagship book
- a set of companion books or field guides
- a laboratory line for advanced investigations

Before pushing to a real remote, the next steps are:

1. initialize a dedicated Git remote
2. run full render and QA inside this repo
3. rewrite any remaining shell-specific paths if found
4. decide the final public URL target under `/library/computational-geography/`
# waywardhouse-computational-geography
