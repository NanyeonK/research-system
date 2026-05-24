# Audit Issue Ledger

Purpose: persistent cross-step tracker for empirical, data, measurement, mechanical, identification, replication, citation, and claim-calibration issues.

Rules:
- Create no later than the first data/architecture audit.
- Never delete rows.
- Update status in place.
- A numeric match does not resolve conceptual, mechanical, measurement, or identification issues.
- Gate 2 cannot pass while any `BLOCKING` row remains unresolved.

| Issue ID | First Raised In | Category | Severity | Blocking Until | Status | Notes |
|---|---|---|---|---|---|---|
| I001 |  | data / measurement / mechanical / methods / identification / replication / citation / claim-calibration | BLOCKING / MAJOR / MINOR | viability / Gate1 / Gate2 / submission / none | OPEN / RESOLVED / REFRAMED / DROPPED / ACCEPTED_LIMITATION |  |

## Category guide

- `data`: source coverage, merge, sample construction, missingness, raw-vs-derived ambiguity.
- `measurement`: variable validity, producer/reporting rules, construct mismatch.
- `mechanical`: shared denominator, residual/complement, sum-to-one, room-to-move, same-source treatment/outcome, algebraic confirmation.
- `methods`: specification, controls, FE, clustering, inference, power, design assumptions.
- `identification`: counterfactual, parallel trends, exclusion, sorting, endogeneity, timing.
- `replication`: number mismatch, code-paper mismatch, table/figure generation issue.
- `citation`: missing, hallucinated, wrong-context, or unsupported citation.
- `claim-calibration`: prose overclaims relative to evidence.

## Severity guide

- `BLOCKING`: prevents headline claim, Gate 2 pass, or submission until resolved/reframed/dropped.
- `MAJOR`: must be addressed before submission but may not block intermediate work.
- `MINOR`: local fix or disclosure issue.

## Status guide

- `OPEN`: live issue.
- `RESOLVED`: fixed by code, data, evidence, or verified correction.
- `REFRAMED`: issue remains but claim was narrowed so it no longer blocks.
- `DROPPED`: affected claim/result was removed from the paper spine.
- `ACCEPTED_LIMITATION`: limitation is disclosed and non-blocking by explicit decision.
