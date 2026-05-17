# UI Skills Codex Plugin

A local Codex plugin that combines the strongest parts of several UI-focused skills into one maintainable UI craft package.

## Structure

```text
.agents/plugins/marketplace.json
plugins/ui-skills/.codex-plugin/plugin.json
plugins/ui-skills/skills/ui-craft/SKILL.md
plugins/ui-skills/skills/ui-craft/scripts/search.py
plugins/ui-skills/skills/ui-craft/data/
plugins/ui-skills/skills/ui-audit/SKILL.md
plugins/ui-skills/docs/source-review.md
plugins/ui-skills/docs/third-party-notices.md
```

## Included Skills

- `ui-craft`: design, build, redesign, refine, and polish UI.
- `ui-audit`: review existing UI and report actionable findings.

`ui-craft` includes the UI/UX Pro Max search data and scripts:

```bash
cd plugins/ui-skills/skills/ui-craft
python scripts/search.py "saas dashboard" --domain product
python scripts/search.py "accessibility motion loading" --domain ux
python scripts/search.py "react responsive" --stack react
```

## Source Decision

See `plugins/ui-skills/docs/source-review.md` for the ranking and integration decision for each source skill.

## Validate

```bash
python scripts/validate_plugin.py
python plugins/ui-skills/skills/ui-craft/scripts/search.py "dashboard" --domain product --max-results 1
```
