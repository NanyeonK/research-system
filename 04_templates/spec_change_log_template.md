# Specification Change Log

Purpose: immutable ledger of changes to locked or provisionally locked research specs.

Rules:
- Never delete rows.
- Every change to source vintage, unit, preprocessing, sample, method, controls, FE, clustering, weights, bins, sorting, algorithm, hyperparameters, output notes, or claim mapping needs a row.
- If a change affects an exhibit or manuscript claim, mark downstream artifacts stale until revalidated.
- If a locked spec change affects outputs, claims, or prose, also create/update `qa/invalidation_ledger.md`.

| Change ID | Date | Spec file | From version | To version | Changed field | Reason | Decision-log entry | Downstream artifacts invalidated | Revalidation required | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| C001 | YYYY-MM-DD | specs/main_spec.md | v1 | v2 |  |  |  |  | Gate1 / Gate2 / rerun analysis / none | OPEN / VALIDATED |

## Downstream invalidation checklist

When a locked spec changes:
- [ ] affected tables marked stale or regenerated
- [ ] affected figures marked stale or regenerated
- [ ] affected manuscript paragraphs marked stale or revised
- [ ] `qa/invalidation_ledger.md` updated for affected outputs/claims/sections
- [ ] `sample_support.md` updated if sample changed
- [ ] `dropped_findings.md` updated if branch status changed
- [ ] `audit_issue_ledger.md` updated if issue status changed
- [ ] Gate 1 rerun if numbers or outputs changed
- [ ] Gate 2 rerun if claims, estimands, evidence status, or caveats changed
