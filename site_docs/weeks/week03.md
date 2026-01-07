# Week 3 · Mapping Socioeconomic Disadvantage

## Research Question

> **"Which areas have the highest socioeconomic disadvantage, and how does this pattern change when we aggregate to different geographic scales?"**

Boundaries shape how we understand social and economic patterns. The same data looks completely different when aggregated by suburb, municipality, or region. This week, you'll join socioeconomic index data to statistical boundaries and explore how geographic choices affect the stories we tell about disadvantage.

This is the same analysis you'll automate in Python during Week 8. By doing it manually first in QGIS, you'll understand exactly what each step accomplishes before writing code to replicate it.

## What you'll learn

By the end of this week, you'll be able to:

1. Identify which areas have the highest socioeconomic disadvantage by joining index data to boundaries.
2. Perform attribute joins between polygon boundaries (e.g., SA2/LGA) and tabular datasets (e.g., SEIFA, ACS).
3. Demonstrate how aggregating data to different geographic scales changes the patterns you see.
4. Create derived indicators using the Field Calculator and critically interpret what they reveal—and hide.

## Before you start

- [ ] Read: [Understanding administrative boundaries](../readings/week03-admin-boundaries.md)—this provides essential context
- [ ] Review the lecture: [Boundary Systems & Data Joins](../lectures/week03-boundaries.md)
- [ ] Download boundary and indicator datasets (ASGS SA2 + SEIFA, or local equivalents) via [Downloading datasets](../onboarding/03-download-data.md)
- [ ] Check off Week 3 items in the [data download checklist](../reference/data-download-checklist.md)
- [ ] Think of one question about boundary changes or data comparability to discuss in class

## This week's activities

### Activity 0: One place, many maps

Before we start joining data, let's see how the same place looks completely different depending on what we map. This activity builds the critical lens you'll need for working with boundaries and socio-economic data.

**The question:** What stories can this place tell—and which ones become invisible with different data choices?

**Steps:**

