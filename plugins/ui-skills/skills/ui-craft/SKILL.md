---
name: ui-craft
description: Use when designing, building, redesigning, refining, or polishing frontend UI. Covers brand pages, product surfaces, dashboards, components, forms, responsive behavior, accessibility, motion, design systems, visual hierarchy, typography, color, spacing, and implementation-quality checks.
license: MIT
---

# UI Craft

Design and implement frontend interfaces with product sense, visual taste, and verification. This skill combines:

- Impeccable as the taste and register spine.
- Anthropic's official `frontend-design` skill as the compact creative directive: pick a bold, context-specific aesthetic and execute it fully.
- Anthropic design examples under `references/design-examples/anthropic/` for concrete theme, typography, and art-direction starting points.
- User Interface Wiki as the interaction, motion, typography, and UX-law audit base.
- Make Interfaces Feel Better as the detail-polish checklist.
- Designer Skills as design-system vocabulary.
- 0xdesign as selective multi-variant exploration inspiration.

The plugin intentionally no longer depends on UI/UX Pro Max, Taste, or ui-skills. Those sources were useful for comparison, but the combined guidance is sharper without their searchable database, randomization requirements, and overlapping hard bans.

## First Pass

Before proposing or editing UI:

1. Identify the surface:
   - Brand: marketing, landing, portfolio, editorial, campaign, place, product showcase.
   - Product: app UI, dashboard, admin, settings, table, form, workflow, authenticated tool.
2. Inspect project context:
   - Existing `PRODUCT.md`, `DESIGN.md`, design tokens, component primitives, CSS variables, Tailwind config, package.json, and nearby UI files.
   - Prefer local components and design-system primitives before adding dependencies.
3. Infer stack and constraints:
   - Package manager, framework, styling system, animation libraries, icon set, routing, metadata pattern.
   - Never import a third-party UI, motion, icon, or state library without checking it exists.
4. Define success in verifiable terms:
   - Example: "No horizontal scroll at 320px, all controls keyboard reachable, primary action visible, no layout-shifting hover states."

## Creative Direction

Before coding, commit to one clear direction:

- Purpose: what job does this page or component do, and who is using it?
- Scene: where, when, and under what pressure is the user encountering it?
- Register: product UI or brand UI?
- Aesthetic lane: restrained operating system, editorial artifact, industrial console, tactile retail, cinematic campaign, playful utility, calm institutional, or another concrete lane.
- Memory: what is the one thing someone should remember after seeing it?

Boldness is not mandatory. Commitment is. Maximalism needs elaborate code and strong art direction; minimalism needs exact spacing, typography, and restraint.

## Core Workflow

1. Context scan:
   - Read the relevant existing UI and design files.
   - Note register, audience, primary task, density, platform, and constraints.
2. Direction:
   - Product surfaces default to restrained, familiar, task-first UI.
   - Brand surfaces need a point of view, imagery or strong art direction, and a clear aesthetic lane.
3. System choices:
   - Pick color strategy before color values.
   - Pick typography for the register, not by category reflex.
   - Decide spacing rhythm, information density, component vocabulary, and motion intensity.
4. Implementation:
   - Make surgical changes.
   - Use existing tokens and components when possible.
   - Add states: default, hover, focus, active, disabled, loading, empty, error.
5. Verification:
   - Run the project checks available.
   - For visible UI work, inspect in a browser across mobile and desktop.
   - Verify no overlap, no horizontal scroll, no broken media, no inaccessible controls.

## Reference Library

Keep `SKILL.md` lean. Load detailed examples only when the request needs them:

- For concrete fonts, type scales, spacing, grids, and CSS snippets, read `references/design-examples/synthesis/typography-layout-recipes.md`.
- For homepage, dashboard, editor, editorial, or variant-board structures, read `references/design-examples/synthesis/page-layout-recipes.md`.
- For buttons, cards, forms, metrics, tables, navigation, loading, empty, and error states, read `references/design-examples/synthesis/component-composition-recipes.md`.
- For Anthropic's original frontend-design direction prompt and theme examples, read `references/design-examples/anthropic/index.md`, then the specific file it points to.

