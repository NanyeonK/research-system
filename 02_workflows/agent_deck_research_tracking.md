# Agent Deck Research Tracking Workflow

Updated: 2026-05-20

Purpose:
- make the research system a dashboard for what each active research agent is doing, which stage it is in, and how the work is progressing
- run early-stage research through Agent Deck while preserving full provenance in git, changelog files, and project state files
- adapt the useful protocols from `alejandroll10/idea-evaluation-pipeline` and `wanshuiyin/Auto-claude-code-research-in-sleep` without copying their runtime assumptions
- separate exploratory paper-idea projects from package-first research repos such as `macroforecast` and `eapctf`
- make first project launch, paper/analysis design, Review/Audit Gate, and Paper Writing human-heavy stages with explicit Yeonchan confirmation and Mac-local review packets when artifacts must be inspected

## Scope

Use this workflow for early-stage paper ideas where Yeonchan starts with a rough concept and wants an agent to help evaluate, pilot, refine, and eventually convert it into a paper project.

Do not use this workflow as the primary process for package-first research software projects. Package-first repos such as `macroforecast` and `eapctf` follow their own package/reproducibility process and may only borrow the status/changelog conventions when useful.

## Core operating rule

One project has one active owning agent at a time.

- The owner may be Claude Code or Codex through Agent Deck.
- Do not run Claude Code and Codex simultaneously inside the same research repo by default.
- Switching tools requires a handoff file and controller approval.
- Different projects may each have their own owner agent, but same-project parallelism is not the default academic workflow.

## External references and what we adopt

### idea-evaluation-pipeline

Adopt:
- rough idea intake template
- sequential idea evaluation, critique review, pivot, literature threat search, citation verification, final verdict
- score gate around 7/10 before promotion
- maximum bounded pivot loop before killing or shelving the idea
- requirement that closest papers and threat papers have verifiable URLs

Adapt:
- outputs become project-tracked Markdown under `idea-stage/`
- stage transitions are reflected in project status files and git commits
- the final verdict becomes a promotion gate into pilot work, not automatic project start

Reject / do not import directly:
- model-specific assumptions
- multiple agents per idea inside one project
- unverified literature claims

### Auto-claude-code-research-in-sleep / ARIS

Adopt:
- Markdown-first research harness
- `Pipeline Status` dashboard in the project control file
- focused `research_contract.md` for the current idea
- experiment plan / tracker / log split
- findings log for non-obvious discoveries and decisions
- manifest of generated artifacts
- adversarial review/audit gates before turning results into claims
- session recovery order: status -> contract -> recent findings -> experiment log

Adapt:
- Agent Deck is the execution surface; Mac/Hermes is the controller
- project state lives in git-tracked files, not hidden chat memory
- review loops must respect Yeonchan's paper-system gates and writing voice rules

Reject / defer:
- autonomous overnight paper writing without human story lock
- any step that creates unsupported claims, fabricated citations, or unreviewed manuscript prose
- broad platform/runtime installation unless separately approved

## Standard project layout

A tracked exploratory research project should use this minimal layout:

