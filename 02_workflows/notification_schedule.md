# Notification Schedule

Updated: 2026-05-24

Status: v2 workflow. Use with `04_templates/work_hours.yaml` and `04_templates/dashboard_schema.yaml`.

Purpose

This workflow defines when the research system should notify Chan during v2 project execution. It separates critical interruptions from digest-level updates. It protects working time while still pushing mandatory human gates immediately.

## 1. Timezone

All schedules use Asia/Seoul unless a project-local config explicitly says otherwise.

## 2. Daily modes

Morning briefing runs once between 09:00 and 12:00. It summarizes overnight work, blocked gates, critical risks, and the day's likely decisions. After the morning briefing, non-critical updates wait for the next digest.

Midday digest runs at 12:00. It summarizes completed lanes, current blockers, and any decisions likely to arrive before 15:00.

Afternoon digests run at 15:00 and 17:00. They should be short. They report lane completions, gate progress, and next likely action.

End-of-day digest runs at 18:00. It records what changed, what remains blocked, and which artifacts were updated.

Overnight handoff briefing runs at 20:00. It states which jobs or agents may continue overnight, what they are allowed to do, and what must wait for Chan.

After 20:00, notifications are critical only.

## 3. Critical notifications

Critical notifications may push immediately during work hours. After 20:00 they should push only if the issue affects safety, irreversible external action, data loss, active paid resources, or a mandatory human gate that Chan asked to receive immediately.

Critical categories:

- Human `gate_4` reached after Phase 2 pilot.
- Human `gate_6` reached after Phase 3 main analysis.
- A lane needs to change locked spec, sample, estimator, outcome, preprocessing, or claim mapping.
- A direct threat paper appears that may change novelty or claim strength.
- A long-running job failed in a way that risks losing state or wasting large compute.
- A credential, upload, external submission, paid download, or live API side effect needs approval.
- An integrity gate blocks writing, submission, or replication release.
- A server, repo, or branch state conflict could make agents overwrite each other.

## 4. Non-critical notifications

Non-critical updates wait for the next digest.

Non-critical categories:

- Routine lane completion.
- New artifact written with no blocker.
- Successful smoke test.
- Minor documentation update.
- Literature scan completed without a direct novelty threat.
- Dashboard or changelog mirror updated.
- Archive index updated after a normal narrowing decision.

## 5. Human gate immediate push rule

When `gate_4` or `gate_6` is reached during work hours, push immediately. The notification should include the gate packet path, recommended decision, risks, and exact options. Do not continue past the gate until Chan records a decision.

When a human gate is reached after 20:00, prepare the gate packet and include it in the 20:00 handoff if possible. If it is reached later, push only if Chan has opted into after-hours gate notifications or the project has a critical deadline.

## 6. Focus mode

`focus_mode_on` suppresses non-critical notifications. It does not suppress critical safety items or mandatory human gates during core work hours.

When focus mode is on, digests should be shorter and only include:

- unresolved human gates
- critical blockers
- state-changing decisions needed today
- overnight permission requests

## 7. Day-of-week customization

Weekdays use the full schedule.

Saturday and Sunday are critical only by default. A weekend digest may be sent only if a project has an active deadline, Chan requested weekend monitoring, or overnight agents require a safety handoff.

Project-local configs may add deadline windows, but they must not create live external side effects without approval.

## 8. Delivery channels

Hermes may deliver notifications through dashboard, changelog mirror, Telegram bridge, or configured Slack bridge. Channel tokens and IDs must live in `.env` or local config outside the public repo.

`04_templates/dashboard_schema.yaml` defines the minimum read-only dashboard fields, the `open_human_gates` labels (`gate_4`, `gate_6`, or both), and the mapping from dashboard state to critical, digest, or silent notification handling. The dashboard is visibility only. It must not infer gate pass status, cross human gates, edit project repos, or expose private channel identifiers.

`04_templates/work_hours.yaml` contains placeholders only. Do not commit real bot tokens, chat IDs, Slack channel IDs, or private webhook URLs.

## 9. Minimum notification payloads

Critical payload:

```text
Project:
Phase:
Severity: critical
Reason:
Artifact paths:
Decision needed:
Options:
Recommended option:
What stops until decision:
```

Digest payload:

```text
Project:
Phase:
Window:
Completed:
Blocked:
Next:
Artifacts changed:
Human action needed:
```

## 10. Agent behavior

Codex master decides whether a research event is critical, but Hermes delivers the notification. Hermes should not infer gate status from notification text alone. Gate status remains in `qa/gate_status.yaml`.

If the notification schedule conflicts with a project-specific human instruction, the human instruction wins and should be recorded in `decision_log.md` or project config.
