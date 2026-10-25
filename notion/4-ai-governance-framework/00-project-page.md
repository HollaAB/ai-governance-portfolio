**Project status:** Completed

**Project type:** Framework

**Domain:** Governance; AI & Data Governance

**Date:** October 2026

**Author:** Abel Holla

## 1. Executive Summary

Kijani Heights Golf and Country Club, a fictional Kenyan members' club, launched an AI chatbot (Kijani Assist) and number-plate recognition with no AI governance: nobody had listed its AI systems, judged their risk or tested them. I set up an AI governance framework with a charter and a lifecycle from proposal to retirement, inventoried and classified seven AI systems, and assessed the chatbot against six harms. The chatbot was tested with 150 prompts before and after fixes: version 1.0 leaked account data in identity and adversarial tests, and version 1.1 passed all of them with 96% overall accuracy (scenario results). The Committee approved version 1.1 and opt-in number-plate recognition, and a vendor CV screening tool was rejected.

## 2. The Problem

**Problem statement:** The Club used AI in member-facing and security services without an inventory, risk classification, testing, human oversight or rules for staff use of generative AI.

**Why it matters:** The chatbot shares account balances and books tee times for members, and number-plate recognition decides who enters the Club. Wrong or leaked answers harm members directly, and the Club relies on a vendor model it cannot inspect.

## 3. Objectives

The project aims to:

- List every AI system the Club uses or plans to use.
- Classify each system by risk and set the approval level for each tier.
- Assess and test high-risk systems before approval and after every significant change.
- Name the person who oversees or can override each system.
- Check AI vendors and record model changes and AI incidents.

## 4. Scope and Assumptions

**Included:** AI governance charter and lifecycle; staff acceptable-use policy for generative AI; AI system inventory and classification; impact assessment and testing of Kijani Assist; human oversight matrix; vendor due diligence; model change and incident registers; findings, KPIs and reporting.

**Excluded:** Personal data assessments, which sit in the Data Protection and Privacy Assurance project; technical testing of the vendor's model internals.

**Assumptions and limitations:** The Club, Sauti AI Labs, ModelCo, test results and incidents are fictional. The 150-prompt test set is described, not published. The case study organisation is described here:

[Replace this line: type /link to page and choose Case Study Organisation]

## 5. Methodology

**My approach:**

1. Asked every department and supplier which tools use AI, including features inside vendor software, and recorded them in an inventory.
2. Scored each use case on six criteria (rights, personal data, autonomy, member-facing, generative, vendor model) to set its tier: Low, Medium, High or not permitted.
3. Completed an impact assessment for the chatbot alongside its DPIA, with harms scored before and after measures.
4. Wrote a test protocol with targets per category and ran it before and after the vendor's fixes.
5. Named an owner and a human reviewer for each system, scored the vendor, and set up change and incident registers with quarterly reporting.

**Standards, frameworks, or references used:** NIST AI Risk Management Framework 1.0 (Govern, Map, Measure, Manage); ISO/IEC 42001:2023 management system approach; Kenya's National AI Strategy 2025 to 2030; Data Protection Act 2019, including s.35 on automated decisions.

## 6. Deliverables

The project produces:

- AI governance charter with a lifecycle diagram, and a staff acceptable-use policy
- AI system inventory (7 systems) and risk classification method with results
- Impact assessment of Kijani Assist (6 harms), testing protocol and test results
- Human oversight and accountability matrix
- Vendor AI due-diligence checklist, model change register and AI incident register
- Findings register (5 findings), corrective-action tracker, KPIs, committee report and executive summary

Full documents:

[Replace this line: /page AI Governance Charter]

[Replace this line: /page Acceptable-Use Policy]

[Replace this line: /page Classification Method]

[Replace this line: /page Impact Assessment: Kijani Assist]

[Replace this line: /page Testing Protocol]

[Replace this line: /page Registers]

[Replace this line: /page Committee Report]

[Replace this line: /page Executive Summary]

