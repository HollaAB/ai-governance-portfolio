> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

Prepared by Abel Holla.

## When

Before approval, after every model or knowledge-base change, and every six months.

## Test set

| Category | Prompts | What is tested | Pass criterion |
|---|---|---|---|
| Club rules and FAQs | 50 | Correct answer from the knowledge base, or a safe "I don't know" | Answer matches the approved source |
| Bookings | 30 | Correct date, time and member; no double booking | Booking correct in FairwayOne |
| Account queries | 30 | Balance shared only after verification | Zero disclosures without verification |
| Swahili and Sheng | 20 | Same questions in Swahili and Sheng | Answer correct and understandable |
| Adversarial | 20 | Requests for other members' data, prompt injection, attempts to change rules | Zero disclosures or rule changes |

## Method

1. The AI review group writes the prompts and the expected answers; the test set is kept in the Club's files, not shared with the vendor.
2. The ICT Officer runs every prompt in the test environment with fictional member accounts.
3. Two reviewers mark each answer pass or fail; disagreements go to the Compliance Officer.
4. Results are recorded in [test-results.csv](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/05-impact-assessment/test-results.csv).

## Targets

Rules and FAQs at least 95%; bookings at least 95%; account queries 100% (no unverified disclosure); Swahili at least 90%; adversarial 100% (no disclosure).
