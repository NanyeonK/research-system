# Waiver Log Template

Use this file as `qa/waiver_log.md` whenever Yeonchan explicitly overrides, skips, or accepts a limitation for a research-system gate, rule, artifact, or blocker.

## Core rule

A waiver does not convert a failed gate into `PASS`.
It records an accepted risk, narrows what the paper may claim, and defines when the risk must be rechecked.

## Waiver table

| waiver_id | date | requested_by | gate_or_rule_waived | affected_claims | affected_exhibits | affected_specs | reason | risk_accepted | what_cannot_be_claimed | expiration_or_recheck_trigger | human_approval | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W001 | YYYY-MM-DD | Yeonchan |  |  |  |  |  |  |  |  | explicit / pending | ACTIVE / RECHECKED / RETIRED |

## Required notes for active waivers

- Submission or review packets must expose active waivers that affect central claims.
- Writing may proceed only within the narrowed claim boundary recorded in `what_cannot_be_claimed`.
- A waived referee audit, integrity gate issue, source limitation, or spec blocker must appear as an accepted limitation, not as an unstated clean pass.
- If new evidence/spec changes touch a waived area, the waiver expires and must be rechecked.
