# Research Idea Evaluation Workflow

Updated: 2026-05-08

Purpose:
- screen early econ/finance research ideas before creating a full project repo
- co-develop promising ideas with the human until they are specific enough to judge
- force new-contribution, identification, data, mechanism, and literature-map checks early
- require a second_brain/Graphify-backed literature map before scoring whenever feasible
- prevent weak ideas from entering the full Paper Project Framework too soon
- preserve the reasoning trail when an idea pivots into a paper project

Source:
- Adapted from Alejandro Lopez-Lira's `idea-evaluation-pipeline`: https://github.com/alejandroll10/idea-evaluation-pipeline
- Source evidence grade: `B` for workflow use. It is a public prompt-based pipeline with concrete templates and steps, but it is not manuscript literature evidence.
- Local deployment status: accepted by human instruction on 2026-04-30.
- Strict prompt-rubric expansion: updated on 2026-04-30 after direct review of the repository prompt files.

## ARIS Bridge

Read `01_policies/aris_bridge.md` before invoking ARIS skills inside this workflow.

Engine skills (run under our gate, not in place of it):
- `/idea-discovery "direction"` — orchestrates ARIS `research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline`. Use for the literature-survey, brainstorm, and adversarial-critique substeps. Outputs must be reformatted into our `04_templates/idea_evaluation_template.md` schema, not consumed in ARIS's `IDEA_REPORT.md` form.
- `/novelty-check "idea"` — replaces parts of Step 5 (Threat Literature Search) and Step 6 (Verify Threat Literature). Use only when web access is available and threat papers must be machine-verified at scale.
- `/research-review "idea or brief"` — runs cross-model adversarial critique (Codex MCP / GPT-5.4 xhigh) on the sharpened brief before our Step 1 score.

Binding rules:
- Our 8-step gate (Evaluate → Review → Pivot → Evaluate Pivot → Literature Map + Threat Lit → Verify Literature + Threat Lit → Final Verdict → Review Final Verdict) is authoritative.
- ARIS may execute substeps, but every score, every threshold, and every status label (`PROCEED`, `PROCEED WITH CONDITIONS`, `PIVOT`, `TARGET DOWN`, `STOP`, `SPLIT`) must come from this workflow.
- ARIS `AUTO_PROCEED=true` is rejected at the idea gate; final verdict requires human confirmation unless `02_workflows/autonomous_progression.md` explicitly authorizes auto-proceed for that project phase.
- ARIS `MAX_PILOT_IDEAS` and pilot-experiment shortcuts do not apply to econ/finance projects; pilots are decided by `02_workflows/project_structure.md` after `PROCEED`.
- ARIS reviewer-independence rule applies: when `/research-review` runs, the executor and reviewer must be in different model families.
- Threat-paper URL requirement is stricter than ARIS defaults: no URL, no citation, even if ARIS surfaces the paper.

## Trigger

Use this workflow when:
- the human asks whether a new research idea is worth pursuing
- an idea exists but should not enter a full project repo yet
- multiple candidate ideas need triage
- an existing project direction may need a pre-analysis rethink
- a paper direction is stuck after repeated weak evaluations or pivots

Do not use this workflow as manuscript evidence. It is a decision aid for project selection.

## Core Rule

An idea should not become a full research-paper project until it passes an idea gate or the human explicitly overrides the gate.

Before Project Start, use this workflow as an idea co-development loop with the human. The goal is not to rubber-stamp the first version. The goal is to sharpen the question, mechanism, identification or method, data, and threat-paper positioning until the idea reaches the normal `7-8` promotion band or the human records a lower-score override.

The idea gate requires:
- a complete idea template
- a literature map covering direct threats, adjacent communities, methods/data-setting clusters, and graph/community evidence from second_brain when available
- three closest threat papers with URLs
- an initial score and critique
- a review of the critique
- a pivot loop if score is below threshold
- a verified threat-literature search before the final proceed decision
- a final verdict with go/no-go preconditions
- preconditions split into automatic checks and human decisions

Default proceed threshold:
- `7/10` for serious project start
- `6-6.5/10` may proceed only with a realistic target-journal adjustment or explicit human override recorded in `decision_log.md` and `qa/waiver_log.md`
- below `6/10` should pivot, split, or stop

