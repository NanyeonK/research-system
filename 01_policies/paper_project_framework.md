# Paper Project Framework

Updated: 2026-05-08

Purpose:
- define the full research-paper workflow from idea screening to submission
- make every research project aware of the same structure, writing rules, table/figure rules, and review gates
- keep analysis decisions, exhibit generation, manuscript writing, and submission artifacts connected

Storage note:
- this framework lives in the synced `research_paper_system/` folder for compatibility with Hermes, Claude Code, and Codex
- the scope is the full paper project lifecycle, not only prose writing
- weekly wiki updates can improve this framework only through the controlled intake and promotion workflow

## Framework Contract

Every active research-paper project should explicitly recognize this framework.

Minimum recognition in project `README.md`:

```markdown
## Paper Project Framework

This project follows the shared Paper Project Framework:
`/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/`

Required project rules:
- use `02_workflows/idea_evaluation.md` before project start when the paper direction is still an idea
- use `02_workflows/autonomous_progression.md` for automatic phase transitions and human-decision gates
- use `02_workflows/project_structure.md` for repo layout
- use `02_workflows/research_project_governance.md` for phase changes, pivots, second_brain memory, optional project wiki, and LLM-wiki promotion
- use `02_workflows/source_deep_reading.md` when long academic PDFs support source context
- use `references/source_verification_protocol.md` when sources/citations/data documentation support central manuscript claims
- use `02_workflows/specification_lock.md` before choosing or changing the main empirical spine, data source/unit, preprocessing path, methodology, portfolio sort, algorithm, fixed exhibit, or output claim mapping
- use `01_policies/integrity_gate_policy.md` before writing kickoff, referee audit, submission readiness, post-revision stabilization, or locked-spec changes
- use `02_workflows/gate_status_protocol.md` and `qa/gate_status.yaml` before marking a project writing-ready, referee-audit-ready, submission-ready, or autonomous-owner-ready
- use `qa/waiver_log.md` for any human override, skip, or accepted limitation; a waiver narrows claims and does not create a clean pass
- use `qa/artifact_mapping.md` when a legacy/equivalent artifact path is used instead of a canonical path
- use `02_workflows/blindspot_audit.md` before final interpretation or exhibit `FIX`
- use `02_workflows/presentation_deck_workflow.md` for research decks
- use `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/table_generation.md` for publishable tables
- use `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/writing_kickoff_deep_interview.md` before prose writing
- use `02_workflows/referee_audit.md` before final empirical submission or replication-package release
- use `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/manuscript_format_style.md` and `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md` for `ryu_fin_lab` style
- read `01_policies/aris_bridge.md` before invoking any ARIS skill (`/idea-discovery`, `/paper-write`, `/paper-claim-audit`, `/citation-audit`, `/auto-review-loop`, `/rebuttal`, etc.); ARIS lives at `~/Library/CloudStorage/SynologyDrive-second_brain/aris/`
```

Server projects should also record:
- selected execution server: server1/server2/server3
- canonical path
- tmux session
- environment activation method
- latest handoff path
- registry source-of-truth server/path
- `agent_deck.eligible`
- `context.needs_context_normalization`
- last registry validation timestamp

## Project Work Location

Default:
- all active project work is performed directly on the selected execution server: server1, server2, or server3
- the working repo path is `/home/nanyeon99/project/<repo_name>`
- Mac-local project clones are not the default working copy

This applies to analysis code, data processing, model runs, table/figure generation, project-local manuscript files, submission packages, replication packages, and handoffs. Mac remains the canonical place for global framework docs, skills, second_brain memory, and human review.

## Continuous Upgrade Layer

The framework evolves through reviewed wiki updates, not ad hoc chat memory.

Primary docs:
- `02_workflows/wiki_intake_continuous_upgrade.md`
- `02_workflows/research_workflow_modules.md`

Baseline source:
- `wiki/projects/ai-econ-wiki-research-workflow-upgrade-2026-04-26.md`
- `wiki/sources/ai-econ-wiki/`

Rule:
- weekly wiki updates are workflow evidence
- source reviews can propose improvements
- only accepted and audited improvements become framework rules, templates, scripts, or skills
- weak sources must pass a local experiment before becoming hard requirements

## Lifecycle

### 0. Idea Screening

Goal:
- decide whether a research idea deserves a full project repo

