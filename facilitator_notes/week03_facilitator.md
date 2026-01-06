# Week 3 Facilitator Notes: Administrative Boundaries & Demographics

## Session Overview

**Duration:** 2-3 hours (depending on class format)
- Welcome & recap: 10 min
- Live demo: 30-40 min
- Student work time: 60-90 min
- Discussion & troubleshooting: 20-30 min
- Wrap-up: 10 min

**Learning Objectives:**

By the end of this session, students will be able to:
1. Explain the role of administrative and statistical boundaries in socio-economic analysis
2. Perform attribute joins between polygon boundaries (e.g., SA2/LGA) and tabular datasets (e.g., SEIFA, ACS)
3. Aggregate and summarize data across geographic levels (count points in polygons, dissolve boundaries)
4. Use the Field Calculator and selection tools to create derived indicators
5. Critically evaluate how boundary choices affect analytical outcomes

**Materials Needed:**

- QGIS installed and tested on all student machines
- Boundary data: SA2 (Australia) or Census Tracts (US) shapefiles or GeoPackages
- Tabular data: SEIFA indexes (Australia) or ACS data (US) in CSV format
- Projector/screen sharing capability for live demo
- Backup datasets in case student downloads fail
- Student handout: Week 3 activity guide (optional print version)

**Data Requirements:**

- ASGS SA2/SA3/LGA boundaries (2021 edition for Australia)
- SEIFA 2021 indexes (IRSD, IRSAD, IER, IEO) by SA2
- Optional: Previous year boundaries for demonstrating boundary changes
- Optional: LGA boundaries for comparison exercises

---

## Before Class Checklist

### Technical Preparation

- [ ] **Test data downloads:** Verify all links in the student materials work
  - ABS ASGS boundaries page loads correctly
  - SEIFA data downloads without errors
  - File formats are compatible with current QGIS version

- [ ] **Prepare backup datasets:** Have a USB drive or shared folder with:
  - SA2 boundaries (2021)
  - SEIFA CSV files
  - Pre-joined sample layer in case students get stuck

- [ ] **Test the join workflow:**
  - Load SA2 boundaries
  - Load SEIFA CSV
  - Perform attribute join
  - Verify field names and data types match
  - Check for common issues (leading zeros, field type mismatches)
  - Export joined layer to GeoPackage

- [ ] **Verify Field Calculator expressions:**
  - Test all example expressions from student materials
  - Prepare additional examples for common student questions

- [ ] **Check visualization:**
  - Create choropleth map with graduated symbology
  - Test different classification methods
  - Prepare color ramp recommendations (avoid red/green for accessibility)

### Content Preparation

- [ ] Review the MAUP (Modifiable Areal Unit Problem) concept
- [ ] Prepare local examples of boundary changes (e.g., recent SA2 splits/merges)
- [ ] Review SEIFA methodology and what each index measures
- [ ] Prepare ethical discussion prompts about mapping disadvantage
- [ ] Review correspondence files for boundary changes between years
- [ ] Have ABS/Census documentation links ready for reference

### Classroom Setup

- [ ] Test projector/screen sharing
- [ ] Load demonstration project with all required layers
- [ ] Prepare troubleshooting space (help queue, dedicated support station)
- [ ] Have Q&A document ready for capturing common issues
- [ ] Print emergency troubleshooting guide (optional)

---

## Session Flow (with timing)

### 1. Welcome & Recap (10 min)

**Opening:**
- "Last week you learned vector basics—points, lines, polygons. This week, we're adding meaning to those shapes by joining data."
- Quick poll: "Who has worked with VLOOKUP or database joins before?"
- Set expectations: "Joins can be frustrating the first time—that's normal. Today is about understanding the logic AND troubleshooting when things go wrong."

**Recap connections:**
- Week 1: File formats (shapefiles vs GeoPackages) matter for joins
- Week 2: Attribute tables—joins add new columns to existing tables
- Today: Bringing external data (census, demographics) into spatial layers

**Preview the workflow:**
1. Understand what boundaries represent
2. Inspect and prepare tabular data
3. Perform the join
4. Create derived indicators
5. Visualize patterns
6. Think critically about what the map shows and hides

---

### 2. Live Demo (30-40 min)

**Key message before starting:**
"I'm going to make mistakes during this demo. Watch how I troubleshoot—that's the most valuable skill you'll learn today."

#### Part A: Understanding Boundaries (8-10 min)

**Load SA2 boundaries:**
```
Layer > Add Layer > Add Vector Layer...
Navigate to SA2_2021_AUST_GDA2020.shp (or .gpkg)
```

**Open attribute table:**
- "Let's explore what we have here."
- Point out key fields:
  - `SA2_CODE_2021` or `SA2_CODE21` (unique identifier)
  - `SA2_NAME21` (human-readable name)
  - `SA3_CODE21`, `SA4_CODE21` (parent geographies)
  - `AREASQKM21` (area metadata)

**Demonstrate hierarchy:**
- Open Layer Properties > Symbology > Categorized
- Value: `SA3_NAME21`
- Show how SA2 areas nest within SA3 regions
- "Notice how smaller areas aggregate into larger ones—this is a spatial hierarchy."

**Key concepts to emphasize:**
- **Statistical boundaries** (SA2): Designed for data collection; boundaries aim for population homogeneity
- **Administrative boundaries** (LGA): Used for governance; based on political/historical divisions
- **Why this matters:** Same data at different scales tells different stories (foreshadow MAUP discussion)

**Compare boundary types (if time allows):**
- Load LGA boundaries alongside SA2
- Show how they don't align perfectly
- "LGAs don't nest cleanly into SA2s—this creates challenges when converting between systems"

#### Part B: Inspect Tabular Data (5-7 min)

**Load SEIFA CSV:**
```
Layer > Add Layer > Add Delimited Text Layer...
Select SEIFA_2021_SA2.csv
File Format: CSV
Geometry Definition: No geometry (attribute only table)
```

**Open attribute table:**
- "We're looking for two things: the join key and our indicators."
- Show the geographic code field: `SA2_CODE_2021`
- Show SEIFA fields: `IRSD_Score`, `IRSD_Decile`, `IRSAD_Score`, etc.

**Explain SEIFA indexes briefly:**
- **IRSD** (Index of Relative Socio-economic Disadvantage): Summarizes disadvantage
- **IRSAD** (Index of Relative Socio-economic Advantage and Disadvantage): Captures both ends
- **IER** (Index of Economic Resources): Income, assets
- **IEO** (Index of Education and Occupation): Skills, employment
- **Deciles:** 1 = most disadvantaged 10%, 10 = least disadvantaged 10%

**Check data quality:**
- "Always check your data before joining!"
- Sort by SA2_CODE—look for consistency
- Check for NULL values
- **IMPORTANT:** Verify codes are text format (show leading zeros if present)

**Common pitfall demonstration (if time):**
- Open CSV in Excel → show how leading zeros disappear
- "This is why we always treat geographic codes as text, never as numbers"

#### Part C: Perform the Join (10-12 min)

**Set up the join:**
```
Right-click SA2 layer > Properties > Joins tab
Click the green + button
```

**Configure join settings:**
- Join layer: SEIFA_2021_SA2
- Join field: `SA2_CODE_2021` (from CSV)
- Target field: `SA2_CODE21` (from shapefile)
- Joined fields: Leave blank (include all) or select specific indicators
- Custom field name prefix: `SEIFA_` (recommended to avoid confusion)
- Check "Cache join layer in virtual memory" for performance

