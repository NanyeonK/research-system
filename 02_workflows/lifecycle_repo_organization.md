# Lifecycle Repo Organization Workflow

Purpose: define how a research project repository should be organized as an idea moves from rough concept to literature map, project promotion, specs, pilot, analysis, exhibits, writing handoff, review, and submission.

v2 priority note: `02_workflows/research_pipeline_v2.md` is the controlling layout for v2 projects when it conflicts with older phase names in this document. Older phase sections remain useful for legacy projects and migration audits. New v2 projects should use the phase-prefixed layout below.

This workflow complements:
- `02_workflows/research_pipeline_v2.md`
- `02_workflows/idea_evaluation.md`
- `02_workflows/project_structure.md`
- `02_workflows/specification_lock.md`
- `01_policies/archive_policy.md`
- `references/writing_system_bridge.md`
- `02_workflows/gate_status_protocol.md`

Canonical execution root:

```text
/home/nanyeon99/project/<repo_name>
```

Mac/second_brain root for pre-repo idea work:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/wiki/research-ideas/<idea_slug>.md
```

## Core Rule

The repo should grow by phase. Do not create empty folders only for aesthetics, but once a phase begins, create the phase's required folders and index files before producing artifacts. Active state is tracked by git tree/commits plus root `CHANGELOG.md`; second_brain receives only an automatic `CHANGELOG.md` mirror.

Every phase must answer:
- where current state is recorded
- where source/literature evidence is recorded
- where machine outputs are stored
- where human decisions are recorded
- which artifacts are active vs superseded

## v2 Phase-Prefixed Layout

New v2 projects use the phase-prefixed layout from `02_workflows/research_pipeline_v2.md`. The phase folders hold phase-specific planning, outputs, and integration memos. Cross-cutting folders hold live contracts and audit files.

```text
<repo_name>/
  README.md
  project_state.md
  decision_log.md
  next_actions.md
  source_context.md
  research_log.md
  CHANGELOG.md
  MANIFEST.md
  00_phase_router/
  01_data_planning/
  02_pilot/
  03_main_analysis/
  04_skeleton/
  05_writing_handoff/
  06_replication/
  specs/
  qa/
  refs/
  logs/
  99_archive/
