# Research Pipeline v2

Updated: 2026-05-24

Status: v2 master reference. This document is additive to the existing Paper Project Framework. It supersedes older lifecycle, routing, and gate language only where it is explicit. Existing policies remain controlling when v2 is silent.

Purpose

This workflow defines the full v2 research pipeline from early triage to replication package release. It is designed for Codex master orchestration, sub-Codex lane dispatch, selective cross-model review, and human gates at the two points where human judgment changes the research direction. It does not replace the writing system handoff. Phase 5 continues to use the existing writing system bridge and writing system controls.

Primary references

- `01_policies/paper_project_framework.md` remains the baseline project lifecycle contract.
- `02_workflows/idea_evaluation.md` remains the idea scoring and pre-project gate.
- `02_workflows/specification_lock.md` remains the empirical and methodological spec lock.
- `02_workflows/referee_audit.md` remains the independent referee audit before final empirical submission or replication release.
- `02_workflows/paper_factory_quality_gates.md` remains the quality gate packet for paper-factory style execution.

v2 is a superset of these documents. It adds a phase router, runtime responsibilities, a fixed phase-prefixed folder layout, a two-point mandatory human gate structure, and type-specific skeleton and exhibit routing. It does not weaken any existing integrity, waiver, source verification, or writing readiness rule.

## 1. Operating principles

The pipeline is phase-based. Each phase has a narrow output, a gate, and an owner. A phase may produce many exploratory artifacts, but only gate-approved artifacts move forward as controlling project state.

The Codex master acts as phase router. It reads `project_state.md`, `decision_log.md`, `qa/gate_status.yaml`, `specs/main_spec.md`, and the phase folder before dispatching work. It then creates lane contracts for sub-Codex agents when work is separable. Sub-Codex agents work on bounded lanes and return artifacts, not global decisions.

The pipeline keeps wide, mid, and detailed plans separate. Wide and mid plans are thinking assets. Detailed plans are execution contracts. After narrowing, wide and mid plans move to `99_archive/wide_plans/<phase>/` so future projects can reuse the option space without confusing it with the active spec.

The pipeline has two mandatory human gates. The first occurs after the pilot phase. The second occurs after main analysis. These are not notification events. They are decision gates. Work cannot silently proceed through them.

The pipeline treats literature work as concentrated rather than constant. Literature scans run at the end of Phase 0 and Phase 1, with a final novelty scan at the end of Phase 3. Background discovery can happen, but only these scheduled points update the gate packet unless the human asks for an extra scan.

## 2. Research type classification

Phase 0 assigns one research type and records it in `project_state.md` under `research_type`. The type controls skeleton choice, exhibit map, baseline methods, and reviewer expectations.

Type A empirical asset pricing

This type studies returns, risk premia, portfolios, factors, cross-sectional pricing, anomalies, or asset-pricing tests. Typical objects are stocks, funds, tokens, real-estate securities, portfolios, or factor returns. The main exhibit spine usually starts with data and factor or portfolio construction, then main pricing results, robustness, and mechanism or limits.

Type B real estate empirics

This type studies housing, commercial property, rent, foot traffic, local markets, urban amenities, transactions, appraisal, zoning, or spatial exposure. Typical objects are parcels, buildings, districts, leases, transactions, listings, or local economic indicators. The main exhibit spine usually starts with a map or market structure figure, then sample construction, baseline specification, heterogeneity, robustness, and economic magnitude.

Type C forecasting

This type studies predictive performance, nowcasting, forecast comparison, target construction, panel forecasting, or model evaluation over time. Typical objects are forecast targets, horizons, rolling windows, model families, benchmarks, and loss functions. The main exhibit spine usually starts with target and horizon structure, then benchmark design, main performance, stability, uncertainty, and economic value.

Type D interpretable ML in finance

This type studies machine learning models where interpretability, uncertainty, feature behavior, or decision support is part of the contribution. Typical objects are models, features, explanations, uncertainty scores, counterfactuals, or human decision tasks. The main exhibit spine usually starts with model task and interpretability object, then prediction or classification performance, explanation validation, robustness, and economic or institutional interpretation.

Type E conceptual or institutional

This type studies market design, legal or institutional architecture, tokenization, disclosure, governance, payment rails, or theory-light conceptual mechanisms. Typical objects are institutions, contracts, frictions, governance choices, workflows, or market participants. The main exhibit spine usually starts with a conceptual map or institutional sequence, then taxonomy, mechanism, evidence cases, limits, and design implications.