**Apply and verify:**
- Click OK
- Open SA2 attribute table
- "You should now see new columns with the SEIFA_ prefix"
- Scroll right to see joined fields
- Click on a few rows: "Do the values look reasonable?"

**Troubleshooting demonstration:**
- If join fails (or simulate failure): "Let's check our join fields"
- Right-click > Properties > Fields
- Check data types: both should be Text/String
- If one is Integer: "We need to convert it—let me show you how"

**Field type fix (if needed):**
```
Field Calculator > Create new field
Output field name: SA2_CODE_text
Output field type: Text (string)
Expression: to_string("SA2_CODE21")
```

**Make join permanent:**
```
Right-click SA2 layer > Export > Save Features As...
Format: GeoPackage
File name: data/processed/week03/sa2_with_seifa.gpkg
CRS: EPSG:7844 (GDA2020) or keep project CRS
Click OK
```

- Remove temporary layers
- Add the new permanent layer
- "Now the join is baked in—no dependencies on the original CSV"

#### Part D: Create Derived Indicators (7-10 min)

**Open Field Calculator:**
- Open attribute table of permanent layer
- Click calculator icon or Ctrl+I

**Example 1: Disadvantage categories**
```
Create output field: disadvantage_category
Output field type: Text (string)
Expression:
CASE
  WHEN "SEIFA_IRSD_Decile" <= 2 THEN 'High disadvantage'
  WHEN "SEIFA_IRSD_Decile" <= 5 THEN 'Moderate disadvantage'
  WHEN "SEIFA_IRSD_Decile" <= 8 THEN 'Low disadvantage'
  ELSE 'Very low disadvantage'
END
```

- Click OK
- Sort by new field to verify it worked

**Example 2: Flag extreme disadvantage**
```
Create output field: extreme_disadvantage
Output field type: Integer
Expression:
CASE
  WHEN "SEIFA_IRSD_Decile" = 1 THEN 1
  ELSE 0
END
```

**Key teaching points:**
- Field Calculator uses SQL-like syntax
- Field names in double quotes, text values in single quotes
- CASE statements are powerful for categorization
- Always check output by sorting/filtering after creation

#### Part E: Spatial Aggregation (8-10 min)

**Say:** "Now let's learn to aggregate data—counting points in polygons and rolling up data from smaller to larger geographies. This is essential for comparing areas fairly."

**Demo 1: Count Points in Polygon**

**Do:**
```
Vector > Analysis Tools > Count Points in Polygon
Polygons: SA2 layer (or LGA)
Points: Load a point layer (cities, facilities, schools)
Count field name: facility_count
Run
```

**Say:** "This counts how many points fall within each polygon. Simple but powerful—how many hospitals per LGA? How many schools per SA2?"

**Show result:**
- Open attribute table → sort by new count field
- "This LGA has 15 hospitals, this one has 2. But wait—raw counts don't tell the full story. A bigger LGA naturally has more of everything."

**Demo 2: Aggregate to Roll Up Boundaries**

**Say:** "Sometimes you want to roll up detailed data to a larger scale. Let's start with something simple—using your Week 1 countries data to calculate population by continent."

**Warm-up with familiar data:**
```
Processing > Toolbox > search "Aggregate"
(Under Vector geometry > Aggregate)

Input: ne_110m_admin_0_countries (Week 1 data)
Group by expression: "CONTINENT"
Click ... next to Aggregates to configure:
  - CONTINENT → First value
  - POP_EST → Sum
  - NAME → Count
Run
```

**Say:** "Look at that—177 countries became 7 continent polygons. Each now has total population and country count. That's aggregation!"

**Show the result:**
- Open attribute table: "Asia has X billion people, Africa has Y countries"
- "This is exactly what a database GROUP BY does, but with geometry too"

**Now apply to boundaries:**
```
Input: SA2 layer with SEIFA data
Group by expression: "SA3_CODE21"
Aggregates:
  - SA3_NAME21 → First value
  - population → Sum
  - IRSD_score → Mean
Run
```

**Say:** "Same technique, now rolling up SA2s into SA3s with totals and averages."

**Tip:** "Aggregate is better than Dissolve for this because it has a clear interface for choosing statistics. Dissolve hides these options and is mainly for merging geometries."

**Compare visually:**
- Toggle between SA2 and SA3 views
- "See this pocket of high disadvantage in the SA2 map? It's invisible at SA3 scale because it's averaged with surrounding areas."

**Key teaching moment:**
"Aggregation is powerful but hides detail. Always ask: What level of geography does my analysis question require?"

**Example 3: Population density (if you have population data)**
```
Create output field: pop_density
Output field type: Decimal (double)
Expression:
CASE
  WHEN "AREASQKM21" > 0 THEN "Tot_P_P" / "AREASQKM21"
  ELSE 0
END
```

- "Notice the CASE statement prevents division by zero"

---

### 3. Student Work Time (60-90 min)

**Activities students should complete:**

1. Activity 1: Understand boundary hierarchies (15 min)
2. Activity 2: Inspect and prepare tabular data (10 min)
3. Activity 3: Perform the attribute join (15 min)
4. Activity 4: Create derived indicators (15 min)
5. Activity 5: Visualize patterns with choropleth maps (15 min)
6. Activity 6: Aggregate and summarize by geography (20 min)
7. Activity 7: Select and filter by attributes (10-15 min)
8. Activity 8: Quality assurance (10-15 min)

**Facilitation strategy:**

- **First 15 min:** Circulate actively—catch setup issues early
- **Mid-session checkpoint (30 min):** Quick poll—"Who has successfully joined data?"
- **Troubleshooting mode:** Keep common issues on whiteboard/shared doc
- **Peer support:** Pair students who finish early with those struggling

**Walking around prompts:**
- "Show me your attribute table—did the join work?"
- "How many records matched vs. didn't match?"
- "What spatial patterns are you seeing in the map?"
- "Try changing the classification method—what happens?"

**Common stopping points:**
- Join shows 0 matched features → field name/type mismatch
- Join works but many NULLs → code formatting issue (leading zeros)
- Field Calculator errors → syntax mistakes (quotes, field names)
- Map looks strange → wrong field selected, NULL handling

---

### 4. Discussion & Troubleshooting (20-30 min)

**Structured discussion prompts:**

#### A. Technical Debrief (10 min)

- "What was the hardest part of today's workflow?"
- "Who encountered join errors? What fixed them?"
- "Share one thing you learned from troubleshooting"

**Capture common issues on board:**
- Lead a quick "issue inventory" session
- Group similar problems
- Have students who solved them explain solutions

#### B. Critical Analysis (10-15 min)

**Prompt 1: The power of boundaries**
- "Open your SA2 map and your LGA map side by side."
- "Pick one LGA—what variation exists within it at the SA2 level?"
- "If a policymaker only sees LGA-level data, what are they missing?"

**Expected insights:**
- Aggregation hides local variation
- "Averages lie"—wealthy and disadvantaged areas can share an LGA
- Decision-making based on wrong scale leads to poor targeting

**Prompt 2: MAUP (Modifiable Areal Unit Problem)**
- "We've just experienced MAUP firsthand—the same data looks different at SA2 vs LGA."
- "When might this cause problems in real-world analysis?"
- "How do you choose the 'right' boundary?"

**Key concept to emphasize:**
- There is no perfect boundary
- Choice depends on research question and data availability
- Always acknowledge boundary effects in reporting

