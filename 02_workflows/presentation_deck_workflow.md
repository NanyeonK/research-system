# Presentation Deck Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Engine skills:
- `/paper-poster` — scaffolds poster LaTeX from paper plan and figures.
- `/paper-slides` — scaffolds slide deck LaTeX (Beamer or similar) from paper plan and figures.
- `/paper-talk` — drafts spoken-talk script aligned with the deck.

Binding rules:
- Deck content (claims, numbers, figure choice) follows our paper's `paper/writing_kickoff_decisions.md` and exhibit memos.
- Visual style follows `/Users/nanyeon/Library/CloudStorage/SynologyDrive-second_brain/writing_system/policies/table_figure_style.md` and the paper's manuscript style; ARIS venue defaults are subordinate.
- Compile/render QA from this workflow stays mandatory: render to PDF, inspect every page, verify figures and tables fit, check overflow.
- Poster/slides voice follows `voice_yeonchan.md` § Tone & Stance and § Citations; ARIS prose templates do not override.

Purpose:
- create and revise research decks as code-generated, rendered, visually checked artifacts
- keep talks, collaborator decks, and audit decks aligned with paper evidence
- prevent silent LaTeX, TikZ, figure, and rhetoric failures before anyone shares a deck

Source:
- Adapted from Scott Cunningham's `MixtapeTools` presentation, beautiful-deck, compiledeck, and TikZ protocols:
  - https://github.com/scunning1975/MixtapeTools/tree/main/presentations
  - https://github.com/scunning1975/MixtapeTools/tree/main/skills/beautiful_deck
  - https://github.com/scunning1975/MixtapeTools/tree/main/skills/compiledeck
  - https://github.com/scunning1975/MixtapeTools/tree/main/skills/tikz
- Source evidence grade: `B` for workflow use. These are concrete public deck-generation and visual-audit protocols, but they are not manuscript literature evidence.
- Local deployment status: accepted by human instruction on 2026-04-30.

## Trigger

Use this workflow when:
- creating a seminar, conference, teaching, collaborator, or referee-audit deck
- revising a Beamer, Quarto, Typst, reveal.js, or Marp deck for research communication
- converting paper evidence into slides
- checking TikZ or figure-heavy slides before sharing

Use the `presentations` skill when the deliverable is a `.pptx` deck. Use this workflow for project policy, evidence discipline, and QA gates around decks.

## Triage Before Slides

Record:
- audience: academic seminar, conference, teaching, coauthor working deck, policy/media/industry, or internal audit
- purpose: persuade, teach, diagnose, decide, or document
- duration and slide budget
- source materials
- one-sentence takeaway
- required exhibits and source paths
- output format
- style constraints from collaborators, journal, lab, or venue

Do not write slides before audience, purpose, and takeaway are explicit.

## Rhetoric Rules

Default rules:
- one idea per slide
- titles state claims, not labels
- the title sequence should summarize the argument
- bullets are a fallback; prefer sequence, contrast, hierarchy, causal chain, table, or figure
- slides serve speech; they are not a paper pasted into frames
- keep cognitive cost roughly balanced across slides

For teaching decks, move from:
- narrative
- application
- picture
- code or worked example
- technical statement

For research talks, keep identification, data, and evidence visible before large claims.

## Evidence Rules

Every quantitative slide must trace to:
- source data or paper source
- generation script
- output file
- table/figure manifest or mapped equivalent
- current claim boundary

Generate figures and tables from code before including them in the deck.

Do not paste manual screenshots as the source of truth unless the screenshot is the object under study or the human explicitly accepts the exception.

## Visual QA

Before sharing a deck:
- compile or render the deck
- inspect the rendered artifact, not only the source
- check overfull and underfull warnings when using LaTeX
- check figure labels, legends, axes, notes, and clipping
- check slide titles for assertion form
- check every TikZ diagram for collisions, missing directional labels, clipped text, and inconsistent repeated diagrams
- rerender after fixes

For TikZ:
- use explicit node dimensions for complex diagrams
- add direction keywords or anchors on edge labels
- avoid `scale` on complex diagrams because text size and coordinates can diverge
- keep a coordinate map comment for nontrivial diagrams

## Output Layout

Recommended project-local layout:

```text
decks/
  <deck_slug>/
    <deck_slug>.tex
    <deck_slug>.pdf
    outline.md
    scripts/
    figures/
    tables/
    audit.md
```

Use existing project conventions when they are coherent. Document the deck path in `project_state.md` or `research_log.md` if the deck drives a research decision.

## Guardrails

- Do not let slide polish change manuscript claims without a decision-log entry.
- Do not use visual appeal to hide weak evidence.
- Do not report a deck as done until the rendered artifact has been checked.
- Do not attempt external sharing, submission, or email without human approval.
