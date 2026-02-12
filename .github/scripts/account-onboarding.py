#!/usr/bin/env python3
"""Account Onboarding Script (Python)
Parses issue form body and generates account scaffold files.
"""
import json
import re
import sys
import pathlib
from datetime import date


def _first_non_empty(*vals):
    for v in vals:
        if v is None:
            continue
        if isinstance(v, str) and v.strip() == "":
            continue
        return v
    return None


def _display(val):
    return "TBD" if val is None or (isinstance(val, str) and val.strip() == "") else val

FIELD_LABELS = {
    "accountName": "Account Name",
    "folderName": "Folder Name (optional)",
    "status": "Status",
    "engagement": "Engagement",
    "industry": "Industry",
    "dealSize": "Deal Size",
    "dealType": "Deal Type",
    "totalDevelopers": "Total Developers",
    "gheSeats": "GHE Seats",
    "ghasSeats": "GHAS Seats",
    "copilotBusinessSeats": "Copilot Business Seats",
    "copilotEnterpriseSeats": "Copilot Enterprise Seats",
    "customerStakeholders": "Customer Stakeholders (table)",
    "githubTeam": "GitHub Team (table)",
    "notes": "Notes",
    "stafftoolsLicensing": "Stafftools Licensing Overview (optional)",
}


def extract_field(markdown: str, label: str) -> str:
    pattern = rf"^### {re.escape(label)}\s*([\s\S]*?)(?=^### |\Z)"
    m = re.search(pattern, markdown, flags=re.MULTILINE)
    return m.group(1).strip() if m else ""


def to_pascal_case(s: str) -> str:
    return "".join(w.capitalize() for w in re.sub(r"[^0-9A-Za-z\s]", " ", s).split())


def render_overview(data: dict | None = None) -> str:
    lines = []
    lines.append(f"# {data['accountName']} - Account Overview\n")

    lines.append("## Account Status")
    lines.append(f"- **Status:** {data.get('status') or 'TBD'}")
    lines.append(f"- **Engagement:** {data.get('engagement') or 'TBD'}")
    lines.append(f"- **Industry:** {data.get('industry') or 'TBD'}\n\n---\n")

    lines.append("## Deal Details")
    lines.append("| Item | Details |")
    lines.append("|------|---------|")
    lines.append(f"| Deal Size | {_display(data.get('dealSize'))} |")
    lines.append(f"| Deal Type | {_display(data.get('dealType'))} |")
    lines.append(f"| Total Developers | {_display(data.get('totalDevelopers'))} |")
    lines.append(f"| GHE Seats | {_display(data.get('gheSeats'))} |")
    lines.append(f"| GHAS Seats | {_display(data.get('ghasSeats'))} |")
    lines.append(
        f"| Copilot Seats | Business: {_display(data.get('copilotBusinessSeats'))}, Enterprise: {_display(data.get('copilotEnterpriseSeats'))} |\n\n---\n"
    )

    lines.append("## Licensing Overview\n")
    lines.append("### GitHub Enterprise")
    ghe_purchased = _first_non_empty(data.get("_parsed_ghe_purchased"), data.get("gheSeats"))
    ghe_consumed = _first_non_empty(data.get("_parsed_ghe_consumed"))
    ghe_remaining = "TBD"
    if str(ghe_purchased).isdigit() and str(ghe_consumed).isdigit():
        try:
            ghe_remaining = str(int(ghe_purchased) - int(ghe_consumed))
        except Exception:
            pass
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Purchased | {_display(ghe_purchased)} |")
    lines.append(f"| Consumed | {_display(ghe_consumed)} |")
    lines.append(f"| Remaining | {_display(ghe_remaining)} |\n")

    lines.append("### Copilot")
    lines.append("| Product | Seats |")
    lines.append("|---------|-------|")
    lines.append(
        f"| Copilot Business | {_display(_first_non_empty(data.get('_parsed_copilot_business'), data.get('copilotBusinessSeats')))} |"
    )
    lines.append(
        f"| Copilot Enterprise | {_display(_first_non_empty(data.get('_parsed_copilot_enterprise'), data.get('copilotEnterpriseSeats')))} |\n\n---\n"
    )

    lines.append("## Key Contacts\n")
    lines.append("### Customer Stakeholders")
    lines.append("| Name | Role | Notes |")
    lines.append("|------|------|-------|")
    if data.get("customerStakeholders"):
        lines.append(data["customerStakeholders"])
    else:
        lines.append("| - | - | - |")
    lines.append("")

    lines.append("### GitHub Team")
    lines.append("| Handle | Role | Notes |")
    lines.append("|--------|------|-------|")
    if data.get("githubTeam"):
        lines.append(data["githubTeam"])
    else:
        lines.append("| - | - | - |")
    lines.append("\n---\n")

    lines.append("## Notes")
    if data.get("notes"):
        for n in filter(bool, data["notes"].splitlines()):
            lines.append(f"- {n}")
    else:
        lines.append("- TBD")
    lines.append("")

    lines.append("## GitHub Issue Tracking")
    lines.append("- MAP Issue: TBD")
    lines.append("- FastTrack Issue: TBD")
    lines.append("")

    lines.append(f"*Last Updated: {date.today().isoformat()}*")
    return "\n".join(lines)


