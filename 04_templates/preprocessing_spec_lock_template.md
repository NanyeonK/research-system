# Preprocessing Specification Lock

LOCK_STATE: EXPLORATORY
SPEC_VERSION: v1
UPDATED: YYYY-MM-DD
OWNER:
INPUT_DATA_SPEC_VERSION:
OUTPUT_PANEL_VERSION:

## Raw Inputs

| Input ID | Source path/table | Source spec version | Expected rows | Expected unique keys |
|---|---|---|---:|---:|
|  |  |  |  |  |

## Transformation Ledger

| Step | Script/function | Operation | Input rows | Output rows | Drop/add reason | Diagnostic path |
|---|---|---|---:|---:|---|---|
| 1 |  |  |  |  |  |  |

## Cleaning Rules

- Deduplication rule:
- Missing-value handling:
- Outlier policy:
- Winsorization/trimming:
- Filters and exclusions:
- Type conversions:

## Variable Construction

| Constructed variable | Formula / algorithm | Input fields | Fit scope | Output column | Validation diagnostic |
|---|---|---|---|---|---|
|  |  |  | full sample / train only / external |  |  |

## Joins And Alignment

| Join | Left source | Right source | Keys | Join type | Expected match rate | Actual match rate | Diagnostics |
|---|---|---|---|---|---:|---:|---|
|  |  |  |  |  |  |  |  |

## Time / Spatial Handling

- Time aggregation rule:
- Lead/lag construction:
- Forecast origin alignment:
- Spatial join rule:
- Boundary vintage:
- Distance/buffer method:

## Output Analysis Panel

- Output path:
- Output unit:
- Output time range:
- Output row count:
- Output unique units:
- Schema path:
- Checksum/snapshot ID:

## Lock Decision

- Decision-log entry:
- Human approval, if required:
- Downstream methodology spec version(s):

## Lock Completeness Checklist

- [ ] input data spec version recorded
- [ ] every raw input path/table recorded
- [ ] expected rows/keys recorded
- [ ] transformation ledger has row counts after major steps
- [ ] cleaning/filter/missing/outlier rules recorded
- [ ] variable construction formulas recorded
- [ ] fit scope recorded for scalers/encoders/features
- [ ] join keys/types/match rates recorded
- [ ] time/spatial alignment rules recorded
- [ ] output panel path/schema/counts/checksum recorded
- [ ] decision-log entry linked

LOCK_ELIGIBLE: yes / no
LOCK_BLOCKERS:
