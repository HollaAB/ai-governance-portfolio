# Security Risk and Incident Management

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

**Status:** In progress (Stage 5 draft for review) | **Stage:** 5 | **Area:** Security

**Organisation:** Kijani Heights Golf and Country Club (fictional), see the [organisation profile](../scenario/organisation-profile.md)

**Notion page:** [TODO: link, added after publishing]

## 1. Overview and business problem

A personal data breach through cloud systems or supplier access is the Club's highest enterprise risk (R-01), yet access had never been reviewed and incident response and recovery had never been tested.

## 2. Objectives, scope and assumptions

Assess security risk across sites and systems, review access, and build and test incident response and continuity. No technical testing of real systems. Assumptions: [assumptions register](01-project-charter/assumptions-register.csv).

## 3. Frameworks and methodology

ISO 31000:2018 risk assessment, NIST Cybersecurity Framework 2.0 functions and ISO 22301:2019 continuity concepts; no certification claimed. Details: [methodology](02-methodology/methodology.md).

## 4. Deliverables and selected evidence

| Deliverable | File | Status |
|---|---|---|
| Security assessment and asset inventory | [asset-inventory.csv](03-security-assessment/asset-inventory.csv), [threat-vulnerability-assessment.csv](03-security-assessment/threat-vulnerability-assessment.csv), [site-security-survey.md](03-security-assessment/site-security-survey.md) | Draft for review |
| Security risk register | [security-risk-register.csv](03-security-assessment/security-risk-register.csv) | Draft for review |
| Access review | [access-control-policy.md](04-access-review/access-control-policy.md), [role-access-matrix.csv](04-access-review/role-access-matrix.csv), [access-review.csv](04-access-review/access-review.csv), [access-review-report.md](04-access-review/access-review-report.md), [phishing-simulation-results.csv](04-access-review/phishing-simulation-results.csv) | Draft for review |
| Incident response playbook | [incident-response-plan.md](05-incident-response/incident-response-plan.md), [severity-matrix.csv](05-incident-response/severity-matrix.csv), [incident-playbooks.md](05-incident-response/incident-playbooks.md), [chain-of-custody-form.md](05-incident-response/chain-of-custody-form.md) | Draft for review |
| Incident chronology | [scenario.md](06-tabletop-exercise/scenario.md), [incident-chronology.csv](06-tabletop-exercise/incident-chronology.csv) | Draft for review |
| Tabletop exercise report | [tabletop-exercise-report.md](06-tabletop-exercise/tabletop-exercise-report.md) | Draft for review |
| Remediation report | [security-management-report.md](09-reporting/security-management-report.md), [business-impact-analysis.csv](07-continuity/business-impact-analysis.csv), [continuity-and-recovery-plan.md](07-continuity/continuity-and-recovery-plan.md), [recovery-test-results.csv](07-continuity/recovery-test-results.csv) | Draft for review |

## 5. Testing results or evaluation criteria

Scenario results: 14 of 24 accounts appropriate; 23% phishing click rate; in the tabletop exercise, ODPC notification at about 50 hours (target 72, met) and member warning at about 52 hours (target 24, not met); 2 of 4 recovery tests met. 10 findings (2 High, 6 Medium, 2 Low); both High fixed within a week.

## 6. Recommendations and implementation roadmap

Named reception accounts (February 2027), member warning template (February 2027), supplier alerts and out-of-hours contact (March 2027), backup frequency decision (March 2027), awareness training and spare recorder (April 2027). See the [security management report](09-reporting/security-management-report.md) and [corrective actions](08-findings-and-actions/corrective-action-tracker.csv).

## 7. Limitations and lessons learned

See [limitations](limitations.md). Lessons: the exercise found the same root cause as the access review (a shared password without MFA), and the slowest step was a communication decision, not a technical fix.

## Project documents

| Document | File |
|---|---|
| Project charter | [project-charter.md](01-project-charter/project-charter.md) |
| Version history | [version-history.md](01-project-charter/version-history.md) |
| Assumptions register | [assumptions-register.csv](01-project-charter/assumptions-register.csv) |
| Methodology | [methodology.md](02-methodology/methodology.md) |
| Evidence index | [evidence-index.csv](evidence-index.csv) |
| Findings register | [findings-register.csv](08-findings-and-actions/findings-register.csv) |
| Corrective-action tracker | [corrective-action-tracker.csv](08-findings-and-actions/corrective-action-tracker.csv) |
| KPI/KRI definitions | [kpi-definitions.csv](09-reporting/kpi-definitions.csv) |
| Executive summary | [executive-summary.md](09-reporting/executive-summary.md) |
| Limitations statement | [limitations.md](limitations.md) |
