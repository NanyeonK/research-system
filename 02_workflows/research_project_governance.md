# Research Project Governance Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Engine skills:
- `/research-wiki sync` — pull updates from the per-project wiki into a session.
- `/research-wiki update` — modify entities, edges, and claim status inside the project wiki.
- `/research-wiki query` — retrieve relevant prior decisions, papers, ideas, experiments, and claims.

Binding rules:
- `~/second_brain/wiki/` is the global ground truth. Per-project ARIS `wiki/` folders are supplemental and feed into the global wiki only through `02_workflows/wiki_intake_continuous_upgrade.md`.
- Phase changes, pivots, and direction locks are recorded in our `decision_log.md` and `project_state.md`. ARIS wiki entries are mirrors, not replacements.
- Pivot review and second_brain memory sync still run after major analysis batches.

Purpose:
- define how research projects move through phases
- handle analysis pivots without losing provenance
- use second_brain as the default research memory layer
- create project-local wiki only when repo-contained memory is needed
- promote stable project knowledge into the shared LLM wiki

## Scope

Use this workflow when:
- starting or resuming a research-paper project
- deciding whether new analysis changes the paper direction
- analysis pivots from the original target claim, sample, method, or audience
- deciding whether second_brain alone is enough or a project-local wiki is needed
- promoting project knowledge into `~/second_brain/wiki/`
- preparing for writing kickoff after a long or changing analysis phase

This workflow extends `02_workflows/project_structure.md`.
Workflow-module adoption and weekly wiki-derived system upgrades follow `02_workflows/research_workflow_modules.md` and `02_workflows/wiki_intake_continuous_upgrade.md`.
Automatic phase progression follows `02_workflows/autonomous_progression.md`.
System learning from unclear prompts, human-audit failures, repeated agent mistakes, and accepted rule changes follows `02_workflows/second_brain_system_evolution.md`.

## Server-First Work Rule

Active project work should be executed directly on the selected execution server, server1/server2/server3, not in a Mac-local project clone by default.

Before changing analysis, writing project files, regenerating exhibits, or preparing submissions:
- confirm selected execution server: server1/server2/server3
- confirm repo path: `/home/nanyeon99/project/<repo_name>`
- confirm branch, tmux session, and environment activation method
- record exceptions if any work must happen locally on the Mac

Mac remains the canonical place for global system instructions, shared Paper Project Framework docs, Codex skills, and second_brain memory. Project repo work belongs on the selected server.

## Default Memory Model

Default:
- use git tree/commits plus repo-local `CHANGELOG.md` as the authoritative active-project state ledger
- use second_brain as the canonical cross-project memory layer
- use Walnut / `04_Ventures/` for project operating memory, but routine repo progress enters it through automatic `CHANGELOG.md` mirroring, not manual agent summaries
- use `~/second_brain/wiki/projects/<project_slug>.md` for durable project pages
- use `~/second_brain/wiki/concepts/`, `sources/`, `methods/`, `journal/rules/`, and `journal/snippets/` for reusable global knowledge

Do not create a repo-local `wiki/` by default only because the project is a research project.

Important distinction:
- recording something in second_brain makes it available as project memory
- routine repo progress should reach second_brain through the synced `04_Ventures/<project>/CHANGELOG.md` mirror
- it does not automatically mean the note is clean global LLM-wiki knowledge
- promotion to global reusable wiki pages still needs review, dedupe, provenance, and status marking

Evolution rule:
- human decisions, unclear audit-request corrections, gate redesigns, archive/rebuild/skip decisions, dataset-lock waivers, table/figure role decisions, and repeated failure patterns must be saved in second_brain as system-learning data
- routine worker progress remains in repo logs/dashboard unless it changes a decision, gate, or reusable rule
- when a human-audit request is unclear to Yeonchan, patch the template/workflow first, then save the correction in the research-system walnut and promote a rule/insight if reusable

Use repo-local `wiki/` only as an exception when the project needs repo-contained memory, such as server-side work where agents may not have reliable access to the Mac second_brain, external collaboration, replication-package portability, or a project with dense local exhibit/source interpretation that should travel with the repo.

