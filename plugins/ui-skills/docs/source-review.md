# Source Review

This is the revised selection pass. The goal is a sharper UI plugin, not a pile of overlapping taste prompts.

## Recommendation

Use this combined plugin as the default UI plugin. Do not install every original skill globally by default. Several are interesting, but rules collide quickly when they are all active.

## Current Ranking

| Source | Decision | Why |
| --- | --- | --- |
| `impeccable` | Core spine | Best overall taste model. Strong brand vs product register, anti-slop rules, context loading, and command taxonomy. Integrated as the main design judgment layer. |
| `anthropics/skills` | Official pattern reference | Best official reference for skill structure and compact creative direction. Integrated `frontend-design` principles and kept the repository as a formatting/spec reference. |
| `userinterface-wiki` | Core audit rules | Very strong rule catalog for animation, timing, UX laws, typography, visual details, audio, and prefetching. Integrated as audit priorities. |
| `make-interfaces-feel-better` | Core polish rules | High signal, low noise. Concentric radius, optical alignment, tabular numbers, hit areas, transitions, text wrapping, image outlines. Integrated directly as polish checks. |
| `designer-skills` | Selective reference | Very broad and modular. Useful for design tokens, visual hierarchy, forms, accessibility, design ops, and critique. Too large to load wholesale. Integrated the shared vocabulary and key audit categories. |
| `0xdesign` / `design-lab` | Selective workflow | Good preflight detection and multi-variant exploration workflow. Too heavy and Claude-specific as-is. Integrated project detection and variant thinking, skipped temp-route mechanics. |
| `ui-ux-pro-max` | Removed | The searchable database is useful, but in practice it can pull the agent toward lookup-driven generic choices. Removed the vendored data and scripts. |
| `taste` | Removed | Strong anti-slop energy, but too prescriptive for this plugin: randomization, GSAP bias, and absolute style bans fight existing product constraints. |
| `ui-skills` | Removed | Practical hardening rules, but much of the value overlaps with User Interface Wiki and Make Interfaces Feel Better. Removed to avoid duplicate hard bans. |
| `ui-design-brain` | Excluded | The located source resolved to a Symfony product repository rather than an installable UI skill. No reusable `SKILL.md` was present in the cloned source, so it was not included. |

## Combined Design

The plugin exposes two skills:

- `ui-craft` for creation and implementation.
- `ui-audit` for review and fixing.

`ui-craft` owns the full workflow:

1. Classify the surface as brand or product.
2. Inspect existing project context and dependencies.
3. Commit to a specific creative direction, using Anthropic's official frontend-design pattern as the compact prompt.
4. Choose color, typography, layout, density, motion, accessibility, and state strategies.
5. Implement surgically in the existing style.
6. Verify with project checks and browser inspection when there is visible UI.

`ui-audit` owns review posture:

1. Accessibility and usability.
2. Responsive layout failures.
3. Missing states.
4. Hierarchy and density.
5. Motion performance.
6. Detail polish.
7. Public-page metadata.

## Why Remove UI/UX Pro Max, Taste, And ui-skills

- `ui-ux-pro-max` is strongest as a lookup tool, but it made this plugin feel database-led instead of judgment-led.
- `taste` is useful for escaping bland output, but it tends to overfit to high-motion landing-page aesthetics.
- `ui-skills` has good rules, but the same practical territory is covered more cleanly by User Interface Wiki plus Make Interfaces Feel Better.

The current plugin routes fewer, stronger principles by context.
