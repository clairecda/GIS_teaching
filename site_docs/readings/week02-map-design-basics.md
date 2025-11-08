# Map Design Basics

Use these principles throughout the course—especially during Week 2 and Week 11—to create clear, accessible maps.

## Visual hierarchy

- Identify the primary message (e.g., high-risk areas, service coverage). Give it the strongest visual weight (colour, size, contrast).
- Secondary elements (context layers, basemaps) should support the story without overpowering it.
- Use drop shadows sparingly; rely on contrast and layout to emphasise key features.

## Colour

- Choose palettes that match the data type:
  - Sequential for ordered values (light → dark).
  - Diverging for values around a midpoint (negatives vs positives).
  - Qualitative for categorical differences.
- Use reputable palette resources (e.g., [ColorBrewer](https://colorbrewer2.org/)).
- Maintain contrast ≥ 4.5:1 for text and critical features to support low-vision users.
- Avoid red–green pairings unless you test with colour-blind simulators.

## Typography

- Limit to two font families (one for headings, one for body/labels).
- Use clear sans-serif fonts for labels; vary weight or size to show hierarchy.
- Keep point sizes readable: ≥ 10 pt for body text, ≥ 8 pt for tight legends.
- Align text consistently (left or centred) and avoid stretching type.

## Layout

- Follow the layout template guide for margins and grids.
- Group related items (legend + map) and keep whitespace consistent.
- Align elements to gridlines; misalignment creates visual noise.
- Reserve enough space for legends, scale bars, and annotations.

## Accessibility

- Provide alt text for maps when publishing online; describe the main insight and geographic coverage.
- Use patterns or symbols in addition to colour for categorical data when possible.
- Ensure legends are readable (contrast, font size) and located near the map.
- When exporting interactive maps, include tooltips or data tables for screen reader compatibility.

## Export tips

- Export at 300 dpi for print, 150 dpi for digital slides.
- Use vector formats (PDF/SVG) for professional printing or when text must remain crisp.
- Embed fonts if licensing allows; otherwise, convert to outlines before printing.
- Review exports in grayscale to confirm the message holds without colour.

## Recommended references

- Axis Maps: [Cartography Guide](https://www.axismaps.com/guide/)
- Tufte, E. R.: *Envisioning Information*
- Brewer, C. A.: *Designed Maps: A Sourcebook for GIS Users*

Apply these principles iteratively—draft, critique, revise—to build polished outputs for the capstone project.
