---
name: ui-audit
description: Use when reviewing, critiquing, or fixing an existing frontend UI for visual quality, accessibility, responsive behavior, metadata, motion performance, interaction states, typography, spacing, hierarchy, and polish.
license: MIT
---

# UI Audit

Audit existing UI with a code-review stance. Findings first, ordered by severity, with file and line references.

## Scope

Use this skill for:

- UI code review.
- Design QA.
- Accessibility review.
- Motion performance review.
- Responsive behavior review.
- Metadata and share-preview checks for public pages.
- Final polish before shipping.

## Audit Order

1. Critical usability and accessibility:
   - Missing accessible names, broken keyboard access, focus traps, hidden labels, bad error association.
2. Layout and responsive failures:
   - Overlap, clipping, mobile horizontal scroll, unstable hover states, fixed heights that break mobile.
3. Interaction states:
   - Missing loading, empty, error, disabled, focus, active, selected, and success states.
4. Visual hierarchy:
   - Weak primary action, flat type scale, bad density, unclear grouping, overused cards.
5. Motion and performance:
   - Layout animation, scroll polling, unbounded loops, large blur/filter animation, `transition: all`.
6. Design polish:
   - Non-concentric radius, awkward optical alignment, inconsistent icons, non-tabular numbers, poor text wrapping.
7. Metadata for public pages:
   - Missing title/description/canonical/OG image, duplicate tags, unstable or localhost share URLs.

## Output Format

Lead with findings. Keep each finding actionable:

```text
[P1] Short title
File: path:line
Problem: ...
Why it matters: ...
Fix: ...
```

If no issues are found, say that clearly and list the verification gaps or residual risk.

## Fixing

If the user asked for fixes, patch only the lines needed for the issue. Do not redesign unrelated areas. After fixing, rerun the smallest meaningful checks available.