**Prompt 3: Ethics of mapping disadvantage**

This is a critical discussion—allocate sufficient time.

- "We've just created maps showing where disadvantaged people live."
- "What are the benefits of this data being public?"
- "What are the risks?"

**Expected responses (guide toward these):**

*Benefits:*
- Resource allocation—funding goes where it's needed
- Advocacy—communities can use data to demand services
- Transparency—holds government accountable
- Research—enables evidence-based policy

*Risks:*
- Stigmatization—labeling neighborhoods as "poor" affects property values, identity
- Determinism—maps imply problems are caused by place, not policy
- Surveillance—can be used to police or exclude communities
- Misinterpretation—people assume correlation = causation

**Follow-up questions:**
- "Who gets to decide how disadvantage is measured?"
- "SEIFA uses census variables like income, education, employment—what does it miss?" (e.g., cultural wealth, social capital, community resilience)
- "How might affected communities want this data visualized differently?"
- "When should we NOT make a map?" (sometimes aggregated statistics are more ethical)

**Ethical principles to establish:**
1. **Do no harm:** Consider how maps might stigmatize or surveil
2. **Involve communities:** People being mapped should inform how they're represented
3. **Context matters:** Never map disadvantage without explaining structural causes
4. **Aggregation protects privacy:** Don't map individual-level data; use appropriate spatial units
5. **Critique your tools:** SEIFA reflects policy priorities, not objective truth

**Real-world example:**
- Redlining maps in the US—how "objective" data was used to exclude
- Or: How Australian SA boundaries are redrawn to maintain population balance but disrupt community boundaries

---

### 5. Wrap-up & Preview (10 min)

**Key takeaways—ask students to share:**
- "In one sentence, what's the most important thing you learned today?"

**Facilitator summary:**
- "Joins connect spatial and non-spatial data—the foundation of GIS analysis"
- "Always verify your joins—check counts, look for NULLs, sort to spot errors"
- "Boundaries shape stories—be critical about what aggregation hides"
- "Mapping disadvantage requires ethical reflection, not just technical skill"

**Preview Week 4:**
- "Next week: Raster and terrain analysis"
- "You'll work with elevation data to create hillshades, slope maps, and identify flood-prone areas"
- "The connection: You'll overlay terrain risk with the disadvantage data you just created—'Which disadvantaged communities face highest flood risk?'"
- "Action item: Download your DEM tiles before next class (check Week 4 materials for links)"

**Submission reminder:**
- QGIS project file saved and organized
- Joined layer exported to `data/processed/week03/`
- At least one derived field created
- Exported map image showing spatial patterns
- Reflection completed (emphasize documenting troubleshooting)

**Q&A:**
- Open floor for final questions
- Point students to support resources (office hours, discussion forum, troubleshooting guide)

---

## Key Concepts to Emphasize

### 1. Boundary Hierarchies

**What students need to understand:**
- Smaller geographies nest within larger ones (SA2 → SA3 → SA4 → State)
- This enables aggregation but also creates analytical choices
- "Roll-up" is easy; "drill-down" requires detailed data

**Teaching tip:**
Use a Russian nesting doll analogy—each level contains the ones below.

**Common misconception:**
Students assume postcodes/ZIP codes are good for analysis. They're not—they're designed for mail delivery, cross meaningful boundaries, and change frequently.

### 2. SEIFA Indexes (or equivalent socio-economic measures)

**What students need to understand:**
- SEIFA measures relative disadvantage, not absolute poverty
- Different indexes capture different dimensions (disadvantage vs advantage, economic vs education)
- Deciles rank areas—1 is most disadvantaged 10% nationally
- Scores are standardized (mean ~1000, SD ~100)—higher IRSD = less disadvantaged

**Teaching tip:**
"Decile 1 doesn't mean everyone is poor—it means this area has more disadvantage indicators than 90% of Australia."

**Common misconception:**
"This area has low disadvantage, so everyone is wealthy." Wrong—it's an average. Rich and poor people live everywhere.

### 3. Attribute Joins

**What students need to understand:**
- Joins link tables using a common key (like VLOOKUP in Excel)
- Both fields must have same data type and format
- Unmatched records result in NULL values—always check!
- Joins are temporary unless exported

**Teaching tip:**
Draw the join logic on whiteboard:

```
SA2 Shapefile          SEIFA CSV
SA2_CODE | Geometry    SA2_CODE | IRSD_Score
---------------------  -----------------------
10101    | polygon     10101    | 950
10102    | polygon     10102    | 1020
                         ↓ JOIN ↓
SA2 Shapefile (with SEIFA)
SA2_CODE | Geometry | IRSD_Score
10101    | polygon  | 950
10102    | polygon  | 1020
```

**Common misconception:**
"The join didn't work because I see NULL values." Sometimes NULL is correct—not all areas have data (e.g., industrial zones with no residents).

### 4. MAUP (Modifiable Areal Unit Problem)

**What students need to understand:**
- Analytical results change based on how you zone/aggregate data
- Two components:
  - **Scale effect:** SA2 vs LGA produces different patterns
  - **Zoning effect:** Different boundary systems at same scale differ
- No "correct" scale—choice depends on research question

**Teaching tip:**
Show the same data at SA2 and LGA levels side-by-side. Ask: "Which is true?" Answer: "Both—they answer different questions."

**Real-world example:**
"Crime rates look different aggregated by police district vs census tract—neither is wrong, but policymakers might make different decisions."

### 5. Why Geography Matters for Analysis

**What students need to understand:**
- Spatial patterns reveal processes (clustering, segregation, sprawl)
- Context matters—disadvantage in urban vs rural areas looks different
- Maps communicate differently than tables—they make inequality visible
- Geographic data enables spatial justice questions

**Teaching tip:**
"A table shows 'Area X has high disadvantage.' A map shows 'All high disadvantage areas are on the city's edge, far from transit and jobs.' The pattern tells a story about structural inequality."

---

## Live Demo Script (Detailed)

Use this as a detailed reference. Adapt based on your teaching style and time constraints.

### Setup (Before Students Arrive)

1. Open QGIS with blank project
2. Set project CRS to EPSG:7844 (GDA2020 for Australia) or appropriate local CRS
3. Have file browser windows open to data folders
4. Load Week 3 slide deck (if using)
5. Test screen sharing / projector setup

### Demo Flow

#### 1. Loading Boundaries (5 min)

**Say:** "Let's start by loading our SA2 boundaries. These are statistical areas designed by the Australian Bureau of Statistics."

**Do:**
```
Layer > Add Layer > Add Vector Layer...
Source: [Navigate to SA2_2021_AUST_GDA2020.shp or .gpkg]
Click Add
```

**Say:** "Notice it loads quickly—we're only loading geometry and attributes, no fancy rendering yet."

**Open attribute table:**
```
Right-click layer > Open Attribute Table
```

**Say (while pointing):**
- "Here's our unique identifier: SA2_CODE21—remember this, we'll need it for joining."
- "SA2_NAME21 is human-readable—like 'Canberra - City' or 'Bondi Beach'."
- "SA3_CODE21, SA4_CODE21—these are parent geographies. SA2s nest inside SA3s."
- "AREASQKM21—useful for calculating densities later."

**Demonstrate hierarchy:**
```
Right-click layer > Properties > Symbology
Change from Single Symbol to Categorized
Value: SA3_NAME21
Click Classify
```

