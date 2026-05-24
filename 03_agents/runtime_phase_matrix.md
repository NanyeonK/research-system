# Runtime Phase Matrix

Updated: 2026-05-24

Status: v2 runtime reference. Use after `../00_START_HERE.md` and `../02_workflows/research_pipeline_v2.md`.

Purpose

This document defines which runtime is active in each v2 phase and what each runtime may decide. It also defines the sub-Codex agent catalog used by Codex master. It does not replace the existing top-level entries for Codex, Claude Code, or Hermes. Those entries remain short compatibility files. This matrix supplies the phase-specific operating layer.

## 1. Runtime control rule

Codex master is the phase router for v2. It owns phase detection, lane dispatch, artifact integration, and gate packet assembly. It does not own mandatory human decisions.

Sub-Codex agents execute bounded lanes. They receive input artifacts and return output artifacts. They do not change phase, alter locked specs, relax gates, or decide writing readiness.

Claude Code is inactive by default. It activates only for graphify-related tasks and writing system handoff tasks.

Hermes handles dashboard, changelog mirror, Telegram bridge, scheduled reminders, and surface-level status delivery. It does not decide research claims, phase promotion, or gate pass status.

Minimax is not a standing runtime. It is a cross-model critique call used only at the v2 points defined in `../02_workflows/research_pipeline_v2.md`.

## 2. Phase activation matrix

| Phase | Codex master | Sub-Codex | Claude Code | Hermes | Minimax |
|---|---|---|---|---|---|
| Phase 0 triage and entry routing | Active as phase router. Reads current state, classifies entry type, assigns research type, opens gate packet. | Optional. `literature-scout` and `idea-prototyper` may support route diagnosis. | Inactive unless graphify corpus inspection is needed. | Active for dashboard and paper-request notification only. | Inactive. |
| Phase 1 wide data collection planning | Active. Builds wide-mid-detailed narrowing path and records decisions. | Active when lanes are separable. Typical agents are `data-scout`, `literature-scout`, `idea-prototyper`, and `pilot-designer`. | Inactive unless project-level graphify structure must be inspected. | Active for digest summaries and changelog mirror. | Inactive. |
| Phase 2 pilot design and execution | Active. Locks pilot scope, dispatches pilot lanes, integrates results, prepares Human Gate 1. | Active. Typical agents are `pilot-designer`, `pilot-executor`, `math-auditor`, and `referee-economist`. | Inactive unless graph-derived evidence is part of the pilot design. | Active for Human Gate 1 immediate push and routine digest. | Active once at end of phase after pilot packet is complete. |
| Phase 3 main analysis with multi-lane parallel | Active. Enforces locked spec, dispatches lane contracts, integrates results, prepares Human Gate 2. | Active. Typical agents are `main-econometrician`, `robustness-runner`, `math-auditor`, `novelty-checker`, `referee-economist`, and `blindspot-auditor`. | Inactive unless graphify is needed for corpus or project structure. | Active for lane completion digests, critical blocks, and Human Gate 2 immediate push. | Active at end of each major lane. |
| Phase 4 idea-result diff and skeleton | Active. Compares original idea to results, dispatches skeleton and critique lanes, assembles writing handoff packet. | Active. Typical agents are `diff-analyzer`, `skeleton-writer`, `referee-economist`, and `blindspot-auditor`. | Active only for graphify-related structure inspection. Not active for ordinary skeleton drafting unless assigned through writing system handoff. | Active for dashboard, changelog mirror, and skeleton readiness notification. | Active once after skeleton packet is complete. |
| Phase 5 writing system handoff | Active only as handoff verifier. It checks that research artifacts are complete before writing begins. | Optional and limited. Sub-Codex may repair research artifacts that block handoff. | Active for writing system handoff when assigned. Must follow sibling writing system load order. | Active for writing dashboard, changelog mirror, and human notification. | Inactive unless Chan explicitly asks for extra adversarial critique. |
| Phase 6 replication package | Active. Routes package build, self-test, environment lock, hash ledger, and release gate. | Active. Typical agents are `replication-builder`, `robustness-runner`, and `math-auditor`. | Inactive unless graphify is needed to inspect code or dependency structure. | Active for replication status and release gate notification. | Inactive by default. |

## 3. Runtime permissions

Codex master may

- determine current phase from canonical artifacts
- create lane contracts
- dispatch sub-Codex agents
- integrate lane outputs
- update phase folders, `decision_log.md`, `project_state.md`, and `qa/gate_status.yaml`
- mark machine-checkable gates as passing or blocked when evidence is explicit
- stop at mandatory human gates

Codex master may not

- proceed past Human Gate 1 or Human Gate 2 without Chan's recorded decision
- treat minimax output as a decision
- move active `specs/` or `qa/` files into archive
- silently change research type after Phase 1
- route unsupported claims to prose

