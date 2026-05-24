# Archive Policy

Updated: 2026-05-24

Status: v2 policy. Use with `02_workflows/research_pipeline_v2.md` and `02_workflows/lifecycle_repo_organization.md`.

Purpose

This policy defines how research projects preserve superseded plans, pivots, dropped findings, alternative specs, and reusable components without confusing them with the active project contract. The goal is provenance without drift.

## 1. Core rule

Archive artifacts when they are no longer active but remain useful for provenance, audit, or reuse. Do not archive active specs, active QA files, current state files, or accepted handoff packets.

Archive movement must be explicit. Every archive action records what moved, where it moved, why it moved, and whether it can be reused.

## 2. Archive root

v2 projects use this archive root:

```text
99_archive/
  INDEX.md
  wide_plans/
  pivots/
  dropped_findings/
  alternative_specs/
  reusable_components/
```

Legacy projects may also contain `archive/`. New v2 work should use `99_archive/`. If a legacy archive is retained, map it in `qa/artifact_mapping.md`.

## 3. What belongs in each archive folder

### `99_archive/wide_plans/`

Store wide and mid plans after narrowing. Use phase subfolders.

```text
99_archive/wide_plans/phase0/
99_archive/wide_plans/phase1/
99_archive/wide_plans/phase2/
99_archive/wide_plans/phase3/
99_archive/wide_plans/phase4/
```

Examples:

- early data source option maps
- rejected identification routes
- broad literature community maps
- model family option lists
- preliminary exhibit spines that were not chosen

### `99_archive/pivots/`

Store pivot packets when the project changes question, sample, method, claim, or research type. A pivot archive should include the pre-pivot state, reason, decision record, and invalidation implications.

Examples:

- question pivot after a weak pilot
- sample pivot after data support failure
- claim pivot after novelty scan
- method pivot after estimator failure

### `99_archive/dropped_findings/`

Store findings that were real enough to document but not suitable for the active paper spine.

Examples:

- null results that constrain interpretation
- heterogeneity findings that fail support checks
- figures that look suggestive but fail source verification
- robustness results that are informative but not part of the claim

### `99_archive/alternative_specs/`

Store spec alternatives that were considered but not active. Alternative specs are not live specs. They cannot be used for analysis unless restored through `decision_log.md` and spec lock rules.

Examples:

- alternative main sample definitions
- alternative outcome definitions
- alternative preprocessing choices
- alternative estimator or model families
- alternative exhibit mappings

### `99_archive/reusable_components/`

Store components that may help future projects but are not active in this one.

Examples:

- generic data cleaning snippets
- table wrappers that did not match this paper
- graphify query recipes
- literature scan query sets
- project setup notes

Reusable components must not contain secrets, private credentials, restricted data, or large artifacts.

## 4. What must stay live

Do not archive these merely because a phase changes:

- `project_state.md`
- `decision_log.md`
- `next_actions.md`
- `CHANGELOG.md`
- `MANIFEST.md`
- `specs/main_spec.md`
- `specs/data_spec.md`
- `specs/preprocessing_spec.md`
- `specs/methodology_spec.md`
- `specs/output_spec.md`
- `specs/spec_change_log.md`
- `qa/gate_status.yaml`
- `qa/source_verification.md`
- `qa/claim_verification_matrix.md`
- `qa/integrity_gate.md`
- `qa/waiver_log.md`
- `qa/invalidation_ledger.md`
- accepted writing handoff packet
- release candidate replication package

If an active file is superseded, create the replacement first, update references, record the decision, then archive the old file with a clear index entry.

## 5. Pivot procedure

When a pivot happens, use this sequence.

1. Identify the pivot scope. State whether it affects question, data, sample, method, output, claim, exhibit, or research type.
2. Stop active lane execution that depends on the old state.
3. Write the pivot decision in `decision_log.md`.
4. Update `qa/invalidation_ledger.md` if locked specs, outputs, claims, or prose are affected.
5. Create an archive bundle under `99_archive/pivots/YYYY-MM-DD_<short_reason>/`.
6. Move or copy superseded phase artifacts into that bundle. Prefer moving generated or obsolete artifacts. Prefer copying small state snapshots when audit continuity needs the old version.
7. Update `99_archive/INDEX.md`.
8. Update `MANIFEST.md` so active artifacts and archived artifacts are distinguishable.
9. Resume only after `project_state.md`, active specs, and `qa/gate_status.yaml` reflect the new state.

## 6. Dropped finding procedure

A dropped finding should not disappear. Use this sequence.

1. Write a short dropped-finding memo explaining the result, source script or data, and reason for dropping.
2. Move supporting non-active tables, figures, logs, or notes under `99_archive/dropped_findings/YYYY-MM-DD_<short_label>/`.
3. Update `99_archive/INDEX.md`.
4. If the finding narrows a claim, update `qa/claim_verification_matrix.md`.
5. If the finding invalidates prose or an exhibit, update `qa/invalidation_ledger.md`.

## 7. Alternative spec procedure

Alternative specs are dangerous because they can create silent spec drift. Use this sequence.

1. Mark the alternative as not active at the top of the file.
2. Move it to `99_archive/alternative_specs/YYYY-MM-DD_<short_label>/`.
3. Add an index entry with the active spec it lost to.
4. Record the decision in `decision_log.md`.
5. Do not run analysis from an alternative spec unless it is restored through the spec lock workflow.

## 8. Archive index format

`99_archive/INDEX.md` should use this format. For new projects, fork `04_templates/archive_index_template.md` into `99_archive/INDEX.md` before the first archive entry.

```markdown
# Archive Index

| Date | Category | Original path | Archive path | Reason | Reusable | Decision log entry |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | wide_plans | 01_data_planning/wide_plan.md | 99_archive/wide_plans/phase1/YYYY-MM-DD_wide_plan.md | Narrowed to detailed plan | yes | decision_log.md#... |
```

If the project avoids tables for readability, use one repeated block per archive item with the same fields. The fields are mandatory either way.

## 9. Restoration rule

Archived artifacts do not become active by being copied back. Restoration requires:

- `decision_log.md` entry
- updated `project_state.md`
- updated `MANIFEST.md`
- updated `qa/gate_status.yaml`
- spec lock or invalidation update when specs, outputs, claims, or prose are affected

## 10. Safety rules

Do not archive secrets. Remove them and record the redaction.

Do not archive large restricted data unless the project data policy allows it. Store a manifest or pointer instead.

Do not archive active QA to make a gate look clean.

Do not use archive as scratch. Scratch belongs in ignored local scratch paths or phase-local scratch folders with cleanup rules.

Do not let archive copies become the source of truth. Active project state remains in the live root, phase folders, `specs/`, `qa/`, and `refs/`.
