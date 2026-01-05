# Week 1 Facilitator Notes: QGIS Orientation & Project Setup

## Session Overview

**Duration:** 2-3 hours (adjust based on class size and tech issues)

**Learning Objectives:**
By the end of this session, students will be able to:
1. Navigate the QGIS interface and enable/arrange key panels
2. Create an organized project workspace with proper folder structure
3. Load vector layers and inspect attribute tables
4. Apply basic symbology (categorized and graduated)
5. Create a simple print layout with title, legend, scale bar, and source

**Materials Needed:**
- QGIS 3.34 LTR (or newer) installed on all computers
- Natural Earth datasets pre-downloaded (especially `ne_110m_admin_0_countries.shp`)
- Projector/screen sharing setup for live demos
- Backup USB drives with QGIS installers and datasets (for installation issues)
- Handout: QGIS Quickstart cheat sheet (optional but helpful)
- Student course website access confirmed

**Tech Setup:**
- Test QGIS on classroom computers at least 1 day before class
- Verify Natural Earth data is accessible (shared drive, cloud link, or USB)
- Have your own demo project ready with layers pre-loaded as backup
- Check screen resolution for projector—QGIS panels can look different on low-res displays

---

## Before Class Checklist

**1 Week Before:**
- [ ] Email students installation instructions and data download guide
- [ ] Ask students to confirm they've installed QGIS and note any issues
- [ ] Prepare troubleshooting guide for common installation problems
- [ ] Create your own Week 1 project as demo reference

**1 Day Before:**
- [ ] Test QGIS on classroom computers (or your teaching computer if online)
- [ ] Download Natural Earth datasets to accessible location
- [ ] Create a backup QGIS project file with layers loaded (in case demo fails)
- [ ] Test projector/screen share with QGIS interface—check visibility of panels
- [ ] Print or share QGIS Quickstart cheat sheet

**30 Minutes Before:**
- [ ] Launch QGIS and confirm it opens without errors
- [ ] Open your demo project or prepare to start fresh
- [ ] Have Natural Earth data location ready in file browser
- [ ] Set QGIS window to good size for projection (not full screen—easier to see)
- [ ] Close unnecessary panels to reduce visual clutter for demo
- [ ] Test audio/video if teaching remotely

**Key Panels to Have Visible:**
- Browser Panel (left side)
- Layers Panel (left side, below Browser)
- Map Canvas (center)
- Processing Toolbox (right side, but can hide initially to reduce overwhelm)

---

## Session Flow

### Opening (5-10 minutes)

**Icebreaker Activity:**
"Before we dive in, let's go around the room. Share your name and one place in the world you'd love to map. It could be your hometown, a place you've traveled, or somewhere you dream of visiting."

**Purpose:**
- Builds community
- Gets students thinking spatially
- You can reference these places during demos ("Maria mentioned mapping coffee farms in Colombia—we'll be able to do that by Week 5!")

**Key Opener Points to Say:**
"Welcome to your GIS journey. Today might feel overwhelming—there are a lot of buttons, menus, and new vocabulary. That's completely normal. By the end of today, you'll have created your first map. It won't be perfect, but you'll have the foundation to build on.

Three things to remember:
1. **It's okay to break things.** QGIS won't explode. If something goes wrong, we can always start over.
2. **Ask questions.** If you're confused, someone else probably is too.
3. **Save often.** You'll thank yourself later.

Let's get started!"

---

### Critical Framing Discussion (10 minutes)

**Purpose:** Establish the course's critical lens early. This brief discussion sets up thinking patterns students will use all semester.

**Setup (say this):**
"Before we open QGIS, I want to share something that will shape how we approach this course. GIS doesn't just map the world—it reflects how the world has been understood, governed, and valued. What does that mean? Let's explore briefly."

**Prompt 1: What do maps leave out?**
"Think of a map you've used recently—Google Maps, a weather map, a subway map. What does it show really well? Now: what does it leave out?"

**Expected responses:**
- Google Maps shows roads well but not pedestrian shortcuts or informal paths
- Weather maps show temperature but not hyperlocal variation
- Subway maps show connections but distort actual geography

**Your follow-up:**
"Exactly. Every map is a choice. It answers some questions brilliantly and makes others almost invisible. This isn't a flaw—it's just how maps work. Our job this semester is to see those choices."

**Prompt 2: Who decided?**
"When you see a boundary on a map—suburbs, districts, zones—who drew that line? And why there?"

**Expected responses:**
- Government officials, planners
- For taxes, services, voting
- Sometimes historical reasons no one remembers

**Your synthesis:**
"Right. Boundaries aren't natural—they're decisions. Those decisions reflect priorities: What was important to the people drawing the lines? We'll come back to this in Week 3, but I want you to start noticing: boundaries are choices."

**Prompt 3: Categories that don't fit**
"Quick thought experiment: You're filling out a form with options 'Employed full-time,' 'Employed part-time,' 'Unemployed,' 'Student,' 'Retired.' You work three gig jobs while taking classes. Which box do you check?"

**Expected response:** It depends, none fit perfectly, I'd pick the closest.

**Your synthesis:**
"Data works the same way. Every dataset puts complex realities into boxes. The boxes are useful, but they're never perfect. When we map 'land use' or 'income brackets' or 'crime types,' we're inheriting someone else's boxes. The skill we'll build this semester is seeing those boxes—asking 'Who decided these categories?' and 'What doesn't fit?'"