```

`00_phase_router/` records entry routing, research type classification, Phase 0 literature scans, and route decisions.

`01_data_planning/` records wide, mid, and detailed plans for data, method, literature, pilot scope, and early exhibit logic.

`02_pilot/` records pilot design, pilot execution, pilot results, pilot limitations, minimax review, and Human Gate 1 packet.

`03_main_analysis/` records main results, lane outputs, robustness results, novelty scan, Figure 1 hook candidates, minimax lane reviews, and Human Gate 2 packet.

`04_skeleton/` records idea-result diff, paper spine, exhibit map, section skeleton, and writing handoff packet.

`05_writing_handoff/` records research-to-writing handoff state. It does not replace the sibling writing system. It stores the research evidence packet that the writing system consumes.

`06_replication/` records dependency graph, master script, environment locks, hash ledger, README, self-test log, and upload-ready package state.

## Cross-Cutting Live Layers

`specs/` remains live. It contains `main_spec.md`, `data_spec.md`, `preprocessing_spec.md`, `methodology_spec.md`, `output_spec.md`, `spec_change_log.md`, and topic-specific refinements when needed. Do not move active specs into archive during phase transitions.

`qa/` remains live. It contains `gate_status.yaml`, `source_verification.md`, `claim_verification_matrix.md`, `integrity_gate.md`, `waiver_log.md`, `artifact_mapping.md`, and `invalidation_ledger.md` when needed. Do not move active QA state into archive.

`refs/` stores active literature maps, source roles, citation metadata, and paper request state. When a literature branch is superseded, archive the superseded branch under `99_archive/` but keep the active map in `refs/`.

`logs/` stores machine logs and execution notes that need to remain discoverable across phases. Large generated logs may be summarized and archived if they are not active gate evidence.

`99_archive/` stores superseded thinking and reusable alternatives. It is governed by `01_policies/archive_policy.md`.

## v2 Archive Boundary

Archive wide plans, dropped findings, pivoted alternatives, alternative specs, and reusable components. Do not archive live `specs/`, live `qa/`, current `project_state.md`, current `decision_log.md`, current `CHANGELOG.md`, or the accepted writing handoff packet.

`99_archive/INDEX.md` should list every archived bundle, original path, archive path, reason, date, and whether it can be reused.

## Phase 0 — Rough Idea Before Repo

Use when the human gives a rough idea and the project is not yet promoted.

Location:

```text
second_brain/wiki/research-ideas/<idea_slug>.md
```

Required sections in the research-idea note:
- raw human idea
- intake answers and gaps
- one-sentence question
- one-sentence mechanism
- expected prediction
- candidate data/sample
- candidate method/identification
- literature map summary
- second_brain/Graphify search summary
- external gap search summary
- idea-evaluation-pipeline score and critique
- pivot attempts
- final verdict
- promotion preconditions

Do not create `/home/nanyeon99/project/<repo_name>` until final verdict is `PROCEED`, `PROCEED WITH CONDITIONS`, or Yeonchan records an override.

## Phase 0A — second_brain-First Literature Map

Search order:

1. Project-specific notes if an older related repo exists.
2. Existing second_brain Graphify outputs:
   - `GRAPH_REPORT.md`
   - `graph.json`
   - graph wiki/index if available
3. second_brain sources and concepts:
   - `wiki/sources/`
   - `wiki/concepts/`
   - `wiki/research-ideas/`
   - `wiki/projects/`
4. bounded Graphify corpus if no relevant existing graph exists.
5. external scholarly indexes only for missing parts:
   - OpenAlex for broad graph/index coverage, concepts, related works, metadata, citation counts
   - Semantic Scholar for citation/context expansion and verification
   - Crossref for DOI/metadata confirmation
   - RePEc, NBER, SSRN, arXiv, CEPR, publisher pages, and Google Scholar for economics/finance working-paper and freshness gaps

Output before repo:

```text
second_brain/wiki/research-ideas/<idea_slug>.md
```

If the literature map is substantial, also create:

```text
second_brain/wiki/research-ideas/<idea_slug>_literature_map.md
```

Rules:
- External search should be targeted at gaps found after second_brain search, not a blind first step.
- OpenAlex/Semantic Scholar hits are leads until metadata and source role are verified.
- Graphify inferred edges are leads until source verification.
- The idea score cannot exceed 6.5 unless the literature map is adequate or the score is explicitly preliminary.

## Phase 1 — Project Promotion / Repo Birth

Trigger:
- final verdict `PROCEED` or `PROCEED WITH CONDITIONS`
- or explicit human override with waiver

Create on selected execution server:

```text
<repo_name>/
  README.md
  project_state.md
  decision_log.md
  next_actions.md
  source_context.md
  research_log.md
  CHANGELOG.md
  MANIFEST.md
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
  qa/
    gate_status.yaml
    artifact_mapping.md        # only if legacy/equivalent paths are used
    waiver_log.md              # only if override/skip exists
```

Populate immediately:
- copy or summarize the second_brain idea note into `ideas/idea_evaluation.md`
- copy the literature map into `ideas/literature_map.md`
- copy accepted source roles into `source_context.md`
- record promotion decision in `decision_log.md`
- set current phase and server/path in `project_state.md`
- create first concrete tasks in `next_actions.md`
- update `MANIFEST.md` with active idea/literature/state artifacts

Do not yet create final tables, paper prose, or submission folders unless needed.

## Phase 2 — Research Direction And Specs

Create:

```text
specs/
  main_spec.md
  data_spec.md
  preprocessing_spec.md
  methodology_spec.md
  output_spec.md
  spec_change_log.md
qa/
  source_verification.md
  claim_verification_matrix.md
  threat_literature_matrix.md
  literature_map.md            # optional mirror if literature claims become QA-facing
  gate_status.yaml
```

Required updates:
- `question/main_question.md`: locked or provisional research question
- `question/decisions.md`: accepted/rejected branches
- `specs/main_spec.md`: main estimand, contribution, claim boundaries, non-claims
- `qa/source_verification.md`: verified source roles for central literature/data/method claims
- `qa/threat_literature_matrix.md`: closest threats when novelty claims enter project state

Topic-specific sub-specs may be added later under:

```text
specs/topic/
```

Examples:
- `specs/topic/portfolio_sorting_spec.md`
- `specs/topic/real_estate_panel_spec.md`
- `specs/topic/forecasting_target_horizon_spec.md`
- `specs/topic/ml_model_family_spec.md`
- `specs/topic/theory_calibration_spec.md`

Generic specs remain canonical; topic sub-specs refine them.

## Phase 3 — Data And Method Setup

Create or fill:

```text
data/
  README.md
  raw/
  interim/
  processed/
  external/
  metadata/
