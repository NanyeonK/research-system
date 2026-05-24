# Integrity Gate Policy

Source pattern: Imbad0202/academic-research-skills, reviewed 2026-05-21. Upstream is CC BY-NC 4.0, so this is a clean-room adaptation with attribution, not an import of upstream text.

## Purpose

The integrity gate is the research system's fail-closed checkpoint for whether a project can move from analysis into stable claims, writing, review, or submission.

It does not replace:
- `02_workflows/specification_lock.md`
- `02_workflows/paper_factory_quality_gates.md`
- `02_workflows/referee_audit.md`
- writing_system prose review

It binds them into a single pass/fail decision.

## Mandatory triggers

Run an integrity gate when any condition holds:

1. Before writing kickoff
   - Main exhibits or empirical claims are about to enter prose.
2. Before referee audit or submission-readiness review
   - The manuscript or replication package is being treated as review-ready.
3. After major revision
   - New claims, new sample, new specification, new source context, or new exhibits were added.
4. After a locked specification changes
   - Any `LOCKED` spec becomes superseded or invalidates outputs.
5. After external referee/editor comments are incorporated
   - Especially if the response changes claims or exhibit interpretation.
6. Before marking an exhibit `FIX`
   - If the exhibit supports a central claim.

## Required inputs

Minimum packet:

```text
project_state.md
source_context.md
specs/main_spec.md
specs/data_spec.md
specs/preprocessing_spec.md
specs/methodology_spec.md
specs/output_spec.md
specs/spec_change_log.md
qa/source_verification.md                 # if citations/sources support claims
qa/claim_verification_matrix.md           # required before prose claim lock
qa/threat_literature_matrix.md            # if novelty/contribution/closest-threat claims enter prose
qa/audit_issue_ledger.md                  # if paper_factory gates were used
qa/waiver_log.md                          # if any gate/rule is overridden, skipped, or accepted as limitation
qa/invalidation_ledger.md                 # if locked specs, outputs, or central claims changed
qa/gate_status.yaml                       # machine-readable readiness status
tables/ or figures/ backing data/scripts  # as applicable
manuscript draft or skeleton              # if prose exists
```

If an equivalent file name is used, record the mapping in `qa/artifact_mapping.md` or `project_state.md`. Unmapped equivalents do not count as evidence.

## Gate dimensions

### 1. Reference existence and source fit

Check:
- important citations exist and match title/author/year/DOI/version
- source claims are not overstated
- source caveats are carried into interpretation
- temporal claims respect publication/data-release dates
- closest-threat papers are not ignored
- novelty/contribution claims are backed by `qa/threat_literature_matrix.md` when they enter prose

Use:
- `references/source_verification_protocol.md`
- `source_context.md`

Blocking failures:
- hallucinated or unverified citation supports a central claim
- source says materially less than the paper claims
- source date makes the claim impossible
- closest-threat paper invalidates novelty and is not addressed

### 2. Data and provenance

Check:
- data source, unit, vintage, coverage, and access route are locked
- preprocessing ledger explains filters, joins, missingness, winsorization, and construction
- row counts and key uniqueness are documented after major transformations
- outcome/treatment/signal timing is compatible with the claim
- raw-vs-derived boundaries are clear

Use:
- `specs/data_spec.md`
- `specs/preprocessing_spec.md`

Blocking failures:
- unit of observation unclear
- source or vintage changed without spec-change log
- treatment and outcome are mechanically entangled without disclosure
- preprocessing cannot reproduce the reported panel

### 3. Specification consistency

Check:
- main question, sample, horizon, model, portfolio sort, weights, breakpoints, FE, controls, clustering, and algorithms are locked where relevant
- output spec points to the exact spec versions used
- any superseded spec has downstream invalidation marked

Use:
- `02_workflows/specification_lock.md`
- `specs/spec_change_log.md`

Blocking failures:
- manuscript/exhibit uses an exploratory or superseded spec as if fixed
- portfolio sort/VW-EW/bin/breakpoint/timing choices are undocumented
- equation or algorithm does not match code/output
- hyperparameters or seeds matter but are not recorded

### 4. Claim support

Check:
- every central claim has a row in `qa/claim_verification_matrix.md`
- claim wording matches evidence strength
- caveats are visible, not buried
- no conclusion outruns the estimand, sample, or source context