**Closing statement:**
"Here's what I want you to carry through this course: Data is produced, not found. Maps are choices. Categories reflect historical priorities. We won't tell you what to think politically—we'll teach you to see assumptions. That makes you a better analyst, a better communicator, and a more thoughtful professional.

Now let's open QGIS and start learning how to work with spatial data. Remember: as you learn techniques, keep asking—what choices are embedded in this data?"

---

### Part 1: Interface Orientation (20-30 minutes)

**Demo: QGIS Interface Tour**

**What to do:**
1. Launch QGIS (project screen if available, or start fresh)
2. Point out major areas:
   - "This big area in the middle is your **map canvas**—this is where your maps appear"
   - "On the left, the **Browser Panel** is like Finder/File Explorer—it shows your files"
   - "Below that, the **Layers Panel** shows what's currently on your map, like layers in Photoshop"
   - "These toolbars at the top have tools we'll use constantly"

**What to say:**
"If your interface looks different from mine, don't panic. QGIS is highly customizable. Let's make sure you have the key panels visible.

Go to **View → Panels** and make sure these are checked:
- Browser Panel
- Layers Panel

If your screen is too cluttered or you want to reset, go to **Settings → Options → System tab** and click **Reset user interface to default**. But let's hold off on that unless you really need it—we want to learn to work with the interface, not fight it."

**Point out key toolbar icons (hover to show names):**
- Pan Map (hand)
- Zoom In/Out (magnifying glass)
- Identify Features (lowercase 'i')
- Open Attribute Table (looks like a grid)

**What to say:**
"Don't try to memorize everything. We'll use these tools repeatedly, and you'll naturally remember the ones you need. For now, just know that if you hover over any icon, QGIS tells you what it does."

**Check-in moment:**
"Can everyone see the Browser Panel and Layers Panel? Thumbs up if yes, raise your hand if you need help."

**Common student issue:**
Panels accidentally closed or docked in weird places.
- **Fix:** View → Panels → re-enable it
- **Tip:** Panels can be dragged and re-docked. If a student's interface is chaotic, offer to help individually during hands-on time rather than holding up the class.

---

### Part 2: Project Workspace Setup (15-20 minutes)

**Demo: Creating Folder Structure**

**What to do (share screen showing file browser):**
1. Open Finder/File Explorer
2. Navigate to Documents or Desktop
3. Create folder: `intro-to-gis` (or `GIS_Course`)
4. Inside it, create subfolders:
   - `data/raw`
   - `data/processed`
   - `projects`
   - `exports`
   - `screenshots`

**What to say:**
"Organization saves lives. Well, maybe not lives, but definitely hours of frustration. We're creating this structure now so we have a consistent place for everything.

**data/raw** — This is sacred. Never edit files here. It's your backup.
**data/processed** — When you clean or filter data, save it here.
**projects** — Your QGIS project files (.qgz) go here.
**exports** — Final maps, images, anything you share or print.
**screenshots** — When something breaks and you need to ask for help, screenshots go here.

Why separate raw and processed? Imagine you spend 3 hours cleaning a dataset, then accidentally save over the original. Now you can't go back. Keeping raw data separate protects you from yourself."

**Demo: Creating and Configuring QGIS Project**

**What to do:**
1. In QGIS: Project → New (or Ctrl/Cmd+N)
2. Click the CRS button (bottom-right corner, shows "EPSG:4326" or similar)
   - Search: `4326`
   - Select "WGS 84 - EPSG:4326"
   - Click OK
3. Project → Properties → General tab
   - Under "Save paths," select **Relative**
   - Click OK
4. Project → Save As
   - Navigate to `projects/` folder
   - Name: `week01_orientation.qgz`
   - Save

**What to say:**
"Let's talk about CRS—Coordinate Reference System. This tells QGIS how to interpret coordinates. Think of it like units of measurement: meters vs. feet. If you don't specify, QGIS guesses, and it doesn't always guess right.

For now, we're using **EPSG:4326**, which means coordinates are in latitude/longitude degrees—the same system your phone's GPS uses. Week 2, we'll dive deeper into projections. Today, just use 4326 for global data.

**Relative paths** — When checked, QGIS saves file locations relative to your project file, not absolute paths like 'C:/Users/YourName/...' This means if you move your entire course folder to a USB drive or cloud storage, everything still works. Always check this box."

**Check-in moment:**
"Who was able to create their project and save it? Any errors?"

**Common student issue:**
Students save the project in random locations (Desktop, Downloads).
- **Fix:** "Let's relocate it now. File → Save As → navigate to your projects folder. QGIS will update the project location."

---

### Part 3: Loading Data and Exploring Attributes (25-30 minutes)

**Demo: Loading Your First Layer**

**What to do:**
1. In Browser Panel, navigate to where Natural Earth data is saved
2. Expand folder to show `.shp` files
3. Find `ne_110m_admin_0_countries.shp`
4. Drag it onto the map canvas (or double-click)
5. World map appears with country outlines

**What to say:**
"This is the moment it becomes real. We're loading actual spatial data—a shapefile of world country boundaries from Natural Earth, a free dataset maintained by cartographers.

Notice the file extension: **.shp**. Shapefiles are the most common GIS vector format. But here's a quirk: a shapefile is actually 3-4 files with the same name but different extensions:
- .shp — the geometry (shapes)
- .shx — the index (helps find shapes quickly)
- .dbf — the attributes (data table)
- .prj — the projection (CRS information)

They must all be in the same folder. If you move the .shp file alone, QGIS can't find the others and it breaks. Always move/copy all the files together."

