# Typography And Layout Recipes

Use this when the user asks for concrete font, type scale, spacing, or layout examples, or when starting a page without an existing design system.

## Typeface Selection

Choose type by product register first.

| Register | Display / headings | Body / UI | Mono / data | Use when |
| --- | --- | --- | --- | --- |
| Product SaaS | Geist Sans, Instrument Sans, IBM Plex Sans | Same family or system UI | JetBrains Mono, IBM Plex Mono | Dashboards, admin tools, B2B workflows |
| Technical console | Tektur, Red Hat Mono, IBM Plex Sans | IBM Plex Sans, Work Sans | JetBrains Mono, Geist Mono | Devtools, AI infrastructure, data products |
| Editorial premium | Gloock, Instrument Serif, Libre Baskerville | Lora, Crimson Pro, Instrument Sans | Geist Mono | Publishing, essays, portfolio, research |
| Retail / lifestyle | Bricolage Grotesque, Outfit, Young Serif | Work Sans, Instrument Sans | DM Mono | Product launches, creator tools, commerce |
| Experimental / event | Big Shoulders, Boldonse, Silkscreen, Jura | National Park, Outfit | Red Hat Mono | Campaigns, posters, festival, music, gaming |

Rules:

- Use one family for dense product UI unless brand value clearly improves with a display face.
- Pair one expressive face with one quiet face. Avoid two expressive fonts fighting.
- Keep labels and metadata plain. Let the headline or hero carry the character.
- If a custom font is used, set `font-display: swap` and define fallbacks.
- For code-heavy UI, enable disambiguation when available and use `slashed-zero`.

Example CSS:

```css
:root {
  --font-ui: "Instrument Sans", ui-sans-serif, system-ui, sans-serif;
  --font-display: "Gloock", Georgia, serif;
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, monospace;
}

html {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-synthesis: none;
}

.metric,
.price,
.timer {
  font-variant-numeric: tabular-nums;
}

.code {
  font-variant-numeric: tabular-nums slashed-zero;
  font-feature-settings: "zero" 1, "ss02" 1;
}
```

## Type Scales

Use the existing project tokens first. If none exist, start from one of these.

### Compact Product Scale

For SaaS, dashboards, settings, tables, and repeat workflows.

| Token | Size | Line height | Weight | Use |
| --- | ---: | ---: | ---: | --- |
| `caption` | 12px | 16px | 500 | Metadata, helper labels |
| `body-sm` | 14px | 20px | 400 | Table cells, dense descriptions |
| `body` | 16px | 24px | 400 | Default readable text |
| `title-sm` | 18px | 24px | 600 | Card and panel titles |
| `title` | 22px | 28px | 650 | Page section titles |
| `h1` | 30px | 36px | 700 | App page title |

Use this scale with a 4px or 8px spacing base. Keep line length around 45-65 characters for descriptions.

### Brand / Landing Scale

For first-view marketing, product launches, and portfolio pages.

| Token | Size | Line height | Weight | Use |
| --- | ---: | ---: | ---: | --- |
| `eyebrow` | 12px | 16px | 650 | Short category label, uppercase only with tracking |
| `body` | 17px | 28px | 400 | Supporting copy |
| `lead` | 20px | 32px | 400 | Hero subcopy |
| `h2` | 40px | 46px | 650 | Section title |
| `h1` | 64px | 68px | 700 | Hero headline |
| `display` | 88px | 88px | 700 | Only for a true hero or campaign moment |

Clamp large sizes on mobile. Do not use viewport-width font scaling directly.

```css
.hero-title {
  font-size: clamp(44px, 8vw, 88px);
  line-height: 0.98;
  letter-spacing: 0;
  text-wrap: balance;
}

.lead {
  max-width: 58ch;
  font-size: clamp(17px, 2vw, 20px);
  line-height: 1.55;
  text-wrap: pretty;
}
```

### Editorial Reading Scale

For essays, research notes, articles, documentation, and case studies.

| Token | Size | Line height | Use |
| --- | ---: | ---: | --- |
| `body` | 18px | 31px | Main prose |
| `small` | 14px | 22px | Captions and footnotes |
| `h2` | 34px | 40px | Article section heading |
| `h1` | 52px | 58px | Article title |

Keep prose at 55-70 characters per line.

```css
.article {
  max-width: 68ch;
  font-size: 18px;
  line-height: 1.72;
}

.article h1,
.article h2 {
  text-wrap: balance;
}

.article p {
  text-wrap: pretty;
}
```

## Spacing Scales

Default to an 8px scale:

| Token | Value | Use |
| --- | ---: | --- |
| `2xs` | 2px | Hairline offsets, optical nudges |
| `xs` | 4px | Icon/text gap inside dense controls |
| `sm` | 8px | Inline gaps, tight stacks |
| `md` | 16px | Component padding, form field gaps |
| `lg` | 24px | Card padding, group gaps |
| `xl` | 32px | Section internal rhythm |
| `2xl` | 48px | Related section spacing |
| `3xl` | 64px | Major page bands |
| `4xl` | 96px | Landing-page section separation |

Rules:

- Related elements sit close. Unrelated groups get a larger gap.
- Internal component padding should usually be one step smaller than the external gap around it.
- Card radius should be concentric: outer radius = inner radius + padding.
- Hover, active, focus, and loading states must not resize the layout.

## Grid Recipes

### Product App Grid

Use for dashboards and operational tools.

```css
.app-shell {
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr);
  min-height: 100dvh;
}

.content {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 24px;
  padding: 24px;
}

@media (max-width: 900px) {
  .app-shell {
    grid-template-columns: 1fr;
  }

  .content {
    grid-template-columns: 1fr;
    padding: 16px;
  }
}
```

### Marketing Page Grid

Use for brand pages where composition matters more than dense controls.

```css
.page-band {
  padding-inline: clamp(20px, 5vw, 72px);
}

.page-inner {
  width: min(100%, 1180px);
  margin-inline: auto;
}

.hero {
  min-height: min(760px, 92dvh);
  display: grid;
  align-items: end;
  padding-block: 96px 56px;
}

.hero-copy {
  max-width: 760px;
}
```

### Editorial Grid

Use for case studies or content-led homepages.

```css
.editorial-layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 68ch) minmax(0, 1fr);
  column-gap: clamp(20px, 5vw, 80px);
}

.article-body {
  grid-column: 2;
}

.side-note {
  grid-column: 3;
  max-width: 28ch;
}

@media (max-width: 900px) {
  .editorial-layout,
  .article-body,
  .side-note {
    display: block;
  }
}
```