```text
project/
├── AGENTS.md or CLAUDE.md              # agent instructions + Pipeline Status
├── AGENT_STATUS.md                     # human-readable owner/status dashboard
├── CHANGELOG.md                        # chronological project changes
├── MANIFEST.md                         # generated artifact index
├── decision_log.md                     # accepted decisions and rationale
├── findings.md                         # lightweight discoveries, anomalies, debug notes
├── idea-stage/
│   ├── idea_input.md                   # Yeonchan rough idea normalized into template
│   ├── eval_*.md                       # idea evaluations
│   ├── review_*.md                     # critique reviews
│   ├── pivot_*.md                      # pivot attempts
│   ├── lit_review_*.md                 # threat literature search
│   ├── verify_lit_review_*.md          # citation verification
│   ├── final_verdict_*.md              # final score and go/no-go
│   └── docs/
│       └── research_contract.md        # focused contract for the active idea
├── pilot/
│   ├── PILOT_PLAN.md                   # data/feasibility pilot plan
│   ├── PILOT_TRACKER.md                # pilot run status
│   ├── PILOT_LOG.md                    # completed pilot results with commands
│   ├── results/                        # pilot tables/figures/metrics before promotion
│   ├── artifacts/                      # small pilot outputs only
│   └── archive/                        # superseded pilot versions
├── refine-logs/
│   ├── EXPERIMENT_PLAN.md              # post-pilot experiment design
│   ├── EXPERIMENT_TRACKER.md           # TODO/RUNNING/DONE status
│   ├── EXPERIMENT_LOG.md               # full experiment records
│   └── PIPELINE_SUMMARY.md             # compact stage summary
└── review-stage/
    ├── AUTO_REVIEW.md                  # adversarial review log
    └── REVIEW_STATE.json               # resumable review status
```

For already-running repos, do not restructure aggressively. Add only the minimum files needed for status, changelog, and stage recovery.

## Scope split: exploratory research projects vs package-managed research repos

This workflow is the default normalization process for exploratory empirical/research-paper projects: idea, pilot, experiment, review/audit, writing, and package/publish transition.

Package-managed research repos are exceptions. Repos such as `macroforecast` and `eapctf` are package/reproducibility/codebase-management projects first. They should not be forced through idea/pilot/research-system folder restructuring as the primary process.

Package-managed repos may still borrow lightweight conventions when useful:
- `CHANGELOG.md`
- `MANIFEST.md`
- `AGENT_STATUS.md`
- review packets under `/Users/nanyeon/Documents/research_review_artifacts/`
- archive/version discipline for generated artifacts
- conductor-mediated launch/session hygiene

But their controlling process remains package-first: API surface, tests, reproducibility runners, docs, release/package state, and benchmark gates explicitly approved by Yeonchan.

All non-package active research sessions should be normalized into this research-system process unless Yeonchan marks the project package-managed or archival.

## Human-heavy gates and divergence handling

The research system has four human-heavy stages. The conductor and owner agents may prepare artifacts, but they must not silently pass these gates.

1. First project launch
   - Yeonchan must confirm that the project should enter the research-system process.
   - Required before launch: project classification, source-of-truth server/path, owner tool, scope, initial idea/claim, expected stage, and no-conflict/dirty-tree status.
   - Package-managed repos (`macroforecast`, `eapctf`) do not enter this workflow unless Yeonchan explicitly overrides.

2. Paper design / analysis design confirmation
   - Before full experiment execution, broad analysis, or result production, Yeonchan must confirm the design packet.
   - Required packet: research question, mechanism, data sources, sample/panel, identification or forecasting target, main estimand/target, baseline specification, controls/fixed effects, table/figure plan, falsification criteria, and expected claim boundary.
   - If the design changes from the initial idea or from a previously accepted design, stop and produce a divergence memo before running the new design.

3. Review/Audit Gate
   - Yeonchan must inspect claim/audit outputs before results become paper claims.
   - Required: Mac-local review packet, result-to-claim map, table/figure traceability, leakage/spec-drift/raw-vs-derived audit, accepted/rejected claim list.

4. Paper Writing
   - Yeonchan must confirm story/exhibit lock before prose drafting.
   - Required: story lock, skeleton, exhibit map, safe/forbidden claims, unresolved gaps, voice rules, and project-local capture of accepted revisions.

Divergence rule:
- If empirical feasibility, analysis design, identification story, forecast target, data availability, table/figure evidence, or results differ from the initial idea or Yeonchan-approved design, do not silently pivot.
- Stop at the current safe point and write a divergence memo under `decision_log.md` or `review-stage/`.
- The memo must state: original accepted idea/design, observed divergence, evidence/artifact path, affected claims/exhibits, options, and recommended decision.
- Allowed options are: continue original design, revise design, pivot project, pause, or kill.
- No silent pivot: only Yeonchan can approve the new direction unless a prior written project contract explicitly allowed that class of change.

