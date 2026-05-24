# Paper Factory Quality Gates

Source pattern: nwilmers/paper_factory, reviewed 2026-05-21. No upstream license was present, so this is a Hermes-native adaptation of workflow ideas, not a copy of upstream prompts or code.

Related source pattern: Imbad0202/academic-research-skills, reviewed 2026-05-21. Upstream is CC BY-NC 4.0, so source-verification, integrity-gate, and claim-matrix additions here are clean-room adaptations with attribution.

Purpose:
- add earlier empirical viability checks
- keep candidate findings focused
- preserve cross-step audit memory
- separate replication/number QA from estimand/claim-validity QA
- stop writing from laundering weak or mechanical findings into strong claims

## Where this fits

Use this workflow inside the research system when a project is moving from idea/data exploration toward paper-shaped empirical claims.

It complements:
- `01_policies/paper_project_framework.md`
- `01_policies/integrity_gate_policy.md`
- `02_workflows/gate_status_protocol.md`
- `02_workflows/idea_evaluation.md`
- `02_workflows/blindspot_audit.md`
- `02_workflows/referee_audit.md`
- `references/source_verification_protocol.md`
- `references/writing_system_bridge.md`

It does not replace the final independent referee audit.

## Stage A. Research and data foundations

Before building candidate findings, create or verify:

```text
project_state.md
decision_log.md
next_actions.md
source_context.md
qa/source_verification.md when citations/sources support central claims
qa/artifact_mapping.md when a legacy/equivalent artifact path is used
qa/gate_status.yaml for machine-readable readiness
data/README.md or docs/data_construction.md
docs/variable_definitions.md or key_variables.md
data_context.md
eda/summary_statistics.md
eda/data_quality_report.md
eda/merge_support_report.md
```

`data_context.md` is required when writing will need to describe data meaning. It should cover producer, documentation, reporting regime, coverage, measurement caveats, source vintage, and what each core measure can and cannot support.

EDA artifacts are required before pilot promotion and before any candidate finding is treated as more than exploratory. Summary statistics must document sample support rather than decorate the paper.

Also create or update spec locks under `specs/` before treating analysis choices as stable:

```text
specs/main_spec.md
specs/data_spec.md
specs/preprocessing_spec.md
specs/methodology_spec.md
specs/output_spec.md
specs/spec_change_log.md
```

Use `02_workflows/specification_lock.md`. These files freeze the main empirical spine, data source/unit, preprocessing, methodology/equations/algorithms, portfolio sort choices, output mappings, and later spec changes.

## Stage B. Weak viability gate

Use `04_templates/viability_gate_template.md`.

Decision rule:
- `VERDICT: PASS` if there is reasonable hope that the main idea can be tested credibly enough to justify the next stage.
- `VERDICT: KILL` only if the core test is structurally impossible with current data.

Kill-level failures:
- no usable outcome for the headline prediction
- no meaningful treatment, exposure, or predictor variation
- no defensible comparison group or counterfactual structure
- no within-unit, pre/post, or treated-vs-control support when the intended design requires it
- too few treated units, effective clusters, or usable periods for the claimed design
- power failure for reasonable quantities
- minimum defensible restrictions leave a trivial estimating sample

Do not kill for:
- likely null results
- weak heterogeneity power
- uncertainty about best specification
- weak story before exploration
- need for reframing

If `KILL`, write `kill_memo.md` and stop unless Yeonchan overrides.

## Stage C. Focused findings packages

When the empirical direction is not yet locked, generate several focused candidate packages.

Default:
- 3-4 candidate packages
- each package: one candidate claim, 1-2 core tables, 1-2 core figures, short memo, and a critique/validation note
- each package must use the same documented data context and variable definitions

Rules:
- No package may hide sample changes, variable redefinitions, preprocessing changes, methodology changes, sorting choices, portfolio weights, or algorithm choices.
- Each package must state unit, sample, treatment/exposure, outcome, controls, FE, clustering, and output paths.
- Each package must identify why it might fail.
- Critique must check mechanical-risk tripwires and source/data context.
- Critique must distinguish unsupported claims, access-limited claims, and contradicted claims; use `04_templates/claim_verification_matrix_template.md` for central claims.

Selection:
- Select one package as the provisional empirical spine.
- Do not merge attractive pieces from multiple packages unless a new explicit integration decision is recorded in `decision_log.md` and the merged spine is re-audited.

## Stage D. Reduced extension and architecture stress test

After selecting a candidate findings package, run targeted extension lanes before locking a paper architecture.

Default extension lanes:
1. identification and design threats
2. measurement and data support
3. heterogeneity or mechanism plausibility
4. robustness and alternative explanations

Architecture lenses:
- empirical rigor
- novelty
- scope control
- narrative coherence
- real-world stakes

Default output:
```text
extension_brief_identification.md
extension_brief_measurement.md
extension_brief_heterogeneity_mechanism.md
extension_brief_robustness.md
paper_map_A.md
paper_map_B.md
argument_decision.md
```

Use two architecture proposals by default. Use more only when Yeonchan wants broad exploration.

## Stage E. Audit issue ledger

Create `audit_issue_ledger.md` no later than the first architecture/data audit.

