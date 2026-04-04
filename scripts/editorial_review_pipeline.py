#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PIPELINE_ROOT = Path("planning/editorial-pipeline")


VOLUMES: dict[str, dict[str, Any]] = {
    "core-book": {
        "config": "_quarto-core-book.yml",
        "title": "Computational Geography: Core Book",
        "audience": "First-time readers on the flagship modelling path.",
        "complexity_position": "Entry point. Grade 10 language with gentle progression toward early undergraduate technical writing.",
        "pedagogy": [
            "Lead with intuition before formalism.",
            "Define notation on first use.",
            "Avoid abrupt abstraction and long theorem-like stretches.",
            "Keep transitions explicit when moving from story to model to equation.",
        ],
        "design": [
            "Every major concept should have an explainer, diagram, worked example, or visualization where it clarifies reasoning.",
            "Use visual aids to reduce abstraction, not decorate the page.",
        ],
    },
    "topic-libraries": {
        "config": "_quarto-topic-libraries.yml",
        "title": "Computational Geography: Topic Libraries",
        "audience": "Second-pass readers moving into specialist companion material.",
        "complexity_position": "Intermediate branch work. Keep Grade 10 readability, but allow denser technical vocabulary with stronger explanatory framing.",
        "pedagogy": [
            "Retain intuition-first framing even when topics are specialist.",
            "Keep prerequisites visible and restate core ideas before extending them.",
            "Use formalism carefully and unpack every new symbol family.",
        ],
        "design": [
            "Specialist chapters should still surface diagrams, comparison tables, and annotated workflows.",
            "Visualizations should expose mechanism, not only results.",
        ],
    },
    "laboratory": {
        "config": "_quarto-laboratory.yml",
        "title": "Computational Geography Laboratory",
        "audience": "Advanced readers working through investigations and practicum-style models.",
        "complexity_position": "Most advanced volume. Language remains readable, but mathematical density can rise when the scaffolding remains generous.",
        "pedagogy": [
            "Preserve explanatory framing even in advanced derivations.",
            "State assumptions, notation, and goal conditions before long technical sections.",
            "Use worked steps and interpretation paragraphs to keep the mathematics learnable.",
        ],
        "design": [
            "Investigations should maximize model diagrams, workflow schematics, and parameter explainers.",
            "Interactive visualizations should expose assumptions, sensitivities, and failure modes.",
        ],
    },
}


CHAPTER_QA_CHECKS = {
    "notation_first_use": "Explain notation on first use.",
    "intuition_before_formalism": "Introduce concepts with intuition before formalism whenever possible.",
    "mathematical_correctness": "Preserve mathematical correctness.",
    "conceptual_pacing": "Improve transitions and conceptual pacing.",
    "abstraction_control": "Avoid abrupt abstraction in early volumes and retain explanatory framing in later volumes.",
    "beginner_accessibility": "Remain readable for first-time learners even when the mathematics becomes difficult.",
}


DESIGN_CHECKS = {
    "visualization_leverage": "Visualizations materially improve understanding of the model.",
    "explainer_leverage": "Explainers, diagrams, or worked examples are used where they reduce cognitive load.",
    "interpretive_support": "The reader is told how to read the figure, table, or model output.",
}


VOLUME_CONSISTENCY_CHECKS = {
    "language_band_consistency": "Language complexity fits the volume calibration profile.",
    "pedagogical_consistency": "The chapters teach at a coherent pace and with shared explanatory habits.",
    "notation_consistency": "Notation and naming conventions are coherent across the volume.",
    "design_consistency": "Visualizations and explainers are used consistently across the volume.",
}


SERIES_CONSISTENCY_CHECKS = {
    "progression_coherence": "The series progresses coherently from flagship to specialist to laboratory work.",
    "language_progression": "Language and abstraction rise at a controlled pace across the series.",
    "reader_fairness": "Prerequisites and expectations are fair at every step.",
    "design_progression": "Visualization and explainer strategy matures without abandoning accessibility.",
}


@dataclass
class Chapter:
    volume_id: str
    path: str
    title: str
    subtitle: str
    part_title: str
    difficulty: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(read_text(path))