## Agent Deck launch and session validity

New academic owner sessions should normally be created through the research conductor/controller workflow.

Rules:
- conductor first reconciles registry, existing sessions, source-of-truth server/path, one-owner status, and dirty-tree status
- launch from the project root only: `/home/nanyeon99/project/<repo>`
- use explicit tool metadata: `-c claude` or `-c codex`
- default owner title: `<project_key>-owner`; reviewer titles must include `<project_key>-reviewer-*`
- raw `shell` sessions are allowed only for explicit shell work, not project ownership
- Agent Deck sessions with `tool=shell` or `path=/home/nanyeon99` are legacy/misregistered until reconciled
- legacy/misregistered sessions may be inspected read-only for handoff/status, but should not perform new project writes without a relaunch decision

Canonical launch shape:

```bash
cd /home/nanyeon99/project/<repo>
agent-deck launch . -t <project_key>-owner -g academic-owner -c <claude|codex> -m "<owner contract>"
```

## Mac-local human review shelf

Review/Audit Gate, Writing Transition, and publish/package checks require substantial Yeonchan inspection. Agents must not force Yeonchan to browse full server repos for review.

Use this Mac-local folder as the human-facing review shelf:

```text
/Users/nanyeon/Documents/research_review_artifacts/
├── server1/<project_key>/
├── server2/<project_key>/
├── server3/<project_key>/
├── _review_index.md
└── REVIEW_PACKET_TEMPLATE.md
```

Rules:
- copy only the artifacts Yeonchan needs to inspect; never sync a full repo, raw dataset, cache, checkpoint, or secret-bearing file
- preserve provenance in the review packet: source server, repo path, source git commit or dirty-tree note, source artifact path, local artifact path, and timestamp KST
- every copied artifact must be indexed in `_review_index.md`
- Review/Audit Gate and Writing Transition cannot exit until the Mac-local packet exists and Yeonchan-facing decisions are explicit
- table and figure review copies must satisfy `table-builder` and `figure-builder` metadata requirements before they are shown as candidate exhibits

Suggested artifact names:
- `YYYYMMDD-HHMM_review_audit_packet.md`
- `YYYYMMDD-HHMM_result_to_claim_map.md`
- `YYYYMMDD-HHMM_table_figure_map.md`
- `YYYYMMDD-HHMM_story_skeleton.pdf`
- `YYYYMMDD-HHMM_publish_readiness_packet.md`

## Active artifact and archive discipline

Active folders must contain only current artifacts or files explicitly marked active in `MANIFEST.md`.

Rules:
- no stale previous-result files beside current tables, figures, model outputs, manuscripts, review packets, or submission files
- every replacement first archives the old active artifact under `archive/YYYY-MM-DD_<stage>_<reason>/`
- every archive move creates `ARCHIVE_MANIFEST.md` and `superseded_by.md`
- `CHANGELOG.md` records the archive move and the new active artifact
- `MANIFEST.md` records current artifact status and archive pointer
- pilot versions remain under `pilot/results/` or `pilot/archive/` until promoted
- raw data, caches, checkpoints, and huge derived files are not archived inside the repo unless explicitly justified; record external path/checksum/retention decision instead

## Required Pipeline Status block

The project control file must include this block near the top:

```yaml
## Pipeline Status
project_key: ""
repo_path: ""
source_of_truth: "serverN:/home/nanyeon99/project/<repo>"
agent_deck_session: ""
owner_agent: "claude-code | codex | none"
stage: "idea_intake | idea_evaluation | pilot | research_contract | experiment_plan | experiment_run | review_audit | result_to_claim | writing_kickoff | paper_writing | paused | killed"
idea: "one sentence current idea"
contract: "idea-stage/docs/research_contract.md"
branch: ""
last_commit: ""
dirty_tree: "clean | dirty:<N> | unknown"
current_task: ""
active_tasks:
  - ""
last_artifact: ""
last_verification: ""
last_updated_kst: "YYYY-MM-DD HH:MM"
next: "one concrete next action"
blocked_on: ""
```

