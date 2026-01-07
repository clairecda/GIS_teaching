# Week 1 · QGIS Orientation & Project Setup

Welcome to your GIS journey! This week you'll set up your workspace, navigate the QGIS interface, and create your first map. By the end of this session, you'll have a working QGIS installation, an organized project folder structure, and hands-on experience loading and styling spatial data. Think of this week as building your foundation—everything that follows builds on these core skills.

## What you'll learn

By the end of this week, you'll be able to:

1. Install QGIS (LTR 3.34 recommended) and configure your workspace.
2. Navigate the QGIS interface (Browser, Layers, Processing Toolbox, Layout Manager).
3. Load vector layers, inspect attribute tables, and apply basic symbology.
4. Create a custom color palette for consistent map styling throughout the course.
5. Build a print layout with title, legend, scale bar, and data credits.

## Before you start

- [ ] Follow the [Install QGIS](../onboarding/01-install-qgis.md) guide and confirm the app launches
- [ ] Review the lecture: [Foundations of GIS](../lectures/week01-fundamentals.md)
- [ ] Read the GIS primer: [Understanding GIS](../readings/week01-what-is-gis.md)

!!! note "Data downloads happen in class"
    We'll download Natural Earth datasets together during class. Your facilitator will guide you through the process—no pre-class downloads required!

## This week's activities

### Activity 1: Confirm your QGIS installation

Let's make sure QGIS is properly installed and your workspace is organized.

**Steps:**

1. Launch QGIS and confirm you see the welcome screen
2. Check the version: `Help ▶ About` — you should see **QGIS 3.34 LTR** (or newer)
3. Enable key panels if they're not visible:
   - `View ▶ Panels ▶ Browser Panel`
   - `View ▶ Panels ▶ Layers Panel`
   - `View ▶ Panels ▶ Processing Toolbox`
4. If your interface looks cluttered, reset it: `Settings ▶ Options ▶ System ▶ Reset user interface`

!!! tip "Save your layout"
    Once you've arranged panels the way you like, QGIS remembers your preferences. Spend a few minutes getting comfortable with the layout now—it'll save time later.

### Activity 2: Set up your project workspace

Organized files make everything easier. You'll create a folder structure that you'll use throughout the course.

**Steps:**

1. Create a course folder (e.g., `GIS_Course` or `intro-to-gis`) in a location you can easily find
2. Inside that folder, create these subfolders:
   - `data/raw` — original downloaded datasets (never edit these)
   - `data/processed` — cleaned and filtered data you create
   - `projects` — your QGIS project files (.qgz)
   - `exports` — maps, images, and outputs you create
   - `screenshots` — helpful for documentation and assignments
3. Navigate to this folder in QGIS's Browser Panel to confirm it appears

!!! note "Why this structure?"
    Keeping raw data separate from processed data helps you trace your steps. If something goes wrong, you can always return to the original data and start fresh.

### Activity 3: Create and configure your first project

Now you'll create a QGIS project file and set some important defaults.

**Steps:**

1. Create a new project: `Project ▶ New` (or Ctrl/Cmd + N)
2. Set the project CRS (Coordinate Reference System):
   - Click the CRS button in the bottom-right corner (shows something like `EPSG:4326`)
   - Search for `4326` (this is WGS 84, a common global CRS)
   - Select it and click OK

!!! info "What is CRS?"
    CRS tells QGIS how to interpret coordinates. Think of it like a language for locations—"EPSG:4326" means coordinates are in latitude/longitude degrees (like GPS). We'll cover this in depth in Week 2. For now, just use 4326 for global data.

3. Enable relative paths (makes your project portable):
   - `Project ▶ Properties ▶ General`
   - Check **"Save paths: Relative"**
   - Click OK
4. Save the project:
   - `Project ▶ Save As...`
   - Navigate to your `projects/` folder
   - Name it `week01_orientation.qgz`
   - Click Save