**Demo: Attribute Table Exploration**

**What to do:**
1. Right-click layer in Layers Panel → Open Attribute Table
2. Click column headers to sort (try `NAME`, `POP_EST`, `CONTINENT`)
3. Scroll through rows
4. Point out specific fields: NAME, CONTINENT, POP_EST, GDP_MD

**What to say:**
"This table is connected to the map. Each row is one country. Each country on the map has a row in this table.

Let's sort by **POP_EST** (estimated population). Click the column header. China and India at the top—makes sense. Scroll down... tiny island nations at the bottom.

This connection—geometry on the map, attributes in the table—is the foundation of GIS. The shapes answer 'where?', the table answers 'what and how much?'"

**Demo: Identify Tool**

**What to do:**
1. Close attribute table
2. Click the Identify tool (lowercase 'i' icon in toolbar)
3. Click on a country (try something recognizable like Australia, Brazil, France)
4. Identify Results panel appears showing that country's data

**What to say:**
"The Identify tool is your best friend. Instead of opening the whole table, you can click any feature to see its data.

Let's click on... France. See? Name: France. Population: ~67 million. Continent: Europe. This is how you quickly inspect individual features.

Try clicking a few countries. Notice how the data updates. This instant feedback makes GIS feel almost magical—you're querying a database by clicking on a map."

**Hands-On Activity (10 minutes):**
"Your turn. Load the countries layer, open the attribute table, and find:
1. The country with the highest GDP (sort by GDP_MD)
2. A country in Africa (filter CONTINENT or just browse)
3. Use the Identify tool to click on the country where you were born (or live now)

Raise your hand if you get stuck. I'll walk around to help."

