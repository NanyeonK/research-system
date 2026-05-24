# Type D Interpretable ML in Finance Skeleton

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

Claim: Name the finance prediction or decision problem and why black-box performance alone is insufficient.
Exhibit: None or Figure 1 interpretability hook.
Expected literature category: Interpretable ML and finance prediction threats.

Paragraph 2

Claim: Explain the interpretability object, such as feature behavior, uncertainty, explanation stability, or human decision support.
Exhibit: Figure 1 hook candidate, usually explanation or uncertainty visual.
Expected literature category: XAI, uncertainty, and finance ML papers.

Paragraph 3

Claim: State the joint contribution in predictive performance and interpretable evidence.
Exhibit: Exhibit map preview.
Expected literature category: Closest interpretable finance ML comparators.

Paragraph 4

Claim: Define limits on causal interpretation and model transportability.
Exhibit: None.
Expected literature category: ML evaluation and external validity literature.

### Prediction Task and Data

Paragraph 1

Claim: Define target, unit, horizon, feature set, sample period, and train-test design.
Exhibit: Table 1 summary.
Expected literature category: Finance prediction and data papers.

Paragraph 2

Claim: Define model families and benchmark models.
Exhibit: Model comparison table or text.
Expected literature category: ML benchmark literature.

Paragraph 3

Claim: State leakage, tuning, and validation controls.
Exhibit: Design schematic.
Expected literature category: ML validation literature.

### Interpretability Design

Paragraph 1

Claim: Define explanation method and what it is allowed to prove.
Exhibit: Method schematic or text.
Expected literature category: Interpretability methodology papers.

Paragraph 2

Claim: Define stability, uncertainty, calibration, or human-use metrics.
Exhibit: Diagnostics exhibit.
Expected literature category: XAI validation literature.

Paragraph 3

Claim: Map explanation claims to artifacts rather than prose impressions.
Exhibit: Exhibit map.
Expected literature category: Closest XAI finance papers.

### Main Results

Paragraph 1

Claim: Present predictive performance against benchmarks.
Exhibit: Table 2 main.
Expected literature category: Forecasting or classification comparators.

Paragraph 2

Claim: Present the main interpretability result and its validation.
Exhibit: Figure 1 or explanation figure.
Expected literature category: Interpretability threat papers.

Paragraph 3

Claim: Explain whether interpretation changes financial understanding or only model diagnostics.
Exhibit: Main exhibit pair.
Expected literature category: Finance mechanism literature.

### Robustness and Failure Modes

Paragraph 1

Claim: Show robustness across windows, model classes, feature groups, or explanation methods.
Exhibit: Table 3 robustness.
Expected literature category: ML robustness literature.

Paragraph 2

Claim: Report failure cases and instability explicitly.
Exhibit: Failure-mode exhibit.
Expected literature category: Model risk literature.

Paragraph 3

Claim: State deployment limits and human-use caveats.
Exhibit: None or appendix.
Expected literature category: Decision-support literature.

### Conclusion

Paragraph 1

Claim: Restate the joint ML and finance contribution at verified claim strength.
Exhibit: None.
Expected literature category: Interpretable ML in finance literature.

Paragraph 2

Claim: State next validation steps without overclaiming real-world adoption.
Exhibit: None.
Expected literature category: Model governance literature.

## Skeleton-writer handoff checks

- [ ] Each paragraph has one claim only.
- [ ] Each claim maps to a verified source, result, or exhibit.
- [ ] Figure 1 hook is selected or three candidates are preserved for Human Gate 2.
- [ ] Literature categories include direct threats, not only background.
- [ ] No paragraph asks writing system to solve a research uncertainty.
