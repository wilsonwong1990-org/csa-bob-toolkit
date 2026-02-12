# Book of Business (BOB) - Account Management Workspace

## About This Repository

This repository is a personal account management workspace for GitHub Customer Success. It contains:
- **Account overviews** with customer context, seats, contacts, and deal details
- **Meeting notes** for customer engagements
- **Success plans** aligned with GitHub's four adoption pillars
- **Reference materials** for Success Engagements and frameworks

## Repository Structure

```
accounts/
├── [AccountName]/
│   ├── overview.md        # Account details, licensing, contacts
│   ├── meeting-notes.md   # Call logs and meeting notes
│   └── success-plan.md    # Outcome-driven success plan
reference/
└── success-plan-framework.md  # Success Engagement catalog
.github/
└── agents/
    ├── success-plan-agent.md       # Agent for creating success plans
    ├── quarterly-recap-agent.md    # Agent for quarterly leadership recaps
    └── weekly-snippets-agent.md    # Agent for weekly Friday snippet updates
```

## Working with Accounts

When working with account data:
1. **Overview files** contain licensing, seats, contacts, and key context
2. **Success plans** must map goals to Success Engagements and adoption pillars
3. **Meeting notes** should capture attendees, notes, and next steps

---

## Adding a New Account

When a user asks to add a new account, follow this process:

### GitHub MCP Server (Default)

When pulling **anything GitHub-related** (issues, PRs, files, releases, etc.), use the **GitHub MCP Server** as the default integration.

- **Default rule:** Prefer GitHub MCP tools (`mcp_io_github_*`) for GitHub interactions.
- **Avoid by default:** Web scraping/fetching GitHub pages (private repos often return 404) and other non-MCP connectors unless explicitly requested.
- **If blocked by permissions:** Ask the user to approve/allow access when prompted, or request they paste the relevant issue/PR text.

**MCP Service Config (reference):**

```json
"io.github.github/github-mcp-server": {
  "type": "http",
  "url": "https://api.githubcopilot.com/mcp/",
  "headers": {
    "Authorization": "${input:Authorization}"
  },
  "gallery": "https://api.mcp.github.com",
  "version": "0.27.0"
}
```

### Step 0: Search for Account Context in GitHub Issues

**Before creating any files**, use the GitHub MCP tools to search for existing account information in the Sales team's repo:

**Repository:** `github/Global-MidMarket-Sales`

**How to Search:**
1. Use `mcp_io_github_git_search_issues` to search for ALL issues containing the account name
2. Search the account name directly - issues may have different prefixes or formats
3. Common issue types: `Master Account Plan`, `MAP`, `FastTrack`, or just the account name
4. **Important:** Search broadly - account info may be spread across multiple issues
5. Always check issue comments - they often contain meeting notes, call plans, and deal updates

**What to Extract from Issues:**
- Deal size and type
- Key stakeholders and contacts
- Strategic priorities and objectives
- Renewal timeline
- Known risks or blockers
- Product entitlements and seat counts
- Migration context (from GitLab, BitBucket, etc.)

**Example Search:**
```
Search github/Global-MidMarket-Sales for issues containing "Pimco"
→ Found: MAP issue with deal context, FastTrack issue with onboarding details
```

**Include in Overview:** If issues are found, add a reference section:
```markdown
## GitHub Issue Tracking
- MAP Issue (URL) - Master Account Plan
- FastTrack Issue (URL) - Onboarding/FastTrack details
```

---

### Step 1: Create Account Folder Structure

Create the following files in `accounts/[AccountName]/`:

```
accounts/
└── [AccountName]/
    ├── overview.md        # Required - create first
    ├── meeting-notes.md   # Create when notes are provided
    └── success-plan.md    # Create using Success Plan Agent
```

**Naming Convention:** Use PascalCase for folder names (e.g., `Pimco`, `SpsCommerce`, `SeismicSoftware`)

### Step 2: Create overview.md

Use this template:

```markdown
# [Account Name] - Account Overview

## Account Status
- **Status:** [Active/Prospect/In Progress]
- **Engagement:** [Description]
- **Industry:** [Industry/Vertical]

---

## Deal Details
| Item | Details |
|------|---------|
| Deal Size | $X |
| Deal Type | [New/Expansion/Renewal] |
| Total Developers | X |
| GHE Seats | X |
| GHAS Seats | X |
| Copilot Seats | X |

---

## Licensing Overview

### GitHub Enterprise
| Metric | Count |
|--------|-------|
| Purchased | X |
| Consumed | X |

### Copilot
| Product | Seats |
|---------|-------|
| Copilot Business | X |
| Copilot Enterprise | X |

---

## Key Contacts

### Customer Stakeholders
| Name | Role | Notes |
|------|------|-------|

### GitHub Team
| Handle | Role | Notes |
|--------|------|-------|

---

## Notes
- [Key context about the account]

---

*Last Updated: [Date]*
```

### Step 3: Create meeting-notes.md (when notes are provided)

Use this template:

```markdown
# [Account Name] - Meeting Notes

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
```

**Important:** Always add new meeting notes at the TOP of the file, not the bottom. Do NOT overwrite existing notes.

### Step 4: Create success-plan.md

Use the **Success Plan Agent** in `.github/agents/success-plan-agent.md` to create a Gainsight-formatted success plan with:
- Customer Business Objectives (narrative bullets)
- Product Measurable Goals with Baseline → Target metrics
- CTAs and To be confirmed CTAs
- Risks & Dependencies

