# Type A Empirical Asset Pricing Skeleton

Status: base template for v2 Phase 4 skeleton-writer. Fork this file into `04_skeleton/section_skeleton.md` and fill it from project evidence. Do not use it as prose.

Rules

- Every paragraph needs one claim, one evidence source, one exhibit link if relevant, and one expected literature category.
- Figure 1 hook belongs in the introduction, usually the last third before the contribution paragraph.
- Claims must match `qa/claim_verification_matrix.md`.
- Unsupported claims return to Phase 3 or Phase 4, not to prose polishing.


## Exhibit spine

- Figure 1 hook: `<fig01_hook_candidate>` in the introduction, normally after motivation and before contribution.
- Table 1 summary: sample or object definition.
- Table 2 main: central result or mechanism.
- Table 3 robustness: claim stability and boundary.

## Section map

### Introduction

Paragraph 1

Claim: Name the pricing puzzle or return pattern and state why it matters for asset-pricing tests.
Exhibit: None or Figure 1 if the hook is a return spread or factor failure visual.
Expected literature category: Direct anomaly or factor-pricing threat papers.

Paragraph 2

Claim: Explain the economic channel or measurement innovation that makes the project distinct.
Exhibit: Figure 1 hook candidate, usually a portfolio spread, factor exposure map, or pricing-error visual.
Expected literature category: Mechanism papers and factor construction papers.

Paragraph 3

Claim: State the paper response as a testable asset-pricing contribution with claim boundaries.
Exhibit: Exhibit map preview.
Expected literature category: Closest empirical asset-pricing comparators.

Paragraph 4

Claim: List contributions without overstating novelty beyond verified threats.
Exhibit: None.
Expected literature category: Recent working papers and survey or synthesis papers.

### Data and Portfolio Construction

Paragraph 1

Claim: Define asset universe, sample period, returns, filters, and portfolio construction.
Exhibit: Table 1 summary.
Expected literature category: Data-provider and portfolio construction standards.

Paragraph 2

Claim: Explain factor, signal, or characteristic measurement and timing.
Exhibit: Appendix or construction exhibit if needed.
Expected literature category: Measurement and factor methodology papers.

Paragraph 3

Claim: State exclusions, missingness, and look-ahead protections.
Exhibit: Sample flow or summary table.
Expected literature category: Replication and data-quality norms.

### Empirical Design

Paragraph 1

Claim: Define main test, benchmark model, and estimand.
Exhibit: Spec reference, not final exhibit unless needed.
Expected literature category: Asset-pricing test methodology.

Paragraph 2

Claim: Explain standard errors, clustering, horizons, and multiple-testing discipline.
Exhibit: None or diagnostics table.
Expected literature category: Inference and multiple-testing literature.

Paragraph 3

Claim: Map each main claim to a table or figure.
Exhibit: Exhibit map.
Expected literature category: Closest design comparators.

### Main Results

Paragraph 1

Claim: Present the central pricing result and magnitude.
Exhibit: Table 2 main.
Expected literature category: Direct threat papers.

Paragraph 2

Claim: Explain whether the result survives benchmark factor controls.
Exhibit: Table 2 or Figure 1 if visual.
Expected literature category: Factor model and omitted factor literature.

Paragraph 3

Claim: State economic significance without converting it into welfare or policy claims unless supported.
Exhibit: Main table or figure.
Expected literature category: Economic magnitude conventions.

### Robustness and Mechanism

Paragraph 1

Claim: Show stability across allowed sample, weighting, or factor choices.
Exhibit: Table 3 robustness.
Expected literature category: Robustness standards in empirical asset pricing.

Paragraph 2

Claim: Test the proposed mechanism or reject unsupported alternatives.
Exhibit: Mechanism exhibit.
Expected literature category: Mechanism-specific literature.

Paragraph 3

Claim: Define the boundary conditions where the claim does not hold.
Exhibit: Robustness table or appendix.
Expected literature category: Null or conflicting evidence papers.

### Conclusion

Paragraph 1

Claim: Restate the asset-pricing contribution at the verified claim strength.
Exhibit: None.
Expected literature category: Direct threat papers.

Paragraph 2

Claim: State what future work should test without introducing new claims.
Exhibit: None.
Expected literature category: Adjacent asset-pricing literature.

## Skeleton-writer handoff checks

- [ ] Each paragraph has one claim only.
- [ ] Each claim maps to a verified source, result, or exhibit.
- [ ] Figure 1 hook is selected or three candidates are preserved for Human Gate 2.
- [ ] Literature categories include direct threats, not only background.
- [ ] No paragraph asks writing system to solve a research uncertainty.
