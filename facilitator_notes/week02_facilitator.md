# Week 2 Facilitator Notes: Symbology, Labelling & Layouts

## Session Overview

### Duration
- **Total:** 3 hours (standard workshop format)
- **Design show-and-tell:** 15-20 minutes
- **Live demos:** 60-70 minutes (broken into segments)
- **Hands-on practice:** 60-70 minutes
- **Wrap-up and Q&A:** 10-15 minutes

### Learning Objectives
By the end of this session, students will be able to:
1. Apply graduated, categorised, and rule-based symbology to communicate spatial patterns
2. Configure labels with data-driven styling and scale-dependent rules
3. Design an export-ready layout using cartographic design principles (hierarchy, balance, accessibility)

### Materials Needed

**Datasets:**
- Natural Earth countries shapefile (from Week 1)
- Renewable energy CSV file (country-level data with ISO_A3 codes)
- World cities CSV file with coordinates and population data

**Software:**
- QGIS 3.34+ (LTR recommended)
- Color Oracle or similar color blindness simulator (optional but recommended)
- Web browser for contrast checking tools

**Reference Materials:**
- Week 2 student guide (/Users/claireboulange/Desktop/GIS/intro-to-gis/site_docs/weeks/week02.md)
- Map Design Basics reading
- Layout Template guide
- Example "good" and "bad" maps for discussion

**Facilitator Resources:**
- Completed example project file (prepare in advance!)
- Screenshots of common error states
- Color ramp comparison handout (optional)

---

## Before Class Checklist

### Technical Preparation (Do this 24-48 hours before)

- [ ] **Test all datasets** - Load renewable energy CSV, world cities CSV, and Natural Earth countries in a fresh QGIS project
- [ ] **Verify the join works** - Test that ISO_A3 codes in CSV match Natural Earth exactly (check for common mismatches like Kosovo, Palestine, etc.)
- [ ] **Create a complete example project** - Build a finished version with all activities completed so you know what students should achieve
- [ ] **Test export functionality** - Verify PNG and PDF exports work on your system
- [ ] **Prepare your demo map** - Have your canvas already zoomed to an appropriate extent (global view showing all continents)
- [ ] **Screenshot common errors** - Capture images of failed joins (NULL values), wrong field types, overlapping labels, etc.

### Content Preparation

- [ ] **Curate 3-4 example maps** for show-and-tell:
  - 1-2 excellent examples (e.g., National Geographic, NYT graphics, professional atlas)
  - 1-2 problematic examples (cluttered legends, poor color choices, missing context)
- [ ] **Review classification methods** - Be ready to explain quantile vs equal interval vs natural breaks with simple analogies
- [ ] **Prepare color theory talking points** - Sequential vs diverging vs qualitative palettes, ColorBrewer origins
- [ ] **Have accessibility examples ready** - Show before/after of color blindness simulation

### Environment Setup

- [ ] **Check projector resolution** - Ensure QGIS interface is readable when projected (increase font size if needed)
- [ ] **Test screen sharing** (if remote/hybrid) - Verify students can see layer panel, attribute tables, and dialogs clearly
- [ ] **Prepare backup data** - Have datasets on USB drive or shared folder in case students didn't download
- [ ] **Set up collaborative space** - For in-person: arrange room so students can see each other's screens for peer learning
- [ ] **Prepare troubleshooting station** - Have one computer available for students who need individual help

---

## Session Flow

### Introduction (5 minutes)

**Opening:**
"Last week you learned the fundamentals of QGIS and loaded spatial data. This week, we're shifting from 'Can I make a map?' to 'Can I make a *good* map?'—one that communicates clearly, looks professional, and is accessible to all audiences."

**Key framing:**
- Emphasize that cartography is both art and science
- Design choices are not arbitrary—they have real impacts on how data is interpreted
- Even small decisions (color, label placement, legend order) shape the story

**Agenda overview:**
- Quick design show-and-tell to build visual literacy
- Learn advanced symbology (making data tell different stories)
- Master labelling (knowing when and how to add text)
- Assemble professional layouts (the final polish)

---

### Activity 1: Design Show-and-Tell (15-20 minutes)

**Purpose:** Build design awareness and vocabulary before diving into technical tools.

#### Facilitation Script

**Start with contributions (5-7 minutes):**
"Who brought a map to share? Let's see what you found."

- Invite 3-4 students to briefly show their inspirational map (on screen or hold up if printed)
- For each, ask: "What design element makes this effective?"
- Guide toward specific vocabulary: hierarchy, contrast, whitespace, color harmony

**Group analysis (5-7 minutes):**
Project 1-2 excellent examples and ask:
- "Where does your eye go first? Why?" (exploring hierarchy)
- "How does color guide interpretation?" (sequential, diverging, qualitative palettes)
- "What would happen if we removed the legend?" (testing clarity)

**Problematic examples (5 minutes):**
Show 1-2 poor maps and diagnose together:
- "What makes this hard to read?" (Common issues: rainbow color ramps, cluttered labels, missing scale bar, illegible fonts)
- "How would you fix it?" (Invite specific suggestions)

**Introduce design vocabulary:**
- **Visual hierarchy:** Most important element (title) → supporting info (legend, scale) → credits
- **Balance:** Distribution of visual weight across the page
- **Contrast:** Making important things stand out
- **Accessibility:** Designing for color blindness, low vision, etc.

**Transition:**
"Now that we know what good design looks like, let's learn the QGIS tools to achieve it."

---

### Activity 2: Classification Methods Demo (25-30 minutes total)

**Split:** 15 minutes demo + 10-15 minutes hands-on

#### Demo Script

**1. Load the CSV (5 minutes)**

**Narration:**
"We have renewable energy data in a CSV file—just a spreadsheet with country codes and percentages. CSVs don't have geometry (no shapes), so we can't map them directly. We need to *join* this data to a shapefile that already has country boundaries."