### Activity 4: Load your first spatial data

Time to see some geography! You'll load Natural Earth country boundaries and explore the attribute table.

**Steps:**

1. In the Browser Panel, navigate to where you saved your Natural Earth data
2. Find the file `ne_110m_admin_0_countries.shp`
3. Drag it onto the map canvas (or double-click it)
4. You should see a world map appear with country outlines
5. Right-click the layer in the Layers Panel → **Open Attribute Table**
6. Explore the table:
   - Click column headers to sort (try sorting by `POP_EST` for population)
   - Notice fields like `NAME`, `CONTINENT`, `GDP_MD`, etc.
   - Each row represents one country
7. Close the attribute table

!!! tip "Understanding the connection"
    Use the ![Identify](../assets/icons/mActionIdentify.svg){: style="height:1.2em; vertical-align:middle" } **Identify Features** tool to click on any country and see its data:

    1. Find the ![Identify](../assets/icons/mActionIdentify.svg){: style="height:1.2em; vertical-align:middle" } icon in the toolbar
    2. Click the icon to activate the tool (your cursor changes)
    3. Click on any country on the map
    4. A panel appears showing that country's attributes (name, population, etc.)

    This shows how the map and table are linked—each shape on the map is connected to a row of data.

**Optional:** Load the Admin 1 layer (`ne_110m_admin_1_states_provinces.shp`) to see states and provinces. Notice how it adds more detail.

### Activity 5: Apply basic symbology

Let's make the map more meaningful by coloring countries by continent.

**Steps:**

1. Right-click your countries layer → **Properties** → **Symbology** tab
2. At the top, change **Single Symbol** to **Categorized**
3. Set **Value** to `CONTINENT`
4. Click **Classify** (this creates a color for each continent)
5. Click **OK** to apply
6. Your map should now show different colors for each continent

!!! info "Symbology types explained"
    | Type | Use for | Example |
    |------|---------|---------|
    | **Single Symbol** | All features look the same | All countries in blue |
    | **Categorized** | Text/category data | Different color per continent |
    | **Graduated** | Numeric data | Darker colors for higher population |

    The **Classify** button tells QGIS to scan your data and create groups automatically.

**Experiment:** Try changing it to **Graduated** symbology using `POP_EST` (population) to see countries colored by population ranges.

!!! note "Week 2 preview"
    Next week you'll dive deeper into color choices, classification methods, and cartographic design principles. For now, just get comfortable with the mechanics.

### Activity 6: Create a course color palette

Consistent colors make your maps look professional. QGIS lets you save custom colors for easy reuse throughout the course.

**Steps:**

1. Open the color picker:
   - Go to `Settings ▶ Options ▶ Colors` tab
   - Or: When in any color selector, click the dropdown arrow → **Colors...**

2. Add colors to your palette:
   - Click the green **+** button to add a new color
   - Use the color wheel or enter hex codes
   - Here are some **example colors** to get you started:

   | Feature | Example Hex | Notes |
   |---------|-------------|-------|
   | Water | `#4a90d9` | Blues for water (cartographic convention) |
   | Vegetation | `#2e7d32` | Greens for forests/parks |
   | Highlights | `#e65100` | Warm colors draw attention |
   | Urban | `#455a64` | Neutral greys |
   | Rivers | `#4fc3f7` | Lighter blue for streams |

3. Label your colors:
   - Double-click on a color swatch
   - Give it a descriptive name (e.g., "Course - Water Teal")
   - Adding "Course -" prefix keeps them grouped together

4. Access your palette anytime:
   - In any color picker, your custom colors appear under **Recent Colors** or **Standard Colors**
   - The palette saves automatically with your QGIS profile

!!! tip "Import/export palettes"
    You can export your palette to share with classmates:

    - In the Colors tab, click **...** → **Export Colors**
    - Save as `.gpl` (GIMP palette) file
    - Share the file; others import via **Import Colors**

**Why this matters:**

