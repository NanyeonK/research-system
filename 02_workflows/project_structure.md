# Research Project Structure Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Engine skills:
- `/research-wiki init` — optional. May seed a per-project wiki at `wiki/` inside the project repo with ARIS's four-entity model (paper / idea / experiment / claim). The global ground truth remains `~/second_brain/wiki/` and is updated through `02_workflows/wiki_intake_continuous_upgrade.md`.
- `/research-pipeline "direction"` — full ML lifecycle scaffold. Allowed for ML/CS projects, not for `ryu_fin_lab` empirical-econ projects.

Binding rules:
- Server-first project root `/home/nanyeon99/project/<repo_name>` and our standard folder layout (`analysis/`, `paper/`, `correspondence/`, `output/`, `code/`, `data/`, `handoff/`) is authoritative.
- ARIS artifact paths (`idea-stage/`, `refine-logs/`, `review-stage/`, `figures/`) are allowed as additional subfolders only when the project explicitly opts in. Otherwise, copy ARIS outputs into our paths per `aris_bridge.md` § Artifact Translation.
- Project `README.md` must record Paper Project Framework recognition before major work; ARIS adoption inside the project is recorded in the same place.

Purpose:
- start research projects with a predictable folder structure
- keep analysis, tables, figures, writing, handoffs, and submissions traceable
- reduce later cleanup when writing kickoff begins
- make Mac/server work reproducible across Codex, Claude Code, and Hermes

## Scope

Use this workflow when:
- starting a new research project
- moving an ad hoc analysis into a project repo
- preparing a project for writing kickoff
- syncing or resuming a project on server1, server2, or server3
- onboarding an already-running project into the Paper Project Framework

Server-related placement follows `/Users/nanyeon/AGENTS.md`.
Direction changes, second_brain project memory, optional project-local wiki, and LLM-wiki promotion follow `02_workflows/research_project_governance.md`.
Early idea screening follows `02_workflows/idea_evaluation.md`.
Phase-by-phase folder creation and artifact placement follow `02_workflows/lifecycle_repo_organization.md`.
Automatic phase progression follows `02_workflows/autonomous_progression.md`.
Workflow modules and weekly wiki-derived upgrades follow `02_workflows/research_workflow_modules.md` and `02_workflows/wiki_intake_continuous_upgrade.md`.

Canonical server path:
- `/home/nanyeon99/project/<repo_name>`

Default tmux session:
- `<repo_name>`

Do not scatter active repos outside `~/project` unless the project README documents the exception.

## Server-First Project Work

Default:
- perform active project work directly on server1, server2, or server3
- use `/home/nanyeon99/project/<repo_name>` as the project working copy
- choose the server by capacity and existing repo freshness, following `/Users/nanyeon/AGENTS.md`

Applies to:
- code edits
- data processing and analysis
- long-running jobs
- table and figure generation
- project-local manuscript files under `paper/`
- submission and replication packages
- project-local handoff and logs

Mac exceptions:
- global Paper Project Framework files under the Synology Drive `research_paper_system/` folder
- Codex/Hermes/Claude global instructions and skills
- canonical second_brain wiki and Walnut memory writes
- human review of artifacts
- explicitly local-only requests

If a project exists only on the Mac, first pick server1, server2, or server3, clone or sync the repo into `/home/nanyeon99/project/<repo_name>`, then work there.

## Core Rule

Every project should be able to answer five questions from files, not memory:
1. What is the research question?
2. Which data, scripts, and settings generated each result?
3. Which tables and figures are writing-ready?
4. Which pivots or direction changes superseded earlier outputs?
5. Which manuscript or submission artifact is current?

Every research-paper project should also recognize the shared Paper Project Framework in `README.md`.

Before creating a full project from an idea, run idea co-development and the idea gate in `02_workflows/idea_evaluation.md`. Create the project only after the final verdict permits promotion or a human override appears in `decision_log.md` and `qa/waiver_log.md`.

Every active project should maintain canonical state files. Legacy or documented equivalents require `qa/artifact_mapping.md` or a mapping table in `project_state.md`:
- `project_state.md`
- `decision_log.md`
- `next_actions.md`
- `source_context.md`

For already-running projects, do not create duplicates when equivalent files already exist. Record the mapping in `README.md` or `project_state.md`.

Required `README.md` block:

```markdown
## Paper Project Framework

This project follows the shared Paper Project Framework:
`/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/`

Current framework phase:
- [ ] Idea screening
- [ ] Project start
- [ ] Research direction
- [ ] Data and method setup
- [ ] Analysis execution
- [ ] Pivot review and memory sync
- [ ] Table and figure generation
- [ ] Writing kickoff
- [ ] Paragraph-level co-writing
- [ ] Review and revision
- [ ] Referee audit
- [ ] Submission
- [ ] Post-submission / publication
```

