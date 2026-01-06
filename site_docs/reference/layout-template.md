# Layout Template Guide

This guide teaches you to create professional map layouts in QGIS and save them as reusable templates. You'll learn the exact steps to build a layout once, then use it for every map you make.

---

## What is a layout template?

A **layout template** (`.qpt` file) saves your page setup, placeholders, and design elements—but not your map data. Think of it like a magazine template: the grid, fonts, and positions are set, but new content goes in each issue.

**Benefits of templates:**
- Consistent look across all your maps
- Faster production (no rebuilding from scratch)
- Professional appearance
- Forces good design habits

---

## Part 1: Creating a new layout

### Step 1: Open the Layout Manager

1. In QGIS, go to **Project → Layout Manager**
2. Click **Create...** (or the blank page icon)
3. Name your layout descriptively: `A3_Landscape_Template`
4. Click **OK**

A new window opens—this is the **Print Layout** editor.

### Step 2: Set page size and orientation

1. Right-click on the blank page → **Page Properties**
   - Or: **Layout → Page Setup**
2. In the **Item Properties** panel (right side), set:
   - **Size:** A3 (or A4 for smaller prints)
   - **Orientation:** Landscape
3. Your page dimensions appear: A3 landscape = 420 × 297 mm

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                      │
│                         420 mm                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │                                                                 │ │
│  │                                                                 │ │
│  │                      Your layout area                          │ 297 mm
│  │                                                                 │ │
│  │                                                                 │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Part 2: Setting up guides and margins

Guides create invisible alignment lines. Professional designers never place elements randomly—they snap to guides.

### Step 3: Add margin guides

1. Go to **View → Manage Guides**
2. Click **Add guides from page margins**
3. Set margins:
   - **Top:** 15 mm
   - **Bottom:** 20 mm (extra space for credits)
   - **Left:** 15 mm
   - **Right:** 15 mm
4. Click **Apply**

You'll see dashed lines marking your safe area.

### Step 4: Add column guides (optional but recommended)

For a 12-column grid (professional standard):

1. In **Manage Guides**, add vertical guides at these positions:
   - Every 32.5 mm from the left margin (for A3)
   - Or calculate: (420 - 30) ÷ 12 = 32.5 mm per column

**Simpler approach:** Add guides at key positions:
- 1/3 page: 140 mm from left
- 2/3 page: 280 mm from left

2. Enable **View → Show Guides** and **View → Snap to Guides**

```
    15mm   ┊        ┊        ┊        ┊   15mm
     │     ┊        ┊        ┊        ┊     │
     ▼     ▼        ▼        ▼        ▼     ▼
┌────┬─────────────┬────────────────┬──────────┐
│    │             │                │          │
│    │             │                │          │
│    │    MAP      │      MAP       │  LEGEND  │
│    │   FRAME     │     FRAME      │   AREA   │
│    │             │                │          │
│    │             │                │          │
├────┴─────────────┴────────────────┴──────────┤
│              CREDITS FOOTER                   │
└───────────────────────────────────────────────┘
       ↑                                    ↑
    Left guide                         Right guide
```

---

## Part 3: Adding layout elements

Now add the components that appear on every map.

### Step 5: Add the main map frame

1. Click **Add Item → Add Map** (or the map icon in toolbar)
2. Draw a rectangle in the main area of your layout
3. Position it precisely in **Item Properties**:
   - **Position and size:**
     - X: 15 mm (left margin)
     - Y: 15 mm (top margin)
     - Width: 280 mm (leaves room for legend)
     - Height: 247 mm (accounts for top/bottom margins)

4. Set map behaviour:
   - Check **Lock layers** if you want specific layers visible
   - Check **Lock styles** to preserve symbology
   - Leave unchecked for flexible reuse

**Tip:** For templates, leave the map unlocked. When you reuse the template, click **Set Map Extent to Match Main Canvas** to show your current project.

### Step 6: Add a legend

1. Click **Add Item → Add Legend**
2. Draw a rectangle to the right of the map frame
3. In **Item Properties**:
   - **Position:** X: 305 mm, Y: 50 mm
   - **Width:** ~100 mm

