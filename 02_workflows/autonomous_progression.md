# Autonomous Progression Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

ARIS exposes per-skill auto-progress constants that interact with our gates. Map them as follows:

| ARIS constant | Default in ARIS | Default for our pipeline |
|---|---|---|
| `AUTO_PROCEED` | `true` (auto-select top idea, auto-continue at checkpoints) | `false` at any cross-phase boundary unless this workflow explicitly authorizes auto-proceed |
| `HUMAN_CHECKPOINT` | `false` (loop runs autonomously) | `true` when the gate touches identification, reproducibility, core interpretation, replication-package release, submission, or R&R response |
| `MAX_ROUNDS` | `4` for `/auto-review-loop` | `2` at submission gate to force a human review between rounds |
| `MAX_PILOT_IDEAS` | `3` | not applicable to econ/finance projects; pilot decisions go through `02_workflows/project_structure.md` |
| `MAX_TOTAL_GPU_HOURS` | `8` | irrelevant for our econ pipeline; replace with budget rules from `02_workflows/project_structure.md` |
| `REVIEWER_DIFFICULTY` | `medium` | `hard` for empirical-econ submission audit; `nightmare` for replication-package release |
| `COMPACT` | `false` | `true` when running ARIS skills inside our flow, so the executor reads `findings.md` and `EXPERIMENT_LOG.md` instead of full logs |
| `AUTO_FEEDBACK_INTERVAL` | not explicit | after each pilot sub-step, emit compact EDA verdict, falsification result, artifact path, and next allowed action before continuing |
| `PILOT_ROUND_TRIGGER` | skill-specific | before real-run promotion, run data probe → write pilot findings snippet → stop for human verdict if kill thresholds or claim-direction choices appear |

Binding rules:
- ARIS `AUTO_PROCEED=true` is rejected at idea-gate, kickoff-gate, exhibit-`FIX`, and submission-gate transitions.
- ARIS `nightmare` mode (reviewer reads repo directly via `codex exec`) is allowed and recommended for the final referee audit.
- ARIS skill chains that span gates (`/research-pipeline`) must be split at our gate boundaries; do not let a single ARIS pipeline cross from analysis to writing without our writing-kickoff acceptance.

Purpose:
- define when agents may continue research-paper work without asking the human
- keep automatic progress bounded by evidence, gates, and reversible state updates
- make phase transitions readable from project files instead of chat memory
- require idea co-development before Project Start

## Core Rule

Agents may continue automatically only inside the current approved gate.

An agent must stop and ask for a human decision when the next action would:
- start a full project from an idea that has not cleared the idea gate
- change the research question, target claim, target audience, or should-not-claim boundary
- label an exhibit `FIX`
- treat a table, figure, manuscript, or empirical pipeline as final
- submit, email, delete, transfer sensitive data, or expand permissions
- choose between two viable paper directions

## Autonomy Levels

Use these levels in `project_state.md` and `next_actions.md`.

| Level | Meaning | Agent may do |
|---|---|---|
| `A0_BLOCKED` | Missing critical input or human decision | Record gaps, propose options, stop |
| `A1_PREPARE` | Safe setup or documentation work | Create folders, templates, probes, logs, and summaries |
| `A2_ANALYZE` | Approved bounded analysis | Run documented scripts, create diagnostics, update logs |
| `A3_REVISE` | Approved bounded repair | Patch code or docs tied to an accepted issue, then validate |
| `A4_REVIEW_READY` | Agent can prepare for human review | Assemble evidence, memos, skeletons, and decision options |
| `A5_HUMAN_REQUIRED` | Human must choose before continuation | Stop after producing a concise decision packet |

Do not use autonomy levels to bypass project gates. `A2_ANALYZE` does not permit writing final prose. `A3_REVISE` does not permit changing the paper direction.

## Required State Fields

Every active project should keep these fields in canonical `project_state.md`; legacy equivalents require `qa/artifact_mapping.md` or a mapping table in `project_state.md`:
- autonomy level
- current gate
- gate status: `OPEN`, `PASS`, `PASS_WITH_GAPS`, `BLOCKED`, or `HUMAN_REQUIRED`
- allowed next actions
- forbidden next actions
- blocked reasons
- required validation
- last validation result
- human decision needed
- latest state probe path

