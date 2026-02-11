---
description: 'Guidelines for structuring code and projects to maximize GitHub Copilot effectiveness through better context management'
applyTo: '**'
---

# Context Engineering

Principles for helping GitHub Copilot understand your codebase and provide better suggestions.

## Project Structure

- **Use descriptive file paths**: `accounts/Pimco/overview.md` > `accounts/p/o.md`. Copilot uses paths to infer intent.
- **Colocate related files**: Keep overview, meeting notes, and success plan in the same account folder.
- **Follow consistent naming**: PascalCase for account folders, lowercase-hyphenated for files.

## Working with Copilot

- **Keep relevant files open in tabs**: Copilot uses open tabs as context signals. Working on an account? Open that account's overview, meeting notes, and success plan.
- **Position cursor intentionally**: Copilot prioritizes content near your cursor.
- **Use Copilot Chat for complex tasks**: Inline completions have minimal context. Chat mode sees more files.

## Context Hints

- **Reference patterns explicitly**: "Follow the same pattern as `accounts/Pimco/success-plan.md`" gives Copilot a concrete example.
- **Use strategic comments**: At the top of complex docs, briefly describe the purpose.

## Multi-File Changes

- **Describe scope first**: Tell Copilot all files involved before asking for changes.
- **Work incrementally**: One file at a time, verifying each change.

## When Copilot Struggles

- **Missing context**: Open the relevant files in tabs, or explicitly paste content.
- **Generic answers**: Be more specific. Add constraints, reference existing files.
