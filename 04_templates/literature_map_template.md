# Literature Map Template

Use with `02_workflows/idea_evaluation.md` before scoring a rough idea and before promoting an idea into a project.

## Metadata

Date:

Idea slug:

Owner:

Topic / mechanism:

Graphify corpus path:

Graphify output path:

External indexes checked: OpenAlex | Semantic Scholar | Crossref | RePEc | NBER | SSRN | arXiv | Google Scholar | publisher pages | other

## Search Scope

### second_brain / Graphify scope

Existing graph checked: YES | NO

Existing graph path:

Existing `GRAPH_REPORT.md` read: YES | NO

Bounded corpus built: YES | NO

Raw-source access mode: existing graph | wiki markdown only | hydrated raw cache | external search only

Hydration cache root, if used: `/Users/nanyeon/second_brain_exec/raw_cache`

Hydration command(s), if used:
- `/Users/nanyeon/bin/second_brain_hydrate.py hydrate raw/...`

Hydration blocked / source materialization gaps:
- 

Corpus folders included:
- `wiki/sources/`
- `wiki/concepts/`
- `wiki/research-ideas/`
- project notes:
- other:

Why this scope is enough for idea-stage evaluation:

Known scope gaps:

### External search scope

OpenAlex query strings:

Semantic Scholar / Crossref / RePEc / SSRN / NBER / arXiv query strings:

Manual search strings:

Freshness window checked:

## Literature Communities

| community_id | label | central papers / nodes | mechanism | data / setting | method / identification | relevance to idea | source |
|---|---|---|---|---|---|---|---|
| C01 |  |  |  |  |  |  | Graphify / OpenAlex / manual |

## Direct Threats

| threat_id | citation | URL / DOI / OpenAlex ID | threat level | why it threatens the idea | what survives | verification status |
|---|---|---|---|---|---|---|
| T01 |  |  | HIGH / MEDIUM / LOW |  |  | VERIFIED / ACCESS_LIMITED / UNVERIFIED |

## Adjacent Literature

| source_id | citation | URL / DOI / OpenAlex ID | role | what it contributes | why it is not a direct threat | verification status |
|---|---|---|---|---|---|---|
| A01 |  |  | background / method / data / setting / mechanism |  |  |  |

## Gap / Bridge Assessment

Plausible gap:

Graph bridge or community connection that supports the idea:

Known crowded cluster:

Where novelty is weakest:

Where contribution is strongest:

## Machine-Generated Findings To Verify

| item_id | machine finding | source | human/auditor check needed | status |
|---|---|---|---|---|
| M01 |  | Graphify / OpenAlex / other |  | OPEN / VERIFIED / REJECTED |

## Idea-Gate Literature Verdict

Literature map status: INCOMPLETE | ENOUGH_FOR_PRELIMINARY_SCORE | ENOUGH_FOR_FINAL_VERDICT | BLOCKED

Can Step 1 score exceed 6.5? YES | NO

Reason:

Required before project promotion:
- [ ] direct threat papers verified
- [ ] closest communities identified
- [ ] novelty gap survives after verification
- [ ] source roles copied into `source_context.md` if promoted
- [ ] central literature claims planned for `qa/claim_verification_matrix.md`
