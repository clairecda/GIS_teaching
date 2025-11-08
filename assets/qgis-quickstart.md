# QGIS Quickstart Cheat Sheet

Use this one-page guide during Week 1 to verify your setup and revisit essential workflows. Convert to PDF for distribution or keep as-is in the repo.

## 1. Launch & Project Setup

- **Open QGIS LTR 3.34** (or course-approved version).
- **Create workspace folders**: `data/`, `projects/`, `exports/`, `screenshots/`.
- **Start new project**: `Project ▶ New`.
- **Set project CRS**: bottom-right status bar ▶ choose `EPSG:4326` (WGS 84) unless told otherwise.
- **Save project**: `Project ▶ Save As…` → `projects/week01_orientation.qgz`, tick “Save paths relative to project”.

## 2. Essential Panels

| Panel | How to toggle | Purpose |
| ----- | ------------- | ------- |
| Browser | `View ▶ Panels ▶ Browser` | Browse local data folders or web services. |
| Layers | `View ▶ Panels ▶ Layers` | Manage layer visibility, order, and grouping. |
| Processing Toolbox | `View ▶ Panels ▶ Processing Toolbox` | Access analysis tools (buffer, dissolve, etc.). |
| Layer Styling | `View ▶ Panels ▶ Layer Styling` | Apply symbology, labels, and formatting quickly. |

> Tip: Arrange Browser on the left, Layers on the right for quick drag-and-drop.

## 3. Add Data

- **Vector files**: Browser panel ▶ navigate to shapefile/GeoPackage ▶ drag into map.
- **CSV with coordinates**: `Layer ▶ Add Layer ▶ Add Delimited Text Layer…` → set X = longitude, Y = latitude, CRS = `EPSG:4326`.
- **Raster files**: Browser ▶ drag GeoTIFF/IMG, or `Layer ▶ Add Layer ▶ Add Raster Layer…`.

## 4. Attribute Table Basics

- Right-click layer ▶ **Open Attribute Table**.
- Use **Select Features** (yellow square) to highlight records.
- **Field Calculator** (abacus icon) for new columns, e.g. `area($geometry)` in metres².
- Toggle edit mode (pencil icon) before modifying attributes.

## 5. Symbology & Labels

1. Select layer ▶ Layer Styling panel.
2. **Symbology tab**:
   - Single symbol for quick fills and outlines.
   - Graduated → choose numeric field + classification (Quantile/Natural Breaks).
   - Categorised → match to text field (e.g. continent).
3. **Labels tab**:
   - Enable Single Labels, select field (e.g. `NAME_EN`).
   - Use **Data defined override** (epsilon icon) for scale-based visibility.

## 6. Export a Map

1. `Project ▶ New Print Layout…` → name (e.g. `week01_quickmap`).
2. In Layout window:
   - Add Map (`Add Item ▶ Add Map`) → draw extent.
   - Add Title, Legend, Scale Bar via `Add Item` menu.
   - Set page size under `Layout ▶ Page Setup`.
3. Export via `Layout ▶ Export as PNG/PDF/SVG` to `exports/`.

## 7. Keyboard Shortcuts

- `Ctrl/Cmd + L` — Open Data Source Manager.
- `Ctrl/Cmd + Shift + F` — Toggle full screen.
- `Ctrl/Cmd + P` — Open Print Layout manager.
- `Ctrl/Cmd + 1/2/3` — Switch between Map/List/Table views in Attribute Table.
- Space bar — Temporarily pan when digitising.

Adjust shortcuts under `Settings ▶ Keyboard Shortcuts`.

## 8. Quick Troubleshooting

| Issue | Fix |
| ----- | ---- |
| Missing panels | `View ▶ Panels` to re-enable; reset UI via `Settings ▶ Options ▶ System ▶ Reset`. |
| Slow performance | Toggle **Render** button (top toolbar) off during complex styling; enable geometry simplification (`Settings ▶ Options ▶ Rendering`). |
| CRS mismatch | Check layer CRS via right-click ▶ Properties ▶ Source; reproject using `Vector ▶ Data Management Tools ▶ Reproject Layer`. |
| Plugin errors | Disable non-essential plugins under `Plugins ▶ Manage and Install Plugins…`. |

## 9. Useful Resources

- QGIS Training Manual: <https://docs.qgis.org/3.34/en/docs/training_manual/>
- Keyboard shortcut reference: `Help ▶ Keyboard Shortcuts Reference`
- Course-specific guides: `resources/docs/qgis-onboarding.md`, `resources/docs/data-download-guide.md`

Keep this cheat sheet nearby during Week 1–2 labs to reinforce muscle memory.
