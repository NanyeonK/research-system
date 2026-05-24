# Multi-Agent Repo Orchestration — Legacy / Exceptional Only

Updated: 2026-05-20

Default academic workflow moved to `02_workflows/agent_deck_research_tracking.md`.

Use this file only when Yeonchan explicitly approves an exceptional multi-lane setup. The normal Agent Deck academic workflow is one project = one active owning agent, tracked by Pipeline Status, git, CHANGELOG, MANIFEST, and project owner contracts.

Purpose:
- document the exceptional conditions under which Codex and Claude Code may work at the same time without corrupting research repos, project memory, or manuscript claims
- make each exceptional lane expose a clear lane contract: source-of-truth path, agent role, branch/worktree, allowed files, forbidden files, verification command, and handoff artifact
- keep Hermes/Mac as the controller and server repos as execution surfaces

## Core rule

Never run Codex and Claude Code against the same repo branch and same file scope at the same time.

Parallel work is allowed only when one of these isolation modes is true:
1. different repos
2. same repo, different git worktrees/branches, non-overlapping file scopes
3. one agent is read-only audit/review while the other edits
4. one agent edits generated artifacts only after the producing agent has finished and committed/staged outputs

If none is true, serialize the work.

## Agent role defaults

Codex default lane:
- package-first code changes
- tests, fixtures, CLIs, wrappers, reproducibility scripts
- refactors with explicit acceptance commands
- deterministic table/figure generation scripts after exhibit requirements are fixed

Claude Code default lane:
- repo status audit
- manuscript/writing-system compliance audit
- exhibit-spine design and table/figure interpretation audit
- one-shot planning in print mode
- prose co-writing only after writing kickoff gates are satisfied

Hermes/controller default lane:
- registry and walnut checks
- lane assignment
- prompt construction
- conflict prevention
- final verification
- walnut/project-wiki save

## Pre-flight gate

Before launching any Codex, Claude Code, Agent Deck, tmux, or remote coding-agent lane:

1. Read `/Users/nanyeon/orchestration/projects/project-registry.yaml`.
2. Confirm the project has:
   - `agent_deck.eligible == true`
   - `context.needs_context_normalization == false`
   - status in `active_analysis` or `active_writing`
3. Confirm source-of-truth server/path from the registry.
4. Read the project walnut if `context.walnut` is set.
5. Confirm no conflicting Agent Deck/tmux sessions already edit the same branch or file scope.
6. Write a lane contract before starting autonomous edits.

If the registry and human correction conflict, the human correction wins, but update the registry and regenerate dashboard/json before launch.

## Lane contract

Each autonomous lane must have a contract. Store it in the project repo when possible:

`docs/agent_lanes/YYYYMMDD-HHMM-<agent>-<short-task>.md`

If repo docs are not ready or the lane is read-only, store the contract in the controller notes and copy it into the repo at the next safe checkpoint.

Required fields:
- Project
- Source-of-truth server/path
- Agent: `codex`, `claude-code`, or `hermes`
- Mode: `edit`, `read-only-audit`, `review`, or `writing`
- Branch/worktree
- Allowed file scope
- Forbidden file scope
- Inputs to read first
- Commands allowed
- Commands forbidden
- Verification command
- Handoff artifact path
- Stop conditions

Use `04_templates/agent_lane_contract_template.md`.

## Same-repo parallel pattern

Use this pattern only for cleanly separable tasks.

Example:
- Codex lane: `agent/codex-package-fixtures`
  - edits: `src/`, `tests/`, `pyproject.toml`, package docs
  - forbidden: `paper/`, `manuscript/`, final tables unless explicitly produced by tests
- Claude lane: `agent/claude-exhibit-audit`
  - mode: read-only audit unless explicitly assigned edits
  - reads: tables, figures, manuscript draft, project state, source context
  - edits: `docs/audits/` or `paper/audit/` only
  - forbidden: code, data, generated outputs

Merge order:
1. Codex finishes code/tests and records verification.
2. Hermes verifies code lane.
3. Claude consumes verified artifacts for exhibit/manuscript audit.
4. Hermes applies any accepted cross-lane changes.

## Different-repo parallel pattern

Preferred when multiple active projects need progress.

Current registry-eligible examples as of 2026-05-20:
- `eapctf` on server2: Codex package/code/test lane. Benchmark-scale runs are forbidden unless yeonchan explicitly switches modes.
- `confo_vol_port` on server2: Claude Code writing-kickoff/exhibit/robustness audit lane. Prose drafting remains paragraph-gated.

## Prompt construction

For paper, manuscript, table, figure, exhibit, and writing tasks, prefix both Codex and Claude Code prompts with:

`/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/agent_prompts/codex_claude_code_prompt_templates.md`

At minimum require the agent to read:
1. `research_paper_system/AGENTS.md`
2. `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md`
3. `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/writing_execution_card.md`
4. `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/voice_yeonchan.md`

For table/figure/exhibit work, also require:
1. `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md`
2. `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/exhibit_design_router.md`
3. matching card under `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/exhibit_cards/`

For code/package tasks, include:
- registry source-of-truth server/path
- walnut phase and next action
- package-first rule
- benchmark/no-benchmark rule
- exact verification commands
- lane contract path

## Stop conditions

Stop the lane and return to Hermes/controller if:
- source-of-truth path is not the registry path
- repo has uncommitted changes outside the lane's allowed scope
- another active session is editing the same file scope
- test/verification command fails for a reason the agent cannot explain
- writing task reaches a human-required paragraph/exhibit decision
- empirical claim needs unsupported citation, result, or method detail
- large benchmark, destructive sync, force push, external posting, or submission action is needed

## Handoff standard

Each lane must finish with a handoff containing:
- files read
- files changed
- branch/worktree
- commands run and outcomes
- verification status
- unresolved gaps
- human decisions needed
- recommended next lane owner

No handoff means the lane is incomplete.

## Final controller gate

Hermes/controller verifies before declaring work complete:
1. `git status --short` in the source-of-truth repo/worktree
2. relevant test/lint/build command
3. generated artifacts exist and are fresh when claimed
4. no forbidden file-scope edits
5. handoff artifact exists
6. walnut/project-wiki update if project state changed

## Practical first rollout

Stage 1: install this orchestration layer in the research system.

Stage 2: pilot two independent repo lanes:
- Codex on `eapctf` for package/test/status work only
- Claude Code on `confo_vol_port` for read-only writing/exhibit audit or writing-kickoff prep

Stage 3: after pilot handoffs are clean, allow same-repo split lanes using separate branches/worktrees.