## Standard Repo Layout

Default layout:

```text
<repo_name>/
  README.md
  project_state.md
  decision_log.md
  next_actions.md
  source_context.md
  CHANGELOG.md
  MANIFEST.md
  research_log.md
  ideas/
    idea_evaluation.md
    literature_map.md
    evaluation/
  question/
    main_question.md
    decisions.md
    pivots/
  plans/
  handoff/
  progress_logs/
  pilot/
    PILOT_PLAN.md
    PILOT_TRACKER.md
    PILOT_LOG.md
    results/
    artifacts/
    archive/
  data/
    README.md
    raw/
    interim/
    processed/
  src/
  scripts/
  analysis/
  output/
    tables/
    figures/
    models/
    logs/
    diagnostics/
      referee2/
  paper/
    main.tex
    main_skeleton.tex
    skeleton_preview.pdf
    first_deep_interview.md
    writing_kickoff_decisions.md
    section_paragraph_map.md
    exhibit_memos/
    sections/
  docs/
    methods.md
    data_construction.md
    variable_definitions.md
  documents/
  decks/
  correspondence/
    referee2/
  code/
    replication/
  submit/
  replication_package/
  archive/
    YYYY-MM-DD_<stage>_<reason>/
      ARCHIVE_MANIFEST.md
      superseded_by.md
      files/
```

Use the repo's existing conventions when they are already coherent, but add missing equivalents instead of creating parallel hidden structures. For new projects, create folders phase-by-phase using `02_workflows/lifecycle_repo_organization.md`, not as a full empty tree on day one.

MixtapeTools compatibility mapping:
- `progress_logs/` can map to `research_log.md` plus `handoff/`
- `documents/` can map to `docs/`, `source_context.md`, or a project-specific literature folder
- `decks/` should hold research and collaborator decks when decks influence analysis, writing, or review decisions
- language-specific `code/R`, `code/python`, and `code/stata` can map to `src/`, `scripts/`, or `code/replication/` as long as the project documents the mapping

For already-running projects:
- do not move files only to match this layout
- document existing equivalent paths in `README.md`
- add missing state files before changing analysis code
- use `research_project_governance.md` to choose onboarding level

## Required Files

`README.md`:
- one-paragraph project summary
- Paper Project Framework recognition block
- current framework phase
- current status
- selected server host and canonical server path
- environment setup command
- main analysis commands
- current manuscript path
- unusual paths, ports, env vars, or external dependencies
- mapping for `project_state.md`, `decision_log.md`, `next_actions.md`, and `source_context.md` if the project uses equivalent paths

`ideas/idea_evaluation.md`:
- initial idea submission or summary
- link to `ideas/literature_map.md` and second_brain research-idea note
- closest three threat papers and URLs
- evaluation, review, pivot, threat-literature search, verification, and final verdict summary
- final gate decision and preconditions for project start
- link to second_brain research-idea page when the evaluation started outside the repo

`ideas/literature_map.md`:
- second_brain / Graphify search summary before external search
- explicit gap list after second_brain search
- targeted OpenAlex, Semantic Scholar, Crossref, RePEc, NBER, SSRN, arXiv, CEPR, publisher, or Google Scholar searches used only for missing pieces
- direct threats, adjacent communities, mechanism/data/method clusters, and verification status
- candidate papers to add/read with evidence tier and next action

`project_state.md`:
- current phase
- autonomy level, active gate, status, allowed next actions, blocked reasons, and human decision needed
- selected server, canonical path, branch, tmux session, and environment
- current source of truth for question, manuscript, outputs, and diagnostics
- active claim and claim boundary
- current evidence status
- open risks and next required gate

`decision_log.md`:
- accepted decisions only
- date, scope, evidence/source, human confirmation, affected files, and status
- superseded decisions linked to pivot memos or archive paths

`next_actions.md`:
- concrete next actions
- automatic execution flag, human-approval flag, validation check, done artifact, and recovery path
- priority, reason, owner, required context, blockers, and done condition
- parking lot separated from current gate

`CHANGELOG.md`:
- authoritative human-readable project-change ledger paired with git tree/commits
- automatically mirrored to second_brain `04_Ventures/<project-or-walnut>/CHANGELOG.md` by `02_workflows/repo_changelog_second_brain_sync.md`
- chronological project-change ledger for human and agent continuity
- every meaningful stage transition, agent handoff, result refresh, exhibit status change, archive move, and publish/package action
- date/time in KST, actor/tool, server/path, branch/commit or dirty-tree note, changed artifact paths, verification result, and next human decision if any
- do not replace `research_log.md`: changelog is compact state-change ledger; research log can be longer narrative/run notes
- do not manually duplicate routine changelog entries into second_brain; edit repo `CHANGELOG.md` and let the sync job mirror it