def merge_defaults(existing: Any, default: Any) -> Any:
    if isinstance(default, dict):
        existing_dict = existing if isinstance(existing, dict) else {}
        merged: dict[str, Any] = {}
        for key, value in default.items():
            merged[key] = merge_defaults(existing_dict.get(key), value)
        for key, value in existing_dict.items():
            if key not in merged:
                merged[key] = value
        return merged
    if isinstance(default, list):
        if isinstance(existing, list) and existing:
            return existing
        return default
    return existing if existing not in (None, "") else default


def parse_chapter_paths(config_path: Path) -> list[str]:
    lines = read_text(config_path).splitlines()
    in_chapters = False
    chapter_paths: list[str] = []

    for raw_line in lines:
        line = raw_line.rstrip()
        if not in_chapters:
            if line.strip() == "chapters:":
                in_chapters = True
            continue
        if not raw_line.startswith("    - "):
            break
        item = raw_line.strip()[2:].strip()
        if not item.endswith(".qmd"):
            continue
        if item == "index.qmd" or item.endswith("/index.qmd"):
            continue
        chapter_paths.append(item)
    return chapter_paths


def parse_frontmatter(source_path: Path) -> dict[str, str]:
    text = read_text(source_path)
    if not text.startswith("---\n"):
        return {}

    fields: dict[str, str] = {}
    lines = text.splitlines()
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        value = value.strip().strip("'").strip('"')
        fields[key] = value
    return fields


def build_chapters(repo_root: Path) -> list[Chapter]:
    chapters: list[Chapter] = []
    for volume_id, volume in VOLUMES.items():
        config_path = repo_root / volume["config"]
        for rel_path in parse_chapter_paths(config_path):
            source_path = repo_root / rel_path
            frontmatter = parse_frontmatter(source_path)
            chapters.append(
                Chapter(
                    volume_id=volume_id,
                    path=rel_path,
                    title=frontmatter.get("title", source_path.stem.replace("-", " ").title()),
                    subtitle=frontmatter.get("subtitle", ""),
                    part_title=frontmatter.get("book-part-title", ""),
                    difficulty=frontmatter.get("difficulty", ""),
                )
            )
    return chapters


def chapter_review_template(chapter: Chapter) -> dict[str, Any]:
    qa_checks = {key: "pending" for key in CHAPTER_QA_CHECKS}
    design_checks = {key: "pending" for key in DESIGN_CHECKS}
    return {
        "stage": "chapter_review",
        "metadata": {
            "volume_id": chapter.volume_id,
            "chapter_path": chapter.path,
            "chapter_title": chapter.title,
            "chapter_subtitle": chapter.subtitle,
            "part_title": chapter.part_title,
            "difficulty": chapter.difficulty,
        },
        "inventory": {
            "status": "pending",
            "summary": "",
            "issues": [],
            "blocking_risks": [],
        },
        "rewrite": {
            "status": "pending",
            "summary": "",
            "full_text_rewritten": False,
            "editor_notes": [],
        },
        "qa_review": {
            "status": "pending",
            "outcome": "pending",
            "summary": "",
            "checks": qa_checks,
            "blocking_issues": [],
            "recommended_repairs": [],
        },
        "repair": {
            "status": "pending",
            "summary": "",
            "actions_taken": [],
        },
        "design_review": {
            "status": "pending",
            "outcome": "pending",
            "summary": "",
            "checks": design_checks,
            "improvements_made": [],
        },
        "completion": {
            "chapter_complete": False,
            "ready_for_volume_review": False,
        },
    }


def calibration_template(volume_id: str, volume: dict[str, Any], chapter_count: int) -> dict[str, Any]:
    return {
        "stage": "calibration_profile",
        "volume_id": volume_id,
        "volume_title": volume["title"],
        "chapter_count": chapter_count,
        "reader_profile": volume["audience"],
        "language_target": "Approximate Grade 10 readability across the series, with controlled increases in technical density where the series progression supports it.",
        "complexity_position": volume["complexity_position"],
        "pedagogy_priorities": volume["pedagogy"],
        "required_rules": [
            "Explain notation on first use.",
            "Introduce concepts with intuition before formalism whenever possible.",
            "Preserve mathematical correctness.",
            "Improve transitions and conceptual pacing.",
            "Avoid abrupt abstraction in early volumes.",
            "Retain explanatory framing in later volumes.",
            "Do not skip QA.",
        ],
        "design_expectations": volume["design"],
        "status": "active",
    }


