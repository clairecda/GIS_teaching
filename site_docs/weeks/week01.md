# Week 1 · QGIS Orientation & Project Setup

Welcome to your GIS journey! This week you'll set up your workspace, navigate the QGIS interface, and create your first map. By the end of this session, you'll have a working QGIS installation, an organized project folder structure, and hands-on experience loading and styling spatial data. Think of this week as building your foundation—everything that follows builds on these core skills.

## What you'll learn

By the end of this week, you'll be able to:

1. Install QGIS (LTR 3.34 recommended) and configure your workspace.
2. Navigate the QGIS interface (Browser, Layers, Processing Toolbox, Layout Manager).
3. Load vector layers, inspect attribute tables, and save a project with organised folders.

## Before you start

- [ ] Follow the [Install QGIS](../onboarding/qgis-install.md) guide and confirm the app launches
- [ ] Create the course workspace structure (`data/`, `projects/`, `exports/`, etc.)
- [ ] Review the QGIS quickstart cheat sheet: [Reference ▸ Quickstart](../reference/qgis-quickstart.md)
- [ ] Review the lecture: [Foundations of GIS](../lectures/week01-fundamentals.md)
- [ ] Read the GIS primer: [Understanding GIS](../readings/week01-what-is-gis.md)
- [ ] Download Natural Earth datasets using the [dataset guide](../onboarding/data-downloads.md) and check off Week 1 items in the [checklist](../reference/data-download-checklist.md)

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
    Use the **Identify tool** (toolbar button with an "i") to click on a country. You'll see its attributes appear—this shows how the map and table are linked.

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

**Experiment:** Try changing it to **Graduated** symbology using `POP_EST` (population) to see countries colored by population ranges.

!!! note "Week 2 preview"
    Next week you'll dive deeper into color choices, classification methods, and cartographic design principles. For now, just get comfortable with the mechanics.

### Activity 6: Create your first layout

A layout is how you turn your QGIS canvas into a polished map ready for export or printing.

**Steps:**

1. Create a new layout: `Project ▶ New Print Layout...`
2. Give it a name (e.g., "World Map") and click OK
3. A new window opens—this is your layout canvas
4. Add a map:
   - Click the **Add Map** button in the toolbar
   - Draw a rectangle on the canvas (this defines where your map appears)
   - Your map from the main QGIS window appears in this frame
5. Add a title:
   - Click **Add Label** button
   - Draw a box at the top of the page
   - In the Label properties panel (right side), replace "Lorem ipsum" with your title: "World Countries by Continent"
   - Increase font size to 18-24pt
6. Add a legend:
   - Click **Add Legend** button
   - Draw a box where you want the legend
   - In Legend properties, you can rename items or remove unnecessary entries
7. Add a scale bar:
   - Click **Add Scale Bar** button
   - Draw a box at the bottom of your map
8. Add data source:
   - Add another label at the bottom: "Source: Natural Earth, 2024"
9. Export your map:
   - Click **Layout ▶ Export as Image...** (or Export as PDF)
   - Save to `exports/week01_first_map.png`

!!! tip "Practice makes perfect"
    Layouts can feel fiddly at first. Don't worry about making it perfect—you'll get lots of practice in Week 2.

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

## Coming up next week

Week 2 focuses on advanced symbology, labelling, and professional layout design. You'll learn about color theory, classification methods, and cartographic conventions. **Bring a map you admire** (digital or printed) to share during the Week 2 design show-and-tell—we'll discuss what makes effective maps work.