Classification rule

Choose the type that controls the main contribution, not the data source. Use `04_templates/research_type_decision.md` when classification is ambiguous or when a project spans real estate, ML, asset pricing, forecasting, or tokenization. A paper using ML for a real-estate question is Type B unless interpretability or ML method behavior is the main contribution. A tokenized real-estate paper is Type E if the institutional mechanism is central, and Type A or B only if the core test is asset pricing or real-estate empirics.

## 3. Phase overview

### Phase 0. Triage and entry routing

Goal

Decide whether the input is an idea, an active project, a restart, a pivot, a writing handoff, or a replication task. Assign the research type. Decide whether the project can enter the v2 pipeline or must first complete missing legacy gates.

Primary owner

Codex master.

Inputs

- Human prompt or project brief.
- Existing `project_state.md` when present.
- Existing `decision_log.md` when present.
- Existing `qa/gate_status.yaml` when present.
- Existing `specs/main_spec.md` when present.
- `02_workflows/idea_evaluation.md` for early ideas.

Required outputs

- `project_state.md` with `research_type` recorded.
- Entry status in `qa/gate_status.yaml`.
- A Phase 0 triage note under `00_phase_router/`.
- Literature scan packet from internal graphify and external indexes.
- Paper request to Chan when direct threat coverage is missing.

Phase 0 literature work

At the end of Phase 0, the literature-scout queries the internal graphify corpus and OpenAlex. The internal corpus is the second_brain literature graph. The external scan uses OpenAlex and, when configured, Semantic Scholar. The result is not a full literature review. It is a threat and routing scan.

Gate 1. Entry gate

The project may proceed only if the input has enough information to choose a route and research type. If not, it remains in triage. If it is an idea, `02_workflows/idea_evaluation.md` controls the next step.

### Phase 1. Wide data collection planning

Goal

Build the feasible data, method, literature, and exhibit option space. Narrow from wide plan to mid plan to detailed plan. Preserve the discarded option space for reuse.

Primary owner

Codex master with sub-Codex data-scout, literature-scout, and idea-prototyper when needed.

Inputs

- Phase 0 triage note.
- `project_state.md` with research type.
- Internal and external literature scan output.
- Existing data availability notes.
- Human constraints.

Required outputs

- `01_data_planning/wide_plan.md`.
- `01_data_planning/mid_plan.md`.
- `01_data_planning/detailed_plan.md`.
- Updated `refs/literature_map.md` or equivalent project reference artifact.
- Updated `decision_log.md` for narrowing decisions.
- Archived wide and mid alternatives under `99_archive/wide_plans/phase1/` after narrowing.

Phase 1 literature work

At the end of Phase 1, literature-scout repeats the internal graphify and OpenAlex scans with the narrowed data and method design. This scan should identify direct threats, method comparators, data-setting comparators, and missing papers that Chan should supply or approve for download.

Gate 2. Plan narrowing gate

The detailed plan must identify the data spine, method candidates, pilot target, expected exhibit spine, and unresolved risks. If the plan is still only wide or mid-level, Phase 2 cannot start.

### Phase 2. Pilot design and execution

Goal

Run a small but honest pilot that tests data viability, signal plausibility, spec feasibility, and exhibit potential. The pilot is not allowed to become the main analysis by inertia.

Primary owner

Codex master with pilot-designer, pilot-executor, math-auditor, and referee-economist as needed.

Inputs

- Phase 1 detailed plan.
- `specs/main_spec.md` draft or pilot spec.
- Data access notes.
- Literature threat packet.

Required outputs

- `02_pilot/pilot_design.md`.
- `02_pilot/pilot_results.md`.
- `02_pilot/pilot_limitations.md`.
- Updated `qa/gate_status.yaml`.
- Updated `specs/main_spec.md` if the pilot supports a lock candidate.
- A cross-model minimax review at the end of the phase.

Minimax call

At the end of Phase 2, Codex master sends the pilot packet to minimax for adversarial review. The call asks whether the pilot result supports main analysis, whether the design has fatal identification or measurement flaws, and whether any claim is overstated. This is a cross-model audit, not a decision authority.

Gate 3. Pilot validity gate

The pilot must show that the proposed data and method can produce interpretable output. A weak result can pass if it is informative and leads to a credible narrowed design. A noisy or null pilot cannot be promoted unless it still proves feasibility and the revised claim is narrower.

Gate 4. Human gate 1 after pilot

