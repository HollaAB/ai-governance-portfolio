# Tabletop Exercise Report: "Saturday Medal"

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates, accounts and events are scenario results for the fictional Club. No real systems, configurations or vulnerabilities are described.

## Summary

The team would have met the 72-hour ODPC deadline (about 50 hours) but would have warned members only after about 52 hours, while fraudsters were already contacting them. The attack itself succeeded because of a shared password without multi-factor authentication. The exercise confirmed three weaknesses already seen in the access review and found two new ones.

## Timings against targets

| Measure | Target | Exercise result | Met? |
|---|---|---|---|
| Time from compromise to detection | Under 1 hour | 3 hours 50 minutes (by a member) | No |
| Time from awareness to containment | Under 2 hours | 45 minutes | Yes |
| Time from awareness to ODPC notification | Under 72 hours | About 50 hours | Yes |
| Time from awareness to member warning (fraud risk) | Under 24 hours | About 52 hours | No |
| Supplier reached out of hours | Within 2 hours | Not reached until Monday | No |

## What went well

- Containment was quick once the ICT support firm was called.
- The DPO's assessment followed the breach response plan and recorded the reasoning.
- The Chairman was told within 2 hours of awareness.

## What needs to improve

| Gap | Finding | Action |
|---|---|---|
| Shared reception login with no MFA | SF-03 | Named accounts with MFA |
| No alert for a large export | SF-04 | Ask FairwayOne for export alerts |
| No weekend contact for FairwayOne | SF-04 | Out-of-hours line in the contract and contact list |
| No member warning template; decision deferred | SF-09 | Pre-approved fraud warning, sent within 24 hours on the DPO's call |
| Staff fall for phishing | SF-08 | Awareness training and repeat simulation |

## Next exercise

July 2027: a ransomware scenario affecting the point-of-sale system.

Full timeline: [incident-chronology.csv](incident-chronology.csv).