## Project Memory Files

Every active project should maintain canonical project-memory files. Legacy or documented equivalents require `qa/artifact_mapping.md` or a mapping table in `project_state.md`:
- `project_state.md`
- `decision_log.md`
- `next_actions.md`
- `source_context.md`

Use templates from `04_templates/` when creating them.

For already-running projects:
- document equivalent existing files in `qa/artifact_mapping.md` rather than duplicating state
- add missing files only when they improve handoff, audit, writing readiness, or reproducibility
- update `source_context.md` before writing if citations, source reviews, or workflow sources affect the paper

## Phase Governance

Every project should record its current phase in `README.md`.

Phase changes require:
- a short entry in `research_log.md`
- an update to the `README.md` phase checklist
- an update to `project_state.md` autonomy level, current gate, and gate status
- a handoff note when another agent or future session may resume the work

Recommended phases:
1. Project start
2. Research direction
3. Data and method setup
4. Analysis execution
5. Pivot review and memory sync
6. Table and figure generation
7. Writing kickoff
8. Paragraph-level co-writing
9. Review and revision
10. Submission
11. Post-submission / publication

Run phase 5 after every major analysis batch and before writing kickoff.

## Ongoing Project Onboarding Audit

Use this audit when a project already exists and should be brought under the framework.

Principle:
- do not restructure a working project by default
- first identify its current phase, current source of truth, and missing state records
- add the minimum framework files needed to make future work reproducible
- only move files when the existing layout actively blocks reproducibility, writing kickoff, or handoff

Check these items first:

1. Location and execution state
- selected execution server host: server1/server2/server3
- repo path under `/home/nanyeon99/project/<repo_name>`
- git branch
- tmux session if server-side
- environment activation method
- running jobs and output paths

2. Project direction
- current research question
- target claim
- intended contribution
- target journal or audience if known
- what the paper should not claim
- human instructions that changed direction

3. Analysis provenance
- main scripts or notebooks
- data sources and versions
- sample filters and unit of observation
- model settings, controls, fixed effects, standard errors, clustering
- seeds, windows, horizons, thresholds, hyperparameters
- current main outputs and diagnostic outputs

4. Pivot state
- whether the project still answers the original question
- whether sample, method, interpretation, or target audience changed
- which outputs are current, superseded, or diagnostic only
- whether more than one paper direction now exists

5. Memory state
- `project_state.md` or mapped legacy equivalent
- `decision_log.md` or mapped legacy equivalent
- `next_actions.md` or mapped legacy equivalent
- `source_context.md` or mapped legacy equivalent
- latest handoff
- `research_log.md` or mapped legacy equivalent
- Walnut / `04_Ventures/` project memory
- `~/second_brain/wiki/projects/<project_slug>.md` if present
- optional repo-local `wiki/` only if one already exists or is clearly needed

6. Writing readiness
- current table and figure outputs
- whether tables/figures are generated artifacts
- whether table/figure interpretation is stable
- whether a skeleton manuscript already exists
- whether writing kickoff has been run

## Onboarding Decision Levels

After the audit, choose the smallest sufficient action.

### Level 0: Recognize Only

Use when:
- project already has clear logs, methods, handoff, and outputs
- current research direction is stable
- no immediate writing or submission risk exists

Action:
- add the Paper Project Framework block to `README.md`
- mark current phase
- record project-memory file mapping
- record current second_brain project memory path

### Level 1: Minimal State Patch

Use when:
- project works technically, but future agents cannot quickly identify state
- README, question, decisions, or handoff are missing
- outputs are understandable but not centrally indexed

Action:
- add or update `README.md`
- add `project_state.md` if absent and no equivalent exists
- add `decision_log.md` if absent and no equivalent exists
- add `next_actions.md` if absent and no equivalent exists
- add `source_context.md` if absent and source/citation context matters
- add `research_log.md` if absent
- add `question/main_question.md`
- add `question/decisions.md`
- add latest `handoff/`
- update second_brain project memory

