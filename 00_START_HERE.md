# Research Paper System — Start Here

Use this file first for research-system tasks.

Goal:
- make Hermes, Claude Code, and Codex follow the same research-paper lifecycle rules
- connect project structure, analysis documentation, evidence governance, audit gates, and submission readiness
- keep writing as a separate sibling system with an explicit evidence handoff

Canonical roots:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/
```

## Minimum load order for research tasks

v2 pipeline is documented in `02_workflows/research_pipeline_v2.md`; legacy lifecycle policy remains controlling unless v2 explicitly supersedes.

1. `01_policies/paper_project_framework.md`
2. `02_workflows/project_structure.md` when starting, moving, or resuming a research project
3. `02_workflows/idea_evaluation.md`, `04_templates/idea_evaluation_template.md`, and `04_templates/literature_map_template.md` when screening a new idea before project start
4. `02_workflows/autonomous_progression.md` when an agent should continue across gates or phases
5. `02_workflows/research_project_governance.md` and `02_workflows/second_brain_system_evolution.md` when analysis direction changes, second_brain memory should be synced, optional project wiki is needed, knowledge should move into the shared LLM wiki, or a system rule/prompt failed and should improve
6. `02_workflows/research_workflow_modules.md` when applying workflow modules from wiki knowledge
7. `02_workflows/source_deep_reading.md` when a long paper PDF needs careful extraction for source context
8. `references/source_verification_protocol.md` before a source/citation supports a manuscript claim or a data/method assertion
9. `02_workflows/specification_lock.md` before choosing a main empirical spine, data source/unit, preprocessing path, methodology, portfolio sort, algorithm, or fixed exhibit
10. `02_workflows/paper_factory_quality_gates.md` before promoting a candidate empirical spine into prose: use viability gate, focused findings packages, spec locks, audit issue ledger, sample support, dropped findings, Gate 1 number QA, and Gate 2 claim-validity QA
11. `01_policies/integrity_gate_policy.md` before writing kickoff, referee audit, submission readiness, post-revision stabilization, or locked-spec changes
12. `02_workflows/gate_status_protocol.md` before marking a project writing-ready, referee-audit-ready, submission-ready, autonomous-owner-ready, or `HUMAN_AUDIT_REQUIRED`
13. `02_workflows/blindspot_audit.md` before a table, figure, or result is interpreted or marked `FIX`
14. `02_workflows/presentation_deck_workflow.md` when creating or revising research decks
15. `02_workflows/referee_audit.md` when auditing a near-final empirical pipeline, replication package, or submission
16. `02_workflows/research_session_launcher_protocol.md`, `02_workflows/agent_deck_research_tracking.md`, and `04_templates/agent_deck_project_owner_contract_template.md` before launching Agent Deck, Claude Code, Codex, tmux, or any autonomous owner against an exploratory research repo
17. agent-specific note in `03_agents/`

## Writing boundary

Writing-specific tasks do not start here. They start at:

```text
/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/START_HERE.md
```

Use `references/writing_system_bridge.md` for the boundary and handoff contract.

Research system must provide the evidence packet before writing begins:
- project state
- source context
- literature map when contribution, novelty, mechanism, method, or field-positioning claims are used
- source verification table when citations/sources support central claims
- decision log
- next actions
- exhibit decision ledger or mapped equivalent
- audit_issue_ledger.md when any empirical, data, measurement, mechanical, identification, replication, citation, or claim-calibration issues have been raised
- sample_support.md when writing uses sample path, treatment support, match rates, or subgroup support
- dropped_findings.md when candidate results were rejected or narrowed
- data_context.md when data producer/reporting rules affect interpretation
- canonical active spec lock files: `specs/main_spec.md`, `specs/data_spec.md`, `specs/preprocessing_spec.md`, `specs/methodology_spec.md`, `specs/output_spec.md`, and `specs/spec_change_log.md`; combined/legacy specs require artifact mapping
- `qa/claim_verification_matrix.md` when central claims are entering prose
- `qa/integrity_gate.md` before writing kickoff, referee audit, submission readiness, or post-revision stabilization
- `qa/gate_status.yaml` before writing handoff, referee audit, submission readiness, or autonomous owner launch
- `qa/waiver_log.md` when any gate/rule is overridden or skipped
- `qa/invalidation_ledger.md` when locked specs, central outputs, or central claims changed
- `qa/artifact_mapping.md` when any canonical artifact uses a legacy/equivalent path
- fixed tables/figures and paths, including human-visible publishable table/figure verdicts
- `paper/section_paragraph_map.md` summarizing each section and each planned paragraph in one sentence before paragraph drafting
- claim boundaries and known gaps
- target journal/style constraints, if known

If writing needs unsupported empirical claims, citations, numbers, methods, or exhibit status, stop writing and return to the research system.

## Operating rules

- Active project repo work happens directly on the selected execution server, server1/server2/server3, under `/home/nanyeon99/project/<repo_name>` by default.
- Mac is the control tower; servers are execution nodes.
- Before launching Agent Deck, Claude Code, Codex, tmux, or another autonomous owner, verify the project registry gate and write/use a project owner contract.
- Default academic workflow is one project = one active owner agent. Do not run Codex and Claude Code simultaneously inside the same research repo unless Yeonchan explicitly approves an exceptional handoff/split.
- Rough idea projects follow idea evaluation -> pilot -> research contract -> experiment/audit -> writing gate.
- Package-first research repos follow their package/reproducibility process while preserving research-system gates where relevant.
- Screen early research ideas through the idea evaluation workflow before creating a full project repo unless the human override is recorded in `decision_log.md` and `qa/waiver_log.md`.
- For already-running projects, run an onboarding audit and apply the smallest sufficient framework patch before changing analysis or writing.
- After major analysis batches, run pivot review and second_brain/project-wiki sync before treating the current direction as stable.
- Before treating a table, figure, or result interpretation as stable, run blindspot audit or record why it does not apply.
- Submission-ready empirical projects should run independent referee audit before the pipeline or replication package is treated as final. Any human skip requires `qa/waiver_log.md` and narrows what may be claimed; it is not a clean PASS.
- Prefer evidence already loaded in the session.
- If a claim needs a citation, number, or method detail that is not loaded, mark the gap instead of inventing support.
- Legacy/equivalent artifact paths count only when mapped in `qa/artifact_mapping.md` or `project_state.md`; unmapped equivalents block writing, referee audit, and submission gates.
- Human audit requests must be explanatory packets, not opaque approval strings. Use `04_templates/human_audit_request_template.md`; include plain-language question, why the gate stopped, evidence inspected, options, recommendation, consequences, exact approval phrase, and after-decision execution plan.
- Progress and decisions that change future behavior must feed back into second_brain through `02_workflows/second_brain_system_evolution.md`; routine progress remains in repo logs/dashboard unless it changes a rule, gate, decision, or reusable lesson.
- Keep documents in English.
- Keep chat replies in Korean or English to match the user message.

## Path policy

- This folder is the single source of truth for research lifecycle and analysis governance.
- The sibling `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/` folder is the single source of truth for writing-specific policies, workflows, templates, voice profile, and prose lint.
- The old nested `research_paper_system/writing_system/` path is a compatibility redirect only.
- Legacy writing redirects under `01_policies/`, `02_workflows/`, and `04_templates/` should point to the sibling writing system.
