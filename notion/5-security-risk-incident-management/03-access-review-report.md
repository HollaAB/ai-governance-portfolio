> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates, accounts and events are scenario results for the fictional Club. No real systems, configurations or vulnerabilities are described.

**Systems:** FairwayOne, point of sale, email, payroll portal, CCTV recorder, Kijani Assist console
**Date:** 13 to 14 January 2027
**Reviewers:** ICT Officer and system owners, checked by the Compliance Officer

## Method

All 24 accounts with elevated or member-data access were compared with the [role access matrix](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/04-access-review/role-access-matrix.csv) and the HR leaver list. Results are in [access-review.csv](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/04-access-review/access-review.csv).

## Results

| Measure | Result |
|---|---|
| Accounts reviewed | 24 |
| Appropriate | 14 (58%) |
| Leaver accounts still active | 4 |
| Active accounts without MFA where required | 4 |
| Shared accounts | 2 (reception in FairwayOne and in the Kijani Assist console) |
| Excess rights | 2 (cashier refunds, guard supervisor export) |

## Actions taken

- All 4 leaver accounts disabled on 14 January 2027, including one with billing admin rights (SF-01).
- The ICT support firm's generic admin accounts to be replaced by named accounts with MFA within 7 days (SF-02).
- Shared reception logins to be replaced by named accounts by 28 February 2027 (SF-03).
- Excess rights removed on the day.

## Conclusion

Only 58% of accounts were appropriate. The leaver process failed because HR did not tell the ICT Officer when people left; the [access control policy](https://github.com/HollaAB/ai-governance-portfolio/blob/main/security-risk-incident-management/04-access-review/access-control-policy.md) now makes this a same-day step.
