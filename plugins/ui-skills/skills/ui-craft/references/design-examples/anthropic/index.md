# Anthropic Design Reference

This folder keeps the design-oriented pieces from `anthropics/skills` separate from the main `ui-craft` instructions.

## What Is Included

- `frontend-design.original.md`: the original Anthropic frontend design skill. Use it as the compact "pick a direction and execute it fully" prompt.
- `canvas-design-philosophy.original.md`: static-art philosophy guidance. Use it when a page needs art direction, poster-like composition, or a visual movement before implementation.
- `theme-factory.original.md`: the Anthropic theme workflow. Use it when a user wants to choose from a finished palette/font direction.
- `brand-guidelines.original.md`: Anthropic brand colors and font guidance. Use only when the artifact is intentionally Anthropic-branded.
- `themes/*.md`: concrete theme recipes with palette, typography, and best-use notes.

## How To Use

For blank-page frontend work:

1. Read `frontend-design.original.md`.
2. Pick one concrete aesthetic lane.
3. If the user has no brand direction, skim `themes/` for a palette/font starting point.
4. Combine that direction with the synthesis recipes in `../synthesis/`.

For UI product work:

1. Do not blindly apply the bold frontend-design style.
2. Use its "purpose, tone, constraints, differentiation" checkpoint.
3. Keep the actual product surface familiar, fast, and task-first.

## Notes

The original files are vendored for reference under their upstream license files in this folder. Font binaries from Anthropic's `canvas-design` skill are not vendored here; the synthesis catalog lists useful font directions without adding binary weight to this plugin.