Every current item in `next_actions.md` should state:
- whether automatic execution is allowed
- whether the action needs human approval
- validation command or check
- expected done artifact
- rollback or recovery path

## Phase Rules

### 0. Idea Screening And Co-Development

Goal:
- improve an idea with the human before creating a full project repo

Can auto-continue:
- fill gaps in the idea template using only user-provided facts and verified sources
- identify missing fields
- search and verify threat papers when web access is available
- run Step 1 through Step 8 of `idea_evaluation.md`
- propose pivots that keep the human's core topic
- create a second_brain research-idea page or `ideas/idea_evaluation.md`

Requires human:
- choosing the preferred idea among competing directions
- accepting a target-journal downgrade
- overriding a score below `7`
- approving a full project start
- approving a pivot that changes the core topic

Pass rule:
- project start is allowed only when final verdict is `PROCEED` or `PROCEED WITH CONDITIONS` with a score of at least `7`
- a score of `7-8` is the normal promotion band
- a score below `7` can move to Project Start only with explicit human override recorded in `decision_log.md` and `qa/waiver_log.md`

State updates:
- save the full idea history in `ideas/idea_evaluation.md` or `wiki/research-ideas/<idea_slug>.md`
- split final-verdict preconditions into `auto_checkable_preconditions` and `human_decision_preconditions`
- put automatic checks into `next_actions.md`
- put human decisions into `decision_log.md` only after the human accepts them

### 1. Project Start

Can auto-continue:
- create standard folders and empty state files
- add framework block to `README.md`
- record selected server, repo path, branch, tmux session, and environment
- copy the accepted idea gate summary into project files

Requires human:
- creating a full project after failed idea gate
- choosing between server placement options when capacity or repo freshness is ambiguous
- accepting nonstandard repo layout that affects future work

Pass rule:
- `README.md`, `project_state.md`, `decision_log.md`, `next_actions.md`, `source_context.md`, `research_log.md`, `question/main_question.md`, and `question/decisions.md` exist; legacy equivalents are mapped in `qa/artifact_mapping.md` or `project_state.md`
- `project_state.md` records current gate and autonomy level

### 2. Research Direction

Can auto-continue:
- summarize inferred question, claim, contribution, and should-not-claim boundary from existing documents
- mark direction status as `INFERRED`
- prepare decision options

Requires human:
- marking direction as `HUMAN_CONFIRMED`
- changing target claim, target journal, or should-not-claim boundary

Pass rule:
- direction status is `HUMAN_CONFIRMED`, or analysis proceeds only as exploratory with claim outputs marked provisional

### 3. Data And Method Setup

Can auto-continue:
- inspect data availability, schema, row counts, missing values, and paths
- create `docs/methods.md`, `data/README.md`, and variable notes
- run read-only probes

Requires human:
- accepting proprietary data use, external data transfer, or irreversible cleaning choices
- approving identifying assumptions when multiple plausible designs remain

Pass rule:
- project files document critical data, sample, method, and identification settings
- critical gaps block analysis; noncritical gaps remain in `next_actions.md`

### 4. Analysis Execution

Can auto-continue:
- run approved scripts in the selected server repo
- create run manifests, logs, diagnostics, and output artifacts
- run EDA probes and emit summary statistics when the current gate allows pre-pilot or pilot diagnostics
- check falsification conditions from `pilot/PILOT_PLAN.md`
- write compact findings to `pilot/PILOT_LOG.md`
- emit auto-feedback notes with EDA verdict, falsification result, artifact path, and next allowed action
- update `research_log.md` and `project_state.md`

Requires human:
- launching expensive or long risky runs when resource cost is unclear
- changing the research design to chase results
- treating exploratory output as final

Pass rule:
- each major run has command, environment, start/end time, exit status, outputs, and validation result

### 5. Pivot Review And Memory Sync