def render_meeting_notes(account_name: str) -> str:
    return f"""# {account_name} - Meeting Notes

---

## [Date] - [Meeting Type]

**Date:** [Date]  
**Type:** [Intro Call/QBR/Technical Review/etc.]  
**Attendees:** [Names]  

### Key Takeaways

1. [Key point]
2. [Key point]

### Next Steps

- [ ] [Action item]

---

*Add new meeting notes above this line*
"""


def render_success_plan(account_name: str) -> str:
    return f"""# {account_name} - Success Plan

> Generated via Issue Ops. Use `.github/agents/success-plan-agent.md` to build a Gainsight-formatted plan. Reference `reference/success-plan-framework.md`.

## Customer Business Objectives
- TBD

## Copilot Measurable Goals
- TBD

## GHAS Measurable Goals
- TBD

## GHE Measurable Goals
- TBD

## Actions Measurable Goals
- TBD

## CTAs
- TBD

## Risks & Dependencies
- TBD
"""

def extract_stafftools_block(body: str) -> str:
    m = re.search(r"##\s+Licensing overview[\s\S]*?(?=\n##\s+|\Z)", body, flags=re.IGNORECASE)
    return m.group(0).strip() if m else ""


def parse_stafftools_licensing(text: str) -> dict:
    """Parse stafftools licensing markdown block for seat counts.

    Returns:
        {
          ghe_purchased, ghe_consumed,
          ghas_max_committers, ghas_purchased,
          copilot_business, copilot_enterprise,
        }
    """
    out = {}

    def table_blocks(t: str):
        blocks = []
        current = []
        for line in t.splitlines():
            if line.strip().startswith('|'):
                current.append(line)
            else:
                if current:
                    blocks.append(current)
                    current = []
        if current:
            blocks.append(current)
        return blocks

    def parse_number(val: str):
        m = re.search(r"([0-9][0-9,]*)", val)
        return int(m.group(1).replace(',', '')) if m else None

    blocks = table_blocks(text)

    # GitHub Enterprise table (first block containing 'GitHub Enterprise')
    for block in blocks:
        if block and 'GitHub Enterprise' in block[0]:
            for row in block[2:]:
                cols = [c.strip() for c in row.strip('|').split('|')]
                if not cols:
                    continue
                first = cols[0]
                if first.lower().startswith('purchased'):
                    n = parse_number(first)
                    if n is not None:
                        out['ghe_purchased'] = n
                elif first.lower().startswith('consumed'):
                    n = parse_number(first)
                    if n is not None:
                        out['ghe_consumed'] = n
            break

    # GHAS table (block containing 'Advanced Security')
    for block in blocks:
        if block and 'Advanced Security' in block[0]:
            # detect "Not purchased"
            text_block = '\n'.join(block)
            if re.search(r'Not purchased', text_block, re.IGNORECASE):
                out['ghas_purchased'] = 0
                out['ghas_max_committers'] = 0
            else:
                for row in block[2:]:
                    first = [c.strip() for c in row.strip('|').split('|')][0]
                    if first.lower().startswith('maximum committers'):
                        n = parse_number(first)
                        if n is not None:
                            out['ghas_max_committers'] = n
            break

    # Copilot table
    for block in blocks:
        if block and 'Copilot' in block[0]:
            for row in block[2:]:
                first = [c.strip() for c in row.strip('|').split('|')][0]
                if first.lower().startswith('copilot business'):
                    n = parse_number(first)
                    if n is not None:
                        out['copilot_business'] = n
                elif first.lower().startswith('copilot enterprise'):
                    n = parse_number(first)
                    if n is not None:
                        out['copilot_enterprise'] = n
            break

    return out


