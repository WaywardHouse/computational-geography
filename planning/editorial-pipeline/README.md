# Editorial Review Pipeline

This pipeline manages QA and editorial review for the `Computational Geography` series at three levels:

1. chapter review
2. volume consistency review
3. full-series progression review

It is designed around the current split-build structure:

- `core-book`
- `topic-libraries`
- `laboratory`

## Commands

Bootstrap or refresh the review scaffolding:

```bash
python3 scripts/editorial_review_pipeline.py bootstrap
```

Validate whether the chapter, volume, and series gates have all passed:

```bash
python3 scripts/editorial_review_pipeline.py status
```

Machine-readable status:

```bash
python3 scripts/editorial_review_pipeline.py status --json
```

## Files

- `planning/editorial-pipeline/manifest.json`
  The generated inventory of volumes and reviewed chapter files.
- `planning/editorial-pipeline/volumes/<volume>/calibration-profile.json`
  The calibration profile for that volume.
- `planning/editorial-pipeline/chapters/<volume>/<chapter>.json`
  The chapter review record.
- `planning/editorial-pipeline/volumes/<volume>/volume-consistency-review.json`
  The volume-level consistency gate.
- `planning/editorial-pipeline/series/series-progression-review.json`
  The series-level progression gate.

## Required Stage Outputs

### 1. Calibration Profile

File: `volumes/<volume>/calibration-profile.json`

This defines the volume's reader profile, language target, pacing expectations, rules, and design expectations.

### 2. Chapter Review

File: `chapters/<volume>/<chapter>.json`

Fill the fields in this order:

1. `inventory`
   Record issue inventory, risks, and blockers.
2. `rewrite`
   Confirm the full text was rewritten and summarize the editorial move.
3. `qa_review`
   Mark every QA rule, then set `outcome` to `pass` or `fail`.
4. `repair`
   Record the repair pass after QA identifies defects.
5. `design_review`
   Confirm that visualizations and explainers are doing real pedagogical work.

Set `completion.chapter_complete` to `true` only after:

- `inventory.status == "completed"`
- `rewrite.status == "completed"`
- `rewrite.full_text_rewritten == true`
- `qa_review.outcome == "pass"`
- `design_review.outcome == "pass"`

### 3. Volume Consistency Review

File: `volumes/<volume>/volume-consistency-review.json`

This review may pass only when every chapter in the volume has already passed chapter review.

Set `completion.volume_complete` to `true` only after `consistency_review.outcome == "pass"`.

### 4. Series Progression Review

File: `series/series-progression-review.json`

This review may pass only when every volume has already passed its volume review.

Set `completion.series_complete` to `true` only after `progression_review.outcome == "pass"`.

## Editorial Rules Enforced By The Pipeline

- Explain notation on first use.
- Introduce concepts with intuition before formalism whenever possible.
- Preserve mathematical correctness.
- Improve transitions and conceptual pacing.
- Avoid abrupt abstraction in early volumes.
- Retain explanatory framing in later volumes.
- Do not skip QA.
- Treat visualizations and explainers as teaching tools, not decoration.

## Completion Rules

- A model is not complete unless it passes QA.
- A volume is not complete unless it passes volume consistency review.
- The series is not complete unless progression across volumes is coherent.