Scoring source rule:
- The score is based on the adapted Alejandro Lopez-Lira `idea-evaluation-pipeline` pressure and rubric: new contribution, identification/method, theoretical or empirical advancement, impact, feasibility/data, relevance/timeliness, and target-journal fit.
- The upstream pipeline is a scoring discipline, not an authority. Local research-system gates, second_brain literature map, source verification, waiver rules, and human final decisions override any upstream-style score.
- Do not score above `6.5` when the literature map is missing or direct threat coverage is unresolved, unless Yeonchan explicitly asks for a preliminary score.

## Strict Rubric From Source Prompts

Keep the original repository's judging pressure. Do not turn this gate into loose brainstorming.

Evaluation must directly judge:
- new contribution and marginal contribution relative to the three closest papers
- whether the idea is more than a robustness check, new setting, or parameter variation
- methodological innovation or credible use of existing methods
- exogenous variation for empirical papers
- new friction, mechanism, or market structure for theory papers
- recognized estimator, test, or procedure problem for methodology papers
- theoretical or empirical advancement
- potential impact on economics, finance, policy, practice, or future research
- feasibility of data, variables, sample period, and method
- relevance to current academic or real-world debates

The source prompts impose these caps and decision hooks:
- Step 1 evaluation: maximum 250 words, with score.
- Step 2 review: maximum 200 words, with `AGREE`, `PARTIALLY AGREE`, or `DISAGREE`.
- Step 3 pivot: maximum 400 words, with a concrete redesigned idea.
- Step 5 threat literature: organized threat memo with URLs for every cited paper.
- Step 7 final verdict: maximum 400 words, with final score, threats, title, abstract, target journals, key risk, and go/no-go preconditions.
- Step 8 final-verdict review: maximum 300 words, with `AGREE`, `PARTIALLY AGREE`, or `DISAGREE`.

Every score must explain why it is not one point higher. The final verdict must also explain why it is not one point lower. Do not round up to be kind.

## Required Input

Use `04_templates/idea_evaluation_template.md`.

Minimum fields:
- idea title
- paper type: empirical, theoretical, methodological, or mixed
- research question
- hypothesis or mechanism
- expected sign or core prediction
- identification strategy or model innovation
- data sources, variables, and sample period
- proposed empirical test, model, simulation, or proof
- three closest papers with citations, URLs, and explicit difference from the idea
- why the field should care

The three closest papers should be the papers a skeptical referee would cite against the idea, not broad background papers.

If an input is missing, mark it as `[GAP: ...]`. Do not fill missing papers, URLs, data access, or identification from memory.

## Interactive Co-Development Mode

Use this mode when the human gives a rough idea, a theme, a dataset, a mechanism, or a half-formed question.

Do not score the idea immediately unless the template is already `READY FOR EVALUATION`. First turn the rough idea into a judgeable submission.

### Intake Questions

Ask only the missing questions needed for the next gate. Prefer one compact batch of questions, not a long interview.

Minimum intake questions:
1. What exact outcome, behavior, price, risk, or decision does the paper explain?
2. What is the proposed mechanism, and what sign or pattern should it produce?
3. Why does this matter now for economics, finance, policy, or practice?
4. What data could measure the outcome, treatment or shock, mechanism, and sample?
5. What source of variation, model innovation, or institutional setting could identify the claim?
6. What are the closest papers the human already knows?
7. What should this paper not claim?
8. What constraints matter: data access, collaborator, deadline, journal, method to avoid, or claim to avoid?

If the human cannot answer a question, write `[GAP: ...]` and continue sharpening with the available information.

### Sharpening Pass

Before Step 1, produce a short idea brief:
- one-sentence research question
- one-sentence mechanism
- expected sign or prediction
- one-sentence new contribution
- candidate data and sample
- candidate identification or method
- literature map status: second_brain/Graphify communities checked, direct threats, adjacent literatures, and missing external-index searches
- closest known papers and missing threat-paper searches
- what the paper should not claim
- blocking gaps

