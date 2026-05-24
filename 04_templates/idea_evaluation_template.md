# Research Idea Evaluation Template

Use with `02_workflows/idea_evaluation.md`.

## Submission Metadata

Date:

Idea slug:

Owner:

Target field:

Target journal or audience:

Paper type: Empirical | Theoretical | Methodological | Mixed

## Idea Title

[One-line title.]

## Research Question

[One or two sentences stating the exact question.]

## Hypothesis Or Mechanism

[State the mechanism, expected sign or prediction, and what alternative explanations would predict differently.]

## Contribution Claim

[One paragraph explaining what the paper would teach that the closest papers do not. State why this is not a robustness check, a country or sample swap, or a simple application of an existing paper.]

## Empirical Design

Use for empirical or mixed papers.

Identification strategy:

Source of exogenous variation:

Instrument, shock, or natural experiment:

Paper, institutional fact, or setting that validates this variation:

Main regression or test:

Main regression equation:

Data sources:

Variables:

Sample period:

Unit of observation:

Controls, fixed effects, and standard errors:

Placebo or falsification test:

Heterogeneity or mechanism test:

Known data-access risk:

## Theory Design

Use for theoretical or mixed papers.

Agents:

Key friction or market structure:

New assumption relative to closest models:

Main prediction:

Comparative statics:

Empirical or calibration target if any:

## Method Design

Use for methodological or mixed papers.

Problem with existing method:

Proposed estimator, test, or procedure:

Key property to prove:

Simulation design:

Empirical demonstration:

What existing result may change:

## Literature Map

Use `04_templates/literature_map_template.md` for the full map. Summarize it here before scoring.

Literature map path:

Graphify existing output checked: YES | NO | NOT_AVAILABLE

Graphify corpus or query scope:

OpenAlex / external indexes checked:

Direct threat communities:

Adjacent literature communities:

Mechanism/data/method clusters:

Plausible gap or bridge:

Map status: INCOMPLETE | ENOUGH_FOR_PRELIMINARY_SCORE | ENOUGH_FOR_FINAL_VERDICT | BLOCKED

## Closest Paper 1

Citation:

URL:

Verified URL type: Google Scholar | SSRN | Publisher | Working paper page | Other

What it does:

How this idea differs:

Why a referee would cite it:

Threat level: HIGH | MEDIUM | LOW

## Closest Paper 2

Citation:

URL:

Verified URL type: Google Scholar | SSRN | Publisher | Working paper page | Other

What it does:

How this idea differs:

Why a referee would cite it:

Threat level: HIGH | MEDIUM | LOW

## Closest Paper 3

Citation:

URL:

Verified URL type: Google Scholar | SSRN | Publisher | Working paper page | Other

What it does:

How this idea differs:

Why a referee would cite it:

Threat level: HIGH | MEDIUM | LOW

## Why This Matters

[Policy relevance, theoretical implication, empirical importance, or practice relevance.]

## Known Weaknesses

[Identification, new-contribution, data, mechanism, measurement, timing, or target-journal risks.]

## Human Constraints

[Data access, collaborator constraints, deadline, preferred journal, methods to avoid, claims not to make.]

## Initial Gate Status

Status: DRAFT | READY FOR EVALUATION | BLOCKED

Blocking gaps:

## Interactive Co-Development Notes

Use this section before scoring when the idea starts rough.

Intake status: DRAFT | INTAKE_COMPLETE | READY_FOR_EVALUATION | BLOCKED

Outcome, behavior, price, risk, or decision to explain:

Mechanism and expected sign:

Why it matters now:

Candidate data:

Candidate identification, model innovation, or institutional setting:

Closest papers already known by the human:

What this paper should not claim:

Human constraints:

Sharpening moves considered:

Accepted sharpening move:

Remaining blocking gaps:

## Idea Brief Before Evaluation

Research question:

Mechanism:

Expected sign or prediction:

New contribution:

Candidate data and sample:

Candidate identification or method:

Literature map status:

Closest threat-paper status:

Should-not-claim boundary:

Ready for Step 1? YES | NO

## Evaluation Output Slots

Use these slots as the master-file structure when running `02_workflows/idea_evaluation.md`.

### Step 1. Evaluate Idea

Scoring rubric source: adapted Alejandro Lopez-Lira idea-evaluation-pipeline pressure; local research-system thresholds and literature-map rules control.

Score:

Criterion notes:
- New contribution and marginal contribution:
- Method or identification:
- Theory or empirical advancement:
- Impact:
- Feasibility and data:
- Relevance and timeliness:

Why not one point higher:

Fatal weaknesses:

### Step 2. Review Evaluation

Decision: AGREE | PARTIALLY AGREE | DISAGREE

Adjusted score if any:

Unfair or missing critique:

Rerun Step 1? YES | NO

### Step 3. Pivot Idea

Pivot version:

One-sentence new contribution:

Identification or method change:

Main regression, model, proof, or simulation change:

Placebo or falsification:

Heterogeneity or mechanism:

Why this avoids the prior weakness:

### Step 4. Evaluate Pivot

Score:

Why not one point higher:

Move to threat-literature search? YES | NO

### Step 5. Literature Map And Threat Literature Search

New threat papers:

Gap that survives:

Strongest not-just-X-applied-to-Y argument:

Defensive recommendations:

### Step 6. Verify Literature Map And Threat Literature

Papers confirmed:

Papers removed:

Citation corrections:

Threat-level corrections:

Missing papers added:

Does the gap still hold? YES | NO | CONDITIONAL

### Step 7. Final Verdict

Final score:

Why not one point higher:

Why not one point lower:

Top three remaining threats:

Suggested title:

One-paragraph abstract skeleton:

Primary target:

Backup target:

Key risk that could kill the paper:

Preconditions for proceeding:

Decision:
- PROCEED
- PROCEED WITH CONDITIONS
- PIVOT
- TARGET DOWN
- STOP
- SPLIT

### Step 8. Review Final Verdict

Decision: AGREE | PARTIALLY AGREE | DISAGREE

Score consistency:

Threat assessment:

Title and framing:

Preconditions:

Missed concerns:

If score is below 7: PIVOT AGAIN | ADJUST | ACCEPT AT LOWER TARGET