If starting from a blank page or if the user asks for "examples", "fonts", "layout", "homepage style", or "make it more complete", read the relevant reference before coding. If editing an existing product with a mature design system, prefer local tokens and components, then use these references only to fill gaps.

## Register Rules

### Product UI

Design serves the task. Familiarity, consistency, density, and speed are strengths.

- Use standard affordances for navigation, tabs, tables, dialogs, menus, forms, and settings.
- System fonts and one-family type systems are acceptable.
- Accent color is for primary actions, selected states, focus, and semantic status.
- Skeletons beat centered spinners inside content.
- Empty states teach the next action.
- Motion must communicate state, not decorate.
- Avoid display fonts in labels, strange custom controls, gratuitous page-load choreography, and inconsistent component vocabulary.

### Brand UI

Design is part of the product. Distinctiveness matters.

- Name the aesthetic lane before building.
- Use real imagery, product screenshots, generated raster assets, canvas, WebGL, or strong art direction when the subject calls for it.
- A text-only brand surface is only acceptable when typography is intentionally carrying the whole composition.
- Commit to the color strategy. Restrained, committed, full palette, and drenched are all valid when chosen deliberately.
- Avoid template signals: centered hero plus cards, generic icon-heading-copy grids, repeated tiny uppercase labels, safe beige/slate sameness, and stock-like empty blocks.

## Hard UI Rules

### Accessibility

- Every interactive control has an accessible name.
- Icon-only buttons need `aria-label`; decorative icons are `aria-hidden`.
- Inputs have persistent labels, associated helper text, inline errors, and `aria-invalid` when invalid.
- Use native elements before ARIA.
- Keyboard focus must be visible; no `tabindex` greater than `0`.
- Dialogs trap focus, restore focus to the trigger, and close on Escape.
- Do not rely on hover or color alone.

### Motion

- Default to no animation unless it helps orientation, feedback, loading, reveal, or state transition.
- Use transform and opacity first.
- Do not animate layout properties on large or continuous surfaces.
- Avoid `transition: all`.
- Interaction feedback should usually finish in 120-200ms; larger state changes in 180-300ms.
- Respect `prefers-reduced-motion`.
- Pause looping motion when off-screen.
- Do not mix multiple animation systems in the same component tree.

### Polish Details

- Nested radius should be concentric: outer radius = inner radius + padding.
- Optically align icons, play triangles, and asymmetric shapes.
- Use tabular numbers for metrics, timers, pricing, and changing values.
- Use `text-wrap: balance` on headings and `text-wrap: pretty` on prose when supported.
- Hit areas should be at least 40x40px, 44x44px for touch-first surfaces.
- Keep hover states dimensionally stable.
- Add subtle image outlines where images otherwise bleed into the surface.
- Use shadows for elevation only when elevation communicates hierarchy.

### Layout And Visual System

- Avoid cards as the default answer. Use them when they frame repeated items, tools, or modals.
- Never nest UI cards inside other cards.
- Use stable dimensions for grids, boards, counters, icon buttons, and fixed-format controls.
- Avoid one-note palettes and common AI purple/blue gradient patterns.
- Use one icon family per surface.
- No emoji as UI icons.
- Use real symbols or icons for controls instead of text pills where an icon is familiar.
- Do not use visible in-app text that explains how the UI works unless it is real help content.

## Variants

Use variants when the design direction is uncertain or the user asks to explore:

- Produce 2-3 genuinely different approaches.
- Vary structure, density, typography, color strategy, and motion purpose.
- Do not force temp routes or cleanup workflows unless the project already supports that style of design lab.
- Recommend one option with tradeoffs.

## Review Output

When reviewing or auditing, lead with findings ordered by severity. Use file and line references when possible. For each finding, state:

- Problem
- Why it matters
- Concrete fix

When implementing, finish with the files changed and verification run. If a verification step could not run, say why.