Status labels:
- `DRAFT`: too vague to evaluate
- `INTAKE_COMPLETE`: enough information for preliminary threat-paper search
- `READY_FOR_EVALUATION`: enough information for Step 1 score
- `BLOCKED`: a critical data, method, or question gap prevents evaluation

### Literature Map Before Scoring

Before Step 1 scoring, create or update a literature map using `04_templates/literature_map_template.md`. The map is broader than closest threat papers. It must identify:
- direct threat papers
- adjacent literature communities
- mechanism, data/setting, and method/identification clusters
- gaps or graph bridges that make the idea plausible
- unresolved freshness or external-index searches

Source hierarchy:
1. Project-specific source files and notes.
2. Existing second_brain Graphify outputs, especially `GRAPH_REPORT.md` and `graph.json` under `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/wiki/_graphify/outputs/` when relevant.
3. Relevant second_brain `wiki/sources/`, `wiki/concepts/`, and `wiki/research-ideas/` folders.
4. External indexes such as OpenAlex, Semantic Scholar, Crossref, RePEc, NBER, SSRN, arXiv, CEPR, publisher pages, and Google Scholar for gaps, freshness, and verification. Use external search after second_brain/Graphify unless the topic is completely absent from the vault.

Graphify rule:
- Do not graphify the whole vault by default. Query an existing relevant graph first. If none exists, build a bounded corpus from the idea's mechanism/data/method/source folders.
- When the bounded corpus includes second_brain raw PDFs, textbooks, or chapter splits under Synology Drive, do not whole-corpus pin and do not read File Provider placeholders directly. Hydrate only the needed files into `/Users/nanyeon/second_brain_exec/raw_cache` with `/Users/nanyeon/bin/second_brain_hydrate.py`, then graphify the hydrated local working set or a small manifest-backed copy.
- Treat `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain` as sync/archive; treat `/Users/nanyeon/second_brain_exec` and its `raw_cache` as the execution layer for Graphify, source-deep-reading, and other PDF-heavy research-system operations.
- If hydration reports `materialization_blocked`, record the missing source as a scope gap or `needs Yeonchan/source materialization` instead of silently substituting a weak analog.
- Graphify edges marked `INFERRED` or `AMBIGUOUS` are discovery leads, not verified evidence. Promote them only after source verification.

Output before repo exists:

```text
~/Library/CloudStorage/SynologyDrive-second_brain/wiki/research-ideas/<idea_slug>.md
~/Library/CloudStorage/SynologyDrive-second_brain/wiki/research-ideas/<idea_slug>_literature_map.md  # optional for large maps
```

Use `04_templates/literature_gap_search_plan_template.md` when the second_brain search reveals missing clusters that need targeted external search.

Output inside a repo:

```text
ideas/literature_map.md
data/external/openalex/ or data/external/semantic_scholar/  # only when structured external results are saved
```

When structured external results are saved, record their paths in `MANIFEST.md`, `source_context.md`, and the literature map.

### Threat-Paper Completion

If the human names fewer than three closest papers:
- search for direct threat papers before Step 1 when web access is available
- use only verified papers with URLs
- mark unresolved searches as `[GAP: direct threat paper search]`
- do not score above `6.5` while direct-threat coverage is missing unless the human explicitly requests a preliminary score

### Co-Development Loop

If the preliminary idea would score below `7`, propose one or two concrete sharpening moves before running the full pivot step:
- sharper mechanism
- cleaner source of variation
- better data source
- narrower sample
- stronger comparison to a direct-threat paper
- different target journal or audience

After each sharpening move, update the idea brief and ask the human to accept, reject, or modify it. Move to Step 1 only when the brief is coherent enough to judge.

### Output Location

Before a repo exists, write the intake and brief to:

```text
~/Library/CloudStorage/SynologyDrive-second_brain/wiki/research-ideas/<idea_slug>.md
```

Inside a project repo, append it to:

```text
ideas/idea_evaluation.md
```

## Pipeline

### 1. Evaluate Idea

Goal:
- score the idea's paper potential and identify fatal weaknesses early

Evaluate:
- new contribution and marginal contribution
- identification or methodological strength
- theoretical or empirical advancement
- potential impact
- feasibility and data
- relevance and timeliness
- target-journal fit
- whether the idea is only an advanced-technique replication, country or sample swap, or parameter-robustness exercise

