# QGIS Toolbar Reference

Use this reference when arranging QGIS panels in Week 1. It lists the core toolbars, icon descriptions, and when to activate them. Convert to a visual graphic later if desired.

## Recommended Layout

- **Top row**: Project, File, Edit, View, Layer, Plugins, Vector, Raster menus.
- **Toolbar arrangement** (left to right):
  1. **Project** (New, Open, Save)
  2. **Map Navigation** (Pan, Zoom In/Out, Zoom Full, Zoom to Layer)
  3. **Attributes** (Identify, Select Features, Select by Polygon/Freehand)
  4. **Digitizing** (Toggle Editing, Add Feature, Move Feature)
  5. **Snapping** (Snapping On/Off, Snapping Options)
  6. **View** (Measure Line/Area, Toggle Overview, Tile Scale)
  7. **Plugins shortcuts** (enable as needed: e.g., Value Tool)

> Drag toolbars using the dotted handle on the left edge. Dock frequently used toolbars on the main bar and collapse less-used ones to the side.

## Icon Cheat Sheet

| Icon | Name | Shortcut | When to use |
| ---- | ---- | -------- | ----------- |
| ![](../assets/icons/new-project.png) | New Project | `Ctrl/Cmd + N` | Start a fresh project file. |
| ![](../assets/icons/open-project.png) | Open Project | `Ctrl/Cmd + O` | Load existing `.qgz` projects. |
| ![](../assets/icons/save-project.png) | Save Project | `Ctrl/Cmd + S` | Save changes frequently. |
| ![](../assets/icons/pan.png) | Pan Map | Space (hold) | Move around the map without changing scale. |
| ![](../assets/icons/zoom-in.png) | Zoom In | Mouse wheel | Focus on a smaller area. |
| ![](../assets/icons/zoom-full.png) | Zoom Full | `Ctrl/Cmd + Shift + F` | Reset view to full layer extent. |
| ![](../assets/icons/identify.png) | Identify Features | `Ctrl/Cmd + Shift + I` | Inspect attribute values by clicking the map. |
| ![](../assets/icons/select-rectangle.png) | Select Features | `Ctrl/Cmd + Shift + R` | Select features for analysis or editing. |
| ![](../assets/icons/toggle-edit.png) | Toggle Editing | `Ctrl/Cmd + E` | Switch a layer into editable mode (displayed pencil icon). |
| ![](../assets/icons/add-feature.png) | Add Feature | `Ctrl/Cmd + Shift + F` | Digitize new points/lines/polygons. |
| ![](../assets/icons/measure-line.png) | Measure Line | `Shift + M` | Get distance between points. |
| ![](../assets/icons/measure-area.png) | Measure Area | `Ctrl/Cmd + Shift + M` | Calculate area of drawn polygon. |
| ![](../assets/icons/render.png) | Render Toggle | `Ctrl/Cmd + R` | Pause map drawing during heavy operations. |
| ![](../assets/icons/plugin-manager.png) | Manage Plugins | None | Install/enable course-required plugins in later weeks. |

> Icon images referenced above should be added to `assets/icons/`. Use PNG files with transparent backgrounds. Replace the placeholders if official icon imagery is added later.

## Tips for Students

- Keep only the toolbars you need to reduce clutter (`View ▶ Toolbars`).
- Customize shortcuts: `Settings ▶ Keyboard Shortcuts`.
- Reset toolbar layout: `Settings ▶ Options ▶ System ▶ Reset user interface`.

## Instructor Suggestions

- Provide a screenshot of the desired layout (export from QGIS) once configured.
- Highlight required toolbars during Week 1 to ensure consistency.
- Revisit this reference in Week 3 when introducing field calculator and editing.
