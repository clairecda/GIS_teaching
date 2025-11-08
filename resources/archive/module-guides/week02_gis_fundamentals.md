# Week 2 — QGIS Symbology, Labelling & Layouts

## Learning objectives

Learners will be able to:

1. Apply graduated, categorised, and rule-based symbology to vector layers to communicate spatial patterns.
2. Configure labels with data-driven styling and expression-based rules.
3. Design an export-ready layout that follows basic cartographic design principles (hierarchy, balance, accessibility).

## Pre-work

- Reopen the Week 1 project and ensure Natural Earth layers are accessible.
- Collect an inspirational map to share (digital or printed) and note one design element you appreciate.
- Skim introductory reading on colour theory and map accessibility (see `resources/docs/readings/week02-map-design-basics.md`).
- Download the thematic datasets listed in `resources/docs/data-download-guide.md` (Our World in Data renewable energy, world cities) and stage them under `data/raw/week02/`.
- Update `resources/docs/data-download-checklist.md` for Week 2 once downloads are complete.

## Session outline (120 minutes)

| Time | Activity | Description | Resources |
| ---- | -------- | ----------- | --------- |
| 0:00–0:15 | Design show-and-tell | Learners present selected maps; facilitators highlight design vocabulary. | Sample map deck |
| 0:15–0:45 | Symbology deep dive | Demonstrate single vs. graduated symbology, blending modes, symbol levels. | Live demo project |
| 0:45–1:05 | Labelling lab | Build expression-based labels (e.g., major city names) with scale-dependent visibility. | Expression cheat sheet |
| 1:05–1:35 | Layout workshop | Assemble layout with title, legend, scale bar, inset map, and branding. | Layout template |
| 1:35–1:50 | Accessibility checklist | Review colour contrast, typography, and export formats (PNG, PDF, SVG). | Accessibility checklist |
| 1:50–2:00 | Reflection & preview | Document takeaways; preview Week 3 vector analysis tools. | `resources/docs/reflections/week02.md` |

## Guided exercise highlights

- Style countries by population class using Natural Earth attributes; adjust class breaks manually.
- Use the Layer Properties ▶ Labels panel to display capital names, applying a scale-based expression to hide labels below 1:20M.
- Configure Print Layout with custom page size, add inset showing zoomed region, and embed a logo placeholder.
- Export final layout to `exports/week02_layout.pdf` and `exports/week02_layout.png`.

## Deliverables

- Updated QGIS project featuring advanced symbology and labelling.
- Exported map layout ready for critique.
- Reflection log capturing design choices and questions for spatial analysis tools.

## Suggested datasets & assets

- Natural Earth capitals layer for labelling.
- Optional CSV of thematic data (e.g., freedom scores) to practice joins and custom symbology.
- Layout template guide (`assets/layout-template.md`) and grid reference (convert to diagram as needed).

## Accessibility & inclusion notes

- Encourage the use of colour-blind friendly palettes (ColorBrewer subsets).
- Provide font alternatives that support extended character sets.
- Demonstrate how to export vector formats for screen readers and maintain alt text in documentation.

## Looking ahead

- Introduce field calculator expressions and attribute management in Week 3.
- Invite learners to identify a dataset tied to their domain for future styling practice.