**Check-in moment:**
Walk around (or monitor chat/cameras if remote). Look for:
- Students who loaded the layer successfully
- Students with blank maps (layer didn't load)
- Students who can't find the attribute table

**Common student issues:**
- **Layer loaded but map is blank:** "Right-click the layer → Zoom to Layer. Sometimes QGIS zooms to a weird location."
- **Attribute table shows weird characters:** Text encoding issue. "Right-click layer → Properties → Source tab → Data source encoding → try 'UTF-8' or 'ISO-8859-1'."
- **Can't find the Identify tool:** "Look for the lowercase 'i' with a cursor. It's in the top toolbar. Hover over icons to find it."

---

### Part 4: Basic Symbology (30-35 minutes)

**Demo: Categorized Symbology (by Continent)**

**What to do:**
1. Right-click countries layer → Properties → Symbology tab
2. Top dropdown: change from "Single Symbol" to "Categorized"
3. Value dropdown: select `CONTINENT`
4. Click "Classify" button
5. QGIS generates a color for each continent
6. Click OK
7. Map updates with colors

**What to say:**
"Right now, every country is the same color—Single Symbol symbology. That's boring and not very informative. Let's color countries by continent.

Step 1: Layer Properties → Symbology.
Step 2: Change 'Single Symbol' to **Categorized**.
Step 3: Choose the field to categorize by—we'll use `CONTINENT`.
Step 4: Click **Classify**. QGIS scans the data, finds all unique continents, and assigns each one a color. Magic!
Step 5: Click OK.

Now your map shows continents in different colors. This is **categorized symbology**—for categorical data like names, types, or groups."

**Discussion Prompt:**
"What kinds of data would make sense for categorized symbology? Think about the attribute table we explored."

**Expected answers:** Country names, continent, region, country type (island vs mainland), anything text-based or with distinct categories.

**Correct and expand:** "Exactly. Categorized works for discrete categories. But what if we want to show population—a number that ranges from small to large? That's where **graduated symbology** comes in."

**Demo: Graduated Symbology (by Population)**

**What to do:**
1. Layer Properties → Symbology
2. Change "Categorized" to "Graduated"
3. Value: select `POP_EST`
4. Classes: keep default (5)
5. Mode: keep "Natural Breaks (Jenks)" for now (explain briefly)
6. Color ramp: choose something intuitive (light to dark)
7. Click Classify
8. Click OK

**What to say:**
"Now we're showing population. Notice QGIS divided countries into 5 groups (classes) based on population ranges. Countries with low population get a light color, high population get dark.

The **Mode** dropdown—Natural Breaks (Jenks)—is an algorithm that finds natural clusters in your data. We'll cover classification methods in depth in Week 2. For now, just know it's trying to create meaningful groups.

Look at the map: China and India are darkest—highest population. Tiny island nations are lightest. This is **graduated symbology**—for numeric data."

**Comparison Moment:**
"Let's compare:
- **Single Symbol:** Everything the same. Use when you just want to show locations.
- **Categorized:** Different colors for categories (continent, type, name).
- **Graduated:** Color gradient for numbers (population, temperature, income).

You'll choose based on your data type and what you want to communicate."

**Hands-On Activity (15 minutes):**
"Your turn. Try both:
1. Apply categorized symbology using a different field (try `SUBREGION` or `INCOME_GRP` if your dataset has it).
2. Apply graduated symbology using `GDP_MD` (GDP in millions of dollars). Which countries are richest?
3. Experiment with different color ramps.

Don't worry about making it pretty. Just practice the mechanics."

**Check-in moment:**
"How many people were able to change the symbology? Any confusion on categorized vs. graduated?"

**Common student issues:**
- **"Classify" button is greyed out:** They forgot to select a Value field. "Choose a field from the Value dropdown first."
- **Colors look ugly/confusing:** "Don't worry about aesthetics today. Week 2 is all about color theory and design. For now, just make it work."
- **Graduated symbology shows weird ranges:** "That's normal. QGIS calculates ranges based on your data. We'll learn to customize this."

---

### Part 5: Creating a Print Layout (35-40 minutes)

**This is the most challenging part for first-timers. Go slowly and show every step.**

**Demo: Creating a New Layout**

**What to do:**
1. Project → New Print Layout
2. Name it: "World Map"
3. Click OK
4. New window opens (blank page)

**What to say:**
"A layout is how you turn your map canvas into a printable or shareable map. The main QGIS window is for analysis. The layout window is for presentation.

Notice this is a separate window—it has its own toolbars. Don't panic if it looks unfamiliar. The tools are on the left side."

**Point out the left toolbar:**
"These are your layout tools. The main ones we'll use today:
- **Add Map** (rectangle with lines) — inserts your map
- **Add Label** (letter A) — adds text
- **Add Legend** (list icon) — adds legend
- **Add Scale Bar** (ruler icon) — adds scale
- **Select/Move Item** (arrow) — click this to move things around after adding them"

**Demo: Adding a Map Frame**

**What to do:**
1. Click "Add Map" tool (rectangle with map lines icon)
2. Click and drag on the layout canvas to draw a rectangle (most of the page, leaving room for title/legend)
3. Release mouse—map from main QGIS window appears in the frame

**What to say:**
"Click the 'Add Map' button. Now click and drag to draw a box where you want your map to appear. Think of it like inserting an image in a Word document.

When you release, your map appears! This is a live snapshot of your main QGIS window. If you go back to the main window and change colors or zoom, you can update the layout map.

**Important:** To move or resize this map frame, you need to click the **Select/Move Item** tool (arrow) first, then click the frame. This is the #1 confusion point—students try to drag the frame without selecting the tool first."

**Demo this:** Switch to Select tool, click frame, drag it. Resize by dragging corner handles.

**Demo: Adding a Title**

**What to do:**
1. Click "Add Label" tool
2. Draw a box at the top of the page
3. In the Item Properties panel on the right, find the text box (says "Lorem ipsum")
4. Replace with: "World Countries by Continent"
5. Scroll down to Font section
6. Increase font size to 20-24pt
7. Click Select/Move tool to deselect

**What to say:**
"Click 'Add Label.' Draw a box where you want your title—usually at the top.

Look at the right panel—this shows properties for whatever item is selected. You'll see a text box with placeholder text 'Lorem ipsum.' Delete that and type your title.

Scroll down in this panel to find **Font** settings. Make it bigger—18 to 24 point. You want it readable.

To stop editing, click the Select/Move arrow tool. This deselects the label."

**Common student issue:**
Students can't find the text box or font settings—the Item Properties panel is collapsed or scrolled past it.
- **Fix:** "Make sure the label is selected (click it with the Select tool). Then look at the right panel. If you don't see it, scroll up to the top."

**Demo: Adding a Legend**

**What to do:**
1. Click "Add Legend" tool
2. Draw a box (usually bottom-right or side)
3. Legend appears showing layer name and symbols

**What to say:**
"Click 'Add Legend.' Draw a box. The legend appears automatically based on your symbology.

You can customize it in Item Properties—rename items, remove layers you don't want to show, adjust fonts. For today, just leave it as-is. We'll refine legends in Week 2."

**Optional:** Show how to remove unwanted layers from legend:
- In Item Properties → Legend Items → click layer → click red minus button to remove

**Demo: Adding a Scale Bar**

**What to do:**
1. Click "Add Scale Bar" tool
2. Draw a box at the bottom of the map
3. Scale bar appears

**What to say:**
"Scale bars show the relationship between distance on the map and real-world distance. Essential for any map.

Click 'Add Scale Bar,' draw a box. Done. You can change the style and units in Item Properties, but defaults are usually fine for now."

**Demo: Adding Data Source**

**What to do:**
1. Click "Add Label" again
2. Draw small box at bottom
3. Type: "Source: Natural Earth, 2024"
4. Reduce font size to 8-10pt

**What to say:**
"Always credit your data sources. It's ethical, and it helps others find the data.

Add another label at the bottom. Type the source. Make the font small—8 to 10 point. It should be visible but not dominate the map."

**Demo: Exporting the Map**

**What to do:**
1. Layout → Export as Image (or Export as PDF)
2. Navigate to `exports/` folder
3. Name: `week01_first_map.png`
4. Click Save
5. Resolution dialog appears—keep default 300 DPI
6. Click Save

**What to say:**
"Time to export. Layout → Export as Image.

Navigate to your `exports` folder—this is why we created that folder structure earlier!

Name it something you'll recognize: `week01_first_map.png`.

Resolution: 300 DPI is good for printing. Lower is fine for web. We'll keep the default.

Click Save. QGIS creates the image file. You can now email it, print it, or post it on Instagram and pretend you're a cartographer."

**Open the exported file to show students the result.**

**Hands-On Activity (20 minutes):**
"Now you create your own layout. Include:
1. Map frame with your symbolized countries
2. Title
3. Legend
4. Scale bar
5. Data source credit

Export it as `week01_first_map.png` to your exports folder.

This will feel awkward. Layouts are finicky. Don't aim for perfection—just get all 5 elements on the page and export it. Go!"

**Check-in moment:**
Walk around or monitor student progress. Common sticking points:
- Can't move items (forgot to click Select tool first)
- Text is too small or too big
- Legend shows too many items
- Map frame is empty or shows weird area

**Common student issues:**
- **Map frame is blank:** "Go back to the main QGIS window. Is your layer visible there? If yes, come back to the layout, right-click the map frame → Item Properties → scroll to Layers → make sure the layer is listed."
- **Can't resize items:** "Click the Select/Move tool (arrow) first, THEN click the item, THEN drag the corner handles."
- **Text won't change:** "Make sure the label is selected (click it with Select tool). Then look at Item Properties on the right for the text box."
- **Export button is greyed out or gives error:** "Make sure you've added at least a map frame. QGIS won't export a blank layout."

---

### Part 6: Troubleshooting Common Issues (10 minutes)

**Group Discussion:**

"Let's talk about what went wrong today—because something always does, and that's okay. What issues did you hit? Let's troubleshoot together."

**Solicit responses. Address common ones:**

**Issue: "My layer won't load / I get an error"**
- **Fix:** Check file path—no special characters or spaces. Make sure all shapefile components (.shp, .shx, .dbf, .prj) are together.

**Issue: "My map is blank after loading the layer"**
- **Fix:** Right-click layer → Zoom to Layer. Or check if layer visibility checkbox is on.

**Issue: "Attribute table shows gibberish"**
- **Fix:** Layer Properties → Source → Data source encoding → try UTF-8.

**Issue: "QGIS crashed / won't save my project"**
- **Fix:** Save frequently. If it crashes, restart QGIS. If problems persist, reset user profile (Settings → Options → System → reset).

**What to say:**
"GIS software is powerful but temperamental. When something breaks:
1. Don't panic.
2. Read the error message (QGIS usually tells you what's wrong).
3. Google it—seriously, someone else has had this problem.
4. Ask for help—me, classmates, GIS Stack Exchange.

Also: **Save your project constantly.** Ctrl+S / Cmd+S. Make it a reflex."

---

### Wrap-Up & Preview (10 minutes)

**Reflection Prompts:**

"Before we finish, take 5 minutes to write quick notes:
- What was one thing that went smoothly today?
- What was one challenge you encountered?
- What surprised you most about QGIS or spatial data?
- What's one keyboard shortcut or tip you want to remember?"

**Optional:** Have a few students share aloud.

**What to say:**
"Today was your foundation. You installed QGIS, loaded data, styled it, and created a map. That's HUGE.

It probably felt overwhelming. You'll forget half of what we did. That's normal. The student-facing materials and cheat sheets are there to help you review.

**What you need to submit for Week 1:**
1. Your QGIS project file: `week01_orientation.qgz` with layers loaded and styled
2. Your exported map: `week01_first_map.png` (or PDF)
3. Your reflection entry

Upload these to [platform] by [deadline]."

**Preview Week 2:**

"Next week, we level up. We'll dive deep into symbology—color theory, classification methods, and how to make maps that actually communicate clearly. We'll also master print layouts.

**Homework for next week:** Bring a map you admire—digital or printed. Could be a weather map, a subway map, an infographic with a map, anything. We'll do a design show-and-tell and discuss what makes effective maps work.

Questions before we wrap up?"

**Final Encouragement:**

"You did great today. GIS has a learning curve, but you've taken the first step. See you next week!"

---

## Key Concepts to Emphasize

### 1. Spatial Data = Geometry + Attributes
**Why it matters:** This is the foundation of GIS. Students must understand that every feature has a shape (where) and data (what).

**How to reinforce:**
- Constantly connect the map to the attribute table
- Use Identify tool repeatedly to show the link
- Ask: "What does this shape represent? Where can we find more info about it?"

### 2. Organization Prevents Disaster
**Why it matters:** New users save files randomly, lose data, or overwrite originals.

**How to reinforce:**
- Show your own organized folder structure
- Explain "raw vs. processed" logic
- Use relative paths—make projects portable
- Repeatedly save to the `projects/` folder during demos

### 3. CRS (Coordinate Reference Systems) Exist (But We Won't Master Them Today)
**Why it matters:** CRS confusion is a top reason maps break. But Week 1 isn't the time for deep dives.

**How to handle:**
- Acknowledge it exists: "This tells QGIS how to read coordinates"
- Use EPSG:4326 for Week 1 (familiar, global)
- Say: "Week 2 we'll go deeper. For now, trust me and use 4326."
- Don't let CRS questions derail the session—defer to Week 2

### 4. Symbology is Communication, Not Decoration
**Why it matters:** Students think symbology is "making it pretty." It's actually about conveying information.

**How to reinforce:**
- Explain categorized vs. graduated based on data type
- Ask: "What are we trying to show? Categories or numbers?"
- Preview Week 2: "We'll learn why some color choices mislead people."

### 5. Layouts Are Separate from Analysis
**Why it matters:** Students get confused about the two windows—main QGIS vs. print layout.

**How to reinforce:**
- Explicitly say: "This is a separate window for presentation, not analysis."
- Show switching back and forth between windows
- Emphasize: Map canvas = workspace. Layout = final product.

---

## Live Demo Script

Use this if you want a step-by-step script for a continuous demo (rather than breaking into parts). Adjust timing as needed.

### Full Demo Flow (60 minutes straight, if no hands-on breaks)

**[0:00-0:05] Opening**
"Welcome! Today you'll create your first map. Let's start by launching QGIS..."

**[0:05-0:15] Interface Tour**
1. Launch QGIS
2. Point out Browser, Layers, Map Canvas
3. View → Panels → ensure key panels are visible
4. Hover over toolbar icons to show names
5. "Don't memorize—just know they're here."

**[0:15-0:25] Folder Setup**
1. Open file browser, create `intro-to-gis` folder
2. Create subfolders: `data/raw`, `data/processed`, `projects`, `exports`, `screenshots`
3. "This keeps you organized. Raw data stays safe."

**[0:25-0:35] Create Project**
1. Project → New
2. Set CRS: click bottom-right, search 4326, select WGS 84
3. Project → Properties → General → Relative paths → Save
4. Project → Save As → `projects/week01_orientation.qgz`
5. "Relative paths make your project portable."

**[0:35-0:45] Load Data**
1. Browser Panel → navigate to Natural Earth data
2. Drag `ne_110m_admin_0_countries.shp` to map canvas
3. World map appears
4. "This is a shapefile—actually 4 files (.shp, .shx, .dbf, .prj). Keep them together."

**[0:45-0:55] Explore Attributes**
1. Right-click layer → Open Attribute Table
2. Click column headers to sort (NAME, POP_EST, CONTINENT)
3. "Each row is a country. The map and table are linked."
4. Close table
5. Identify tool → click on countries → show data
6. "This is how you query: click the map, see the data."

**[0:55-1:10] Categorized Symbology**
1. Layer Properties → Symbology
2. Change to Categorized → Value: CONTINENT → Classify → OK
3. "Different color per continent. Use categorized for categories."

**[1:10-1:20] Graduated Symbology**
1. Layer Properties → Symbology
2. Change to Graduated → Value: POP_EST → Classify → OK
3. "Color gradient for numbers. Use graduated for numeric data."

**[1:20-1:25] Create Layout**
1. Project → New Print Layout → name "World Map" → OK
2. "This is your presentation window. Separate from the main QGIS window."

**[1:25-1:35] Add Map Frame**
1. Add Map tool → draw rectangle on canvas
2. Map appears
3. Select/Move tool → resize/reposition
4. "This is a snapshot of your main QGIS window."

**[1:35-1:40] Add Title**
1. Add Label tool → draw box at top
2. Item Properties → replace text: "World Countries by Continent"
3. Increase font size to 20pt

**[1:40-1:45] Add Legend**
1. Add Legend tool → draw box
2. Legend appears automatically
3. "Shows your symbology. Can customize in Item Properties."

**[1:45-1:50] Add Scale Bar**
1. Add Scale Bar tool → draw box at bottom
2. "Shows map scale. Essential for any map."

**[1:50-1:55] Add Source**
1. Add Label → draw small box at bottom
2. Type: "Source: Natural Earth, 2024"
3. Font size 8-10pt

**[1:55-2:00] Export**
1. Layout → Export as Image
2. Navigate to `exports/` → name `week01_first_map.png` → Save
3. Open exported file to show result
4. "Done! You've created your first map."

---

## Discussion Prompts

Use these throughout the session to check understanding and encourage critical thinking.

### After Loading Data:
**"What do you notice about the shapes of countries near the poles (like Greenland or Antarctica)?"**
- **Expected answer:** "They look huge/distorted."
- **Follow-up:** "That's because of map projection. EPSG:4326 is unprojected lat/lon, which distorts size near poles. Week 2 we'll explore this more."

### After Exploring Attribute Table:
**"What kind of questions could you answer with this dataset?"**
- **Expected answers:** "Which continent has most countries? Which country has highest population? Which countries have the lowest GDP?"
- **Follow-up:** "Exactly. GIS lets you answer spatial questions by combining geography and data."

### After Categorized Symbology:
**"Can you think of other fields in this dataset that would work well with categorized symbology?"**
- **Expected answers:** SUBREGION, INCOME_GRP (if available), TYPE (if available).
- **Wrong answer to correct gently:** "Population." → "Close, but population is numeric. We'd use graduated for that."

### After Graduated Symbology:
**"Why might using graduated symbology for population be more useful than just listing numbers in a table?"**
- **Expected answer:** "You can see spatial patterns—where high/low population countries are clustered."
- **Expand:** "Right! Maps make patterns visible that are hard to see in tables. That's the power of GIS."

### After Creating Layout:
**"What's the difference between the main QGIS window and the print layout window?"**
- **Expected answer:** "Main window is for working/analysis. Layout is for exporting/presenting."
- **Reinforce:** "Exactly. You analyze in one, present in the other."

### During Wrap-Up:
**"What's one thing you learned today that you could use outside this class?"**
- **Examples students might give:** "How to organize project files. How to make a map. How to explore data visually."
- **Purpose:** Connect learning to real-world applications.

---

## Common Student Issues

### Installation/Setup Issues

**Issue:** QGIS won't launch (Mac Gatekeeper error)
- **Symptom:** "QGIS can't be opened because it's from an unidentified developer"
- **Fix:** Right-click QGIS app → Open (this bypasses Gatekeeper the first time). Then it will open normally.

**Issue:** QGIS crashes on startup (Windows)
- **Symptom:** QGIS window appears briefly then closes
- **Fix:** Run as Administrator. Or reset user profile: delete `C:\Users\[username]\AppData\Roaming\QGIS\QGIS3\`

**Issue:** Student doesn't have admin rights to install QGIS
- **Fix:** Contact IT beforehand. Or use QGIS portable version (doesn't require installation). Or provide virtual machine access.

### Data Loading Issues

**Issue:** Layer doesn't appear after loading
- **Symptoms:** Layer shows in Layers Panel but map canvas is blank
- **Fixes:**
  1. Right-click layer → Zoom to Layer
  2. Check layer visibility checkbox (is it ticked?)
  3. Check layer order (is it behind another layer?)
  4. Check CRS mismatch (advanced—defer to Week 2)

**Issue:** "Invalid layer" error when loading shapefile
- **Symptoms:** Red triangle icon next to layer name, error message
- **Fixes:**
  1. Check all shapefile components (.shp, .shx, .dbf, .prj) are present
  2. Check file path has no special characters or spaces
  3. Re-download the file (might be corrupted)

**Issue:** Attribute table is empty or shows "NULL"
- **Symptoms:** Table opens but all rows are blank or say NULL
- **Fixes:**
  1. Check you opened the correct layer's table
  2. The data might genuinely be empty (wrong file)
  3. Encoding issue (try Layer Properties → Source → Data source encoding → UTF-8)

### Interface Issues

**Issue:** Can't find a panel (Browser, Layers, etc.)
- **Fix:** View → Panels → check the panel name

**Issue:** Panels are docked in weird places or floating
- **Fix:** Drag panel by its title bar to re-dock. Or Settings → Options → System → Reset user interface to default (nuclear option).

**Issue:** Toolbars disappeared
- **Fix:** View → Toolbars → re-enable needed toolbars

**Issue:** QGIS interface is tiny/huge on high-DPI screen
- **Fix:** Settings → Options → General → Override system locale → increase/decrease UI scaling. Requires restart.

### Symbology Issues

**Issue:** "Classify" button is greyed out
- **Fix:** Student forgot to select a Value field. Choose field from dropdown first, THEN classify.

**Issue:** Graduated symbology shows weird ranges (e.g., 0-1000000000)
- **Expected behavior:** This is normal if data has extreme outliers. Explain that QGIS calculates ranges based on data distribution.
- **Week 2 fix:** "We'll learn to manually set ranges next week."

**Issue:** Colors don't change after clicking OK
- **Fix:** Student might have clicked Apply on wrong tab. Re-open Properties → Symbology → re-apply.

**Issue:** Legend shows layer name instead of categories
- **Fix:** In Symbology, make sure they selected Categorized or Graduated (not Single Symbol). If still wrong, it's a legend issue—remove and re-add legend in layout.

### Layout Issues

**Issue:** Can't move or resize items in layout
- **Fix:** Click the Select/Move Item tool (arrow) first. This is the #1 layout frustration.

**Issue:** Map frame is empty/blank
- **Fixes:**
  1. Go back to main QGIS window—is layer visible there?
  2. In layout, right-click map frame → Item Properties → Layers section → ensure layer is listed
  3. Click "Update Preview" button in Item Properties

**Issue:** Text won't change in label
- **Fix:** Make sure label is selected (click it with Select tool), THEN look for text box in Item Properties on the right. Students often don't have the label selected.

**Issue:** Legend shows too many items or wrong items
- **Fix:** In Item Properties → Legend Items → select unwanted layers → click red minus button to remove.

**Issue:** Can't export layout / export button greyed out
- **Fixes:**
  1. Make sure at least one item (e.g., map frame) is in the layout
  2. Try Layout → Export as PDF instead of Image
  3. Check file path for export location is valid (no special characters)

### Project Saving Issues

**Issue:** "Could not save project" error
- **Fixes:**
  1. Check folder permissions (can you write to that location?)
  2. File path has special characters or spaces—rename folders
  3. Save to a different location (e.g., Desktop) as test

**Issue:** Project file disappears or won't re-open
- **Symptoms:** Student saved project, closed QGIS, can't find it
- **Fix:** Use File → Open Recent. Or search computer for `.qgz` files. Emphasize saving to `projects/` folder with clear names.

**Issue:** Relative paths don't work—layers show as broken when project is moved
- **Fix:** Check Project → Properties → General → Save paths is set to "Relative." If already set but still broken, data might be outside the project folder structure (can't use relative paths if data is on different drive).

---

## Wrap-Up & Preview

### Closing Script

**[5 minutes before end of class]**

"Alright, let's bring it together. Today you:
- Set up QGIS and organized your workspace
- Loaded spatial data and explored attributes
- Applied symbology to show patterns
- Created a print layout and exported your first map

That's a LOT. If your brain feels full, that's normal.

**What you need to do before next week:**

1. **Submit your Week 1 deliverables:**
   - QGIS project file: `week01_orientation.qgz`
   - Exported map: `week01_first_map.png`
   - Reflection entry (answer those 4 questions)
   - Due: [deadline]

2. **Review the student materials:**
   - Re-read Week 1 page on the course website
   - Check out the QGIS Quickstart cheat sheet
   - Watch the [optional video tutorial, if you made one]

3. **Prepare for Week 2:**
   - Find a map you admire (digital or printed). Could be a weather map, transit map, infographic with spatial data—anything. Bring it to class or have the link ready. We'll discuss what makes good maps work.

**Questions? Concerns? Victories to share?**

[Take questions]

**Final thought:**

You're now GIS users. You might not feel like it yet, but you've crossed the threshold. Everything from here builds on what you did today.

See you next week. Great job!"

---

## Week 2 Preview (for Your Prep)

To prepare for next week, review these topics:
- **Color theory for maps:** ColorBrewer, accessibility, sequential vs. diverging vs. qualitative schemes
- **Classification methods:** Jenks, quantiles, equal interval, standard deviation
- **Advanced layout design:** Grid alignment, visual hierarchy, typography
- **Labeling:** Placement rules, label engines, expression-based labels
- **Cartographic conventions:** North arrows, scale bars, neat lines, citations

**Activity ideas for Week 2:**
- Map critique: students present maps they found and discuss design choices
- Color scheme comparison: same data, different color ramps—what's the impact?
- Layout refinement: take Week 1 maps and improve them

---

## Additional Facilitator Tips

### Time Management
- **If running short on time:** Skip the optional Admin 1 layer in Activity 4. Focus on getting everyone through one complete workflow rather than exploring extras.
- **If ahead of schedule:** Add an extra hands-on challenge—"Load the populated places layer and style it by population size."
- **Build in buffer time:** Always assume 15-20% of class time will be troubleshooting. Plan for 90 minutes of content in a 120-minute session.

### Managing Mixed Skill Levels
- **Fast finishers:** Give extension tasks—"Try loading the rivers layer and styling it by stroke width" or "Experiment with layer blending modes."
- **Struggling students:** Pair them with a buddy or work with them individually during hands-on time. Sometimes screen-sharing 1-on-1 for 2 minutes solves everything.
- **Encourage peer help:** "If you finish early, help someone near you. Teaching solidifies your own learning."

### Online Teaching Adjustments
- **Screen sharing:** Use two monitors if possible—one for demo, one for student gallery view.
- **Breakout rooms:** During hands-on time, create breakout rooms for small group troubleshooting.
- **Chat monitoring:** Assign a TA or ask students to post issues in chat. Address common ones publicly.
- **Recording:** Record your demos so students can rewatch. Post to course site.

### Accessibility Considerations
- **Font size:** Increase QGIS UI scaling for demos (Settings → Options → General).
- **Color blindness:** Mention that Week 2 covers colorblind-friendly palettes. For Week 1, don't stress it.
- **Keyboard shortcuts:** Demonstrate them but don't require them. Some students can't use shortcuts due to assistive tech.
- **Captioning:** If teaching online, enable auto-captions or provide live captioning.

### Building a Supportive Environment
- **Normalize mistakes:** Share your own early GIS blunders. "I once spent an hour troubleshooting before realizing I forgot to turn the layer on."
- **Celebrate small wins:** "Who got their first layer to load? That's worth celebrating!"
- **Encourage questions:** "There are no dumb questions. GIS is full of weird quirks. Ask!"
- **Create a class chat/forum:** Slack, Discord, or forum where students help each other between sessions.

### Dealing with Tech Failures
- **QGIS crashes during demo:** Have a backup project file pre-loaded. "This is why we save constantly!"
- **Projector fails:** Have screenshots of key steps ready. Or pivot to students doing hands-on while you walk around.
- **Data files missing:** Keep a USB backup. Or share via cloud link in chat immediately.

---

## Self-Reflection (For Facilitator After Class)

After teaching, jot down notes:
- **What went well?** (e.g., "Students grasped symbology quickly.")
- **What confused students?** (e.g., "Layout window vs. main window—need clearer explanation.")
- **What took longer than expected?** (e.g., "Troubleshooting layer loading took 15 extra minutes.")
- **What could I cut next time?** (e.g., "Skip the optional Admin 1 layer demo.")
- **What should I add?** (e.g., "More time for layout practice—students struggled.")

Use these notes to refine Week 1 for next cohort and to inform Week 2 planning.

---

## Quick Reference: What Students Should Achieve by End of Week 1

**Minimum viable success (every student should accomplish):**
- [ ] QGIS installed and launches without errors
- [ ] Organized folder structure created
- [ ] QGIS project saved in `projects/` folder
- [ ] At least one layer loaded and visible on map
- [ ] Attribute table opened and explored
- [ ] Basic symbology applied (categorized OR graduated)
- [ ] Simple layout created with map, title, and legend
- [ ] Map exported as image or PDF

**Stretch goals (if time allows):**
- [ ] Multiple layers loaded
- [ ] Both categorized AND graduated symbology applied
- [ ] Layout includes all elements: map, title, legend, scale bar, source
- [ ] Student experimented with different color ramps
- [ ] Student used Identify tool to explore features

**Red flags (students who need extra support):**
- QGIS won't launch or repeatedly crashes
- Can't load any layers / all layers show as invalid
- Can't find or navigate the interface
- Didn't save project or can't locate saved files

Identify these students early and schedule office hours or extra support sessions.

---

## Resources for Facilitator

**Bookmark these:**
- [QGIS Training Manual](https://docs.qgis.org/latest/en/docs/training_manual/) — official tutorials
- [QGIS Documentation](https://docs.qgis.org/latest/en/docs/user_manual/) — full user manual
- [GIS Stack Exchange](https://gis.stackexchange.com/) — Q&A forum for troubleshooting
- [ColorBrewer](https://colorbrewer2.org/) — for Week 2 symbology
- [Natural Earth Data](https://www.naturalearthdata.com/) — dataset source

**Join communities:**
- QGIS users mailing list
- r/QGIS on Reddit
- QGIS Official Twitter/Mastodon

**Prep materials to create (if not already done):**
- QGIS Quickstart cheat sheet (keyboard shortcuts, common tools)
- Video tutorial of Week 1 workflow (10-15 min screencast)
- Troubleshooting FAQ document
- Example finished Week 1 project for students to reference

---

**Good luck! You've got this. Week 1 is always the hardest to teach—once students have the foundation, everything else builds naturally. Be patient, be encouraging, and remember: every expert GIS user was once bewildered by their first shapefile. Your job is to guide them through that bewilderment with empathy and clarity.**
