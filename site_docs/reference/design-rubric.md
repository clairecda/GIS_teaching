# Map Design Principles

This guide introduces graphic design fundamentals that make maps effective. The same principles used in magazines, websites, and professional publications apply to cartography.

---

## Why design matters

A map isn't just data—it's a **visual argument**. Good design helps your audience:

- Understand the message quickly
- Know where to look first
- Trust the information
- Remember the key points

Bad design creates confusion, even when the analysis is excellent.

---

## The grid system

Professional designers don't place elements randomly. They use an invisible **grid** to create order and alignment.

### How grids work

Elements snap to column boundaries:

| Element | Columns | Width |
|---------|---------|-------|
| **Title** | 1–9 | 75% of page |
| **Main map** | 1–8 | 67% of page |
| **Legend** | 9–11 | 25% of page |
| **Credits** | 1–12 | Full width |

In this example:
- **Title** spans 9 of 12 columns
- **Map** takes 8 columns (2/3 of the page)
- **Legend** takes 3 columns (1/4 of the page)
- **Credits** span the full width

**Magazine example:** Open any magazine. Notice how headlines, images, and text align to invisible vertical lines. That's a grid.

**For maps:** Use a 12-column grid. Elements snap to column edges, creating visual order even when viewers don't consciously notice it.

### Gutters

The spaces between columns are called **gutters**. They prevent elements from touching and give the eye room to move.

- Standard gutter: 5mm
- Larger gutters (10mm) for more breathing room

---

## Visual hierarchy

**Hierarchy** controls what viewers see first, second, third. Without it, everything competes for attention.

### The tools of hierarchy

| Tool | How it works | Map example |
|------|--------------|-------------|
| **Size** | Larger = more important | Title bigger than legend text |
| **Color** | Bright/saturated = attention | Red for key features, grey for context |
| **Position** | Top-left gets read first | Title at top, credits at bottom |
| **Contrast** | High contrast = focal point | Dark text on light background |
| **Isolation** | Surrounded by space = important | Main map has margins around it |

### The squint test

**Squint at your map.** What do you see?

- The blurry shapes that stand out are your visual hierarchy
- If everything blurs together equally, you have no hierarchy
- If the wrong thing stands out, adjust size/color/position

---

## Balance