**Say:** "Now each color represents a different SA3 region. See how multiple SA2 polygons share a color? They're grouped into larger statistical areas. This hierarchy lets us aggregate up—sum all SA2 populations to get SA3 totals."

**Teaching moment:** "Why do we have these nested levels? Because different questions need different scales. Local service planning might use SA2. Regional health planning might use SA3."

#### 2. Loading Tabular Data (5 min)

**Say:** "Now let's load our SEIFA data—these are socio-economic indexes. The data is in CSV format with no geometry, so we'll add it as an attribute table only."

**Do:**
```
Layer > Add Layer > Add Delimited Text Layer...
File name: [Browse to SEIFA_2021_SA2.csv]
File format: CSV (confirm auto-detection)
Record and Fields Options: [leave defaults]
Geometry Definition: No geometry (attribute only table)
Click Add
```

**Say:** "It appears in our layers panel, but there's no map—this is pure tabular data."

**Open attribute table:**
```
Right-click SEIFA layer > Open Attribute Table
```

**Say (while pointing):**
- "SA2_CODE_2021—our join key. It must match the SA2 boundary codes exactly."
- "IRSD_Score—Index of Relative Socio-economic Disadvantage. Higher scores = less disadvantaged."
- "IRSD_Decile—ranks areas from 1 (most disadvantaged 10%) to 10 (least)."
- "IRSAD, IER, IEO—other indexes measuring different aspects."

**Check field properties:**
```
Click on the SA2_CODE_2021 header > Properties (or right-click)
```

**Say:** "Data type is String—that's correct. If it were Integer, we'd lose leading zeros, and the join would fail."

**Teaching moment—open Excel demo (optional but impactful):**
- Open the same CSV in Excel
- Show how code "01234" displays as "1234"
- "This is why we never prepare geographic data in Excel without extreme care. Always use text format."

#### 3. Performing the Join (10 min)

**Say:** "Now the main event—joining SEIFA data to our SA2 boundaries. We're matching on the SA2 code."

**Do:**
```
Right-click SA2 layer > Properties
Go to Joins tab
Click the green + button (Add Join)
```

**Configure (explain each setting):**
- **Join layer:** SEIFA_2021_SA2 — "The table we're bringing in"
- **Join field:** SA2_CODE_2021 — "The key in the CSV"
- **Target field:** SA2_CODE21 — "The key in the shapefile"
- **Cache join layer in virtual memory:** [Check] — "Makes it faster"
- **Joined fields:** [Leave blank] — "Include all SEIFA fields"
- **Custom field name prefix:** SEIFA_ — "So we know which fields came from the join"

**Say:** "Always use a prefix! Otherwise you might have two fields called 'Code' and not know which is which."

**Do:**
```
Click OK
Click OK again to close Properties
```

**Verify:**
```
Open SA2 attribute table
Scroll right to see new fields: SEIFA_IRSD_Score, SEIFA_IRSD_Decile, etc.
```

**Say:** "Success! We now have socio-economic data attached to every SA2 polygon."

**Click on a few rows:**
- "This SA2 has IRSD_Decile = 1—that's high disadvantage."
- "This one is Decile 9—low disadvantage."

**Teaching moment:**
"What if we had NULL values here? That means the SA2 code in the shapefile didn't match any code in the CSV. Common causes: typos, different years (2016 vs 2021 boundaries), or genuinely missing data (like uninhabited areas)."

**Simulate troubleshooting (optional—if time allows):**

**Say:** "Let me show you what happens if the join fails."

**Do:**
```
Edit the join: Properties > Joins > Select join > Edit (pencil icon)
Change Target field to wrong field (like SA3_CODE21)
Apply
Open attribute table—all NULLs!
```

**Say:** "See? Wrong join field = no matches. Always double-check your keys!"

**Fix it:**
```
Properties > Joins > Edit join back to correct field
Apply
```

#### 4. Making the Join Permanent (5 min)

**Say:** "Right now, this join only exists in our QGIS project file. If I share this shapefile with a colleague, they won't see the SEIFA data. Let's make it permanent by exporting."

**Do:**
```
Right-click SA2 layer > Export > Save Features As...
Format: GeoPackage (explain: modern, efficient, single-file format)
File name: data/processed/week03/sa2_with_seifa.gpkg
Layer name: sa2_seifa_2021
CRS: Keep as EPSG:7844 (or project CRS)
Encoding: UTF-8
[Leave other settings default]
Click OK
```

**Say:** "QGIS automatically adds the new layer. Now all the SEIFA data is baked into the geometry file—one self-contained layer."

**Clean up:**
```
Remove the original SA2 layer (temporary join version)
Remove the SEIFA CSV table (no longer needed)
Keep only: sa2_seifa_2021
```

**Say:** "This is your working layer now. The join is permanent."

#### 5. Creating Derived Indicators (10 min)

**Say:** "Raw SEIFA scores are useful, but sometimes we want categories or flags for analysis. Let's use Field Calculator to create new fields."

**Do:**
```
Open attribute table for sa2_seifa_2021
Click Field Calculator icon (or Ctrl+I)
Toggle editing mode ON (if not already)
```

**Example 1: Categorize disadvantage**

**Say:** "Let's create meaningful categories from the deciles."

**Do:**
```
Create new field: [Check]
Output field name: disadvantage_category
Output field type: Text (string)
Output field length: 30

Expression:
CASE
  WHEN "SEIFA_IRSD_Decile" <= 2 THEN 'High disadvantage'
  WHEN "SEIFA_IRSD_Decile" <= 5 THEN 'Moderate disadvantage'
  WHEN "SEIFA_IRSD_Decile" <= 8 THEN 'Low disadvantage'
  ELSE 'Very low disadvantage'
END

Click OK
```

**Verify:**
- Scroll to new field
- Sort by it: click column header
- "See how SA2s are now grouped into categories?"

**Example 2: Flag extreme disadvantage**

**Say:** "Let's create a binary flag—1 for most disadvantaged decile, 0 otherwise. Useful for filtering later."

**Do:**
```
Field Calculator > Create new field
Output field name: extreme_disadvantage
Output field type: Whole number (integer)

Expression:
CASE
  WHEN "SEIFA_IRSD_Decile" = 1 THEN 1
  ELSE 0
END

Click OK
```

**Say:** "Now we can quickly filter: 'Show me only areas with extreme_disadvantage = 1'."

**Example 3: Handle NULL values**

**Say:** "If some SA2s didn't have SEIFA data, we might have NULLs. Let's handle that gracefully."

**Do:**
```
Field Calculator > Create new field
Output field name: disadvantage_clean
Output field type: Integer

Expression:
CASE
  WHEN "SEIFA_IRSD_Decile" IS NULL THEN 0
  ELSE "SEIFA_IRSD_Decile"
END

Click OK
```

**Say:** "This replaces NULL with 0. Whether that's appropriate depends on your analysis—document your decision!"

**Save edits:**
```
Click Save Edits (pencil icon with disk)
Toggle editing mode OFF
```

#### 6. Creating a Choropleth Map (7 min)

**Say:** "Let's visualize the spatial patterns in disadvantage."

**Do:**
```
Right-click sa2_seifa_2021 > Properties > Symbology
Change from Single Symbol to Graduated
```

**Configure:**
- **Value:** SEIFA_IRSD_Decile
- **Color ramp:** Click dropdown
  - Suggest: "RdYlGn" (Red-Yellow-Green) REVERSED
  - Or better for accessibility: "Viridis" or "YlOrRd"
