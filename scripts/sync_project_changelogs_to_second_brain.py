#!/usr/bin/env python3
"""Sync remote project CHANGELOG.md files into second_brain 04_Ventures folders.

Design principles:
- Repo state remains authoritative in git + repo-local CHANGELOG.md.
- second_brain receives a read-only mirror of CHANGELOG.md only.
- Agents should update the repo CHANGELOG.md, not hand-write second_brain project memory.
- This script is deterministic and safe to run from launchd/cron.

Default destination:
  /Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/04_Ventures/<walnut_or_project>/CHANGELOG.md

Project discovery:
  /Users/nanyeon/orchestration/projects/project-registry.yaml
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional

DEFAULT_REGISTRY = Path("/Users/nanyeon/orchestration/projects/project-registry.yaml")
DEFAULT_VAULT = Path("/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain")
DEFAULT_EXTRA_PROJECTS = Path("/Users/nanyeon/orchestration/projects/agentdeck-changelog-sync-extra.json")
ACTIVE_STATUSES = {"active_analysis", "active_writing", "human_gated", "setup_design", "clean_restart"}
DENY_STATUSES = {"stale_archive", "completed_shipped", "infra"}

SERVER_ALIASES = {
    "server1": "nanyeon99@115.145.17.140",
    "server2": "nanyeon99@115.145.17.139",
    "server3": "server3",
}


def sh(cmd: List[str], timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)


def parse_registry_minimal(path: Path) -> Dict[str, Dict[str, Optional[str]]]:
    """Parse only fields needed from project-registry.yaml using stdlib.

    The registry has stable indentation:
      projects:
        key:
          status:
          source_of_truth:
            server:
            path:
          context:
            walnut:
    """
    text = path.read_text(encoding="utf-8")
    projects: Dict[str, Dict[str, Optional[str]]] = {}
    in_projects = False
    cur: Optional[str] = None
    section: Optional[str] = None

    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("projects:"):
            in_projects = True
            cur = None
            section = None
            continue
        if not in_projects:
            continue
        m_project = re.match(r"^  ([A-Za-z0-9_.-]+):\s*$", raw)
        if m_project:
            cur = m_project.group(1)
            projects[cur] = {"project": cur, "status": None, "server": None, "path": None, "walnut": None}
            section = None
            continue
        if cur is None:
            continue
        m_section = re.match(r"^    ([A-Za-z0-9_.-]+):\s*$", raw)
        if m_section:
            section = m_section.group(1)
            continue
        m_key = re.match(r"^    ([A-Za-z0-9_.-]+):\s*(.*)$", raw)
        if m_key and section is None:
            key, val = m_key.group(1), clean_yaml_scalar(m_key.group(2))
            if key == "status":
                projects[cur]["status"] = val
            continue
        m_nested = re.match(r"^      ([A-Za-z0-9_.-]+):\s*(.*)$", raw)
        if m_nested:
            key, val = m_nested.group(1), clean_yaml_scalar(m_nested.group(2))
            if section == "source_of_truth" and key in {"server", "path"}:
                projects[cur][key] = val
            elif section == "context" and key == "walnut":
                projects[cur]["walnut"] = None if val in {"null", "None", ""} else val
    return projects


def clean_yaml_scalar(value: str) -> str:
    value = value.strip()
    if value in {"null", "~"}:
        return "null"
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1]
    return value


def slug_for_project(project: Dict[str, Optional[str]]) -> str:
    return project.get("walnut") or project.get("project") or "unknown-project"


def should_sync(project: Dict[str, Optional[str]], include_human_gated: bool = True) -> bool:
    status = project.get("status") or ""
    if status in DENY_STATUSES:
        return False
    if status == "human_gated" and include_human_gated:
        return True
    return status in ACTIVE_STATUSES


def remote_read(server: str, repo_path: str, rel: str, timeout: int = 30) -> Optional[str]:
    host = SERVER_ALIASES.get(server, server)
    # Use python on remote to avoid shell glob surprises; repo_path/rel are registry controlled.
    code = (
        "from pathlib import Path; "
        f"p=Path({repo_path!r})/{rel!r}; "
        "import sys; "
        "sys.exit(3) if not p.exists() else None; "
        "print(p.read_text(encoding='utf-8', errors='replace'), end='')"
    )
    cp = sh(["ssh", host, "python3 -c " + shell_quote(code)], timeout=timeout)
    if cp.returncode != 0:
        return None
    return cp.stdout


def remote_git_summary(server: str, repo_path: str, timeout: int = 20) -> Dict[str, str]:
    host = SERVER_ALIASES.get(server, server)
    cmd = (
        f"cd {shell_quote(repo_path)} 2>/dev/null && "
        "printf 'branch=' && git rev-parse --abbrev-ref HEAD 2>/dev/null || true; "
        "printf '\ncommit=' && git rev-parse --short HEAD 2>/dev/null || true; "
        "printf '\ndirty=' && if [ -n \"$(git status --porcelain 2>/dev/null)\" ]; then echo true; else echo false; fi"
    )
    cp = sh(["ssh", host, "sh", "-lc", cmd], timeout=timeout)
    out: Dict[str, str] = {"branch": "unknown", "commit": "unknown", "dirty": "unknown"}
    if cp.returncode != 0:
        return out
    for line in cp.stdout.splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def shell_quote(s: str) -> str:
    return "'" + s.replace("'", "'\"'\"'") + "'"


def write_changelog_mirror(dest: Path, project: Dict[str, Optional[str]], changelog: str, git_summary: Dict[str, str]) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    now = _dt.datetime.now().astimezone().isoformat(timespec="seconds")
    header = f"""---