4. Configure legend settings:
   - Uncheck **Auto update** (gives you control)
   - **Title:** Leave blank or add "Legend"
   - **Fonts:**
     - Title: 12 pt bold
     - Subgroup: 10 pt bold
     - Item: 9 pt regular

5. Styling:
   - **Columns:** 1 (or 2 for many items)
   - **Symbol width/height:** 6 mm × 4 mm
   - **Spacing:** Item space 2 mm

### Step 7: Add a scale bar

1. Click **Add Item → Add Scale Bar**
2. Draw below or beside the map
3. In **Item Properties**:
   - **Style:** Single Box or Double Box
   - **Units:** Meters or Kilometers (match your CRS)
   - **Segments:** Left 0, Right 4
   - **Fixed width:** 50 mm (or 100 mm for A3)
   - **Height:** 3 mm
   - **Label:** Every segment

4. Position: bottom-left of map frame, inside the margin

### Step 8: Add a north arrow

1. Click **Add Item → Add North Arrow**
2. Draw a small box (15 × 15 mm)
3. In **Item Properties**:
   - Choose a simple SVG arrow (avoid ornate compass roses)
   - **Rotation:** Sync with map (for rotated maps)

4. Position: top-right or bottom-right corner of map frame

**Note:** Only include north arrows when orientation isn't obvious (rotated maps, unfamiliar areas). For standard north-up maps of well-known regions, they're optional.

### Step 9: Add title text

1. Click **Add Item → Add Label**
2. Draw a text box at the top of your layout
3. Enter placeholder text: `[MAP TITLE]`
4. In **Item Properties**:
   - **Font:** 24–32 pt, bold, sans-serif
   - **Horizontal alignment:** Left or Center
   - **Vertical alignment:** Middle

5. Add a subtitle label below:
   - **Font:** 14 pt, regular
   - **Text:** `[Subtitle or date]`

### Step 10: Add credits/data sources