**On screen:**
1. `Layer > Add Layer > Add Delimited Text Layer`
2. Browse to renewable energy CSV
3. **Important:** Set Geometry definition to **"No geometry (attribute table only)"**
4. Click Add, then Close

**Talking point:**
"Notice it appears in the Layers panel but doesn't show on the map—that's expected because it's just a data table. Now we connect it to our countries layer."

**2. Perform the join (5 minutes)**

**Narration:**
"A join is like a lookup table. We tell QGIS: 'For every country in the shapefile, find its matching row in the CSV using the country code, and attach that data.'"

**On screen:**
1. Right-click countries layer → Properties → Joins tab
2. Click the green + button
3. **Join layer:** Select renewable energy CSV
4. **Join field:** ISO_A3 (or whatever the country code column is named in CSV)
5. **Target field:** ISO_A3 (in the shapefile)
6. Check "Custom field name prefix" and leave blank (or use short prefix like "re_")
7. Click OK

**Verify immediately:**
1. Right-click countries → Open Attribute Table
2. Scroll right to show new columns
3. **Point out:** "See these new columns? That's the CSV data now attached to each country."

**Common issue to address proactively:**
"If you see NULL or blank values, the codes didn't match. Check for typos, extra spaces, or case sensitivity. We'll troubleshoot this in the common issues section."

**3. Apply Graduated Symbology (10 minutes)**

**Narration:**
"Now we can visualize the data. Graduated symbology divides numeric data into classes and assigns each class a color. But *how* you create those classes changes the story dramatically."

**On screen:**
1. Layer Properties → Symbology tab
2. Change from "Single Symbol" to **"Graduated"**
3. **Value:** Select the renewable energy percentage field
4. **Color ramp:** Choose a ColorBrewer sequential palette (e.g., YlGnBu - yellow to blue)
5. **Classes:** 5
6. **Mode:** Start with "Natural Breaks (Jenks)"
7. Click **Classify** (emphasize this step!)
8. Click Apply to preview

**Now demonstrate the differences:**

**Natural Breaks:**
"This method finds 'natural' clusters in the data by minimizing variance within each class. Good for revealing genuine patterns, but class breaks might be odd numbers like 23.7%."

**Switch to Quantile:**
"Quantile puts an equal *number* of countries in each class. This ensures visual balance—each color appears equally on the map—but countries with very different values might end up in the same class. Look at the ranges: see how uneven they are?"

**Switch to Equal Interval:**
"Equal interval divides the data into equal-sized ranges (e.g., 0-10%, 10-20%, 20-30%). Clean and intuitive, but might result in empty classes or most countries in one class if data is skewed."

**Key teaching moment:**
"There's no single 'correct' method. Ask yourself: What story am I telling? Am I showing where high adoption is concentrated (Natural Breaks)? Am I comparing countries fairly (Quantile)? Am I using intuitive thresholds (Equal Interval)?"

