# Research Workflow Modules

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Each workflow module here may map to an ARIS skill. When a module is operationally identical to an ARIS skill, name the skill explicitly inside the module description so future agents know which engine to invoke. When a module has no ARIS analogue, document it as our own and treat ARIS as silent on that module.

ARIS skills available for module use (non-exhaustive):
- `/research-lit "topic"`, `/alphaxiv "arxiv-id"`, `/semantic-scholar`, `/openalex`, `/exa-search`, `/gemini-search` — literature lookup.
- `/idea-creator "direction"`, `/idea-discovery` — idea generation.
- `/novelty-check "idea"`, `/research-review`, `/kill-argument` — adversarial critique.
- `/experiment-plan`, `/experiment-bridge`, `/run-experiment`, `/monitor-experiment`, `/experiment-queue`, `/analyze-results` — experiment lifecycle (ML-leaning).
- `/paper-plan`, `/paper-write`, `/paper-figure`, `/paper-illustration`, `/paper-compile`, `/paper-poster`, `/paper-slides` — paper production.
- `/result-to-claim`, `/experiment-audit`, `/paper-claim-audit`, `/citation-audit` — claim and integrity gates.
- `/research-wiki <subcommand>` — knowledge base.
- `/meta-optimize` — skill self-improvement (subordinate to our `voice_update.md`).

Binding rules:
- Adoption of an ARIS skill into a module follows the same evidence ladder as wiki intake: raw → reviewed → candidate → experiment → accepted → deployed → monitored.
- Do not promote a skill to "accepted" inside a module without at least one project-internal trial run with the human in the loop.

Purpose:
- define reusable workflow modules extracted from the 157 AI-econ-wiki source reviews
- map wiki knowledge into concrete research and writing system behavior
- keep module adoption auditable and reversible

Primary synthesis:
- `wiki/projects/ai-econ-wiki-research-workflow-upgrade-2026-04-26.md`

Concept pages:
- `wiki/concepts/project-memory.md`
- `wiki/concepts/data-workflow.md`
- `wiki/concepts/agentic-pipeline.md`
- `wiki/concepts/writing-voice.md`
- `wiki/concepts/paper-review.md`
- `wiki/concepts/replication.md`
- `wiki/concepts/skill-library.md`
- `wiki/concepts/visual-output.md`
- `wiki/concepts/research-ideation.md`
- `wiki/concepts/privacy-security.md`
- `wiki/concepts/meeting-admin.md`
- `wiki/concepts/general-ai-research-workflow.md`

## Module Map

### Project Memory

Use when starting, resuming, pivoting, or handing off projects.

Required behavior:
- maintain canonical `project_state.md`, `decision_log.md`, `next_actions.md`, and `source_context.md`; legacy equivalents require `qa/artifact_mapping.md` or a mapping table in `project_state.md`
- update memory after significant analysis, writing, or review sessions
- treat memory as a resume aid, not as unverified truth

Failure modes:
- stale memory
- undocumented reversals
- false continuity

### Data Workflow

Use when collecting, cleaning, joining, or transforming data.

Required behavior:
- preserve raw outputs before transformation
- record schema, source, retrieval time, hash when feasible, and transformation script
- separate raw, interim, processed, and analysis-ready data
- link data artifacts to claims, tables, and figures

Failure modes:
- untracked joins
- schema drift
- missing credentials
- irreproducible cleaning

### Agentic Pipeline

Use when agents execute bounded project work.

Required behavior:
- plan: define task, allowed files, success criteria, and rollback path
- execute: run in server repo, sandbox, branch, or bounded workspace
- audit: inspect code diff, outputs, logs, and claims
- promote: move only validated outputs into project memory, exhibits, or prose

Failure modes:
- silent failure
- hardcoding
- benchmark leakage
- permission creep

### Writing Voice

Use when drafting or revising manuscript prose.

Required behavior:
- load voice profile, project writing handoff, and source context
- draft paragraph by paragraph
- audit hedging, causal language, citations, and tone
- propose voice updates only after human-approved writing

Failure modes:
- overconfident prose
- style homogenization
- citation-context loss

### Paper Review

