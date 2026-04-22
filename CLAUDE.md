# CLAUDE.md — Computational Geography Project

> Claude Code: read `AGENTS.md` first — it is the authoritative project spec.
> This file adds Claude-specific notes only.

---

## Quick orientation

See `AGENTS.md` for the full project context, structure, completed phases, and remaining work.

---

## Claude-specific reminders

### Tools to reach for
- Use **`Edit`** (not full `Write`) when modifying existing files — sends only the diff
- Use **`Bash`** for git operations and multi-file bulk updates via scripts
- Use **`Glob`** to find files by pattern; **`Grep`** to search chapter contents
- Use **`Read`** before any `Edit` — required by harness

### Commit hygiene
- Every completed phase gets its own commit: `"Phase N: short description"`
- Stage specific files (`git add path/to/file`) not `git add -A`
- Never push to `main` without explicit user instruction

### Bulk chapter updates
- Write idempotent Python scripts in `scripts/` (check "already has this field" before inserting)
- Run with `python3 scripts/<name>.py` from the repo root
- Commit the script itself along with the chapter changes

### Don't ask, just do
These actions are pre-approved for `restructure/pathways-v1`:
- Adding/updating frontmatter fields to existing `.qmd` files
- Creating new `.qmd` chapters in `scientific-computing/`, `laboratory/`, `planning/`
- Creating or updating `_quarto-*.yml` config files
- Creating scripts in `scripts/`
- Committing changes with meaningful messages

### Always ask before
- Renaming or deleting existing chapter files
- Changing `_quarto.yml` (default config)
- Modifying `.github/workflows/`
- Merging or rebasing onto `main`
