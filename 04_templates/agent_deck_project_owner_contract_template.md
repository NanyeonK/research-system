# Agent Deck Project Owner Contract Template

Use this before launching a single owning Agent Deck agent on an exploratory research-paper repo.

This template is for early-stage idea -> pilot -> paper-project work and for normalizing non-package active research-paper projects. Package-managed repos such as `macroforecast` and `eapctf` use their own package/reproducibility process, unless explicitly borrowing the status/changelog/provenance/review-packet conventions only.

## Owner identity

Project:
Registry key:
Walnut:
Date/time KST:
Controller:
Owner agent: claude-code | codex
Agent Deck session:
Agent Deck tool metadata: claude | codex
Agent Deck launch cwd: /home/nanyeon99/project/<repo>
Mode: read-only-status | idea-evaluation | pilot | experiment | review-audit | writing-support

## Source of truth

Server:
Repo path:
Base branch:
Owner branch/worktree:
Last commit before launch:
Dirty tree before launch: clean | dirty:<N> | unknown

Registry gate:
- [ ] registry validated/regenerated
- [ ] `agent_deck.eligible == true` or user explicitly approved read-only/status-only launch
- [ ] `context.needs_context_normalization == false` or this task is context normalization
- [ ] source-of-truth server/path verified
- [ ] walnut/core context read if available

## Pipeline status at launch

Stage:
Idea one-liner:
Current contract path:
Current task:
Blocked on:
Expected next artifact:

## Task

Goal:
Non-goals:
Reason this owner/tool was chosen:

ARS-Codex routing posture, if relevant:
- [ ] upstream `Imbad0202/academic-research-skills-codex` is used only as classification/protocol vocabulary
- [ ] no upstream prompts, templates, agent files, slash-command semantics, or installable skill runtime are imported
- [ ] local research_system gates remain source of truth
- [ ] writing_system boundary remains intact; no manuscript prose unless writing gates are cleared
- [ ] owner uses one-project-one-owner routing, not an ARS-style same-project agent team

ARS-inspired local QA packet, when source/claim/integrity work is in scope:
- [ ] `qa/source_verification.md` separates source existence, locator, temporal fit, source role, and claim role
- [ ] `qa/claim_verification_matrix.md` separates claim wording, support grade, required evidence, allowed wording, forbidden wording, and action
- [ ] `qa/integrity_gate.md` gives a human-readable PASS / PASS_WITH_LIMITATIONS / REVISE / BLOCKED verdict
- [ ] `qa/gate_status.yaml` gives machine-readable readiness fields checked by the project verifier

## File scope

Allowed to read:
-

Allowed to edit:
-

Forbidden to edit:
-

Conflict check:
- [ ] no active owner session for this same project
- [ ] no active legacy tmux/session editing same branch/file scope
- [ ] repo/worktree status captured before launch
- [ ] launch is conductor-mediated or explicitly approved by Yeonchan
- [ ] session will not be created as `tool=shell` unless this is a raw shell task
- [ ] launch cwd is the registry source-of-truth project root, not `/home/nanyeon99`

## Required context load

