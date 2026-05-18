# UI Skills Collection

**English** | [中文](README.zh-CN.md)

A personal UI design library and Codex plugin collection for designing, reviewing, and polishing frontend interfaces with sharper taste and repeatable checks.

This repository is intentionally not a giant bundle of every UI prompt or skill. It keeps a focused core: product-vs-brand design judgment, official skill structure patterns, visual hierarchy, accessibility, motion restraint, responsive checks, and small polish details that make interfaces feel finished.

## What Is Inside

```text
.agents/plugins/marketplace.json
plugins/ui-skills/.codex-plugin/plugin.json
plugins/ui-skills/skills/ui-craft/SKILL.md
plugins/ui-skills/skills/ui-craft/references/design-examples/
plugins/ui-skills/skills/ui-audit/SKILL.md
plugins/ui-skills/docs/
demos/homepage-variants/
docs/personal-design-library-roadmap.md
scripts/validate_plugin.py
```

## Skills

- `ui-craft`: design, build, redesign, refine, and polish UI.
- `ui-audit`: review existing UI and report actionable findings.

## Design Examples

The plugin now includes a concrete example library under [plugins/ui-skills/skills/ui-craft/references/design-examples](plugins/ui-skills/skills/ui-craft/references/design-examples).

- `anthropic/`: vendored Anthropic design-oriented skill references and theme recipes.
- `synthesis/`: typography scales, font pairing directions, page layouts, grids, and component composition recipes synthesized from the stronger UI skill sources.

## Current Design Philosophy

The current version removed UI/UX Pro Max, Taste, and ui-skills from the active plugin. They were useful for comparison, but they made the library too lookup-driven or too prescriptive.

The active mix is tighter:

- Impeccable-style product/brand register.
- Anthropic official skill patterns and compact frontend-design direction.
- User Interface Wiki audit priorities.
- Make Interfaces Feel Better detail polish.
- Designer Skills vocabulary for systems, hierarchy, forms, and critique.
- A small amount of 0xdesign-style multi-variant exploration.

## Demo

Open [demos/homepage-variants/index.html](demos/homepage-variants/index.html) to compare three homepage directions built from the current philosophy.

Preview images:

- [Product console](demos/homepage-variants/product-preview.png)
- [Editorial brand](demos/homepage-variants/editorial-preview.png)
- [Cinematic studio](demos/homepage-variants/cinematic-preview.png)
- [Mobile check](demos/homepage-variants/mobile-preview.png)

## Roadmap

The next step is turning this from a good UI plugin into a real personal design library. See [docs/personal-design-library-roadmap.md](docs/personal-design-library-roadmap.md).

## Validate

```bash
python scripts/validate_plugin.py
```

## Repository

Remote: <https://github.com/sn0wjin19/ui-skills-collection>
