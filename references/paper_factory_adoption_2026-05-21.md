# Paper Factory Adoption Decision

Source reviewed: https://github.com/nwilmers/paper_factory/tree/main
Reviewed on: 2026-05-21
Local target systems:
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/`
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/`

## License gate

The upstream repository did not include a `LICENSE` file at review time. Treat direct code or prompt import as not cleared for reuse.

Adoption policy:
- Do not copy `run_paper.sh`, `launch_agents.sh`, Stata wrappers, prompt files, style files, or scripts verbatim into the local systems.
- Adapt workflow patterns in Hermes-native and Yeonchan-native language, with attribution to the upstream repository.
- Runtime orchestration remains local: Hermes, walnut, Agent Deck, server tmux, and project-specific package/reproducibility commands.

## Adopted into research system

### 1. Weak viability gate after data/variable reconnaissance

Pattern:
- Run a permissive viability screen before full paper construction.
- `PASS` unless the core empirical test is structurally impossible.
- `KILL` only for hard failures: no usable outcome, no exposure/treatment variation, no defensible comparison, no within-unit/pre-post support when required, too few effective treated clusters, or power failure for reasonable quantities.

Local target:
- `02_workflows/paper_factory_quality_gates.md`
- `04_templates/viability_gate_template.md`

### 2. Data context as separate artifact

Pattern:
- Do not jump from data wrangling straight to results.
- Add a standalone data context memo covering producer rules, documentation, reporting regimes, coverage, measurement caveats, and variable meaning.

Local target:
- `04_templates/data_context_memo_template.md`
- writing evidence packet requirement in `references/writing_system_bridge.md`

### 3. Parallel findings packages with explicit selection

Pattern:
- Generate several focused candidate findings packages.
- Each package should be narrow: one candidate claim, 1-2 core tables, 1-2 core figures, plus validation/critique.
- Select one package to carry forward. Do not synthesize opportunistically across packages.

Local target:
- `02_workflows/paper_factory_quality_gates.md`

Local adaptation:
- Default to 3-4 packages, not six, unless the project is large enough.
- Treat this as optional for mature package-first projects that already have a fixed empirical spine.

### 4. Reduced extension and architecture layer

Pattern:
- After selecting a findings package, run targeted extension/stress-test lanes before locking paper architecture.
- Use lenses: empirical rigor, novelty, scope, narrative coherence, and stakes.

Local adaptation:
- Use four extension lanes by default:
  1. identification and design threats
  2. measurement/data support
  3. heterogeneity/mechanism plausibility
  4. robustness and alternative explanations
- Use two architecture proposals, not five, unless the human asks for broad exploration.

Local target:
- `02_workflows/paper_factory_quality_gates.md`

### 5. Persistent audit issue ledger

Pattern:
- Use one cross-step ledger for data, measurement, mechanical, methods, identification, replication, citation, and claim-calibration issues.
- Never delete rows; update status in place.
- Gate pass cannot ignore unresolved blocking issues.

Local target:
- `04_templates/audit_issue_ledger_template.md`

### 6. Mechanical-risk tripwires

Pattern:
- Treat shared-denominator, residual/complement, sum-to-one, room-to-move, and same-source treatment/outcome findings as default risks.
- Require companion evidence before using such results as headline claims.

Local target:
- `02_workflows/paper_factory_quality_gates.md`
- `04_templates/audit_issue_ledger_template.md`

### 7. Two hard manuscript-quality gates

Pattern:
- Gate 1: replication and number QA. Numbers, samples, controls, fixed effects, clustering, and method descriptions must match code/logs/tables.
- Gate 2: estimand and claim-validity QA. Even numerically correct results cannot pass if the headline claim remains mechanically or conceptually exposed.

Local target:
- `02_workflows/paper_factory_quality_gates.md`
- `scripts/verify_paper_numbers.py`

### 8. Sample support and dropped findings artifacts

Pattern:
- Before prose, create a sample support memo and a dropped findings memo.
- Writing is not allowed to resurrect discarded or weak findings without explicit clearance.

Local target:
- `04_templates/sample_support_template.md`
- `04_templates/dropped_findings_template.md`
- `references/writing_system_bridge.md`

### 9. Language-agnostic number verifier

Pattern:
- First-pass script extracts prose numbers from manuscript text and checks whether comparable numbers exist in tables/logs.
- It is not a substitute for manual audit; it flags candidates.

Local target:
- `scripts/verify_paper_numbers.py`

## Adopted into writing system

Pattern-level writing rules were routed to the sibling writing system instead of research system.

Local target:
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/references/paper_factory_writing_patterns.md`

Adopted patterns:
- Do not draft abstract until a stable paper draft exists.
- Use sample support, dropped findings, and audit issue ledger as binding inputs.
- Do not present unresolved mechanical-risk findings as standalone evidence.
- Convert AI-like prose patterns into natural academic prose without changing numbers, citations, or technical meaning.

## Skipped

Skipped for direct import:
- `run_paper.sh`: tightly coupled orchestrator.
- `launch_agents.sh`: factory-specific project manager.
- `stata_submit.sh` and `stata_wrapper.sh`: Stata-specific job runner.
- Stata-specific do-file conventions and esttab fragments.
- Raw prompt files: no license clearance, and many are runtime-specific.
- LaTeX style and bibliography files: no license clearance; use only as style inspiration if needed.

## Integration status

Integrated locally:
- `02_workflows/paper_factory_quality_gates.md`
- `04_templates/audit_issue_ledger_template.md`
- `04_templates/sample_support_template.md`
- `04_templates/dropped_findings_template.md`
- `04_templates/viability_gate_template.md`
- `04_templates/data_context_memo_template.md`
- `scripts/verify_paper_numbers.py`
- `writing_system/references/paper_factory_writing_patterns.md`

Not yet piloted:
- Run a small real project slice through viability gate + audit ledger + number verifier before treating this as fully mature.
