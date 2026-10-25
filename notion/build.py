"""Build the paste-ready Notion subpage files from the project documents.

Run from the repository root after any project document changes:

    python3 notion/build.py

Each subpage file is the source document with its first heading removed (the
Notion page title replaces it) and every relative link turned into a full
GitHub link, because relative links do not work once pasted into Notion.
The 00-project-page.md files are written by hand and are not touched.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "notion")
GITHUB = "https://github.com/HollaAB/ai-governance-portfolio"
LABEL = "> **Portfolio project.**"

# Share links of the Google Sheets built so far; add each new sheet when it exists.
SHEETS = {
    "Scenario Assumptions": "https://docs.google.com/spreadsheets/d/1EDWdZJCT_bpGn-bPAAUf_3yXC1zwogaKbJT26HELL24/edit?usp=sharing",
    "Compliance Register": "https://docs.google.com/spreadsheets/d/1tzT1RGcLlqHepqQ1ULwBknp7fVk33E_-d9_jNzCFAjI/edit?usp=sharing",
    "Risk and Control Register": "https://docs.google.com/spreadsheets/d/1_9c-IGjCLbFHAOw7-p3wI2s1UeyEEzG0UUB396VboA8/edit?usp=sharing",
    "Governance Registers": "https://docs.google.com/spreadsheets/d/1prfa91EFsgP97aQs0rnhaqysLOVxt9SBWpS1QKpl1eA/edit?usp=sharing",
    "Governance Dashboard": "https://docs.google.com/spreadsheets/d/1WdWOBQaNvYuPVBOwzLxsbHAFZ01MXY0msRdhnJ_AuzQ/edit?usp=sharing",
    "Data Protection Registers": "https://docs.google.com/spreadsheets/d/1xvSJqwO70hrNuU17q9cTIVuVynfDOQkJpjpIOjFVN6s/edit?usp=sharing",
    "AI Registers": "https://docs.google.com/spreadsheets/d/10NqLBDhwQJyzEpQieYNtJJ7SAKmWJNhL2XUsC8JNSAM/edit?usp=sharing",
}

# Each subpage: (file name, list of parts). A part is a source path, or
# ("text", line) for a line written as is, or ("embed", sheet name).
PROJECTS = {
    "1-compliance-management-system": [
        ("01-project-charter.md", ["compliance-management-system/01-project-charter/project-charter.md"]),
        ("02-methodology.md", ["compliance-management-system/02-methodology/methodology.md"]),
        ("03-obligations-register.md", [
            ("text", "The Club's obligations, controls, calendar and evidence."),
            ("embed", "Compliance Register"),
            "compliance-management-system/03-obligations-register/data-dictionary.md",
        ]),
        ("04-regulatory-change-procedure.md", ["compliance-management-system/03-obligations-register/regulatory-change-procedure.md"]),
        ("05-gap-assessment.md", [
            "compliance-management-system/04-gap-assessment/assessment-methodology.md",
            "compliance-management-system/04-gap-assessment/interview-questionnaire.md",
            ("embed", "Compliance Register"),
        ]),
        ("06-compliance-policy.md", ["compliance-management-system/05-controls-and-policies/compliance-policy.md"]),
        ("07-monitoring-plan.md", ["compliance-management-system/05-controls-and-policies/monitoring-plan.md"]),
        ("08-findings-and-actions.md", [
            ("text", "Findings from the gap assessment and their corrective actions."),
            ("embed", "Compliance Register"),
        ]),
        ("09-risk-and-control-register.md", [
            ("text", "Risks across compliance, governance and security, scored 1 to 25."),
            ("embed", "Risk and Control Register"),
        ]),
        ("10-management-report.md", ["compliance-management-system/07-reporting/management-report.md"]),
        ("11-executive-summary.md", ["compliance-management-system/07-reporting/executive-summary.md"]),
    ],
    "2-enterprise-governance-risk-dashboard": [
        ("01-governance-framework.md", ["enterprise-governance-risk-dashboard/03-governance-framework/governance-framework.md"]),
        ("02-terms-of-reference.md", ["enterprise-governance-risk-dashboard/03-governance-framework/committee-terms-of-reference.md"]),
        ("03-conflict-of-interest-declaration.md", ["enterprise-governance-risk-dashboard/03-governance-framework/conflict-of-interest-declaration.md"]),
        ("04-risk-appetite-statement.md", ["enterprise-governance-risk-dashboard/05-risk-governance/risk-appetite-statement.md"]),
        ("05-board-paper.md", [
            "enterprise-governance-risk-dashboard/06-board-oversight/oversight-workflow.md",
            "enterprise-governance-risk-dashboard/06-board-oversight/board-paper.md",
        ]),
        ("06-minutes.md", ["enterprise-governance-risk-dashboard/06-board-oversight/minutes.md"]),
        ("07-registers.md", [
            ("text", "Delegation, RACI, escalation, risks, KRIs, decisions and actions."),
            ("embed", "Governance Registers"),
        ]),
        ("08-dashboard-and-committee-report.md", [
            ("embed", "Governance Dashboard"),
            "enterprise-governance-risk-dashboard/08-reporting/committee-report.md",
        ]),
        ("09-executive-summary.md", ["enterprise-governance-risk-dashboard/08-reporting/executive-summary.md"]),
    ],
    "3-data-protection-privacy-assurance": [
        ("01-data-flow-map.md", ["data-protection-privacy-assurance/03-data-inventory/data-flow-map.md"]),
        ("02-dpia-gate-cctv-and-anpr.md", ["data-protection-privacy-assurance/04-dpia/dpia-01-gate-cctv-and-anpr.md"]),
        ("03-dpia-kijani-assist.md", ["data-protection-privacy-assurance/04-dpia/dpia-02-kijani-assist.md"]),
        ("04-dpia-procedure.md", ["data-protection-privacy-assurance/04-dpia/dpia-procedure.md"]),
        ("05-transfer-assessment.md", ["data-protection-privacy-assurance/05-processors/cross-border-transfer-assessment.md"]),
        ("06-privacy-notice.md", ["data-protection-privacy-assurance/07-rights-and-notices/privacy-notice.md"]),
        ("07-request-procedure.md", ["data-protection-privacy-assurance/07-rights-and-notices/data-subject-request-procedure.md"]),
        ("08-breach-response-plan.md", ["data-protection-privacy-assurance/08-breach-response/breach-response-plan.md"]),
        ("09-registers.md", [
            ("text", "Inventory, processors, retention, requests and breaches."),
            ("embed", "Data Protection Registers"),
        ]),
        ("10-assurance-report.md", ["data-protection-privacy-assurance/10-reporting/privacy-assurance-report.md"]),
        ("11-executive-summary.md", ["data-protection-privacy-assurance/10-reporting/executive-summary.md"]),
    ],
    "4-ai-governance-framework": [
        ("01-ai-governance-charter.md", ["ai-governance-framework/06-oversight/ai-governance-charter.md"]),
        ("02-acceptable-use-policy.md", ["ai-governance-framework/06-oversight/ai-acceptable-use-policy.md"]),
        ("03-classification-method.md", ["ai-governance-framework/04-classification/ai-risk-classification-method.md"]),
        ("04-impact-assessment-kijani-assist.md", ["ai-governance-framework/05-impact-assessment/ai-impact-assessment-kijani-assist.md"]),
        ("05-testing-protocol.md", ["ai-governance-framework/05-impact-assessment/ai-testing-protocol.md"]),
        ("06-registers.md", [
            ("text", "Inventory, classification, tests, oversight, vendor, changes and incidents."),
            ("embed", "AI Registers"),
        ]),
        ("07-committee-report.md", ["ai-governance-framework/10-reporting/ai-governance-committee-report.md"]),
        ("08-executive-summary.md", ["ai-governance-framework/10-reporting/executive-summary.md"]),
    ],
    "5-security-risk-incident-management": [
        ("01-site-security-survey.md", ["security-risk-incident-management/03-security-assessment/site-security-survey.md"]),
        ("02-access-control-policy.md", ["security-risk-incident-management/04-access-review/access-control-policy.md"]),
        ("03-access-review-report.md", ["security-risk-incident-management/04-access-review/access-review-report.md"]),
        ("04-incident-response-plan.md", ["security-risk-incident-management/05-incident-response/incident-response-plan.md"]),
        ("05-incident-playbooks.md", [
            "security-risk-incident-management/05-incident-response/incident-playbooks.md",
            "security-risk-incident-management/05-incident-response/chain-of-custody-form.md",
        ]),
        ("06-tabletop-exercise.md", [
            "security-risk-incident-management/06-tabletop-exercise/scenario.md",
            "security-risk-incident-management/06-tabletop-exercise/tabletop-exercise-report.md",
            ("embed", "Security Registers (select the Chronology tab before copying the link)"),
        ]),
        ("07-continuity-plan.md", ["security-risk-incident-management/07-continuity/continuity-and-recovery-plan.md"]),
        ("08-registers.md", [
            ("text", "Assets, threats, risks, access, incidents and recovery tests."),
            ("embed", "Security Registers"),
        ]),
        ("09-security-report.md", ["security-risk-incident-management/09-reporting/security-management-report.md"]),
        ("10-executive-summary.md", ["security-risk-incident-management/09-reporting/executive-summary.md"]),
    ],
    "6-integrated-grc-capstone": [
        ("01-integrated-case-study.md", ["integrated-grc-capstone/03-case-study/integrated-case-study.md"]),
        ("02-evidence-trail.md", ["integrated-grc-capstone/03-case-study/evidence-trail.md"]),
        ("03-remediation-roadmap.md", ["integrated-grc-capstone/05-findings-and-remediation/remediation-roadmap.md"]),
        ("04-committee-paper.md", ["integrated-grc-capstone/06-dashboard/committee-paper.md"]),
        ("05-registers.md", [
            ("text", "Requirements mapping, risks, findings, roadmap and dashboard."),
            ("embed", "Capstone Registers"),
        ]),
        ("06-executive-report.md", ["integrated-grc-capstone/07-executive/executive-report.md"]),
        ("07-executive-summary.md", ["integrated-grc-capstone/07-executive/executive-summary.md"]),
        ("08-presentation-outline.md", ["integrated-grc-capstone/07-executive/presentation-outline.md"]),
        ("09-lessons-learned.md", ["integrated-grc-capstone/07-executive/lessons-learned.md"]),
    ],
}

LINK = re.compile(r"\]\(([^)\s]+)\)")


def absolute_links(text, source):
    """Turn links relative to the source file into full GitHub links."""
    base = os.path.dirname(source)

    def fix(match):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        path, _, anchor = target.partition("#")
        rel = os.path.normpath(os.path.join(base, path)).replace(os.sep, "/")
        kind = "tree" if os.path.isdir(os.path.join(ROOT, rel)) else "blob"
        url = f"{GITHUB}/{kind}/main/{rel}" + (f"#{anchor}" if anchor else "")
        return f"]({url})"

    return LINK.sub(fix, text)


def convert(source, first):
    """Read one document; drop its title if first, else drop its repeated label."""
    with open(os.path.join(ROOT, source), encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if first and lines and lines[0].startswith("# "):
        lines = lines[1:]
    if not first:
        lines = [line for line in lines if not line.startswith(LABEL)]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines).strip())
    return absolute_links(text, source)


def embed_line(sheet):
    """Placeholder for a sheet embed, carrying the share link once the sheet exists."""
    name = sheet.split(" (")[0]
    if name in SHEETS:
        return f"[/embed: {SHEETS[name]} ({sheet})]"
    return f"[/embed: paste the {sheet} sheet link]"


def build_page(parts):
    blocks = []
    for i, part in enumerate(parts):
        if isinstance(part, tuple):
            kind, value = part
            blocks.append(value if kind == "text" else embed_line(value))
        else:
            # Only a document that opens the page gives up its title to the Notion page title.
            blocks.append(convert(part, i == 0))
    return "\n\n".join(blocks) + "\n"


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    write(os.path.join(OUT, "0-case-study-organisation.md"),
          convert("scenario/organisation-profile.md", True) + "\n")
    for folder, pages in PROJECTS.items():
        for name, parts in pages:
            write(os.path.join(OUT, folder, name), build_page(parts))


if __name__ == "__main__":
    main()