This gate is mandatory. Chan chooses one of four decisions.

- Continue to main analysis.
- Continue with narrowed claim.
- Redesign pilot or data spine.
- Stop or park the project.

The decision must be recorded in `decision_log.md` and reflected in `qa/gate_status.yaml`. No Phase 3 work begins until this gate is resolved.

Human gate 1 template

```markdown
# Human Gate 1. Pilot Decision

Project:
Research type:
Pilot packet:
Minimax review:
Main risks:
Recommended decision:

Decision:
- [ ] Continue to main analysis
- [ ] Continue with narrowed claim
- [ ] Redesign pilot or data spine
- [ ] Stop or park

Required changes before Phase 3:
Waivers or accepted limitations:
Decision owner:
Date:
```

### Phase 3. Main analysis with multi-lane parallel execution

Goal

Run the locked main analysis and controlled robustness lanes. Produce the candidate exhibit set and the three Figure 1 hook candidates.

Primary owner

Codex master with main-econometrician, robustness-runner, math-auditor, novelty-checker, referee-economist, and blindspot-auditor.

Inputs

- Human gate 1 decision.
- Locked or lock-ready `specs/main_spec.md`.
- Phase 2 results.
- Literature map.
- Data and preprocessing specs.

Required outputs

- `03_main_analysis/main_results.md`.
- `03_main_analysis/exhibit_candidates.md`.
- `03_main_analysis/robustness_results.md`.
- `03_main_analysis/figure1_hook_candidates.md` with three candidates.
- Updated `qa/source_verification.md`.
- Updated `qa/claim_verification_matrix.md`.
- Updated `qa/integrity_gate.md`.
- Updated `qa/gate_status.yaml`.
- Minimax lane reviews at the end of each major lane.
- Final novelty-checker scan against recent working papers.

Multi-lane rule

Phase 3 may run multiple lanes in parallel only after the main spec is locked enough to prevent spec drift. Each lane receives a lane contract with input artifacts, output artifacts, allowed changes, forbidden changes, and stopping criteria. Lanes must not silently alter the main sample, main outcome, main estimator, preprocessing path, or claim mapping.

Minimax call

At the end of each major Phase 3 lane, Codex master sends the lane output to minimax for targeted critique. The critique checks validity, overclaiming, hidden multiple testing, and unexplained contradictions across lanes.

Novelty scan

At the end of Phase 3, novelty-checker runs an external scan for recent working papers and close threats. This scan is required even if Phase 0 and Phase 1 literature work was strong, because the paper is now concrete enough to search against direct claims.

Figure 1 hook requirement

Every research type must produce three Figure 1 hook candidates by the end of Phase 3. A candidate may be a figure, schematic, map, conceptual diagram, or carefully designed table-like visual if that is the correct hook for the type. Chan selects the final hook at Human gate 2.

Gate 5. Main analysis integrity gate

The main analysis must pass source verification, claim verification, integrity gate, and spec consistency checks. Failures do not automatically kill the project, but they block writing handoff until corrected or waived.

Gate 6. Human gate 2 after main analysis

This gate is mandatory. Chan chooses the paper spine, Figure 1 hook, claim strength, and writing readiness status.

Human gate 2 template

```markdown
# Human Gate 2. Main Analysis Decision

Project:
Research type:
Main result packet:
Integrity gate status:
Novelty scan status:
Figure 1 candidates:
Recommended paper spine:
Recommended claim strength:

Decision:
- [ ] Lock paper spine and proceed to idea-result diff
- [ ] Narrow the claim and proceed
- [ ] Run additional analysis before writing
- [ ] Pivot the project
- [ ] Stop or park

Selected Figure 1 hook:
Required changes before Phase 4:
Waivers or accepted limitations:
Decision owner:
Date:
```

No Phase 4 synthesis or writing preparation begins until this decision is recorded.

### Phase 4. Idea-result diff and skeleton

Goal

Compare the original idea against actual results. Decide what the paper is now. Build a skeleton that reflects evidence rather than hope.

Primary owner

Codex master with diff-analyzer, skeleton-writer, referee-economist, blindspot-auditor, and Claude Code only if graphify-related structure inspection is needed.

Inputs

- Human gate 2 decision.
- Phase 3 result packet.
- Original idea, pilot design, and main spec.
- Literature map and novelty scan.
- Type-specific skeleton template.

Required outputs

