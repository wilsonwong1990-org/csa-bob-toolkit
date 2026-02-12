---
name: CTA-selection-framework
description: A framework to help guide and assist with developing CTAs.
---


## Intelligent CTA Selection Framework

**CRITICAL:** Do NOT copy-paste the same CTAs for every product. Analyze the customer context and select CTAs that directly address their situation.

### CTA Selection Decision Tree

Before assigning CTAs, ask:

1. **What's the customer's maturity with this product?**
   - New/Not started → Kick-off, Goal Setting Workshop
   - Early adoption → Enablement (Workshop), Champion Program
   - Scaling → Metrics/Usage Insights, Office Hours
   - Mature → Health Check, Product Release Updates

2. **What blockers or challenges exist?** (from meeting notes/overview)
   - Technical blockers → Office Hours, Health Check
   - Lack of executive buy-in → Goal Setting Workshop, Metrics/Usage Insights
   - Skills gap → Enablement (Workshop/Guided), Champion Program
   - Migration complexity → Migration Guidelines
   - Low engagement → Champion Program, Metrics/Usage Insights

3. **What's the customer's timeline pressure?**
   - Urgent/Renewal soon → Prioritize high-impact, quick-win CTAs
   - Long runway → Foundational CTAs (Goal Setting, Kick-off)

4. **What did the customer explicitly ask for?** (from meeting notes)
   - Honor customer requests first
   - Supplement with strategic recommendations

### CTA Selection Rules

| Customer Signal | Recommended CTA(s) |
|-----------------|--------------------|
| Just purchased, no usage | Product Kick-off |
| Low adoption, unclear why | Metrics/Usage Insights discussion → then Goal Setting |
| Developers struggling | Product Enablement (Workshop) |
| Need internal advocates | Champion Program |
| Migrating from competitor | Migration Guidelines |
| Platform performance issues for GitHub Enterprise | Health Check |
| Want to track ROI | Metrics/Usage Insights |
| Executives want updates | Goal Setting Workshop (for alignment) |
| Self-serve preferred | Product Enablement (Guided), Office Hours |
| Major version upgrade | Upgrade Guidelines, Product Release Updates |
| Scaling to new teams | Champion Program, Enablement (Guided) |

### Anti-Patterns (AVOID)

❌ **Don't do this:**
- Listing ALL available CTAs for a product
- Same CTAs appearing in Copilot, GHAS, GHE, and Actions sections
- Generic "Enablement Workshop" without context on why
- CTAs that don't connect to a stated goal or blocker

✅ **Do this instead:**
- Select 1-3 CTAs per product that directly address the customer's situation
- Explain WHY each CTA was selected (in the CTA description or Note)
- Vary CTAs across products based on different maturity levels
- Prioritize CTAs mentioned in meeting notes or customer requests

### CTA Output Standards

- **Tailored selection** - CTAs must be selected based on account context, NOT copied from templates
- **Unique per product** - Avoid repeating the same CTA across multiple product sections
- **Include rationale** - Add brief context (e.g., "Champion Program – Copilot (CSA) | To scale adoption across BUs after pilot")
- **Prioritize customer requests** - If meeting notes mention a need, address it first
- **Limit quantity** - 1-3 CTAs per product section; quality over quantity
- **Match maturity** - New customers get kick-offs; mature customers get health checks
- **Consider engagement levels** - Consider how receptive the customer is to meeting and wanting to partner up
- **ALWAYS include dates** - Every Key Activity must include a target date or timeframe. Use specific months for near-term items (e.g., "Late March 2026"), fiscal quarters for mid-term (e.g., "Q4 FY26"), or "Ongoing"/"Quarterly cadence" for recurring activities. All fiscal dates must use GitHub FY notation.

### Key Activity Format

Key Activities should follow this format:
```
1. **CTA Name** - Timeline | Description of activity and expected outcome
```

**Examples:**
- `1. **Product Enablement (Workshop)** - Late March 2026 | Deep-dive session on Agent HQ, CLI, and automation features`
- `2. **Metrics/Usage Insights** - Q4 FY26 | Analyze token consumption patterns and provide recommendations`
- `3. **Champion Program** - Ongoing | Support internal advocacy through regular office hours and best practice sharing`

## CTA Selections for particular products

### Copilot

**CTA Reference (Select based on customer context—do NOT use all):**

| CTA | Best For | Avoid When |
|-----|----------|------------|
| Goal Setting Workshop – Copilot | New customers, unclear objectives, executive alignment needed | Already has clear goals |
| Product Enablement (Workshop) – Copilot | Skills gaps, low engagement, new teams onboarding | Already trained, self-serve preferred |
| Product Enablement (Guided) – Copilot | Self-serve customers, async learners, scaling | Needs hands-on support |
| Office Hours – Copilot | Ongoing questions, troubleshooting, edge cases | Brand new, needs structure first |
| Champion Program – Copilot | Scaling adoption, internal advocates needed | Too early, no core users yet |
| Metrics/Usage Insights – Copilot | ROI tracking, executive reporting, identify gaps | No baseline data yet |
| Product Kick-off – Copilot | Just purchased, first introduction | Already using product | 

While these are the main CTAs we can access, also consider any bespoke CTAs we can use to better build the relationship with the customer.

**Selection Logic:** Review meeting notes for what the customer asked for. Check overview for maturity signals. Pick 1-2 CTAs that directly address the goal if there an ask or opportunity for GitHub.

