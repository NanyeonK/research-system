# Research Session Launcher Protocol

Purpose: provide a single control-tower entrypoint for starting new research worker sessions without making Yeonchan decide low-level infrastructure details every time.

## Problem

A raw instruction like "start a new session" is underspecified because the launch layer must decide:
1. which execution server should own the work
2. which agent engine should run the owner session: Codex, Claude Code, or another tool
3. whether Agent Deck metadata will correctly show the tool instead of a generic `shell`
4. whether the launch is a real owner session, a read-only audit, or a human-audit packet preparation pass

Therefore, project work should not be launched by opening an arbitrary shell and typing a prompt.

## Default launch model

The current Hermes conversation is the Mac control-tower interface. It receives Yeonchan's intent and prepares the launch.

Actual project work runs in a separate owner session on the selected execution server:

```text
Yeonchan -> Mac Hermes control tower -> launcher/router -> Agent Deck owner session on server1/server2/server3
```

The owner session must start from the source-of-truth repo path:

```text
/home/nanyeon99/project/<repo_name>
```

and must be registered with Agent Deck metadata:

```text
tool = claude | codex
command = claude | codex
path = /home/nanyeon99/project/<repo_name>
title = <project-key>-owner | <project-key>-audit | <project-key>-eda
```

Sessions showing `tool=shell` or `path=/home/nanyeon99` are not valid new owner sessions unless Yeonchan explicitly requested a raw shell. Treat them as misregistered or legacy until reconciled.

## Launch router decision order

### 1. Resolve project and source of truth

Before launch:
- read `/Users/nanyeon/orchestration/projects/project-registry.yaml`
- run `/Users/nanyeon/orchestration/projects/scripts/validate_and_render.py`
- read generated registry/dashboard
- confirm `agent_deck.eligible == true`
- confirm `context.needs_context_normalization == false`
- confirm source-of-truth server/path
- if registry conflicts with Yeonchan's correction, update registry first

### 2. Select server

Use this priority:
1. if the registry has a source-of-truth server/path, use it
2. if the repo exists on multiple servers, choose the server with the cleanest/freshest repo state unless Yeonchan specifies otherwise
3. for new or missing repos, choose by capacity:
   - CPU/RAM EDA: least loaded server with enough free RAM
   - GPU work: only a GPU-healthy node; server2 GPU is avoided while NVML mismatch persists
   - long risky job: node with most slack
4. never choose server by project identity alone

Before launching, check:
- hostname
- repo path
- git branch and dirty tree
- active Agent Deck sessions for the same repo
- tmux panes for legacy sessions
- CPU/RAM/GPU state if work is nontrivial

### 3. Select agent engine

Default engine rules:

- Claude Code:
  - read-only status/audit
  - long-context synthesis
  - writing-system/exhibit-spine/manuscript-readiness audit
  - human-audit packet preparation
  - broad research interpretation or design review

- Codex:
  - package/code/test/refactor work
  - deterministic scripts
  - reproducibility work
  - data/EDA implementation and small pipeline patches
  - table/figure generation code

- Hermes direct session:
  - control tower orchestration
  - dashboard/cron/system edits
  - brief deterministic checks
  - not default for long remote repo ownership unless intentionally installed/tested remotely

For academic projects, default to one active owner agent per repo. Do not run Claude and Codex on the same repo/branch concurrently without an explicit handoff or isolated branch/worktree scope.

### 4. Select launch mode

- `read_only_audit`: inspect status, risks, next executable actions; no edits
- `eda_pre_pilot`: data inventory, schema, row counts, missingness, merge support, summary statistics, table/figure plan shell
- `implementation`: code/test/refactor within approved scope
- `human_audit_packet`: create `qa/human_audit_request.md`; no decision execution
- `writing_prep`: only after research-to-writing handoff gates are satisfied

Default for uncertain or dirty repos: `read_only_audit`.
Default for current research-system rollout: `eda_pre_pilot` when gate permits.

## Valid Agent Deck launch pattern

Run from Mac through SSH or the conductor after registry/source-path checks:

```bash
ssh <server> 'cd /home/nanyeon99/project/<repo> && agent-deck launch . -t <project-key>-<mode> -g academic-owner -c <claude|codex> -m "<launch prompt>"'
```

Do not launch from `$HOME`.
Do not omit `-c <claude|codex>`.
Do not accept `tool=shell` metadata for a new owner session.

After launch, verify on the target server:

```bash
agent-deck session show <id> --json
agent-deck list --json
```

Required verification:
- status is running or waiting normally
- tool/command is `claude` or `codex`
- path is the repo root
- title names project and mode
- dashboard can index it

If metadata shows `shell`, fix metadata or relaunch before allowing project work.

## Minimal Yeonchan command

Yeonchan should not need to decide server/tool every time. A valid command is:

```text
<project> 새 worker 시작. 목표: data/EDA pre-pilot. 금지: direct archive restore, prose, gate crossing. human audit 필요하면 packet부터.
```

The launcher/router must then resolve server, engine, mode, and Agent Deck command.

If the choice materially changes cost, risk, or scientific path, surface a short launcher packet:

```text
Launch decision needed:
- Project:
- Repo/source path:
- Candidate server(s):
- Recommended server and why:
- Recommended engine and why:
- Launch mode:
- What will not be allowed:
```

## Anti-patterns

- Starting Agent Deck from `/home/nanyeon99` and then navigating manually
- Launching with generic shell so dashboard sees `tool=shell`
- Asking Yeonchan to choose server/tool without first checking registry and resource state
- Launching Claude and Codex against the same repo simultaneously
- Treating read-only audit as permission to edit
- Starting a human-audit decision without `qa/human_audit_request.md`

## Persistence

Each launch should leave evidence in:
- Agent Deck metadata
- dashboard output
- repo-local `AGENT_STATUS.md` or `research_log.md` if the owner makes changes
- second_brain / walnut only for launch decisions, failures, rule changes, or reusable patterns