- **Mode:** Natural Breaks (Jenks)
- **Classes:** 5

**Say:** "Natural Breaks finds clusters in the data—good for revealing patterns. Quantile would put equal numbers of areas in each class—good for comparison."

**Do:**
```
Click Classify
Click Apply (to preview without closing)
```

**Say:** "See the spatial pattern? [Point out clusters—e.g., disadvantaged areas in outer suburbs, advantaged near coast/city center]."

**Adjust symbology:**
```
Legend format: Precision = 0 decimal places
Uncheck "Legend is showing in tree" if you want cleaner legend
Click OK
```

**Teaching moment—classification methods:**
```
Reopen Symbology
Change Mode to Quantile > Apply
Change to Equal Interval > Apply
```

**Say:** "Each method tells a slightly different story. Natural Breaks emphasizes clusters. Quantile ensures even distribution. Equal Interval shows absolute differences. Choose based on what you're communicating."

**Set final:**
```
Mode: Natural Breaks
Classes: 5
Color ramp: YlOrRd (yellow = low disadvantage, red = high)
```

**Zoom in to a city:**
```
Use zoom tool to focus on a metro area
```

**Say:** "Now we can see local variation—this is the power of SA2-level data. Zoom out to LGA level and you'd lose this detail."

---

## Discussion Prompts (with expected responses)

### 1. Technical Reflection

**Prompt:** "What was the hardest part of the join workflow? What helped you solve it?"

**Expected responses:**
- Field names didn't match exactly (case sensitivity, underscores vs spaces)
- Data type mismatches (one field was integer, other was text)
- Leading zeros disappeared when opening CSV in Excel
- NULL values appeared after join—wasn't sure why

**Facilitator follow-up:**
- "How did you figure out what was wrong?"
- "What would you do differently next time?"
- Document solutions on board or shared doc

**Teaching moment:**
"Troubleshooting is a skill. The best GIS analysts don't avoid errors—they diagnose them systematically. Always check: field names, data types, value formats, record counts."

---

### 2. Boundary Choices and MAUP

**Prompt:** "We used SA2 boundaries today. How would our analysis differ if we used LGAs instead? Pull up both—what do you notice?"

**Expected responses:**
- LGAs are larger—less local variation visible
- Disadvantaged and advantaged SA2s can be in the same LGA (averaging hides inequality)
- LGA boundaries follow political divisions; SA2 boundaries follow population patterns
- Harder to spot spatial clusters at LGA scale

**Follow-up questions:**
- "When would LGA boundaries be more appropriate than SA2?" (e.g., analyzing local government service delivery, budgets)
- "What if you're studying education outcomes—school catchments don't match either boundary. What do you do?" (spatial overlay, point-in-polygon for school locations)

**Teaching moment:**
"This is the Modifiable Areal Unit Problem (MAUP). Results change based on how you zone space. There's no 'correct' boundary—acknowledge this limitation in your reporting."

**Advanced prompt (if students are engaged):**
"SA2 boundaries changed between 2016 and 2021 census. How would you compare disadvantage trends over time?"

**Expected responses:**
- Use correspondence files (ABS provides mappings)
- Aggregate to a stable geography (e.g., SA3, which change less)
- Accept some uncertainty—boundaries change as population shifts

---

### 2.5. "Who Decides?" Thread

Use this question throughout the session to reinforce critical thinking. Return to it whenever students work with a new layer or attribute.

**Core question:** "Who decided?"

**Apply it to:**
- **Boundaries:** "Who decided where SA2 boundaries go? For what purpose?"
- **Categories:** "Who decided what SEIFA measures? What values does the index embed?"
- **Data collection:** "Who decided what census questions to ask? What didn't they ask?"
- **Classification:** "Who decided the decile thresholds for 'disadvantaged'? Is decile 3 really different from decile 4?"

**This isn't about finding villains.** Decisions have to be made—we need boundaries and categories to function. But seeing them as *decisions* (not natural facts) is the critical skill.

**Script for introducing this thread:**

> "Throughout today, I'm going to keep asking one question: 'Who decided?' When you use SA2 boundaries, someone decided where those lines go. When you use SEIFA scores, someone decided what counts as disadvantage. When you classify into deciles, someone decided those thresholds.
>
> This isn't to say the decisions are wrong—they're usually thoughtful and carefully made. But they're still decisions. Seeing them as decisions, not facts, is what separates a technician from an analyst."

**Touchpoints during the session:**
1. When loading boundaries: "Who drew these? For what purpose?"
2. When joining SEIFA: "What does SEIFA measure? What doesn't it capture?"
3. When classifying: "Why deciles? Who benefits from this classification?"
4. When creating maps: "How might different communities want this visualized differently?"

---

### 3. Ethics of Mapping Disadvantage

This is the most important discussion of the session. Allocate 15-20 minutes if possible.

**Setup:** "We've created a map that shows where disadvantaged people live. Before we share or publish this, we need to think about consequences."

#### Prompt A: Benefits of disadvantage data

**Ask:** "Why is it important to measure and map socio-economic disadvantage?"

**Expected responses (affirm these):**
- Allocate funding fairly (e.g., schools, health services)
- Identify areas needing support
- Hold governments accountable (is policy reducing inequality?)
- Advocacy—communities can use data to demand resources
- Research—understand causes and effects of disadvantage

**Add if not mentioned:**
- Visibility—disadvantage that's measured is harder to ignore
- Evidence-based policy—replaces assumptions with data

#### Prompt B: Risks and harms

**Ask:** "What could go wrong? How might this map be misused or cause harm?"

**Expected responses (guide discussion toward these):**
- **Stigmatization:** Labeling a neighborhood "disadvantaged" affects residents' identity, property values, insurance rates
- **Determinism:** Maps imply problems are inherent to places, not caused by policy/history
- **Discrimination:** Could be used to exclude (e.g., lending, policing, zoning)
- **Oversimplification:** SEIFA reduces complex lives to a single number
- **Privacy:** Even aggregated data can reveal sensitive info about small communities

**Real-world example (choose relevant to context):**
- **Redlining (US):** "Objective" maps in 1930s-60s labeled Black neighborhoods as risky, denying loans—creating the disadvantage the maps claimed to measure
- **Public housing stigma (Australia):** Media maps of "crime hotspots" disproportionately show social housing areas, reinforcing stereotypes

**Ask:** "Who decides what 'disadvantage' means? What's included in SEIFA?"

**Expected responses:**
- Census variables: income, education, employment, internet access, car ownership
- Decided by ABS based on statistical correlation with disadvantage outcomes

**Follow-up:** "What's NOT in SEIFA that might matter?"
- Cultural wealth, social capital, community networks
- Historical context (why is disadvantage concentrated here?)
- Resilience, informal economies
- Structural causes (e.g., discriminatory zoning, lack of transit investment)

**Teaching moment:**
"Indexes like SEIFA reflect policy priorities, not objective truth. They're useful tools, but they're also political—they define what counts as a 'problem' and what solutions are imaginable."

#### Prompt C: Ethical mapping practices

**Ask:** "Given these risks, how should we approach mapping disadvantage responsibly?"

**Build toward these principles:**

1. **Community involvement:** Include affected communities in decisions about measurement and visualization
   - Example: Some Indigenous communities prefer cultural indicators, not just economic

