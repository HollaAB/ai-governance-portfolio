**Project status:** Completed

**Project type:** Assessment

**Domain:** Security

**Date:** October 2026

**Author:** Abel Holla

## 1. Executive Summary

Kijani Heights Golf and Country Club, a fictional Kenyan members' club, rated a personal data breach through cloud systems or supplier access as its highest risk, but had never reviewed who could access its systems or tested its response and recovery. I assessed security risk across the Club's sites and systems, reviewed 24 accounts against a role access matrix, and ran an authorised phishing simulation for 40 office staff. An incident response plan and three playbooks were then tested in the "Saturday Medal" tabletop exercise, and four recovery tests checked the continuity plan. The Club met the 72-hour deadline for notifying the Data Protection Commissioner but warned members only after about 52 hours, and only 14 of 24 accounts were appropriate (scenario results). Both High findings were fixed within a week.

## 2. The Problem

**Problem statement:** Access to the Club's systems had never been reviewed, and incident response and recovery had never been tested.

**Why it matters:** The Club's member data sits in cloud systems that staff and suppliers can reach. A single phished password could expose 1,850 members to fraud, and the law gives the Club 72 hours to notify the regulator. Untested plans usually fail at the first real incident.

## 3. Objectives

The project aims to:

- Rate the Club's assets, threats and security risks on the same scale as the enterprise risk register.
- Check that every account with access to member data or admin rights is appropriate.
- Write an incident response plan and playbooks, and test them against the legal deadlines.
- Set recovery objectives for critical processes and test recovery.

## 4. Scope and Assumptions

**Included:** Asset inventory, threat and vulnerability assessment, security risk register and site security survey; access control policy, role access matrix, access review and phishing simulation; incident response plan, severity matrix, playbooks and chain-of-custody form; tabletop exercise; business impact analysis, continuity plan and recovery tests.

**Excluded:** Technical testing of any real system. No live system was scanned, and no real configurations, network details or vulnerabilities are published.

**Assumptions and limitations:** The Club, its accounts, staff, suppliers and incidents are fictional. Descriptions of systems and sites are general. The case study organisation is described here:

[Replace this line: type /link to page and choose Case Study Organisation]

## 5. Methodology

**My approach:**

1. Listed and rated 14 information, system and physical assets, assessed 11 threats, and scored each security risk from 1 to 25.
2. Walked the gates, perimeter, clubhouse, stores and car parks against a site survey checklist.
3. Set a role access matrix, reviewed 24 privileged and member-data accounts against it and the HR leaver list, and ran an authorised phishing simulation.
4. Wrote the incident response plan, severity matrix and playbooks, then tested them in a tabletop exercise with a timed chronology.
5. Ran a business impact analysis for 7 processes, set recovery objectives and tested recovery four times.

**Standards, frameworks, or references used:** ISO 31000:2018 for risk assessment; NIST Cybersecurity Framework 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) for structure; ISO 22301:2019 concepts for business continuity; Data Protection Act 2019 (72-hour breach notification).

## 6. Deliverables

The project produces:

- Asset inventory (14 assets), threat and vulnerability assessment (11 threats), security risk register (11 risks) and site security survey
- Access control policy, role access matrix, access review (24 accounts) and report, phishing simulation results
- Incident response plan, severity matrix, three playbooks and a chain-of-custody form
- "Saturday Medal" tabletop scenario, incident chronology and exercise report
- Business impact analysis (7 processes), continuity and recovery plan, recovery test results
- Findings register (10 findings), corrective-action tracker, KPIs, security management report and executive summary

Full documents:

[Replace this line: /page Site Security Survey]

[Replace this line: /page Access Control Policy]

[Replace this line: /page Access Review Report]

[Replace this line: /page Incident Response Plan]

[Replace this line: /page Incident Playbooks]

[Replace this line: /page Tabletop Exercise]

[Replace this line: /page Continuity Plan]

[Replace this line: /page Registers]

[Replace this line: /page Security Report]

[Replace this line: /page Executive Summary]