Can auto-continue:
- detect pivot triggers
- draft pivot memo
- mark outputs as current, superseded, or diagnostic
- update second_brain project memory after accepted work

Requires human:
- accepting a paper pivot
- splitting a project
- freezing an old direction
- changing the target audience or central claim

Pass rule:
- pivot status is `NO_PIVOT`, `MINOR_ADJUSTMENT`, `PIVOT_PENDING_HUMAN`, `PIVOT_ACCEPTED`, or `SPLIT_ACCEPTED`

Automatic pivot triggers:
- main estimate changes sign
- sample, data source, unit, or model family changes
- target claim no longer matches the main output
- main exhibit status resets from `FIX` to another label
- two viable paper directions coexist

### 6. Table And Figure Generation

Can auto-continue:
- generate table and figure packs
- create manifests
- run blindspot audit
- assign `DRAFT`, `AUTO_REVIEW_READY`, `REVISE`, or `GAP`

Requires human:
- assigning `FIX`
- dropping a central exhibit
- accepting a claim boundary that changes the paper direction

Pass rule:
- main exhibits are at least `AUTO_REVIEW_READY` before writing kickoff
- final prose may use only `FIX` exhibits

Allowed exhibit statuses:
- `DRAFT`
- `AUTO_REVIEW_READY`
- `NEEDS_HUMAN_FIX_DECISION`
- `FIX`
- `REVISE`
- `DROP`
- `ADD`
- `GAP`

### 7. Writing Kickoff

Can auto-continue:
- gather existing evidence
- create `PROVISIONAL_SKELETON`
- create exhibit memos
- mark missing answers as `GAP`
- prepare human decision packet

Requires human:
- accepting target claim
- assigning exhibit `FIX`
- accepting writing structure
- approving first final prose target

Pass rule:
- skeleton status is `HUMAN_ACCEPTED` before final paragraph drafting
- otherwise write only provisional notes with gaps

### 8. Paragraph-Level Co-Writing

Can auto-continue:
- draft placeholders or provisional section notes when evidence gaps are marked
- revise accepted paragraphs within existing claim strength
- run prose lint

Requires human:
- accepting final paragraphs
- moving from paragraph mode to full-section drafting
- changing voice profile or claim strength

Modes:
- `CONTROLLED_PARAGRAPH`: one paragraph at a time, default
- `PROVISIONAL_SECTION_DRAFT`: rough section draft with explicit gaps; not final prose

### 9. Review And Revision

Can auto-continue:
- run prose lint, source-context checks, exhibit consistency checks, and manuscript readiness summary
- patch mechanical issues that do not change claims

Requires human:
- accepting claim changes
- accepting unresolved limitations
- approving submission readiness

Pass rule:
- manuscript readiness records evidence, source, exhibit, method, prose, and replication status

### 10. Referee Audit And Repair

Can auto-continue:
- run referee audit
- create report
- draft patch plan
- patch author code only after switching back to the main project-agent role
- rerun affected checks

Requires human:
- accepting disputed concerns
- deferring major issues
- treating audit limitations as acceptable for submission

Repair loop:
1. referee report
2. patch plan
3. author or main agent patch
4. rerun affected checks
5. round-two audit or targeted verification

### 11. Submission

Can auto-continue:
- assemble checklists and draft packages
- verify file presence and reproducibility

Requires human:
- external submission
- email or portal upload
- final package approval

## State Probe

Before resuming an automated project session, create or update:

```text
handoff/project_status_probe.md
```

Use:

```text
04_templates/project_status_probe_template.md
```

Required fields:
- host
- repo path
- branch
- tmux session
- environment activation
- current gate
- autonomy level
- blocked reasons
- latest run manifest
- latest outputs
- latest handoff
- next allowed automatic action
- next human decision needed

## Guardrails

- Do not hide uncertainty to keep the automation moving.
- Do not convert `GAP` into assumptions without marking it.
- Do not promote provisional outputs into final prose.
- Do not create a full project from a weak idea only because the user is enthusiastic; co-develop and rescore first.
- Do not make external communications, submissions, deletions, or sensitive data transfers without explicit approval.
