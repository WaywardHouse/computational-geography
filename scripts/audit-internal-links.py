#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_BOOK_DIRS = ["_book-core", "_book-topics", "_book-lab", "_book"]
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}
IGNORED_EXTENSIONS = {
    ".css",
    ".js",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".pdf",
    ".xml",
    ".ico",
    ".zip",
    ".csv",
    ".txt",
}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                self.hrefs.append(value)


def parse_volume_chapters(config_path: Path) -> set[Path]:
    chapter_paths: set[Path] = set()
    lines = config_path.read_text(encoding="utf-8").splitlines()
    in_chapters = False
    for line in lines:
        stripped = line.strip()
        if stripped == "chapters:":
            in_chapters = True
            continue
        if in_chapters:
            if not stripped:
                continue
            if re.match(r"^[A-Za-z]", line):
                break
            match = re.match(r"^\s*-\s+(.+\.qmd)\s*$", line)
            if match:
                chapter_paths.add(Path(match.group(1)))
    return chapter_paths


def source_href_candidates(text: str) -> list[str]:
    matches = re.findall(r'href="([^"]+)"', text)
    matches.extend(re.findall(r"\[[^\]]+\]\(([^)]+)\)", text))
    return matches


def discover_book_dirs(root: Path, explicit: list[str] | None) -> list[Path]:
    if explicit:
        return [root / entry for entry in explicit if (root / entry).exists()]

    found = [root / entry for entry in DEFAULT_BOOK_DIRS if (root / entry).exists()]
    split = [path for path in found if path.name in {"_book-core", "_book-topics", "_book-lab"}]
    return split or found


def normalize_target(book_dir: Path, page_path: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme in IGNORED_SCHEMES:
        return None
    if href.startswith("#"):
        return None

    raw_path = parsed.path
    if not raw_path:
        return None

    target = (book_dir / raw_path.lstrip("/")) if raw_path.startswith("/") else (page_path.parent / raw_path)
    target = target.resolve()

    try:
        target.relative_to(book_dir.resolve())
    except ValueError:
        return target

    return target


def target_exists(target: Path) -> bool:
    if target.exists():
        return True
    if target.suffix == "":
        return (target / "index.html").exists()
    if target.suffix == ".html" and target.stem == "index":
        return target.exists()
    return False


def audit_book_dir(book_dir: Path) -> dict[str, list[str]]:
    missing: dict[str, list[str]] = defaultdict(list)
    for page_path in sorted(book_dir.rglob("*.html")):
        parser = LinkParser()
        parser.feed(page_path.read_text(encoding="utf-8", errors="ignore"))
        for href in parser.hrefs:
            target = normalize_target(book_dir, page_path, href)
            if target is None:
                continue
            if target.suffix.lower() in IGNORED_EXTENSIONS:
                continue
            if not target_exists(target):
                rel_page = page_path.relative_to(book_dir)
                missing[str(rel_page)].append(href)
    return missing


def audit_source_volume(root: Path, config_name: str) -> dict[str, list[str]]:
    config_path = root / config_name
    chapter_paths = parse_volume_chapters(config_path)
    missing: dict[str, list[str]] = defaultdict(list)

    for chapter in sorted(chapter_paths):
        source_path = root / chapter
        if not source_path.exists():
            continue
        for href in source_href_candidates(source_path.read_text(encoding="utf-8", errors="ignore")):
            parsed = urlparse(href)
            if parsed.scheme in IGNORED_SCHEMES or href.startswith("#"):
                continue
            if not parsed.path.endswith(".html"):
                continue
            target_qmd = (chapter.parent / parsed.path).resolve().relative_to(root.resolve())
            target_qmd = target_qmd.with_suffix(".qmd")
            if target_qmd not in chapter_paths:
                missing[str(chapter)].append(parsed.path)
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit rendered or source internal links for missing targets.")
    parser.add_argument("book_dirs", nargs="*", help="Rendered output directories to inspect.")
    parser.add_argument("--source-volumes", action="store_true", help="Audit source links against split-book chapter manifests.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    if args.source_volumes:
        configs = ["_quarto-core-book.yml", "_quarto-topic-libraries.yml", "_quarto-laboratory.yml"]
        any_missing = False
        for config_name in configs:
            missing = audit_source_volume(root, config_name)
            label = config_name.replace("_quarto-", "").replace(".yml", "")
            if not missing:
                print(f"{label}: OK")
                continue
            any_missing = True
            total = sum(len(hrefs) for hrefs in missing.values())
            print(f"{label}: {total} broken source link(s)")
            for page, hrefs in sorted(missing.items()):
                for href in hrefs:
                    print(f"  {page} -> {href}")
        return 1 if any_missing else 0

    book_dirs = discover_book_dirs(root, args.book_dirs or None)
    if not book_dirs:
        print("No rendered book directories found.", file=sys.stderr)
        return 1

    any_missing = False
    for book_dir in book_dirs:
        missing = audit_book_dir(book_dir)
        if not missing:
            print(f"{book_dir.name}: OK")
            continue

        any_missing = True
        total = sum(len(hrefs) for hrefs in missing.values())
        print(f"{book_dir.name}: {total} broken internal link(s)")
        for page, hrefs in sorted(missing.items()):
            for href in hrefs:
                print(f"  {page} -> {href}")

    return 1 if any_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