**Final touches:**
1. Show how to reverse color ramp (dropdown arrow → Invert)
2. Demonstrate editing individual class labels (double-click symbol to edit text)
3. Mention "Mode: Color" vs "Mode: Size" (we'll use Size later for cities)

**Transition to hands-on:**
"Now try all three methods yourself. Open the attribute table while you do this—look at the actual values and see how they're grouped differently."

#### Hands-On Activity (10-15 minutes)

**Instructions to students:**
1. Load the renewable energy CSV as delimited text (no geometry)
2. Join it to your countries layer using ISO_A3 codes
3. Apply Graduated symbology and try all three classification methods
4. Decide which method best represents the data
5. Customize your color ramp and class labels

**Circulate and watch for:**
- Students forgetting to click "Classify"
- Join showing NULL values (field mismatch)
- Confusion about which field to select
- Students using rainbow color ramps (gently redirect to ColorBrewer)

**Wrap this segment:**
"Show of hands: Who chose Natural Breaks? Quantile? Equal Interval? All valid choices depending on your intent."

---

### Activity 3: Intelligent Labels Demo (20-25 minutes total)

**Split:** 10 minutes demo + 10-15 minutes hands-on

#### Demo Script

**1. Load cities with coordinates (3 minutes)**

**Narration:**
"Unlike the renewable energy CSV, this cities file has latitude and longitude columns, so we can load it with geometry."

**On screen:**
1. `Layer > Add Layer > Add Delimited Text Layer`
2. Browse to worldcities.csv
3. **Geometry definition:** Point coordinates
4. **X field:** lng
5. **Y field:** lat
6. **Geometry CRS:** EPSG:4326 (WGS 84)
7. Add and close

**Point out:** "Now you see points on the map—that's because we told QGIS how to create geometry from the coordinates."

**2. Filter to major cities (2 minutes)**

**Narration:**
"There are thousands of cities here. We only want to label the major ones—otherwise the map becomes unreadable."

**On screen:**
1. Right-click layer → Filter
2. Expression: `"population" > 5000000`
3. Click OK
4. **Show the result:** "Now only cities over 5 million people are visible."

**3. Enable and style labels (5 minutes)**

**Narration:**
"Labels turn abstract points into recognizable places. But bad labelling is worse than no labelling—cluttered, overlapping text makes maps unusable."

**On screen:**
1. Layer Properties → Labels tab
2. Change "No Labels" to **"Single Labels"**
3. **Value:** Select the city name field
4. Apply—show the messy result

**Talk through the problems:**
"See the overlap? Some labels are unreadable against dark backgrounds. Let's fix this."

**Style improvements:**
1. **Font:** Choose something clean (Arial, Open Sans, Roboto)
2. **Size:** 10-11 pt
3. **Text tab → Buffer:** Check "Draw text buffer"
   - Color: White
   - Size: 1-2 mm
4. Apply—show improvement

**Advanced: Scale-dependent visibility (5 minutes)**

**Narration:**
"Labels should appear only when they're useful. At global scale, city labels clutter the map. When zoomed in too close, you're looking at streets, not country-level context."

**On screen:**
1. In Labels tab, scroll to **Rendering** section
2. Check "Scale dependent visibility"
3. **Maximum (most out):** 1:50,000,000
4. **Minimum (most in):** 1:100,000
5. Apply

**Demonstrate:**
- Zoom out beyond 1:50,000,000 → labels disappear
- Zoom back in → labels reappear
- Zoom in close → labels disappear again

**Optional advanced feature (if time):**
Show expression-based labels:
1. Click ε button next to Value
2. Enter: `"name" || ' (' || format_number("population" / 1000000, 1) || 'M)'`
3. Explain: "The || concatenates (joins) text. This shows both name and population in millions."
4. Result: "Tokyo (37.4M)"

**Transition:**
"Now you'll add labels to your own map. Experiment with placement, buffers, and scale visibility."

#### Hands-On Activity (10-15 minutes)

**Instructions:**
1. Load world cities CSV with coordinates
2. Filter to cities over 5 million population
3. Enable labels with readable fonts and text buffers
4. Add scale-dependent visibility so labels appear only at appropriate zoom levels
5. Challenge: Try expression-based labels to show population

**Circulate and watch for:**
- Wrong X/Y field assignments (swapped lat/lng)
- Labels without buffers (unreadable)
- Scale ranges set backwards (min > max)
- Confusion about expression builder syntax

---

### Activity 4: Proportional Symbols Demo (15-20 minutes total)

**Split:** 8 minutes demo + 7-12 minutes hands-on

#### Demo Script

**Narration:**
"We've labelled cities. Now let's make the symbols themselves tell a story—bigger cities get bigger markers."

**On screen:**
1. Right-click cities layer → Duplicate Layer
2. Rename to "Major Cities - Population Size"
3. Open Layer Styling panel (or Properties → Symbology)
4. Change from "Single Symbol" to **"Graduated"**
5. **Value:** `"population" / 1000000` (explain: "This puts values in millions for cleaner legend")
6. **Mode:** Quantile, **Classes:** 4
7. Click Classify
8. **Critical step:** Change **Method** from "Color" to **"Size"**

**Explain:**
"This tells QGIS to vary marker size instead of color. All cities stay the same color, but size reflects population."

**Fine-tuning:**
1. Set **Min size:** 2.5 mm, **Max size:** 10 mm
2. Choose one fill color (e.g., coral or orange) with white stroke (0.3 mm)
3. Click Classify again to regenerate

**Customize legend labels:**
1. Double-click each class range
2. Rename to friendly labels: "1-4 M", "4-8 M", "8-15 M", "15 M+"
3. Explain: "These labels will appear directly in your layout legend."

**Match visibility with labels:**
1. Rendering tab → Scale dependent visibility
2. Use same scales as the label layer (1:50,000,000 to 1:100,000)

**Show result:**
Zoom in/out to demonstrate how symbols and labels appear together at appropriate scales.

**Optional: Preview in layout (if time):**
Create quick layout and add legend to show how the size classes appear automatically.

#### Hands-On Activity (7-12 minutes)

**Instructions:**
1. Duplicate your filtered cities layer
2. Apply Graduated symbology with Method: Size
3. Use population (in millions) as the value
4. Set appropriate min/max sizes (2.5-10 mm recommended)
5. Customize class labels for the legend
6. Match scale visibility with your label layer

**Circulate and watch for:**
- Forgetting to change Method from Color to Size
- Not clicking Classify after changing settings
- Min/max sizes too similar (not enough visual difference)
- Mismatched scale visibility between symbol and label layers

---

### Activity 5: Professional Layouts Demo (25-30 minutes total)

**Split:** 15 minutes demo + 10-15 minutes hands-on

#### Reference the Layout Template Guide

**Before starting the demo:**
"Remember the Layout Template guide from Week 1? Now's when it really pays off. Open `reference/layout-template.md` on the course website as your reference."

**Key points to reinforce:**
- Standard A3/A4 margins (15mm recommended)
- Guide placement for professional alignment
- Visual hierarchy principles (title → map → legend → credits)
- This is the foundation for all your maps going forward

#### Demo Script

**1. Create and set up layout (3 minutes)**

**Narration:**
"The map canvas is your workspace. The print layout is your final product. Everything we've built now gets assembled into a polished, export-ready composition."

**On screen:**
1. `Project > New Print Layout`
2. Name: "Renewable Energy Map"
3. Right-click canvas → Page Properties
4. Set to A3 Landscape (or A4 if students will print on standard paper)

**2. Add the map (3 minutes)**

**On screen:**
1. Click **Add Map** tool (rectangle icon)
2. Draw a large rectangle covering ~70-80% of the page
3. Leave margins on top (for title) and right/bottom (for legend, scale, credits)

**Important note:**
"Whatever is visible in your main QGIS window is what gets captured here. Before creating a layout, zoom to your desired extent."

**Item Properties panel:**
- Show **Scale** option: "You can lock this to a specific scale like 1:50,000,000"
- Show **Lock layers** and **Lock styles**: "Check these if you don't want the map to update when you change the main project"

**3. Add title (2 minutes)**

**On screen:**
1. **Add Label** tool → draw box across the top
2. In Item Properties → Main Properties, replace "Lorem ipsum" with:
   "Global Renewable Energy Share by Country, 2023"
3. Font → 20-24 pt, bold
4. Alignment → Center
5. Adjust box size to fit

**Design tip:**
"Titles should be the most prominent text element. Everything else is supporting information."

**4. Add and customize legend (4 minutes)**

**Narration:**
"QGIS auto-generates legends from your layers, but we need to clean them up—remove clutter, rename technical field names, and ensure it's readable."

**On screen:**
1. **Add Legend** tool → draw box on right side or below map
2. In Item Properties, uncheck **Auto update**
3. Remove unnecessary items:
   - Select items like basemaps, grid lines, etc.
   - Click the red minus button
4. Rename remaining items:
   - Select "ne_50m_admin_0_countries_renewable_energy_pct" → Edit → Rename to "Renewable Energy (%)"
   - Rename class labels to be human-friendly (e.g., "Less than 10%" instead of "0.00 - 10.00")
5. Adjust font size if needed (Item Properties → Fonts)

**Show the size legend (if Activity 4 was completed):**
"If you used Graduated Size for cities, they'll appear in the main legend with different sized markers. You can also add a dedicated data-defined size legend: `Add Item > Add Legend > Size Legend`."

**5. Add scale bar (2 minutes)**

**On screen:**
1. **Add Scale Bar** tool → draw at bottom of map
2. In Item Properties → Main Properties:
   - Style: Choose one that fits aesthetic (e.g., "Single Box", "Line Ticks Below")
   - Units: Check that it matches your map (usually kilometers for global maps)
3. Adjust segments and size for readability

**6. Add data credits (1 minute)**

**Narration:**
"Always attribute your data sources. It's ethical, often legally required, and builds credibility."

**On screen:**
1. **Add Label** → small text box at bottom
2. Text: "Data: Natural Earth, Our World in Data | Map: [Your Name], 2024"
3. Font: 8-9 pt
4. Alignment: Left or Center

**7. Optional: Add north arrow (1 minute)**

**On screen:**
1. **Add North Arrow** → draw in corner
2. Choose a simple, unobtrusive style
3. Note: "Only include north arrow if map orientation isn't obvious or if you've rotated the map."

**8. Export (2 minutes)**

**Narration:**
"You can export as image (for web) or PDF (for print quality)."

**On screen:**
1. `Layout > Export as Image`
   - Format: PNG
   - Save to: `exports/week02_renewable_energy.png`
   - **Resolution:** 300 DPI (for print) or 150 DPI (for screen)
2. `Layout > Export as PDF`
   - Save to: `exports/week02_renewable_energy.pdf`

**Design tips to mention:**
- Use View > Show Grid and Show Guides to align elements
- Hold Shift while resizing to maintain proportions
- Preview your export before finalizing—what looks good on screen might have issues when exported

**Transition:**
"Now you'll create your own layout. Focus on hierarchy: title first, map dominant, supporting elements secondary."

#### Hands-On Activity (10-15 minutes)

**Instructions:**
1. Create a new print layout (A3 landscape recommended)
2. Add your map with appropriate margins
3. Add a clear title
4. Add a legend (remove clutter, rename items)
5. Add a scale bar
6. Add data credits
7. Export as both PNG and PDF

**Circulate and watch for:**
- Map extent not set before adding to layout
- Legend including too many layers (students forget to hide/remove)
- Text too small to read
- Poor alignment (suggest using grid/guides)
- Forgetting to save the project (layouts are stored in .qgz file)

---

### Activity 6: Accessibility Check (10 minutes)

**This can be a brief guided demonstration or self-directed if time is short.**

#### Facilitation Script

**Narration:**
"A beautiful map is worthless if some of your audience can't read it. About 8% of men and 0.5% of women have color vision deficiency. Let's make sure your map works for everyone."

**1. Color blindness simulation (5 minutes)**

**On screen:**
1. Take a screenshot of your layout
2. Open Color Oracle (or similar tool) or use an online simulator like Coblis
3. Show how your map appears with Deuteranopia (red-green color blindness)
4. Show Protanopia and Tritanopia as well

**Point out:**
- "See how these two classes become almost identical?"
- "This is why we avoid red-green combinations and use ColorBrewer palettes—they're designed to be colorblind-safe."

**If problematic:**
- "Let's swap to a yellow-blue palette instead."
- Demonstrate the change and re-check

**2. Contrast checking (3 minutes)**

**Show a contrast checker tool (WebAIM):**
1. Sample a label color and its background
2. Check contrast ratio
3. Explain WCAG AA standard: minimum 4.5:1 for normal text

**If labels fail:**
- Increase buffer thickness
- Use darker/lighter text color
- Add background box with high-contrast fill

**3. Font size check (1 minute)**

**Quick checklist:**
- Title: 20-24 pt
- Labels: 10-12 pt minimum for screen, 8-9 pt for print
- Credits: 8-9 pt minimum

**4. Write alt text (1 minute)**

**Narration:**
"If you publish this map online, you should include alt text for screen readers."

**Example:**
"Choropleth map showing renewable energy share by country in 2023. Colors range from yellow (less than 10%) to dark blue (over 40%). Northern Europe shows the highest adoption, while fossil fuel-producing nations in the Middle East show the lowest."

**Transition:**
"Quickly check your own map. If you're using a ColorBrewer palette, you're probably fine, but it's worth verifying."

---

### Wrap-Up & Preview (10 minutes)

#### Reflection Prompts

**Ask students to consider (can be discussed or written):**
1. "Which classification method did you choose for renewable energy? Why?"
2. "What design choices did you make in your layout? How do they guide the reader's eye?"
3. "Did your map pass the accessibility checks? What did you adjust?"
4. "What was most challenging about creating the layout?"

**Invite 1-2 students to share their maps on screen:**
- Celebrate successes
- Offer constructive feedback
- Point out effective design choices

#### Key Takeaways

**Summarize:**
"Today you learned that cartography is about intentional choices:
- **Classification methods** change the story your data tells
- **Labels** add context but must be used sparingly and intelligently
- **Layouts** require hierarchy, balance, and attention to detail
- **Accessibility** is non-negotiable—design for all audiences"

#### Coming Up Next Week

**Preview Week 3:**
"Next week we'll work with administrative boundaries and socio-economic data. You'll learn how to join census data to statistical areas and start answering real-world questions about inequality, access, and demographics. This is where GIS becomes a tool for social analysis."

**Homework/preparation:**
- Download Week 3 datasets (SA2 boundaries and SEIFA, or local equivalents)
- Complete Week 2 reflection in the reference guide
- Submit your QGIS project file and exported layout
- Optional: Start collecting more inspirational maps for your reference library

**Final note:**
"If you get stuck on your assignment, revisit the troubleshooting section in the student guide. Most issues have simple fixes!"

---

## Key Concepts to Emphasize

### 1. Classification Methods Aren't Neutral

**Analogy to use:**
"Imagine dividing students into grade brackets. Equal interval is like A=90-100, B=80-89, C=70-79—fixed ranges. Quantile is like curving the test so exactly 20% get each grade, regardless of actual scores. Natural Breaks is like looking for natural gaps in the scores and dividing there."

**Key points:**
- Each method tells a different story
- Natural Breaks highlights genuine clusters but can produce odd break values
- Quantile ensures visual balance but can group very different values
- Equal Interval is intuitive but might create empty classes or unbalanced distributions
- Always check the actual values in the attribute table while choosing

**When students ask "Which is correct?":**
"The correct method depends on your data distribution and your message. Are you showing relative rankings (quantile)? Absolute thresholds (equal interval)? Natural groupings (natural breaks)? There's no universal answer."

### 2. Color Theory Basics

**Sequential palettes (single hue, light to dark):**
- Use for data with a clear progression: low to high, less to more
- Example: Population density, temperature, percentages
- ColorBrewer examples: YlGnBu, Reds, Purples

**Diverging palettes (two hues meeting at a midpoint):**
- Use for data with a meaningful middle value or when showing deviation
- Example: Temperature anomalies (cooler/warmer than average), election results (left/right)
- ColorBrewer examples: RdBu (red-blue), BrBG (brown-green)

**Qualitative palettes (distinct hues):**
- Use for categorical data with no inherent order
- Example: Land use types, political parties, regions
- ColorBrewer examples: Set1, Set2, Paired

**What to avoid:**
- Rainbow color ramps (no natural progression, misleading)
- Red-green combinations (problematic for colorblind viewers)
- Too many classes (more than 7 becomes hard to distinguish)

### 3. Join Pitfalls

**Common reasons joins fail:**

**Exact match required:**
- "AUS" ≠ "Australia" ≠ "aus"
- Leading/trailing spaces: "AUS " ≠ "AUS"
- Special characters or encoding issues

**Field type mismatch:**
- Joining text field to number field won't work
- Check field types in attribute table (hover over column header)

**NULL values appearing:**
- Codes in CSV don't match codes in shapefile
- Some countries might be missing from one dataset
- Solution: Open both attribute tables side-by-side and compare

**How to diagnose:**
1. Open both attribute tables
2. Sort both by the join field
3. Compare values visually
4. Look for inconsistencies

**Quick fixes:**
- Use Field Calculator to trim whitespace: `trim("field_name")`
- Convert text to uppercase for matching: `upper("field_name")`
- Create a new standardized join field if necessary

### 4. Label Placement Best Practices

**Core principles:**
- Labels should enhance, not clutter
- Use scale-dependent visibility liberally
- Text buffers are essential for readability
- Fewer labels are often better than more

**When to label:**
- Major cities, landmarks, or features your audience needs to recognize
- Features that provide orientation and context
- Elements specifically discussed in your map narrative

**When NOT to label:**
- Every single feature (leads to clutter)
- At scales where labels overlap
- When the feature is already obvious from context

**Placement hierarchy:**
- Points: Right of point, slightly above
- Lines: Along the line, following its curve
- Polygons: Centered, horizontal (or follow shape if very elongated)

---

## Live Demo Script

*This is a condensed version for quick reference during your demo. See detailed facilitation scripts above for full narration.*

### Setup (Before students arrive)
1. Open QGIS with Natural Earth countries already loaded
2. Have renewable energy CSV and world cities CSV in an easily accessible folder
3. Zoom to global extent showing all continents
4. Set QGIS interface to readable font size for projection

### Demo Sequence

**Part 1: CSV Join and Classification (15 minutes)**

```
1. Add delimited text layer
   - Browse to renewable_energy.csv
   - Geometry: No geometry
   - Add, Close

2. Join to countries
   - Countries layer → Properties → Joins
   - Add join: CSV layer, ISO_A3 → ISO_A3
   - OK

3. Verify join
   - Open attribute table
   - Scroll right to show new columns
   - Point out data presence

4. Graduated symbology
   - Symbology → Graduated
   - Value: renewable_energy_pct (or similar)
   - Color ramp: YlGnBu
   - Classes: 5
   - Mode: Natural Breaks → Classify → Apply
   - Compare with Quantile and Equal Interval

5. Customize
   - Invert color ramp if needed
   - Edit class labels to be human-friendly
   - Apply
```

**Part 2: Point Data and Labels (12 minutes)**

```
1. Add cities with coordinates
   - Add delimited text layer
   - Browse to worldcities.csv
   - Geometry: Point coordinates
   - X: lng, Y: lat
   - CRS: EPSG:4326
   - Add, Close

2. Filter to major cities
   - Right-click → Filter
   - "population" > 5000000
   - OK

3. Enable labels
   - Properties → Labels
   - Single Labels
   - Value: name field
   - Font: Arial, 10 pt
   - Buffer: white, 1.5 mm
   - Apply

4. Scale-dependent visibility
   - Rendering section
   - Check scale dependent visibility
   - Max: 1:50,000,000
   - Min: 1:100,000
   - Apply
   - Zoom in/out to demonstrate

5. [Optional] Expression-based labels
   - ε button next to Value
   - "name" || ' (' || format_number("population" / 1000000, 1) || 'M)'
   - OK
```

**Part 3: Proportional Symbols (8 minutes)**

```
1. Duplicate cities layer
   - Right-click → Duplicate
   - Rename: "Major Cities - Population Size"

2. Graduated symbology with size
   - Symbology → Graduated
   - Value: "population" / 1000000
   - Mode: Quantile, Classes: 4
   - Classify
   - Method: Change from Color to Size

3. Customize sizes
   - Min: 2.5 mm, Max: 10 mm
   - Choose single color (coral) with white stroke
   - Classify again

4. Edit class labels
   - Double-click each range
   - Rename: "1-4 M", "4-8 M", etc.

5. Match visibility
   - Rendering → Scale dependent visibility
   - Same as label layer
```

**Part 4: Layout Assembly (15 minutes)**

```
1. Create layout
   - Project → New Print Layout
   - Name: "Renewable Energy Map"
   - Page Properties: A3 Landscape

2. Add map
   - Add Map tool
   - Draw large rectangle (leave margins)

3. Add title
   - Add Label
   - "Global Renewable Energy Share by Country, 2023"
   - Font: 20-24 pt, bold, centered

4. Add legend
   - Add Legend
   - Item Properties: uncheck Auto update
   - Remove unnecessary layers
   - Rename remaining items
   - Adjust font size

5. Add scale bar
   - Add Scale Bar
   - Choose style
   - Adjust units and segments

6. Add credits
   - Add Label
   - "Data: Natural Earth, Our World in Data | Map: [Your Name], 2024"
   - Font: 8 pt

7. Export
   - Layout → Export as Image (PNG, 300 DPI)
   - Layout → Export as PDF
```

**Part 5: Accessibility Check (5 minutes)**

```
1. Screenshot your layout

2. Open Color Oracle or online simulator
   - Show Deuteranopia view
   - Check if classes remain distinguishable

3. Check contrast
   - WebAIM contrast checker
   - Test label colors against backgrounds

4. Verify font sizes
   - Title: 20+ pt
   - Labels: 10+ pt
   - Credits: 8+ pt
```

---

## Discussion Prompts

Use these throughout the session to encourage critical thinking and engagement.

### During Design Show-and-Tell
- "Where does your eye go first in this map? What design choice caused that?"
- "How would this map look different if we changed the color palette?"
- "Can you identify the visual hierarchy? What's primary, secondary, tertiary?"
- "Who is the audience for this map? How do you know?"
- "What would someone with color blindness see in this map?"

### During Classification Demo
- "Look at the class ranges for quantile vs equal interval—what's different?"
- "Which method would you use if you wanted to show: (a) Countries objectively meeting a 25% renewable threshold? (b) The top 20% of performers? (c) Natural groupings in the data?"
- "How might changing the number of classes (3 vs 5 vs 7) change interpretation?"
- "Should we include countries with no data? How should they be symbolized?"

### During Label Activity
- "When is it better to have no label than a cluttered label?"
- "Why use scale-dependent visibility instead of just making labels smaller?"
- "How do you decide which cities to label?"

### During Layout Assembly
- "What's the first thing you want viewers to understand from this map?"
- "How does your layout guide the eye from title → map → legend → details?"
- "If you had to remove one element from this layout, what would it be? Why?"
- "How would you adapt this layout for: (a) A scientific journal? (b) A newspaper? (c) Social media?"

### During Accessibility Check
- "Why is accessibility not just 'nice to have' but essential?"
- "Can you think of contexts where poor color choices could have serious consequences?" (Medical data, emergency response, etc.)
- "How would you describe this map to someone who can't see it?"

---

## Common Student Issues

### Technical Issues

#### 1. Join shows all NULL values

**Symptoms:**
- New columns appear in attribute table but contain NULL/blank
- Symbology doesn't work because field has no data

**Diagnosis:**
- Open both attribute tables side by side
- Sort by join field in both
- Compare values—look for mismatches

**Common causes:**
- Case sensitivity: "AUS" vs "aus"
- Extra spaces: "AUS " vs "AUS"
- Different coding schemes: "AUS" vs "AU" vs "Australia"
- Encoding issues (special characters)

**Solutions:**
1. Use Field Calculator to standardize:
   - `trim("ISO_A3")` to remove spaces
   - `upper("ISO_A3")` to convert to uppercase
2. Create new join field with consistent codes
3. Check CSV encoding (UTF-8 recommended)
4. Manually edit problematic values in CSV before importing

**Prevention:**
Always verify join immediately by opening attribute table before proceeding to symbology.

#### 2. Graduated symbology shows no variation (all one color)

**Symptoms:**
- All features the same color after applying graduated symbology
- No legend classes appear

**Common causes:**
- Wrong field selected (text field instead of numeric)
- Field contains no data (all NULL)
- All values are identical
- Student forgot to click "Classify" button
- Field imported as text instead of number

**Solutions:**
1. Verify field type: hover over column header in attribute table
2. Click "Classify" button explicitly
3. Check data has variation: open attribute table and sort by field
4. If field is text type, create new numeric field:
   - Field Calculator → Create new field
   - Type: Decimal (real)
   - Expression: `to_real("field_name")`

**Prevention:**
Teach students to always check field type before applying symbology.

#### 3. Labels overlap and are unreadable

**Symptoms:**
- Text overlapping other text
- Labels covering important features
- Cluttered appearance

**Solutions:**
1. **Reduce number of labels:**
   - Filter to fewer features (higher population threshold)
   - Use scale-dependent visibility
2. **Improve placement:**
   - Labels tab → Placement → Try "Around Point" or "Free (Angled)"
   - Rendering → Check "Show all labels..." (QGIS will try harder to fit them)
3. **Manually move labels (for final maps):**
   - Enable Label Toolbar: View → Toolbars → Label Toolbar
   - Use "Move Label" tool to drag individual labels
4. **Add backgrounds:**
   - Labels tab → Background → Enable
   - White or semi-transparent fill

**Prevention:**
Emphasize "less is more" with labels. Start with fewer, add more only if needed.

#### 4. Wrong field type for coordinates when loading CSV

**Symptoms:**
- Points appear in wrong location (e.g., all in null island at 0,0)
- Points don't appear at all

**Common causes:**
- Swapped X and Y (lng/lat vs lat/lng)
- Wrong CRS selected
- Coordinate fields contain non-numeric characters

**Solutions:**
1. Remove layer and re-add with correct X/Y assignment
2. Ensure CRS is EPSG:4326 (WGS 84) for lat/lng data
3. Check CSV in text editor—ensure coordinate columns are clean numbers

#### 5. Print Layout map doesn't update

**Symptoms:**
- Changed symbology in main canvas but layout still shows old version
- Map appears blank or frozen

**Common causes:**
- "Lock layers" or "Lock styles" is checked in Map Item Properties
- Layout hasn't been refreshed

**Solutions:**
1. Select map item → Item Properties → uncheck "Lock layers" and "Lock styles"
2. Click "Refresh" button in Map Item Properties
3. If still not working, delete map item and re-add

**Prevention:**
Only check "Lock layers/styles" after finalizing design.

#### 6. Legend shows too many items or wrong labels

**Symptoms:**
- Legend includes every layer in project
- Legend shows technical field names like "ne_50m_admin_0_countries_renewable_energy_pct"

**Solutions:**
1. In Legend Item Properties, uncheck "Auto update"
2. Select unwanted items and click red minus button to remove
3. Select items to rename → click pencil/edit icon → enter friendly name
4. Reorder items by dragging up/down

**Common mistake:**
Students forget to uncheck "Auto update" before editing, so changes get overwritten.

#### 7. Exported image is blurry or low quality

**Symptoms:**
- PNG looks pixelated when zoomed in
- Text is fuzzy or hard to read

**Solutions:**
1. Increase export DPI: `Layout → Export as Image → Resolution: 300 DPI`
2. For print: always use 300 DPI
3. For web/screen: 150 DPI is usually sufficient
4. Alternative: Export as PDF for vector quality (scales infinitely)

### Conceptual Confusion

#### 8. "Why doesn't my CSV show on the map?"

**Misunderstanding:**
Student expects CSV to automatically appear as map features.

**Explanation:**
"CSVs are just data tables—they don't have geometry (shapes). You need to either:
1. **Join** the data to a layer that has geometry (like we did with countries), OR
2. Load with coordinates if the CSV has lat/lng columns (like we did with cities)"

**Demonstration:**
Show how the renewable energy CSV appears in Layers panel but not on canvas, vs the cities CSV which has points.

#### 9. "What's the difference between Classification and Categorization?"

**Student confusion:**
Graduated vs Categorized symbology—when to use which?

**Explanation:**
- **Graduated (Classification):** For continuous numeric data. Divides into ranges. Example: population 0-100, 100-500, 500-1000
- **Categorized:** For discrete categories. Each unique value gets its own symbol. Example: Land use types (forest, urban, water)

**Analogy:**
"Graduated is like letter grades (A=90-100, B=80-89...). Categorized is like team jerseys (each team has its own color)."

#### 10. "Why do my class breaks change when I switch methods?"

**Student observation:**
Quantile shows different ranges than Equal Interval.

**Explanation:**
"That's the point! Each method divides the data differently:
- **Equal Interval:** Splits the *number line* into equal parts (e.g., 0-20%, 20-40%, 40-60%)
- **Quantile:** Splits the *number of features* equally (e.g., 20% of countries in each class, regardless of values)
- **Natural Breaks:** Finds natural clusters in the data distribution"

**Show visually:**
Open attribute table, sort by the field, and point out how values are distributed across classes with different methods.

#### 11. "Why can't I see my labels when zoomed out?"

**Student confusion:**
Set scale-dependent visibility but doesn't understand why labels disappear.

**Explanation:**
"Scale-dependent visibility is intentional—labels that are readable at city scale become clutter at continental scale. The map should show different information at different zoom levels."

**Demonstration:**
Zoom smoothly from close to far, narrating: "At this scale, street names are useful. At this scale, city labels are useful. At this scale, only country names make sense."

---

## Wrap-up & Preview

### Session Summary

**What students accomplished today:**
- Learned to join tabular data to spatial layers
- Applied three different classification methods and understood when to use each
- Created intelligent labels with scale-dependent visibility
- Built proportional symbols based on data attributes
- Assembled a professional print layout with all essential cartographic elements
- Checked their maps for accessibility

**Key skills gained:**
- Understanding that classification method = design choice = impacts interpretation
- Knowing when to use sequential, diverging, and qualitative color palettes
- Troubleshooting joins (the #1 GIS frustration)
- Making intentional design decisions rather than accepting defaults

### Assessment of Understanding

**Quick formative check (show of hands or poll):**
- "Who feels confident joining CSV data to shapefiles?"
- "Who can explain the difference between quantile and equal interval?"
- "Who successfully exported a professional-looking layout?"

**Address any gaps:**
If majority struggled with a concept, briefly revisit it or point to resources for further study.

### Preview of Week 3

**What's coming:**
"Next week we dive into administrative and statistical boundaries. You'll work with real census data—joining socio-economic indicators like income, education, and access to services to geographic areas. This is where GIS becomes a tool for social analysis and equity work."

**Why it matters:**
"Understanding how to work with census geographies (like SA2 in Australia or census tracts in the US) opens up enormous analytical possibilities: identifying areas of disadvantage, analyzing service gaps, understanding demographic patterns."

**What to prepare:**
- Download Week 3 datasets: SA2 boundaries and SEIFA data (or local equivalents)
- Read the pre-work materials on understanding statistical boundaries
- Review your Week 2 layout—we'll use similar principles next week

### Assignment Reminders

**Due this week:**
1. Completed QGIS project file with all activities (joins, symbology, labels)
2. Exported layout: PNG or PDF of your renewable energy map
3. Week 2 reflection entry

**What good work looks like:**
- Join successfully completed (no NULL values)
- Thoughtful choice of classification method with justification in reflection
- Clean, readable labels that don't clutter
- Professional layout with hierarchy (title prominent, legend clear, credits present)
- Passes basic accessibility checks (colorblind-safe palette, adequate contrast)

**Common submission mistakes to avoid:**
- Submitting the wrong QGIS version (must be .qgz, not .qgs)
- Forgetting to export the layout
- Not documenting design choices in reflection
- Technical field names still visible in legend

### Resources for Continued Learning

**Recommended for this week:**
- ColorBrewer documentation: understanding when to use each palette type
- QGIS documentation on label expressions: for more advanced data-driven labels
- Map critique exercises: find maps in the news and analyze their design choices

**Office hours/support:**
- "I'm available [days/times] for troubleshooting"
- "Post questions in [forum/discussion board]—chances are others have the same question"
- "Bring your maps to next week's session for peer feedback"

### Closing Motivation

**Final thought:**
"The difference between a mediocre map and a great map isn't technical skill—it's intentionality. Every choice you made today (classification method, color ramp, label placement, layout hierarchy) communicates something to your audience. As you practice, these choices become intuitive. You're not just learning software; you're learning a visual language."

**Encouragement:**
"If your layout doesn't look perfect yet, that's completely normal. Design takes practice. Keep collecting examples of maps you admire, and keep asking 'why does this work?' Your eye will develop faster than your hands, but your hands will catch up."

**Thank students:**
"Great work today. Looking forward to seeing your final layouts!"

---

## Additional Facilitator Tips

### Time Management

**If running behind:**
- **Skip optional elements:** North arrow, inset map, expression-based labels
- **Reduce hands-on time:** Do more as live demo with less independent practice
- **Combine activities:** Demonstrate labels and scale-dependent visibility together without separate hands-on time
- **Cut accessibility check to mention only:** "Remember to check colorblind-safe palettes; see student guide for tools"

**If ahead of schedule:**
- **Add advanced challenges:**
  - Create rule-based symbology (e.g., highlight countries above 50% renewable with special pattern)
  - Add inset map showing zoomed area context
  - Create second layout page showing different classification method for comparison
- **Peer review activity:** Students swap screens and give feedback on each other's layouts
- **Map critique:** Analyze additional real-world maps as a group

### Handling Different Skill Levels

**For students struggling:**
- Have pre-prepared project files at each stage (post-join, post-symbology, etc.) so they can catch up
- Pair with a peer for troubleshooting
- Provide simplified version: skip proportional symbols, focus on core tasks
- Schedule individual check-in during hands-on time

**For advanced students:**
- Challenge extensions:
  - Create bivariate map (two variables shown simultaneously with color and pattern)
  - Use geometry generator for custom symbols
  - Create atlas/series showing multiple countries automatically
  - Design mobile-responsive layout (vertical orientation, larger text)
- Encourage them to help peers (builds teaching skills and community)

### Remote/Hybrid Considerations

**Screen sharing:**
- Share entire screen, not just QGIS window (students need to see mouse movements, dialogs)
- Use zoom/annotation tools to highlight specific buttons
- Verbally narrate every click: "Now I'm clicking the Joins tab... now clicking the green plus button..."

**Engagement strategies:**
- More frequent check-ins: "Put a thumbs up in chat if your join worked"
- Use breakout rooms for hands-on practice with peer support
- Have students share screens to show their work
- Record the session for students to review later

**Technical support:**
- Have a co-facilitator monitoring chat for questions
- Create shared troubleshooting document where students can post issues
- Consider using a second screen to monitor student questions while demoing

### Accessibility for Your Session

**Make your teaching accessible:**
- Describe visual elements verbally: "The button with the green plus symbol..."
- Use high-contrast QGIS theme for projection
- Provide all materials in multiple formats (slides, written guide, video)
- Allow extra time for students with processing or motor challenges
- Offer alternative assignment formats if requested (e.g., written analysis instead of creating layout)

### Building a Supportive Learning Environment

**Normalize mistakes:**
- Share your own: "I always forget to click Classify the first time"
- Celebrate errors as learning: "Great question—that's a common issue, let's troubleshoot together"
- Use mistakes as teaching moments for the whole class

**Encourage questions:**
- "There are no silly questions—GIS is complicated and everyone gets stuck"
- Pause regularly: "What questions do we have so far?"
- Answer with patience, even if you've explained before

**Foster peer learning:**
- "Has anyone figured out how to fix this issue? Can you share?"
- Acknowledge student expertise: "Great solution—I hadn't thought of that approach"
- Create buddy system for troubleshooting

**Cultural responsiveness:**
- Use diverse place name examples
- Be aware that some cultures read right-to-left (affects layout design discussion)
- Recognize different levels of prior tech experience
- Avoid jargon; explain acronyms (CSV, CRS, DPI, etc.)

---

## Final Checklist: Are You Ready?

**24 hours before session:**
- [ ] All datasets tested and accessible
- [ ] Complete example project built and saved
- [ ] Presentation/demo materials prepared
- [ ] Room/tech setup confirmed (projector, internet, etc.)
- [ ] Student guide reviewed
- [ ] Common errors screenshots prepared

**1 hour before session:**
- [ ] QGIS open with Natural Earth loaded
- [ ] Datasets folder open and ready to browse
- [ ] External monitor/projector tested and readable
- [ ] Example maps for show-and-tell ready to display
- [ ] Chat/Q&A monitoring plan set (if remote)
- [ ] Backup plans ready (alternative datasets, pre-built projects at different stages)

**During session:**
- [ ] Energetic and encouraging tone
- [ ] Regular check-ins on student progress
- [ ] Circulating during hands-on time (in-person) or monitoring chat (remote)
- [ ] Celebrating successes and normalizing struggles
- [ ] Sticking to time while being flexible for questions

**After session:**
- [ ] Collect student feedback (what worked, what was confusing)
- [ ] Note any technical issues that arose for future prep
- [ ] Make notes on timing adjustments for next offering
- [ ] Follow up on any unanswered questions

---

## Good luck! Remember: Your enthusiasm for cartography is contagious. Have fun with it!
