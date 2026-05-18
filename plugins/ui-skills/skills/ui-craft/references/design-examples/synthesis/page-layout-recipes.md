# Page Layout Recipes

Use these as starting layouts, not as templates to copy blindly. Pick one, then adapt density, imagery, and interaction to the product.

## 1. Product-First Landing Homepage

Best for SaaS, devtools, AI products, fintech, and productivity products.

Structure:

1. Header with logo, 3-5 nav items, one primary action.
2. First viewport with product name or literal offer as the H1.
3. Supporting copy max 55-65ch.
4. Primary product screenshot, real UI, generated bitmap, or interactive scene visible in the first viewport.
5. A hint of the next proof section visible below the fold.

Layout:

```css
.landing-hero {
  min-height: 92dvh;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  background: var(--surface);
}

.hero-stage {
  display: grid;
  grid-template-columns: minmax(0, 0.82fr) minmax(460px, 1.18fr);
  gap: clamp(32px, 6vw, 88px);
  align-items: center;
  padding: clamp(32px, 7vw, 96px) clamp(20px, 5vw, 72px) 56px;
}

.product-frame {
  aspect-ratio: 16 / 10;
  min-height: 360px;
}

@media (max-width: 900px) {
  .hero-stage {
    grid-template-columns: 1fr;
  }

  .product-frame {
    min-height: 280px;
  }
}
```

Avoid:

- Centered text above a generic cards grid.
- Tiny product preview hidden below the fold.
- Decorative imagery that does not reveal the product, place, object, or state.

## 2. Dense Product Dashboard

Best for admin panels, analytics, trading, CRM, operations, and internal tools.

Structure:

1. Stable app shell.
2. Page title + one primary action.
3. Compact filter/search row.
4. KPI strip with tabular numbers.
5. Main table/chart area.
6. Secondary side panel only if it helps repeated work.

Layout:

```css
.dashboard-page {
  display: grid;
  gap: 20px;
  padding: 24px;
}

.dashboard-header {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 16px;
  align-items: center;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}

.work-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
  gap: 20px;
  align-items: start;
}

@media (max-width: 1100px) {
  .kpi-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .work-grid {
    grid-template-columns: 1fr;
  }
}
```

Rules:

- Use smaller headings than marketing pages.
- Prioritize scan speed over drama.
- Keep controls native and predictable.
- Use skeletons or preserved layout slots for loading states.

## 3. Editorial Brand Homepage

Best for studios, personal sites, research labs, portfolios, books, and cultural products.

Structure:

1. Large typographic signal in the first viewport.
2. One strong image, artifact, or composition.
3. Text measured like an article, not stretched across the page.
4. Content sections with varied rhythm: statement, work list, case detail, closing call.

Layout:

```css
.editorial-home {
  padding-inline: clamp(20px, 5vw, 72px);
}

.editorial-hero {
  min-height: 86dvh;
  display: grid;
  grid-template-columns: minmax(280px, 0.9fr) minmax(0, 1.1fr);
  gap: clamp(32px, 7vw, 96px);
  align-items: end;
  padding-block: 112px 56px;
}

.editorial-title {
  max-width: 11ch;
  font-size: clamp(52px, 11vw, 132px);
  line-height: 0.92;
}

.editorial-copy {
  max-width: 62ch;
}
```

Rules:

- Let the composition have a strong point of view.
- Use a real type pairing, not default UI fonts.
- Avoid overusing uppercase labels and tiny eyebrow text.

## 4. Tool Surface / Editor

Best for canvas tools, design tools, IDE-like products, prompt builders, and creation workflows.

Structure:

1. Command bar at top.
2. Left rail for navigation or assets.
3. Central canvas/work area.
4. Right inspector for properties.
5. Status bar or bottom dock only when it contains real state.

Layout:

```css
.tool-shell {
  display: grid;
  grid-template-columns: 56px 280px minmax(0, 1fr) 320px;
  grid-template-rows: 48px minmax(0, 1fr);
  height: 100dvh;
  overflow: hidden;
}

.command-bar {
  grid-column: 1 / -1;
}

.canvas-area {
  min-width: 0;
  min-height: 0;
  overflow: auto;
}

@media (max-width: 1200px) {
  .tool-shell {
    grid-template-columns: 56px minmax(0, 1fr);
  }

  .secondary-panel,
  .inspector {
    display: none;
  }
}
```

Rules:

- Icon buttons need accessible labels and tooltips.
- Stable dimensions matter more than decorative animation.
- Do not put the canvas inside a decorative card unless the tool itself needs a framed artboard.

## 5. Comparison / Variant Board

Best when showing multiple design directions or pricing/product options.

Structure:

1. A short framing title.
2. 2-4 variants in a single row on desktop.
3. Each variant has a distinct layout, palette, density, and type direction.
4. End with a recommendation and tradeoffs.

Layout:

```css
.variant-board {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.variant-card {
  min-height: 520px;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr) auto;
}

@media (max-width: 980px) {
  .variant-board {
    grid-template-columns: 1fr;
  }
}
```

Rules:

- Variants must differ structurally, not only by color.
- Use real content, not placeholder labels.
- Recommend one option rather than leaving the user with three equal choices.