This block is the first thing a new agent reads and the first thing the controller checks.

## Stage model

### 0. Rough idea intake

Input: Yeonchan's rough idea.

Agent action:
- normalize the idea into `idea-stage/idea_input.md`
- require research question, mechanism, data, identification or forecast target, closest papers, and why the field should care
- if closest papers are missing, mark `[GAP: closest papers]` rather than inventing them

Exit gate:
- `idea-stage/idea_input.md` exists
- `CHANGELOG.md` records the intake
- `Pipeline Status.stage = idea_evaluation`

### 1. Idea evaluation gate

Use the idea-evaluation-pipeline logic:
1. evaluate idea
2. review evaluation fairness
3. pivot if score < 7
4. evaluate pivot
5. threat literature search
6. verify every citation/URL
7. final verdict
8. review final verdict

Exit gates:
- final score and verdict are written
- threat literature is verified; unverifiable papers are removed or flagged
- if score is below threshold after bounded pivots, set stage to `killed` or `paused`
- if score passes and Yeonchan agrees, set stage to `pilot`

### 2. Pilot gate

Purpose: test whether the idea is feasible enough to deserve a real project.

Pilot must be small:
- minimal data access test
- variable construction smoke test
- one baseline table/figure/regression/forecast if feasible
- explicit failure modes

Required files:
- `pilot/PILOT_PLAN.md`
- `pilot/PILOT_TRACKER.md`
- `pilot/PILOT_LOG.md`
- `pilot/results/`
- `pilot/artifacts/`
- `pilot/archive/`

Pilot storage rules:
- all pilot execution and pilot results stay under `pilot/` until explicitly promoted
- pilot tables, figures, metrics, and compact machine-readable outputs go to `pilot/results/`
- pilot-only logs, temporary models, and diagnostics go to `pilot/artifacts/`
- superseded pilot runs move to `pilot/archive/YYYY-MM-DD_<reason>/` with an `ARCHIVE_MANIFEST.md`
- broad-analysis `output/` folders must not contain stale pilot versions
- when a pilot result is promoted into `output/`, archive any previous active output version first and update `MANIFEST.md`

Before broad analysis starts, the pilot must produce a pre-analysis story/exhibit packet:
- one-sentence provisional story
- paper skeleton with section jobs, not prose
- table/figure map using `table-builder` and `figure-builder` requirements
- planned exhibit role: spine, setup, identification, mechanism, robustness, appendix detail, or drop
- source script/data path planned for each exhibit
- what each table/figure must show for the project to survive

Exit gates:
- pilot commands and outputs are recorded
- result is classified as `promote`, `pivot`, `pause`, or `kill`
- story, skeleton, and table/figure map are accepted or explicitly deferred by Yeonchan
- controller/human accepts promotion before full project execution

### 3. Research contract

When the pilot looks promising, write `idea-stage/docs/research_contract.md`.

The contract must include:
- claim in one sentence
- mechanism
- identification / forecasting design
- data objects and source paths
- main estimand or target
- baseline result from pilot
- closest threats
- proposed exhibits
- next executable tasks
- what would falsify the project

Exit gate:
- status points to the contract
- contract is committed or explicitly recorded as dirty live work

### 4. Experiment plan and execution

Use ARIS-style split:
- `EXPERIMENT_PLAN.md`: design and run order
- `EXPERIMENT_TRACKER.md`: execution state
- `EXPERIMENT_LOG.md`: completed run records
- `findings.md`: non-obvious discoveries and decisions

Every run record must include:
- run id
- command
- host/server
- git commit or dirty-tree note
- input data snapshot/path
- output artifact path
- result summary
- failure or caveat

### 5. Review/audit gate