2. **Contextualize:** Never show disadvantage without explaining structural causes
   - Not: "This area is poor"
   - Instead: "Decades of disinvestment in transit left this area isolated from jobs"

3. **Aggregate appropriately:** Use scales that protect privacy
   - SA2 is usually okay (1000-10000 people)
   - Never map individuals or households

4. **Acknowledge limitations:** Be explicit about what your data misses
   - "SEIFA measures economic indicators, not social cohesion or wellbeing"

5. **Ask: Who benefits?** Before publishing, consider power dynamics
   - Will this map empower communities or enable surveillance?

6. **Sometimes don't map:** Tables or text might be more appropriate
   - If spatial patterns aren't relevant to your argument, don't create them

**Real example:**
"COVID-19 case maps by neighborhood—helpful for resource allocation, but also enabled stigma and harassment of affected areas. Some health departments stopped publishing location data."

**Ask:** "When should we NOT make a map?"

**Expected responses:**
- When it invades privacy (small areas, identifiable individuals)
- When it creates stigma without actionable solutions
- When the spatial pattern isn't relevant to the question
- When affected communities object

---

### 4. Choice of Classification Methods

**Prompt:** "We used Natural Breaks (Jenks) for our choropleth. What happens if we use Quantile instead? Which is 'right'?"

**Do together:**
- Reopen symbology
- Switch between Natural Breaks, Quantile, Equal Interval
- Compare legends and visual patterns

**Expected observations:**
- Natural Breaks: Emphasizes clusters, legend values are uneven
- Quantile: Each class has same number of areas, but value ranges differ
- Equal Interval: Legend is neat (e.g., 1-2, 2-3), but classes may be empty or overcrowded

**Teaching moment:**
"There's no 'correct' method—each answers a different question."
- Natural Breaks: "Where are the clusters?"
- Quantile: "Which areas are relatively high/low?"
- Equal Interval: "How do areas compare to absolute thresholds?"

**Ethical consideration:**
"Classification choices affect perception. A map with 5 classes labeled 'Extreme', 'High', 'Moderate', 'Low', 'Very Low' creates different impressions than one labeled '1st quintile', '2nd quintile', etc. Be intentional about framing."

---

### 5. Longitudinal Analysis Challenge

**Prompt (advanced):** "Imagine you want to track disadvantage trends from 2016 to 2021. But SA2 boundaries changed between those years. How would you handle this?"

**Expected responses:**
- Use correspondence files (ABS provides crosswalks)
- Aggregate to stable geography (SA3 changes less frequently)
- Accept some areas aren't comparable
- Use population-weighted interpolation

**Facilitator adds:**
"This is a common real-world problem. Boundaries change because population shifts. Your options:"
1. **Correspondence files:** Map old codes to new (ABS provides these)
2. **Aggregate up:** SA3/SA4 are more stable
3. **Spatial interpolation:** Allocate 2016 data to 2021 boundaries based on overlap area
4. **Acknowledge limits:** Some areas won't be comparable—document this

**Show resource:**
"ABS publishes 'correspondence files'—tables linking 2016 SA2 codes to 2021 codes, with population/area weightings. Essential for time-series analysis."

---

## Common Student Issues (and solutions)

### Issue 1: Join shows 0 matched features

**Symptom:** Join completes but attribute table shows all NULLs for joined fields.

**Diagnosis steps:**
1. Check field names: Do they match EXACTLY? (Case-sensitive, spaces, underscores)
2. Check data types: Are both fields Text/String? (Right-click field header > Properties)
3. Check values: Open both tables, spot-check if codes look identical

**Common causes:**
- **Field name mismatch:** `SA2_CODE_2021` vs `SA2_CODE21` vs `SA2CODE2021`
- **Data type mismatch:** One is Integer (numeric), other is String (text)
- **Different vintages:** 2016 boundary codes won't match 2021 data codes

**Solutions:**

**A. Field name mismatch:**
- Double-check join configuration—type field names carefully, or select from dropdown

**B. Data type mismatch:**
```
Fix with Field Calculator:
- Create new field: SA2_CODE_text
- Type: String
- Expression: to_string("SA2_CODE21")
- Use new field for join
```

**C. Different vintages:**
- Use ABS correspondence files to map old codes to new
- Or: Obtain matching-year data

**Prevention:**
"Always inspect your data before joining! Open both attribute tables, check field properties, spot-check values."

---

### Issue 2: Join works but many NULL values

**Symptom:** Join appears successful, but many rows have NULL for SEIFA fields.

**Diagnosis:**
1. Count total features in boundary layer
2. Count total rows in CSV
3. Count non-NULL values in joined field: `Field Calculator > Count > "SEIFA_IRSD_Score" IS NOT NULL`

**Common causes:**

**A. Leading zeros stripped:**
- CSV codes: `1234`, `5678`
- Shapefile codes: `01234`, `05678`
- Result: No matches because "1234" ≠ "01234"

**Solution:**
```
Fix CSV codes with Field Calculator:
- Create new field: SA2_CODE_padded
- Type: String
- Expression: lpad("SA2_CODE_2021", 5, '0')
  (pads to 5 digits with leading zeros)
- Re-do join with padded field
```

**B. Extra whitespace:**
- CSV: `"01234 "` (trailing space)
- Shapefile: `"01234"`

**Solution:**
```
Field Calculator:
- Expression: trim("SA2_CODE_2021")
- Removes leading/trailing spaces
```

**C. Genuinely missing data:**
- Some SA2 areas have no residents (industrial zones, parks)
- SEIFA legitimately excludes them

**Solution:**
- Filter to identify: `"SEIFA_IRSD_Score" IS NULL`
- Check if they're expected (open attribute table, look at names—do they make sense?)
- Document: "125 of 2,310 SA2 areas had no SEIFA data; inspection confirms these are non-residential areas"

**Prevention:**
"Always check record counts: matched features should equal your boundary layer count (if you expect full coverage) or CSV row count (if some boundaries are empty)."

---

### Issue 3: Leading zeros disappear when opening CSV in Excel

**Symptom:** Student opens CSV in Excel to check data; codes lose leading zeros (01234 becomes 1234); join fails.

**Explanation:**
Excel auto-converts text that looks like numbers into Number format, stripping leading zeros.

**Solutions:**

**A. Don't use Excel for geographic codes** (preferred)
- Use QGIS "Add Delimited Text Layer" instead—it preserves text format
- Or use a text editor (Notepad++, VS Code) to inspect CSVs

**B. If you must use Excel:**
1. Open Excel FIRST (blank workbook)
2. Data > Get Data > From Text/CSV
3. Select your file
4. In preview, click dropdown on code column > change type to **Text**
5. Load

**C. Already messed up? Fix with Field Calculator:**
```
Expression: lpad(to_string("SA2_CODE"), 5, '0')
```

**Teaching moment:**
"Geographic codes are identifiers, not numbers—treat them as text ALWAYS. The number '01234' has meaning (it's a specific SA2); the number 1234 is a different SA2 entirely."

---

### Issue 4: Field Calculator expression errors

**Symptom:** Error message when trying to create derived field.

**Common errors:**

**A. Quote mistakes:**
```
Wrong: CASE WHEN IRSD_Decile <= 2 THEN 'High' END
Error: "IRSD_Decile" not found

Right: CASE WHEN "IRSD_Decile" <= 2 THEN 'High' END
Rule: Field names in DOUBLE quotes, text values in SINGLE quotes
```

