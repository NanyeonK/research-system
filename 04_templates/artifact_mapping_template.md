# Artifact Mapping Template

Use this file as `qa/artifact_mapping.md` only for legacy projects or onboarding projects whose current files do not yet match the canonical research-system paths.

## Canonical artifact rule

Active research-paper projects should use the canonical artifact paths below. "Equivalent" artifacts are allowed only during onboarding, legacy migration, or a documented compatibility period.

Equivalent artifacts do not weaken gates. If a canonical path is not used, this mapping must exist before writing kickoff, exhibit `FIX`, referee audit, submission-readiness review, or autonomous owner launch.

## Required canonical artifacts

```text
project_state.md
decision_log.md
next_actions.md
source_context.md
specs/main_spec.md
specs/data_spec.md
specs/preprocessing_spec.md
specs/methodology_spec.md
specs/output_spec.md
specs/spec_change_log.md
qa/source_verification.md
qa/claim_verification_matrix.md
qa/integrity_gate.md
qa/gate_status.yaml
```

Conditionally required artifacts:

```text
qa/artifact_mapping.md              # required when any equivalent path is used
qa/waiver_log.md                    # required when any gate/rule is overridden or skipped
qa/invalidation_ledger.md           # required after locked spec changes or major revision invalidates outputs/claims
qa/threat_literature_matrix.md      # required when novelty, contribution, closest-threat, or literature-positioning claims enter prose
qa/audit_issue_ledger.md            # required when empirical/data/measurement/mechanical/identification issues have been raised
sample_support.md                   # required when writing uses sample path, match rates, treatment support, or subgroup support
dropped_findings.md                 # required when candidate results were rejected or narrowed
data_context.md                     # required when data producer/reporting rules affect interpretation
```

## Mapping table

| canonical_name | actual_path | reason | migration_status | owner | date | gate impact |
|---|---|---|---|---|---|---|
| project_state.md |  | legacy / existing project / compatibility | OPEN / MIGRATING / CANONICALIZED |  | YYYY-MM-DD | blocks writing/referee/submission until mapped |

## Rules

- Do not create a mapping row for convenience if the canonical file can be created directly.
- Do not treat an unmapped equivalent as evidence.
- Do not mark a gate `PASS` when a required canonical artifact is missing and no mapping row exists.
- Mark `migration_status: CANONICALIZED` only after the canonical file exists and future agents no longer need the equivalent path.
