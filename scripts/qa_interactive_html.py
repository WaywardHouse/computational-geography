#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


INTERACTIVE_PATTERNS = (
    re.compile(r'<label\b', re.I),
    re.compile(r'<input\b', re.I),
    re.compile(r'<select\b', re.I),
    re.compile(r'<canvas\b', re.I),
    re.compile(r'<script\b', re.I),
    re.compile(r'class="viz-container"', re.I),
    re.compile(r'class="pyodide-cell"', re.I),
    re.compile(r'class="controls"', re.I),
    re.compile(r'class="button-group"', re.I),
    re.compile(r'class="info-panel"', re.I),
    re.compile(r'class="[^"]*-info"', re.I),
)

INTERACTIVE_TAGS = ("label", "input", "select", "canvas", "script")
OUTPUT_DIRS = ("_book", "_book-core", "_book-topics", "_book-lab")
SOURCE_EXCLUDES = set(OUTPUT_DIRS) | {".git", ".quarto", "node_modules"}


@dataclass
class Issue:
    kind: str
    path: str
    detail: str
    line: int | None = None
    output_path: str | None = None


def is_interactive(text: str) -> bool:
    return any(pattern.search(text) for pattern in INTERACTIVE_PATTERNS)


def split_fences(text: str) -> list[tuple[str, str]]:
    parts: list[tuple[str, str]] = []
    lines = text.splitlines(keepends=True)
    in_fence = False
    fence_info = ""
    fence_marker = ""
    buf: list[str] = []

    for line in lines:
        match = re.match(r"^(~~~+|```+)(.*)$", line.rstrip("\n"))
        if match:
            marker, info = match.groups()
            if in_fence and marker == fence_marker:
                buf.append(line)
                parts.append(("fence", "".join(buf)))
                buf = []
                in_fence = False
                fence_info = ""
                fence_marker = ""
                continue
            if not in_fence:
                if buf:
                    parts.append(("text", "".join(buf)))
                buf = [line]
                in_fence = True
                fence_info = info.strip()
                fence_marker = marker
                continue
        buf.append(line)

    if buf:
        parts.append(("fence" if in_fence else "text", "".join(buf)))
    return parts


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_source(path: Path) -> list[Issue]:
    text = path.read_text()
    issues: list[Issue] = []

    for kind, chunk in split_fences(text):
        if kind != "text":
            # Inspect raw html fences for over-indented tags that Pandoc can mis-handle.
            fence_header = chunk.splitlines()[0] if chunk else ""
            if "{=html}" in fence_header:
                for m in re.finditer(r"(?m)^(?P<indent>\s{2,})(?P<line><(?P<tag>label|input|select|canvas|script|div)\b.*)$", chunk):
                    if m.group("tag").lower() == "div" and not is_interactive(m.group("line")):
                        continue
                    issues.append(
                        Issue(
                            kind="indented-html-in-raw-fence",
                            path=str(path),
                            detail=f"Indented <{m.group('tag')}> inside raw HTML fence",
                            line=line_number(text, text.find(chunk) + m.start()),
                        )
                    )
            continue

        for m in re.finditer(r"(?m)^(?P<indent>\s*)<(?P<tag>label|input|select|canvas|script|div)\b.*$", chunk):
            line = m.group(0)
            if not is_interactive(line):
                continue
            issues.append(
                Issue(
                    kind="interactive-html-outside-raw-fence",
                    path=str(path),
                    detail=f"Interactive <{m.group('tag')}> outside ```{{=html}} fence",
                    line=line_number(text, text.find(chunk) + m.start()),
                )
            )

    return issues


def extract_ids(text: str) -> set[str]:
    return set(re.findall(r'\bid="([^"]+)"', text))


def candidate_outputs(root: Path, source: Path) -> Iterable[Path]:
    rel = source.relative_to(root).with_suffix(".html")
    for outdir in OUTPUT_DIRS:
        candidate = root / outdir / rel
        if candidate.exists():
            yield candidate


def scan_output(root: Path, source: Path) -> list[Issue]:
    source_text = source.read_text()
    source_ids = extract_ids(source_text)
    expects_interactive = is_interactive(source_text)
    if not expects_interactive:
        return []

    issues: list[Issue] = []
    for output in candidate_outputs(root, source):
        output_text = output.read_text()

        for tag in INTERACTIVE_TAGS:
            escaped = f"&lt;{tag}"
            if escaped in output_text:
                issues.append(
                    Issue(
                        kind="escaped-interactive-html-in-output",
                        path=str(source),
                        output_path=str(output),
                        detail=f"Escaped {escaped} found in rendered HTML",
                    )
                )

        for source_id in sorted(source_ids):
            if source_id not in output_text and html.escape(source_id) in output_text:
                issues.append(
                    Issue(
                        kind="id-present-only-in-escaped-output",
                        path=str(source),
                        output_path=str(output),
                        detail=f'id "{source_id}" appears only in escaped form',
                    )
                )

        live_hits = sum(output_text.count(f"<{tag}") for tag in ("label", "input", "select", "canvas"))
        if live_hits == 0 and any(tag in source_text for tag in ("<label", "<input", "<select", "<canvas")):
            issues.append(
                Issue(
                    kind="missing-live-controls-in-output",
                    path=str(source),
                    output_path=str(output),
                    detail="Rendered HTML has no live control tags",
                )
            )

    return issues


def iter_sources(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.qmd"):
        if any(part in SOURCE_EXCLUDES for part in path.parts):
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description="QA interactive raw HTML blocks in Quarto sources and outputs.")
    parser.add_argument("root", nargs="?", default=".", help="Repo root to scan")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    issues: list[Issue] = []

    for source in sorted(iter_sources(root)):
        issues.extend(scan_source(source))
        issues.extend(scan_output(root, source))

    if args.json:
        print(json.dumps([asdict(issue) for issue in issues], indent=2))
    else:
        if not issues:
            print("No interactive HTML issues found.")
            return 0
        for issue in issues:
            loc = f":{issue.line}" if issue.line else ""
            out = f" -> {issue.output_path}" if issue.output_path else ""
            print(f"[{issue.kind}] {issue.path}{loc}{out} :: {issue.detail}")

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
