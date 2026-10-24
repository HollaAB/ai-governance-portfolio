> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates and decisions are scenario results for the fictional Club.

## 1. Summary

Over five months, Kijani Heights Golf and Country Club, a fictional Kenyan members' golf club, moved from informal compliance and no AI or security governance to a connected system. Compliance with its 36 applicable obligations rose from 18 to 25. All 4 High compliance findings from October 2026 are closed. Both high-risk AI systems were assessed, tested and approved by the Committee. A January 2027 incident exercise showed the Club can now meet the ODPC's 72-hour breach deadline, but also exposed three cross-cutting weaknesses, now in one remediation roadmap.

## 2. The five projects

| Project | What it did | Key result |
|---|---|---|
| [Compliance Management System](https://github.com/HollaAB/ai-governance-portfolio/blob/main/compliance-management-system/README.md) | 37 obligations registered, 22 controls tested | 25 of 36 obligations now compliant |
| [Enterprise Governance and Risk Dashboard](https://github.com/HollaAB/ai-governance-portfolio/blob/main/enterprise-governance-risk-dashboard/README.md) | Governance framework, risk appetite, Committee oversight trail | Maturity from 2.5 to 3.0 of 5; decisions tracked to closure |
| [Data Protection and Privacy Assurance](https://github.com/HollaAB/ai-governance-portfolio/blob/main/data-protection-privacy-assurance/README.md) | Inventory, DPIAs, processors, retention, rights, breach plan | 5 of 6 data protection findings closed; breach plan proven |
| [AI Governance Framework](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/README.md) | AI inventory, risk tiers, chatbot assessment and testing | Chatbot leaks fixed; 96% test pass rate |
| [Security Risk and Incident Management](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/README.md) | Security risks, access review, incident response, continuity | Leavers and admin MFA fixed; exercise met the ODPC deadline |

## 3. The incident that tied them together

In the "Saturday Medal" exercise, a phished shared password led to the export of 1,850 members' contacts and fake payment requests. The ODPC was notified in about 50 hours, inside the 72-hour limit; members were warned in about 52 hours, outside the 24-hour target. The [requirements-to-controls mapping](https://github.com/HollaAB/ai-governance-portfolio/blob/main/integrated-grc-capstone/04-requirements-mapping/requirements-to-controls-mapping.csv) traces 16 requirements: 9 met, 2 partly met and 5 not met.

## 4. Cross-cutting findings

| Finding | Severity | Functions |
|---|---|---|
| IF-01 Shared accounts and missing MFA | High | Security; Compliance |
| IF-02 Supplier oversight stops at the contract | Medium | Compliance; Security |
| IF-03 No authority to warn members quickly | High | Governance; Compliance |
| IF-04 One awareness programme for data, security and AI | Medium | Security; Compliance; AI & Data Governance |
| IF-05 Recovery depends on supplier backups | Medium | Security; Governance |

## 5. Recommendations

1. Approve the integrated roadmap of 28 open actions ([roadmap](https://github.com/HollaAB/ai-governance-portfolio/blob/main/integrated-grc-capstone/05-findings-and-remediation/remediation-roadmap.md)).
2. Give the DPO authority to warn members within 24 hours of a breach with fraud risk.
3. Put incident support terms into every critical supplier contract.
4. Fund one combined awareness programme and the continuity fixes.
5. Keep the [portfolio dashboard](https://github.com/HollaAB/ai-governance-portfolio/blob/main/integrated-grc-capstone/06-dashboard/portfolio-dashboard.csv) as a standing Committee item.

## 6. What remains outside appetite

6 of 18 enterprise risks: R-01 personal data breach through cloud systems or supplier access; R-04 licence or permit lapses; R-05 bribery in procurement or member admission; R-06 fire or life-safety incident during a large event; R-07 food safety incident; R-17 conflicts of interest influence committee decisions on suppliers.