Required when the paper direction is still an idea:
- complete `04_templates/idea_evaluation_template.md`
- build a literature map using second_brain/Graphify first when relevant, plus external indexes for gaps and freshness
- identify the three closest threat papers with URLs
- evaluate novelty, identification or method, theory or empirics, impact, feasibility, and timeliness
- review the evaluation for unfairness or factual error
- pivot when score is below threshold
- run threat-literature search and verification before proceeding
- record final verdict and go/no-go preconditions

Primary docs:
- `02_workflows/idea_evaluation.md`
- `02_workflows/lifecycle_repo_organization.md`
- `02_workflows/autonomous_progression.md`

Primary files:
- `ideas/idea_evaluation.md`
- `ideas/literature_map.md` when a repo exists
- `ideas/evaluation/`
- or `wiki/research-ideas/<idea_slug>.md` before a repo exists

Promotion rule:
- before Project Start, co-develop the idea with the human through evaluation and pivots until it reaches the normal `7-8` promotion band
- start a full project only after `PROCEED` or `PROCEED WITH CONDITIONS`, or after an explicit human override recorded in `decision_log.md` and `qa/waiver_log.md`
- record any below-7 override in `decision_log.md` and `qa/waiver_log.md`; it narrows project claims until rechecked

### 1. Project Start

Goal:
- make the project legible before analysis begins

Required:
- place repo under the canonical server root
- create or verify standard folder structure according to `02_workflows/lifecycle_repo_organization.md`
- create only the folders required for the current lifecycle phase plus canonical state files; avoid empty decorative scaffolding
- create `README.md`
- create `project_state.md` or map a legacy equivalent in `qa/artifact_mapping.md`
- create `decision_log.md` or map a legacy equivalent in `qa/artifact_mapping.md`
- create `next_actions.md` or map a legacy equivalent in `qa/artifact_mapping.md`
- create `source_context.md` or map a legacy equivalent in `qa/artifact_mapping.md`
- create `question/main_question.md`
- create `question/decisions.md`
- create `research_log.md`
- document environment setup

For all project work:
- follow `/Users/nanyeon/AGENTS.md`
- use `/home/nanyeon99/project/<repo_name>`
- use tmux session `<repo_name>`

### 2. Research Direction

Goal:
- preserve the human's intended research direction before analysis branches multiply

Required:
- current research question
- target claim
- intended contribution
- target journal or audience if known
- what the paper should not claim
- accepted and rejected analysis branches
- active `specs/main_spec.md` state and version when a main empirical spine exists

Primary files:
- `project_state.md`
- `decision_log.md`
- `next_actions.md`
- `source_context.md`
- `qa/source_verification.md` when citations, sources, or data documentation support central claims
- `qa/claim_verification_matrix.md` when central claims enter prose or review
- `ideas/literature_map.md` or `qa/literature_map.md` when novelty, contribution, mechanism, method, or literature-boundary claims matter
- `qa/threat_literature_matrix.md` when novelty, contribution, closest-threat, or literature-boundary claims enter prose
- `qa/gate_status.yaml` for machine-readable readiness status
- `qa/waiver_log.md` when any gate/rule is overridden or skipped
- `qa/artifact_mapping.md` when canonical artifacts are mapped to legacy/equivalent paths
- `question/main_question.md`
- `question/decisions.md`
- `specs/main_spec.md`
- `specs/spec_change_log.md`
- `plans/`
- `handoff/`
- lifecycle phase folders specified by `02_workflows/lifecycle_repo_organization.md`
- `qa/gate_status.yaml`
- `qa/waiver_log.md` when any skip/override exists
- `qa/invalidation_ledger.md` when specs/outputs/claims changed

### 3. Data And Method Setup

Goal:
- prevent undocumented settings from becoming hidden assumptions

Required:
- data source and version
- preprocessing path
- sample filters
- unit of observation
- variable construction
- model design
- controls, fixed effects, standard errors, clustering
- rolling windows, horizons, thresholds, hyperparameters, seeds
- locked data source/unit, preprocessing, and methodology specifications before outputs are treated as paper evidence
- source verification for any external source, citation, data documentation, or method reference that supports a central claim
- data context memo when producer/reporting rules affect interpretation
- pre-pilot data collection and EDA gate before Phase 4 pilot begins
- weak viability gate before heavy analysis if the empirical spine is not yet proven
- real-run dataset lock before full analysis outputs are treated as paper evidence

