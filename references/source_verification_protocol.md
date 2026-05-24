# Source Verification Protocol

Source pattern: Imbad0202/academic-research-skills, reviewed 2026-05-21. Upstream is CC BY-NC 4.0, so this is a clean-room adaptation with attribution, not an import of upstream text.

## Purpose

This protocol verifies that sources used by a project actually exist, say what the project claims they say, and are appropriate evidence for the role assigned to them.

Use it before:
- a source enters `source_context.md` as manuscript evidence
- a paper citation supports a key claim
- a table/figure note names a dataset, method, or external estimate
- a literature review paragraph is marked ready for writing_system handoff
- Gate 2 claim-validity QA or integrity gate review

## Evidence role categories

Each source must have one primary role.

| Role | Meaning | Required verification |
|---|---|---|
| Manuscript evidence | supports a claim in the paper | existence + claim-context check |
| Closest-threat paper | can invalidate novelty, identification, or interpretation | existence + full-source read |
| Method reference | supports equation, estimator, algorithm, or evaluation protocol | existence + method-context check |
| Data reference | documents data source, variable, unit, coverage, or reporting regime | existence + data-context check |
| Workflow reference | informs process, not manuscript claims | existence check; do not cite as evidence unless independently read |
| Background only | useful orientation | clearly marked; cannot support a claim alone |

## Evidence grade

Grade source strength separately from project relevance.

| Grade | Meaning | Typical examples |
|---|---|---|
| A | Direct primary evidence or canonical documentation | official data documentation, published paper being replicated, legal/statistical source |
| B | Strong scholarly or technical evidence | peer-reviewed paper, working paper with code/data, established method documentation |
| C | Useful but indirect evidence | survey article, handbook, credible institutional report |
| D | Weak or context-only evidence | blog, slide deck, unverified preprint, secondary summary |
| X | Not acceptable for manuscript evidence | missing source, hallucinated citation, inaccessible unverifiable item, contradicted source |

Rules:
- A D-grade source can guide exploration but cannot be the only support for a central claim.
- X-grade sources must be removed or replaced before writing handoff.
- Workflow-source evidence must not be mixed with manuscript evidence.

## Existence verification ladder

For every important citation, verify at least one authoritative identifier or index record.

1. DOI or official landing page
   - DOI resolves to the expected title/author/year.
   - Publisher or repository page matches the cited work.
2. Scholarly index cross-check
   - OpenAlex is the default first-pass scholarly graph/index for broad literature discovery, citation metadata, related works, and field/community coverage when API access is available.
   - Crossref is preferred for DOI/metadata confirmation.
   - Semantic Scholar is useful for citation/context/related-paper expansion.
   - RePEc, NBER, SSRN, arXiv, Google Scholar, publisher pages, or field-specific indexes are used for working papers, economics/finance coverage gaps, and freshness.
   - Record which index was checked and the match quality.
   - OpenAlex presence alone does not verify claim context; full source or abstract/metadata must still be checked for the assigned role.
3. PDF or full-text artifact
   - Local path or stable URL recorded.
   - First page metadata matches citation.
4. Access-limited fallback
   - If full text is inaccessible, record what is verifiable and what remains unverified.

A source is not verified merely because a search result looks plausible.

## Match checks

Record mismatches explicitly.

| Field | Pass condition | Blocking mismatch examples |
|---|---|---|
| Title | same title or obvious subtitle/working-paper variant | different title with same author/year |
| Authors | same lead author and compatible author list | same title but different authors without explanation |
| Year | publication/working-paper version understood | cited year conflicts with source chronology |
| DOI/URL | resolves to expected source | DOI points to another article |
| Venue/version | version is known | journal article and preprint mixed without noting changes |
| Topic | source actually covers the cited claim domain | source is only loosely related |

## Claim-context verification

For any source supporting a manuscript claim, record:
- exact claim text or claim ID
- source page/section/table/figure
- quotation or paraphrase basis
- whether the project claim is narrower, equal to, or broader than the source claim
- caveats the source states
- whether the source is empirical, theoretical, review, policy, or documentation

Verdicts:
- `VERIFIED`: source supports the claim as written
- `MINOR_DISTORTION`: source supports the direction but wording/caveat needs adjustment
- `MAJOR_DISTORTION`: source is materially misrepresented
- `UNSUPPORTED`: source does not support the claim
- `ACCESS_LIMITED`: source existence verified but full claim context cannot be checked
- `CONTRADICTED`: source or stronger evidence contradicts the claim

## Data-source verification

For each data source used in `specs/data_spec.md`, verify:
- producer and access route
- raw unit of observation
- reporting frequency and time zone if relevant
- geographic boundary vintage if relevant
- variable definitions and measurement caveats
- version/vintage/access date
- license or usage restrictions
- whether the same source constructs both treatment and outcome

Data source verification must be linked to `specs/data_spec.md` and `specs/preprocessing_spec.md`.

## Temporal verification

Any claim involving chronology must record precision.

| Precision | Example | Requirement |
|---|---|---|
| day | 2024-03-31 | source date or event record |
| month | 2024-03 | source month or reporting period |
| year | 2024 | source year only; do not imply month/day |
| interval | 2020Q1-2023Q4 | start/end source and inclusion rule |
| unknown | date not established | cannot support sequence-sensitive claims |

Temporal red flags:
- citing a source as if it existed before the event it discusses
- using later revisions as evidence for earlier information sets
- mixing online publication date, print date, working-paper date, and data-release date
- claiming priority/novelty without checking preprints and working papers

## Contamination and hallucination signals

These are warnings, not automatic rejection.

Flag a source when:
- title is generic and appears only in LLM-generated contexts
- no DOI, no index record, no publisher page, and no stable repository copy
- author/year/title combination appears inconsistent across indexes
- citation appears in AI-generated bibliographies but not in scholarly indexes
- source publication date is after the text that supposedly cited it
- source has suspicious venue, fake volume/issue/page range, or impossible metadata

If flagged, either replace the source or mark it `UNVERIFIED` with a limitation.

## Output artifact

Projects may keep a source verification table in:

```text
qa/source_verification.md
```

Minimum columns:

| source_id | role | citation | index_checked | identifier | match_status | evidence_grade | claim_ids | caveats | action |
|---|---|---|---|---|---|---|---|---|---|

## Integration with local gates

- `source_context.md`: records accepted source role and caveats.
- `specs/data_spec.md`: records verified data source/unit/coverage.
- `04_templates/claim_verification_matrix_template.md`: links claims to verified sources and outputs.
- `02_workflows/paper_factory_quality_gates.md`: Gate 2 cannot pass with unresolved major source mismatches.
- `01_policies/integrity_gate_policy.md`: integrity gate checks source existence, claim context, and temporal fit.
