# GEMINI.md — Computational Geography Project

> Gemini CLI: read `AGENTS.md` first — it is the authoritative project spec.
> This file adds Gemini-specific notes only.
eg

## Quick orientation

See `AGENTS.md` for the full project context, structure, completed phases, and remaining work.

---

## Gemini-specific reminders

### Working branch
Always confirm you are on `restructure/pathways-v1` before making changes:
```bash
git branch --show-current
```

### File modification approach
- Read a file before editing it
- For bulk chapter updates, write a Python script in `scripts/` and run it rather than editing files one-by-one
- The pattern `scripts/add-lab-metadata.py` is a good template for idempotent bulk updates

### Committing
Each completed phase deserves its own commit:
```bash
git add <specific files>
git commit -m "Phase N: short description of what changed"
```

### Quarto configs
There are four separate book configs — don't confuse them:
- `_quarto-core-book.yml` → Core learning platform
- `_quarto-laboratory.yml` → 39 lab investigations
- `_quarto-topic-libraries.yml` → Topic libraries
- `_quarto.yml` → Legacy default (avoid rendering this)

### Pre-approved actions (no need to confirm)
- Frontmatter additions/updates to `.qmd` files on `restructure/pathways-v1`
- New `.qmd` chapters in `scientific-computing/`, `laboratory/`, `planning/`
- New or updated `_quarto-*.yml` config files
- Scripts in `scripts/`
- Commits on `restructure/pathways-v1`

### Require user confirmation
- Renaming or deleting existing `.qmd` files
- Changes to `_quarto.yml`
- Changes to `.github/workflows/`
- Anything touching `main` branch
