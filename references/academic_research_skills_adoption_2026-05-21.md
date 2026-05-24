# Academic Research Skills Adoption Review

Source reviewed: `Imbad0202/academic-research-skills`
URL: https://github.com/Imbad0202/academic-research-skills
Reviewed commit: `51ebf9dd8d54ee50fdd4c18d977dca7f58f1bb40`
Review date: 2026-05-21
Local owner: research_paper_system

Codex sibling checked: `Imbad0202/academic-research-skills-codex`
URL: https://github.com/Imbad0202/academic-research-skills-codex
Checked date: 2026-05-22
Codex package version observed: `0.1.8`
Decision update:
- The Codex sibling is useful as a packaging and router reference for Agent Deck Codex owners, but it does not change the local adoption posture.
- Do not install it wholesale into the local research system or treat `$academic-research-suite` as an automatic project owner.
- Use it as an attributed, noncommercial reference for clean-room protocol adaptation and for Codex prompt routing ideas only.
- Agent Deck integration should happen through local owner contracts, research-system gates, and one-project-one-owner sessions, not through ARS slash-command or agent-team semantics.

## License gate

Upstream license: CC BY-NC 4.0.

Decision:
- Do not import upstream code, prompts, agent files, templates, or long-form wording into the local framework.
- Use only clean-room pattern adaptation with attribution.
- Treat upstream as a noncommercial scholarly reference, not as a product component.
- Any public redistribution of adapted material should re-check license and attribution requirements.

Upstream positioning also says the system is a human-in-the-loop academic research copilot, not an autonomous paper-writing system. That aligns with the local boundary: research system governs lifecycle/evidence/specs; writing_system remains independent and paragraph-level.

## Review method

Reviewed:
- top-level docs: `README.md`, `POSITIONING.md`, `LICENSE`, `MODE_REGISTRY.md`
- skill entry points: `academic-pipeline/SKILL.md`, `deep-research/SKILL.md`, `academic-paper/SKILL.md`, `academic-paper-reviewer/SKILL.md`
- research references under `academic-pipeline/references/`
- source and literature references under `deep-research/references/`
- review and writing-boundary references under `academic-paper-reviewer/` and `academic-paper/`
- shared protocols under `shared/`

The local system already has:
- `02_workflows/specification_lock.md`
- `02_workflows/paper_factory_quality_gates.md`
- `02_workflows/source_deep_reading.md`
- `02_workflows/referee_audit.md`
- `02_workflows/autonomous_progression.md`
- `references/writing_system_bridge.md`

Therefore adoption focuses on gaps: source verification, claim verification, integrity gates, checkpoint discipline, external review handling, and optional literature-monitoring/preregistration references.

## Immediate additions integrated now

### 1. Source verification and evidence grading

Source files reviewed:
- `deep-research/references/source_quality_hierarchy.md`
- `deep-research/references/semantic_scholar_api_protocol.md`
- `deep-research/references/openalex_api_protocol.md`
- `deep-research/references/crossref_api_protocol.md`
- `deep-research/agents/source_verification_agent.md`
- `deep-research/agents/bibliography_agent.md`
- `deep-research/agents/timeline_extraction_agent.md`

Local addition:
- `references/source_verification_protocol.md`

Why:
- Local `source_deep_reading.md` says summaries are inputs, not authority, but did not define a strict external-source verification ladder.
- Local paper gates checked claim validity, but citation existence, DOI/title mismatch, index disagreement, temporal precision, and contaminated-source flags were not consolidated.

Adapted rules:
- Evidence grades separate study relevance from source reliability.
- Important citations must pass at least one authoritative lookup or be marked access-limited/unverified.
- Multi-index checks use DOI/title/author/year consistency, not mere search-result presence.
- Temporal claims require date precision and source date, not just a prose citation.
- LLM-era contamination signals are warnings, not automatic rejection.

### 2. Integrity gate policy

Source files reviewed:
- `academic-pipeline/SKILL.md`
- `academic-pipeline/references/integrity_review_protocol.md`
- `academic-pipeline/references/pipeline_state_machine.md`
- `academic-pipeline/references/two_stage_review_protocol.md`
- `academic-pipeline/references/ai_research_failure_modes.md`
- `academic-pipeline/references/claim_verification_protocol.md`
- `academic-pipeline/references/external_review_protocol.md`
- `academic-pipeline/references/passport_as_reset_boundary.md`
- `academic-pipeline/references/progress_dashboard_template.md`
- `academic-pipeline/references/score_trajectory_protocol.md`

Local addition:
- `01_policies/integrity_gate_policy.md`

Why:
- Local quality gates existed, but integrity checkpoints were distributed across number QA, claim QA, source context, referee audit, and writing handoff.
- This new policy defines when integrity checks are mandatory and what blocks forward movement.

Adapted rules:
- Run integrity gate before writing kickoff, before referee audit/submission, after major revision, and after any locked-spec change that invalidates claims.
- Gate dimensions: reference existence, source-context fit, data/provenance, spec consistency, claim support, output reproducibility, AI failure-mode scan.
- Verdicts are PASS / PASS_WITH_LIMITATIONS / REVISE / BLOCKED.
- A blocked gate cannot be bypassed by prose improvement.

### 3. Claim verification matrix

Source files reviewed:
- `academic-pipeline/references/claim_verification_protocol.md`
- `academic-pipeline/references/claim_audit_calibration_protocol.md`
- `shared/handoff_schemas.md`
- `shared/artifact_reproducibility_pattern.md`

