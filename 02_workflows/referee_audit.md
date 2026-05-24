# Referee Audit Workflow

Updated: 2026-05-08

Purpose:
- run an independent implementation, replication, and econometrics audit before submission
- create a formal referee report and author response trail inside the project
- keep audit scripts separate from author code
- reduce the chance that code errors, merge mistakes, weak automation, or specification problems reach submission

Source:
- Adapted from Scott Cunningham's `MixtapeTools` Referee 2 protocol: https://github.com/scunning1975/MixtapeTools/tree/main/skills/referee2
- Detailed upstream protocol: https://github.com/scunning1975/MixtapeTools/blob/main/personas/referee2.md
- Source evidence grade: `B` for workflow use. It is a concrete public research-audit protocol with templates, checklists, and artifact locations, but it is not manuscript literature evidence.
- Local deployment status: accepted by human instruction on 2026-04-30.

## ARIS Bridge

Read `01_policies/aris_bridge.md` first. The cross-model adversarial protocol from ARIS is core to this audit; self-audit by the same model that produced the work is rejected.

Engine skills (run as cross-model independent audits inside our five-audit framework):
- `/experiment-audit [results-dir]` — feeds Audit 1 (Code) and Audit 4 (Output Automation). Cross-model reviewer reads code and result files directly; catches fake ground truth, score normalization, phantom results, scope inflation.
- `/result-to-claim "experiment description"` — feeds Audit 5 (Econometrics). Codex MCP judgment of whether numerical results support intended claims, with verdict, supporting evidence, and missing-evidence list.
- `/paper-claim-audit [paper-dir]` — feeds Audit 5 and the manuscript-claim layer. Zero-context fresh reviewer cross-checks every numerical claim and comparison in the paper against raw evidence.
- `/citation-audit [paper-dir]` — feeds the bibliography layer. Verifies existence, metadata, and context appropriateness for every `\cite{}`. Catches hallucinated authors, wrong years, fabricated venues, and wrong-context citations.
- `/research-review "scope"` — feeds Major-Concerns / Minor-Concerns synthesis. Multi-round critical review at xhigh reasoning depth.
- `/auto-review-loop "scope" — difficulty: hard | nightmare` — drives iterative review-fix-rereview rounds when the project agent must close the audit before submission. `nightmare` lets the reviewer read the repo directly and prevents the executor from filtering reviewer context.

Binding rules:
- The ARIS executor and reviewer must be in different model families. When the human ran the analysis, the reviewer model is sufficient as long as the auditor was not the executor.
- Every ARIS audit artifact is filed under `correspondence/referee2/` or `output/diagnostics/referee2/` per our path scheme — copy or symlink ARIS default paths into our locations.
- A clean ARIS `/paper-claim-audit` does not by itself satisfy our Audit 5 (Econometrics); identification, controls, and clustering still need human-verified judgment.
- A clean ARIS `/citation-audit` is required before our final verdict can be `Accept` or `Minor Revisions`.
- ARIS `/auto-review-loop` `MAX_ROUNDS` defaults to 4; for our submission gate, override via `— MAX_ROUNDS: 2` to force human review between rounds 2 and 3.
- ARIS `HUMAN_CHECKPOINT=true` is required when the audit affects identification, reproducibility, core interpretation, or replication-package release.
- Reviewer-independence is per `aris/skills/shared-references/reviewer-independence.md`: pass file paths only, never executor summaries, never executor framings.
- Self-claims of "all closed" are rejected per `feedback_self_audit_unreliable.md`. An ARIS reviewer in a different model family must reach the verdict.

## Trigger

Use this workflow when:
- a draft, table package, or empirical pipeline is close to submission
- a major analysis batch claims to be final
- the project team is preparing a replication package
- the user asks for an adversarial audit, referee-style review, or independent replication check
- a revision response needs to verify that code changes addressed prior concerns

Do not use this workflow as a substitute for writing kickoff or exhibit decisions. Referee audit checks implementation, reproducibility, and empirical credibility after the analysis and exhibit set have stabilized.

## Independence Rule

The auditor must not be the agent that produced the analysis being audited.

The auditor should read artifacts directly rather than relying on executor summaries.

