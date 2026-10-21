# Methodology: Security Risk and Incident Management

Draft 0.1, prepared for review by Abel Holla.

1. **Assets.** List the Club's information, system and physical assets and rate their criticality (1 to 5) in the [asset inventory](../03-security-assessment/asset-inventory.csv).
2. **Threats and vulnerabilities.** For each critical asset, identify plausible threats and weaknesses through interviews, a site walk and document review, in the [threat and vulnerability assessment](../03-security-assessment/threat-vulnerability-assessment.csv).
3. **Risk.** Score each security risk (likelihood x impact, 1 to 25, the same scale as Stage 2) and set a treatment in the [security risk register](../03-security-assessment/security-risk-register.csv).
4. **Site survey.** Walk the gates, perimeter, clubhouse, stores and car parks against a checklist ([site security survey](../03-security-assessment/site-security-survey.md)).
5. **Access.** Set a role access matrix, then review a sample of user accounts against it and against HR leaver records.
6. **People.** Run an authorised phishing simulation for office staff.
7. **Incidents.** Write the response plan, severity matrix and playbooks, then test them in a tabletop exercise and record the chronology and timings.
8. **Continuity.** Run a business impact analysis, set recovery time and recovery point objectives, and test recovery of the most critical services.
9. **Report.** Record findings with corrective actions and report to the Security and Safety sub-committee.

## Reference frameworks

ISO 31000:2018 for risk assessment; the NIST Cybersecurity Framework 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover) for structure; ISO 22301:2019 concepts for business continuity. No certification is implied.

## Rule

No live systems were scanned or tested. Real security configurations, network details and vulnerabilities must never be published.