A balanced layout feels stable. An unbalanced layout feels uncomfortable (even if viewers can't say why).

### Symmetrical vs asymmetrical

=== "Symmetrical"

    | Left | Center | Right |
    |:----:|:------:|:-----:|
    | | 🗺️ MAP | |
    | | Legend | |

    Everything centered on the page. Simple but static.

=== "Asymmetrical"

    | Map Area (2/3) | Legend (1/3) |
    |:--------------:|:------------:|
    | 🗺️ MAP | Legend |

    Heavier on left, balanced by legend on right. More dynamic and professional.

**Asymmetrical balance** is more dynamic and professional. Balance a large element (map) with smaller elements (legend, title) on the opposite side.

### Visual weight

Different elements have different "weights":

- Large elements are heavy
- Dark elements are heavier than light
- Complex/detailed areas feel heavier than simple areas
- Isolation makes elements feel heavier

**Balance the weights** across your page.

---

## Negative space (white space)

**Negative space** is the empty area around and between elements. Beginners fill every inch; professionals use emptiness strategically.

### What negative space does

- **Separates elements** without needing boxes or lines
- **Creates breathing room** so the eye can rest
- **Emphasizes importance** — isolation draws attention
- **Improves readability** — text needs margins

### Common mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Filling every corner | Feels cluttered, overwhelming | Remove or shrink non-essential elements |
| Legend touching map | Elements compete | Add 10mm margin between |
| Text to edge | Feels cramped | Maintain 15mm page margins |
| Equal spacing everywhere | Nothing stands out | Vary spacing to group related items |

### The "remove one thing" rule

When your layout feels done, **remove one element**. If the map still works, leave it out. Repeat until removing anything would hurt the message.

---

## Alignment

Elements that align feel intentional. Elements that *almost* align feel like mistakes.

=== "Bad (ragged)"

    | Element | Position |
    |---------|----------|
    | Title | slightly left |
    | Map | center-ish |
    | Legend | far right |
    | Scale bar | left of center |
    | Credits | random indent |

    Left edges don't line up — looks accidental.

=== "Good (aligned)"

    | Element | Position |
    |---------|----------|
    | Title | left edge |
    | Map | left edge |
    | Legend | left edge |
    | Scale bar | left edge |
    | Credits | left edge |

    Everything aligns to the same edge — looks intentional.

**Rule:** Pick alignment edges and stick to them. In QGIS, use guides or a grid.

---

## Contrast and color

### Contrast for readability

Text needs **contrast ratio of 4.5:1 or higher** against its background.

| Good contrast | Poor contrast |
|---------------|---------------|
| Black on white | Grey on white |
| White on dark blue | Yellow on white |
| Dark text on light map | Light text on busy map |

**Test:** If you squint and the text disappears into the background, contrast is too low.

### Color for meaning

Colors aren't decoration—they carry meaning:

| Color use | Purpose |
|-----------|---------|
| **Sequential** (light→dark) | Ordered data (low→high) |
| **Diverging** (red←white→blue) | Data with meaningful center |
| **Categorical** (distinct hues) | Different types (no order) |

**Limit colors:** 3-5 colors maximum. More creates visual noise.

---

## Putting it together

Good map design uses all these principles:

| Row | Left (2/3) | Right (1/3) |
|-----|------------|-------------|
| **Top** | 📰 TITLE — Large, high contrast | |
| **Middle** | 🗺️ MAIN MAP | 📋 LEGEND<br/>📏 Scale bar |
| **Bottom** | Data: ABS 2021 \| CRS: EPSG:7856 \| Author: Your Name | |

| Principle | How it's applied |
|-----------|------------------|
| **Hierarchy** | Title is largest, at top position |
| **Balance** | Large map balanced by legend column |
| **Alignment** | All elements snap to grid columns |
| **Negative space** | Margins around edges, gutters between elements |
| **Grid** | 3-column structure, credits span full width |

---

## Design critique rubric

Use this during peer feedback sessions:

### 1. Clarity (Is the message clear?)

| Score | Description |
|-------|-------------|
| **4** | Message clear within 5 seconds |
| **3** | Message clear after 10-15 seconds |
| **2** | Requires explanation to understand |
| **1** | Unclear even with explanation |

### 2. Visual hierarchy (Do you know where to look?)

| Score | Description |
|-------|-------------|
| **4** | Clear focal point, eye moves naturally |
| **3** | Mostly clear, minor competing elements |
| **2** | Multiple elements compete for attention |
| **1** | No clear hierarchy, chaotic |

### 3. Technical accuracy

| Score | Description |
|-------|-------------|
| **4** | All labels correct, sources cited, scale accurate |
| **3** | Minor issues that don't affect interpretation |
| **2** | Notable errors causing confusion |
| **1** | Major errors undermining credibility |

### 4. Accessibility

| Score | Description |
|-------|-------------|
| **4** | Works for colorblind viewers, good contrast, readable fonts |
| **3** | Minor accessibility issues |
| **2** | Some categories indistinguishable, text too small |
| **1** | Major barriers, unusable for many viewers |

### Giving feedback

1. **What works:** "The graduated color scheme makes density patterns immediately clear."
2. **What could improve:** "The legend overlaps part of the study area."
3. **Suggestion:** "Move the legend to the empty ocean area in the lower right."

---

## Further reading

- [Cartography Guide](https://www.axismaps.com/guide) — Axis Maps
- [ColorBrewer](https://colorbrewer2.org/) — Color schemes for maps
- [Butterick's Practical Typography](https://practicaltypography.com/) — Typography basics