Review is read-only by default. The auditor may inspect, classify, and recommend, but must not rewrite manuscript claims, patch code, change specs, or edit response letters unless a separate repair task is explicitly assigned.

Before a full referee audit, run `01_policies/integrity_gate_policy.md` if the project is being treated as writing-ready, review-ready, submission-ready, or post-revision stable.

## Two-stage review discipline

Use a two-stage pattern when time permits:

1. Stage 1: adversarial review
   - identify major threats, minor threats, missing evidence, and misleading claims
   - classify findings as `CONSENSUS`, `SPLIT`, `ADVERSARIAL_CRITICAL`, or `LOW_CONFIDENCE`
   - do not propose prose fixes until evidence/spec implications are clear
2. Stage 2: verification review
   - after repairs, verify whether each original issue was resolved, reframed, accepted as limitation, or still open
   - do not rubber-stamp a revision because prose improved
   - if a critical adversarial finding is rebutted, require evidence-based withdrawal, downgrade, maintain, or strengthen decision

`ADVERSARIAL_CRITICAL` findings block submission-readiness unless explicitly resolved or accepted as a visible limitation by Yeonchan.

The auditor may:
- read author code
- run author code
- create independent audit scripts
- create comparison outputs
- file referee reports
- file optional audit decks

The auditor must not:
- edit author code
- rewrite author tables or figures
- silently fix data construction
- patch manuscript prose
- replace the author's pipeline with the audit pipeline

Only the author or main project agent changes author files after reading the report.

## Audit Scope

Calibrate intensity to project type:

| Project state | Required audit intensity |
|---|---|
| submission or replication package | full audit |
| dissertation or working paper draft | full audit unless data access blocks it |
| major analysis batch before writing | code, output automation, econometrics, and table/figure traceability |
| quick exploratory analysis | code and data sanity check only |
| slide deck only | use presentation/deck QA; do not run cross-language replication |

## Required Inputs

Before auditing, gather:
- project root and selected server
- current branch and environment activation method
- current manuscript path
- latest table and figure outputs
- table manifests or mapped equivalents
- analysis scripts and master run script
- data README and method docs
- writing kickoff decisions when present
- prior referee reports and author responses if this is a later round

If a required input is missing, record it as an audit limitation.

## Required Output Locations

Use project-local paths:

```text
correspondence/referee2/
  YYYY-MM-DD_round1_report.md
  response_YYYY-MM-DD_round1.md
  report_YYYY-MM-DD_round2.md

code/replication/
  referee2_*.R
  audit_referee2_*.py
  check_referee2_*.do

output/diagnostics/referee2/
  comparison_*.csv
  audit_manifest.md
```

If the project uses `src/`, `scripts/`, or `replication_package/` instead of `code/`, keep author code untouched and place audit scripts under an explicit `referee2/` or `replication/` subfolder.

## Five Audits

### 1. Code Audit

Check:
- missing value handling
- merge diagnostics and row-count checks
- duplicate handling
- variable construction
- sample filters
- loop, indexing, and date-window logic
- package defaults that may change estimates
- hardcoded paths or machine-specific assumptions

Output:
- file and line references when possible
- severity: `Major`, `Minor`, `Question`, or `No issue`
- explanation of why the issue affects estimates, interpretation, or reproducibility

### 2. Cross-Language Or Independent Replication

Goal:
- verify key numerical outputs through an independent implementation

Preferred:
- replicate in two other languages among R, Python, and Stata
- compare point estimates, standard errors, sample sizes, and key generated variables to at least six decimal places when feasible

Fallbacks:
- if cross-language replication is infeasible, write a clean-room implementation in the same language
- if raw data are unavailable, replicate from intermediate analysis-ready data
- if data cannot be accessed, use summary checks and document the limitation prominently

Output:
- audit scripts under `code/replication/` or mapped equivalent
- comparison tables under `output/diagnostics/referee2/`
- diagnosis of discrepancies as package defaults, syntax/logic errors, missing data, numerical precision, or unresolved

### 3. Directory And Replication Package Audit

Check:
- clear separation of raw, interim, processed, output, docs, paper, submit, and replication package paths
- relative paths instead of machine-specific absolute paths
- master run script or documented command sequence
- dependency and version records
- seed setting for stochastic steps
- README sufficient for another researcher to reproduce the pipeline

