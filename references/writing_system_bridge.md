# Writing System Bridge

Purpose: define the contract between the independent research system and the independent writing system.

Canonical roots:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/
```

## Ownership boundary

Research system owns:
- idea screening and project start gates
- project lifecycle, project state, decision logs, and next actions
- server-first execution under `/home/nanyeon99/project/<repo_name>`
- data provenance, analysis panels, specifications, leakage checks, and reproducibility
- source context, literature map, and citation support
- table/figure/exhibit evidence status: `FIX`, `REVISE`, `DROP`, `ADD`, `GAP`, plus whether Yeonchan can inspect the exhibit as publishable
- blindspot audit before interpreting results or locking exhibits
- referee audit, replication checks, submission readiness, and project governance

Writing system owns:
- paragraph drafting and revision
- voice profile and voice updates
- prose lint and deterministic prose QA
- manuscript wording, captions, notes, response letters, and academic style adaptation
- table/figure prose after the research system provides evidence status
- style packs, Word/docx manuscript formatting, and venue-specific writing rules

## Handoff contract

v2 reference: `02_workflows/research_pipeline_v2.md` calls this file during Phase 5, `writing system handoff`. Phase 5 does not create a second writing contract. It uses this bridge as the entry contract and the evidence packet below as the shared definition of writing readiness. If v2 Phase 5 language and this bridge appear to differ, update both documents before prose starts.

Before a research project enters writing, the research system must provide a writing evidence packet:

```text
project_state.md
source_context.md
qa/source_verification.md when sources/citations support central claims; legacy equivalents require `qa/artifact_mapping.md`
ideas/literature_map.md or qa/literature_map.md when novelty, contribution, mechanism, method, or literature-positioning claims enter prose
decision_log.md
next_actions.md
exhibit_decision_ledger.md or mapped equivalent
audit_issue_ledger.md when issues have been raised
sample_support.md when sample path, treatment support, match rates, or subgroup support matter
dropped_findings.md when any candidate results were rejected or narrowed
data_context.md when data producer/reporting rules affect interpretation
eda/summary_statistics.md, eda/data_quality_report.md, and eda/merge_support_report.md when sample/data support matters
output/tables/plan.md and output/figures/plan.md before exhibit generation or writing handoff
active spec lock files or combined specs/spec_lock.md: main_spec, data_spec, preprocessing_spec, methodology_spec, output_spec, and spec_change_log
qa/claim_verification_matrix.md when central claims enter prose; legacy equivalents require `qa/artifact_mapping.md`
qa/integrity_gate.md, when writing kickoff or review-readiness is the next step
qa/gate_status.yaml
qa/waiver_log.md when any gate/rule is overridden or skipped
qa/invalidation_ledger.md when locked specs, central outputs, or central claims changed
qa/artifact_mapping.md when any canonical artifact uses a legacy/equivalent path
fixed tables/figures and paths, with human-visible publishable verdicts
paper/section_paragraph_map.md with one sentence per section and one sentence per planned paragraph before paragraph drafting
qa/audit_ownership_matrix.md when machine/human audit split matters or a gate is contested
claim boundaries and known gaps
target journal/style constraints, if known
```

The writing system may draft only within that packet. Before paragraph-level drafting, Yeonchan must be able to inspect the publishable tables/figures and a section/paragraph map that states one sentence per section and one sentence per planned paragraph. Unsupported claims must be marked with `[GAP: ...]` or `[ASSUMPTION: ...]`. Legacy/equivalent paths count only when mapped; unmapped equivalents block handoff.

## Routing rules

- For writing-only tasks, start at `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md`.
- For project lifecycle, analysis, empirical claims, table/figure readiness, or submission gates, start at `research_paper_system/00_START_HERE.md`.
- If a writing request depends on analysis readiness, exhibit `FIX`, source context, or submission state, return to the research system before drafting.
- If a research task reaches prose generation, hand off to the writing system after the evidence packet exists.

## Canonical artifact rule

The canonical paths in this bridge are binding for active projects. Equivalent artifacts are allowed only during onboarding or legacy migration, and only if `qa/artifact_mapping.md` or `project_state.md` maps `canonical_name`, `actual_path`, `reason`, `migration_status`, `owner`, and `date`.

A waiver, skip, or override does not create a clean pass. It must be recorded in `qa/waiver_log.md` and narrows the claim boundary visible to the writing system.

## Compatibility

The old nested path `research_paper_system/writing_system/` is a redirect bridge only. Do not add new writing rules there.