docs/
  data_construction.md
  methods.md
  variable_definitions.md
scripts/
src/
analysis/
  notebooks/        # optional, only if notebooks are used
eda/
  EDA_PLAN.md
  EDA_LOG.md
  summary_statistics.md
  data_quality_report.md
  merge_support_report.md
  variable_catalog.csv
qa/
  source_verification.md
  gate_status.yaml
```

Rules:
- `data/raw/` stores immutable raw inputs or pointers/manifests when data is too large or external.
- `data/external/` stores third-party downloaded metadata/corpus files such as OpenAlex/Semantic Scholar JSON/CSV if used for the project.
- `data/metadata/` stores data dictionaries, producer documentation, and provenance manifests.
- `docs/data_construction.md` explains raw-to-processed construction.
- `docs/methods.md` explains model/econometric design at the level needed for reproduction.
- `docs/variable_definitions.md` gives variables, units, transformations, and source fields.

### Phase 3A — Data Collection And EDA Gate

Run data collection and EDA before finalizing the pilot plan.

Required EDA artifacts:
- `eda/EDA_PLAN.md`: EDA questions, commands, expected evidence, and falsification conditions.
- `eda/EDA_LOG.md`: dated observations, failed joins, surprising distributions, and follow-up tasks.
- `eda/summary_statistics.md`: N, unique keys, time range, missing rates, winsorization/trimming diagnostics, treatment/exposure variation, and outcome distribution per source.
- `eda/data_quality_report.md`: duplicates, key uniqueness, panel balance, outliers, structural missingness, and mechanical exposure flags.
- `eda/merge_support_report.md`: merge keys, join types, match rates, non-match patterns, drop reasons, and merge-risk verdict.
- `eda/variable_catalog.csv`: variable name, source, unit, dtype, role, missing share, and allowed use.

Gate rule:
- Pilot cannot begin until EDA confirms that outcome, treatment/exposure/predictor, key/time/unit, and minimum merge support exist.
- If EDA reveals a kill-level failure, write `kill_memo.md` and stop unless Yeonchan records an override.
- If key/time/unit is unclear, return `needs_info`; do not invent variable meanings.
- Record EDA gate status in `qa/gate_status.yaml`.

## Phase 4 — Pilot / Feasibility

Create:

```text
pilot/
  PILOT_PLAN.md
  PILOT_TRACKER.md
  PILOT_LOG.md
  results/
  artifacts/
  archive/
output/diagnostics/pilot/
```

Use for:
- data access tests
- merge/support/missingness checks
- minimal descriptive pattern
- first model smoke test
- first figure/table prototype
- kill-risk test

Rules:
- Pilot outputs do not become paper evidence until promoted through specs, output mapping, and QA.
- Failed pilots stay in `pilot/archive/` or `output/diagnostics/pilot/`, not in final `output/tables/`.
- `pilot/results/summary_statistics.md` is required before pilot promotion decision.
- Pilot summary statistics must include per-source N, time range, unit count, treatment/exposure variation, outcome distribution, key missingness, winsorization/trimming bounds, and a machine-readable CSV table.
- Before pilot promotion, create `output/tables/plan.md` and `output/figures/plan.md`.
- Exhibit plan rows must include ID, type, role (`main`, `robustness`, `heterogeneity`, `mechanism`, `appendix`, `drop`), expected content, expected takeaway, source script/data if known, and status (`PLANNED`, `REVISED`, `FIX`, `DROP`, `GAP`).
- Promotion or kill decision goes in `decision_log.md`.
- Pilot promotion requires summary-statistics and exhibit-plan gate status recorded in `qa/gate_status.yaml`.

## Phase 5 — Analysis Execution

Create or fill:

```text
analysis/
  runs/
  notebooks/        # optional
  scratch/          # temporary, ignored or archived
output/
  logs/
  models/
  diagnostics/
  intermediate/