1. Add another label in the bottom margin
2. Enter placeholder: `Data: [SOURCE, YEAR] | CRS: [EPSG CODE] | Author: [NAME]`
3. In **Item Properties**:
   - **Font:** 8–9 pt, regular
   - **Color:** Dark grey (#333333)

---

## Part 4: Saving as a template

### Step 11: Save the template file

1. Go to **Layout → Save as Template...**
2. Navigate to your templates folder (create one if needed):
   ```
   intro-gis/
   └── templates/
       └── A3_landscape_standard.qpt
   ```
3. Name it descriptively: `A3_landscape_standard.qpt`
4. Click **Save**

The `.qpt` file contains:
- Page size and orientation
- All layout items (map frame, legend, scale bar, text boxes)
- Positions and styling
- Guide positions

It does **not** contain:
- Your actual map data
- Layer styles
- Project settings

---

## Part 5: Using your template

### Loading a template for a new map

1. Open your QGIS project with the map you want to export
2. Go to **Project → Layout Manager**
3. Click **New from Template...**
4. Browse to your `.qpt` file
5. Name the new layout: `Week03_Choropleth_Map`
6. Click **OK**

### Updating the map content

1. Click on the **map frame** in your layout
2. In **Item Properties**, click **Set Map Extent to Match Main Canvas**
   - Or: **Update Preview** to refresh
3. If layers changed, click **Refresh** in the Items panel

### Updating text placeholders

1. Click on each text label
2. Replace placeholder text:
   - `[MAP TITLE]` → `Socioeconomic Disadvantage by SA2`
   - `[Subtitle]` → `Greater Sydney, 2021`
   - `[SOURCE, YEAR]` → `ABS Census 2021`
   - `[EPSG CODE]` → `EPSG:7856`
   - `[NAME]` → `Your Name`

### Updating the legend

1. Click on the legend
2. In **Item Properties**, click **Update All** to pull current layers
3. Remove unwanted items: select → click minus button
4. Rename items: double-click to edit text
5. Reorder: drag items up/down

---

## Part 6: Template variations

Create multiple templates for different purposes:

### Portrait template
- Size: A4 portrait (210 × 297 mm)
- Map frame: Top 2/3 of page
- Legend and text: Bottom 1/3
- Good for: Reports, single-page handouts

### Comparison template
- Two map frames side by side
- Shared legend below
- Good for: Before/after, two time periods

### Dashboard template
- Main map with 2-3 small inset maps
- Space for charts or statistics
- Good for: Executive summaries, presentations

```
COMPARISON TEMPLATE              DASHBOARD TEMPLATE
┌──────────┬──────────┐          ┌─────────────┬─────┐
│          │          │          │             │░░░░░│
│  MAP 1   │  MAP 2   │          │   MAIN MAP  │░░░░░│
│  (2016)  │  (2021)  │          │             ├─────┤
│          │          │          │             │░░░░░│
├──────────┴──────────┤          ├──────┬──────┼─────┤
│      LEGEND         │          │INSET1│INSET2│STATS│
└─────────────────────┘          └──────┴──────┴─────┘
```

---

## Quick reference: Layout toolbar

| Icon | Tool | Shortcut |
|------|------|----------|
| 🗺️ | Add Map | — |
| 📋 | Add Legend | — |
| 📏 | Add Scale Bar | — |
| ⬆️ | Add North Arrow | — |
| 📝 | Add Label | — |
| 🖼️ | Add Picture | — |
| ⬜ | Add Shape | — |
| ↖️ | Select/Move | V |
| ✋ | Pan Layout | P |
| 🔍 | Zoom | Z |

---

## Common problems and fixes

| Problem | Cause | Solution |
|---------|-------|----------|
| Map shows wrong area | Extent not updated | Click **Set Map Extent to Match Main Canvas** |
| Legend shows wrong layers | Auto-update enabled | Uncheck auto-update, manually select layers |
| Scale bar shows wrong units | CRS mismatch | Check project CRS matches layout CRS |
| Elements won't align | Snapping off | Enable **View → Snap to Guides** |
| Template loads empty | Normal behaviour | Map frames are placeholders—update extent |
| Text cut off | Box too small | Resize label box or reduce font size |
| Blurry export | Low DPI | Export at 300 DPI for print |

---

## Export settings

### For print (PDF)
- **Resolution:** 300 DPI
- **Format:** PDF
- **Export → Export as PDF**
- Check: **Print as raster** if you have transparency issues

### For digital/web (PNG)
- **Resolution:** 150 DPI (or 96 for screen-only)
- **Format:** PNG
- **Export → Export as Image**
- Choose PNG for transparency support

### For presentations
- **Resolution:** 150 DPI
- **Dimensions:** 1920 × 1080 px (match your slides)
- Export to PNG, then insert in PowerPoint/Google Slides

---

## Your template library

Over the course, build these templates:

1. **Week 2:** `A3_landscape_standard.qpt` — Your main template
2. **Week 4:** `A3_terrain_with_hillshade.qpt` — For raster/elevation maps
3. **Week 5:** `A3_comparison_two_maps.qpt` — Side-by-side analysis
4. **Capstone:** Customize for your project's specific needs

Save all templates in `intro-gis/templates/` so they're easy to find.

---

## Design checklist

Before exporting, verify:

- [ ] Map fills the frame appropriately (not too zoomed/too wide)
- [ ] Legend matches visible layers (no extras, nothing missing)
- [ ] Scale bar shows sensible numbers (not 17.3 km)
- [ ] All placeholder text has been replaced
- [ ] Fonts are readable at intended size
- [ ] Elements align to guides
- [ ] Data source and date are credited
- [ ] Tested at 100% zoom—everything legible?

---

## Further reading

- [Map Design Principles](design-rubric.md) — Visual hierarchy, balance, grids
- [Project Checklist](project-checklist.md) — Full quality control list
- [QGIS Print Layout Documentation](https://docs.qgis.org/latest/en/docs/user_manual/print_composer/index.html)
