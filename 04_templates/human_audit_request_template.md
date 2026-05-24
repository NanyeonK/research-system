# Human Audit Request: <project> / <decision slug>

Status: DRAFT | READY_FOR_HUMAN | DECIDED
Created: YYYY-MM-DD
Prepared by: <agent/session>
Project repo: `<server>:<repo_path>`
Gate blocked: <gate name>
Decision owner: Yeonchan

## 1. Plain-language question
What decision is needed, in one sentence a non-agent can understand?

Example: Should this project rebuild the analysis from scripts/config references only, instead of directly restoring archived data/output/paper artifacts?

## 2. Why this is being asked now
- What gate or workflow stopped?
- What artifact, result, or conflict triggered human audit?
- Why can the agent not decide this alone?

## 3. Evidence inspected
| Artifact | Path | What it shows | Reliability |
|---|---|---|---|
| <artifact> | `<path>` | <fact> | source / diagnostic / superseded / unknown |

## 4. Options

### Option A — <human-readable name>
Meaning:
- <what will happen>

Use this if:
- <condition>

Consequences:
- Time/cost: <estimate or MISSING>
- Scientific risk: <risk>
- Provenance risk: <risk>
- What gets skipped/rebuilt/restored: <explicit list>

### Option B — <human-readable name>
Meaning:
- <what will happen>

Use this if:
- <condition>

Consequences:
- Time/cost: <estimate or MISSING>
- Scientific risk: <risk>
- Provenance risk: <risk>
- What gets skipped/rebuilt/restored: <explicit list>

## 5. Agent recommendation
Recommended option: <A/B/C or NONE>

Reason:
- <evidence-based rationale>

What would be unsafe about the other option(s):
- <specific concern>

## 6. Exact approval phrase
If you approve the recommendation, reply with:

```text
Approve: <human-readable option name>. <one sentence restating the concrete action>.
```

If you choose a different option, reply with:

```text
Choose: <option name>. <any constraint or exception>.
```

## 7. After-decision execution plan
If approved, the next agent action will be:
1. <action>
2. <action>
3. <verification>

The agent will not do these without separate approval:
- <side effect>
- <gate crossing>

## 8. If no decision is made
Default safe behavior:
- <wait / continue only non-blocking EDA / mark blocked>
