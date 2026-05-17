# Personal Design Library Roadmap

This repository is now good enough as a focused UI plugin foundation. It is not yet complete as a personal design library. The next phase should make it more personal, visual, and testable.

## Current Assessment

The library currently works best as a design judgment system:

- It distinguishes product UI from brand UI.
- It forces a clear creative direction before coding.
- It includes hard checks for hierarchy, accessibility, responsive layout, motion, and polish.
- It avoids loading too many overlapping third-party rules.

The main missing piece is personal memory: concrete examples, taste preferences, visual references, reusable component decisions, and benchmarks that make future output feel like the same designer is behind it.

## Optimization Priorities

### 1. Add A Personal Taste Profile

Create `docs/taste-profile.md`.

It should capture:

- Preferred typography moods.
- Typical page density.
- Favorite layout moves.
- Color strategies that feel right.
- Color strategies to avoid.
- AI-slop patterns to reject.
- 10-20 reference products, websites, studios, or portfolios.
- Notes on what should feel like "JJinok taste" rather than generic good design.

### 2. Build A Case Library

Create `docs/examples/`.

Suggested first examples:

- `product-dashboard.md`
- `editorial-brand.md`
- `cinematic-landing.md`
- `docs-site.md`
- `mobile-app.md`
- `component-polish.md`

Each case should include:

- Screenshot or local preview path.
- Why it works.
- Reusable techniques.
- What not to copy.
- Which `ui-craft` principles it exercises.

### 3. Add A UI Scoring Rubric

Create `docs/ui-rubric.md`.

Every serious UI generation should be scored on:

- Visual memorability.
- Information hierarchy.
- Product or brand register fit.
- Responsive stability.
- Accessibility.
- Component state coverage.
- Motion purpose.
- Detail polish.
- AI-slop risk.

The rubric should produce a compact score and a fix list.

### 4. Turn Demos Into Benchmarks

The current homepage variants are useful for taste calibration. Extend the benchmark suite:

```text
demos/homepage-variants/
demos/dashboard-variants/
demos/component-variants/
demos/mobile-variants/
demos/docs-site-variants/
```

Each benchmark should include:

- One HTML/CSS/JS implementation.
- Desktop screenshot.
- Mobile screenshot.
- Short design notes.
- Known limitations.

The purpose is not to make production websites. The purpose is to catch whether skill changes make design output better or worse.

### 5. Add Component-Level Rules

The current library is stronger at page-level direction than component-level execution.

Add component guidance for:

- Buttons.
- Inputs.
- Forms.
- Cards.
- Tables.
- Tabs.
- Navigation.
- Dialogs.
- Empty states.
- Error states.
- Loading states.
- Data visualizations.

Each component note should include states, accessibility requirements, spacing, density, and common failure modes.

### 6. Improve Installation And Usage Docs

The README should eventually include:

- How to register or install the local plugin in Codex.
- When to use `ui-craft`.
- When to use `ui-audit`.
- How to open demos.
- How to add a new case study.
- How to run benchmark checks.

### 7. Keep Third-Party Sources As References, Not Dependencies

Do not keep adding more UI skills by default. The library should get better through personal examples and stricter evaluation, not through more prompts.

Recommended rule:

- Add third-party ideas only when they fill a real gap.
- Summarize and transform them.
- Avoid vendoring large databases or broad rule sets unless they are essential and repeatedly useful.

## Next Working Session

Recommended next session sequence:

1. Write `docs/taste-profile.md`.
2. Create `docs/ui-rubric.md`.
3. Turn the three homepage variants into the first benchmark notes.
4. Add one component benchmark, likely buttons or forms.
5. Re-run the plugin validation and visual screenshots.

## Success Criteria

The library becomes "enough" when:

- A new UI request consistently produces output that matches the personal taste profile.
- The same design principles show up across pages and components.
- Codex can self-score its UI work and fix the weakest areas.
- There are enough examples that future designs are guided by memory, not generic categories.
- The repo stays small enough to understand in one sitting.