Links: [all files on GitHub](https://github.com/HollaAB/ai-governance-portfolio/tree/main/ai-governance-framework)

## 7. Testing Results or Evaluation Criteria

Kijani Assist was tested with 150 prompts in five categories, before and after fixes. All results are scenario results.

| Category | Prompts | Version 1.0 | Version 1.1 | Target |
|---|---|---|---|---|
| Club rules and FAQs | 50 | 88% | 96% | 95% |
| Bookings | 30 | 93% | 97% | 95% |
| Account queries (no unverified disclosure) | 30 | 90% | 100% | 100% |
| Swahili and Sheng | 20 | 75% | 85% | 90% |
| Adversarial (no disclosure) | 20 | 90% | 100% | 100% |

Version 1.1 passed 144 of 150 prompts (96%) and met four of five targets. Swahili and Sheng accuracy is still below target. The vendor, Sauti AI Labs, scored 35 of 45 in due diligence.

## 8. Key Findings or Design Decisions

**Finding 1: Testing changed the decision.** Version 1.0 shared balances after weak identity checks in 3 of 30 tests and revealed other members' data in 2 of 20 adversarial tests. A one-time PIN and limited look-ups fixed both, and the retest gave the Committee hard evidence to approve version 1.1.

**Decision 2: Reject a risky tool early.** A vendor CV screening tool would rank job applicants with no practical human review. The classification method marks such use as not permitted, so it was rejected before any data was shared.

**Decision 3: Keep a human in control of every system.** The oversight matrix names, for each system, who reviews outputs and who can override them; for example, a guard handles every number-plate non-match.

## 9. Practical Recommendations

| Recommendation | Rationale | Priority |
|---|---|---|
| Approve the AI governance charter, Kijani Assist version 1.1 and opt-in number-plate recognition | Both systems are assessed, tested and controlled | High |
| Add Swahili content, hand off to staff on low confidence, and retest by March 2027 | Swahili and Sheng accuracy is 85% against a 90% target | Medium |
| Obtain the vendor's ISO/IEC 27001 certificate or an independent security report by February 2027 | The vendor claims certification but has not provided evidence | Medium |
| Brief all office staff on the acceptable-use policy | Staff use public AI tools without guidance | Low |

## 10. Implementation Roadmap

- **December 2026 (Management Committee):** charter, acceptable-use policy, Kijani Assist version 1.1 and opt-in number-plate recognition approved. Done in the scenario.
- **By February 2027 (Compliance Officer):** vendor security certificate or report.
- **By March 2027 (Membership and Events Manager, HR Manager):** Swahili improvements and retest; staff briefing on the acceptable-use policy.
- **June 2027 (AI review group):** review Kijani Assist; retest after any model change.

## 11. Skills Demonstrated

- **AI risk classification:** an inventory and a six-criterion method that sets approval levels.
- **AI impact assessment:** harms scored before and after measures.
- **Testing and validation:** a written protocol with targets, run before and after fixes.
- **Third-party AI risk:** vendor due diligence, contract terms on model changes, and a change register.

## 12. Lessons Learned

Testing before and after fixes turned opinion into evidence: the chatbot looked fine until structured tests showed it leaked data. A clear classification method made it easy to reject a risky vendor tool early. A real test set would be larger and refreshed regularly, and a real club would also need the vendor's own security evidence.

## 13. Next Steps

- Close the three open actions by March 2027.
- Retest Kijani Assist after any model change and at the June 2027 review.
- Report AI KPIs to the Committee each quarter.

## 14. Evidence & Transparency

**My contribution:** Planned and produced the project end to end: scope, method, registers, assessments, findings, recommendations and reporting.

**Tools used:** Markdown and CSV files on GitHub, Mermaid diagrams, Google Sheets, Notion.

**Sources:** NIST AI RMF 1.0; ISO/IEC 42001:2023; Kenya's National AI Strategy 2025 to 2030; Data Protection Act 2019.

**GitHub evidence:** [View the evidence on GitHub](https://github.com/HollaAB/ai-governance-portfolio/tree/main/ai-governance-framework)

**Limitations:** The Club, vendor, model provider, test results and incidents are invented. Testing covers the chatbot's behaviour, not the vendor's model internals. NIST AI RMF and ISO/IEC 42001 are used as structure only.

**Confidentiality:** The published material uses a fictional organisation and contains no restricted or identifying information.

## 15. Documents in this Project

- [Project charter](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/01-project-charter/project-charter.md)
- [Version history](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/01-project-charter/version-history.md)
- [Assumptions register](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/01-project-charter/assumptions-register.csv)
- [Methodology](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/02-methodology/methodology.md)
- [Evidence index](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/evidence-index.csv)
- [Findings register](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/09-findings-and-actions/findings-register.csv)
- [Corrective-action tracker](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/09-findings-and-actions/corrective-action-tracker.csv)
- [KPI definitions](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/10-reporting/kpi-definitions.csv)
- [Executive summary](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/10-reporting/executive-summary.md)
- [README](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/README.md)
- [Limitations statement](https://github.com/HollaAB/ai-governance-portfolio/blob/main/ai-governance-framework/limitations.md)

This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.
