# Claim Verification Matrix Template

Use this file as `qa/claim_verification_matrix.md` when manuscript-level claims, exhibit interpretations, or literature claims are about to become stable.

## Header

Project:
Date:
Reviewer:
Gate trigger:
Related specs:
- `specs/main_spec.md`:
- `specs/data_spec.md`:
- `specs/preprocessing_spec.md`:
- `specs/methodology_spec.md`:
- `specs/output_spec.md`:

## Verdict vocabulary

| Verdict | Meaning | Required action |
|---|---|---|
| VERIFIED | Evidence supports the claim as written | may proceed |
| MINOR_DISTORTION | Direction is supported but wording/caveat needs adjustment | revise wording before FIX |
| MAJOR_DISTORTION | Claim materially overstates or misstates evidence | rewrite or downgrade claim |
| UNSUPPORTED | Evidence does not support claim | remove or replace evidence |
| ACCESS_LIMITED | Source exists but claim context cannot be fully checked | mark limitation or obtain source |
| CONTRADICTED | Stronger evidence or project output contradicts claim | stop; redesign or drop claim |

## Claim matrix

| claim_id | location | exact claim text | claim type | supporting source/output | source_context_id | spec version | exhibit/output_id | verification basis | verdict | caveat required | action | owner | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C001 | intro paragraph 2 |  | literature / data / method / result / contribution |  |  |  |  | page/table/code path |  |  |  |  | open |

## Claim type rules

### Literature claim

Must link to:
- source ID in `source_context.md`
- page/section/table if possible
- source verification row if central

Do not allow:
- broad field consensus claim from one paper
- novelty claim without closest-threat check
- temporal priority claim without date precision

### Data claim

Must link to:
- `specs/data_spec.md`
- source documentation or data context memo
- unit, coverage, and vintage

Do not allow:
- unit ambiguity
- source/vintage mismatch
- measurement caveat omitted from interpretation

### Method claim

Must link to:
- `specs/methodology_spec.md`
- equation, algorithm, estimator, or evaluation protocol
- code path if implemented

Do not allow:
- undocumented estimator variants
- default package behavior that matters but is not recorded
- robustness spec described as main spec

### Result claim

Must link to:
- table/figure/output ID
- `specs/output_spec.md`
- backing data/script path
- number QA status if numerical

Do not allow:
- causal wording without design support
- out-of-sample/general claim from in-sample evidence
- stale output from superseded spec

### Contribution claim

Must link to:
- closest-threat papers
- novelty boundary
- what the paper does not claim

Do not allow:
- “first” or “novel” without search/verification basis
- contribution broader than locked main spec

## Summary

| category | count |
|---|---:|
| verified | 0 |
| minor distortion | 0 |
| major distortion | 0 |
| unsupported | 0 |
| access limited | 0 |
| contradicted | 0 |
| open | 0 |

## Blocking issues

| issue_id | claim_id | severity | issue | required fix | status |
|---|---|---|---|---|---|

## Final gate statement

Verdict:

Proceed conditions:

Claims that must be removed/downgraded:

Claims that may proceed only with caveat:
