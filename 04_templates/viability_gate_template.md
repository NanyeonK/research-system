# Viability Gate

At the top, write exactly one line:

```text
VERDICT: PASS
```

or

```text
VERDICT: KILL
```

Use a deliberately weak screen. Pass unless the core empirical test is structurally impossible with current data.

## Headline Prediction

State the one main prediction screened.

## Proposed Main Test

- Outcome:
- Treatment / exposure / predictor:
- Unit of observation:
- Minimum sample restrictions:
- Design family:
- Controls / fixed effects / clustering, if known:
- Required comparison or counterfactual:

## Minimal Support Checks

Be quantitative where possible.

- Usable outcome exists:
- Meaningful treatment/exposure variation:
- Defensible comparison group:
- Within-unit / pre-post / treated-control variation if required:
- Effective treated units / clusters / periods:
- Main estimating sample after minimum restrictions:
- Power / minimum detectable effect / CI-width diagnostic:

## Decision

Explain why the project passes or fails under this weak screen.

## If KILL: Revival Condition

If `VERDICT: KILL`, also write `kill_memo.md` with:
- research question
- screened headline prediction
- proposed main test
- 3-5 concrete non-viability facts
- data or design change needed to revive