`MANIFEST.md`:
- current artifact inventory and status map
- identifies active vs superseded tables, figures, models, logs, review packets, manuscripts, and submission files
- records version, source script, source data, output path, generated timestamp, verification status, and archive pointer if superseded
- must be updated before writing kickoff, Review/Audit Gate, package/publish, and any archive move

`source_context.md`:
- source map for cited papers, datasets, code, and workflow sources
- evidence grade for sources
- what each citation supports and does not support
- workflow sources separated from manuscript evidence

`research_log.md`:
- dated run notes
- major decisions
- model or sample changes
- table and figure regeneration notes
- blindspot audit summaries
- referee audit round summaries

`question/main_question.md`:
- research question
- target claim
- intended contribution
- what the paper should not claim

`question/decisions.md`:
- human instructions that affect research direction
- accepted/rejected analysis branches
- target journal or audience decisions

`question/pivots/`:
- pivot memos when the target claim, sample, method, interpretation, or audience changes
- each major pivot should follow `02_workflows/research_project_governance.md`

Optional repo-local `wiki/`:
- create only when the project needs repo-contained memory
- second_brain is the default project memory layer
- if created, keep concepts, sources, mechanisms, exhibit interpretations, and export candidates here
- provisional by default; shared LLM-wiki promotion must be deliberate

Optional layout:

```text
wiki/
  README.md
  project_index.md
  claims.md
  concepts/
  sources/
  methods/
  exhibits/
  export/
    llm_wiki_candidates.md
```

`handoff/`:
- dated handoff files
- latest state for another agent or future session
- include current host, path, branch, environment, running jobs, and next step

`data/README.md`:
- raw data source
- access requirements
- data version
- preprocessing scripts
- files intentionally not committed or not synced

`documents/` or documented equivalent:
- source PDFs, referee letters, data documentation, and external documents that belong with the project
- long source PDFs should use `02_workflows/source_deep_reading.md` before their claims enter `source_context.md`

`decks/` or documented equivalent:
- seminar, conference, collaborator, teaching, and referee-audit decks
- deck outputs should follow `02_workflows/presentation_deck_workflow.md`

`docs/methods.md`:
- model design
- sample filters
- variable construction
- controls, fixed effects, standard errors, clustering
- rolling windows, horizons, thresholds, hyperparameters, seeds

## Analysis And Output Rules

Analysis code:
- keep reusable importable code in `src/`
- keep executable pipelines, runners, orchestration scripts, and one-off regeneration commands in `scripts/`
- keep exploratory notebooks, scratch checks, model-selection probes, diagnostics, and analysis notebooks in `analysis/`
- promote repeated notebook logic into `scripts/` before writing or review
- promote reusable functions/classes from `scripts/` or `analysis/` into `src/` once they are used by more than one runner, table, figure, or test
- `src/` should not contain project-specific ad hoc shelling, dated run constants, or notebook-only experiment branches
- `scripts/` should be runnable from the repo root and should write outputs only into documented `output/`, `pilot/`, or `archive/` paths
- `analysis/` outputs are provisional unless promoted into `output/` with a manifest entry

Pilot execution and results:
- pilot work lives under `pilot/`, not mixed into final `output/`
- `pilot/PILOT_PLAN.md` records the pilot question, minimal sample, commands, pass/fail criteria, and falsification conditions
- `pilot/PILOT_TRACKER.md` records each run, status, source script, data slice, and result path
- `pilot/PILOT_LOG.md` records dated interpretation and decisions
- `pilot/results/` holds pilot tables, figures, metrics, and compact machine-readable outputs
- `pilot/artifacts/` holds pilot-only logs, temporary model outputs, and diagnostic files worth keeping
- `pilot/archive/` uses the same versioned archive rules as the repo root for superseded pilot runs
- no broad analysis may start until the promoted pilot result has a story, paper skeleton, table/figure map, exhibit roles, and falsification criteria

Outputs:
- generated tables go to `output/tables/`
- generated figures go to `output/figures/`
- model artifacts go to `output/models/`
- run logs go to `output/logs/`
- diagnostics and QA artifacts go to `output/diagnostics/`

Every publishable table should have:
- machine-readable data
- generated `.tex`
- manifest
- generation script
- status from writing kickoff when writing begins

Every publishable figure should have:
- generated image or vector file
- machine-readable source data when feasible
- generation script
- note/caption source
- status from writing kickoff when writing begins

After major analysis batches:
- run pivot review using `02_workflows/research_project_governance.md`
- update `question/pivots/` if the direction changed
- update second_brain project memory
- update optional repo-local `wiki/` only if it exists
- reset affected table/figure statuses before writing kickoff