- `04_skeleton/idea_result_diff.md`.
- `04_skeleton/paper_spine.md`.
- `04_skeleton/exhibit_map.md`.
- `04_skeleton/section_skeleton.md`.
- `04_skeleton/writing_handoff_packet.md`.
- Minimax review after skeleton creation.

Minimax call

After skeleton-writer drafts the skeleton, Codex master sends the Phase 4 packet to minimax. The critique asks whether the skeleton follows from the evidence, whether the contribution is overstated, whether the closest literature is faced directly, and whether Figure 1 supports the real paper spine.

Gate 7. Skeleton readiness gate

The skeleton may proceed only if every major claim has a mapped exhibit or source, the selected Figure 1 hook is consistent with the introduction claim, and the writing handoff packet separates evidence-backed claims from speculation.

### Phase 5. Writing system handoff

Goal

Move from research evidence to prose under the existing writing system. v2 does not replace this phase. It prepares the handoff and then uses the writing system controls.

Bridge contract

Phase 5 uses `references/writing_system_bridge.md` as the entry contract for writing handoff. The bridge defines the same writing evidence packet required here: project state, source context, decision log, next actions, mapped exhibits, locked specs, claim verification, integrity and gate status artifacts, waivers, invalidation records, section and paragraph map, claim boundaries, and style constraints. If Phase 5 and the bridge appear to differ, treat them as one contract and update both before starting prose. The writing system begins only after this shared evidence packet exists.

Primary owner

Writing system workflow with Claude Code active only for writing system handoff when assigned. Codex master remains responsible for ensuring the handoff packet is complete before the writing system starts.

Inputs

- `04_skeleton/writing_handoff_packet.md`.
- `04_skeleton/section_skeleton.md`.
- `04_skeleton/exhibit_map.md`.
- `qa/claim_verification_matrix.md`.
- Writing system entry files.

Required outputs

- Writing kickoff packet.
- Section and paragraph maps.
- Drafting or revision artifacts controlled by the writing system.
- Updated `qa/gate_status.yaml` when writing readiness changes.

Gate 8. Writing handoff gate

The project may enter writing only if the handoff packet is complete, the claim matrix is mapped, and any waiver is explicit. If the writing system finds unsupported claims, the project returns to Phase 4 or Phase 3 rather than solving research uncertainty through prose.

### Phase 6. Replication package

Goal

Build a self-contained replication package that can reproduce the paper's core results and satisfy journal or archive expectations.

Primary owner

Codex master with replication-builder, robustness-runner, and math-auditor as needed.

Inputs

- Final or near-final analysis artifacts.
- Main scripts and output specs.
- Environment files.
- Data access and licensing notes.
- Referee audit output when available.

Required outputs

- `06_replication/` self-contained package.
- Dependency graph.
- Master script.
- Environment lock files.
- SHA256 hash ledger.
- AEA-style README when applicable.
- Self-test log.
- Upload-ready zip for Zenodo, OpenICPSR, or journal archive. Live upload requires separate human approval.

Gate 9. Replication release gate

The package cannot be marked release-ready until the self-test passes, hashes are recorded, data restrictions are documented, and the README explains how to reproduce the main tables and figures. If restricted data prevents full reproduction, the limitation must be explicit and claim scope must match the reproducible artifacts.

## 4. Runtime orchestration

Codex master

Codex master is the default controller. It reads current project state, decides the active phase, dispatches sub-Codex agents, integrates outputs, updates gate artifacts, and stops at human gates.

Sub-Codex agents

Sub-Codex agents execute bounded lanes. They never change phase, relax gates, alter the locked spec, or decide human questions. Their outputs must be written to phase folders or QA artifacts named in the lane contract.

Minimax cross-model calls

Minimax is used only at three points.

- End of Phase 2 after pilot execution.
- End of each major Phase 3 lane.
- After Phase 4 skeleton creation.

Minimax output is critique. Codex master decides how to route that critique through existing gates. Human gate decisions remain human decisions.

Claude Code

Claude Code is inactive by default. It becomes active for graphify-related tasks and writing system handoff tasks only. Graphify-related tasks include corpus structure inspection, graph-derived project mapping, and graphify report interpretation. Writing handoff tasks must follow the writing system load order.

Hermes

Hermes handles dashboard updates, changelog mirror, and Telegram bridge notifications. Hermes does not decide phase status, claim strength, or writing readiness. It may surface gate packets and notify Chan when gates need review.

## 5. Planning funnel

Every phase uses three plan layers when the scope is uncertain.

Wide plan

