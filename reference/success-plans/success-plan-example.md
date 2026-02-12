# Acme Corp - Success Plan

**Created:** February 4, 2026  
**CSA:** Jane Smith  
**Review Cadence:** Quarterly  
**Next Review:** May 2026 (End of Q4 FY26)

---

## Customer Business Objectives

### Current State
Acme Corp is a mid-market SaaS company with 1,500+ GitHub Enterprise Cloud users. The organization has established strong platform adoption with 95% GHE seat utilization and has grown Copilot usage by 20% since October 2025. Acme is actively engaged with GitHub to improve Copilot adoption across distributed engineering teams (US, Ireland, India), expand GHAS code scanning coverage beyond secret scanning, and explore modernizing their CI/CD by migrating from Jenkins to GitHub Actions. Only two customer meetings have been held to date (January 15 and February 3, 2026); engagement is still early-stage.

### Goals
1. **Scale Copilot adoption and engagement across engineering teams** - Increase engaged user rate from 55% to 70% by end of Q4 FY26 through targeted enablement, champion program development, and advanced feature training for distributed teams.

2. **Expand GHAS code scanning to match secret scanning maturity** - Increase code scanning coverage from 12% to 40% of active repositories by end of Q1 FY27, focusing on high-value applications and critical repositories while maintaining 95%+ secret scanning coverage.

3. **Evaluate GitHub Actions migration from Jenkins** - Complete proof-of-concept migration of 3-5 representative Jenkins pipelines to GitHub Actions by end of Q4 FY26, demonstrating unified platform benefits and cost analysis.

4. **Maintain platform health and governance standards** - Sustain 90%+ GHE seat utilization through Q1 FY27 while implementing repository governance best practices (rulesets, CODEOWNERS, branch protection) across key repositories.

### Gaps
- **Distributed team enablement challenge** - Engineering teams across US, Ireland, and India require virtual-first training approach, which can reduce hands-on engagement compared to in-person sessions.
- **Security tooling overlap** - Active Snyk deployment creates uncertainty about GHAS positioning; no clear tool delineation strategy documented.
- **Jenkins migration complexity** - Unknown pipeline architecture and dependencies make migration planning difficult; team has limited Actions experience.
- **Early-stage engagement** - Only two meetings held to date; deeper relationship building required to understand full platform strategy.

### Key Activities
1. **Product Enablement (Workshop) - Copilot** - Late March 2026 | Deep-dive session on advanced Copilot features (Agent HQ, CLI, code review) for engineering leads across all regions
2. **Health Check - GHAS (CSA)** - Q4 FY26 | Assess current GHAS deployment, identify code scanning adoption barriers, and develop expansion roadmap targeting 40% coverage
3. **Migration Guidelines - Actions (CSA)** - Q4 FY26 | Deliver Jenkins-to-Actions migration patterns and runner optimization strategies for proof-of-concept
4. **Establish Regular Communication Cadence (CSA + CSM)** - Ongoing | Formalize monthly sync meetings with engineering leadership to maintain momentum on all initiatives

**Note:** These objectives represent a framework based on two introductory meetings and metrics data. Goals and key activities should be validated through ongoing customer engagement as the relationship develops.

---

## Copilot Measurable Goals

### Current State
Acme Corp has 520 licensed Copilot users with strong installation (80%) but a significant gap between active and engaged users. Usage has grown 20% since October 2025, indicating positive momentum. However, developers primarily use basic IDE completions and are unaware of advanced capabilities like Copilot CLI, code review, and custom instructions. Some teams use competing tools (Cursor, Claude) due to feature awareness gaps.

----------- Copilot Usage Metrics (Last Updated: February 4, 2026) -----------

Number of Licensed Users: 520
Installation Rate: 80% (goal: >= 88%)
Active Users: 65%
Gap between Active & Engaged Users: 10% (goal: <5%)
Engaged Users: 55%

### Goals
1. **Increase engaged user adoption from 55% to 70% by Q4 FY26** - Drive engagement through advanced feature enablement training and champion program development across distributed teams

