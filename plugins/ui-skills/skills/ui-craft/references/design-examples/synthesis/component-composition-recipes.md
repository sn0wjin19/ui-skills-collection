# Component Composition Recipes

Use these when a page feels correct at the concept level but weak at the component level.

## Buttons

Rules:

- One primary action per view or panel.
- Minimum hit area: 40x40px desktop, 44x44px touch-first.
- Icon-only buttons need `aria-label` and tooltip.
- Press state should be subtle: `scale(0.96)` is enough.
- Hover and active states must not change layout dimensions.

Example:

```css
.button {
  min-height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-radius: 10px;
  padding: 0 14px;
  transition-property: transform, background-color, color, box-shadow;
  transition-duration: 160ms;
  transition-timing-function: cubic-bezier(0.2, 0, 0, 1);
}

.button:active {
  transform: scale(0.96);
}
```

## Cards And Panels

Use cards for repeated items, tools, modals, and bounded content. Do not use cards as the default page section.

Recipe:

- Outer radius: 16-24px for marketing, 8-12px for product UI.
- Inner controls: radius should be outer radius minus padding, optically adjusted.
- Padding: 16px dense, 20-24px normal, 32px brand/editorial.
- Use subtle shadows for elevation, borders for containment, not both at full strength.

```css
.panel {
  border-radius: 14px;
  padding: 20px;
  background: var(--panel);
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.06),
    0 12px 32px rgba(0, 0, 0, 0.06);
}

.panel > .inner-control {
  border-radius: 10px;
}
```

## Forms

Hierarchy:

1. Label
2. Input
3. Helper text
4. Error

Rules:

- Labels are persistent. Do not rely only on placeholder text.
- Helper text and errors should not shift nearby layout unexpectedly.
- Group related fields with smaller gaps and sections with larger gaps.
- Use clear focus rings and `aria-invalid` for invalid fields.

```css
.field {
  display: grid;
  gap: 6px;
}

.form-grid {
  display: grid;
  gap: 18px;
}

.field-group {
  display: grid;
  gap: 12px;
}
```

## Metrics

Rules:

- Use tabular numbers.
- Keep units visually quieter than values.
- Show trend, timeframe, and status if the metric drives action.
- Avoid changing card sizes when values update.

```css
.metric-value {
  font-variant-numeric: tabular-nums;
  font-size: 32px;
  line-height: 1;
  letter-spacing: 0;
}

.metric-unit {
  font-size: 0.48em;
  color: var(--muted);
}
```

## Tables

Rules:

- Dense tables need strong alignment and quiet typography, not oversized cards.
- Keep row height stable.
- Use sticky headers when scrolling long datasets.
- Align text left, numbers right or decimal-aligned, actions right.
- Truncate secondary text intentionally and expose full text on hover/focus if needed.

```css
.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-variant-numeric: tabular-nums;
}

.data-table th {
  position: sticky;
  top: 0;
  z-index: 1;
  background: var(--surface);
  text-align: left;
}

.data-table td,
.data-table th {
  height: 44px;
  padding: 0 12px;
}

.data-table .number {
  text-align: right;
}
```

## Navigation

Rules:

- Current state must be visually stronger than available states.
- Disabled state must not look like current state.
- Use familiar patterns for product navigation.
- Marketing navigation should stay quiet unless the brand itself calls for expressive nav.

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 40px;
  border-radius: 8px;
  padding: 0 10px;
  color: var(--muted);
}

.nav-item[aria-current="page"] {
  color: var(--foreground);
  background: var(--selected);
}
```

## Empty, Loading, Error

Rules:

- Empty states should explain the next action, not the whole product.
- Loading states preserve layout shape.
- Errors should name what failed and offer recovery.

```css
.skeleton {
  border-radius: 8px;
  background:
    linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent),
    var(--skeleton);
  background-size: 200% 100%, 100% 100%;
  animation: shimmer 1.2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .skeleton {
    animation: none;
  }
}
```
