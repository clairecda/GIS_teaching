# QGIS Quickstart Cheat Sheet

Use this page during Week 1 to verify your setup and revisit essential workflows throughout the course.

## Launch & project setup

- Open QGIS LTR 3.34.x (course-approved version).
- Create workspace folders: `data/`, `projects/`, `exports/`, `screenshots/`, `notes/`.
- Start a new project (`Project ▶ New`) and set the project CRS to `EPSG:4326` unless instructed otherwise.
- Save the project as `projects/week01_orientation.qgz`, ensuring **Save paths relative to project** is checked.

## Essential panels

| Panel | Toggle | Purpose |
| ----- | ------ | ------- |
| Browser | `View ▶ Panels ▶ Browser` | Browse local folders or services. |
| Layers | `View ▶ Panels ▶ Layers` | Manage layer order and visibility. |
| Processing Toolbox | `View ▶ Panels ▶ Processing Toolbox` | Access geoprocessing tools. |
| Layer Styling | `View ▶ Panels ▶ Layer Styling` | Apply symbology, labels, formatting. |

> Arrange Browser on the left and Layers on the right for quick drag-and-drop.

## Add data

- **Vector:** Drag shapefile/GeoPackage from Browser onto the map.
- **CSV with coordinates:** `Layer ▶ Add Layer ▶ Add Delimited Text Layer…` → set X = longitude, Y = latitude, CRS = `EPSG:4326`.
- **Raster:** `Layer ▶ Add Layer ▶ Add Raster Layer…` or drag GeoTIFFs directly.

## Attribute table essentials

- Right-click a layer → **Open Attribute Table**.
- Use **Select Features** to highlight records.
- **Field Calculator** adds new columns (e.g., `area($geometry)`).
- Toggle editing (pencil icon) before modifying attributes.

## Symbology & labels

1. Select a layer and open **Layer Styling**.
2. **Symbology:** choose Single, Graduated (numeric), or Categorised (text).
3. **Labels:** enable Single Labels, choose attribute, use data-defined overrides for scale-based visibility.

## Export a map layout

1. `Project ▶ New Print Layout…` → name it.
2. Add map frame, title, legend, scale bar via the **Add Item** menu.
3. Export as PNG/PDF/SVG to the `exports/` folder.

## Keyboard shortcuts

- `Ctrl/Cmd + L` — Open Data Source Manager.
- `Ctrl/Cmd + Shift + F` — Toggle full screen.
- `Ctrl/Cmd + P` — Print Layout manager.
- `Ctrl/Cmd + 1/2/3` — Map/List/Table views in Attribute Table.
- Hold Space — Temporarily pan when digitising.

Adjust shortcuts via `Settings ▶ Keyboard Shortcuts`.

## Troubleshooting quick fixes

| Issue | Solution |
| ----- | -------- |
| Missing panels | Re-enable under `View ▶ Panels`, or reset UI (`Settings ▶ Options ▶ System ▶ Reset`). |
| Slow rendering | Pause rendering (Render toggle button) or enable simplification (`Settings ▶ Options ▶ Rendering`). |
| CRS mismatch | Check layer CRS (`Layer ▶ Properties ▶ Source`); reproject with `Vector ▶ Data Management Tools ▶ Reproject Layer`. |
| Plugin errors | Disable non-essential plugins until core workflows are stable. |

## Useful links

- QGIS Training Manual: <https://docs.qgis.org/latest/en/docs/training_manual/>
- Keyboard shortcuts reference: `Help ▶ Keyboard Shortcuts Reference`
- Course onboarding: [Install QGIS](../onboarding/qgis-install.md), [Downloading datasets](../onboarding/data-downloads.md)