2. **Reduce active-to-engaged gap from 10% to <5% by Q1 FY27** - Address the 52 users (10% of 520) who are active but not engaged through targeted outreach and workflow optimization guidance

3. **Grow installation rate from 80% to 88%+ by Q1 FY27** - Drive 42 additional installations among licensed-but-not-installed users through targeted enablement and addressing installation barriers

### Gaps
- **Feature awareness gap** - Developers unaware of Copilot CLI, code review, custom instructions, and agent capabilities
- **External tool competition** - Some developers perceive value in Cursor and Claude due to lack of Copilot feature knowledge
- **Distributed team complexity** - Training delivery across US, Ireland, and India time zones requires async-friendly formats

### Key Activities
1. **Product Enablement (Workshop) - Copilot** - Late March 2026 | Advanced features deep-dive for engineering leads focusing on CLI, code review, and custom instructions
2. **Champion Program - Copilot** - Q4 FY26 | Identify and enable 5-10 power users across regions to drive peer-to-peer enablement
3. **Metrics/Usage Insights - Copilot** - Ongoing | Monthly usage analytics review to track engagement patterns and identify targeted enablement opportunities

---

## GHAS Measurable Goals

### Current State
Acme Corp has deployed GitHub Advanced Security with 480 used seats out of 500 purchased (96% utilization) and strong secret scanning coverage (95% across 1,200 repositories). However, code scanning adoption remains low at 12% coverage (144 repositories), representing a significant opportunity for security posture improvement. The organization also uses Snyk for dependency scanning, creating potential tool overlap that needs clarification.

----------- GHAS Usage Metrics (Last Updated: February 4, 2026) -----------

Current State: 480 Used Seats / 500 Purchased Seats = 96%
Secret Scanning:
Repos with Secret Scanning enabled: 1,200
Coverage: 95%
Code Scanning:
Repos with Code Scanning enabled: 144
Coverage: 12%

### Goals
1. **Expand code scanning coverage from 12% to 40% by Q1 FY27** - Prioritize high-value repositories and critical applications, focusing on teams ready for immediate adoption

2. **Maintain secret scanning excellence at 95%+ coverage** - Sustain strong secret scanning posture while scaling code scanning through Q1 FY27

3. **Define GHAS-Snyk positioning strategy by Q4 FY26** - Document clear use case delineation (GHAS for first-party code scanning, Snyk for dependency management) or establish migration plan

### Gaps
- **Code scanning adoption lag** - 12% code scanning vs. 95% secret scanning suggests enablement gaps or developer workflow friction
- **Security tooling overlap** - Snyk deployment creates unclear tool boundaries; need to define complementary vs. competing use cases
- **AppSec team engagement** - No direct engagement with security team stakeholders to date; priorities and enablement needs not yet documented

### Key Activities
1. **Health Check - GHAS (CSA)** - Q4 FY26 | Assess current deployment, identify code scanning adoption barriers, and develop phased expansion roadmap
2. **Product Enablement (Workshop) - GHAS** - Q1 FY27 | Deliver code scanning enablement workshop for development teams, focusing on high-value repositories

---

## GHE Measurable Goals

### Current State
Acme Corp operates on GitHub Enterprise Cloud (GHEC) with 1,425 consumed seats out of 1,500 purchased (95% utilization). The platform serves as the primary source code repository with generally strong adoption. However, governance adoption varies across teams — larger teams have robust branch protection and CODEOWNERS policies, while smaller teams often lack basic controls.

----------- GHE Usage Metrics (Last Updated: February 4, 2026) -----------

License Utilization
GHE Usage: 1,425 Used Seats / 1,500 Purchased Seats = 95%

### Goals
1. **Maintain 90%+ seat utilization through Q1 FY27** - Continue strong platform adoption while supporting organic developer growth

2. **Implement repository governance best practices by Q1 FY27** - Deploy rulesets, CODEOWNERS standards, and branch protection across top 100 repositories to establish governance baseline

