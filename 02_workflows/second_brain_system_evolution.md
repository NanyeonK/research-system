# Second Brain System Evolution Workflow

Purpose: make research-system progress, decisions, blocked audits, and repeated agent failures accumulate into second_brain so the framework improves over time without turning routine progress into noisy summaries.

## Scope

Use this workflow when:
- a research agent reaches a gate, block, pivot, or human audit request
- an automation rule is added, changed, or found confusing
- a project produces reusable lessons for future research projects
- a decision changes the allowed path for data, methods, tables, figures, writing handoff, or archive usage

## Storage layers

1. Repo-local source of truth
- `research_log.md`: chronological project actions.
- `decision_log.md`: human or agent decisions with rationale.
- `qa/gate_status.yaml`: machine-readable gate state.
- `qa/human_audit_request.md`: human-facing decision packet when a gate needs Yeonchan.
- `CHANGELOG.md`: repo progress ledger when the repo is package-like or long-lived.

2. Walnut / `04_Ventures/`
- Store cross-session operating memory and major system/project decisions.
- Do not mirror every routine log line manually.
- Record enough context for a cold agent to understand why a system rule changed.

3. Global wiki
- `wiki/projects/<project>.md`: stable project state and links.
- `wiki/journal/YYYY/MM/DD.md`: daily notable operations, decisions, and unresolved human audits.
- `wiki/journal/rules/<slug>.md`: reusable rules after repeated failures or accepted system changes.
- `wiki/journal/insights/<slug>.md`: durable methodological or operating insight.

## What must be saved

Always save these:
- human decisions and approvals, including exact wording when relevant
- gate blocks and human audit packets
- accepted automation/system-rule changes
- archive restore / rebuild / skip decisions
- dataset-lock decisions and waivers
- table/figure `FIX`, skip, or role decisions
- repeated failure patterns or confusing prompts

Do not manually save every routine worker step. Routine progress belongs in repo logs and dashboard indexes.

## Human-audit feedback loop

When Yeonchan says a human-audit request was unclear:
1. Treat it as a system design bug, not user friction.
2. Update the human-audit request template or relevant workflow immediately.
3. Save the correction to the research-system walnut.
4. If the pattern can recur, promote it to `wiki/journal/rules/` with examples.

## Evolution record format

For system changes, write a short run note or journal/rules note with:
- Trigger: what user/agent failure exposed the issue.
- Old behavior: what was unclear or unsafe.
- New rule: exact replacement behavior.
- Files changed: absolute paths.
- Verification: how the change was checked.

## Minimum daily/project bridge

At a natural pause after system changes:
- update the relevant walnut with zero-context log
- write or append a wiki rule/insight if the change is reusable
- keep `research_paper_system` docs as the canonical operational rule

## Anti-noise rule

Second_brain should evolve from decisions, repeated patterns, and stable lessons. It should not become a raw transcript dump. If a fact will be stale in a week and is already in a repo log/dashboard, do not promote it to global wiki unless it explains a rule change.