Output:
- `ideas/evaluation/eval_idea1.md` or mapped equivalent
- score from `1` to `10`
- concise critique
- explicit reason why the score is not one point higher
- missing information as `GAP`
- maximum 250 words unless the human asks for an expanded audit

Scoring guide:
- `1-3`: low potential; lacks a meaningful new contribution or feasible design
- `4-6`: moderate potential; needs a pivot or much sharper design
- `7-8`: good potential; can proceed after concrete preconditions
- `9-10`: excellent potential; rare and still needs threat verification

### 2. Review Evaluation

Goal:
- audit whether the first critique is too harsh, too lenient, factually wrong, or missing an important angle

Check:
- whether the evaluation characterizes cited papers correctly
- whether the identification critique is fair
- whether standard instruments, shocks, or research designs were missed
- whether the evaluation over- or under-rates the new contribution
- whether feasibility is realistic
- whether the target-journal benchmark is appropriate

Output:
- `ideas/evaluation/review_eval_idea1.md`
- decision: `AGREE`, `PARTIALLY AGREE`, or `DISAGREE`
- adjusted score if needed
- instruction to rerun Step 1 if the critique is materially unfair
- maximum 200 words unless the human asks for an expanded audit

### 3. Pivot Idea

Trigger:
- score below `7`
- review says the idea has a fixable weakness
- human wants a stronger version of the same core topic

Pivot rules:
- keep the core topic unless the human approves a larger reset
- add or sharpen credible identification, a theory mechanism, or method innovation
- for empirical papers, name a specific shock, instrument, natural experiment, or source of variation
- name the paper or institutional fact that makes the identification approach credible when available
- state the new one-sentence contribution
- name datasets, variables, sample period, and empirical design when empirical
- write the main regression equation when possible
- include at least one placebo or falsification test when empirical
- include at least one heterogeneity or mechanism test when empirical
- state what failed in prior pivot attempts
- explain why a referee cannot dismiss the pivot as a simple application of an existing paper

Output:
- `ideas/evaluation/pivot_idea1.md`
- if iterating: `pivot_idea1_v2.md`, `pivot_idea1_v3.md`
- maximum 400 words unless the human asks for an expanded design memo

Maximum:
- three pivot iterations before recommending stop, split, or new idea search unless the human override is recorded in `decision_log.md` and `qa/waiver_log.md`.

### 4. Evaluate Pivot

Goal:
- rescore the pivot with the same criteria as Step 1

Output:
- `ideas/evaluation/eval_pivot_idea1.md`
- if score drops or stays flat, return to Step 3 with full history
- if score reaches threshold, move to threat-literature search

### 5. Literature Map And Threat Literature Search

Goal:
- organize the broader literature map, then find missed papers that threaten the contribution before committing to the project

Search sequence:
1. Extract missing clusters from `ideas/literature_map.md` / second_brain notes.
2. Query OpenAlex for broad graph/index coverage and related works.
3. Query Semantic Scholar for citation/context expansion and verification.
4. Query Crossref for DOI/metadata confirmation.
5. Query RePEc, NBER, SSRN, arXiv, CEPR, publisher pages, or Google Scholar for econ/finance working-paper and freshness gaps.

Search for:
- papers testing the same mechanism
- papers using the same identification strategy on a related question
- recent working papers from SSRN, NBER, CEPR, arXiv, or institution repositories
- adjacent finance, economics, accounting, urban, real estate, or ML papers that could preempt the contribution
- top finance and top economics papers first, then direct working-paper threats

For every threat paper, record:
- full citation
- verifiable URL
- two to three sentences explaining the direct threat
- threat level: `HIGH`, `MEDIUM`, or `LOW`
- why it threatens the idea
- what part of the idea survives

Output:
- `ideas/literature_map.md`
- `ideas/evaluation/threat_lit_idea1.md`
- structured external search files under `data/external/` only after project promotion, or summarized in the second_brain research-idea note before repo promotion

Hard rule:
- no URL, no citation. If you cannot verify a paper, do not include it as evidence.

### 6. Verify Literature Map And Threat Literature