Use:
- `04_templates/claim_verification_matrix_template.md`
- `02_workflows/paper_factory_quality_gates.md` Gate 2

Blocking failures:
- central claim is unsupported, contradicted, or only access-limited
- estimated association is written as causal without design support
- robustness result is described as main result
- sample-specific result is generalized beyond sample

### 5. Output reproducibility and number consistency

Check:
- table/figure numbers trace to scripts and machine-readable backing data when feasible
- reported manuscript numbers match output artifacts
- table/figure notes identify transformations and sample restrictions
- output paths and generation scripts are stable

Use:
- `scripts/verify_paper_numbers.py` for first-pass number QA
- `specs/output_spec.md`

Blocking failures:
- manuscript number does not match source table/figure
- output generated from wrong sample or superseded spec
- no backing data/script for a central exhibit without explanation
- `qa/gate_status.yaml` marks writing or review allowed while required artifacts are missing

### 6. AI research failure-mode scan

Scan for:
- fake or misidentified citations
- hallucinated results or tables
- shortcut reliance on summaries instead of sources
- code bug converted into substantive insight
- methodology fabrication or undocumented estimator details
- frame-lock: early narrative survives contradictory evidence
- polishing that hides uncertainty or unresolved limitations

Blocking failures:
- any failure mode affects a central claim and remains unresolved
- prose improvement masks unresolved evidence/spec problems

## Waivers and overrides

Human overrides, skipped gates, and accepted limitations must be recorded in `qa/waiver_log.md` using `04_templates/waiver_log_template.md`.

Rules:
- A waiver does not convert a failed gate into `PASS`.
- A waiver records accepted risk and narrows what the manuscript may claim.
- Active waivers affecting central claims must be visible in writing handoff, referee-audit packet, and submission-readiness packet.
- If new evidence/spec changes touch a waived area, the waiver expires and must be rechecked.

## Verdicts

| Verdict | Meaning | Forward movement |
|---|---|---|
| PASS | all blocking checks clear | may proceed |
| PASS_WITH_LIMITATIONS | no blockers, but caveats must be visible | may proceed with limitation text |
| REVISE | fixable issues affect claims/artifacts | cannot proceed to FIX/submission until repaired |
| BLOCKED | central evidence/spec/provenance failure | stop; redesign or downgrade claim |

## Required output

Create or update:

```text
qa/integrity_gate.md
qa/gate_status.yaml
```

Minimum structure:

```markdown
# Integrity Gate: YYYY-MM-DD

Project:
Gate trigger:
Reviewer:
Verdict: PASS | PASS_WITH_LIMITATIONS | REVISE | BLOCKED

## Inputs checked

## Dimension verdicts
| dimension | verdict | blocking issues | required action |
|---|---|---|---|

## Claim/exhibit impacts
| claim_or_exhibit | status | reason | action |
|---|---|---|---|

## Spec invalidation check

## Source verification check

## Number/output check

## Failure-mode scan

## Final decision
```

## External review and revision loop

When the trigger is external reviewer/editor feedback:

1. Intake comments without rewriting them.
2. Classify each comment as evidence, method, framing, writing, or scope.
3. Link each comment to affected specs, claims, exhibits, or paragraphs.
4. Repair artifacts before prose when evidence/spec changes are required.
5. Re-run the integrity gate after revision.

Reviewer comments do not authorize silent spec drift.

## Machine-readable status

After the gate, update `qa/gate_status.yaml` according to `02_workflows/gate_status_protocol.md`. Markdown gate prose is not enough to mark a project writing-ready, referee-audit-ready, or submission-ready.

## Relationship to referee audit

- Integrity gate is a pass/fail evidence/spec/provenance checkpoint.
- Referee audit is adversarial review of scientific validity and submission risk.
- If integrity gate is `BLOCKED`, do not spend effort on full referee-audit prose until blockers are fixed.
- If referee audit finds new blockers, return to integrity gate after repairs.

## Read-only review rule

An integrity reviewer is read-only by default.

Allowed:
- inspect files
- identify mismatches
- classify severity
- recommend repairs

Not allowed unless explicitly assigned:
- edit manuscript claims
- patch code
- change specs
- rewrite reviewer responses

This prevents a reviewer from silently becoming the executor whose work they are supposed to audit.