**B. Syntax errors:**
```
Wrong: CASE WHEN "decile" <= 2 THEN 'High'
Error: CASE without END

Right: CASE WHEN "decile" <= 2 THEN 'High' END
Rule: CASE must close with END
```

**C. Division by zero:**
```
Wrong: "population" / "area"
Error: Division by zero (if area = 0)

Right: CASE WHEN "area" > 0 THEN "population" / "area" ELSE 0 END
Rule: Always check for zero before dividing
```

**D. NULL propagation:**
```
Wrong: "field_a" + "field_b"
Error: NULL if either field is NULL

Right: coalesce("field_a", 0) + coalesce("field_b", 0)
Rule: Use coalesce() to replace NULL with default value
```

**Debugging tips:**
1. Test expression on a single row first (use "Select features" to highlight one, then use "Update existing field" mode)
2. Check field names match exactly (copy-paste from attribute table)
3. Use Expression preview pane—it shows errors immediately
4. Start simple, add complexity incrementally

---

### Issue 5: Choropleth map looks wrong or doesn't show patterns

**Symptom:** Map is single color, or colors don't make sense.

**Common causes:**

**A. Wrong field selected:**
- Student selects `SA2_CODE` instead of `SEIFA_IRSD_Score`
- Result: Colors based on codes, not data

**Solution:** Reopen Symbology > check Value dropdown > select correct field

**B. NULL values dominate:**
- Many features have NULL for SEIFA data
- QGIS assigns them to a class, skewing classification

**Solution:**
```
Symbology > Advanced > Data-defined override > Filter features
Expression: "SEIFA_IRSD_Score" IS NOT NULL
```

**C. Single symbol still active:**
- Forgot to switch from Single Symbol to Graduated

**Solution:** Symbology > Change dropdown from Single Symbol to Graduated

**D. Classification method doesn't suit data:**
- Equal Interval creates empty classes if data is clustered
- Natural Breaks can hide extreme outliers

**Solution:** Try different methods; choose based on distribution

**E. Color ramp is non-intuitive:**
- Random colors for ranked data
- Red/green (problematic for colorblindness)

**Solution:**
- Use sequential ramps for ranked data (light to dark)
- Use diverging ramps for data with meaningful midpoint
- Avoid red/green; prefer ColorBrewer schemes designed for accessibility

---

### Issue 6: Joined fields disappear after reopening project

**Symptom:** Student saves project, closes QGIS, reopens—SEIFA fields are gone.

**Cause:** Join was temporary (stored in project file, not in layer file). If CSV file moves or is deleted, join breaks.

**Solution:**
"Always export joined layers to make them permanent!"

```
Right-click joined layer > Export > Save Features As...
Format: GeoPackage
File name: data/processed/week03/sa2_with_seifa.gpkg
```

**Prevention:**
Build this into workflow from start—demo makes it clear that exporting is NOT optional.

---

### Issue 7: Aggregation/Dissolve produces unexpected results

**Symptom:** Count Points in Polygon shows 0 for all areas, or Dissolve creates wrong boundaries.

**Common causes:**

**A. CRS mismatch:**
- Points and polygons in different coordinate systems
- QGIS may not correctly determine spatial relationships

**Solution:**
- Ensure both layers use the same CRS
- Reproject one layer to match the other before running

**B. Points outside polygons:**
- Points fall in gaps between polygons or outside study area

**Solution:**
- Zoom to points and polygons together
- Check if points actually fall inside polygons
- Use Select by Location to verify: "How many points intersect my polygons?"

**C. Dissolve field has NULL values:**
- Areas with NULL in the dissolve field group together unexpectedly

**Solution:**
- Check for NULL values before dissolving: `"SA3_CODE" IS NULL`
- Filter out NULL values or assign them to a category

**D. Statistics not configured:**
- Dissolve runs but no statistics calculated (only geometry merged)

**Solution:**
- In Dissolve, click the **...** button to access advanced options
- Under **Statistics**, add fields and select aggregation functions
- Or use Processing Toolbox version: "Aggregate"

**Teaching moment:**
"Always verify aggregation results. Open the attribute table, check counts, and compare to source data."

---

### Issue 8: "Cannot add layer to project" error

**Symptom:** Error when trying to load shapefile or CSV.

**Common causes:**

**A. File path has spaces or special characters:**
```
Wrong: C:\My Files\Week 3\SA2 Boundaries.shp
```

**Solution:** Rename folders/files to remove spaces, or use quotes in path

**B. Shapefile components missing:**
- Shapefile requires .shp, .shx, .dbf, .prj at minimum
- Student only copied .shp file

**Solution:** Copy ALL shapefile components (*.shp, *.shx, *.dbf, *.prj, *.cpg)

**C. CRS not recognized:**
- .prj file missing or corrupt

**Solution:** Manually assign CRS when adding layer

**D. CSV formatting issues:**
- Malformed delimiters (mixed commas and tabs)
- Special characters breaking parser

**Solution:** Open in text editor, check structure; re-export from data source if needed

---

## Wrap-up & Preview

### Concluding the Session

**Recap key skills (ask students to name them):**
1. "What's the first step in a join?" → Identify the common key field
2. "What should you always check after a join?" → Record counts, NULL values
3. "How do you make a join permanent?" → Export layer
4. "Why do boundaries matter?" → They shape the story (MAUP)
5. "What's an ethical consideration when mapping disadvantage?" → Stigmatization, oversimplification, community involvement

**Celebrate wins:**
- "Who successfully created a choropleth map today? That's a major GIS skill!"
- "Who troubleshot a join error? You're now better equipped than most GIS beginners!"

**Acknowledge challenges:**
- "Joins are finicky—it's okay if you struggled. Every GIS analyst has a story about joins failing at 4:59pm on a deadline. You're building resilience."

**Final thought:**
"Today you learned technical skills—joins, Field Calculator, symbology. But you also learned critical skills—questioning how boundaries shape data, reflecting on ethics of mapping. Both matter equally in GIS."

---

### Preview Week 4: Raster & Terrain Analysis

**Setup:**
"Next week we shift from vectors (boundaries, points) to rasters (continuous grids). We'll work with elevation data to model terrain."

**What students will do:**
- Load Digital Elevation Models (DEMs)
- Create hillshade visualizations (makes terrain look 3D)
- Calculate slope and aspect (steepness and direction)
- Identify flood-prone areas (low elevation + gentle slopes)
- **Overlay terrain risk with disadvantage data** (combining Week 3 and Week 4 skills)

**Why it matters:**
"Environmental justice question: Do disadvantaged communities face higher exposure to natural hazards? You'll have the tools to answer this by overlaying your Week 3 disadvantage map with Week 4 flood risk surfaces."

**Action items for students:**

1. **Download DEM data before next class:**
   - Australia: ELVIS (Geoscience Australia)
   - US: USGS Earth Explorer or SRTM
   - Check Week 4 materials for specific download instructions
   - "DEMs are large files—don't wait until the night before!"

2. **Complete Week 3 reflection:**
   - Document what worked, what failed, how you solved it
   - These notes are goldmines for future projects

3. **Submit Week 3 deliverables:**
   - QGIS project file (organized, with relative paths)
   - Joined layer (`sa2_with_seifa.gpkg`)
   - Exported map image
   - At least one derived indicator field

4. **Optional reading:**
   - MAUP primer (link in Week 3 materials)
   - SEIFA methodology (ABS website)
   - Ethics article: "Who Maps Inequality?"

