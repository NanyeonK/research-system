# Agent Lane Contract Template

Use this before launching Codex, Claude Code, Agent Deck, tmux, or any autonomous coding/writing agent on a research repo.

## Lane identity

Project:
Registry key:
Walnut:
Date/time KST:
Controller:
Agent:
Mode: edit | read-only-audit | review | writing

## Source of truth

Server:
Repo path:
Base branch:
Lane branch/worktree:
Agent Deck session or tmux session:

Registry gate:
- [ ] `agent_deck.eligible == true`
- [ ] `context.needs_context_normalization == false`
- [ ] status is `active_analysis` or `active_writing`
- [ ] source-of-truth server/path verified
- [ ] walnut read if available

## Task

Goal:
Non-goals:

## File scope

Allowed to read:
- 

Allowed to edit:
- 

Forbidden to edit:
- 

Conflict check:
- [ ] no active session editing same branch/file scope
- [ ] repo/worktree status captured before launch

## Required context load

For all research-paper tasks:
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/AGENTS.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/00_START_HERE.md`

For writing/table/figure/exhibit tasks:
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/writing_execution_card.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/voice_yeonchan.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md` when table/figure/exhibit work
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/exhibit_design_router.md` when table/figure/exhibit work
- [ ] matching exhibit card when table/figure/exhibit work

Project-local context:
- [ ] `README.md`
- [ ] `project_state.md` or documented equivalent
- [ ] `decision_log.md` or documented equivalent
- [ ] `next_actions.md` or documented equivalent
- [ ] `source_context.md` or documented equivalent

## Allowed commands

Commands allowed:
- 

Commands forbidden:
- large benchmark runs unless explicitly approved
- destructive sync/delete
- force push
- external post/submission
- secret reads beyond explicitly required config

## Verification

Primary verification command:
Expected result:
Secondary verification command:
Expected result:
Artifact freshness checks:
- 

## Stop conditions

Stop and return to controller if:
- source-of-truth path differs from registry
- uncommitted changes outside allowed scope exist
- another lane conflicts with this file scope
- verification fails without clear local fix
- human decision is needed
- unsupported claim/citation/result is required
- large benchmark or external side effect is required

## Handoff artifact

Handoff path:

Handoff must list:
- files read
- files changed
- commands run and outcomes
- verification status
- unresolved gaps
- human decisions needed
- recommended next lane owner