- **Consistency:** Same colors across all 12 weeks = professional portfolio
- **Efficiency:** No searching for "that blue I used last time"
- **Accessibility:** Plan accessible colors once, use them everywhere

!!! info "ColorBrewer for map-specific palettes"
    For choropleth maps (graduated colors), use [ColorBrewer](https://colorbrewer2.org/) to generate accessible, sequential or diverging palettes. You'll practice this in Week 2.

### Activity 7: Create your first layout

A layout is how you turn your QGIS canvas into a polished map ready for export or printing.

**Steps:**

1. Create a new layout: `Project ▶ New Print Layout...`
2. Give it a name (e.g., "World Map") and click OK
3. A new window opens—this is your layout canvas (a blank page)

!!! info "Finding the layout tools"
    The layout window has its own toolbar on the left side. Key tools:

    | Icon | Tool | What it does |
    |:----:|------|--------------|
    | ![Add Map](../assets/icons/mLayoutItemMap.svg){: style="height:1.5em; vertical-align:middle" } | **Add Map** | Inserts your map canvas |
    | ![Add Label](../assets/icons/mLayoutItemLabel.svg){: style="height:1.5em; vertical-align:middle" } | **Add Label** | Adds text (titles, credits) |
    | ![Add Legend](../assets/icons/mLayoutItemLegend.svg){: style="height:1.5em; vertical-align:middle" } | **Add Legend** | Adds map legend |
    | ![Add Scale Bar](../assets/icons/mLayoutItemScaleBar.svg){: style="height:1.5em; vertical-align:middle" } | **Add Scale Bar** | Adds scale reference |
    | ![Add North Arrow](../assets/icons/mLayoutItemNorthArrow.svg){: style="height:1.5em; vertical-align:middle" } | **Add North Arrow** | Shows map orientation (required!) |

    Hover over any icon in QGIS to see its name.

4. Add a map:
   - Click the ![Add Map](../assets/icons/mLayoutItemMap.svg){: style="height:1.2em; vertical-align:middle" } **Add Map** button in the toolbar
   - Draw a rectangle on the canvas (click and drag to define the area)
   - Your map from the main QGIS window appears in this frame

5. Add a title:
   - Click the ![Add Label](../assets/icons/mLayoutItemLabel.svg){: style="height:1.2em; vertical-align:middle" } **Add Label** button
   - Draw a box at the top of the page
   - In the panel on the right, find the text box (shows "Lorem ipsum" as placeholder text)
   - Delete the placeholder and type your title: "World Countries by Continent"
   - Scroll down in the panel to find **Font** settings → increase size to 18-24pt
6. Add a legend:
   - Click the ![Add Legend](../assets/icons/mLayoutItemLegend.svg){: style="height:1.2em; vertical-align:middle" } **Add Legend** button
   - Draw a box where you want the legend
   - In Legend properties, you can rename items or remove unnecessary entries
7. Add a scale bar:
   - Click the ![Add Scale Bar](../assets/icons/mLayoutItemScaleBar.svg){: style="height:1.2em; vertical-align:middle" } **Add Scale Bar** button
   - Draw a box at the bottom of your map
8. Add a north arrow:
   - Click **Add Item → Add North Arrow** (or find the compass icon in the toolbar)
   - Draw a small box in the top-right or bottom-right corner
   - Choose a simple arrow style

!!! warning "North arrow is required"
    Every map must have a north arrow. A map without one is incomplete and will not be accepted for submission.

9. Add data source:
   - Add another ![Add Label](../assets/icons/mLayoutItemLabel.svg){: style="height:1.2em; vertical-align:middle" } label at the bottom: "Source: Natural Earth, 2024"
10. Export your map:
   - Click **Layout ▶ Export as Image...** (or Export as PDF)
   - Save to `exports/week01_first_map.png`

!!! tip "Practice makes perfect"
    Layouts can feel fiddly at first. Don't worry about making it perfect—you'll get lots of practice in Week 2.

## Troubleshooting

### QGIS won't launch or crashes on startup
- **Mac:** Right-click the app → Open (bypasses Gatekeeper security warning the first time)
- **Windows:** Run as Administrator if you get permission errors
- **All platforms:** Delete the QGIS user profile folder to reset settings:
  - Windows: `C:\Users\[username]\AppData\Roaming\QGIS\QGIS3\`
  - Mac: `~/Library/Application Support/QGIS/QGIS3/`
  - Linux: `~/.local/share/QGIS/QGIS3/`

### Layer doesn't appear on the map
- **Check visibility:** Is the checkbox ticked in the Layers panel?
- **Check layer order:** Drag layers up/down—polygons should be below points
- **Zoom to layer:** Right-click layer → **Zoom to Layer** to find it
- **Check CRS:** If the layer is in a different CRS, it may appear in the wrong location. Right-click → **Properties** → **Source** to see the CRS

### "Layer is not valid" error when adding data
- **File path issue:** Move files out of folders with special characters or spaces
- **Missing components:** Shapefiles need all companion files (.shp, .shx, .dbf, .prj) in the same folder
- **Corrupted download:** Re-download the file

### Attribute table is empty or shows wrong data
- **Check the right layer:** Make sure you opened the correct layer's attribute table
- **Encoding issue:** Try `Layer Properties ▶ Source ▶ Data source encoding` → change to UTF-8

### Can't find a tool or panel
- **Panels:** `View ▶ Panels` → check the panel you need
- **Toolbars:** `View ▶ Toolbars` → check the toolbar you need
- **Processing Toolbox:** `Processing ▶ Toolbox` or press `Ctrl+Alt+T`
- **Reset interface:** `Settings ▶ Options ▶ System ▶ Reset user interface to default`

### Project won't save or gives errors
- **Invalid path:** Avoid special characters in folder/file names
- **Permissions:** Make sure you have write access to the folder
- **Relative paths:** Check `Project ▶ Properties ▶ General ▶ Save paths` is set to "Relative"

## Support materials

- Slides: [Week 01 lecture deck](../slides/index.md)
- Reading: [Understanding GIS](../readings/week01-what-is-gis.md)
- Cheat sheet: [QGIS Quickstart](../reference/qgis-quickstart.md)
- Dataset checklist: [Week 1 items](../reference/data-download-checklist.md)

## Reflect

Take 10 minutes to answer these questions in your [Week 1 reflection](../reference/reflections.md#week-1--qgis-orientation):

- What was one thing that went smoothly during setup?
- What was one challenge you encountered? How did you solve it (or what do you still need help with)?
- What surprised you most about QGIS or spatial data?
- What's one keyboard shortcut or panel arrangement that you want to remember?

!!! tip "Keep notes"
    Recording your successes and struggles helps you troubleshoot later and makes it easier to help classmates. Your reflection is also valuable for your own learning—you'll look back and see how far you've come!

## What you'll submit

- [ ] QGIS project file: `projects/week01_orientation.qgz` with Natural Earth layers loaded and styled
- [ ] Exported map: `exports/week01_first_map.png` (or PDF) showing your categorized world map
- [ ] Your Week 1 reflection entry

!!! danger "Map submission requirements"
    Your exported map **must** include these four elements or it will not be accepted:

    - [ ] **Title** — What the map shows
    - [ ] **Legend** — What the colors/symbols mean
    - [ ] **Scale bar** — Distance reference
    - [ ] **North arrow** — Map orientation

    See [Map Design Principles](../reference/design-rubric.md) for the complete checklist.

## Coming up next week

Week 2 focuses on advanced symbology, labelling, and professional layout design. You'll learn about color theory, classification methods, and cartographic conventions. **Bring a map you admire** (digital or printed) to share during the Week 2 design show-and-tell—we'll discuss what makes effective maps work.