## Paper Folder Rules

`paper/` owns writing artifacts.

Before writing kickoff:
- `paper/main.tex` may be absent or rough
- the fixed first-round form creates `paper/first_deep_interview.md` and records gate results
- the kickoff workflow creates `paper/main_skeleton.tex` and `.pdf`
- `paper/writing_kickoff_decisions.md` records table/figure decisions
- `paper/exhibit_memos/` records one fixed exhibit interview form per table or figure, including evidence grade and FIX eligibility

After writing kickoff:
- paragraph-level co-writing uses the accepted skeleton
- only `FIX` exhibits are final prose evidence
- `REVISE`, `ADD`, and `GAP` exhibits must not be cited as final results

Do not use a Word file, PDF export, or manually edited table as the source of truth.

## Submission And Archive Rules

`submit/`:
- journal-specific submission files
- cover letters
- response letters
- final exported DOCX/PDF packages
- dated subfolders when useful

`replication_package/`:
- clean package assembled near submission or publication
- should not be the only place where active analysis exists

`archive/`:
- obsolete branches, superseded outputs, frozen old states, and previous result versions
- do not hide active results here
- archive every replaced result version before writing a new version into an active output path
- previous result files must not remain beside current active files in `output/tables/`, `output/figures/`, `output/models/`, `paper/`, `submit/`, or `replication_package/` unless `MANIFEST.md` marks them active
- use versioned archive subfolders:

```text
archive/
  YYYY-MM-DD_<stage>_<reason>/
    ARCHIVE_MANIFEST.md
    superseded_by.md
    files/
      output/
      paper/
      docs/
      logs/
```

Archive manifest requirements:
- timestamp in KST
- actor/tool
- source server, repo path, branch, and commit
- dirty-tree note if archived files were uncommitted
- original file paths
- archive file paths
- reason for archive
- superseding artifact paths or `none`
- regeneration command or explanation why not reproducible
- related `decision_log.md`, `CHANGELOG.md`, `MANIFEST.md`, and review-packet entries

Versioning rules:
- current active artifacts keep stable names when useful for writing, e.g. `output/tables/main_table_1.tex`
- archived versions keep dated names under `archive/`, not in active output folders
- version root shorthand: `archive/YYYY-MM-DD_<stage>_<reason>/`
- dated exploratory outputs stay in `pilot/results/` or `analysis/` until promoted
- when promoting a pilot or analysis result into `output/`, archive the previous active artifact first, then update `MANIFEST.md`
- large raw data, caches, and generated checkpoints should not be copied into repo archive; record external path, checksum if feasible, and retention decision in `ARCHIVE_MANIFEST.md`
- never use `archive/` as a dumping ground for unknown files; if provenance is unknown, create an audit note before moving

## Server Start Checklist

Before starting or resuming a server project:
1. confirm host
2. confirm repo path
3. confirm branch
4. confirm tmux session
5. confirm environment activation method
6. confirm latest handoff
7. confirm output root
8. confirm whether data is local, external, or intentionally unsynced
9. create or update `handoff/project_status_probe.md`

Use `04_templates/project_status_probe_template.md` for the probe. Automatic continuation should read this probe before choosing the next action.

For new server projects:
- create or clone under `/home/nanyeon99/project/<repo_name>`
- use tmux session `<repo_name>`
- create project memory files from `04_templates/project_state_template.md`, `decision_log_template.md`, `next_actions_template.md`, and `source_context_template.md`
- create `handoff/project_status_probe.md` from `04_templates/project_status_probe_template.md`
- add README status and environment setup before long runs
- keep data copying intentional; do not mirror large raw data by default

## Writing Kickoff Readiness

A project is ready for writing kickoff when it has:
- `question/main_question.md`
- resolved or documented pivot status
- latest `handoff/` file
- documented analysis settings in `docs/methods.md` or mapped equivalent
- current table and figure outputs
- current `source_context.md` when citations, sources, or workflow sources affect the manuscript
- scripts or commands that regenerate main tables and figures
- current second_brain project memory, plus optional repo-local wiki status if one exists
- enough notes to identify missing settings as `GAP`

If these are missing, create a cleanup handoff before writing kickoff.

## Agent Behavior

When starting a project:
- create the standard structure unless a coherent project structure already exists
- document deviations in `README.md`
- do not move large data or outputs without explicit need
- keep server-specific paths documented but avoid hardcoding them in reusable scripts
- load `research_project_governance.md` when the project needs pivot handling, memory sync, optional project-local wiki, or LLM-wiki promotion

When entering writing:
- confirm pivot review and second_brain/project-wiki sync are current
- load `writing_kickoff_deep_interview.md`
- use `paper/` for skeleton, decision ledger, and exhibit memos
- use `output/` as the source for generated tables and figures
