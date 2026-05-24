# Gate Status Protocol

Purpose: provide a machine-readable project status layer so agents can verify whether a project is allowed to move into writing, exhibit `FIX`, referee audit, submission readiness, or autonomous owner launch.

## Required file

Active research-paper projects should maintain:

```text
qa/gate_status.yaml
```

Use this protocol together with:
- `02_workflows/specification_lock.md`
- `01_policies/integrity_gate_policy.md`
- `references/writing_system_bridge.md`
- `04_templates/artifact_mapping_template.md`
- `04_templates/waiver_log_template.md`

ARS-Codex integration note:
- Agent Deck Codex owners may use `Imbad0202/academic-research-skills-codex` only as clean-room routing vocabulary for source verification, claim verification, integrity gating, handoff bundles, and temporal-fit checks.
- Do not import upstream prompts, templates, slash commands, agent files, or runtime semantics into project repos.
- Local `qa/gate_status.yaml` is authoritative even when an owner uses ARS-inspired labels in a report.

## Minimal schema

```yaml
project: project_slug
updated: YYYY-MM-DD
reviewer: agent_or_human

artifacts:
  project_state: present
  decision_log: present
  next_actions: present
  source_context: present
  human_audit_request: not_needed
  artifact_mapping: not_needed
  waiver_log: not_needed

specs:
  main_spec: LOCKED
  data_spec: LOCKED
  preprocessing_spec: LOCKED
  methodology_spec: LOCKED
  output_spec: LOCKED
  spec_change_log: present

qa:
  source_verification: PASS
  claim_verification_matrix: PASS
  literature_map: PASS
  threat_literature_matrix: PASS_WITH_LIMITATIONS
  audit_ownership_matrix: PASS
  section_paragraph_map: PASS
  invalidation_ledger: not_needed
  integrity_gate: PASS
  gate1_number_qa: PASS
  gate2_claim_validity: PASS
  blindspot_audit: PASS_WITH_LIMITATIONS
  referee_audit: NOT_RUN

writing_handoff:
  evidence_packet_complete: true
  publishable_exhibits_human_checked: true
  section_paragraph_map_complete: true
  allowed: true
  limitations:
    - "Do not claim causal effects beyond the locked design."

blocked:
  status: false
  reasons: []

human_audit:
  required: false
  packet: not_needed
  plain_language_question: ""
  options_ready: false
  recommendation_ready: false
  exact_approval_phrase_ready: false

# Optional flat owner-summary fields for Agent Deck/conductor routing.
# These duplicate selected nested values so lightweight controllers can decide
# whether a single bounded continuation is safe without parsing prose.
writing_ready: true
referee_audit_ready: false
autonomous_owner_ready: true
human_audit_required: false
auto_continue_allowed: true
next_action_type: single_bounded
next_allowed_action: "Update AGENT_STATUS.md from verified artifacts only."
active_plan: "docs/research_system/plans/2026-05-23-status-sync.md"
current_plan_step: "step-1"
plan_checkpoint_status: clear
plan_change_required: false
blocked_on: none
required_human_decision: none
required_artifact: none
ready_for_conductor_auto_nudge: true
```

## Allowed status vocabulary

Spec states:
- `EXPLORATORY`
- `PROVISIONAL_LOCK`
- `LOCKED`
- `SUPERSEDED`
- `missing`

Gate states:
- `PASS`
- `PASS_WITH_LIMITATIONS`
- `REVISE`
- `BLOCKED`
- `NOT_RUN`
- `not_needed`
- `missing`

Artifact states:
- `present`
- `mapped`
- `missing`
- `not_needed`

Flat owner-summary booleans:
- `writing_ready`: true only when `writing_handoff.allowed=true` and no writing blockers remain.
- `referee_audit_ready`: true only when writing handoff is allowed and the review packet is complete.
- `autonomous_owner_ready`: true only when the owner has enough repo-local context to continue without changing research direction.
- `human_audit_required`: true only when the next step needs Yeonchan's scholarly/design/provenance decision.
- `auto_continue_allowed`: true only when the next action is non-destructive, repo-local, single-bounded, and does not cross a human-heavy gate.
- `next_allowed_action`: exactly one concrete action when `auto_continue_allowed=true`; exact gate description otherwise.
- `active_plan`: repo-local plan path, `plan_creation_needed`, or `none`.
- `current_plan_step`: current step id, `create_plan`, or `none`.
- `plan_checkpoint_status`: `clear`, `human_check_required`, `artifact_missing`, `verification_failed`, or `none`.
- `plan_change_required`: true only when the current plan must change beyond local tactical replanning.
- `blocked_on`: `none`, `decision`, `artifact`, `policy`, `verification_failure`, `human_gate`, or `external_dependency`.
- `required_human_decision`: `none` or the exact plain-language question Yeonchan must answer.
- `required_artifact`: `none` or the exact missing path/export/source.
- `ready_for_conductor_auto_nudge`: true only when all auto-continuation consistency checks pass.