1. Choose a familiar area (your suburb, a place you've lived, or a well-known neighborhood)
2. Load your SA2 layer and zoom to that area
3. Create four different maps of the same place by styling different attributes:

   **Map A: Administrative identity**
   - Categorize by state or LGA name
   - What official boundaries define this place?

   **Map B: Geographic hierarchy**
   - Categorize by SA3 or SA4 region
   - Where does this place sit in the statistical hierarchy?

   **Map C: Population (if available)**
   - Graduated symbology by population or area
   - Is this a dense urban area or sparse rural?

   **Map D: Your choice**
   - After completing Activity 3 (join), return here and map by SEIFA decile
   - What socio-economic story does this place tell?

4. For each map, note:
   - What question does this map answer well?
   - What does it hide or make invisible?

!!! tip "The point isn't that maps lie"
    Maps don't lie—they answer specific questions. The skill is recognizing WHICH question each map answers, and what other questions become harder to ask. You'll return to Map D after joining SEIFA data.

**Reflection prompt:** Each map shows the same geography but tells a different story. Which version feels most "true" to your experience of this place? Which could be misleading without context?

### Activity 1: Understand boundary hierarchies

Before joining data, you need to understand what your boundaries represent and how they relate to each other.

**Steps:**

1. Load your SA2 (or equivalent statistical area) shapefile
2. Open the attribute table and explore the fields:
   - What's the unique identifier? (e.g., `SA2_CODE_2021`)
   - What parent geographies exist? (e.g., SA3, SA4, state codes)
   - What metadata is included? (area, population counts, names)
3. Compare boundary types:
   - **Statistical boundaries** (SA2, census tracts): designed for data collection and analysis
   - **Administrative boundaries** (LGA, municipalities): used for governance and service delivery
   - **Postal areas** (postcodes, ZIP codes): designed for mail delivery, not analysis
4. Visualize the hierarchy:
   - Color by a higher-level geography (e.g., SA3 or state)
   - Notice how smaller areas nest within larger ones

!!! note "Why boundaries matter"
    The boundary you choose affects your results. SA2 areas show local variation that disappears when aggregated to LGA level. Postcodes often cross meaningful boundaries and shouldn't be used for spatial analysis.

### Activity 2: Inspect and prepare your tabular data

You'll join SEIFA (or equivalent socio-economic index) data to your boundaries. First, make sure the data is clean.

**Steps:**

1. Download your SEIFA (or ACS, deprivation index) CSV file
2. Open it in a spreadsheet or text editor
3. Check the structure:
   - Does it have a geographic identifier that matches your shapefile? (e.g., `SA2_CODE_2021`)
   - Are codes formatted consistently? (Watch for leading zeros: "00123" vs "123")
   - What indicators are included? (IRSD, IRSAD, percentiles, etc.)
4. Load into QGIS:
   - `Layer ▶ Add Layer ▶ Add Delimited Text Layer...`
   - Select your CSV file
   - **Geometry definition:** "No geometry (attribute only table)"
   - Click Add
5. Open the attribute table and verify:
   - Geographic codes appear as text (not numbers—leading zeros matter!)
   - No unexpected missing values
   - Field names are clear

!!! warning "Common pitfall: Leading zeros"
    Geographic codes like "01234" often lose their leading zero when opened in Excel, becoming "1234". This breaks joins. Always treat codes as text/strings, not numbers.

### Activity 3: Perform the attribute join

Now you'll link your socio-economic data to your spatial boundaries.

**Steps:**

1. Right-click your SA2 layer → **Properties** → **Joins** tab
2. Click the **+** button to add a new join
3. Configure the join:
   - **Join layer:** your SEIFA CSV layer
   - **Join field:** the geographic code in the CSV (e.g., `SA2_CODE_2021`)
   - **Target field:** the matching code in your shapefile (e.g., `SA2_CODE21`)
   - **Joined fields:** leave blank to include all, or select specific indicators
   - **Custom field name prefix:** optionally add "SEIFA_" to avoid field name collisions
4. Click OK twice to close
5. Open the attribute table of your SA2 layer—you should now see new columns from SEIFA
6. Check a few rows to verify values look correct

**Make the join permanent:**

Joins are temporary by default. To save them:
1. Right-click your SA2 layer → **Export** → **Save Features As...**
2. Format: GeoPackage
3. File name: `data/processed/week03/sa2_with_seifa.gpkg`
4. Click OK

!!! tip "Why export?"
    Exporting makes your join permanent and faster to work with. The joined layer is now a single file you can share or reuse without worrying about the original CSV.

### Activity 4: Create derived indicators with Field Calculator

Raw index scores are useful, but you might want to create normalized rates, categories, or other calculations.

**Steps:**

1. Open the attribute table of your exported layer (from Activity 3)
2. Open the Field Calculator (calculator icon in toolbar or Ctrl+I)
3. **Example 1: Normalize by area**
   - Create output field: `pop_density`
   - Output field type: Decimal (double)
   - Expression: `"population" / ("area_sqkm")`
   - Click OK
4. **Example 2: Categorize by decile**
   - Create output field: `disadvantage_category`
   - Output field type: Text (string)
   - Expression:
     ```
     CASE
       WHEN "IRSD_decile" <= 2 THEN 'High disadvantage'
       WHEN "IRSD_decile" <= 5 THEN 'Moderate disadvantage'
       WHEN "IRSD_decile" <= 8 THEN 'Low disadvantage'
       ELSE 'Very low disadvantage'
     END
     ```
   - Click OK
5. **Example 3: Rate per 1,000 residents**
   - Create output field: `rate_per_1000`
   - Expression: `("count_field" / "population") * 1000`

**Challenge:** Create a field that flags areas in the bottom 20% for disadvantage AND top 20% for remoteness.

### Activity 5: Visualize and explore spatial patterns

Now that your data is joined, let's map it to see patterns.

**Steps:**

1. Apply graduated symbology to your disadvantage index:
   - Layer Properties → Symbology → Graduated
   - Value: `IRSD_score` (or your disadvantage indicator)
   - Method: Natural Breaks (Jenks)
   - Classes: 5
   - Color ramp: choose a diverging or sequential palette
   - Click OK
2. Explore the map:
   - Where are the most disadvantaged areas?
   - Do you see spatial clusters or random distribution?
   - Are patterns related to urban/rural divides?
3. Try different classification methods (Quantile, Equal Interval)—how does the story change?
4. Use the Identify tool to click on specific areas and read their values

### Activity 6: Aggregate and summarize by geography

One of the most powerful GIS operations is aggregating data from one geographic level to another. You might count points per polygon, sum values when combining areas, or roll up detailed data to a larger region.

**Key tools:**

| Tool | What it does | Example |
|------|--------------|---------|
| **Count Points in Polygon** | Count features in each area | Schools per LGA |
| **Join attributes by location (summary)** | Summarize any statistic spatially | Sum population, mean income |
| **Dissolve** | Merge polygons + aggregate attributes | Combine SA2s into SA3s with totals |

#### Part A: Count points in polygons

**Steps:**

1. Load a point layer (e.g., schools, health facilities, or cities from Week 2)
2. Run the count tool:
   - `Vector ▶ Analysis Tools ▶ Count Points in Polygon`
   - **Polygons:** your SA2 or LGA layer
   - **Points:** your point layer (e.g., schools)
   - **Count field name:** `facility_count`
   - **Output:** save to `data/processed/week03/sa2_facility_count.gpkg`
3. Open the attribute table—each polygon now has a count field
4. Style by the count field using graduated symbology
5. Interpret: Which areas have the most/fewest facilities? Does this relate to population or disadvantage?

#### Part B: Summarize with spatial join

**Steps:**

1. Open the Processing Toolbox (`Processing ▶ Toolbox`)
2. Search for "Join attributes by location (summary)"
3. Configure:
   - **Join to features in:** your SA2 layer
   - **By comparing to:** your point layer
   - **Geometric predicate:** Intersects (or Contains)
   - **Fields to summarise:** select relevant fields (e.g., capacity, size)
   - **Summaries to calculate:** Count, Sum, Mean (select what makes sense)
   - **Output:** save to `data/processed/week03/sa2_with_summary.gpkg`
4. This is more flexible than Count Points—you can calculate multiple statistics at once

#### Part C: Aggregate to roll up boundaries

Sometimes you need to roll up smaller areas into larger ones while calculating summary statistics. Let's start with a simple example using your Week 1 data, then apply it to boundaries.

**Warm-up: Population by continent**

Using your Natural Earth countries layer from Week 1:

1. Open the Processing Toolbox (`Processing ▶ Toolbox`)
2. Search for **Aggregate** (under Vector geometry)
3. Configure:
   - **Input layer:** `ne_110m_admin_0_countries` (your countries layer)
   - **Group by expression:** `"CONTINENT"`
   - **Aggregates:** Click **...** to configure:
     - `CONTINENT` → First value
     - `POP_EST` → Sum
     - `GDP_MD` → Sum
     - `NAME` → Count (gives number of countries)
   - **Output:** save to `data/processed/week03/continents_aggregated.gpkg`
4. Click **Run**
5. Open the result—you now have **7 polygons** (one per continent) with:
   - Total population per continent
   - Total GDP per continent
   - Count of countries per continent

!!! tip "What just happened?"
    You transformed ~177 country polygons into 7 continent polygons, with summarized statistics. This is the power of spatial aggregation—rolling up detailed data to answer bigger questions.

**Now apply to boundaries: SA2 → SA3**

The same technique works for statistical boundaries:

1. **Input layer:** your SA2 layer (with joined SEIFA data)
2. **Group by expression:** `"SA3_CODE21"` (or `"LGA_CODE"` for LGA-level)
3. **Aggregates:**
   - `SA3_NAME21` → First value (keeps one name per group)
   - `population` → Sum
   - `IRSD_score` → Mean
   - `AREASQKM` → Sum
4. **Output:** save to `data/processed/week03/sa3_aggregated.gpkg`
5. Compare the SA2 map to the SA3 map—what patterns become visible or invisible?

!!! tip "Aggregate vs Dissolve"
    **Aggregate** (Processing Toolbox) is better for calculating statistics—it has a clear interface for choosing sum, mean, count, etc. **Dissolve** (Vector menu) is simpler but hides the statistics options. Use Aggregate when you need to summarize numeric fields.

!!! warning "Aggregation changes the story"
    When you aggregate SA2 to SA3, you lose local variation. A disadvantaged pocket within an affluent SA3 becomes invisible. Always consider what level of detail your analysis question requires.

**Challenge:** Calculate a facility-to-population ratio:

1. Use Field Calculator on your count output
2. Expression: `("facility_count" / "population") * 10000`
3. This gives facilities per 10,000 people—a fairer comparison than raw counts

### Activity 7: Select and filter by attributes or location

You'll often want to focus on a subset of areas that meet certain criteria.

**Steps:**

1. **Select by attribute:**
   - Open attribute table → **Select features using an expression** (yellow button)
   - Expression: `"IRSD_decile" <= 2` (select most disadvantaged)
   - Click Select Features
   - Your map highlights selected areas in yellow
2. **Select by location:**
   - `Vector ▶ Research Tools ▶ Select by Location...`
   - Select features from: SA2 layer
   - That intersect: a custom boundary (e.g., Greater Sydney)
   - Click Run
3. **Save selection:**
   - Right-click layer → **Export** → **Save Selected Features As...**
   - Save to `data/processed/week03/high_disadvantage_metro.gpkg`
4. Clear selection: Click **Deselect All** button or press Ctrl+Shift+A

!!! tip "Combining criteria"
    You can combine multiple criteria: `"IRSD_decile" <= 2 AND "state" = 'NSW'` selects only disadvantaged areas in NSW.

### Activity 8: Quality assurance and troubleshooting

Joins can fail silently. Always verify your results.

**Steps:**

1. **Check record counts:**
   - Original SA2 layer: _____ features
   - SEIFA CSV: _____ rows
   - After join: _____ features (should match SA2 count)
2. **Identify unmatched records:**
   - Open attribute table
   - Sort by a SEIFA field (e.g., `IRSD_score`)
   - Look for NULL values—these are SA2 areas that didn't match
3. **Common join issues:**
   - **Mismatched codes:** Check for leading zeros, extra spaces, different vintages
   - **Wrong field type:** Ensure both join fields are text/string
   - **Different data years:** 2021 boundaries don't match 2016 codes
4. **Document your work:**
   - Note which SA2 areas had no match (if any)
   - Record assumptions (e.g., "Using 2021 boundaries with 2021 SEIFA")
   - Save your notes in your Week 3 reflection

!!! note "Boundary correspondence files"
    When boundaries change between census years, use correspondence files from ABS (Australia) or Census Bureau (US) to map old codes to new codes.

## Troubleshooting

### Join shows 0 matched features
- **Field names don't match:** Check exact spelling, case, and spaces in both layers
- **Data types differ:** One field is text, the other is number. Convert using Field Calculator: `to_string("numeric_field")` or `to_int("text_field")`
- **Leading zeros stripped:** Excel often removes leading zeros from codes. Re-import CSV with the field formatted as text
- **Different vintages:** 2016 census codes won't match 2021 boundary codes exactly

### Join shows partial matches (some NULL values)
- **Spelling variations:** "Sydney (City)" vs "City of Sydney" won't match
- **Extra spaces:** Use `trim("field_name")` in Field Calculator to remove
- **Missing records:** Some areas may genuinely have no data (e.g., unpopulated regions)
- **Check unmatched:** After joining, filter for NULL values to see which records failed

### Joined fields disappear after saving
- **Temporary join:** By default, joins are stored in the project, not the layer. To make permanent:
  1. Right-click the joined layer → **Export** → **Save Features As...**
  2. Save as GeoPackage to `data/processed/week03/`
  3. Add the new permanent layer to your project

### Field Calculator expression errors
- **Syntax error:** Check quotes—field names use double quotes `"field"`, text values use single quotes `'value'`
- **Division by zero:** Wrap calculations in `CASE WHEN "population" > 0 THEN ... ELSE 0 END`
- **NULL values:** Use `coalesce("field", 0)` to replace NULL with zero

### Choropleth map looks wrong after join
- **Wrong field:** Make sure you're mapping the joined field, not the original
- **NULL values showing:** Set a default color for NULL/no data values in Symbology
- **Classification method:** Try different methods (Quantile vs Natural Breaks) to see patterns

### Attribute table shows field names like "layer_field"
- **Join prefix:** QGIS adds the source layer name as a prefix. You can rename after exporting to a permanent layer
- **Too many fields:** After joining, export only the fields you need to keep the table clean

## Your Research Findings

After completing this week's analysis, summarize your findings:

### Research Question
"Which areas have the highest socioeconomic disadvantage, and how does this pattern change when we aggregate to different geographic scales?"

### Key Findings
Complete these based on your analysis:

1. The SA2s with highest disadvantage (bottom decile) are: _________________________________
2. When aggregated to SA3 level, the most disadvantaged region is: _________________________________
3. I observed ______ (clustering / scattered distribution) of disadvantaged areas.
4. The relationship between disadvantage and [urban/rural location, population density, or another variable] is: _________________________________

### Methodology
- **Data sources:** ABS SA2 boundaries (ASGS 2021), SEIFA IRSD scores
- **Key parameters:** Classification method: _____, Number of classes: _____
- **Tools used:** Attribute Join, Field Calculator, Aggregate/Dissolve

### Limitations
This analysis does NOT capture:

- [ ] Change over time (single census snapshot only)
- [ ] Variation within SA2 areas (could hide local pockets of disadvantage)
- [ ] Why areas are disadvantaged (correlation vs causation)
- [ ] How disadvantage relates to access to services

### QGIS ↔ Python comparison

| QGIS (Week 3) | Python (Week 8) |
|---------------|-----------------|
| Layer Properties > Joins | `geopandas.merge()` |
| Field Calculator | `.assign()` with expressions |
| Dissolve / Aggregate tool | `.dissolve(by='column')` |
| Manual symbology | `geopandas.plot()` |

### If this were your capstone
- How would you adapt this for your study area?
- What additional data would strengthen the analysis?
- What research question would you ask?

## Support materials

- Slides: [Week 03 lecture deck](../slides/index.md)
- Reading: [Understanding administrative boundaries](../readings/week03-admin-boundaries.md)
- Lecture notes: [Boundary Systems & Data Joins](../lectures/week03-boundaries.md)
- Python equivalent: [Week 8 · Python Vector Workflows](week08.md) (automates this analysis)
- Dataset checklist: [Week 3 items](../reference/data-download-checklist.md)
- Reference: ABS correspondence files for boundary changes (link in lecture notes)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 3 reflection](../reference/reflections.md#week-3--vector-analysis--joins):

- How do boundary choices affect the story your data tells? Compare what you see at SA2 vs LGA level.
- When you dissolved SA2 to a larger geography, what patterns became visible? What local detail was lost?
- What happens when boundaries change between census releases? How would you handle this in a longitudinal study?
- Did your join work perfectly, or did you have unmatched records? What might explain the mismatches?
- What spatial patterns did you observe in the socio-economic data? Were you surprised by anything?
- Which boundary level (SA2, LGA, postcode, etc.) makes sense for your emerging capstone ideas? Why?

!!! tip "Document your troubleshooting"
    If you encountered join errors or data issues, write down what went wrong and how you solved it. These notes are incredibly valuable for future projects—and for helping classmates!

## What you'll submit

- [ ] QGIS project file (`projects/week03_boundaries_joins.qgz`) with completed joins
- [ ] Joined boundary layer: `data/processed/week03/sa2_with_seifa.gpkg` (or equivalent)
- [ ] Aggregated output: `data/processed/week03/sa2_facility_count.gpkg` or dissolved layer
- [ ] At least one derived indicator created with Field Calculator
- [ ] Exported map showing spatial patterns in socio-economic data
- [ ] Your Week 3 reflection entry

!!! danger "Map submission requirements"
    Your exported map **must** include: **Title**, **Legend**, **Scale bar**, and **North arrow**. Maps missing any of these elements will not be accepted. See [Map Design Principles](../reference/design-rubric.md).

## Coming up next week

Week 4 shifts from vectors to rasters with a **flood risk assessment** of the Hawkesbury-Nepean region. You'll work with digital elevation models (DEMs) to calculate slope, identify low-lying areas, and classify flood risk zones. This builds on your Week 3 boundary work—you'll use zonal statistics to summarize flood risk by SA2, combining terrain analysis with the administrative boundaries you now understand.

!!! tip "Week 4 ↔ Week 9 connection"
    In Week 4, you'll do the flood risk analysis manually in QGIS. In Week 9, you'll automate the same analysis in Python—the same parallel as Week 3 ↔ Week 8 for vector analysis.