def main(event_path: str):
    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)
    body = event.get("issue", {}).get("body") or ""

    data = {}
    for key, label in FIELD_LABELS.items():
        data[key] = extract_field(body, label)

    # Stafftools licensing block: either field or raw body section
    stafftools_block = data.get("stafftoolsLicensing") or extract_stafftools_block(body)
    parsed = parse_stafftools_licensing(stafftools_block) if stafftools_block else {}
    if parsed:
        data["_parsed_ghe_purchased"] = parsed.get("ghe_purchased")
        data["_parsed_ghe_consumed"] = parsed.get("ghe_consumed")
        data["_parsed_ghas_max_committers"] = parsed.get("ghas_max_committers")
        data["_parsed_copilot_business"] = parsed.get("copilot_business")
        data["_parsed_copilot_enterprise"] = parsed.get("copilot_enterprise")

    # prefer parsed values when form fields missing
    if not data.get("gheSeats") and parsed.get("ghe_purchased") is not None:
        data["gheSeats"] = parsed["ghe_purchased"]
    if not data.get("ghasSeats") and parsed.get("ghas_max_committers") is not None:
        data["ghasSeats"] = parsed["ghas_max_committers"]
    if not data.get("copilotBusinessSeats") and parsed.get("copilot_business") is not None:
        data["copilotBusinessSeats"] = parsed["copilot_business"]
    if not data.get("copilotEnterpriseSeats") and parsed.get("copilot_enterprise") is not None:
        data["copilotEnterpriseSeats"] = parsed["copilot_enterprise"]

    if not data.get("accountName"):
        print("Account Name is required", file=sys.stderr)
        sys.exit(1)
    if data.get("folderName") is None or "No response" in data.get("folderName"):
        data["folderName"] = to_pascal_case(data["accountName"])


    dir_path = pathlib.Path.cwd() / "accounts" / data["folderName"]
    dir_path.mkdir(parents=True, exist_ok=True)

    files = [
        ("overview.md", render_overview(data)),
        ("meeting-notes.md", render_meeting_notes(data["accountName"])),
        ("success-plan.md", render_success_plan(data["accountName"])),
    ]

    created_files = []
    skipped_files = []
    for name, content in files:
        file_path = dir_path / name
        try:
            with open(file_path, "x", encoding="utf-8") as fh:
                fh.write(content)
            created_files.append(str(file_path.relative_to(pathlib.Path.cwd())))
        except FileExistsError:
            skipped_files.append(str(file_path.relative_to(pathlib.Path.cwd())))

    output = {
        "accountName": data["accountName"],
        "folderName": data["folderName"],
        "createdFiles": created_files,
        "skippedFiles": skipped_files,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: account-onboarding.py <GITHUB_EVENT_PATH>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