### Level 2: Governance Cleanup

Use when:
- direction changed during analysis
- model/sample/settings changed without a decision record
- current and superseded outputs are mixed
- tables or figures may be misinterpreted

Action:
- create `question/pivots/YYYY-MM-DD_<short_slug>.md`
- mark superseded outputs or archive frozen states
- update `docs/methods.md` or mapped equivalent
- reset affected table/figure statuses
- update second_brain project page and Walnut memory

### Level 3: Writing Kickoff Prep

Use when:
- analysis is mostly complete
- writing is about to start
- tables/figures need interpretation, status, or format decisions
- a draft exists but was written before exhibit decisions were fixed

Action:
- confirm pivot review and memory sync
- create or repair table/figure packs
- create exhibit memos
- run `writing_kickoff_deep_interview.md`
- produce skeleton LaTeX/PDF and writing kickoff decisions

### Level 4: Split Or Freeze

Use when:
- two viable papers now coexist
- the original question is no longer the current paper
- old results should remain traceable but not drive the new manuscript
- repo layout mixes incompatible samples, methods, or claims

Action:
- freeze old direction in `archive/pivots/<date_slug>/` or a branch
- create a new project or branch for the new paper
- update second_brain project memory to explain the split
- do not let one README claim cover two active papers unless the distinction is explicit

## Onboarding Output

Every onboarding pass should end with one short note in either `handoff/` or `research_log.md`:

```markdown
# Framework Onboarding: YYYY-MM-DD

Decision level:
Current phase:
Current source of truth:
Main outputs:
Missing records:
Pivot status:
second_brain memory path:
Next action:
```

## Pivot Protocol

A pivot is any change that alters what the paper is trying to prove, how the main evidence is generated, or which audience the paper is targeting.

Pivot triggers:
- main empirical result contradicts the original target claim
- sample, data source, or unit of observation changes the paper's scope
- method changes from robustness to core identification or forecasting design
- table or figure interpretation no longer supports the intended story
- target journal or audience changes the contribution framing
- human instruction changes the research direction

Pivot classes:
- `Minor adjustment`: same main question and target claim; record in `research_log.md` and `question/decisions.md`
- `Analysis pivot`: same project, but central sample/model/mechanism changes; create a pivot memo
- `Paper pivot`: main claim, contribution, or audience changes; freeze old direction and update `question/main_question.md`
- `Project split`: a second paper emerges; create a new project or branch rather than overloading one repo

Required memo path:

```text
question/pivots/YYYY-MM-DD_<short_slug>.md
```

Pivot memo template:

```markdown
# Pivot: <short title>

Date:
Decision:
Class: Minor adjustment | Analysis pivot | Paper pivot | Project split

Previous direction:

Trigger evidence:

Human instruction:

New direction:

Retained assets:

Invalidated or superseded assets:

Required reruns:

Table/figure status changes:

Writing implication:

Memory updates:

LLM-wiki promotion impact:

Next step:
```

Pivot rules:
- do not delete old outputs only because the direction changed
- mark superseded outputs clearly or move frozen states to `archive/pivots/<date_slug>/`
- reset affected table/figure statuses from `FIX` to `REVISE`, `DROP`, or `GAP`
- update exhibit memos when a pivot changes interpretation
- update `question/main_question.md` after any `Paper pivot`
- update `docs/methods.md` when the pivot changes model, sample, controls, horizons, clustering, seeds, or filters
- create a new project or branch when two target papers now coexist

## Project-Local Wiki Exception

A project-local wiki is optional provisional working memory inside one repo. It is not the default because second_brain already provides shared memory across projects.

If needed, use:

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

Use a project-local wiki when:
- second_brain is not reliably accessible from the execution environment
- repo-contained handoff is more important than central memory
- collaborators or replication users need the notes with the repo
- the project has many concepts, mechanisms, sources, or exhibit interpretations
- multiple agents will resume the project over time
- writing kickoff would otherwise depend on memory scattered across chats and handoffs

