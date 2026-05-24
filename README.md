# Research Paper System

Purpose: project lifecycle, analysis discipline, evidence governance, and submission readiness for Yeonchan's research-paper projects.

Canonical root:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/
```

Sibling system:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/
```

The writing system is independent. This research system hands off to it through `references/writing_system_bridge.md` after evidence is ready.

## Scope

v2 pipeline is documented in `02_workflows/research_pipeline_v2.md`; legacy lifecycle policy remains controlling unless v2 explicitly supersedes.

This system owns:
- early research idea screening and go/no-go gates
- research project structure and project state files
- server-first project work under `/home/nanyeon99/project/<repo_name>`
- research direction tracking, decision logs, pivots, and second_brain sync
- data provenance, raw-vs-derived documentation, analysis panel discipline, leakage/spec-drift audit
- source deep reading and source-context extraction
- table/figure/exhibit readiness decisions before prose use
- blindspot audits before result interpretation or exhibit `FIX`
- research deck generation and visual QA
- independent referee audit, replication checks, and submission readiness
- agent-specific entrypoints for Hermes, Claude Code, and Codex

This system does not own prose mechanics. Paragraph drafting, voice, prose lint, manuscript wording, style packs, and response-letter wording belong to the sibling writing system.

## Folder map

- `00_START_HERE.md` — main entrypoint for research-system tasks
- `01_policies/paper_project_framework.md` — full lifecycle policy
- `01_policies/integrity_gate_policy.md` — fail-closed source/spec/claim/provenance gate before writing, review, submission, or post-revision stabilization
- `02_workflows/idea_evaluation.md` — idea evaluation and promotion gate
- `02_workflows/autonomous_progression.md` — automatic continuation and human-stop gates
- `02_workflows/project_structure.md` — standard repo/project structure
- `02_workflows/lifecycle_repo_organization.md` — phase-by-phase repo folder organization from rough idea through submission
- `02_workflows/research_project_governance.md` — pivots, phase changes, second_brain sync, wiki promotion
- `02_workflows/repo_changelog_second_brain_sync.md` — automatic repo `CHANGELOG.md` mirror into second_brain `04_Ventures/`; git tree + repo changelog remain authoritative
- `02_workflows/research_workflow_modules.md` — workflow modules from reviewed wiki evidence
- `02_workflows/source_deep_reading.md` — long-source extraction into source context
- `02_workflows/specification_lock.md` — locks main empirical spine, data source/unit, preprocessing, methodology, outputs, and spec changes
- `02_workflows/paper_factory_quality_gates.md` — viability, findings selection, audit ledger, number QA, and claim-validity gates adapted from paper_factory
- `references/source_verification_protocol.md` — source existence, claim-context, temporal, data-source, OpenAlex/index, and contamination checks adapted from academic-research-skills
- `02_workflows/gate_status_protocol.md` — machine-readable `qa/gate_status.yaml` protocol and verifier for writing/review/submission readiness
- `02_workflows/blindspot_audit.md` — result/exhibit peripheral-vision audit
- `02_workflows/presentation_deck_workflow.md` — research deck creation and QA
- `02_workflows/referee_audit.md` — independent implementation, replication, and econometrics audit
- `02_workflows/agent_deck_research_tracking.md` — single-owner Agent Deck tracking workflow
- `02_workflows/multi_agent_repo_orchestration.md` — exceptional/legacy multi-lane orchestration only
- `references/paper_factory_adoption_2026-05-21.md` — adoption decision record for upstream paper_factory patterns
- `references/academic_research_skills_adoption_2026-05-21.md` — adoption decision record for upstream academic-research-skills patterns
- `03_agents/` — agent-specific loading notes
- `04_templates/` — project, contract, gate, ledger, literature-map, literature-gap-search, section/paragraph-map, audit-ownership, and audit templates
- `scripts/verify_paper_numbers.py` — first-pass manuscript number verifier for Gate 1
- `scripts/verify_research_gate_status.py` — first-pass verifier for canonical artifacts, locked specs, and machine-readable gate status
- `05_runs/` — dated system evolution records
- `references/writing_system_bridge.md` — boundary and handoff contract with sibling writing system
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/README.md` — sibling writing-system entrypoint for writing-specific rules

## Operating rules

- Start research-system tasks from `00_START_HERE.md`.
- Keep project work server-first unless the human explicitly asks for local-only work.
- Active project repos live under `/home/nanyeon99/project/<repo_name>` on the selected execution server: server1, server2, or server3.
- Organize project repos by lifecycle phase using `02_workflows/lifecycle_repo_organization.md`; create phase folders and index files before producing phase artifacts.
- Manage active repo state through git tree/commits plus root `CHANGELOG.md`; second_brain receives only an automatic `CHANGELOG.md` mirror via `02_workflows/repo_changelog_second_brain_sync.md`.
- Research projects should maintain canonical artifacts: `project_state.md`, `decision_log.md`, `next_actions.md`, `source_context.md`, explicit spec lock files under `specs/`, QA files under `qa/`, and `qa/gate_status.yaml`. Legacy equivalents are allowed only when mapped in `qa/artifact_mapping.md` or `project_state.md`.
- Before launching autonomous owners, verify the project registry gate and use a project owner contract.
- Default academic workflow is one project = one active owner agent.
- Before interpreting a table, figure, or result as stable, run blindspot audit or document why it does not apply.
- Before treating a central claim as stable, verify source/output/spec support in canonical `qa/claim_verification_matrix.md`; legacy equivalent paths must be mapped before they count.
- Before writing kickoff, referee audit, submission readiness, post-revision stabilization, or locked-spec changes, run the integrity gate in `01_policies/integrity_gate_policy.md` and update `qa/gate_status.yaml`.
- Do not send writing tasks to the writing system until the research evidence packet exists.
- Do not let the writing system invent empirical support, citations, numbers, or method details.
- Submission-ready empirical projects should run `02_workflows/referee_audit.md`; any human skip requires `qa/waiver_log.md`, visible accepted-risk notes, and narrowed claims.

## Writing handoff

When analysis is ready for prose, create or verify a writing evidence packet:

```text
project_state.md
source_context.md
qa/source_verification.md when citations/sources support central claims
ideas/literature_map.md or qa/literature_map.md when novelty/literature/mechanism/method claims matter
decision_log.md
next_actions.md
exhibit_decision_ledger.md or mapped equivalent
qa/audit_issue_ledger.md when issues have been raised
sample_support.md when sample path, treatment support, match rates, or subgroup support matter
dropped_findings.md when candidate results were rejected or narrowed
data_context.md when data producer/reporting rules affect interpretation
specs/main_spec.md
specs/data_spec.md
specs/preprocessing_spec.md
specs/methodology_spec.md
specs/output_spec.md
specs/spec_change_log.md
qa/claim_verification_matrix.md when central claims enter prose
qa/integrity_gate.md before writing kickoff or review-readiness
qa/gate_status.yaml
qa/waiver_log.md when any rule/gate is overridden or skipped
qa/invalidation_ledger.md when locked specs or central outputs/claims changed
fixed tables/figures and paths, with human-visible publishable verdicts
paper/section_paragraph_map.md with one sentence for every section and planned paragraph
claim boundaries and known gaps
target journal/style constraints, if known
```

The authoritative writing evidence packet is defined in `references/writing_system_bridge.md`. If this README conflicts with the bridge, the bridge wins.

Then route writing-specific work to:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md
```

## Current status

- `research_paper_system/` is the source of truth for research lifecycle and analysis governance.
- `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/` is now a sibling source of truth for writing-specific policy, voice, prose lint, templates, and style packs.
- Old nested writing files under `research_paper_system/01_policies`, `02_workflows`, and `04_templates` remain compatibility redirects only.
- ARIS is a separate execution engine at `~/Library/CloudStorage/SynologyDrive-second_brain/aris/`; research and writing system rules remain controlling when ARIS behavior conflicts.
