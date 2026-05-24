# Wiki Intake And Continuous Upgrade Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Engine skills:
- `/research-wiki ingest` — adds a paper, idea, experiment, or claim to the per-project wiki at `wiki/`.
- `/research-wiki query` — retrieves prior knowledge during research and writing.
- `/research-wiki sync` — keeps the per-project wiki current.
- `/research-wiki lint` — checks for broken edges, orphan nodes, and stale claims.
- `/research-wiki stats` — reports knowledge-base size and density.

Binding rules:
- Per-project ARIS `wiki/` is allowed and useful. The global ground truth remains `~/second_brain/wiki/` and is updated only through this workflow's promotion ladder: raw → reviewed → candidate → experiment → accepted → deployed → monitored.
- An ARIS skill, prompt, or template may be promoted into our system only when it has run with the human in the loop on at least one project and produced an artifact we accept.
- Promotion of an ARIS-derived rule into `01_policies/` or `02_workflows/` requires the same evidence grade rules as wiki sources: weak workflow anecdotes do not become hard rules.

Purpose:
- turn weekly wiki updates into controlled improvements to the research and writing system
- prevent weak workflow anecdotes from becoming hard rules without local audit
- keep second_brain, Paper Project Framework, Codex skills, and project templates evolving together

## Source Batch

Current baseline:
- source collection: `wiki/sources/ai-econ-wiki/`
- reviewed source count: 157
- synthesis page: `wiki/projects/ai-econ-wiki-research-workflow-upgrade-2026-04-26.md`
- review status: `wiki/_meta/ai_econ_wiki_review/direct_review_status.md`

Accepted post-baseline workflow sources:
- `alejandroll10/idea-evaluation-pipeline` (GitHub, reviewed 2026-04-30): evidence grade `B`, module `research-ideation`, deployed as `02_workflows/idea_evaluation.md` and `04_templates/idea_evaluation_template.md`.
- `scunning1975/MixtapeTools skills/referee2` (GitHub, reviewed 2026-04-30): evidence grade `B`, module `referee-audit`, deployed as `02_workflows/referee_audit.md` and `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/templates/referee_response_template.md`.
- `scunning1975/MixtapeTools` full repository pass (GitHub, reviewed 2026-04-30): evidence grade `B`, modules `blindspot-audit`, `source-deep-reading`, `visual-output`, `project-memory`, deployed as `02_workflows/blindspot_audit.md`, `02_workflows/source_deep_reading.md`, `02_workflows/presentation_deck_workflow.md`, and small project-structure updates.

Interpretation:
- this corpus is mainly workflow/practitioner evidence, not literature evidence
- use it to improve operations, not to support manuscript claims unless the source is independently citable
- blog, SNS, and video sources are weak evidence until locally tested or backed by reproducible artifacts

## Workflow Modules

Route every reviewed source or weekly update into one or more modules:
- `project-memory`
- `data-workflow`
- `agentic-pipeline`
- `writing-voice`
- `paper-review`
- `referee-audit`
- `blindspot-audit`
- `source-deep-reading`
- `skill-library`
- `visual-output`
- `research-ideation`
- `privacy-security`
- `meeting-admin`
- `general-ai-research-workflow`

Module definitions live in `02_workflows/research_workflow_modules.md` and `wiki/concepts/<module>.md`.

## Evidence Grades

Assign a workflow evidence grade before any system change:

- `A`: peer-reviewed paper, reproducible code, or local experiment confirms the pattern
- `B`: practitioner/code/tool source with concrete artifacts, commands, or templates
- `C`: blog, newsletter, video, or thread with useful pattern but no local validation
- `D`: vague claim, hype, inaccessible evidence, or non-reproducible demo

Only `A` and approved `B` evidence can directly change framework rules. `C` evidence must become a local experiment first. `D` evidence stays in notes unless it identifies a risk.

## Promotion Ladder

Weekly updates move through this ladder:

1. `RAW`: raw page, browser capture, PDF, code snapshot, or source diff is stored.
2. `REVIEWED`: source review exists under `wiki/sources/`.
3. `CANDIDATE`: the review proposes a workflow module, benefit, risk, and affected docs.
4. `EXPERIMENT`: one bounded local test is defined for a real or sandbox project.
5. `ACCEPTED`: local test passes or the user explicitly accepts the rule.
6. `DEPLOYED`: update lands in framework docs, templates, skills, scripts, or project onboarding.
7. `MONITORED`: later weekly checks confirm whether the rule still helps.

No weekly update should skip from `RAW` or `REVIEWED` directly to `DEPLOYED` unless the change is purely clerical.

## Weekly Intake Output

Each weekly pass should create or update:

```text
wiki/projects/ai-econ-wiki-weekly-upgrade-YYYY-MM-DD.md
```

Required sections:
- New or changed sources
- Source type and evidence grade summary
- Candidate modules
- Proposed project experiments
- Proposed framework changes
- Proposed skill or template changes
- Accepted changes
- Rejected or deferred changes
- Risks and privacy notes
- Follow-up actions for next week

## Upgrade Decision Rules

Promote to framework rule when:
- at least one real project would benefit now
- risk is low or mitigated
- the rule can be expressed as a check, template, or gate
- the rule does not conflict with server-first project work or human approval gates

Promote to skill when:
- the same workflow or correction recurs at least three times
- the task has clear trigger conditions
- the output contract is stable
- the guardrails fit inside a concise skill

Promote to template when:
- agents repeatedly need the same structured state
- the template improves handoff, audit, or writing readiness
- it can be filled by humans and agents without hidden tooling

Do not promote when:
- source evidence is weak and no local test exists
- the change mainly follows AI trend language
- it would increase permission scope without a clear need
- it would make Mac/server roles ambiguous
- it would bypass human approval for submissions, emails, deletions, or external communication

## Integration Points

Research system:
- project-state files
- source context and citation maps
- data provenance ledgers
- idea stress tests
- agentic plan-execute-audit-promote loops
- visual-output QA

Writing system:
- source-context loading before drafting
- paragraph-level writing with claim-strength limits
- citation-context audit
- voice-profile update proposals
- prose lint and exhibit evidence gates

Skills:
- `$research-paper-project` handles project governance and weekly system-upgrade routing
- `$paper-writing-voice` handles prose, source-context writing, and voice updates
- new skills are created only after stable repeated use

## Weekly Checklist

1. Read the latest import/update report.
2. Confirm raw files and source reviews exist.
3. Count source types and workflow modules.
4. Grade evidence quality.
5. Identify candidate changes for research, writing, skills, templates, and graphify.
6. Choose experiments before hard rules for weak sources.
7. Apply accepted framework changes.
8. Validate affected Codex skills.
9. Update wiki rule pages and Hermes log.
10. Record deferred candidates for the next weekly pass.

## Graphify Notes

Use graph nodes:
- `Source`
- `WorkflowPattern`
- `Risk`
- `Module`
- `Project`
- `RawArtifact`
- `EvidenceQuality`

Use graph edges:
- `supports_module`
- `warns_against`
- `implements`
- `requires_audit`
- `derived_from_raw`
- `candidate_for_project`

Graph centrality does not equal evidence strength. Keep module centrality and evidence quality separate.
