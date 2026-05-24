# Specification Lock Workflow

Purpose: force every research project to freeze the exact empirical object before claims, tables, writing, or review harden.

Core rule:
- A research result is not stable until the relevant specs are locked in writing.
- A table, figure, paragraph, abstract, slide, or referee response may only use locked specs or explicitly marked exploratory specs.
- Changing a locked spec requires a new version, a decision-log entry, and downstream invalidation/revalidation of affected outputs.

## When to use

Use this workflow when:
- moving from exploration to main empirical spine
- choosing a main portfolio construction, sorting design, sample, model, or algorithm
- creating candidate findings packages
- marking any table or figure as `FIX`
- starting writing kickoff
- running Gate 1 number QA or Gate 2 claim-validity QA
- preparing submission or replication package

## Lock states

Every spec artifact must declare one state at the top:

```text
LOCK_STATE: EXPLORATORY
LOCK_STATE: PROVISIONAL_LOCK
LOCK_STATE: LOCKED
LOCK_STATE: SUPERSEDED
```

Meaning:
- `EXPLORATORY`: may be changed freely; cannot support final prose.
- `PROVISIONAL_LOCK`: chosen for the next batch of analysis; changes require a decision-log entry.
- `LOCKED`: main paper contract; changes require version bump, decision-log entry, and downstream revalidation.
- `SUPERSEDED`: no longer active; preserve for provenance.

## Required lock files

At minimum, maintain these canonical files:

```text
specs/main_spec.md
specs/data_spec.md
specs/preprocessing_spec.md
specs/methodology_spec.md
specs/output_spec.md
specs/spec_change_log.md
```

Use templates:
- `04_templates/main_spec_lock_template.md`
- `04_templates/data_spec_lock_template.md`
- `04_templates/preprocessing_spec_lock_template.md`
- `04_templates/methodology_spec_lock_template.md`
- `04_templates/output_spec_lock_template.md`
- `04_templates/spec_change_log_template.md`

For small or legacy projects, one combined `specs/spec_lock.md` is allowed only during onboarding or compatibility migration, only if it contains all required fields from the templates, and only if `qa/artifact_mapping.md` or `project_state.md` maps the combined file to each canonical spec path.

## Main spec lock

Purpose: freeze what the paper's main empirical object is.

Must include:
- research question
- main outcome or target variable
- main treatment, exposure, predictor, signal, or strategy
- main unit of observation
- main sample and time range
- main estimand or predictive target
- main identification or evaluation design
- main table/figure spine
- accepted vs rejected empirical branches
- what the paper will not claim

Portfolio-specific fields, when relevant:
- sorting variable(s)
- sort timing and rebalance frequency
- number of bins or dimensions, e.g. `5x5`, `10x1`, `tercile x tercile`
- independent vs sequential sorts
- breakpoints: NYSE, full sample, country-specific, rolling, expanding, fixed-period
- portfolio weights: value-weighted, equal-weighted, capped, liquidity-adjusted
- holding period and skip period
- return definition: raw, excess, log, arithmetic, delisting-adjusted
- benchmark/factor model
- transaction costs and constraints
- long-short construction
- inference method: time-series SE, Newey-West lag, block bootstrap, Fama-MacBeth, clustered panel SE

Forecasting/ML-specific fields, when relevant:
- target horizon
- train/validation/test split design
- rolling or expanding window rules
- feature availability timestamp and leakage controls
- hyperparameter tuning protocol
- metric hierarchy
- baseline models
- seed policy

Real-estate/panel-specific fields, when relevant:
- unit: parcel, building, store, listing, transaction, grid, district, census tract, station catchment
- spatial join rule and boundary vintage
- time unit and aggregation rule
- treatment/exposure timing
- rent/price outcome definition
- fixed effects, controls, clustering
- panel balance and attrition treatment

## Data spec lock

Purpose: freeze data source identity and unit meaning.

Must include for each source:
- producer / owner
- raw location and access path
- version, vintage, date accessed
- license/use restriction if known
- raw unit of observation
- time coverage
- geography coverage
- key identifiers
- raw row counts and unique key counts
- source documentation path or citation
- known coverage gaps and measurement caveats
- raw-vs-derived variable boundary

No derived result may cite a dataset whose source, vintage, unit, and row-count baseline are missing.

## Preprocessing spec lock

Purpose: freeze transformations between raw data and analysis panel.

Must include:
- raw input files/tables
- cleaning rules
- filters and exclusions
- deduplication rule
- missing-value handling
- winsorization/trimming/outlier policy
- variable construction formulas
- merge/join keys and join type
- geographic/spatial joins
- time alignment and lag/lead construction
- aggregation/disaggregation rules
- train-only fitting rules for scalers/encoders/features
- row-count ledger after each major step
- output analysis panel path and schema

Every major preprocessing step must have a count diagnostic. If counts are unknown, the spec is not locked.

## Methodology spec lock

Purpose: freeze equations, algorithms, estimands, and inference.

