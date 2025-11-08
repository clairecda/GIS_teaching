# Install QGIS

Follow these steps to prepare a stable QGIS workspace before Week 1.

## 1. Choose the right build

- **Recommended:** QGIS Long-Term Release (LTR) 3.34.x for stability across the entire course.
- Download links:
  - **macOS (Apple silicon & Intel):** [.dmg installer](https://qgis.org/en/site/forusers/download.html#mac)
  - **Windows:** Standalone installer (64-bit) — select the LTR option.
  - **Linux:** Use the distribution-specific repositories listed on the QGIS site; stick with the LTR channel.
- Avoid unofficial package managers (Homebrew, OSGeo4W) unless you are comfortable troubleshooting.

## 2. Prepare your course workspace

Create a dedicated folder (e.g., `~/Documents/intro-to-gis-course/`) with the following structure:

```
intro-to-gis-course/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── projects/
├── exports/
├── screenshots/
└── notes/
```

- Keep raw downloads read-only; work from copies in `processed/`.
- Store QGIS project files (`.qgz`) in `projects/`.
- Save exported maps (PNG, PDF, SVG) in `exports/`.
- Capture process screenshots for documentation in `screenshots/`.

## 3. Install & verify

1. Run the installer and accept default options.
2. Launch QGIS and confirm the splash screen shows the expected version (e.g., “QGIS 3.34 LTR (Prizren)”).
3. In the main window:
   - Enable the **Browser**, **Layers**, and **Processing Toolbox** panels (`View ▶ Panels`).
   - Switch to **Dark Theme** or a high-contrast theme if preferred (`Settings ▶ Options ▶ General`).
4. Go to `Settings ▶ Options ▶ System` and confirm “Use native file dialogs” is enabled to avoid path quirks.

## 4. First project checklist

- Connect your `data/` folder in the Browser panel by right-clicking **Favourites** ▶ **Add Favourite…**.
- Add a Natural Earth shapefile (e.g., `ne_10m_admin_0_countries.shp`) to the map canvas.
- Save the project as `projects/week01_orientation.qgz` and ensure “Save paths relative to project” is checked (`Project ▶ Properties ▶ General`).
- Open the Attribute Table, sort by population, and confirm you can edit field aliases.

## 5. Troubleshooting tips

- **Installer blocked on macOS:** Control-click the installer ▶ Open to bypass Gatekeeper prompt.
- **Missing menus or icons:** Reset UI via `Settings ▶ Options ▶ System ▶ Reset user interface to default state`.
- **Slow rendering:** Enable rendering simplification (`Settings ▶ Options ▶ Rendering`) and disable antialiasing temporarily.
- **Plugin errors:** Limit plugin installs during Weeks 1–2; re-enable only essential plugins once core workflows are stable.

## 6. Optional enhancements

- Install the **Value Tool** and **QuickMapServices** plugins in Week 3 when directed.
- Configure data source authentication (`Settings ▶ Options ▶ Authentication`) if working with secured services later in the course.
- Set up a version-controlled notes folder (Git or cloud sync) to track reflections and screenshots.

## 7. Support channels

- Course Slack `#qgis-help` (or equivalent) for quick questions.
- Office hours (listed in the syllabus) for screen-share troubleshooting.
- QGIS documentation: <https://docs.qgis.org/> — keep the LTR docs bookmarked.

> Once you can open QGIS, load sample data, and export a simple map, you’re ready for Week 1.
