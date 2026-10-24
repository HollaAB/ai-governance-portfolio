> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates and decisions are scenario results for the fictional Club.

| Item | Detail |
|---|---|
| System | Kijani Assist chatbot, versions 1.0 and 1.1 |
| Tier | High ([classification](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/04-classification/use-case-classification.csv)) |
| Owner | Membership and Events Manager |
| Assessed by | AI review group |
| Related | [DPIA-02](https://github.com/HollaAB/ai-governance-portfolio/blob/main/data-protection-privacy-assurance/04-dpia/dpia-02-kijani-assist.md) for personal data risks |
| Decision | Version 1.1 approved by the Management Committee, 9 December 2026 (D-2026-12-02) |

## 1. Intended use and limits

Kijani Assist answers questions about Club rules, events and facilities, books tee times, and shares a member's own balance after verification. It must not give legal, medical or financial advice, change membership status, process refunds, or discuss other members.

## 2. Who could be affected

Members (wrong answers, missed bookings, disclosure of their data), staff (handling complaints), and the Club (reputation, regulatory exposure).

## 3. Harms considered

| ID | Harm | Before measures (L x I) | Measure | After |
|---|---|---|---|---|
| AH-01 | Wrong answers about rules, dates or fees (hallucination) | 4 x 3 = 12 | Answers limited to an approved Club knowledge base, refreshed monthly; "I don't know, please contact reception" when no source | 2 x 3 = 6 |
| AH-02 | Balance shared after weak identity check | 3 x 4 = 12 | One-time PIN through the app (v1.1) | 1 x 4 = 4 |
| AH-03 | Crafted questions reveal other members' bookings | 3 x 4 = 12 | Look-ups limited to the verified member; adversarial tests | 1 x 4 = 4 |
| AH-04 | Poorer service in Swahili or Sheng | 4 x 2 = 8 | Swahili test set; human hand-off on low confidence; target 90% accuracy | 3 x 2 = 6 |
| AH-05 | Members unaware they are using AI | 4 x 2 = 8 | Disclosure in the first message | 1 x 2 = 2 |
| AH-06 | Vendor changes the model without notice | 3 x 3 = 9 | Contract: 30 days' notice of model changes; retest before switching | 2 x 3 = 6 |

## 4. Human oversight

Reception reviews every conversation the chatbot hands off, and a 5% random sample of all conversations each week. Staff can disable the chatbot within minutes from the Sauti AI Labs console. See the [oversight matrix](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/06-oversight/human-oversight-matrix.csv).

## 5. Testing

Tested with 150 prompts before and after the version 1.1 fixes: [test protocol](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/05-impact-assessment/ai-testing-protocol.md), [results](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/05-impact-assessment/test-results.csv). Version 1.1 met every target except Swahili accuracy (85% against 90%), which is tracked as finding AIF-02.

## 6. Conclusion

Version 1.0 should not have been launched without this assessment. Version 1.1 is acceptable with the measures above, a six-month review, and a retest after any model change.