Goal:
- verify literature-map sources, remove hallucinated or mischaracterized citations before the idea gate, and separate machine-discovered graph/index leads from verified manuscript evidence

For every cited paper:
- verify title, authors, year, outlet, and URL
- correct citation metadata when wrong
- remove fabricated or unverifiable papers
- check whether threat level is accurate
- add obvious missed direct-threat papers found during verification

Output:
- updated `ideas/literature_map.md`
- updated `ideas/evaluation/threat_lit_idea1.md`
- `ideas/evaluation/review_threat_lit_idea1.md`

The verification summary must state whether the gap still holds after removing weak or fake evidence.

The verification file must record:
- papers confirmed real with URLs
- papers removed as fabricated or unverifiable
- citation metadata corrections
- characterization or threat-level corrections
- missing papers added during verification
- whether the gap analysis still holds

### 7. Final Verdict

Goal:
- decide whether to start a full project, pivot again, downgrade target, or stop

Output:
- `ideas/evaluation/final_verdict_idea1.md`

Required sections:
- final score and score justification
- criterion-level justification for new contribution, methods, theory or empirics, impact, feasibility, and timeliness
- why the score is not one point higher or lower
- top three remaining threats
- how to address each threat
- exact preconditions for proceeding
- primary and backup target journal/audience
- suggested title
- one-paragraph abstract skeleton
- key risk that could kill the paper
- decision label from the allowed status list below

Allowed statuses:
- `PROCEED`
- `PROCEED WITH CONDITIONS`
- `PIVOT`
- `TARGET DOWN`
- `STOP`
- `SPLIT`

Preconditions must be concrete go/no-go gates, such as:
- verify data access
- confirm first-stage strength
- reproduce key variable construction
- read two direct-threat papers fully
- run a minimal empirical, theoretical, or simulation test

### 8. Review Final Verdict

Goal:
- audit whether the final verdict follows the evidence

Check:
- whether the score is consistent with the full history
- whether criterion-level scores map to the final score
- whether threat assessment is too harsh or too lenient
- whether earlier threat papers or weaknesses were dropped without reason
- whether title and abstract frame the strongest contribution
- whether preconditions are actionable
- whether earlier concerns were dropped without reason

Output:
- `ideas/evaluation/review_final_verdict_idea1.md`
- final decision confirmation or required return to Step 3
- decision: `AGREE`, `PARTIALLY AGREE`, or `DISAGREE`
- if score is below `7`, recommend `PIVOT AGAIN`, `ADJUST`, or `ACCEPT AT LOWER TARGET`
- maximum 300 words unless the human asks for an expanded audit

## Master File

Maintain one master file:

```text
ideas/idea_evaluation.md
```

or, before a repo exists:

```text
~/Library/CloudStorage/SynologyDrive-second_brain/wiki/research-ideas/<idea_slug>.md
```

Append each step under dated headings. The file should read as the idea's complete evaluation history.

## Project Promotion

When final decision is `PROCEED` or `PROCEED WITH CONDITIONS`:
- create or choose the project repo under `/home/nanyeon99/project/<repo_name>`
- copy or summarize the master evaluation into `question/main_question.md`
- record the final verdict in `decision_log.md`
- put unresolved preconditions in `next_actions.md`
- list literature-map communities, threat papers, adjacent papers, and accepted source roles in `source_context.md`
- split final-verdict preconditions into `auto_checkable_preconditions` and `human_decision_preconditions`
- move to `02_workflows/project_structure.md`

When final decision is `PIVOT`, `TARGET DOWN`, `STOP`, or `SPLIT`:
- keep the evaluation in second_brain research ideas or project memory
- do not create a full project repo unless the human asks
- if a project already exists, record the result in `question/pivots/` or `research_log.md`

## Guardrails

- Do not inflate scores to justify work already started.
- Do not treat a clever method as a contribution unless it answers a meaningful economics or finance question.
- Do not accept "different country/sample" as a new contribution by itself.
- Do not infer causality from descriptive, predictive, or correlational designs.
- Do not fabricate citations, journals, URLs, data access, or identification sources.
- Keep target journal realistic; a strong field-journal idea is better than a weak top-3 claim.
- Human override is allowed, but record it as a decision.
