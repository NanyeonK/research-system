#!/usr/bin/env python3
"""First-pass number verifier for research manuscripts.

This is a local clean-room utility inspired by the paper_factory workflow pattern.
It scans manuscript prose for reported numbers and checks whether comparable
numbers appear in project tables/logs/output files. It is not a substitute for
manual audit.
"""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

NUMBER_RE = re.compile(r"(?<![A-Za-z0-9_])-?\d[\d,]*(?:\.\d+)?%?")
COMMAND_RE = re.compile(
    r"\\(?:label|ref|autoref|eqref|input|includegraphics|cite[tp]?|citealp|url|href|bibliographystyle|bibliography)\{[^}]*\}"
)
ENV_RE = re.compile(r"\\(?:begin|end)\{[^}]*\}")
TABULAR_RE = re.compile(r"\\begin\{tabular\}.*?\\end\{tabular\}", re.DOTALL)

DEFAULT_EXTS = {
    ".tex", ".txt", ".md", ".log", ".out", ".csv", ".tsv", ".json", ".yaml", ".yml"
}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def parse_number(raw: str) -> tuple[float, bool] | None:
    clean = raw.replace(",", "")
    is_percent = clean.endswith("%")
    clean = clean.rstrip("%")
    try:
        value = float(clean)
    except ValueError:
        return None
    if value == 0 or not math.isfinite(value):
        return None
    return value, is_percent


def strip_latex_noise(text: str) -> str:
    doc_start = text.find(r"\begin{document}")
    if doc_start >= 0:
        text = text[doc_start:]
    text = TABULAR_RE.sub(" ", text)
    text = COMMAND_RE.sub(" ", text)
    text = ENV_RE.sub(" ", text)
    return text


def extract_numbers_from_text(text: str, *, prose: bool) -> list[dict]:
    if prose:
        text = strip_latex_noise(text)
    rows = []
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("%"):
            continue
        if prose and stripped.startswith("\\"):
            continue
        for match in NUMBER_RE.finditer(line):
            raw = match.group(0)
            parsed = parse_number(raw)
            if parsed is None:
                continue
            value, is_percent = parsed
            # Skip years and small enumerators in prose. Keep all reference numbers.
            if prose:
                if re.fullmatch(r"(?:19|20)\d{2}", raw):
                    continue
                if value.is_integer() and 1 <= abs(value) <= 20 and "." not in raw and "," not in raw and not is_percent:
                    continue
            context_start = max(0, match.start() - 60)
            context_end = min(len(line), match.end() + 60)
            rows.append(
                {
                    "raw": raw,
                    "value": value,
                    "is_percent": is_percent,
                    "line": lineno,
                    "context": line[context_start:context_end].strip(),
                }
            )
    return rows


def iter_reference_files(roots: list[Path], exts: set[str]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
            continue
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.suffix.lower() in exts:
                files.append(path)
    return files


def comparable(value: float, refs: set[float], tolerance: float) -> bool:
    candidates = [value]
    candidates.extend([value / 100.0, value * 100.0, value / 1000.0, value * 1000.0])
    for candidate in candidates:
        for ref in refs:
            if ref == candidate:
                return True
            scale = max(abs(ref), 1.0)
            if abs(candidate - ref) / scale <= tolerance:
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify manuscript prose numbers against project outputs.")
    parser.add_argument("paper", type=Path, help="Manuscript .tex/.md/.txt file")
    parser.add_argument("--roots", nargs="+", type=Path, default=None, help="Reference roots/files to scan. Default: paper parent")
    parser.add_argument("--ext", action="append", default=[], help="Extra extension to scan, e.g. --ext .rout")
    parser.add_argument("--tolerance", type=float, default=0.02, help="Relative tolerance for matches. Default 0.02")
    parser.add_argument("--out", type=Path, default=None, help="Optional markdown report path")
    args = parser.parse_args()

    paper = args.paper.expanduser().resolve()
    if not paper.exists():
        raise SystemExit(f"paper not found: {paper}")

    roots = [p.expanduser().resolve() for p in (args.roots or [paper.parent])]
    exts = set(DEFAULT_EXTS) | {e if e.startswith(".") else f".{e}" for e in args.ext}

    paper_text = paper.read_text(errors="ignore")
    prose_numbers = extract_numbers_from_text(paper_text, prose=True)

    ref_files = [p for p in iter_reference_files(roots, exts) if p.resolve() != paper]
    ref_values: set[float] = set()
    for ref_file in ref_files:
        try:
            text = ref_file.read_text(errors="ignore")
        except Exception:
            continue
        for row in extract_numbers_from_text(text, prose=False):
            ref_values.add(row["value"])

    matched = []
    unmatched = []
    for row in prose_numbers:
        (matched if comparable(row["value"], ref_values, args.tolerance) else unmatched).append(row)

    lines = []
    lines.append("# Number Verification Report")
    lines.append("")
    lines.append(f"Paper: `{paper}`")
    lines.append(f"Reference roots: {', '.join(f'`{r}`' for r in roots)}")
    lines.append(f"Reference files scanned: {len(ref_files)}")
    lines.append(f"Reference numbers found: {len(ref_values)}")
    lines.append(f"Paper prose numbers found: {len(prose_numbers)}")
    lines.append(f"Matched: {len(matched)}")
    lines.append(f"Unmatched: {len(unmatched)}")
    lines.append("")
    lines.append("This is a first-pass screen. Every unmatched coefficient, p-value, effect size, sample count, and percentage needs manual source verification. False positives are expected.")
    lines.append("")
    if unmatched:
        lines.append("## Unmatched numbers")
        lines.append("")
        lines.append("| Number | Line | Context |")
        lines.append("|---:|---:|---|")
        for row in unmatched:
            ctx = row["context"].replace("|", "\\|")
            lines.append(f"| {row['raw']} | {row['line']} | {ctx} |")
        lines.append("")
    if matched:
        lines.append("## Matched numbers")
        lines.append("")
        lines.append("| Number | Line | Context |")
        lines.append("|---:|---:|---|")
        for row in matched[:200]:
            ctx = row["context"].replace("|", "\\|")
            lines.append(f"| {row['raw']} | {row['line']} | {ctx} |")
        if len(matched) > 200:
            lines.append(f"\nMatched list truncated to 200 rows out of {len(matched)}.")

    report = "\n".join(lines) + "\n"
    if args.out:
        args.out.expanduser().write_text(report)
    print(report)
    return 1 if unmatched else 0


if __name__ == "__main__":
    raise SystemExit(main())