System context:
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/AGENTS.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/00_START_HERE.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/02_workflows/agent_deck_research_tracking.md`

Project context:
- [ ] `AGENTS.md` or `CLAUDE.md` with `Pipeline Status`
- [ ] `AGENT_STATUS.md` if present
- [ ] `CHANGELOG.md` if present
- [ ] `MANIFEST.md` if present
- [ ] `decision_log.md` if present
- [ ] `idea-stage/docs/research_contract.md` if present
- [ ] latest `findings.md` entries if present
- [ ] relevant `PILOT_LOG.md` or `EXPERIMENT_LOG.md` if present

For writing/table/figure/exhibit tasks:
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/writing_execution_card.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/voice_yeonchan.md`
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md` when table/figure/exhibit work
- [ ] `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/exhibit_design_router.md` when table/figure/exhibit work

## Tracking obligations

Owner must update these when work changes state:
- [ ] `Pipeline Status` block in `AGENTS.md` or `CLAUDE.md`
- [ ] `AGENT_STATUS.md`
- [ ] `CHANGELOG.md`
- [ ] `MANIFEST.md` for created/updated artifacts
- [ ] `decision_log.md` for accepted decisions
- [ ] `findings.md` for non-obvious discoveries or failures
- [ ] archive previous result versions before replacing active outputs
- [ ] `ARCHIVE_MANIFEST.md` and `superseded_by.md` for every archive folder
- [ ] pilot runs/results under `pilot/` until promoted

## Allowed commands

Commands allowed:
-

Commands forbidden:
- large benchmark runs unless explicitly approved
- destructive sync/delete
- force push
- external post/submission
- secret reads beyond explicitly required config
- autonomous full-paper drafting before writing gates

## Verification

Primary verification command:
Expected result:
Secondary verification command:
Expected result:
Artifact freshness checks:
-

Gate-status fields to verify before auto-continuation or handoff:
- `writing_ready` / `writing_handoff.allowed` must not be true while source, claim, spec, or integrity artifacts are missing or blocked.
- `referee_audit_ready` must not be true unless writing handoff is allowed and review artifacts are complete.
- `autonomous_owner_ready` and `auto_continue_allowed` must be explicit; absence is treated as false.
- `human_audit_required` or `human_audit.required=true` requires a concrete `qa/human_audit_request.md` or equivalent packet before surfacing a Yeonchan decision.
- `next_action_type` must be a single bounded action. Multiple options mean not auto-continuable until a controller or Yeonchan chooses.

Owner final-response contract:
- Every owner response must end with one `OWNER_STATUS_V1` block.
- If the owner gives multiple options, missing fields, or a decision/artifact dependency, it must set `auto_continue_allowed=false`.
- If `auto_continue_allowed=true`, `next_action_type` must be `single_bounded`, `blocked_on` must be `none`, `required_human_decision` must be `none`, `required_artifact` must be `none`, and `next_allowed_action` must contain exactly one concrete action.
- Missing or malformed `OWNER_STATUS_V1` is treated as not auto-continuable by the conductor.
- Non-human-gated work must proceed from a repo-local execution plan. If no plan exists, the next safe action is to create a bounded plan for already-approved scope. If a plan exists, execute the next green plan step and stop only when a checkpoint creates a real human/design/artifact/policy decision.

```text
OWNER_STATUS_V1:
project_key: <canonical project key>
stage: <current stage/gate>
HUMAN_AUDIT_REQUIRED: yes|no
auto_continue_allowed: true|false
next_action_type: single_bounded|human_design_gate|artifact_supply_gate|packet_reply_gate|status_only|blocked|none
next_allowed_action: <exactly one action, or exact gate if blocked>
active_plan: <path|plan_creation_needed|none>
current_plan_step: <step id|create_plan|none>
plan_checkpoint_status: clear|human_check_required|artifact_missing|verification_failed|none
plan_change_required: true|false
blocked_on: none|decision|artifact|policy|verification_failure|human_gate|external_dependency
required_human_decision: <none or exact plain-language question>
required_artifact: <none or exact path/export/source>
forbidden_actions_preserved: yes|no
verification: <commands/artifacts>
changed_files: <none or paths>
ready_for_conductor_auto_nudge: yes|no
```

## Human review and confirmation gates

The project owner must treat these as human-heavy gates:

1. First project launch
   - Confirm project classification, source-of-truth server/path, owner tool, launch scope, initial idea/claim, stage, and dirty-tree/no-conflict status with Yeonchan.

2. Paper design / analysis design confirmation
   - Before broad analysis or experiment execution, prepare a design packet and wait for Yeonchan confirmation.
   - The packet must cover research question, mechanism, data, sample/panel, identification/forecasting target, main estimand/target, baseline specification, controls/fixed effects, table/figure plan, falsification criteria, and expected claim boundary.

3. Review/Audit Gate
   - Prepare Mac-local review packet, result-to-claim map, table/figure traceability, leakage/spec-drift/raw-vs-derived audit, and accepted/rejected claim list.
   - Do not promote results into claims without Yeonchan confirmation.

4. Paper Writing
   - Confirm story/exhibit lock before prose.
   - Draft only after safe claims, forbidden claims, unresolved gaps, and voice rules are explicit.

Divergence handling:
- If analysis design, feasibility, data availability, identification story, forecast target, results, or table/figure evidence differs from the initial idea or Yeonchan-approved design, stop.
- Write a divergence memo listing original design, observed divergence, evidence/artifact path, affected claims/exhibits, options, and recommended decision.
- Allowed options: continue original design, revise design, pivot project, pause, kill.
- Do not silently pivot or rewrite the project direction.

## Human review and Mac review shelf

Required for review-audit, writing-support, and publish/package modes:
- [ ] Yeonchan-facing artifacts copied to `/Users/nanyeon/Documents/research_review_artifacts/<server>/<project_key>/`
- [ ] `/Users/nanyeon/Documents/research_review_artifacts/_review_index.md` updated
- [ ] copied artifacts are small review artifacts only, not full repo/raw data/cache/checkpoints
- [ ] source server, repo path, commit/dirty note, and source path recorded
- [ ] human decision needed is explicit

For review-audit mode:
- [ ] owner produced primary review packet
- [ ] independent reviewer 1 checked leakage/spec drift/data provenance/raw-vs-derived ambiguity
- [ ] independent reviewer 2 checked result-to-claim validity/table-figure traceability/unsupported interpretation
- [ ] reviewer outputs are read-only and do not create same-project concurrent owner work

For table/figure/publish artifacts:
- [ ] table-builder applied to every table shell or table artifact
- [ ] figure-builder applied to every figure shell or figure artifact
- [ ] exhibit role and sequence checked through the writing-system exhibit router/card

For writing-support mode:
- [ ] story lock exists
- [ ] paper skeleton exists
- [ ] table/figure map exists
- [ ] Yeonchan voice profile loaded
- [ ] accepted human revisions will be captured project-locally and routed to voice update when stable/repeated

## Stop conditions

Stop and return to controller if:
- source-of-truth path differs from registry
- another owner is active for the same project
- uncommitted changes outside allowed scope exist
- verification fails without a clear local fix
- human decision is needed
- unsupported claim/citation/result is required
- large benchmark/external side effect is required
- package-first process conflict appears
- session was launched with `tool=shell` or `/home/nanyeon99` cwd and no relaunch/handoff decision exists
- active output folders contain stale previous-result versions not marked active in `MANIFEST.md`
- pilot work is being written outside `pilot/` before promotion
- Review/Audit Gate, Writing Transition, or publish/package promotion lacks a Mac-local review packet for Yeonchan
- table/figure artifacts lack required `table-builder` or `figure-builder` metadata
- writing requires a new voice rule that has not been accepted or recorded

## Handoff artifact

Handoff path:

Handoff must list:
- current stage
- files read
- files changed
- commands run and outcomes
- artifacts created
- verification status
- unresolved risks
- human decisions needed
- exact next action
- recommended next owner, if any
