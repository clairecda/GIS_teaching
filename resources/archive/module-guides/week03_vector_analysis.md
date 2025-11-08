# Week 3 — Vector Analysis & Attribute Joins

## Learning objectives

Learners will be able to:

1. Explain the role of administrative and statistical boundaries in socio-economic analysis.
2. Perform attribute joins between polygon boundaries (e.g., SA2/LGA) and tabular datasets (e.g., SEIFA, ACS).
3. Use the Field Calculator and selection tools to create derived indicators.

## Pre-work

- Review `resources/docs/readings/week03-admin-boundaries.md` to understand why boundaries differ and how they are used.
- Download boundary + indicator datasets listed in `resources/docs/data-download-guide.md` (ASGS SA2 + SEIFA for Australia, or local equivalents). Confirm items in the checklist are ticked.
- Bring at least one question about boundary changes or data comparability to the session.

## Session outline (120 minutes)

| Time | Activity | Description | Resources |
| ---- | -------- | ----------- | --------- |
| 0:00–0:15 | Boundary deep dive | Facilitator reviews boundary hierarchy (ADM0–ADM2, statistical vs political) with local examples. | Slides referencing `resources/docs/readings/week03-admin-boundaries.md` |
| 0:15–0:45 | Join workflow demo | Walk through joining SA2 shapefile to SEIFA table; highlight common pitfalls (mismatched IDs, projections). | Live QGIS demo |
| 0:45–1:15 | Guided exercise | Learners replicate join with their chosen dataset; use Field Calculator to compute rates or categories. | Worksheet checklist |
| 1:15–1:35 | Interpretation & storytelling | Discuss why different boundary choices change the story. Compare SA2 vs LGA vs custom geographies. | Group discussion |
| 1:35–2:00 | Troubleshooting clinic | Address join errors, missing data, or boundary updates. | Troubleshooting doc |

## Guided exercise highlights

- Inspect boundary metadata (`Layer ▶ Properties ▶ Information`) to verify CRS and vintage.
- Use `Layer ▶ Add Layer ▶ Add Delimited Text Layer…` to load SEIFA CSV (if not already cleaned).
- Join via `Layer ▶ Properties ▶ Joins ▶ Add…`, selecting `SA2_CODE_2021` (or your local equivalent).
- After joining, open the attribute table to confirm numeric fields are available (convert text to numbers if needed).
- Create derived metrics: e.g., `seifa_decile * 10` to create a score or normalise counts by population.
- Use selections to focus on specific regions (e.g., filter to Greater Sydney SA2s).

## Discussion prompts

- How do boundary choices affect the story you tell? (e.g., SA2 vs LGA vs postcode)
- What happens when boundaries change between census releases? How will you document this?
- Which boundary level makes sense for your capstone ideas?

## Deliverables

- Joined boundary layer saved as GeoPackage (e.g., `data/processed/week03/sa2_seifa.gpkg`).
- Short reflection summarising one insight and one open question (use `resources/docs/reflections/week03.md`).

## Suggested datasets & assets

- ABS ASGS SA2 shapefile and SEIFA CSV (or local equivalents listed in the data inventory).
- Cheatsheet summarising join steps (to be created).
- Before/after map snapshots showing impact of different boundary levels.

## Accessibility & inclusion notes

- Provide definitions for unfamiliar boundary terms during the boundary deep dive.
- Offer printed or screen-reader accessible metadata extracts where possible.
- Encourage learners to explore boundaries relevant to their community to build engagement.

## Looking ahead

- Preview Week 4 focus on raster overlays and terrain analysis.
- Ask learners to consider which boundary level they might use for the Week 5 crime case study.