def volume_review_template(volume_id: str, volume: dict[str, Any], chapters: list[Chapter]) -> dict[str, Any]:
    return {
        "stage": "volume_consistency_review",
        "metadata": {
            "volume_id": volume_id,
            "volume_title": volume["title"],
            "chapter_count": len(chapters),
        },
        "consistency_review": {
            "status": "pending",
            "outcome": "pending",
            "summary": "",
            "checks": {key: "pending" for key in VOLUME_CONSISTENCY_CHECKS},
            "blocking_issues": [],
            "repair_actions": [],
        },
        "completion": {
            "volume_complete": False,
        },
    }


def series_review_template(chapters: list[Chapter]) -> dict[str, Any]:
    return {
        "stage": "series_progression_review",
        "metadata": {
            "series_title": "Computational Geography",
            "volume_count": len(VOLUMES),
            "chapter_count": len(chapters),
        },
        "progression_review": {
            "status": "pending",
            "outcome": "pending",
            "summary": "",
            "checks": {key: "pending" for key in SERIES_CONSISTENCY_CHECKS},
            "blocking_issues": [],
            "repair_actions": [],
        },
        "completion": {
            "series_complete": False,
        },
    }


def manifest_template(chapters: list[Chapter]) -> dict[str, Any]:
    by_volume: dict[str, list[dict[str, Any]]] = {}
    for chapter in chapters:
        by_volume.setdefault(chapter.volume_id, []).append(
            {
                "chapter_path": chapter.path,
                "title": chapter.title,
                "part_title": chapter.part_title,
                "difficulty": chapter.difficulty,
            }
        )

    return {
        "series_title": "Computational Geography",
        "volumes": {
            volume_id: {
                "title": VOLUMES[volume_id]["title"],
                "config": VOLUMES[volume_id]["config"],
                "chapter_count": len(items),
                "chapters": items,
            }
            for volume_id, items in by_volume.items()
        },
    }


def chapter_review_path(repo_root: Path, chapter: Chapter) -> Path:
    return repo_root / PIPELINE_ROOT / "chapters" / chapter.volume_id / chapter.path.replace(".qmd", ".json")


def bootstrap(repo_root: Path) -> int:
    chapters = build_chapters(repo_root)
    manifest_path = repo_root / PIPELINE_ROOT / "manifest.json"
    write_json(manifest_path, manifest_template(chapters))

    for volume_id, volume in VOLUMES.items():
        volume_chapters = [chapter for chapter in chapters if chapter.volume_id == volume_id]
        calibration_path = repo_root / PIPELINE_ROOT / "volumes" / volume_id / "calibration-profile.json"
        existing_calibration = load_json(calibration_path)
        calibration = merge_defaults(existing_calibration, calibration_template(volume_id, volume, len(volume_chapters)))
        write_json(calibration_path, calibration)

        volume_review_path = repo_root / PIPELINE_ROOT / "volumes" / volume_id / "volume-consistency-review.json"
        existing_volume_review = load_json(volume_review_path)
        volume_review = merge_defaults(existing_volume_review, volume_review_template(volume_id, volume, volume_chapters))
        write_json(volume_review_path, volume_review)

    series_review_path = repo_root / PIPELINE_ROOT / "series" / "series-progression-review.json"
    existing_series_review = load_json(series_review_path)
    series_review = merge_defaults(existing_series_review, series_review_template(chapters))
    write_json(series_review_path, series_review)

    for chapter in chapters:
        review_path = chapter_review_path(repo_root, chapter)
        existing = load_json(review_path)
        merged = merge_defaults(existing, chapter_review_template(chapter))
        write_json(review_path, merged)

    print(f"Bootstrapped editorial pipeline for {len(chapters)} chapters across {len(VOLUMES)} volumes.")
    print(f"Pipeline root: {repo_root / PIPELINE_ROOT}")
    return 0


