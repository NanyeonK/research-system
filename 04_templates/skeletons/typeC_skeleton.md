# Type C Forecasting Skeleton

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

Claim: Name the forecasting target, decision context, and failure of current benchmarks.
Exhibit: None or Figure 1 target/horizon hook.
Expected literature category: Forecasting benchmark papers.

Paragraph 2

Claim: Explain what changes in information, model class, horizon, or evaluation makes the paper distinct.
Exhibit: Figure 1 hook candidate, usually horizon-performance or target structure visual.
Expected literature category: Forecasting methods and target-construction papers.

Paragraph 3

Claim: State the contribution as forecast improvement, stability, uncertainty, or economic value.
Exhibit: Exhibit map preview.
Expected literature category: Closest forecasting comparators.

Paragraph 4

Claim: Define what the paper does not claim, especially causal interpretation.
Exhibit: None.
Expected literature category: Forecast evaluation literature.

### Data and Forecast Task

Paragraph 1

Claim: Define target, horizons, forecast origin, sample period, and information set.
Exhibit: Table 1 summary.
Expected literature category: Target and data-source papers.

Paragraph 2

Claim: Define benchmark models and candidate model families.
Exhibit: Model comparison table or text.
Expected literature category: Forecasting benchmark literature.

Paragraph 3

Claim: State leakage controls and train-test split discipline.
Exhibit: Design schematic or appendix.
Expected literature category: Forecast evaluation standards.

### Evaluation Design

Paragraph 1

Claim: Define loss functions, test windows, rolling or expanding design, and comparison tests.
Exhibit: Spec reference or design exhibit.
Expected literature category: Forecast comparison tests.

Paragraph 2

Claim: Explain uncertainty or interval evaluation when relevant.
Exhibit: Uncertainty exhibit.
Expected literature category: Prediction interval and calibration literature.

Paragraph 3

Claim: Map performance claims to metrics and economic interpretation.
Exhibit: Exhibit map.
Expected literature category: Economic value of forecasts literature.

### Main Results

Paragraph 1

Claim: Present main forecast performance against benchmarks.
Exhibit: Table 2 main.
Expected literature category: Direct benchmark threats.

Paragraph 2

Claim: Explain where gains occur across horizons, states, or target definitions.
Exhibit: Figure 1 or performance curve.
Expected literature category: State-dependent forecasting papers.

Paragraph 3

Claim: State whether gains are statistically and economically meaningful.
Exhibit: Main table and economic value exhibit.
Expected literature category: Forecast evaluation papers.

### Robustness and Diagnostics

Paragraph 1

Claim: Show robustness across windows, horizons, metrics, or benchmark sets.
Exhibit: Table 3 robustness.
Expected literature category: Forecast robustness standards.

Paragraph 2

Claim: Diagnose failure cases and instability rather than hiding them.
Exhibit: Diagnostics figure.
Expected literature category: Model stability literature.

Paragraph 3

Claim: State operational limits of using the forecast.
Exhibit: None or appendix.
Expected literature category: Deployment or decision-support literature.

### Conclusion

Paragraph 1

Claim: Restate the forecasting contribution at verified claim strength.
Exhibit: None.
Expected literature category: Forecasting literature.

Paragraph 2

Claim: State what future data or model change could improve the task.
Exhibit: None.
Expected literature category: Adjacent forecasting papers.

## Skeleton-writer handoff checks

- [ ] Each paragraph has one claim only.
- [ ] Each claim maps to a verified source, result, or exhibit.
- [ ] Figure 1 hook is selected or three candidates are preserved for Human Gate 2.
- [ ] Literature categories include direct threats, not only background.
- [ ] No paragraph asks writing system to solve a research uncertainty.
