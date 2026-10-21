# Integrated Case Study: "Saturday Medal"

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates and decisions are scenario results for the fictional Club.

## The scenario

Kijani Heights Golf and Country Club uses a cloud club management system hosted in South Africa, shares data with suppliers, and runs an AI chatbot and number-plate recognition. On a competition Saturday, a receptionist enters the shared reception password on a phishing page. An attacker exports the contact details of about 1,850 members, and members start receiving fake requests to pay subscriptions to a new paybill. The incident was run as a [tabletop exercise](../../security-risk-incident-management/06-tabletop-exercise/tabletop-exercise-report.md) on 20 January 2027.

## Timeline

| Time | What happened | Function |
|---|---|---|
| Sat 07:40 | Shared reception password entered on a phishing page | Security |
| Sat 09:10 | Member list exported from FairwayOne; no alert | Security, supplier |
| Sat 11:30 | First member reports a fake paybill SMS | Detection by a member |
| Sat 12:45 | DPO told; 72-hour clock starts | Compliance |
| Sat 13:30 | Password reset, sessions ended | Security |
| Sat 13:45 | FairwayOne cannot be reached at the weekend | Supplier oversight |
| Sat 14:00 | Chairman told | Governance |
| Sat 16:00 | Member warning deferred: no template and no clear authority | Governance |
| Mon 11:00 | Breach assessed as notifiable | Compliance |
| Mon 15:00 | ODPC notified (about 50 hours) | Compliance |
| Mon 17:00 | Members warned (about 52 hours) | Governance, compliance |

Full chronology: [incident-chronology.csv](../../security-risk-incident-management/06-tabletop-exercise/incident-chronology.csv).

## Compliance workstream

**Obligations triggered:** breach notification to the ODPC within 72 hours and to affected people without undue delay (OB-05); processor contracts (OB-07); security of personal data; transfers outside Kenya (OB-08).

**Position:** the [breach response plan](../../data-protection-privacy-assurance/08-breach-response/breach-response-plan.md) from Stage 4 worked: the ODPC deadline was met. The processor agreement with FairwayOne was in place, but it did not require export alerts or an out-of-hours contact. The member warning was too slow for a fraud risk.

## Governance workstream

**Accountability:** the [delegation of authority](../../enterprise-governance-risk-dashboard/03-governance-framework/delegation-of-authority.csv) from Stage 3 did not say who may warn members after a breach, so the decision waited for Monday. The [escalation matrix](../../enterprise-governance-risk-dashboard/04-accountability/escalation-matrix.csv) worked: the Chairman was told within about an hour of the DPO.

**Oversight:** the incident is reported to the Committee in the [integrated committee paper](../06-dashboard/committee-paper.md) with the [portfolio dashboard](../06-dashboard/portfolio-dashboard.csv).

## Security workstream

**Risks:** account takeover through phishing (SR-01, score 20) and supplier breach (SR-03) in the [security risk register](../../security-risk-incident-management/03-security-assessment/security-risk-register.csv).

**Position:** the [access review](../../security-risk-incident-management/04-access-review/access-review-report.md) had already found the shared login; the exercise showed its consequence. Containment was fast once the ICT support firm was called. Detection relied on members.

## Data and AI

Kijani Assist was not involved, and its version 1.1 controls (one-time PIN, look-ups limited to the verified member) would have stopped the attacker using the chatbot to reach account data. This shows the value of the Stage 4 testing.

## Evidence trail

See [evidence-trail.md](evidence-trail.md) for how the documents in the five projects connect.
