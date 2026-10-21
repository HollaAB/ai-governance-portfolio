# Gap Assessment Methodology

> **Portfolio project.** This is an independent learning project using a fictional organisation and illustrative data. It is not an audit, legal opinion, or certification.

Draft 0.2, prepared for review by Abel Holla.

## Scope

All 36 applicable obligations in the [obligations register](../03-obligations-register/compliance-register.csv) and the 22 controls in the [controls matrix](../03-obligations-register/obligations-to-controls-matrix.csv). Fieldwork: 12 to 23 October 2026 (scenario dates).

## Approach

1. **Prepare.** For each obligation, write the requirement and the test step in the [requirements checklist](requirements-checklist.csv). Send the [evidence request list](evidence-request-list.csv) to owners five working days before fieldwork.
2. **Interview.** Meet each owner using the [interview questionnaire](interview-questionnaire.md).
3. **Test.** For each control, inspect the evidence, take a sample where there is a population (files, messages, certificates, months of filings), and record the result in the [testing workpapers](testing-workpapers.csv).
4. **Rate.** Give each control a result and each obligation a status (scales below).
5. **Report.** Record each exception as a finding in the [findings register](../06-remediation/findings-register.csv), agree a corrective action with the owner, and summarise in the [management report](../07-reporting/management-report.md).
6. **Follow up.** Retest each action after its due date and record closure in the [corrective-action tracker](../06-remediation/corrective-action-tracker.csv).

## Sampling

| Population size | Sample |
|---|---|
| 1 to 5 items | All items |
| 6 to 50 | At least 10, or all if fewer |
| More than 50 | 25 items, selected at random |

## Control results

| Result | Meaning |
|---|---|
| Tested and effective | Evidence shows the control works for the whole sample |
| Tested with exceptions | The control exists but failed for part of the sample |
| Not implemented | The control does not exist |

## Obligation status

| Status | Meaning |
|---|---|
| Compliant | All controls for the obligation are tested and effective |
| Partly compliant | At least one control has exceptions, but the obligation is mostly met |
| Not compliant | The obligation is not met, or its control is not implemented |
| Not applicable | The obligation does not apply to the Club |

## Finding severity

| Severity | Meaning | Action due |
|---|---|---|
| High | Likely penalty, harm to people, or loss of a licence | Within 30 days |
| Medium | Partial breach or weak control with limited immediate impact | Within 90 days |
| Low | Documentation or process gap with little direct impact | Within 180 days |

## Risk scoring (used in the risk and control register)

Score = likelihood (1 to 5) x impact (1 to 5).

| Score | Rating |
|---|---|
| 1 to 4 | Low |
| 5 to 9 | Medium |
| 10 to 16 | High |
| 20 to 25 | Critical |
