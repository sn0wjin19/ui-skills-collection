# UI Skills Codex Plugin

A local Codex plugin that combines a focused set of UI design and review principles into one maintainable UI craft package.

## Structure

```text
.agents/plugins/marketplace.json
plugins/ui-skills/.codex-plugin/plugin.json
plugins/ui-skills/skills/ui-craft/SKILL.md
plugins/ui-skills/skills/ui-audit/SKILL.md
plugins/ui-skills/docs/anthropic-official-patterns.md
plugins/ui-skills/docs/source-review.md
plugins/ui-skills/docs/third-party-notices.md
demos/homepage-variants/
```

## Included Skills

- `ui-craft`: design, build, redesign, refine, and polish UI.
- `ui-audit`: review existing UI and report actionable findings.

## Current Source Mix

The current version removes UI/UX Pro Max, Taste, and ui-skills from the active plugin. It keeps a tighter mix: Impeccable, Anthropic official frontend-design patterns, User Interface Wiki, Make Interfaces Feel Better, Designer Skills, and a small amount of 0xdesign-style variant exploration.

## Demo

Open `demos/homepage-variants/index.html` to compare three homepage directions built from the current design philosophy.

## Source Decision

See `plugins/ui-skills/docs/source-review.md` for the ranking and integration decision for each source skill.

## Validate

```bash
python scripts/validate_plugin.py
```
