# AI Governance Framework

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

**Status:** Draft complete, for review | **Stage:** 4 | **Area:** Governance; AI & Data Governance

**Organisation:** Kijani Heights Golf and Country Club (fictional), see the [organisation profile](../scenario/organisation-profile.md)

**Notion page:** added after the site is published

## 1. Overview and business problem

The Club launched an AI chatbot (Kijani Assist) and number-plate recognition without listing, classifying or testing them, and with no rules for staff use of generative AI.

## 2. Objectives, scope and assumptions

Put every AI system under a lifecycle with classification, assessment, testing, human oversight, vendor checks and change control. Personal data assessments sit in the [data protection project](../data-protection-privacy-assurance/README.md). Assumptions: [assumptions register](01-project-charter/assumptions-register.csv).

## 3. Frameworks and methodology

NIST AI RMF 1.0 functions and the ISO/IEC 42001:2023 management system approach, in Kenya's data protection context. No certification is claimed. Details: [methodology](02-methodology/methodology.md).

## 4. Deliverables and selected evidence

| Deliverable | File | Status |
|---|---|---|
| AI governance charter | [ai-governance-charter.md](06-oversight/ai-governance-charter.md) | Draft for review |
| AI system inventory and use-case register | [ai-system-inventory.csv](03-ai-inventory/ai-system-inventory.csv) | Draft for review |
| AI risk classification methodology | [ai-risk-classification-method.md](04-classification/ai-risk-classification-method.md), [use-case-classification.csv](04-classification/use-case-classification.csv) | Draft for review |
| AI impact assessment | [ai-impact-assessment-kijani-assist.md](05-impact-assessment/ai-impact-assessment-kijani-assist.md) | Draft for review |
| AI testing and validation protocol | [ai-testing-protocol.md](05-impact-assessment/ai-testing-protocol.md), [test-results.csv](05-impact-assessment/test-results.csv) | Draft for review |
| Human oversight and accountability matrix | [human-oversight-matrix.csv](06-oversight/human-oversight-matrix.csv) | Draft for review |
| AI acceptable-use policy | [ai-acceptable-use-policy.md](06-oversight/ai-acceptable-use-policy.md) | Draft for review |
| Vendor AI due-diligence checklist | [vendor-ai-due-diligence-checklist.csv](07-third-party/vendor-ai-due-diligence-checklist.csv) | Draft for review |
| Model change register | [model-change-register.csv](07-third-party/model-change-register.csv) | Draft for review |
| AI incident and exception register | [ai-incident-register.csv](08-incidents/ai-incident-register.csv) | Draft for review |
| AI governance committee report | [ai-governance-committee-report.md](10-reporting/ai-governance-committee-report.md) | Draft for review |

## 5. Testing results or evaluation criteria

Kijani Assist was tested with 150 prompts (scenario results): version 1.0 failed 3 of 30 account tests and 2 of 20 adversarial tests; version 1.1 passed all of them and reached 96% overall. Swahili accuracy reached 85% against a 90% target. Sauti AI Labs scored 35 of 45 in vendor due diligence. Details: [test results](05-impact-assessment/test-results.csv).

## 6. Recommendations and implementation roadmap

Approve the charter, Kijani Assist v1.1 and opt-in ANPR; improve Swahili accuracy and retest (March 2027); obtain the vendor's security certificate (February 2027); brief staff on the acceptable-use policy (March 2027). See the [committee report](10-reporting/ai-governance-committee-report.md).

## 7. Limitations and lessons learned

See [limitations](limitations.md). Lessons: testing before and after fixes gave the Committee hard evidence for its decision; and a structured classification made it easy to reject a risky vendor tool early.

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
