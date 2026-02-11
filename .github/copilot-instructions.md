# Book of Business (BOB) - CSA Account Management Toolkit

## About This Repository

This is a shared toolkit for GitHub Customer Success Architects (CSAs) to manage their Book of Business. It contains:
- **Custom agents** for Success Plans, Quarterly Recaps, Competitor Analysis, Weekly Updates, and more
- **Account templates** for consistent account documentation
- **Reference materials** for Success Engagements and frameworks
- **Instructions** for optimizing GitHub Copilot within your workspace

## Repository Structure

```
.github/
├── agents/
│   ├── success-plan-agent.md          # Create Gainsight-formatted success plans
│   ├── competitor-analysis-agent.md   # Analyze competitor landscape across accounts
│   ├── quarterly-recap-agent.md       # Create leadership quarterly recaps
│   ├── weekly-updates-agent.md        # Draft weekly status updates
│   ├── prompt-engineer.agent.md       # Analyze and improve any prompt/agent
│   └── task-researcher.agent.md       # Deep research specialist
├── instructions/
│   └── context-engineering.instructions.md  # Copilot optimization guidelines
└── copilot-instructions.md            # This file
accounts/
├── _template/                         # ← Start here! Copy for new accounts
│   ├── overview.md
│   ├── meeting-notes.md
│   └── success-plan.md
└── [YourAccounts]/                    # Your account folders go here
reference/
└── success-plan-framework.md          # Success Engagement catalog
```

## Getting Started

### 1. Fork or clone this repo
Each CSA should have their own copy of this toolkit.

### 2. Create your first account
Copy `accounts/_template/` to `accounts/[AccountName]/` and fill in the details.

### 3. Use the agents
Open Copilot Chat, select an agent, and start working:
- **Success Plan Agent**: "Create a success plan for [Account]"
- **Competitor Analysis Agent**: "Who are the competitors at [Account]?"
- **Quarterly Recap Agent**: "Create my Q3 FY26 quarterly recap"
- **Weekly Updates Agent**: "Help me write my weekly update"
- **Prompt Engineer**: Paste any agent file to get improvement suggestions

---

## Working with Accounts

1. **Overview files** contain licensing, seats, contacts, and key context
2. **Success plans** must map goals to Success Engagements and adoption pillars
3. **Meeting notes** should capture attendees, notes, and next steps
4. **Meeting notes** are added at the TOP of the file, not the bottom

### Naming Convention
Use PascalCase for folder names (e.g., `Pimco`, `SpsCommerce`, `SeismicSoftware`)

---

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

| Agent | File | Purpose |
|-------|------|---------|
| **Success Plan Agent** | `success-plan-agent.md` | Create Gainsight-formatted success plans with CTAs and measurable goals |
| **Competitor Analysis Agent** | `competitor-analysis-agent.md` | Analyze competitor landscape across accounts for Copilot, GHE, Actions, and GHAS |
| **Quarterly Recap Agent** | `quarterly-recap-agent.md` | Create leadership quarterly recaps |
| **Weekly Updates Agent** | `weekly-updates-agent.md` | Draft professional weekly status updates |
| **Prompt Engineer** | `prompt-engineer.agent.md` | Analyze and improve any prompt or agent |
| **Task Researcher** | `task-researcher.agent.md` | Deep research specialist for comprehensive analysis |

---

## Customizing for Your Team

### Update the Sales Repo Reference
The Success Plan Agent references `github/Global-MidMarket-Sales` for account context. Update this to your team's repo.

### Update the Weekly Snippets Source
The Quarterly Recap Agent references `github/Panam-MidMarket-CSA` for weekly snippets. Update this to your team's discussion source.

### Add Your Own Agents
Create new `.md` files in `.github/agents/` following the existing patterns.

---

## Contributing

Improvements to agents, templates, and reference materials are welcome! Please:
1. Test your changes with real account data (in your private fork)
2. Submit a PR with a clear description of what changed and why
3. Tag relevant team members for review

---

*Maintained by the GitHub Customer Success team*