---

## Updating Existing Accounts

**Overview files:** Update with new licensing data, contacts, or deal changes. This is the source of truth for account details.

**Meeting notes:** Always ADD new notes at the top. Never overwrite existing notes.

**Success plans:** Update goals, metrics, and CTAs as priorities change. Update revision history.

## Four Adoption Pillars

All customer goals should align to:
| Pillar | Focus |
|--------|-------|
| **Vision & Value** | Objectives, sponsorship, business outcomes |
| **GitHub Platform** | Health, governance, migrations |
| **Skills & Capability** | Enablement, champions, certifications |
| **Developer Experience** | Usage, productivity, advocacy |

---

## Agents

This workspace includes custom agents in `.github/agents/` for specialized tasks:

| Agent | File | Purpose |
|-------|------|---------|
| **Success Plan Agent** | `success-plan-agent.md` | Create Gainsight-formatted success plans with CTAs and measurable goals |
| **Quarterly Recap Agent** | `quarterly-recap-agent.md` | Create leadership quarterly recaps from weekly snippets |
| **Weekly Snippets Agent** | `weekly-snippets-agent.md` | Generate weekly Friday snippets from meeting notes and issue context |

### Success Plan Agent

Creates comprehensive, outcome-driven Success Plans aligned with GitHub's four adoption pillars.

**Use when:**
- Creating a new success plan for a customer
- Updating goals and CTAs for an existing plan
- Defining measurable goals for Copilot, GHAS, GHE, or Actions

**Example prompts:**
- "Create a success plan for Pimco"
- "Help me define Copilot goals for Addepar"
- "Update the GHAS section for BeyondTrust"

### Quarterly Recap Agent

Creates professional quarterly recap documents for CSA leadership and management.

**Use when:**
- End of quarter (Q1, Q2, Q3, Q4) to compile team updates
- Leadership needs a summary of wins, challenges, and learnings
- Preparing for quarterly reviews or all-hands

**Sections:**
- Regional Customer Highlights & Key Wins 🏆
- Key Team Wins & Collaboration Highlights 🤝
- Key Customer Challenges 🚧
- Lessons Learned 📚
- Thanks & Acknowledgments 🙏

**Data Sources:**
- Weekly snippets from `github/Panam-MidMarket-CSA` discussions
- Account files in this workspace

**Example prompts:**
- "Create my Q3 FY26 quarterly recap"
- "Help me write a leadership update for this quarter"
- "Compile team wins and challenges for Q2"

**Output:** Saves to `quarterly-recaps/[Quarter]-[FY]-recap.md`

### Weekly Snippets Agent

Generates concise, leadership-ready weekly snippets from meeting notes and supplemental issue context.

**Use when:**
- It's Friday and you need to submit your weekly snippet
- Compiling a summary of the week's customer engagements
- Preparing your weekly update for your manager

**How it works:**
1. Scans `accounts/*/meeting-notes-*.md` for notes from the current week (Saturday → Friday)
2. Checks for an open GitHub Issue with the `weekly-snippets` label for supplemental context
3. Categorizes each customer into the most relevant snippet topic
4. Generates a clean Markdown snippet ready to post as a GitHub Issue comment

**Snippet Topics:** Key Decisions or Ships 🚢, Important topics for CSA-XLT Discussion 🛑, Celebrations 🎉, More Updates 👇

**GitHub Issue Template:** Use the `Weekly Snippets` issue template to add extra context throughout the week

**GitHub Actions:**
- `weekly-snippets-open.yml` — Opens a new snippets issue every Monday at 9 AM UTC
- `weekly-snippets-close.yml` — Closes the snippets issue every Friday at 6 PM UTC

**Example prompts:**
- "Generate my weekly snippet for this Friday"
- "Create a weekly snippet for the week ending February 6, 2026"
- "Draft my weekly snippet and let me review before saving"

**Output:** Saves to `reference/weekly-snippets/weekly-snippet-YYYY-MM-DD.md`

---

## Key References

When creating success plans, always reference:
- `reference/success-plan-framework.md` - Full Success Engagement catalog
- `accounts/<AccountName>/overview.md` - Account context

---

## External Data Sources

### Global-MidMarket-Sales Repository

The Sales team maintains account information in GitHub issues at `github/Global-MidMarket-Sales`.

**When to Search:**
- Creating a new account folder
- Building a success plan
- Looking for deal context, renewal dates, or stakeholder info
- Checking for existing MAP (Master Account Plan) or FastTrack issues

**Issue Types to Look For:**
| Issue Type | Contains |
|------------|----------|
| MAP (Master Account Plan) | Strategic objectives, deal size, key stakeholders, renewal timeline |
| FastTrack | Onboarding details, implementation status, technical context |
| Account name variations | Some issues use owner's name + "Master Account Plan" format |
| General Account Issues | Meeting notes, action items, risks |

**How to Search:**
Use GitHub MCP tools to search for issues:
- `mcp_io_github_git_search_issues` - Search ALL issues containing account name
- If you need the full issue body/comments and the MCP tools in this environment don’t expose them directly, ask the user to share/allow access when prompted or paste the relevant content.

**Always cite sources:** When using info from Sales issues, note the source in the overview or success plan.
