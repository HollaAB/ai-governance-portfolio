> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates, accounts and events are scenario results for the fictional Club. No real systems, configurations or vulnerabilities are described.

**To:** Security and Safety sub-committee, Kijani Heights Golf and Country Club
**From:** ICT Officer and Head of Security
**Period:** January 2027

## 1. Summary

A security assessment of 14 assets, a review of 24 accounts, a phishing simulation, a tabletop exercise and four recovery tests found 10 weaknesses (2 High, 6 Medium, 2 Low). The two High findings (leaver accounts and admin accounts without MFA) were fixed within a week. The exercise showed the Club can meet the 72-hour ODPC deadline but warns members too slowly when fraud follows a breach.

## 2. Measures

| Measure | Result |
|---|---|
| Accounts appropriate | 58% (14 of 24, January 2027) |
| Leaver accounts disabled on time | 0% before January 2027 (4 late) |
| Admin accounts with MFA | 100% after SF-02 (was 75%, 6 of 8) |
| Phishing click rate | 23% (9 of 40) |
| Phishing report rate | 15% (6 of 40) |
| Recovery tests met | 50% (2 of 4) |
| Security findings overdue | 0% |

## 3. Highest security risks

| Risk | Score | Treatment |
|---|---|---|
| SR-01 Account takeover through phishing | 20 (Critical) | Reduce: individual accounts, MFA, awareness training |
| SR-02 Unauthorised access by former staff | 16 (High) | Reduce: same-day leaver process, quarterly access review |
| SR-03 FairwayOne outage or breach | 15 (High) | Reduce: weekend contact, restore tests, manual fallback |
| SR-04 Supplier admin account misuse | 15 (High) | Reduce: MFA for all admin accounts, logging |
| SR-05 Point-of-sale fraud | 9 (Medium) | Reduce: remove cashier refund rights |

Full register: [security-risk-register.csv](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/03-security-assessment/security-risk-register.csv).

## 4. Tabletop exercise

ODPC notification in about 50 hours (target 72, met); member warning in about 52 hours (target 24, not met); FairwayOne not reachable at the weekend. See the [exercise report](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/06-tabletop-exercise/tabletop-exercise-report.md).

## 5. Decisions requested

1. Approve the [access control policy](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/04-access-review/access-control-policy.md), [incident response plan](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/05-incident-response/incident-response-plan.md) and [continuity plan](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/07-continuity/continuity-and-recovery-plan.md).
2. Approve spending on a spare CCTV recorder and fuel store camera and lighting (scenario estimate KES 650,000).
3. Decide whether to accept nightly backups (SF-05) or pay FairwayOne for more frequent backups.