def chapter_passes(review: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    metadata = review.get("metadata", {})
    chapter_name = metadata.get("chapter_path", "<unknown>")

    if review.get("inventory", {}).get("status") != "completed":
        errors.append(f"{chapter_name}: inventory.status must be 'completed'")
    if review.get("rewrite", {}).get("status") != "completed":
        errors.append(f"{chapter_name}: rewrite.status must be 'completed'")
    if review.get("rewrite", {}).get("full_text_rewritten") is not True:
        errors.append(f"{chapter_name}: rewrite.full_text_rewritten must be true")
    if review.get("qa_review", {}).get("outcome") != "pass":
        errors.append(f"{chapter_name}: qa_review.outcome must be 'pass'")
    if review.get("design_review", {}).get("outcome") != "pass":
        errors.append(f"{chapter_name}: design_review.outcome must be 'pass'")
    if review.get("completion", {}).get("chapter_complete") is not True:
        errors.append(f"{chapter_name}: completion.chapter_complete must be true")

    return (not errors, errors)


def validate_status(repo_root: Path, as_json: bool) -> int:
    manifest = load_json(repo_root / PIPELINE_ROOT / "manifest.json")
    if not manifest:
        message = "Pipeline manifest not found. Run bootstrap first."
        if as_json:
            print(json.dumps({"ok": False, "errors": [message]}, indent=2))
        else:
            print(message)
        return 1

    errors: list[str] = []
    summary: dict[str, Any] = {"volumes": {}, "series": {"ok": False}}

    for volume_id in manifest["volumes"]:
        volume_meta = manifest["volumes"][volume_id]
        volume_ok = True
        volume_errors: list[str] = []
        passed_chapters = 0

        for chapter_meta in volume_meta["chapters"]:
            review_path = repo_root / PIPELINE_ROOT / "chapters" / volume_id / chapter_meta["chapter_path"].replace(".qmd", ".json")
            review = load_json(review_path)
            ok, chapter_errors = chapter_passes(review)
            if not ok:
                volume_ok = False
                volume_errors.extend(chapter_errors)
            else:
                passed_chapters += 1

        volume_review_path = repo_root / PIPELINE_ROOT / "volumes" / volume_id / "volume-consistency-review.json"
        volume_review = load_json(volume_review_path)
        if volume_review.get("consistency_review", {}).get("outcome") != "pass":
            volume_ok = False
            volume_errors.append(f"{volume_id}: consistency_review.outcome must be 'pass'")
        if volume_review.get("completion", {}).get("volume_complete") is not True:
            volume_ok = False
            volume_errors.append(f"{volume_id}: completion.volume_complete must be true")

        summary["volumes"][volume_id] = {
            "ok": volume_ok,
            "chapter_count": volume_meta["chapter_count"],
            "chapters_passed": passed_chapters,
            "errors": volume_errors,
        }
        errors.extend(volume_errors)

    series_review = load_json(repo_root / PIPELINE_ROOT / "series" / "series-progression-review.json")
    series_ok = True
    if any(not volume_summary["ok"] for volume_summary in summary["volumes"].values()):
        series_ok = False
        errors.append("series: all volumes must pass before the series can pass")
    if series_review.get("progression_review", {}).get("outcome") != "pass":
        series_ok = False
        errors.append("series: progression_review.outcome must be 'pass'")
    if series_review.get("completion", {}).get("series_complete") is not True:
        series_ok = False
        errors.append("series: completion.series_complete must be true")

    summary["series"] = {"ok": series_ok}
    summary["ok"] = not errors
    summary["errors"] = errors

    if as_json:
        print(json.dumps(summary, indent=2))
    else:
        if summary["ok"]:
            print("Editorial pipeline status: PASS")
        else:
            print("Editorial pipeline status: FAIL")
            for volume_id, volume_summary in summary["volumes"].items():
                print(
                    f"- {volume_id}: {volume_summary['chapters_passed']}/{volume_summary['chapter_count']} chapters passed; "
                    f"volume gate {'PASS' if volume_summary['ok'] else 'PENDING'}"
                )
            print(f"- series gate {'PASS' if summary['series']['ok'] else 'PENDING'}")
            sample = errors[:12]
            if sample:
                print("- sample blockers:")
                for error in sample:
                    print(f"  - {error}")
            if len(errors) > len(sample):
                remaining = len(errors) - len(sample)
                print(f"- {remaining} additional blockers omitted; run with --json for the full list")
    return 0 if summary["ok"] else 1


def parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(description="Manage editorial QA and review manifests for the Computational Geography series.")
    cli.add_argument("command", choices=["bootstrap", "status"], help="Pipeline command to run")
    cli.add_argument("--root", default=".", help="Repository root")
    cli.add_argument("--json", action="store_true", help="Emit machine-readable status output")
    return cli


def main() -> int:
    args = parser().parse_args()
    repo_root = Path(args.root).resolve()

    if args.command == "bootstrap":
        return bootstrap(repo_root)
    if args.command == "status":
        return validate_status(repo_root, args.json)
    return 1


if __name__ == "__main__":
    sys.exit(main())
