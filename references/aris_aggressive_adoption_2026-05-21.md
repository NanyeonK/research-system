# ARIS Aggressive Adoption Note — 2026-05-21

Source: `wanshuiyin/Auto-claude-code-research-in-sleep` (`/tmp/Auto-claude-code-research-in-sleep` reviewed 2026-05-21).
License: MIT. Pattern adoption allowed with attribution; local implementation remains Hermes/research-system native.

## Local Boundary

Adopt ARIS as research automation patterns, not as autonomous prose/gate-crossing authority.

Research system may automate:
- data collection probes
- EDA bundles
- pilot diagnostics
- manifest-driven experiment queues
- read-only stage dashboards
- cross-agent review feedback
- result-to-claim audits
- table/figure planning metadata

Research system may not automate without Yeonchan approval:
- final research decisions
- crossing human gates
- archive restoration as active evidence
- prose drafting
- exhibit `FIX` status
- submission readiness

## Adopt Immediately

1. Read-only stage dashboard indexer.
   - Local implementation: `/Users/nanyeon/.hermes/scripts/research_stage_dashboard.py`.
   - Output: `/Users/nanyeon/Documents/research_review_artifacts/RESEARCH_STAGE_DASHBOARD.md`.
   - Cron: `research-stage-dashboard-indexer`, every 10 minutes, silent unless concrete `HUMAN_AUDIT_REQUIRED` appears.

2. Pre-pilot data collection and EDA gate.
   - Required artifacts: `eda/EDA_PLAN.md`, `eda/EDA_LOG.md`, `eda/summary_statistics.md`, `eda/data_quality_report.md`, `eda/merge_support_report.md`, `eda/variable_catalog.csv`.
   - Hard stop if key/time/unit is unclear.
   - Kill memo if outcome/treatment/exposure/merge support is structurally missing.

3. Auto-feedback after pilot sub-steps.
   - Each automated pilot sub-step writes compact feedback: artifact path, EDA verdict, falsification result, next allowed action.
   - Escalation only when a concrete human decision is needed.

4. Real-run dataset lock.
   - Full analysis requires locked `data_spec.md` + locked `preprocessing_spec.md` + row-count ledger + merge support evidence + summary statistics.

5. Table/figure planning before real run.
   - Use table-builder and figure-builder metadata discipline before generation.
   - Unknowns must be `MISSING`, never invented.
   - Plans live at `output/tables/plan.md` and `output/figures/plan.md`.

## Adapt Next

- Result-to-claim gate: experiment/pilot output -> supported/partial/unsupported claim verdict.
- Experiment queue: manifest-driven multi-job scheduler for server1/server2/server3.
- Review tracing: save reviewer prompts/responses for audit accountability.
- 6-state verdict schema: `PASS`, `WARN`, `FAIL`, `BLOCKED`, `ERROR`, `NOT_APPLICABLE`.
- Kill-argument protocol: independent adversarial rejection memo + defense for mature claims.
- FigureSpec-style deterministic JSON-to-SVG diagrams for pipeline/exhibit maps.

## Skip As-Is

- ARIS autonomous paper-writing and auto-paper-improvement loops: writing boundary violation.
- Overleaf/Feishu/cloud GPU integrations: not current local stack.
- Patent and DSE-specific workflows: outside current research system scope.

## Current Policy Patches

Patched docs:
- `02_workflows/lifecycle_repo_organization.md`
- `01_policies/paper_project_framework.md`
- `02_workflows/autonomous_progression.md`
- `02_workflows/specification_lock.md`
- `02_workflows/paper_factory_quality_gates.md`
- `references/writing_system_bridge.md`

Signed: Hermes