sync_source: repo_CHANGELOG_md
project: {project.get('project')}
repo_server: {project.get('server')}
repo_path: {project.get('path')}
repo_branch: {git_summary.get('branch', 'unknown')}
repo_commit: {git_summary.get('commit', 'unknown')}
repo_dirty: {git_summary.get('dirty', 'unknown')}
synced_at: {now}
managed_by: sync_project_changelogs_to_second_brain.py
---

# Repo CHANGELOG Mirror — {project.get('project')}

This file is an automatic mirror of the project repo's `CHANGELOG.md`.
Do not edit this second_brain copy manually. Edit the repo `CHANGELOG.md` and let the sync refresh this file.

---

"""
    content = header + changelog.rstrip() + "\n"
    old = dest.read_text(encoding="utf-8") if dest.exists() else None
    if old == content:
        return False
    dest.write_text(content, encoding="utf-8")
    return True


def run(args: argparse.Namespace) -> int:
    registry = Path(args.registry).expanduser()
    vault = Path(args.vault).expanduser()
    if not registry.exists():
        print(f"FAIL registry missing: {registry}", file=sys.stderr)
        return 2
    if not vault.exists():
        print(f"FAIL vault missing: {vault}", file=sys.stderr)
        return 2

    projects = parse_registry_minimal(registry)
    extra_path = Path(args.extra_projects).expanduser()
    if extra_path.exists():
        for row in __import__("json").loads(extra_path.read_text(encoding="utf-8")):
            key = row["project"]
            projects[key] = {"project": key, "status": row.get("status"), "server": row.get("server"), "path": row.get("path"), "walnut": row.get("walnut")}
    selected = args.projects or []
    changed = 0
    skipped = 0
    missing = 0
    errors = 0

    for key, project in projects.items():
        if selected and key not in selected and slug_for_project(project) not in selected:
            continue
        if not args.all and not should_sync(project, include_human_gated=args.include_human_gated):
            skipped += 1
            continue
        server = project.get("server")
        repo_path = project.get("path")
        if not server or not repo_path or repo_path == "null":
            skipped += 1
            continue
        try:
            changelog = remote_read(server, repo_path, "CHANGELOG.md", timeout=args.timeout)
            if changelog is None:
                missing += 1
                if args.verbose:
                    print(f"MISS {key}: no remote CHANGELOG.md at {server}:{repo_path}")
                continue
            git_summary = remote_git_summary(server, repo_path, timeout=max(10, min(args.timeout, 30)))
            slug = slug_for_project(project)
            dest = vault / "04_Ventures" / slug / "CHANGELOG.md"
            did_change = write_changelog_mirror(dest, project, changelog, git_summary)
            if did_change:
                changed += 1
                print(f"SYNC {key} -> {dest}")
            elif args.verbose:
                print(f"OK {key}: unchanged")
        except Exception as exc:  # keep cron/launchd run robust across one bad project
            errors += 1
            print(f"ERROR {key}: {exc}", file=sys.stderr)

    print(f"summary changed={changed} missing={missing} skipped={skipped} errors={errors}")
    return 1 if errors else 0


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--extra-projects", default=str(DEFAULT_EXTRA_PROJECTS))
    ap.add_argument("--all", action="store_true", help="Sync non-deny projects, not only active statuses")
    ap.add_argument("--include-human-gated", action="store_true", default=True)
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("projects", nargs="*", help="Optional project keys or walnut slugs to sync")
    return run(ap.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