Use `04_templates/audit_issue_ledger_template.md`.

Rules:
- One row per issue.
- Never delete rows.
- Update status in place: `OPEN`, `RESOLVED`, `REFRAMED`, `DROPPED`, or `ACCEPTED_LIMITATION`.
- Any unresolved `BLOCKING` issue prevents Gate 2 pass.
- A numeric match does not resolve a conceptual, mechanical, identification, or measurement issue.

## Mechanical-risk tripwires

Flag a result when:
- treatment/exposure and outcome share a denominator
- outcome is a residual, complement, or sum-to-one component
- heterogeneity may reflect baseline levels or room-to-move
- treatment and outcome are constructed from the same raw source
- sample restrictions select on the outcome or a close correlate
- merge/drop patterns are correlated with treatment or outcome
- a confirmation test is algebraic rather than independent evidence
- unit of observation differs from the argument's implied unit

Default action:
- record an issue in `audit_issue_ledger.md`
- require companion evidence: counts, levels, alternate denominators, independent measures, placebo structure, or raw-source validation
- downgrade or drop headline claim if companion evidence is missing

## Stage F. Sample support and dropped findings before prose

Before prose writing, create:
- `sample_support.md` from `04_templates/sample_support_template.md`
- `dropped_findings.md` from `04_templates/dropped_findings_template.md`
- locked spec files under `specs/` or a combined `specs/spec_lock.md` with all required fields
- `qa/claim_verification_matrix.md` from `04_templates/claim_verification_matrix_template.md` when central claims enter prose
- `qa/integrity_gate.md` when writing kickoff or review-readiness is the next step
- `qa/gate_status.yaml` before writing handoff or review-readiness
- `qa/waiver_log.md` when any gate/rule is overridden or skipped
- `qa/invalidation_ledger.md` when locked specs, central outputs, or central claims changed

These become part of the writing evidence packet.

Writing may not:
- infer sample support from scattered table notes
- resurrect dropped findings in introduction, discussion, conclusion, or abstract
- present open `BLOCKING` issues as resolved

## Gate 1. Replication and number QA

Trigger:
- stable draft or stable table/figure package exists
- before final claim-validity review

Inputs:
- manuscript or memo with empirical claims
- tables and figures
- logs and scripts
- data construction and variable documentation
- sample support
- dropped findings
- audit issue ledger
- active spec lock files: main, data, preprocessing, methodology, output, and change log

Checks:
- every reported number traces to table/log/output
- code implements the described locked specification
- controls, fixed effects, clustering, sample restrictions, horizons, transformations, weights, sorting bins, breakpoints, algorithms, hyperparameters, and seeds match the locked specs and methods text
- tables and figures were generated from the claimed data and scripts
- dropped findings did not reappear without clearance
- sample-path claims match `sample_support.md`

Optional first-pass helper:
```bash
python3 /Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/scripts/verify_paper_numbers.py <paper.tex> --roots <project_root> --out <report.md>
```

Verdict line:
```text
GATE1: PASS
GATE1: REOPEN_ANALYSIS
```

Gate 1 may resolve replication issues. It does not resolve mechanical, identification, or claim-validity issues merely because numbers match.

## Gate 2. Estimand and claim-validity QA

Trigger:
- Gate 1 has run
- manuscript claims are near final

Checks:
- Gate 1 replication/number QA is passed or unresolved issues are clearly carried forward
- all claims point to locked, non-superseded specs
- central claims have rows in canonical `qa/claim_verification_matrix.md`; legacy/equivalent paths count only if mapped in `qa/artifact_mapping.md`
- key sources/citations pass source verification or unresolved access/source limitations are visible
- conceptual argument aligns with actual findings
- headline claims are not mechanically exposed
- causal language matches design strength
- unresolved `BLOCKING` issues have explicit resolution, reframing, or exclusion
- appendix/body placement does not hide necessary caveats
- tables/figures support the stated interpretation

Verdict line:
```text
VERDICT: PASS_WITH_DIRECT_FIXES
VERDICT: REOPEN_TEXT
VERDICT: REOPEN_ANALYSIS
```

Use `PASS_WITH_DIRECT_FIXES` only if remaining issues are non-blocking or directly fixable without new analysis.

Use `REOPEN_TEXT` when the evidence exists but claims need narrowing, caveats, or restructuring.

Use `REOPEN_ANALYSIS` when new regressions, regenerated tables/figures, data changes, or specification changes are required.

Gate 2 cannot pass while `audit_issue_ledger.md` contains unresolved `BLOCKING` rows.

## Integrity gate handoff

After Gate 2, run `01_policies/integrity_gate_policy.md` when any of these apply:
- writing kickoff will begin
- referee audit or submission-readiness review will begin
- major revision changed evidence, specs, claims, or exhibits
- locked spec changed and invalidated downstream outputs or prose

The integrity gate is fail-closed. A polished manuscript cannot override unresolved source, spec, provenance, or claim-support blockers. Update `qa/gate_status.yaml`; machine-readable blocked status overrides optimistic prose summaries.

## Relationship to referee audit

These gates are internal project gates. The independent referee audit still applies before submission or replication-package release.

Use this workflow to make the final referee audit less likely to find preventable number, support, and claim-calibration failures.