scripts/
src/
```

Rules:
- Reproducible scripts go in `scripts/` or package code under `src/`.
- One-off exploratory notebooks may live under `analysis/notebooks/` but must have a promotion path to scripts.
- Long-running logs go to `output/logs/`.
- Model artifacts go to `output/models/`.
- Diagnostics and robustness outputs go to `output/diagnostics/`.
- Update `research_log.md`, `CHANGELOG.md`, `MANIFEST.md`, and `qa/gate_status.yaml` after major runs. Do not hand-write routine run summaries into second_brain; the root `CHANGELOG.md` is mirrored automatically.

## Phase 6 — Pivot Review And Memory Sync

Create or update:

```text
question/pivots/
handoff/
archive/YYYY-MM-DD_<stage>_<reason>/
qa/invalidation_ledger.md
MANIFEST.md
CHANGELOG.md
```

second_brain updates:

```text
second_brain/04_Ventures/<project>/
second_brain/wiki/projects/<project_slug>.md
second_brain/wiki/research-ideas/<idea_slug>.md
```

Rules:
- Superseded outputs are marked in `MANIFEST.md` and moved or linked to `archive/` when needed.
- If locked specs or central claims change, update `qa/invalidation_ledger.md`.
- Only checked reusable knowledge goes to the shared wiki.

## Phase 7 — Tables And Figures

Create:

```text
output/
  tables/
    data/
    tex/
    csv/
    logs/
    manifests/
  figures/
    data/
    raw/
    final/
    logs/
    manifests/
  diagnostics/
qa/
  claim_verification_matrix.md
  audit_ownership_matrix.md
paper/
  exhibit_memos/
```

Rules:
- Each publishable table needs machine-readable backing data, generated TeX, generation script, manifest, notes, and output spec mapping.
- Each publishable figure needs source data where feasible, generated vector/image, generation script, caption/note source, manifest, and output spec mapping.
- `paper/exhibit_memos/` records one-sentence takeaway, allowed claim strength, status, and human publishable verdict.
- Only `FIX` + human publishable `PASS` exhibits may anchor final prose.

## Phase 8 — Writing Kickoff / Skeleton

Create:

```text
paper/
  main_skeleton.tex
  main_skeleton.pdf
  first_deep_interview.md
  writing_kickoff_decisions.md
  section_paragraph_map.md
  exhibit_memos/
handoff/
  writing_evidence_packet.md
qa/
  integrity_gate.md
  gate_status.yaml
  audit_ownership_matrix.md
```

Rules:
- `paper/section_paragraph_map.md` must state one sentence per section and one sentence per planned paragraph.
- Each paragraph row must list evidence IDs, source IDs, exhibit IDs, claim strength, and status.
- The writing system receives a packet, not a vague instruction to write.
- If Yeonchan cannot inspect the table/figure and the paragraph claim map, writing handoff is blocked.

## Phase 9 — Paragraph Drafting And Revision

Create or fill:

```text
paper/
  main.tex
  sections/
  drafts/
  review_notes/
qa/
  claim_verification_matrix.md
  integrity_gate.md
  gate_status.yaml
output/diagnostics/
```

Rules:
- Research system preserves evidence boundaries; writing system owns wording.
- Any unsupported claim returns to research system.
- Any new number or citation in prose needs claim/source verification.
- Gate 1 number QA and Gate 2 claim-validity QA run before treating prose as review-ready.

## Phase 10 — Referee Audit / Submission

Create:

```text
output/diagnostics/referee_audit/
correspondence/referee2/
code/replication/
replication_package/
submit/
archive/YYYY-MM-DD_submission_state/
```

Rules:
- Referee audit is independent and fail-closed for submission-ready empirical projects unless waived.
- Submission package must preserve exact submitted state.
- Replication package uses relative paths and documented commands.

## Machine vs Human Organization Duties

Machine-owned checks:
- phase folders and required index files exist
- canonical paths or artifact mappings exist
- `qa/gate_status.yaml` vocabulary is valid
- source IDs, DOI/OpenAlex/S2 IDs, and URLs are recorded
- stale/superseded outputs are marked
- writing handoff has `section_paragraph_map.md` and human publishable flags

Human-owned checks:
- repo phase reflects actual project maturity
- literature gap is substantively real
- topic-specific sub-specs are adequate
- exhibit set is publishable
- section/paragraph map tells the intended paper story
- waivers and limitations are acceptable

When in doubt, create the smallest missing state file rather than moving large artifacts.
