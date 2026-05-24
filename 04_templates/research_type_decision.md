# Research Type Decision Tree

Purpose: classify a v2 project into one research type when the topic spans more than one domain. Fork this file only as a routing note if classification is contested. Otherwise record the result in `project_state.md` under `research_type`.

Entry question

What is the main contribution?

## Primary routing

If the main contribution is about returns, risk, portfolios, factors, cross-sectional pricing, anomalies, or asset-pricing tests, route to Type A empirical asset pricing.

If the main contribution is about housing, rent, commercial property, spatial exposure, local markets, transactions, appraisals, amenities, zoning, or urban economic structure, route to Type B real estate empirics.

If the main contribution is about prediction performance, forecast horizon design, nowcasting, forecast comparison, rolling evaluation, benchmark design, target construction, or predictive economic value, route to Type C forecasting.

If the main contribution is about model behavior, interpretability, uncertainty quantification, explanation validity, feature behavior, counterfactuals, or model-assisted decision support, route to Type D interpretable ML in finance.

If the main contribution is about institutional design, market design, governance, disclosure, legal architecture, tokenization structure, payment rails, contracting, or conceptual mechanism design, route to Type E conceptual or institutional.

## Ambiguous cases

### Real estate plus ML

If interpretability, model behavior, explanation validity, or uncertainty quantification is the main contribution, route to Type D interpretable ML in finance.

If the real-estate market question is the main contribution and ML is a tool for measurement, prediction, heterogeneity, or robustness, route to Type B real estate empirics.

### Asset pricing plus ML

If the anomaly, factor, return cross-section, risk premium, or portfolio result is the main contribution, route to Type A empirical asset pricing.

If the ML model's behavior, uncertainty, explanation, or decision-support role is the main contribution, route to Type D interpretable ML in finance.

### Tokenization plus asset pricing

If institutional architecture, governance, contract design, disclosure, legal structure, or market plumbing is the main contribution, route to Type E conceptual or institutional.

If the return cross-section, pricing kernel, risk premium, portfolio behavior, or traded-asset test is the main contribution, route to Type A empirical asset pricing.

## Tie-break rules

Do not classify by data source. Classify by the claim that would remain in the title and abstract if only one contribution could survive.

Do not classify by preferred method. A forecasting model used to estimate a real-estate market question is not Type C unless forecast performance or horizon design is the paper's central contribution.

Do not classify by exhibit convenience. The research type determines the base skeleton and exhibit map. It does not prevent the project from borrowing a secondary exhibit format when the evidence requires it.

If two types remain equally plausible after the entry question, record both candidates in `decision_log.md`, choose the type that controls the Human Gate 2 decision, and mark the other as `secondary_type` in `project_state.md`.
