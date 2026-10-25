# Compliance Management System

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

**Status:** Complete | **Stage:** 1 and 2 | **Area:** Compliance

**Organisation:** Kijani Heights Golf and Country Club (fictional), see the [organisation profile](../scenario/organisation-profile.md)

**Notion page:** added after the site is published

## 1. Overview and business problem

Kijani Heights Golf and Country Club, a fictional members' golf club in Kiambu County, has no single view of what it must comply with. Renewals sit in personal calendars and evidence is spread across departments. With data protection enforcement rising, the Management Committee wants to know every obligation, who owns it, and how compliance is shown.

## 2. Objectives, scope and assumptions

Build an obligations register, map each obligation to a control, set a compliance calendar and an evidence register (Stage 1), then test the controls and plan corrective actions (Stage 2). Legal advice and rules that do not apply to a golf club are out of scope. Assumptions: [assumptions register](01-project-charter/assumptions-register.csv).

## 3. Frameworks and methodology

Structured after ISO 37301:2021 (compliance management systems), applied to Kenyan law including the Data Protection Act 2019 and the Bribery Act 2016. No certification is claimed. Details: [methodology](02-methodology/methodology.md).

## 4. Deliverables and selected evidence

| Deliverable | File | Status |
|---|---|---|
| Legal and regulatory obligations register | [compliance-register.csv](03-obligations-register/compliance-register.csv) | Complete |
| Obligations-to-controls matrix | [obligations-to-controls-matrix.csv](03-obligations-register/obligations-to-controls-matrix.csv) | Complete |
| Compliance calendar | [compliance-calendar.csv](03-obligations-register/compliance-calendar.csv) | Complete |
| Evidence register | [evidence-register.csv](03-obligations-register/evidence-register.csv) | Complete |
| Regulatory change-monitoring procedure | [regulatory-change-procedure.md](03-obligations-register/regulatory-change-procedure.md) | Complete |
| Gap assessment and testing workpapers | [assessment-methodology.md](04-gap-assessment/assessment-methodology.md), [testing-workpapers.csv](04-gap-assessment/testing-workpapers.csv) | Complete |
| Controls matrix and compliance policy | [compliance-policy.md](05-controls-and-policies/compliance-policy.md) | Complete |
| Monitoring plan | [monitoring-plan.md](05-controls-and-policies/monitoring-plan.md) | Complete |
| Risk and control register (shared with later projects) | [risk-and-control-register.csv](risk-and-control-register.csv) | Complete |
| Management report | [management-report.md](07-reporting/management-report.md) | Complete |

## 5. Testing results or evaluation criteria

All 22 controls were tested against evidence, with samples where there was a population ([methodology](04-gap-assessment/assessment-methodology.md), [workpapers](04-gap-assessment/testing-workpapers.csv)). Scenario results: 7 controls effective, 10 with exceptions, 5 not implemented; 18 of 36 obligations compliant, 14 partly, 4 not. 16 findings (4 High, 9 Medium, 3 Low).

## 6. Recommendations and implementation roadmap

Fix the four High findings within 30 days (DPIAs, processor contracts, breach procedure, fire drill), Medium findings within 90 days and Low within 180 days, per the [corrective-action tracker](06-remediation/corrective-action-tracker.csv). Approve the [compliance policy](05-controls-and-policies/compliance-policy.md) and report the [KPIs](07-reporting/kpi-definitions.csv) quarterly under the [monitoring plan](05-controls-and-policies/monitoring-plan.md). See the [management report](07-reporting/management-report.md).

## 7. Limitations and lessons learned

See [limitations](limitations.md). Lessons: a single register exposed that most gaps sit in newer activities (AI, ANPR, cloud suppliers) rather than long-standing duties like tax; and tying every finding to an obligation and a control made the corrective actions easy to assign.

## Project documents

| Document | File |
|---|---|
| Project charter | [project-charter.md](01-project-charter/project-charter.md) |
| Version history | [version-history.md](01-project-charter/version-history.md) |
| Assumptions register | [assumptions-register.csv](01-project-charter/assumptions-register.csv) |
| Methodology | [methodology.md](02-methodology/methodology.md) |
| Evidence index | [evidence-index.csv](evidence-index.csv) |
| Data dictionary | [data-dictionary.md](03-obligations-register/data-dictionary.md) |
| Findings register | [findings-register.csv](06-remediation/findings-register.csv) |
| Corrective-action tracker | [corrective-action-tracker.csv](06-remediation/corrective-action-tracker.csv) |
| KPI/KRI definitions | [kpi-definitions.csv](07-reporting/kpi-definitions.csv) |
| Executive summary | [executive-summary.md](07-reporting/executive-summary.md) |
| Limitations statement | [limitations.md](limitations.md) |