Links: [all files on GitHub](https://github.com/HollaAB/ai-governance-portfolio/tree/main/security-risk-incident-management)

## 7. Testing Results or Evaluation Criteria

All results are scenario results.

- **Access review:** 14 of 24 accounts appropriate (58%); 4 leaver accounts still active, one with billing admin rights; 2 supplier admin accounts without multi-factor authentication.
- **Phishing simulation:** 9 of 40 staff clicked (23%), 4 entered a password, and 6 reported the email.
- **Tabletop exercise:** the Data Protection Commissioner was notified at about 50 hours (target 72, met); members were warned at about 52 hours (target 24, not met).
- **Recovery tests:** 2 of 4 met their targets. Restoring member data took 5 hours with data 22 hours old; the CCTV cameras were off for 9 hours because there was no spare recorder.
- **Findings:** 10 (2 High, 6 Medium, 2 Low); both High fixed within a week.

## 8. Key Findings or Design Decisions

**Finding 1: One weakness, found twice.** The access review and the exercise found the same root cause: a shared reception password without multi-factor authentication. Named accounts with MFA fix both.

**Finding 2: The slowest step was a decision, not a fix.** The technical response was quick, but warning members waited two days because nobody had the authority to send the warning. A pre-approved warning that the DPO can send fixes this.

**Finding 3: Recovery depends on suppliers.** Nightly backups by the club management system supplier mean up to 24 hours of bookings and billing could be lost, against a target of 1 to 4 hours. The Club must ask for more frequent backups or formally accept the risk.

## 9. Practical Recommendations

| Recommendation | Rationale | Priority |
|---|---|---|
| Replace shared reception logins with named accounts and MFA | The phishing exercise succeeded through a shared password | High |
| Pre-approve a member fraud warning that the DPO can send within 24 hours | Members were warned after about 52 hours while fraud continued | High |
| Agree export alerts and an out-of-hours contact with FairwayOne | The supplier gave no alert on a large export and had no weekend contact | Medium |
| Run awareness training for all office staff and repeat the simulation in 6 months | 23% of staff clicked and 4 entered a password | Medium |
| Buy a spare CCTV recorder and cover the fuel store and staff car park | Cameras were off for 9 hours in a recovery test; the fuel store has no camera | Medium |

## 10. Implementation Roadmap

- **Within a week (ICT Officer):** disable leaver accounts and give supplier admins named accounts with MFA. Done in the scenario in January 2027.
- **By February 2027 (ICT Officer, Membership and Events Manager):** named reception accounts; pre-approved member warning.
- **By March 2027 (Compliance Officer, ICT Officer):** supplier alerts and out-of-hours contact; backup frequency decision.
- **By April 2027 (HR Manager, Head of Security):** awareness training, spare recorder, fuel store camera and lighting.
- **By May 2027 (Head of Security):** complete the key register and rekey the cash office.

## 11. Skills Demonstrated

- **Security risk assessment:** assets, threats and risks across physical and information security.
- **Access control:** a role access matrix and an access review against HR records.
- **Incident response:** a plan, playbooks and evidence handling tested against legal deadlines.
- **Business continuity:** a business impact analysis with recovery objectives measured by real tests.

## 12. Lessons Learned

The exercise and the access review pointed to the same root cause, which shows the value of testing the same risk in two ways. The slowest step in the incident was a communication decision, not a technical fix, so governance matters as much as technology. A real assessment would add authorised technical testing by a qualified provider.

## 13. Next Steps

- Close the eight open actions by May 2027.
- Repeat the phishing simulation and the access review in six months.
- Carry the cross-cutting weaknesses into the integrated capstone roadmap.

## 14. Evidence & Transparency

**My contribution:** Planned and produced the project end to end: scope, method, registers, assessments, findings, recommendations and reporting.

**Tools used:** Markdown and CSV files on GitHub, Mermaid diagrams, Google Sheets, Notion.

**Sources:** ISO 31000:2018; NIST Cybersecurity Framework 2.0; ISO 22301:2019; Data Protection Act 2019.

**GitHub evidence:** [View the evidence on GitHub](https://github.com/HollaAB/ai-governance-portfolio/tree/main/security-risk-incident-management)

**Limitations:** The Club, its accounts, staff, suppliers and incidents are invented. No real system was scanned or tested; the phishing simulation and exercise are described scenarios. Scores, timings and test results are scenario results.

**Confidentiality:** The published material uses a fictional organisation and contains no real security configurations, network details, vulnerabilities or incident records.

## 15. Documents in this Project

- [Project charter](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/01-project-charter/project-charter.md)
- [Version history](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/01-project-charter/version-history.md)
- [Assumptions register](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/01-project-charter/assumptions-register.csv)
- [Methodology](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/02-methodology/methodology.md)
- [Evidence index](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/evidence-index.csv)
- [Findings register](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/08-findings-and-actions/findings-register.csv)
- [Corrective-action tracker](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/08-findings-and-actions/corrective-action-tracker.csv)
- [KPI definitions](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/09-reporting/kpi-definitions.csv)
- [Executive summary](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/09-reporting/executive-summary.md)
- [README](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/README.md)
- [Limitations statement](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/limitations.md)

This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.