---

### Support Resources Reminder

**If you get stuck:**
- Office hours: [Time/location]
- Discussion forum: [Link]
- Troubleshooting guide: Week 3 materials folder
- Peer support: Slack/Teams channel

**Documentation:**
- QGIS docs: docs.qgis.org
- ABS SEIFA technical paper: [Link]
- Correspondence files: [Link to ABS]

**Next class:**
- Bring questions! We'll start with Q&A about Week 3 issues

---

### Q&A Protocol

**Open floor:**
"What questions do you have? No question is too basic—if you're wondering, others are too."

**Common last-minute questions:**

**Q: "Do we have to use SA2, or can we use LGA?"**
A: "SA2 is recommended because it shows local variation. But if your capstone project focuses on local government policy, LGA might be more appropriate. Justify your choice in your reflection."

**Q: "What if some SA2 areas have no SEIFA data?"**
A: "Check if they're non-residential (parks, industrial). If so, document it. If residential areas are missing data, that's a data quality issue—report it."

**Q: "Can I use this workflow for other countries?"**
A: "Absolutely! US = Census tracts + ACS data. UK = LSOAs + IMD. Canada = Dissemination areas + census. Same logic, different boundary names."

**Q: "How do I know which SEIFA index to use?"**
A:
- IRSD: General disadvantage (most common)
- IRSAD: Captures both advantage and disadvantage (use if studying inequality spectrum)
- IER: Economic resources specifically
- IEO: Education/skills specifically
"Choose based on your research question."

**Q: "Can I combine multiple variables in one map?"**
A: "Yes! Bivariate mapping—e.g., disadvantage vs remoteness. We'll touch on this later, but Field Calculator can create combined indicators now."

---

## Additional Teaching Notes

### Timing Adjustments

**If running short on time:**
- Skip the Excel demonstration (just warn about it)
- Reduce number of Field Calculator examples (do one, assign others as practice)
- Shorten discussion of classification methods (show Natural Breaks only)

**If you have extra time:**
- Add bivariate analysis: `"IRSD_Decile" <= 2 AND "remoteness" = 'Very Remote'`
- Demonstrate Select by Location (e.g., "Disadvantaged areas within 5km of CBD")
- Show how to create custom color ramps
- Introduce Geometry Generator for boundary visualization

### Differentiation Strategies

**For advanced students:**
- Challenge: "Create a field that flags areas in bottom 20% for BOTH disadvantage AND education"
- "Use spatial statistics to test if disadvantage is clustered (we'll cover this formally in Week 8)"
- "Create a bivariate choropleth using QGIS expressions"

**For struggling students:**
- Provide pre-joined sample layer as backup
- Pair with peer mentor
- Focus on getting ONE successful join, worry about derived indicators later
- Offer step-by-step checklist handout

**For visual learners:**
- Draw join logic on whiteboard
- Use physical nested boxes to demonstrate boundary hierarchy
- Create flowchart of troubleshooting steps

---

### Accessibility Considerations

**Color vision deficiency:**
- Avoid red/green color ramps
- Recommend ColorBrewer schemes (designed for accessibility)
- Show how to check maps with colorblindness simulators

**Screen readers:**
- Emphasize keyboard shortcuts (Ctrl+I for Field Calculator, etc.)
- Describe choropleth patterns verbally: "Dark areas in the southwest, light areas in the northeast"

**Cognitive load:**
- Break complex tasks into steps
- Provide written checklist alongside verbal instructions
- Allow time for note-taking between steps

---

### Assessment Rubric (if grading)

**QGIS Project File (20%)**
- [ ] Opens without errors
- [ ] Layers organized in logical groups
- [ ] Relative file paths used (portable project)
- [ ] Appropriate CRS applied

**Joined Layer (30%)**
- [ ] Join successful (no or minimal NULLs)
- [ ] Exported to GeoPackage
- [ ] Field names are clear
- [ ] At least one derived indicator created correctly

**Visualization (20%)**
- [ ] Appropriate symbology (graduated for continuous data)
- [ ] Thoughtful classification method choice
- [ ] Accessible color ramp
- [ ] Legend is clear

**Reflection (30%)**
- [ ] Discusses boundary choice and implications
- [ ] Documents troubleshooting steps
- [ ] Reflects on ethical considerations
- [ ] Connects to emerging capstone ideas
- [ ] Shows critical thinking about MAUP

---

### Emergency Backup Plan

**If data downloads fail across the board:**
1. Use your pre-downloaded backup files
2. Share via USB drive or local network
3. Have students work in pairs on one machine if needed

**If QGIS crashes repeatedly:**
1. Switch to simpler dataset (fewer features)
2. Have students save projects every 5 minutes
3. Demonstrate workflow only; students practice later

**If projector/screen sharing fails:**
1. Walk through demo verbally while students follow on their screens
2. Use pre-prepared screenshots
3. Pair students for peer teaching

**If you finish early:**
- Open discussion: "Share one insight from today that surprised you"
- Peer troubleshooting session
- Preview Week 4 more deeply
- Office hours on the spot

---

## Final Facilitator Checklist

**Before class:**
- [ ] Data downloads tested
- [ ] Demo project prepared and tested
- [ ] Backup data on USB drive
- [ ] Projector/screen sharing tested
- [ ] Attendance/sign-in sheet ready
- [ ] Reviewed SEIFA methodology
- [ ] Prepared ethical discussion prompts

**During class:**
- [ ] Welcome & recap completed
- [ ] Live demo successful (or troubleshot transparently)
- [ ] Students had sufficient work time
- [ ] Circulated to troubleshoot individual issues
- [ ] Facilitated ethical discussion
- [ ] Previewed Week 4
- [ ] Q&A addressed

**After class:**
- [ ] Note common issues for future sessions
- [ ] Update troubleshooting guide if new issues emerged
- [ ] Check discussion forum for follow-up questions
- [ ] Prepare Week 4 materials
- [ ] Grade submissions (if applicable)

---

## Recommended Readings for Facilitators

To deepen your understanding and prepare for student questions:

1. **MAUP:**
   - Openshaw, S. (1984). *The Modifiable Areal Unit Problem*. GeoBooks. (Foundational)
   - Dark, S.J., & Bram, D. (2007). The modifiable areal unit problem (MAUP) in physical geography. *Progress in Physical Geography*, 31(5), 471-479.

2. **SEIFA Methodology:**
   - ABS (2021). *Socio-Economic Indexes for Areas (SEIFA), Australia, 2021: Technical Paper*. Australian Bureau of Statistics.

3. **Ethics of Mapping Inequality:**
   - Crampton, J. (2010). *Mapping: A Critical Introduction to Cartography and GIS*. Wiley-Blackwell. (Chapter on power and mapping)
   - Mapping Inequality project (U.S. redlining): https://dsl.richmond.edu/panorama/redlining/

4. **Boundary Changes:**
   - ABS correspondence files documentation: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/correspondences

---

## Notes for Future Iterations

**What worked:**
- [Add notes after teaching]

**What to improve:**
- [Add notes after teaching]

**Student feedback themes:**
- [Add notes after teaching]

**Timing adjustments needed:**
- [Add notes after teaching]

**New issues encountered:**
- [Add notes after teaching]

---

**End of Week 3 Facilitator Notes**

Good luck with the session! Remember: troubleshooting IS the lesson. Students learn more from watching you diagnose and fix errors than from a perfect demo.
