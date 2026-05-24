#!/usr/bin/env python3
"""First-pass verifier for research-system gate artifacts.

This script intentionally uses only Python stdlib. It checks file presence,
lock-state headers, basic gate_status.yaml vocabulary, and obvious blockers.
It is not a substitute for the integrity gate or referee audit.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_ARTIFACTS = [
    "project_state.md",
    "decision_log.md",
    "next_actions.md",
    "source_context.md",
    "specs/main_spec.md",
    "specs/data_spec.md",
    "specs/preprocessing_spec.md",
    "specs/methodology_spec.md",
    "specs/output_spec.md",
    "specs/spec_change_log.md",
    "qa/source_verification.md",
    "qa/claim_verification_matrix.md",
    "qa/integrity_gate.md",
    "qa/gate_status.yaml",
]

SPEC_FILES = [
    "specs/main_spec.md",
    "specs/data_spec.md",
    "specs/preprocessing_spec.md",
    "specs/methodology_spec.md",
    "specs/output_spec.md",
]

ALLOWED_LOCK_STATES = {"EXPLORATORY", "PROVISIONAL_LOCK", "LOCKED", "SUPERSEDED"}
BLOCKING_GATE_VALUES = {"BLOCKED", "REVISE", "REOPEN_ANALYSIS", "REOPEN_TEXT", "NOT_RUN", "missing"}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def lock_state(text: str) -> str | None:
    m = re.search(r"^LOCK_STATE:\s*([A-Z_]+)\s*$", text, re.MULTILINE)
    return m.group(1) if m else None


def simple_yaml_scalars(text: str) -> dict[str, str]:
    """Extract simple key: value pairs, preserving section-qualified names."""
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
        full = ".".join([x[1] for x in stack] + [key])
        out[full] = val
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_root", help="Path to project repository/root")
    ap.add_argument("--allow-unlocked", action="store_true", help="Do not fail when specs are not LOCKED")
    args = ap.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    problems: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"FAIL: project root does not exist: {root}")
        return 2

    for rel in REQUIRED_ARTIFACTS:
        if not (root / rel).exists():
            problems.append(f"missing required artifact: {rel}")

    for rel in SPEC_FILES:
        p = root / rel
        if not p.exists():
            continue
        state = lock_state(read_text(p))
        if state is None:
            problems.append(f"missing LOCK_STATE header: {rel}")
        elif state not in ALLOWED_LOCK_STATES:
            problems.append(f"invalid LOCK_STATE {state}: {rel}")
        elif state != "LOCKED" and not args.allow_unlocked:
            problems.append(f"spec is not LOCKED: {rel} ({state})")

    gate_path = root / "qa/gate_status.yaml"
    if gate_path.exists():
        scalars = simple_yaml_scalars(read_text(gate_path))
        allowed_value = re.compile(r"^(PASS|PASS_WITH_LIMITATIONS|REVISE|BLOCKED|NOT_RUN|not_needed|missing|present|mapped|EXPLORATORY|PROVISIONAL_LOCK|LOCKED|SUPERSEDED|true|false|single_bounded|status_only|human_evidence_audit|human_design_decision|prepare_review_packet|blocked)$")
        for key, val in scalars.items():
            if any(part in key for part in ["spec", "gate", "qa", "artifact", "allowed", "status"]):
                if not allowed_value.match(val) and not re.match(r"^[A-Za-z0-9_.-]+$", val):
                    warnings.append(f"unusual gate_status value: {key}: {val}")
        for key, val in scalars.items():
            if val in BLOCKING_GATE_VALUES:
                problems.append(f"blocking gate_status value: {key}: {val}")
        if scalars.get("writing_handoff.allowed") == "true" and scalars.get("blocked.status") == "true":
            problems.append("gate_status contradiction: writing_handoff.allowed=true but blocked.status=true")
        if scalars.get("writing_ready") == "true" and scalars.get("writing_handoff.allowed") == "false":
            problems.append("gate_status contradiction: writing_ready=true but writing_handoff.allowed=false")
        if scalars.get("auto_continue_allowed") == "true" and scalars.get("blocked.status") == "true":
            problems.append("gate_status contradiction: auto_continue_allowed=true but blocked.status=true")
        if scalars.get("auto_continue_allowed") == "true" and scalars.get("human_audit_required") == "true":
            problems.append("gate_status contradiction: auto_continue_allowed=true but human_audit_required=true")
        if scalars.get("auto_continue_allowed") == "true" and scalars.get("human_audit.required") == "true":
            problems.append("gate_status contradiction: auto_continue_allowed=true but human_audit.required=true")
        if scalars.get("human_audit_required") == "true" or scalars.get("human_audit.required") == "true":
            packet_state = scalars.get("human_audit.packet")
            packet_path = root / "qa/human_audit_request.md"
            if packet_state not in {"present", "mapped"} and not packet_path.exists():
                problems.append("human audit is required but qa/human_audit_request.md is missing or unmapped")
        if scalars.get("auto_continue_allowed") == "true" and scalars.get("next_action_type") not in {"single_bounded", "status_only"}:
            problems.append("auto_continue_allowed=true requires next_action_type single_bounded or status_only")
        if scalars.get("writing_handoff.allowed") == "true":
            section_map = root / "paper/section_paragraph_map.md"
            if scalars.get("writing_handoff.section_paragraph_map_complete") != "true":
                problems.append("writing_handoff.allowed=true but section_paragraph_map_complete is not true")
            if not section_map.exists():
                problems.append("writing_handoff.allowed=true but missing paper/section_paragraph_map.md")
            if scalars.get("writing_handoff.publishable_exhibits_human_checked") != "true":
                problems.append("writing_handoff.allowed=true but publishable_exhibits_human_checked is not true")

    claim_path = root / "qa/claim_verification_matrix.md"
    if claim_path.exists():
        text = read_text(claim_path)
        if "| C001 |" in text and text.count("| C") <= 1:
            warnings.append("claim_verification_matrix appears to contain only template row")
        if any(v in text for v in ["UNSUPPORTED", "CONTRADICTED", "MAJOR_DISTORTION"]):
            warnings.append("claim matrix contains potentially blocking verdict vocabulary; inspect unresolved rows")

    waiver = root / "qa/waiver_log.md"
    if waiver.exists():
        text = read_text(waiver)
        if "ACTIVE" in text and "what_cannot_be_claimed" not in text:
            problems.append("active waiver log lacks claim-narrowing field")

    invalid = root / "qa/invalidation_ledger.md"
    if invalid.exists() and "OPEN" in read_text(invalid):
        warnings.append("invalidation ledger contains OPEN rows; affected claims/exhibits may be blocked")

    print(f"Project root: {root}")
    if problems:
        print("VERDICT: FAIL")
        print("\nBlocking problems:")
        for p in problems:
            print(f"- {p}")
    else:
        print("VERDICT: PASS")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"- {w}")

    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