Before results become claims:
- run an adversarial result audit
- check leakage/spec drift/raw-vs-derived ambiguity
- verify tables/figures map to scripts and data
- write review to `review-stage/AUTO_REVIEW.md`

This is a human-heavy gate. Yeonchan must be able to inspect the review packet from the Mac. The owner agent prepares the packet; independent reviewer agents may critique it; the conductor/controller synthesizes status but does not decide claims alone.

Required reviewer structure:
- owner agent: produces the primary review packet and source artifact list
- independent reviewer agent 1: checks leakage, spec drift, data provenance, and raw-vs-derived ambiguity
- independent reviewer agent 2: checks result-to-claim validity, table/figure traceability, and unsupported interpretation
- controller/conductor: verifies that review outputs exist, copies Yeonchan-facing artifacts to the Mac review shelf, and escalates decisions

Reviewer agents are allowed here as an exception to the single-owner production rule because they are read-only reviewers, not concurrent project owners. They must not edit project code, change analysis, or write manuscript prose unless Yeonchan explicitly approves a separate owner handoff.

Mac review packet requirement:
- create or update `/Users/nanyeon/Documents/research_review_artifacts/<server>/<project_key>/`
- copy only `AUTO_REVIEW.md`, `REVIEW_STATE.json`, result-to-claim maps, candidate table/figure review artifacts, story/skeleton review PDFs/Markdown, and concise source summaries needed for inspection
- append copied artifacts to `/Users/nanyeon/Documents/research_review_artifacts/_review_index.md`

Exit gate:
- accepted claims are listed separately from rejected/unsupported claims
- unsupported claims cannot enter writing kickoff
- independent reviewer-agent findings are recorded or explicitly waived by Yeonchan
- Mac-local review packet exists and points to all human-facing artifacts
- Yeonchan accepts the result-to-claim map before writing transition

### 6. Writing transition

Writing starts only after story/exhibit lock gates in the writing system.

Rules:
- no autonomous full-paper drafting by default
- paragraph co-writing only after accepted skeleton/exhibit decisions
- table/figure interpretations must reference machine-readable artifacts and source scripts
- load and apply Yeonchan voice rules before drafting: `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/writing_execution_card.md` and `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/voice_yeonchan.md`
- use `table-builder` and `figure-builder` for exhibit shells, captions, notes, and validation before interpreting results in prose
- expect substantial Yeonchan revision; accepted revisions must be captured as project-local writing notes and, when stable/repeated, routed through the voice update workflow so future projects inherit the rule
- do not promote a one-off edit into global voice unless it is repeated, explicitly accepted, or tied to a manuscript milestone

Writing transition required artifacts:
- story lock
- paper skeleton
- exhibit/table/figure map
- writing handoff listing safe claims, forbidden claims, source tables/figures, and unresolved gaps
- Mac-local packet under `/Users/nanyeon/Documents/research_review_artifacts/<server>/<project_key>/`

## Autonomous continuation after normalization

Once a non-package project has been patched into the research-system format, the conductor may continue automatically only inside non-human-heavy gates.

Allowed automatic work:
- keep `AGENT_STATUS.md`, `CHANGELOG.md`, `MANIFEST.md`, `decision_log.md`, and `findings.md` current
- preserve handoffs from legacy sessions
- produce design packets, literature packets, review packets, divergence memos, and owner relaunch proposals
- run read-only audits and read-only reviewer feedback agents
- run small deterministic smoke checks only when the project contract already allows them and they do not change the accepted design
- apply ARIS-style pipeline status, experiment plan/tracker/log, findings log, and recovery-order maintenance
- apply ZeroPaper-style stable IDs, versioned process logs, stage-transition records, gate verdicts, scorer/status trajectory, and artifact catalog updates

Disallowed without Yeonchan approval:
- crossing a human-heavy gate
- changing accepted design, story, sample, identification, forecast target, or claim boundary
- archiving/moving/deleting active outputs
- committing/pushing
- owner relaunch into edit-mode
- broad analysis reruns, benchmark-scale jobs, prose drafting, or result-to-claim promotion