Must include:
- exact equation(s) or algorithm pseudocode
- dependent variable / target
- treatment/exposure/key regressor/signal
- controls
- fixed effects
- clustering or covariance estimator
- sample restrictions
- weighting
- hyperparameters
- random seeds
- software/package versions when package defaults matter
- model selection or tuning protocol
- primary vs secondary specifications
- robustness specifications and why they are robustness, not main

For empirical equations, write the equation in math form and map every symbol to a column name or constructed object.

For algorithms, include pseudocode and stopping/tuning rules. Do not rely on prose like "standard random forest" or "standard double ML" without the exact implementation choices.

## Output spec lock

Purpose: freeze how locked specs become tables, figures, and claim sources.

Must include:
- table/figure ID
- source script
- source data/panel
- exact spec version used
- output path
- machine-readable backing data path
- display transformation
- note/caption source
- status: `EXPLORATORY`, `REVISE`, `FIX`, `DROP`, `GAP`
- claim supported
- known caveats

No exhibit can be `FIX` unless it points to locked main/data/preprocessing/methodology specs.

## State transition discipline

Allowed transitions:

| From | To | Required evidence | Gate impact |
|---|---|---|---|
| `EXPLORATORY` | `PROVISIONAL_LOCK` | decision-log entry; minimum data/preprocessing viability check; owner/date/version filled | analysis packages may be built, but final prose still blocked |
| `PROVISIONAL_LOCK` | `LOCKED` | completeness checklist passed; required fields filled; linked specs consistent; unresolved blockers = 0 | exhibit `FIX`, writing handoff, and review may proceed only if other gates pass |
| `LOCKED` | `SUPERSEDED` | new version created; `specs/spec_change_log.md` row; `qa/invalidation_ledger.md` row; affected outputs/claims/manuscript sections listed | affected artifacts are stale until revalidated |
| `SUPERSEDED` | `LOCKED` | forbidden | create a new version instead |
| `LOCKED` | `EXPLORATORY` or `PROVISIONAL_LOCK` | forbidden | create a new version and mark old version `SUPERSEDED` |

No spec may jump from `EXPLORATORY` to `LOCKED` without a decision-log entry and documented completeness check.

## Change discipline

When a locked spec changes:
1. Create a new version header, e.g. `SPEC_VERSION: v2`.
2. Add a row to `specs/spec_change_log.md`.
3. Add a row to `qa/invalidation_ledger.md` using `04_templates/invalidation_ledger_template.md` when outputs, claims, or prose may be affected.
4. Add or update `decision_log.md`.
5. Mark affected tables/figures/manuscript paragraphs as stale.
6. Rerun required analyses or record why not needed.
7. Rerun Gate 1 and Gate 2 if any empirical claim changes.
8. Rerun/update `qa/integrity_gate.md` and `qa/gate_status.yaml` if central claims, exhibits, or writing handoff status changed.

Forbidden:
- silent changes to sample filters, FE, controls, weights, bins, sort timing, breakpoints, variable construction, source vintage, or algorithm hyperparameters
- treating a robustness spec as main because it gives cleaner results
- changing output notes/captions without updating output spec
- writing prose from exploratory outputs

## Gate checks

Before focused findings packages:
- `main_spec.md` can be `EXPLORATORY` or `PROVISIONAL_LOCK`.
- `data_spec.md` and `preprocessing_spec.md` must be at least `PROVISIONAL_LOCK`.

Before real-run dataset lock:
- `data_spec.md` must be `LOCKED`, not only `PROVISIONAL_LOCK`.
- `preprocessing_spec.md` must be `LOCKED` and include a complete row-count ledger.
- All merge keys, join types, match-rate evidence, non-match patterns, and drop reasons must be documented.
- Dataset vintage, access date, source path, license/use restriction if known, and unit-of-observation must be frozen in `specs/data_spec.md`.
- `data_context.md` must exist when data producer/reporting rules affect interpretation.
- External data used for labels, joins, enrichments, or validation must have a dedicated row in `specs/data_spec.md`.
- `eda/summary_statistics.md`, `eda/data_quality_report.md`, and `eda/merge_support_report.md` must exist or be mapped in `qa/artifact_mapping.md`.
- Agents may not proceed to real-run analysis until dataset-lock gate status is `PASS` or Yeonchan records a waiver.

Before marking an exhibit `FIX`:
- main, data, preprocessing, methodology, and output specs for that exhibit must be `LOCKED`.
- all linked audit ledger `BLOCKING` issues must be resolved, reframed, dropped, or recorded as explicit accepted limitations in `qa/waiver_log.md`.
- `qa/gate_status.yaml` must not contain blocking values for that exhibit.

Before writing kickoff:
- main spec must be `LOCKED`.
- all fixed exhibits must map to output spec rows.
- writing evidence packet must include canonical active spec lock files or mapped legacy equivalents.
- `qa/gate_status.yaml` must show writing handoff allowed.

Before submission:
- no active manuscript claim may point to a superseded or exploratory spec.
- replication package must include or reference the locked specs.