Local addition:
- `04_templates/claim_verification_matrix_template.md`

Why:
- Local Gate 2 says claims must point to locked specs and evidence, but projects need a reusable row-level artifact.

Adapted rules:
- Every manuscript-level claim gets a row.
- Each row links to source context, spec version, exhibit/output, support grade, caveat, and downstream action.
- Verdict taxonomy distinguishes verified, minor distortion, major distortion, unsupported, access-limited, and contradicted.

## High-value additions identified but not yet fully integrated

### 4. Literature monitoring cadence

Source files reviewed:
- `deep-research/references/literature_monitoring_strategies.md`
- `deep-research/agents/monitoring_agent.md`

Local target:
- new `02_workflows/literature_monitoring.md` or extension of second_brain paper-scout workflows

Use:
- after a project has a locked source universe or is under revision monitoring
- monitor new papers, retractions, working-paper updates, code/data releases, and benchmark shifts

Status: defer. Needs alignment with existing RSS/paper-scout cron and wiki ingest pipeline.

### 5. Preregistration / pre-analysis-plan guide

Source files reviewed:
- `deep-research/references/preregistration_guide.md`
- `deep-research/templates/preregistration_template.md`

Local target:
- new `references/preregistration_preanalysis_plan.md`
- optional template under `04_templates/`

Use:
- empirical projects where design must be frozen before execution
- robustness against specification drift

Status: defer. Specification lock already covers the immediate need; preregistration is a separate external-facing artifact.

### 6. PRISMA/systematic-review support

Source files reviewed:
- `deep-research/references/systematic_review_protocol.md`
- `deep-research/references/systematic_review_toolkit.md`
- `deep-research/templates/prisma_protocol_template.md`
- `deep-research/templates/prisma_report_template.md`
- `shared/prisma_trAIce_protocol.md`

Local target:
- optional systematic-review module only if a project explicitly becomes a systematic review

Decision: skip for default econ/finance empirical pipeline. Keep as future optional module.

### 7. Reviewer consensus and adversarial review discipline

Source files reviewed:
- `academic-paper-reviewer/SKILL.md`
- `academic-paper-reviewer/agents/editorial_synthesizer_agent.md`
- `academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md`
- `academic-paper-reviewer/agents/eic_agent.md`

Local target:
- extension of `02_workflows/referee_audit.md`
- sibling writing_system may separately adapt paragraph-level adversarial review later

Use:
- classify reviewer findings as consensus, split, or adversarial-critical
- prevent reviewer softening when challenged without evidence
- keep review read-only unless a separate revision task is authorized

Status: partially integrated by patching `referee_audit.md` with two-stage review discipline and read-only review rule.

## Rejected direct imports

Rejected:
- Claude Code plugin structure and slash commands
- full ARS agent teams
- prompt files and templates as written
- autonomous full-paper writer/reviewer pipeline
- skip-permission/runtime assumptions
- PRISMA-trAIce as a default rule
- cross-model verification flags as a default requirement
- JSON contracts that assume ARS runtime

Reason:
- local runtime is Hermes/Mac-control-tower/server execution, not Claude Code plugin runtime
- writing_system is independent and paragraph-level
- research projects require spec-lock and project-state governance, not generic paper generation
- license is noncommercial and not open-source

## Local integration checklist

Completed in this adoption wave:
- add adoption decision document
- add `01_policies/integrity_gate_policy.md`
- add `references/source_verification_protocol.md`
- add `04_templates/claim_verification_matrix_template.md`
- patch start/readme/framework/quality-gate/bridge/referee docs to reference the new artifacts

Completed in the Codex/Agent Deck pilot wave:
- Created a disposable server2 pilot repo at `/home/nanyeon99/project/ars_codex_agentdeck_pilot`.
- Ran a Codex owner-style pilot against a mock research packet without installing upstream ARS-Codex or copying upstream prompt/template files.
- Produced local QA artifacts: `qa/source_verification.md`, `qa/claim_verification_matrix.md`, `qa/integrity_gate.md`, and `qa/gate_status.yaml`.
- Produced a deterministic validator, `scripts/verify_ars_pilot.py`; validation result: PASS.
- Confirmed the most useful ARS-Codex pieces are not the runtime or slash commands, but the split between source audit, claim audit, integrity gate, temporal-fit check, and machine-readable handoff status.
- Patched `04_templates/agent_deck_project_owner_contract_template.md` and `02_workflows/gate_status_protocol.md` so future Agent Deck Codex owners can use ARS-inspired local QA packets under the one-project-one-owner rule.

Pilot runtime note:
- The first Agent Deck/Codex launch on server2 failed in sandboxed mode because Codex could not write under its sandbox environment.
- A direct Codex run with full local access in the disposable repo completed the pilot and left a verifiable diff.
- Do not generalize that bypass to active research repos without a repo hygiene gate and explicit scope; use it only when the project is disposable or the controller has approved edit-mode.

Next pilot:
- choose one active project
- create `claim_verification_matrix.md`
- run source verification on 5 important citations and 3 manuscript claims
- run integrity gate before marking any exhibit/prose as stable
- add the optional flat owner-summary fields to that project's `qa/gate_status.yaml` so the conductor can safely distinguish `auto_continue_allowed`, `human_evidence_audit`, and `blocked` states
