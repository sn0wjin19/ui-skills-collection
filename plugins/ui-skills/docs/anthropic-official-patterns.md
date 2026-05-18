# Anthropic Official Patterns

`anthropics/skills` is most valuable here as an official pattern reference, not as a wholesale UI dependency.

## What To Keep

- A skill should be a focused folder with a `SKILL.md`, optional scripts, and optional resources.
- The description should be precise enough that the agent knows when to load it.
- Instructions should be compact, procedural, and easy to apply.
- Complex skills can include scripts and resources, but only when they materially improve repeatability.
- `frontend-design` is useful because it forces a specific point of view before coding: purpose, tone, constraints, differentiation, and execution quality.

## What To Avoid

- Do not copy every official skill into this UI plugin. Most of the repository is not UI-specific.
- Do not let "bold" become a license for decoration. A distinctive direction still needs product fit, accessibility, performance, and responsive behavior.
- Do not use official examples as static rules. Treat them as proof of structure and compactness.

## Integration

`ui-craft` uses the official `frontend-design` idea as a pre-coding checkpoint:

1. Pick a concrete aesthetic lane.
2. Name the memorable idea.
3. Match implementation complexity to that idea.
4. Build working UI, not a moodboard.

Concrete Anthropic references now live inside the skill at `skills/ui-craft/references/design-examples/anthropic/`. Keep them as optional examples, not always-loaded rules.
