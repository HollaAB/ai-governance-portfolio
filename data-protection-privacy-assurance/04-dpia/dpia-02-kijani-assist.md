# DPIA-02: Kijani Assist Chatbot

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

All results, dates and decisions are scenario results for the fictional Club.

| Item | Detail |
|---|---|
| Activity | PA-04 Kijani Assist chatbot |
| Owner | Membership and Events Manager |
| Assessor | Compliance Officer (DPO), with the ICT Officer |
| Date | November 2026 |
| Decision | Version 1.1 approved by the Management Committee, 9 December 2026 (D-2026-12-02) |

This DPIA covers the personal data risks. The wider AI risks (accuracy, language, misuse, oversight) are in the [AI impact assessment](../../ai-governance-framework/05-impact-assessment/ai-impact-assessment-kijani-assist.md).

## 1. Description

Kijani Assist runs on WhatsApp and the member app. It answers questions about Club rules and events, books tee times and, after identity checks, shares a member's account balance. Sauti AI Labs runs the service; it sends the text of each question to ModelCo's language model, hosted outside Kenya, to draft answers.

## 2. Necessity and proportionality

| Question | Assessment |
|---|---|
| Purpose | Faster answers and bookings for members, at any hour. |
| Less intrusive options | Members can still call or visit reception. Account balances are also in the app. |
| Data minimisation | ModelCo receives question text only. Account data is fetched by Sauti AI Labs from FairwayOne and added to the answer after the model responds, so it never reaches ModelCo. |
| Retention | Conversation logs kept 90 days for quality checks (RS-04). |
| Lawful basis | Contract: the service is part of membership. |
| Transfers | Question text goes to ModelCo outside Kenya under Sauti AI Labs' agreement; see the [transfer assessment](../05-processors/cross-border-transfer-assessment.md). |

## 3. Risks

| ID | Risk to individuals | Likelihood | Impact | Score before measures |
|---|---|---|---|---|
| DR-06 | Account balance shared with someone who is not the member | 3 | 4 | 12 |
| DR-07 | Another member's booking or details disclosed through a crafted question | 3 | 4 | 12 |
| DR-08 | Members type sensitive information (for example health) into the chat | 3 | 3 | 9 |
| DR-09 | Prompts used by the vendor or model provider to train models | 2 | 3 | 6 |
| DR-10 | Members do not know they are talking to an AI or how data is used | 4 | 2 | 8 |

## 4. Measures

| Risk | Measure | Owner |
|---|---|---|
| DR-06 | One-time PIN sent through the app before any balance is shared (version 1.1) | ICT Officer |
| DR-07 | The chatbot can only look up the verified member's own records; tested against 20 crafted attacks | ICT Officer |
| DR-08 | Warning in the first message not to share sensitive information; logs scanned and redacted weekly | Membership and Events Manager |
| DR-09 | Contract terms: no training on Club data by Sauti AI Labs or ModelCo; prompts deleted by ModelCo within 30 days | Compliance Officer (DPO) |
| DR-10 | First message says "You are chatting with Kijani Assist, an automated assistant" and links to the privacy notice | Membership and Events Manager |

## 5. Residual risk

| ID | Score after measures | Rating |
|---|---|---|
| DR-06 | 4 | Low |
| DR-07 | 4 | Low |
| DR-08 | 6 | Medium |
| DR-09 | 3 | Low |
| DR-10 | 2 | Low |

## 6. DPO opinion

Version 1.0 should not have gone live without this assessment; its identity check was too weak. Version 1.1 can continue with the measures above. Test results are in the [AI testing results](../../ai-governance-framework/05-impact-assessment/test-results.csv).

## 7. Decision

Approved by the Management Committee on 9 December 2026 (D-2026-12-02), with a review after six months.
