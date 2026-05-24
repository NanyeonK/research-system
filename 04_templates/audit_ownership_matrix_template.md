# Audit Ownership Matrix Template

Purpose: separate deterministic/machine checks from human scholarly judgment. Use with `qa/gate_status.yaml`, `qa/integrity_gate.md`, referee audit, and writing handoff.

## Metadata

Project:

Date:

Reviewer:

Phase:

## Ownership Matrix

| audit_item | artifact | machine_check | human_check | owner | blocking_if_unresolved | status | notes |
|---|---|---|---|---|---|---|---|
| Canonical artifact presence | project root / `qa/artifact_mapping.md` | file exists, mapped paths exist | mapping rationale is acceptable | machine then human | YES | OPEN |  |
| Gate status vocabulary | `qa/gate_status.yaml` | YAML parse, allowed labels, blocked flag | status accurately reflects project state | machine then human | YES | OPEN |  |
| Spec lock completeness | `specs/*.md` | `LOCK_STATE`, `LOCK_ELIGIBLE`, required sections present | spec choices are intellectually defensible | machine then human | YES | OPEN |  |
| Data source verification | `qa/source_verification.md`, `specs/data_spec.md` | identifiers, URLs, producer fields present | data source is appropriate for the claim | machine then human | YES | OPEN |  |
| Literature map | `ideas/literature_map.md` or `qa/literature_map.md` | graph/report/index IDs/URLs recorded | literature coverage and threat assessment are adequate | machine then human | YES before promotion/writing | OPEN |  |
| Claim support | `qa/claim_verification_matrix.md` | every central claim has source/output/spec IDs | claim wording is properly narrowed | machine then human | YES | OPEN |  |
| Numbers in prose | manuscript, tables, backing data | numeric string/table matching | interpretation is correct and material | machine then human | YES before submission | OPEN |  |
| Table/figure reproducibility | `output/`, scripts, manifests | paths/scripts/data exist; rerun status if available | exhibit is publishable and worth showing | machine then human | YES before FIX | OPEN |  |
| Identification / causal language | specs, tables, manuscript claims | flags causal words and missing design fields | identification is credible enough for wording | human primary | YES | OPEN |  |
| Mechanism interpretation | output, source context, manuscript skeleton | links mechanism claim to exhibit/source rows | mechanism is convincing and not overclaimed | human primary | YES | OPEN |  |
| Waivers / limitations | `qa/waiver_log.md` | waiver file exists when needed | accepted risk is acceptable and claim narrowing is sufficient | human primary | YES when central | OPEN |  |
| Invalidation after changes | `qa/invalidation_ledger.md` | open stale outputs/claims detected | reanalysis scope is sufficient | machine then human | YES | OPEN |  |
| Section and paragraph claim plan | `paper/section_paragraph_map.md` | every paragraph has one sentence and support IDs | section order and contribution story are publishable | human primary | YES before paragraph drafting | OPEN |  |

## Machine Audit Scope

Machine may pass/fail:
- file existence and canonical path mapping
- schema parse and allowed status vocabulary
- URL/DOI/OpenAlex/Crossref/Semantic Scholar identifier presence
- obvious citation metadata mismatch
- numeric consistency between manuscript text, tables, and machine-readable outputs
- unresolved `BLOCKED`, `OPEN`, `SUPERSEDED`, or stale states
- missing support IDs for claims, exhibits, sections, and paragraphs

Machine must not decide alone:
- novelty is sufficient
- identification is credible
- mechanism is economically meaningful
- exhibit is publishable
- target journal fit is realistic
- waiver risk is acceptable
- causal wording is justified beyond mechanical flag checks

## Human Audit Scope

Human must decide:
- whether the idea is worth starting despite risks
- whether the literature map is substantively complete enough
- whether the main design answers an economics/finance question
- whether fixed tables/figures are publishable and worth building prose around
- whether each section and paragraph plan tells the intended story
- whether limitations/waivers are acceptable

## Final Audit Split

Machine gate verdict: PASS | PASS_WITH_LIMITATIONS | REVISE | BLOCKED

Human gate verdict: PASS | PASS_WITH_LIMITATIONS | REVISE | BLOCKED | NOT_REVIEWED

If machine and human disagree, stricter verdict controls unless Yeonchan records an override in `decision_log.md` and `qa/waiver_log.md`.
