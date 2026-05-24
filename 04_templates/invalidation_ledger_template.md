# Invalidation Ledger Template

Use this file as `qa/invalidation_ledger.md` after a locked spec changes, a major revision changes evidence, or any output/claim/manuscript section may have become stale.

## Core rule

Locked-spec changes invalidate downstream artifacts until revalidated. Do not rely on stale outputs, claim rows, or prose because the previous number still looks plausible.

## Invalidation ledger

| change_id | date | changed_spec | old_version | new_version | affected_outputs | affected_claims | affected_manuscript_sections | required_reruns | revalidation_status | cleared_by | cleared_date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C001 | YYYY-MM-DD | specs/main_spec.md | v1 | v2 |  |  |  | Gate1 / Gate2 / integrity gate / rerun analysis / source verification | OPEN / PARTIAL / CLEARED |  |  |

## Status rules

- `OPEN`: affected artifact cannot support writing, referee audit, or submission.
- `PARTIAL`: some affected outputs/claims cleared; unresolved rows still block affected claims.
- `CLEARED`: reruns/rechecks are complete and linked.

## Required cross-links

Every row should cross-link to:
- `specs/spec_change_log.md`
- affected output rows in `specs/output_spec.md`
- affected claim rows in `qa/claim_verification_matrix.md`
- rerun logs or output regeneration paths
- updated `qa/integrity_gate.md` when a central claim/exhibit is affected