Primary docs:
- `02_workflows/specification_lock.md`
- `02_workflows/paper_factory_quality_gates.md`

Primary files:
- `data/README.md`
- `docs/data_construction.md`
- `docs/methods.md`
- `docs/variable_definitions.md`
- `specs/data_spec.md`
- `specs/preprocessing_spec.md`
- `specs/methodology_spec.md`
- `data_context.md` when source meaning or reporting regime affects interpretation
- `eda/summary_statistics.md`, `eda/data_quality_report.md`, and `eda/merge_support_report.md` before pilot
- `viability_gate.md` or `kill_memo.md` when the empirical spine is not yet proven
- `qa/gate_status.yaml` updated after major data/method readiness changes

### 4. Analysis Execution

Goal:
- make analysis reproducible enough for future writing and revision

Required:
- scripts or notebooks that produce results
- dated run logs
- output paths
- major model or sample changes recorded in `research_log.md`
- handoff after major state changes

Primary folders:
- `src/`
- `scripts/`
- `analysis/`
- `output/logs/`
- `handoff/`
- `qa/gate_status.yaml`
- `qa/waiver_log.md` when any skip/override exists
- `qa/invalidation_ledger.md` when specs/outputs/claims changed

### 5. Pivot Review And Memory Sync

Goal:
- keep research direction, pivots, and project knowledge explicit before exhibits and writing harden

Required:
- review whether new analysis changed the target claim, method, sample, or audience
- create pivot memos for direction changes
- mark superseded outputs and update affected exhibit statuses
- update `qa/invalidation_ledger.md` when locked specs, central outputs, or central claims become stale
- update second_brain project memory and project page
- create a project-local wiki only when repo-contained memory is needed
- promote only checked reusable knowledge into the shared LLM wiki

Primary docs:
- `02_workflows/research_project_governance.md`

Primary files and folders:
- `question/pivots/`
- `~/second_brain/04_Ventures/<project>/`
- `~/second_brain/wiki/projects/<project_slug>.md`
- optional repo-local `wiki/`
- `research_log.md`

### 6. Table And Figure Generation

Goal:
- plan, generate, trace, and interpret exhibits
- pre-plan the exhibit set during Phase 4 pilot review before full analysis execution
- assign exhibit roles (`main`, `robustness`, `heterogeneity`, `mechanism`, `appendix`, `drop`) per `specs/output_spec.md` row

Required for tables:
- pre-planning rows in `output/tables/plan.md` before generation begins
- table-builder-compatible title/body/notes metadata, with `MISSING` for unknown fields instead of invented values
- machine-readable data
- generated `.tex`
- manifest
- generation script
- note text
- locked output spec row mapping table to main/data/preprocessing/methodology spec versions
- human-visible publishable verdict: Yeonchan can inspect the generated table, understand the one-sentence takeaway, and decide whether it is worth prose

Required for figures:
- pre-planning rows in `output/figures/plan.md` before generation begins
- figure-builder-compatible title/caption/notes metadata, with `MISSING` for unknown fields instead of invented values
- generated image/vector file
- machine-readable source data when feasible
- generation script
- caption/note source
- locked output spec row mapping figure to main/data/preprocessing/methodology spec versions
- human-visible publishable verdict: Yeonchan can inspect the generated figure, understand the one-sentence takeaway, and decide whether it is worth prose

Primary docs:
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/table_generation.md`
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md`
- `02_workflows/specification_lock.md`

Primary folders:
- `output/tables/`
- `output/figures/`
- `output/diagnostics/`

### 7. Writing Kickoff

Goal:
- convert analysis into a human-approved paper skeleton before prose writing

Required:
- validated writing evidence packet from `references/writing_system_bridge.md`
- `qa/gate_status.yaml` showing writing handoff allowed
- fixed first deep interview form with gate results
- deep interview
- project-local deep research synthesis
- fixed exhibit interview form per candidate table or figure, including evidence grade and FIX eligibility
- exhibit-by-exhibit deep research memos
- skeleton LaTeX
- compiled skeleton PDF when possible
- writing kickoff decision ledger
- `paper/section_paragraph_map.md`: every section and every planned paragraph has one sentence, evidence IDs, source IDs, exhibit IDs, claim strength, and status

Primary files:
- `paper/main_skeleton.tex`
- `paper/main_skeleton.pdf`
- `paper/writing_kickoff_decisions.md`
- `paper/section_paragraph_map.md`
- `paper/exhibit_memos/*.md`

Rule:
- only exhibits labeled `FIX` can support final prose
- `FIX` requires locked main, data, preprocessing, methodology, and output specs for the exhibit
- `FIX` also requires a human-visible publishable check; machine reproducibility alone is not enough
- `REVISE`, `ADD`, and `GAP` exhibits must not be written as final evidence
- paragraph drafting cannot begin until `paper/section_paragraph_map.md` is accepted or explicitly waived

### 8. Paragraph-Level Co-Writing

Goal:
- hand off controlled paragraph drafting to the independent writing system after research evidence is ready

Research-system responsibility:
- preserve the accepted skeleton, accepted section/paragraph map, exhibit `FIX` status, human publishable verdicts, claim boundaries, source/spec support, and known gaps
- stop or return from writing when prose needs unsupported empirical claims, citations, numbers, methods, or exhibit status

Writing-system responsibility:
- paragraph drafting, voice, prose lint, manuscript wording, response-letter prose, and style mechanics

Primary docs:
- `references/writing_system_bridge.md`
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md`

### 9. Review And Revision

Goal:
- turn a draft into a submission-ready manuscript

Required:
- consistency check between claims and exhibits
- Gate 1 number QA and Gate 2 claim-validity QA from `02_workflows/paper_factory_quality_gates.md` when empirical claims enter prose
- claim verification matrix rows for all central claims that enter prose
- integrity gate output when writing kickoff, referee audit, submission readiness, post-revision stabilization, or locked-spec changes apply
- source-context and citation-context audit
- prose lint
- table/figure QA
- blindspot audit for final exhibit interpretations
- method-setting audit
- citation and gap audit
- independent referee audit for submission-ready empirical pipelines; any skip requires `qa/waiver_log.md`, visible accepted-risk notes, and narrowed claims
- humanizer/review pass when appropriate

Primary docs:
- `01_policies/integrity_gate_policy.md`
- `references/source_verification_protocol.md`
- `04_templates/claim_verification_matrix_template.md`
- `02_workflows/gate_status_protocol.md`
- `04_templates/waiver_log_template.md`
- `04_templates/invalidation_ledger_template.md`
- `04_templates/threat_literature_matrix_template.md`
- `04_templates/artifact_mapping_template.md`
- `02_workflows/paper_factory_quality_gates.md`
- `02_workflows/blindspot_audit.md`
- `02_workflows/referee_audit.md`

Primary files:
- `paper/main.tex`
- `paper/sections/`
- `output/diagnostics/`
- `output/diagnostics/blindspot/`
- `correspondence/referee2/`
- `code/replication/` or project equivalent
- `handoff/`
- `qa/gate_status.yaml`
- `qa/waiver_log.md` when any skip/override exists
- `qa/invalidation_ledger.md` when specs/outputs/claims changed

### 10. Submission

Goal:
- preserve the exact submitted state

Required:
- final manuscript export
- cover letter
- response letter if revision
- submission checklist
- dated submission package
- replication package when needed

Primary folders:
- `submit/`
- `replication_package/`
- `archive/`

### 11. Post-Submission / Publication

Goal:
- keep revisions and accepted versions traceable

Required:
- response-to-reviewers notes
- revision decision logs
- final accepted manuscript
- publication PDF when available
- voice/style updates after major milestones

Primary docs:
- Codex skill when available: `$paper-writing-voice`
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/workflows/voice_update.md`
- `research_log.md`
- `submit/`
- `archive/`

## Agent Behavior

When a user starts a research project:
- load this framework
- load `autonomous_progression.md`
- load `project_structure.md`
- if the direction is still an idea, run idea co-development and the idea gate before Project Start
- create or verify the framework recognition block in `README.md`
- document deviations rather than silently using ad hoc paths

When resuming a research project:
- read `README.md`
- confirm whether the project recognizes this framework
- if not, add or recommend the framework recognition block before major new work
- read latest `handoff/`
- confirm current phase in the lifecycle
- if analysis direction changed, load `research_project_governance.md` and run pivot review

When entering writing:
- do not treat existing analysis outputs as ready for prose
- confirm pivot review and second_brain/project-wiki sync are current
- run writing kickoff first
- create exhibit memos before using tables or figures as final evidence
- after the skeleton and exhibit decisions are accepted, use `$paper-writing-voice` for actual paragraph drafting, revision, lint, and voice upkeep when available
