# Week 1 — QGIS Orientation & Project Setup

## Learning objectives

Learners will be able to:

1. Install QGIS (Long-Term Release recommended) and configure the initial workspace.
2. Navigate the QGIS interface (Browser, Layers, Processing Toolbox, Layout Manager).
3. Load vector and raster layers, inspect attribute tables, and save a project with organised folders.

## Pre-work

- Download QGIS LTR (current recommendation: QGIS 3.34) from [qgis.org](https://qgis.org/en/site/forusers/download.html).
- Create a course workspace folder with subdirectories: `data/`, `projects/`, `exports/`, `screenshots/`.
- Review the QGIS quickstart cheat sheet (`assets/qgis-quickstart.md` — convert to PDF if desired).
- Read the Esri overview and watch the 5-minute intro video linked in `resources/docs/readings/week01-what-is-gis.md`; jot down one insight and one question for discussion.
- Skim `resources/docs/readings/week03-admin-boundaries.md` to familiarise yourself with administrative/statistical boundary concepts before Week 3.
- Tick off the Week 1 items in `resources/docs/data-download-checklist.md` once the Natural Earth datasets are staged under `data/raw/week01/`.

## Session outline (120 minutes)

| Time | Activity | Description | Resources |
| ---- | -------- | ----------- | --------- |
| 0:00–0:15 | Welcome & goals | Introduce course structure, emphasise QGIS-to-Python journey, align expectations. | Slides, syllabus |
| 0:15–0:35 | Guided install check | Walk through install verification, interface tour, customise panels and toolbars. | Live demo |
| 0:35–1:00 | Data import lab | Learners add Natural Earth layers, inspect attribute tables, explore metadata. | Refer to `resources/docs/data-download-guide.md` |
| 1:00–1:20 | Project organisation | Practice saving projects, defining relative paths, staging data folders. | File organisation checklist |
| 1:20–1:40 | Quick map challenge | Style countries by continent and export a PNG; share observations. | Styling reference |
| 1:40–2:00 | Support clinic | Troubleshoot install issues, log follow-up needs for asynchronous support. | Troubleshooting doc |

## Guided exercise highlights

- Use the Browser panel to connect to your local `data/` folder.
- Drag `ne_10m_admin_0_countries.shp` into the map canvas; inspect attributes.
- Configure project CRS to EPSG:4326 and discuss when local projections will be needed later.
- Save the project as `projects/week01_orientation.qgz`, ensuring relative paths are enabled.
- Export the styled map to `exports/week01_country_style.png`.

## Deliverables

- QGIS project file with Natural Earth layers loaded and symbology applied.
- Screenshot or exported map showcasing first styling attempt.
- Reflection entry capturing comfort level with the interface and questions for Week 2.

## Suggested datasets & assets

- Natural Earth Admin 0 & Admin 1 layers.
- Starter geodatabase with sample points (e.g., world cities) for quick joins.
- Toolbar layout reference (`assets/qgis-toolbar-reference.md`, convert to visual when ready).

## Accessibility & inclusion notes

- Provide Windows and macOS-specific install screenshots.
- Highlight keyboard shortcuts and high-contrast icon themes.
- Offer alternative text for screenshots included in guides.

## Looking ahead

- Preview Week 2 focus on symbology, labelling, and layout design.
- Ask learners to bring a map they admire for critique in the next session.
