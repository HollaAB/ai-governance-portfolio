# Data Protection and Privacy Assurance

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

**Status:** Draft complete, for review | **Stage:** 4 | **Area:** Compliance; AI & Data Governance

**Organisation:** Kijani Heights Golf and Country Club (fictional), see the [organisation profile](../scenario/organisation-profile.md)

**Notion page:** added after the site is published

## 1. Overview and business problem

The [Stage 2 compliance review](../compliance-management-system/07-reporting/management-report.md) found the Club's biggest gaps in data protection: no record of processing, no DPIAs for number-plate recognition or the AI chatbot, processor contracts without data protection terms, no retention schedule and no breach procedure.

## 2. Objectives, scope and assumptions

Build a working data protection programme and close those findings. AI-specific governance of the chatbot is covered in the [AI Governance Framework](../ai-governance-framework/README.md). Assumptions: [assumptions register](01-project-charter/assumptions-register.csv).

## 3. Frameworks and methodology

Kenya's Data Protection Act 2019 and its 2021 regulations, with the DPIA structure from ODPC guidance (to verify). Details: [methodology](02-methodology/methodology.md).

## 4. Deliverables and selected evidence

| Deliverable | File | Status |
|---|---|---|
| Personal data inventory (record of processing) | [personal-data-inventory.csv](03-data-inventory/personal-data-inventory.csv) | Draft for review |
| Data-flow map | [data-flow-map.md](03-data-inventory/data-flow-map.md) | Draft for review |
| DPIAs | [dpia-01-gate-cctv-and-anpr.md](04-dpia/dpia-01-gate-cctv-and-anpr.md), [dpia-02-kijani-assist.md](04-dpia/dpia-02-kijani-assist.md), [dpia-procedure.md](04-dpia/dpia-procedure.md) | Draft for review |
| Processor register and transfer assessment | [processor-register.csv](05-processors/processor-register.csv), [cross-border-transfer-assessment.md](05-processors/cross-border-transfer-assessment.md) | Draft for review |
| Retention schedule | [retention-schedule.csv](06-retention/retention-schedule.csv), [disposal-log.csv](06-retention/disposal-log.csv) | Draft for review |
| Privacy notice and CCTV signs | [privacy-notice.md](07-rights-and-notices/privacy-notice.md) | Draft for review |
| Data subject request procedure | [data-subject-request-procedure.md](07-rights-and-notices/data-subject-request-procedure.md), [data-subject-request-log.csv](07-rights-and-notices/data-subject-request-log.csv) | Draft for review |
| Breach response plan | [breach-response-plan.md](08-breach-response/breach-response-plan.md), [breach-log.csv](08-breach-response/breach-log.csv) | Draft for review |
| Privacy assurance report | [privacy-assurance-report.md](10-reporting/privacy-assurance-report.md) | Draft for review |

## 5. Testing results or evaluation criteria

A follow-up privacy assurance review (scenario results): 5 of 6 October findings closed; 14 of 14 activities recorded; 3 of 3 high-risk activities with an approved DPIA; 4 of 6 processors under agreement; 4 of 4 requests answered on time; one breach assessed within 24 hours. Five new findings (2 Medium need Committee attention).

## 6. Recommendations and implementation roadmap

Sign agreements with Linda Guard Services (January 2027) and the events partner (March 2027), finish disposal of old records (January 2027), and train staff (March 2027). See the [privacy assurance report](10-reporting/privacy-assurance-report.md) and [corrective actions](09-findings-and-actions/corrective-action-tracker.csv).

## 7. Limitations and lessons learned

See [limitations](limitations.md). Lessons: most risk came from new technology adopted without assessment, and simple fixes (shorter retention, opt-in ANPR, no account data to the model provider) cut residual risk sharply without stopping the services.

## Project documents

| Document | File |
|---|---|
| Project charter | [project-charter.md](01-project-charter/project-charter.md) |
| Version history | [version-history.md](01-project-charter/version-history.md) |
| Assumptions register | [assumptions-register.csv](01-project-charter/assumptions-register.csv) |
| Methodology | [methodology.md](02-methodology/methodology.md) |
| Evidence index | [evidence-index.csv](evidence-index.csv) |
| Findings register | [findings-register.csv](09-findings-and-actions/findings-register.csv) |
| Corrective-action tracker | [corrective-action-tracker.csv](09-findings-and-actions/corrective-action-tracker.csv) |
| KPI/KRI definitions | [kpi-definitions.csv](10-reporting/kpi-definitions.csv) |
| Executive summary | [executive-summary.md](10-reporting/executive-summary.md) |
| Limitations statement | [limitations.md](limitations.md) |
