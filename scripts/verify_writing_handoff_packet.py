#!/usr/bin/env python3
"""Verify the research-to-writing handoff packet.

This is a deterministic first-pass checker. It reports one of three statuses:
READY, READY_WITH_WAIVERS, or BLOCKED.

It checks required files, mapped legacy/equivalent artifacts, basic gate_status.yaml
scalars, human-audit packet availability, and active waiver/limitation signals. It
uses only Python stdlib so it can run in bare project environments.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CORE_REQUIRED = [
    "project_state.md",
    "source_context.md",
    "decision_log.md",
    "next_actions.md",
    "qa/gate_status.yaml",
    "qa/integrity_gate.md",
    "paper/section_paragraph_map.md",
]

SPEC_REQUIRED = [
    "specs/main_spec.md",
    "specs/data_spec.md",
    "specs/preprocessing_spec.md",
    "specs/methodology_spec.md",
    "specs/output_spec.md",
    "specs/spec_change_log.md",
]

CLAIM_REQUIRED = [
    "qa/claim_verification_matrix.md",
]

MAPPABLE = {
    "qa/source_verification.md": "source_verification",
    "ideas/literature_map.md": "literature_map",
    "qa/literature_map.md": "literature_map",
    "exhibit_decision_ledger.md": "exhibit_decision_ledger",
    "audit_issue_ledger.md": "audit_issue_ledger",
    "sample_support.md": "sample_support",
    "dropped_findings.md": "dropped_findings",
    "data_context.md": "data_context",
    "qa/claim_verification_matrix.md": "claim_verification_matrix",
    "qa/waiver_log.md": "waiver_log",
    "qa/invalidation_ledger.md": "invalidation_ledger",
    "qa/audit_ownership_matrix.md": "audit_ownership_matrix",
}

BLOCKING_VALUES = {
    "BLOCKED",
    "REVISE",
    "REOPEN_ANALYSIS",
    "REOPEN_TEXT",
    "NOT_RUN",
    "missing",
}

LIMITATION_VALUES = {
    "PASS_WITH_LIMITATIONS",
    "READY_WITH_WAIVERS",
    "mapped",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def simple_yaml_scalars(text: str) -> dict[str, str]:
    """Extract simple key: value pairs with section-qualified keys."""
    out: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if ":" not in line or line.startswith("-"):
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if val == "":
            stack.append((indent, key))
            continue
        out[".".join([x[1] for x in stack] + [key])] = val
    return out


def mapped_names(root: Path) -> set[str]:
    path = root / "qa/artifact_mapping.md"
    if not path.exists():
        return set()
    text = read_text(path)
    names = set(re.findall(r"(?im)^\s*canonical_name\s*[:|]\s*`?([A-Za-z0-9_.\-/]+)`?", text))
    names.update(re.findall(r"`([A-Za-z0-9_.\-/]+\.md)`", text))
    names.update(re.findall(r"(?im)^\s*\|\s*([A-Za-z0-9_.\-/]+)\s*\|", text))
    return names


def exists_or_mapped(root: Path, rel: str, mappings: set[str]) -> bool:
    if (root / rel).exists():
        return True
    key = MAPPABLE.get(rel, rel)
    candidates = {rel, key, Path(rel).name, rel.replace("/", ".")}
    return bool(candidates & mappings)


def packet_markers_present(path: Path) -> bool:
    if not path.exists():
        return False
    text = read_text(path)
    markers = [
        "## 1. Plain-language question",
        "## 2. Why this is being asked now",
        "## 4. Options",
        "## 5. Agent recommendation",
        "## 6. Exact approval phrase",
    ]
    return all(marker in text for marker in markers)


def active_waiver(root: Path) -> bool:
    path = root / "qa/waiver_log.md"
    if not path.exists():
        return False
    text = read_text(path)
    return bool(re.search(r"(?i)\bACTIVE\b|\bAPPROVED_WITH_LIMITATIONS\b|what_cannot_be_claimed", text))


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify research-to-writing handoff packet readiness.")
    ap.add_argument("project_root", help="Path to project repository/root")
    ap.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = ap.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    blockers: list[str] = []
    warnings: list[str] = []
    waiver_signals: list[str] = []

    if not root.exists():
        result = {"project_root": str(root), "status": "BLOCKED", "blockers": ["project root does not exist"], "warnings": [], "waiver_signals": []}
        print(json.dumps(result, indent=2) if args.json else f"STATUS: BLOCKED\n- project root does not exist: {root}")
        return 2

    mappings = mapped_names(root)

    for rel in CORE_REQUIRED + SPEC_REQUIRED + CLAIM_REQUIRED:
        if not exists_or_mapped(root, rel, mappings):
            blockers.append(f"missing required handoff artifact: {rel}")

    gate_path = root / "qa/gate_status.yaml"
    scalars: dict[str, str] = {}
    if gate_path.exists():
        scalars = simple_yaml_scalars(read_text(gate_path))
        if scalars.get("writing_handoff.allowed") != "true":
            blockers.append("gate_status writing_handoff.allowed is not true")
        if scalars.get("writing_handoff.evidence_packet_complete") != "true":
            blockers.append("gate_status writing_handoff.evidence_packet_complete is not true")
        if scalars.get("writing_handoff.section_paragraph_map_complete") != "true":
            blockers.append("gate_status writing_handoff.section_paragraph_map_complete is not true")
        if scalars.get("writing_handoff.publishable_exhibits_human_checked") != "true":
            blockers.append("gate_status writing_handoff.publishable_exhibits_human_checked is not true")
        if scalars.get("blocked.status") == "true":
            blockers.append("gate_status blocked.status is true")
        if scalars.get("human_audit_required") == "true" or scalars.get("human_audit.required") == "true":
            if not packet_markers_present(root / "qa/human_audit_request.md"):
                blockers.append("human audit required but qa/human_audit_request.md is missing or incomplete")
        for key, val in scalars.items():
            if val in BLOCKING_VALUES:
                blockers.append(f"blocking gate_status value: {key}: {val}")
            if val in LIMITATION_VALUES:
                waiver_signals.append(f"limitation gate_status value: {key}: {val}")
        if scalars.get("writing_handoff.limitations") not in {None, "[]", ""}:
            waiver_signals.append("writing_handoff limitations are present")
    else:
        blockers.append("missing qa/gate_status.yaml")

    if active_waiver(root):
        waiver_signals.append("active waiver_log signal")

    invalid = root / "qa/invalidation_ledger.md"
    if invalid.exists() and re.search(r"(?i)\bOPEN\b", read_text(invalid)):
        blockers.append("invalidation ledger contains OPEN items")

    if blockers:
        status = "BLOCKED"
        code = 1
    elif waiver_signals:
        status = "READY_WITH_WAIVERS"
        code = 0
    else:
        status = "READY"
        code = 0

    result = {
        "project_root": str(root),
        "status": status,
        "blockers": blockers,
        "warnings": warnings,
        "waiver_signals": sorted(set(waiver_signals)),
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Project root: {root}")
        print(f"STATUS: {status}")
        if blockers:
            print("\nBlocking problems:")
            for item in blockers:
                print(f"- {item}")
        if waiver_signals:
            print("\nWaiver or limitation signals:")
            for item in sorted(set(waiver_signals)):
                print(f"- {item}")
        if warnings:
            print("\nWarnings:")
            for item in warnings:
                print(f"- {item}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
