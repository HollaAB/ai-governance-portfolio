# Data Dictionary: Obligations Register Files

## compliance-register.csv

| Column | Meaning | Allowed values |
|---|---|---|
| id | Obligation identifier | OB-01 onwards |
| obligation | What the Club must do, in plain words | Text |
| source | Law, regulation, contract or internal rule | Text |
| area | Compliance area | Data protection, Anti-bribery, Employment, Health and safety, Tax, Licensing, Environment, Corporate, Payments, Security, Golf operations, Anti-money laundering |
| type | Kind of source | Statute, Regulation, Statute and regulation, County law, Contract, Internal rule |
| applies | Whether it applies to the Club | Yes, No |
| applicability_reason | Why it applies or not | Text |
| owner_role | Role accountable for meeting it | A role from the organisation profile |
| frequency | How often it recurs | Continuous, Monthly, Quarterly, Annually, Event-driven, other stated period |
| due_rule | When it must be done | Text |
| control_refs | Controls that meet it | CTL-xx, separated by semicolons |
| evidence_refs | Evidence that shows it is met | EV-xx |
| source_check | Whether the legal reference has been checked against the official text | To verify, Verified |
| status | Compliance status | Not yet assessed, Compliant, Partly compliant, Not compliant |

## obligations-to-controls-matrix.csv

| Column | Meaning | Allowed values |
|---|---|---|
| control_id | Control identifier | CTL-01 onwards |
| control | What the control does | Text |
| control_type | How it works | Preventive, Detective, Corrective |
| owner_role | Role that runs the control | Role |
| obligations_covered | Obligations the control meets | OB-xx, separated by semicolons |
| status | Control status | Proposed, Implemented, Tested and effective, Tested with exceptions |
| test_planned | When it will be tested | Text |

## compliance-calendar.csv

| Column | Meaning | Allowed values |
|---|---|---|
| id | Calendar entry | CAL-01 onwards |
| obligation_id | Obligation it serves | OB-xx |
| activity | Task to do | Text |
| frequency | Recurrence | Monthly, Quarterly, Annually, Every 24 months, Event-driven |
| due_rule | Rule for the deadline | Text |
| owner_role | Role responsible | Role |
| reminder_before | Lead time for the reminder | Text |
| next_due | Next due date (scenario) | YYYY-MM-DD or "When triggered" |

## evidence-register.csv

| Column | Meaning | Allowed values |
|---|---|---|
| id | Evidence identifier | EV-01 onwards |
| obligation_id | Obligation it supports | OB-xx |
| evidence_item | The document or record | Text |
| format | File type | Text |
| location | Where it is kept (fictional) | Text |
| owner_role | Role that keeps it | Role |
| status | Collection status | Not yet collected, Collected, Reviewed |

## Validation rules

- Every obligation with `applies` = Yes has an owner, at least one control and at least one evidence item.
- Every control lists at least one obligation.
- `status` stays "Not yet assessed" until the Stage 2 gap assessment tests it.
