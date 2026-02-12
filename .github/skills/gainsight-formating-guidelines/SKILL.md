---
name: success-planning-gainsight
description: Guide and assist with building out Success Plans trying the best to match Gainsight formatting. Use with any Success Plan agent.
---

Success Plans are built to be imported into Gainsight which is a tool CSAs use to record meeting, risks, CTAs, Success Plans, etc. 

Gainsight uses rich text formatting. 

## Gainsight Format Guidelines

### Key Format Rules

1. **Document title** must be `# [Account Name] - Success Plan` — NOT "Customer Success Plan Template"
2. **Header block** must include Created date, CSA, Review Cadence, and Next Review (with fiscal quarter)
3. **Section separators** — Use `---` between each major section (Customer Business Objectives, Copilot, GHAS, GHE, Actions, Risks, Summary)
4. **Customer Business Objectives** — Use narrative bullet points, NOT tables
5. **Goals** — Use numbered lists with `**Bold Title** - description` format
6. **Gaps** — Use bullet lists with `- **Gap Title** - description` format
7. **Key Activities** — Use numbered lists with `**CTA Name** - Timeline | description` format. Every Key Activity MUST include a target date or timeframe.
8. **Metrics blocks** — Use plain text format (not bold labels). Keep the `----------- Product Usage Metrics (Last Updated: Date) -----------` separator style.
9. **No table-heavy format** — Keep it readable for Gainsight copy/paste
10. Ensure to use the framework and templates within `references/success-plans` directory. If any of the reference materials conflict with these guidelines, prioritize the templates in `references/success-plans`. If there are any custom instructions provided within the GitHub Issue that triggered this agent, prioritize those instructions above all else.
11. When writing the output, use the template provided in `references/success-plans/success-plan-template-westx.md` This template **MUST** be used and followed.
12. If there are any CTAs you find, add them to each section at the end. The CSA will review them as an additional task to open a CTA for it. Consider which Key Activities may make for good CTAs along with any Gaps that may flag a Risk CTA.
13. **Include Risks & Dependencies section** — Document current risks with severity and mitigation, and dependencies that block goals.
14. **Include Success Metrics Summary table** — End with a summary table showing Product, Key Metric, Current, Target, and Timeline columns.
15. **Include Revision History** — Track document changes with Date, Author, and Changes columns.

### Reference Examples

The example success plan at `reference/success-plans/success-plan-example.md` is the gold-standard formatting reference. It demonstrates every formatting convention required: header block, section separators, goal formatting, Key Activity format with dates, plain-text metrics blocks, Risks & Dependencies, Success Metrics Summary table, and Revision History. When in doubt about formatting, reference this file for structure and style guidance.