### Gaps
- **Variable governance adoption** - Inconsistent use of branch protection and CODEOWNERS across teams; smaller teams lack basic controls
- **Repository hygiene patterns** - Binaries and large files stored in repositories impacting platform health
- **Limited governance visibility** - Unknown adoption of merge queues, rulesets, and Enterprise Admin settings

### Key Activities
1. **Product Enablement (Workshop) - GHE** - Q4 FY26 | Best practices session on rulesets, CODEOWNERS, and branch protection for platform administrators
2. **Health Check - GHE (CSA)** - Q1 FY27 | Platform health assessment covering repository hygiene, license utilization, and governance maturity

---

## Actions Measurable Goals

### Current State
Acme Corp primarily uses Jenkins for CI/CD with approximately 700 pipelines across the organization. GitHub Actions adoption is minimal, used mainly for auxiliary automation tasks (linters, dependency scanning). The organization has expressed interest in migrating to Actions but needs to understand migration complexity, cost implications, and performance at their scale.

----------- Actions Usage Metrics (Last Updated: February 4, 2026) -----------

Current State:
Over the last 30 days, the customer used 45,000 minutes of GitHub Hosted Runners Minutes and 12,000 minutes of Self Hosted Runners Minutes.

### Goals
1. **Complete Actions proof-of-concept by Q4 FY26** - Migrate 3-5 representative Jenkins pipelines to GitHub Actions, demonstrating unified platform benefits and documenting cost comparison

### Gaps
- **Jenkins entrenchment** - 700+ pipelines represent significant migration scope; team has limited Actions expertise
- **Cost uncertainty** - Migration cost implications not yet analyzed; need runner strategy assessment
- **No migration plan** - Pipeline architecture and dependencies not yet documented

### Key Activities
1. **Migration Guidelines - Actions (CSA)** - Q4 FY26 | Deliver Jenkins-to-Actions migration patterns, runner optimization strategies, and cost analysis framework
2. **Product Enablement (Guided) - Actions** - Q1 FY27 | Provide async enablement resources for teams selected for pilot migration

---

## Risks & Dependencies

### Current Risks
- **Early-stage engagement risk** - Only two meetings held to date; limited understanding of full organizational priorities and potential blockers. Mitigation: Establish regular monthly cadence and expand stakeholder engagement.
- **Security tooling overlap** - Snyk and GHAS coexistence may create adoption confusion or budget contention. Mitigation: Facilitate GHAS-Snyk strategy session with security and engineering leadership by Q4 FY26.
- **Jenkins migration complexity** - Unknown pipeline dependencies may significantly increase migration effort. Mitigation: Conduct pipeline audit as part of proof-of-concept scoping.

### Dependencies
1. **Stakeholder alignment** - Copilot expansion and GHAS code scanning goals depend on engineering leadership buy-in from distributed teams
2. **Snyk strategy decision** - GHAS expansion plan depends on clarifying GHAS-Snyk positioning with security team
3. **Jenkins pipeline audit** - Actions migration feasibility depends on documenting pipeline architecture and dependencies

---

## Success Metrics Summary

| Product | Key Metric | Current | Target | Timeline |
|---------|-----------|---------|--------|----------|
| **Copilot** | Engaged Users | 55% | 70% | Q4 FY26 |
| **Copilot** | Installation Rate | 80% | 88%+ | Q1 FY27 |
| **GHAS** | Code Scanning Coverage | 12% | 40% | Q1 FY27 |
| **GHAS** | Secret Scanning Coverage | 95% | Maintain 95%+ | Ongoing |
| **GHE** | Seat Utilization | 95% | Maintain 90%+ | Q1 FY27 |
| **Actions** | POC Completion | Not started | 3-5 pipelines migrated | Q4 FY26 |

---

## Revision History

| Date | Author | Changes |
|------|--------|---------|
| February 4, 2026 | Jane Smith | Initial Success Plan created based on January and February 2026 meetings and Q3 FY26 metrics |

---

*Last Updated: February 4, 2026*