Flat owner-summary action labels:
- `single_bounded`
- `status_only`
- `human_design_gate`
- `artifact_supply_gate`
- `packet_reply_gate`
- `human_evidence_audit`
- `human_design_decision`
- `prepare_review_packet`
- `blocked`

Conductor consistency rule:
- Missing flat owner-summary fields are interpreted conservatively.
- `auto_continue_allowed: true` is valid only with `next_action_type: single_bounded`, exactly one `next_allowed_action`, `blocked_on: none`, `required_human_decision: none`, `required_artifact: none`, and `ready_for_conductor_auto_nudge: true`.
- Non-human-gated continuation should proceed from `active_plan`. If no plan exists, only a `create_plan` action for already-approved scope is auto-continuable.
- `plan_checkpoint_status` other than `clear`, or `plan_change_required: true`, blocks auto-continuation until a human/artifact/verification gate is resolved.
- Multiple proposed next actions or unresolved choices/artifacts force `auto_continue_allowed: false` even if `human_audit_required: false`.

If a flat field conflicts with the nested status, the safer value wins. Example: `auto_continue_allowed: true` plus `blocked.status: true` means blocked.

## Human audit request standard

When `HUMAN_AUDIT_REQUIRED` or `human_audit.required=true` appears, the project must provide a human-facing packet at:

```text
qa/human_audit_request.md
```

Use `04_templates/human_audit_request_template.md`.

Do not ask Yeonchan to approve an internal label such as `Approve rebuild_reference_no_direct_restore` by itself. Internal option slugs are allowed only after a plain-language explanation.

The packet must include:
- the plain-language decision question
- why the gate stopped now
- evidence inspected, with paths and reliability labels
- human-readable options
- consequences of each option: time/cost, scientific risk, provenance risk, and what will be rebuilt/restored/skipped
- agent recommendation, including why other options are unsafe or inferior
- exact approval phrase in natural language
- after-decision execution plan and actions that still require separate approval
- default safe behavior if no decision is made

Dashboard/indexer behavior:
- show `HUMAN_AUDIT_REQUIRED` only when `qa/human_audit_request.md` exists or a repo status file contains the same packet sections
- otherwise report the project as `human_audit_packet_missing`, not as a decision-ready human audit
- never surface only an opaque option slug as the final decision request

## Blocking rules

Writing handoff is blocked when:
- any required artifact is `missing`
- any core spec needed by a central claim is not `LOCKED`
- `ideas/literature_map.md` or `qa/literature_map.md` is missing when novelty, contribution, mechanism, method, or literature-positioning claims enter prose
- `qa/claim_verification_matrix.md` is missing when central claims enter prose
- `qa/integrity_gate.md` is `REVISE`, `BLOCKED`, `NOT_RUN`, or `missing`
- `paper/section_paragraph_map.md` is missing when paragraph drafting is the next step
- publishable tables/figures have not received a human-visible publishable check when they anchor final prose
- active waivers affect central claims but `qa/waiver_log.md` is missing
- invalidated outputs/claims remain `OPEN` in `qa/invalidation_ledger.md`

Referee audit or submission readiness is blocked when:
- writing handoff is not allowed
- Gate 1 or Gate 2 is `REOPEN_ANALYSIS`, `REOPEN_TEXT`, `REVISE`, `BLOCKED`, `NOT_RUN`, or `missing`
- unresolved `BLOCKING` audit issues remain
- `ADVERSARIAL_CRITICAL` findings are unresolved or not accepted as explicit limitations

## Verification helpers

Run the general gate-status verifier:

```bash
python3 /Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/scripts/verify_research_gate_status.py <project_root>
```

Run the research-to-writing packet verifier before prose drafting:

```bash
python3 /Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/research_paper_system/scripts/verify_writing_handoff_packet.py <project_root>
```

The handoff verifier reports `READY`, `READY_WITH_WAIVERS`, or `BLOCKED`. `READY_WITH_WAIVERS` means the packet is complete enough to enter writing, but active waivers, mapped equivalents, or limitation-bearing gates narrow what can be claimed.

The helpers are deterministic first-pass checks. They do not replace human or referee judgment. Use `04_templates/audit_ownership_matrix_template.md` to make the split explicit: machine checks presence, schema, identifiers, numeric consistency, and stale states; Yeonchan or a human scholarly reviewer checks novelty, identification, mechanism, exhibit publishability, target fit, and waiver acceptability.
