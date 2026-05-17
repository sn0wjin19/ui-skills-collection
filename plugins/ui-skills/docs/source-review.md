# Source Review

This is the selection pass for the requested UI skills. I favored skills that are reusable across projects, enforce verifiable behavior, and improve actual UI implementation rather than only aesthetic prompting.

## Recommendation

Install this combined plugin as the default UI plugin. Do not install every original skill globally by default. Several are excellent, but their rules overlap or conflict when loaded together. This plugin keeps the best parts and avoids the worst collisions.

## Ranking

| Source | Decision | Why |
| --- | --- | --- |
| `impeccable` | Core spine | Best overall taste model. Strong brand vs product register, anti-slop rules, context loading, and command taxonomy. Integrated as the main design judgment layer. |
| `ui-ux-pro-max` | Core tool | Most useful installable asset because it includes searchable UI data, palettes, typography, UX guidance, stack guidance, charts, and design-system generation. Vendored the scripts and data. |
| `userinterface-wiki` | Core audit rules | Very strong rule catalog for animation, timing, UX laws, typography, visual details, audio, and prefetching. Integrated as audit priorities. |
| `make-interfaces-feel-better` | Core polish rules | High signal, low noise. Concentric radius, optical alignment, tabular numbers, hit areas, transitions, text wrapping, image outlines. Integrated directly as polish checks. |
| `ui-skills` | Core hardening rules | Good practical checks for baseline UI, accessibility, motion performance, and metadata. Integrated into accessibility, motion, metadata, and minimal-change guidance. |
| `designer-skills` | Selective reference | Very broad and modular. Useful for design tokens, visual hierarchy, forms, accessibility, design ops, and critique. Too large to load wholesale. Integrated the shared vocabulary and key audit categories. |
| `0xdesign` / `design-lab` | Selective workflow | Good preflight detection and multi-variant exploration workflow. Too heavy and Claude-specific as-is. Integrated project detection and variant thinking, skipped temp-route mechanics. |
| `taste` | Selective anti-template rules | Useful anti-slop energy, dependency verification, no emoji, state coverage, and layout variety. Some variants over-prescribe GSAP, randomization, and bans that would fight existing products. Integrated only the durable parts. |
| `ui-design-brain` | Excluded | The located source resolved to a Symfony product repository rather than an installable UI skill. No reusable `SKILL.md` was present in the cloned source, so it was not included. |

## Combined Design

The plugin exposes two skills:

- `ui-craft` for creation and implementation.
- `ui-audit` for review and fixing.

`ui-craft` owns the full workflow:

1. Classify the surface as brand or product.
2. Inspect existing project context and dependencies.
3. Search the vendored UI/UX database when the request benefits from references.
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

## Why Not Load Everything

All-original installation would create conflicts:

- `impeccable` permits ambitious brand motion, while `ui-skills` bans animation unless requested.
- `taste` pushes high motion and layout variance, while product UI often needs restraint and familiarity.
- `0xdesign` requires an interview-heavy design lab, while goal-mode Codex tasks often need direct implementation.
- Several skills ban different font and gradient choices in absolute terms.

The combined plugin routes these rules by context instead of applying them all at once.