**If customer OWNS Copilot but usage is low or unknown:**
```markdown
## Copilot Measurable Goals

**Goal:** Understand current Copilot adoption state and identify blockers to activation.

**Baseline:**
- Seats assigned: [X]
- Seat coverage: [X]% ([X] / [Y] committers)
- Engagement: Unknown or low

**Target:**
- Seat coverage: [X + 15]% by [Timeline]
- Engagement rate: 65% of assigned seats actively using by [Timeline]
- Establish baseline usage metrics by [Timeline]

**Recommended Action:** Establish baseline usage metrics and identify adoption gaps before setting targets.

**CTAs:**
- Metrics/Usage Insights - Copilot - [Timeline] | Establish baseline and identify gaps

**To be confirmed CTAs:**
- Goal Setting Workshop - Copilot | Once baseline exists, define targets
- Product Enablement (Workshop) - Copilot | If enablement gaps identified

**Note:** Do not set engagement targets until baseline usage data is available.
```

**If customer DOES NOT have Copilot (no entitlement, using competitor):**
```markdown
## Copilot Measurable Goals

No Copilot entitlement for this account.

**Known AI Tooling:** [e.g., "Developers use Cursor/Tabnine/etc." or "Unknown"]

**Recommended Action:** No action required. Monitor for interest. If customer expresses interest in Copilot, schedule a discovery conversation.
```

### GHAS

**CTA Reference (Select based on customer context—do NOT use all):**

| CTA | Best For | Avoid When |
|-----|----------|------------|
| Product Enablement (Workshop) – GHAS | Security teams new to GHAS, hands-on learning | Already proficient |
| Product Enablement (Guided) – GHAS | Self-serve security teams, async rollout | Needs hands-on guidance |
| Health Check – GHAS | Low utilization, coverage gaps, config issues | Just started, no data |
| Office Hours – GHAS | Troubleshooting, advanced questions | Brand new, needs onboarding |
| Champion Program – GHAS | Scaling across repos/teams, security advocates | Single team, early stage |
| Metrics/Usage Insights – GHAS | Executive reporting, compliance tracking | No usage yet |
| Migration Guidelines – GHAS | Moving from Snyk/Veracode/BlackDuck | No existing security tool |
| Product Release Updates – GHAS | Mature customers, staying current | Still onboarding |

**Selection Logic:** Check if migrating from another tool → Migration Guidelines. Low coverage → Health Check. New to GHAS → Kick-off or Enablement.

**If customer DOES NOT have GHAS (no entitlement, using competitor):**
```markdown
## GHAS Measurable Goals

No GHAS entitlement for this account.

**Known Security Tooling:** [e.g., "Customer uses Snyk/Veracode/BlackDuck/etc." or "Unknown"]

**Recommended Action:** No action required. Monitor for interest. If migration discussions arise, schedule Migration Guidelines – GHAS.
```

### GHE

**CTA Reference (Select based on customer context—do NOT use all):**

| CTA | Best For | Avoid When |
|-----|----------|------------|
| Health Check – GHE | Performance issues, governance gaps, security review | Just migrated, still stabilizing |
| Upgrade Guidelines – GHE | On old version, planning upgrade | Already on latest |
| Migration Guidelines – GHE | Moving from GitLab/Bitbucket/Azure DevOps | Native GHE customer |
| Office Hours – GHE | Admin questions, best practices | Needs structured onboarding |
| Champion Program – GHE | Scaling platform adoption, admin advocacy | Single admin, small org |
| Product Enablement (Guided) – GHE | New admins, self-serve teams | Need hands-on migration help |
| Product Kick-off – GHE | Brand new customer, first GHE setup | Already operational |
| Product Release Updates – GHE | Staying current on features | Still learning basics |

**Selection Logic:** Migrating → Migration Guidelines. Performance/governance concerns → Health Check. New admins → Enablement.

### GHAS

**CTAs:**
- Metrics/Usage Insights - Actions - [Timeline] | Establish baseline usage

**To be confirmed CTAs:**
- Product Enablement (Workshop) - Actions | If optimization opportunities identified

**Note:** Actions is typically included with GHE. Focus on optimization rather than activation unless migration is a priority.
```

**If customer is NOT using Actions (using competitor CI/CD):**
```markdown
## Actions Measurable Goals

No Actions usage data or CI/CD priorities identified for this account.

**Known CI/CD Tooling:** [e.g., "Customer uses Jenkins/GitLab CI/CircleCI/Azure DevOps/etc." or "Unknown"]

**Recommended Action:** No action required. Revisit if customer expresses CI/CD consolidation interest.

**CTA Reference (Select based on customer context—do NOT use all):**

| CTA | Best For | Avoid When |
|-----|----------|------------|
| Migration Guidelines – Actions | Moving from Jenkins/GitLab CI/CircleCI | Already on Actions |
| Product Enablement (Workshop) – Actions | Teams new to Actions, workflow design | Already proficient |
| Product Enablement (Guided) – Actions | Self-serve teams, async learning | Complex migration needs |
| Office Hours – Actions | Troubleshooting, optimization questions | Needs structured training |
| Champion Program – Actions | Scaling Actions org-wide | Single team usage |
| Metrics/Usage Insights – Actions | Optimizing minutes, cost tracking | No significant usage yet |

**Selection Logic:** Migrating CI/CD → Migration Guidelines. Optimizing costs → Metrics/Usage Insights. Scaling → Champion Program.

**If customer is using Actions but usage/priorities are unclear:**
## Actions Measurable Goals

**Goal:** Understand current Actions usage and identify optimization or expansion opportunities.

**Baseline:**
- Minutes usage: [X/month or Unknown]
- Key workflows: Unknown
- Pipeline coverage: [X]% of CI/CD on Actions

**Target:**
- Minutes usage: [Baseline + 30]% increase by [Timeline]
- Pipeline coverage: [Baseline + 20]% by [Timeline]
- Migrate 2-3 pilot pipelines from legacy CI/CD by [Timeline]

**Recommended Action:** Gather usage metrics and understand CI/CD strategy before setting targets.