The wide plan records the option universe. It may include multiple data sources, identification strategies, model families, exhibit structures, and claim routes. It should be broad enough that later narrowing is not hidden.

Mid plan

The mid plan records viable candidate routes after obvious failures are removed. It should explain why options were kept or dropped.

Detailed plan

The detailed plan is the execution contract. It names artifacts, commands or scripts when relevant, lane responsibilities, acceptance criteria, and gate outputs.

Archive rule

After narrowing, wide and mid plans move to `99_archive/wide_plans/<phase>/`. They remain reusable option maps. They do not control the active project unless a later pivot explicitly restores them through `decision_log.md`.

## 6. Literature layer

The v2 literature layer has two scheduled concentration points and one final freshness check.

End of Phase 0

The goal is route selection and threat detection. The scan asks what community the idea belongs to, which papers are direct threats, and whether the project should continue as an idea, pilot, restart, or stop.

End of Phase 1

The goal is design validation. The scan uses the narrowed data and method plan to identify closer threats, method comparators, data-setting comparators, and missing papers.

End of Phase 3

The goal is novelty protection. Novelty-checker scans recent working papers and close external threats against the concrete main results and claims.

Chan paper request

When the scan finds missing papers, paywalled items, ambiguous closest threats, or papers that require human judgment, the system sends a paper request to Chan. The request states what is needed, why it matters, and whether the paper blocks a gate.

## 7. Notification policy

The notification schedule is defined in `02_workflows/notification_schedule.md` and `04_templates/work_hours.yaml`. Until those files exist, use the following v2 defaults.

Morning briefing runs once between 9 and 12. After that, only critical items interrupt before midday. Midday digest runs at 12. Afternoon digests run at 15 and 17. End-of-day runs at 18. Overnight handoff briefing runs at 20. After 20, notifications are critical only.

Human gate reached during work hours is critical and should be pushed immediately. Non-critical progress, routine lane completions, and low-risk QA updates wait for the next digest.

## 8. Folder layout

A v2 project uses phase-prefixed folders.

```text
00_phase_router/
01_data_planning/
02_pilot/
03_main_analysis/
04_skeleton/
05_writing_handoff/
06_replication/
specs/
qa/
refs/
logs/
99_archive/
```

Cross-cutting folders remain live. `specs/` and `qa/` are never archived merely because a phase changes. They are the active contract and audit layer.

`99_archive/` stores wide plans, pivots, dropped findings, alternative specs, and reusable components. It does not store active specs or active QA status.

## 9. Gate summary

Gate 1. Entry gate after Phase 0 triage.

Gate 2. Plan narrowing gate after Phase 1.

Gate 3. Pilot validity gate after Phase 2 pilot execution.

Gate 4. Human gate 1 after Phase 2. Mandatory.

Gate 5. Main analysis integrity gate after Phase 3.

Gate 6. Human gate 2 after Phase 3. Mandatory.

Gate 7. Skeleton readiness gate after Phase 4.

Gate 8. Writing handoff gate before Phase 5 writing execution.

Gate 9. Replication release gate after Phase 6 self-test.

## 10. Interaction with existing framework docs

`01_policies/paper_project_framework.md` remains the broad contract. v2 provides a more operational phase router and a stronger multi-agent execution model. If the older lifecycle sequence is less specific than this document, use v2.

`02_workflows/idea_evaluation.md` remains authoritative for early idea scoring. v2 Phase 0 routes into that workflow when the input is still an idea. v2 does not lower the proceed threshold or remove the literature-map requirement.

`02_workflows/specification_lock.md` remains authoritative for locking data, preprocessing, methodology, exhibit, and claim mapping. v2 Phase 2 and Phase 3 call that workflow rather than replacing it.

`02_workflows/referee_audit.md` remains authoritative for independent referee-style audit. v2 uses it before submission and replication release when the project is empirical or when claims are strong enough to need adversarial review.

`02_workflows/paper_factory_quality_gates.md` remains authoritative for source verification, claim verification, and integrity gate packet structure. v2 adds phase timing and runtime ownership.

## 11. Stop rules

Stop for Chan when either mandatory human gate is reached. Stop when a project tries to change research type after Phase 1. Stop when a lane needs to alter the locked main spec. Stop when literature scan finds an unaddressed direct threat that changes novelty. Stop when a replication package requires live upload or external credential use.

The system may continue through routine lane execution only when the active phase allows it, artifacts are written to the expected files, and no gate is unresolved.