Sub-Codex agents may

- inspect assigned input artifacts
- create assigned output artifacts
- run bounded analysis, QA, literature, or packaging work
- report blockers and contradictions

Sub-Codex agents may not

- change phase
- edit locked specs unless the lane contract explicitly allows proposing a diff
- decide gate status
- rewrite global project narrative outside assigned artifacts
- call external services with credentials unless the lane contract permits it

Claude Code may

- inspect graphify outputs, graph reports, and graph-derived project structure
- support writing system handoff when the writing system load order is explicit
- review code or artifact structure when assigned by Codex master

Claude Code may not

- become the default research phase router
- draft ordinary research prose outside the writing system controls
- bypass `qa/gate_status.yaml` or waiver rules

Hermes may

- maintain dashboard state
- mirror changelog entries
- deliver Telegram bridge notifications
- surface human gate packets
- run scheduled status checks

Hermes may not

- mark a research gate as passed from notification state alone
- decide claim strength
- decide writing readiness
- perform live external uploads without approval

## 4. Sub-Codex agent catalog

Each sub-Codex agent is a role, not a separate policy authority. Codex master supplies a lane contract with exact input artifacts, output artifacts, allowed edits, forbidden edits, and stop conditions.

### data-scout

Calling phase

Phase 1, with optional Phase 0 support when data feasibility controls routing.

Master caller

Codex master.

Input artifacts

- Phase 0 triage note.
- Candidate research type in `project_state.md`.
- Existing data notes, if any.
- Human constraints and known access limits.

Output artifacts

- `01_data_planning/data_option_map.md`.
- Data feasibility notes for `01_data_planning/wide_plan.md` or `mid_plan.md`.
- Data risks for `qa/gate_status.yaml`.

Primary job

Map feasible data sources, units, time coverage, access status, and blocking risks. It does not download large data unless the lane contract explicitly says so.

### idea-prototyper

Calling phase

Phase 0 and Phase 1.

Master caller

Codex master.

Input artifacts

- Human idea brief.
- Phase 0 triage note.
- `02_workflows/idea_evaluation.md` output when available.
- Literature threat notes.

Output artifacts

- Candidate route memo under `00_phase_router/` or `01_data_planning/`.
- Refined research question candidates.
- Explicit split or stop suggestions for `decision_log.md`.

Primary job

Sharpen rough ideas into testable routes while preserving the distinction between idea scoring and project execution.

### pilot-designer

Calling phase

Phase 1 and Phase 2.

Master caller

Codex master.

Input artifacts

- `01_data_planning/detailed_plan.md`.
- Candidate `specs/main_spec.md` or pilot spec.
- Data option map.
- Research type.

Output artifacts

- `02_pilot/pilot_design.md`.
- Pilot acceptance criteria.
- Pilot risk list for `qa/gate_status.yaml`.

Primary job

Design a small pilot that tests feasibility and signal without becoming the main analysis by inertia.

### pilot-executor

Calling phase

Phase 2.

Master caller

Codex master.

Input artifacts

- `02_pilot/pilot_design.md`.
- Pilot data paths or documented placeholders.
- Pilot acceptance criteria.

Output artifacts

- `02_pilot/pilot_results.md`.
- Reproducibility notes.
- Script or command log under `logs/` when code is executed.

Primary job

Run or simulate the pilot according to the design. It reports failures directly instead of changing design mid-run.

### math-auditor

Calling phase

Phase 2, Phase 3, and Phase 6.

Master caller

Codex master.

Input artifacts

- Pilot or main analysis formulas.
- Estimator definitions.
- Model equations.
- Output tables and transformation notes.

Output artifacts

- Math audit memo under the active phase folder.
- Blocking issues for `qa/integrity_gate.md`.
- Proposed correction notes for `decision_log.md` when needed.

Primary job

Check mathematical consistency, estimator interpretation, transformations, standard errors, and reported quantities.

### novelty-checker

Calling phase

Phase 3, with optional Phase 0 or Phase 1 support through `literature-scout` if needed.

Master caller

Codex master.

Input artifacts

- Main result packet.
- Claim candidates.
- Literature map.
- Research type.

Output artifacts

- `03_main_analysis/novelty_scan.md`.
- Direct threat list with URLs.
- Claim narrowing recommendations for Human Gate 2.

Primary job

Scan recent working papers and close external threats against the concrete main claims after results exist.

### main-econometrician

Calling phase

Phase 3.

Master caller

Codex master.

Input artifacts

- Locked or lock-ready `specs/main_spec.md`.
- Data and preprocessing specs.
- Phase 2 decision.
- Lane contract.

Output artifacts

- Main analysis outputs under `03_main_analysis/`.
- Result memo for `03_main_analysis/main_results.md`.
- Spec drift warnings for `qa/gate_status.yaml`.