When an automatic step completes, the conductor must update the project logs and its own Mac review inventory. If it reaches a human-heavy gate, it stops with `NEED:` and presents the decision packet.

## Literature and graphify protocol

Literature work should start from Yeonchan's second_brain before external requests.

Order:
1. Search existing second_brain wiki/source notes for project-specific literature, mechanisms, data sources, and closest/threat papers.
2. If a relevant second_brain subcorpus already has `graphify-out/GRAPH_REPORT.md` or `graphify-out/graph.json`, query/read that graph before raw-file review.
3. If no graph exists but the bounded corpus is small enough, run `graphify` on the project/topic corpus and write the graph outputs beside that corpus, not inside active analysis outputs.
4. For any Graphify/source-deep-reading/PDF-heavy step that needs second_brain raw PDFs or textbook chapter splits, use on-demand hydration: `/Users/nanyeon/bin/second_brain_hydrate.py hydrate <raw/path.pdf>` into `/Users/nanyeon/second_brain_exec/raw_cache`, then read/graphify the local hydrated path. Do not whole-corpus pin Synology Drive and do not process raw PDFs directly from File Provider placeholders.
5. If hydration is blocked, label the source as `needs Yeonchan/source materialization` or `locally missing`; do not fabricate missing papers or silently substitute weak analogs.
6. Use graph evidence to produce literature packets: closest papers, threat papers, mechanisms, identification/forecasting precedent, and source gaps.
7. If useful or necessary literature is absent from second_brain and cannot be retrieved from existing local sources, ask Yeonchan for it explicitly.

Literature packets must distinguish:
- already in second_brain / graph-supported
- locally missing but externally discoverable
- needs Yeonchan-provided PDF/source
- not found / unresolved gap

## Git and changelog discipline

All meaningful progress must be traceable through both git and project logs.

Required after each stage transition:
1. update `Pipeline Status`
2. append `CHANGELOG.md`
3. append `MANIFEST.md` for new artifacts
4. append `decision_log.md` for accepted decisions
5. commit if the work is stable enough, or record why it remains dirty

Suggested commit prefixes:
- `idea:` rough intake/evaluation/pivot outputs
- `pilot:` pilot plan/log/artifacts
- `contract:` research contract changes
- `exp:` experiment plan/tracker/log updates
- `audit:` review/audit outputs
- `claim:` result-to-claim mapping
- `write:` writing-system outputs
- `status:` Pipeline Status / dashboard updates

Dirty tree rule:
- an owner agent may continue with a dirty tree only if `Pipeline Status.dirty_tree` and `CHANGELOG.md` explain what is dirty and why
- before assigning a new owner, create a handoff and either commit, stash, archive, or explicitly preserve the dirty tree

## Agent Deck launch gate

Before launching an owner agent:
1. validate project registry
2. confirm source-of-truth server/path
3. confirm the project is not package-first unless explicitly using only the tracking convention
4. read the project walnut/context if available
5. inspect git branch, dirty count, and recent commit
6. write or update the project owner contract
7. launch one Agent Deck owner session only

If registry blocks launch, update/normalize the registry first or run a read-only status audit only.

## Owner handoff

Before switching owner agents or ending a stage, write a handoff artifact under:

`docs/agent_handoffs/YYYYMMDD-HHMM-<from>-to-<to>.md`

The handoff must list:
- current stage
- last commit and dirty status
- files changed
- commands run
- artifacts created
- verification status
- unresolved risks
- exact next action

## Controller dashboard meaning

The research system dashboard should answer, for every active exploratory project:
- Which agent owns it?
- Which Agent Deck session is active?
- Which stage is it in?
- What file is the current contract?
- What was the last artifact?
- What verification/audit passed last?
- What is blocked?
- What is the next concrete action?
- Is the git tree clean, intentionally dirty, or unknown?

This is the system's purpose: not agent parallelism, but recoverable research progress visibility.