Do not use the project wiki for:
- knowledge that already belongs cleanly in second_brain global wiki
- raw run logs that belong in `research_log.md` or `output/logs/`
- generated table or figure data that belongs in `output/`
- active manuscripts that belong in `paper/`
- large raw data or private restricted files

Recommended page front matter:

```yaml
---
project: <repo_name>
status: draft
source_scope: project-local
evidence:
global_target:
last_reviewed: YYYY-MM-DD
---
```

Allowed statuses:
- `draft`: useful note, not yet checked
- `checked`: reviewed against project evidence
- `superseded`: kept for provenance, no longer current
- `export_candidate`: stable enough to consider for the shared wiki
- `exported`: promoted to the shared wiki; include the global path

Project wiki rules:
- keep project-specific claims in `wiki/claims.md` unless they become reusable knowledge
- link exhibit interpretations to `paper/exhibit_memos/`
- mark pages superseded after pivots rather than silently rewriting history
- maintain `wiki/project_index.md` so future agents can see the knowledge structure quickly
- list export candidates in `wiki/export/llm_wiki_candidates.md`

## Shared LLM-Wiki Integration

The shared LLM wiki is:

```text
~/second_brain/wiki/
```

Promotion is deliberate. A project-local page becomes global only when it is useful outside the project and has enough provenance.

If the note already starts in second_brain, the same rule applies: project-page notes and Walnut logs are not automatically canonical concept/source/method pages. They are candidates until checked and promoted.

Promotion destinations:
- project overview or status: `~/second_brain/wiki/projects/<project_slug>.md`
- reusable concept: `~/second_brain/wiki/concepts/<concept_slug>.md`
- source note: `~/second_brain/wiki/sources/<source_slug>.md`
- reusable method pattern: `~/second_brain/wiki/methods/<method_slug>.md` or the nearest existing methods folder
- durable operating rule: `~/second_brain/wiki/journal/rules/<rule_slug>.md`
- reusable code pattern: `~/second_brain/wiki/journal/snippets/<snippet_slug>.md`

Promotion checklist:
1. confirm the project-local page status is `checked` or `export_candidate`
2. search the shared wiki for duplicates or near-duplicates before creating a new page
3. preserve project provenance, source paths, and date reviewed
4. separate stable general knowledge from project-specific claims
5. add backlinks to the project page when useful
6. update the project-local page status to `exported`
7. record the promotion in `research_log.md`

For notes that start directly in second_brain:
1. confirm the page is not just a transient project log
2. search for existing concept/source/method pages
3. move or summarize reusable content into the correct global destination
4. link back to the project page or Walnut source
5. record the promotion in project memory

Do not promote:
- exploratory notes without checked evidence
- superseded pivot branches
- intermediate outputs whose interpretation may still change
- restricted data or private source details
- project-specific claims that are not useful beyond that paper

## Writing Kickoff Gate

Before running `writing_kickoff_deep_interview.md`, confirm:
- current `README.md` phase is accurate
- open pivot questions are resolved or marked as `GAP`
- `question/main_question.md` reflects the current paper direction
- pivot memos exist for major direction changes
- second_brain project memory is current
- any optional project-local wiki pages relevant to the manuscript are not silently superseded
- table/figure statuses are reset if the analysis direction changed

If these conditions are not met, run a governance cleanup before creating the skeleton LaTeX/PDF.

## Agent Behavior

When starting a project:
- load `paper_project_framework.md`
- load `project_structure.md`
- load this workflow
- create framework recognition in `README.md`
- use second_brain as default project memory
- create repo-local `wiki/` only when there is a concrete reason

During analysis:
- record major state changes in `research_log.md`
- create pivot memos when direction changes
- keep old outputs traceable instead of overwriting them without explanation
- update second_brain project memory, and optional project-local wiki pages only if they exist

Before writing:
- run pivot review and second_brain/project-wiki sync
- then run writing kickoff

When promoting to the shared wiki:
- dedupe first
- preserve provenance
- mark local pages as exported with the global path