Use when turning papers or research-related sources into wiki knowledge.

Required schema:
- question
- contribution
- data
- method
- findings
- limitations
- evidence quality
- wiki links
- graph hints

Failure modes:
- summary drift
- invented metadata
- over-linking weak sources

### Source Deep Reading

Use when an academic PDF needs careful extraction for project source context.

Required behavior:
- use `02_workflows/source_deep_reading.md` for long PDFs that support project claims
- preserve original PDFs
- create reusable markdown extraction next to the source PDF
- record source path, extraction path, evidence grade, supported claims, unsupported claims, and replication notes in `source_context.md`

Failure modes:
- one-shot shallow summaries
- context blowups from reading too many PDF pages in the main session
- generated extracts treated as manuscript evidence
- original PDFs moved, overwritten, or deleted

### Referee Audit

Use when empirical outputs, drafts, or replication packages are close to final.

Required behavior:
- use `02_workflows/referee_audit.md`
- keep audit scripts separate from author code
- run code, output automation, directory, replication, and econometrics checks at the needed intensity
- file referee reports under `correspondence/referee2/`
- require an author response before later audit rounds

Failure modes:
- same-session self-review
- silent code edits by the auditor
- shallow review without running code
- unresolved discrepancies treated as harmless

### Blindspot Audit

Use when a table, figure, or result is about to be interpreted.

Required behavior:
- use `02_workflows/blindspot_audit.md`
- list visible features before interpreting the main result
- identify missing checks, unexplained absences, overlooked mechanisms, and undersold strengths
- block `FIX` when the ruling is `HOLD`
- record claim boundaries for `CONDITIONAL`

Failure modes:
- main-result tunnel vision
- unexplained anomalies written around
- missed robustness checks
- interesting but unsupported claims added to prose

### Skill Library

Use when repeated workflows should become reusable agent behavior.

Promotion rule:
- repeated task/correction pattern appears at least three times
- trigger conditions are clear
- output contract is stable
- guardrails can be concise
- one project-level test succeeds

Failure modes:
- premature abstraction
- stale procedures
- too-broad permissions

### Visual Output

Use for tables, figures, slides, dashboards, and rendered artifacts.

Required behavior:
- compile or render the artifact
- inspect visual output, not only source code
- check labels, overlap, readability, and source consistency
- rerender after fixes
- use `02_workflows/presentation_deck_workflow.md` for research decks
- keep deck claims tied to project evidence, scripts, and exhibits
- check LaTeX warnings, TikZ collisions, clipped labels, and title-as-claim sequence when relevant

Failure modes:
- unseen rendering failures
- chart distortion
- label overlap
- slide polish that outruns evidence

### Research Ideation

Use before committing serious time to a new paper direction.

Required behavior:
- use `02_workflows/idea_evaluation.md` when an idea is being screened before full project start
- state question and mechanism
- check novelty against source map
- probe data availability and identification
- list failure modes
- define minimal empirical, theoretical, or simulation test
- verify direct-threat papers before treating the idea as project-ready

Failure modes:
- novelty hallucination
- weak identification
- data overpromising

### Privacy And Security

Use whenever data, code, tools, or external communication may carry risk.

Required behavior:
- default to read-only for sensitive sources
- redact private data before external model calls
- sandbox risky code
- require human approval before external communication, deletion, submission, or permission expansion

Failure modes:
- secret leakage
- destructive actions
- unbounded agent access

### Meeting Admin

Use when meeting notes, emails, chats, or voice transcripts affect projects.

Required behavior:
- extract decisions, tasks, deadlines, owners, and project links
- push durable decisions into `decision_log.md`
- push next work into `next_actions.md`
- keep raw transcript/email separate from interpretation

Failure modes:
- action loss
- decision drift
- mixing raw communication with accepted project state

## Adoption Rule

Modules are defaults for project work, but new hard requirements must pass `02_workflows/wiki_intake_continuous_upgrade.md`.

For already-running projects:
- do not restructure only to satisfy these modules
- add missing equivalents when they improve handoff, audit, writing readiness, or reproducibility
- record the chosen onboarding level in `research_log.md` or `handoff/`