Output:
- replication readiness score from `1` to `10`
- concrete deficiencies
- minimal fixes required before submission or package release

### 4. Output Automation Audit

Check:
- code generates tables; the manuscript does not rely on hand-typed table values
- code generates figures; the project does not rely on manual exports as the only source
- in-text statistics link to generated outputs or carry a synchronization marker
- rerunning code regenerates the expected outputs
- table and figure notes match the generator and manifest

Output:
- status for tables: `Automated`, `Manual`, or `Mixed`
- status for figures: `Automated`, `Manual`, or `Mixed`
- status for in-text statistics: `Automated`, `Manual`, `Mixed`, or `Not checked`
- deductions and required fixes

### 5. Econometrics Audit

Check:
- identification strategy and source of variation
- estimating equation versus code
- clustering level and number of clusters
- fixed effects and possible collinearity
- controls and bad-control risk
- sample definition and exclusion rules
- pre-trends for DiD
- first stage for IV
- balance checks for RCT or RD
- magnitude plausibility
- claim strength versus design

Output:
- identification assessment
- specification concerns
- claim-strength limits
- required reruns or robustness checks

## Referee Report

File:

```text
correspondence/referee2/YYYY-MM-DD_roundN_report.md
```

Required sections:
- Summary
- Audit 1: Code Audit
- Audit 2: Cross-Language Or Independent Replication
- Audit 3: Directory And Replication Package
- Audit 4: Output Automation
- Audit 5: Econometrics
- Major Concerns
- Minor Concerns
- Questions For Authors
- Verdict
- Recommendations

Verdict labels:
- `Accept`
- `Minor Revisions`
- `Major Revisions`
- `Reject`

Do not use `Accept` unless major concerns are absent and the remaining items do not threaten implementation, reproducibility, or core interpretation.

## Author Response

The author or main project agent must respond before the next audit round.

Use:
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/templates/referee_response_template.md`

File:

```text
correspondence/referee2/YYYY-MM-DD_roundN_response.md
```

Each concern must receive one status:
- `Fixed`
- `Justified`
- `Acknowledged`
- `Deferred`
- `Disputed`

Responses must list changed files and explain why the change addresses the concern.

## Repair Loop For Automatic Progression

After a referee report, the main project agent may continue only through this bounded loop:
1. summarize each finding into a patch plan
2. classify each item as `Fixed`, `Justified`, `Acknowledged`, `Deferred`, or `Disputed`
3. patch author files only in the main project-agent role, not in the auditor role
4. rerun affected code, output, and manuscript checks
5. update the response file with changed files and validation results
6. run a targeted second audit or round-two audit for unresolved major issues

The human must decide before the project defers, disputes, or accepts any major issue that affects implementation, reproducibility, identification, or core interpretation.

## Later Rounds

For round 2 and later, the auditor must read:
- prior report
- author response
- revised code and outputs
- changed files list

The new report must classify each prior concern:
- `Resolved`
- `Adequately justified`
- `Still open`
- `Ignored`
- `New issue introduced`

## Optional Audit Deck

An audit deck may be useful for complex discrepancies or collaborator meetings.

If created, file it under:

```text
correspondence/referee2/YYYY-MM-DD_roundN_audit_deck.tex
output/diagnostics/referee2/audit_deck_YYYY-MM-DD_roundN.pdf
```

The deck must be rendered and visually checked. Use the presentation workflow or the `presentations` skill when needed.

## Integration With Existing Gates

Run this workflow after:
- code has generated major analysis outputs
- pivot review and memory sync are current
- table/figure packs have reached review-ready status
- writing kickoff has labeled main exhibits when prose has begun

Run this workflow before:
- submission
- replication package release
- final response letter
- treating the empirical pipeline as final

## Guardrails

- Do not edit author code during the audit.
- Do not inflate the verdict to avoid more work.
- Do not require cross-language replication where data restrictions make it impossible; document the limitation and use the strongest feasible fallback.
- Do not treat formatting issues as major concerns unless they block reproducibility or submission.
- Do not mark a concern resolved without rerunning the relevant check.
- Do not add external communication, submission, or deletion steps without human approval.