Primary job

Execute the main empirical or model analysis exactly under the lane contract. It does not change sample, estimator, target, or preprocessing without stopping.

### robustness-runner

Calling phase

Phase 3 and Phase 6.

Master caller

Codex master.

Input artifacts

- Locked main spec.
- Allowed robustness list.
- Main result packet.
- Output spec.

Output artifacts

- `03_main_analysis/robustness_results.md` or replication robustness logs.
- Robustness exhibit candidates.
- Contradiction list for `qa/claim_verification_matrix.md`.

Primary job

Run pre-approved robustness checks and report whether they support, narrow, or contradict the main claim.

### referee-economist

Calling phase

Phase 2, Phase 3, and Phase 4. Optional before Phase 6 release.

Master caller

Codex master.

Input artifacts

- Active phase packet.
- Literature map.
- Main claims.
- Gate status.

Output artifacts

- Referee-style critique memo under the active phase folder.
- Threats and overclaiming flags for QA artifacts.

Primary job

Act as a skeptical economics or finance referee. It does not fix the work. It states what would block publication or require claim narrowing.

### blindspot-auditor

Calling phase

Phase 3 and Phase 4.

Master caller

Codex master.

Input artifacts

- Main result packet.
- Exhibit candidates.
- Claim verification matrix.
- Skeleton draft when available.

Output artifacts

- Blindspot audit memo.
- Missing alternative explanation list.
- Suggested additional checks or waivers.

Primary job

Find omitted mechanisms, sample restrictions, confounds, unsupported interpretation, and exhibit-story mismatches.

### diff-analyzer

Calling phase

Phase 4.

Master caller

Codex master.

Input artifacts

- Original idea or Phase 0 brief.
- Pilot packet.
- Main result packet.
- Human Gate 2 decision.

Output artifacts

- `04_skeleton/idea_result_diff.md`.
- Claim retention, claim narrowing, and claim drop list.

Primary job

Separate the paper that was imagined from the paper that the evidence supports.

### skeleton-writer

Calling phase

Phase 4.

Master caller

Codex master.

Input artifacts

- `04_skeleton/idea_result_diff.md`.
- Type-specific skeleton template.
- Exhibit candidates.
- Claim verification matrix.
- Human Gate 2 decision.

Output artifacts

- `04_skeleton/paper_spine.md`.
- `04_skeleton/exhibit_map.md`.
- `04_skeleton/section_skeleton.md`.
- `04_skeleton/writing_handoff_packet.md`.

Primary job

Create an evidence-locked skeleton and handoff packet. It does not write polished prose unless routed through Phase 5 writing controls.

### replication-builder

Calling phase

Phase 6.

Master caller

Codex master.

Input artifacts

- Phase 3 and Phase 4 result artifacts.
- Final output spec.
- Main scripts.
- Environment files.
- Data access notes.

Output artifacts

- `06_replication/dependency_graph.md`.
- `06_replication/run_all` script or documented equivalent.
- Environment lock files.
- SHA256 hash ledger.
- AEA-style README.
- Self-test log.
- Upload-ready zip when human approves packaging scope.

Primary job

Build a self-contained replication package and run the local self-test. It does not perform live Zenodo, OpenICPSR, or journal uploads without human approval.

### literature-scout

Calling phase

Phase 0 and Phase 1, then Phase 3 through novelty-checker if the scan is claim-specific.

Master caller

Codex master.

Input artifacts

- Research question.
- Research type.
- Data and method notes.
- Existing literature map.
- Graphify and external search configuration.

Output artifacts

- Literature scan memo.
- Direct threat list with URLs.
- Paper request to Chan when needed.
- Updates for `refs/literature_map.md`.

Primary job

Run concentrated internal and external literature scans. It does not treat unverified citations as evidence.

## 5. Lane contract minimum fields

Every sub-Codex call should include these fields.

```markdown
# Agent Lane Contract

Agent:
Phase:
Research type:
Master caller: Codex master
Input artifacts:
Output artifacts:
Allowed edits:
Forbidden edits:
External calls allowed:
Stop conditions:
Verification command or review check:
Return format:
```

Forbidden edits should be explicit. For empirical work they normally include locked sample changes, preprocessing changes, estimator changes, outcome changes, claim-strength changes, and gate-status changes.

## 6. Review and stopping rules

Stop when a lane finds a direct contradiction with the locked spec. Stop when a lane needs a file outside its allowed edits. Stop when a human gate is reached. Stop when external credentials, live uploads, or paid downloads are required. Stop when the runtime matrix conflicts with a project-local instruction and ask Codex master to resolve it through `decision_log.md`.

Routine lane completion can continue to the next integration step only if the required output artifacts exist and the lane did not request a phase, spec, or claim change.
