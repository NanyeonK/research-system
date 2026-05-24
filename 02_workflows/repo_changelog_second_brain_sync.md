# Repo Changelog To second_brain Sync

Purpose: keep project operating memory lightweight and automatic. The project repo remains the source of truth through git history/tree plus repo-local `CHANGELOG.md`; second_brain receives only a mirror of `CHANGELOG.md` into the matching `04_Ventures/<project-or-walnut>/` folder.

## Policy

Authoritative state:
1. git tree, branch, commits, and dirty-tree status in the project repo
2. repo-local `CHANGELOG.md`
3. repo-local canonical state/QA/spec files when needed
4. second_brain mirror of `CHANGELOG.md` for memory/search convenience

Agents must not manually summarize routine project progress into second_brain project pages when a repo `CHANGELOG.md` can carry the state. Agents should update the repo `CHANGELOG.md`; the sync job mirrors it.

second_brain is not the primary state ledger for active repo work. It is a synced memory surface.

## Destination

For each registry project with `context.walnut`:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/04_Ventures/<context.walnut>/CHANGELOG.md
```

For projects without `context.walnut`:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/04_Ventures/<project_key>/CHANGELOG.md
```

The destination file is managed. Do not edit it manually.

## Sync source

Registry:

```text
/Users/nanyeon/orchestration/projects/project-registry.yaml
```

Remote source:

```text
<source_of_truth.server>:<source_of_truth.path>/CHANGELOG.md
```

The sync uses the registry source-of-truth server/path. It does not scan random repos.

## Local command

```bash
/Users/nanyeon/bin/research-changelog-sync
```

Optional:

```bash
/Users/nanyeon/bin/research-changelog-sync <project_key_or_walnut_slug> --verbose
```

Script implementation:

```text
/Users/nanyeon/bin/research-changelog-sync.py
```

Research-system reference copy:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/scripts/sync_project_changelogs_to_second_brain.py
```

## Automatic Hermes cron job

Launchd was tested but disabled because macOS denied background writes into the Synology CloudStorage vault (`Operation not permitted`). The active automation is a Hermes cron job.

Cron job:

```text
job_id: 51116c364a20
name: research-changelog-sync
schedule: every 10m
mode: no_agent
script: research_changelog_sync.sh
```

Script:

```text
/Users/nanyeon/.hermes/scripts/research_changelog_sync.sh
```

Logs:

```text
/Users/nanyeon/logs/research-changelog-sync.out.log
/Users/nanyeon/logs/research-changelog-sync.err.log
```

Manual run:

```bash
/Users/nanyeon/.hermes/scripts/research_changelog_sync.sh
```

Manage job through Hermes cron controls. The disabled launchd plist remains at `/Users/nanyeon/Library/LaunchAgents/com.nanyeon.research-changelog-sync.plist` for reference only; do not rely on it unless macOS Full Disk Access / CloudStorage permissions are fixed.

## CHANGELOG.md standard

Every active project repo should have a root-level `CHANGELOG.md`.

Each meaningful change should append/prepend a dated entry with:
- date/time KST
- actor/tool
- server/path
- git branch/commit or dirty-tree note
- changed artifact paths
- verification result
- next human decision if any

The git tree handles exact file-level history. The changelog handles human-readable state transitions.

## What sync does not do

It does not:
- mirror the full repo
- mirror raw data, caches, outputs, checkpoints, secrets, or submission files
- replace git
- replace `MANIFEST.md`, specs, or QA gates
- manually update wiki prose pages
- resolve missing repo `CHANGELOG.md` files automatically

If a repo has no `CHANGELOG.md`, the sync logs a miss and leaves second_brain untouched.

## Current setup note

The first live launchd run completed with exit 0 and reported missing repo `CHANGELOG.md` files for many registry projects. This is expected until active repos add the root changelog. Do not mass-create changelogs across remote repos without a project-specific onboarding action.
