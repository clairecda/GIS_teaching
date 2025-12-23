# Week 3 · Vector Analysis & Attribute Joins

Boundaries shape how we understand social and economic patterns. The same data looks completely different when aggregated by suburb, municipality, or region. This week, you'll learn how administrative and statistical boundaries work, how to join tabular data to spatial layers, and how to think critically about the stories boundaries tell—and hide.

## What you'll learn

By the end of this week, you'll be able to:

1. Explain the role of administrative and statistical boundaries in socio-economic analysis.
2. Perform attribute joins between polygon boundaries (e.g., SA2/LGA) and tabular datasets (e.g., SEIFA, ACS).
3. Use the Field Calculator and selection tools to create derived indicators.

## Before you start

- [ ] Read: [Understanding administrative boundaries](../readings/week03-admin-boundaries.md)—this provides essential context
- [ ] Review the lecture: [Boundary Systems & Data Joins](../lectures/week03-boundaries.md)
- [ ] Download boundary and indicator datasets (ASGS SA2 + SEIFA, or local equivalents) via [Downloading datasets](../onboarding/data-downloads.md)
- [ ] Check off Week 3 items in the [data download checklist](../reference/data-download-checklist.md)
- [ ] Think of one question about boundary changes or data comparability to discuss in class

## This week's activities

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

### Activity 6: Select and filter by attributes or location

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

### Activity 7: Quality assurance and troubleshooting

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

## Support materials

- Slides: [Week 03 lecture deck](../slides/index.md)
- Reading: [Understanding administrative boundaries](../readings/week03-admin-boundaries.md)
- Lecture notes: [Boundary Systems & Data Joins](../lectures/week03-boundaries.md)
- Dataset checklist: [Week 3 items](../reference/data-download-checklist.md)
- Reference: ABS correspondence files for boundary changes (link in lecture notes)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 3 reflection](../reference/reflections.md#week-3--vector-analysis--joins):

- How do boundary choices affect the story your data tells? Compare what you see at SA2 vs LGA level.
- What happens when boundaries change between census releases? How would you handle this in a longitudinal study?
- Did your join work perfectly, or did you have unmatched records? What might explain the mismatches?
- What spatial patterns did you observe in the socio-economic data? Were you surprised by anything?
- Which boundary level (SA2, LGA, postcode, etc.) makes sense for your emerging capstone ideas? Why?

!!! tip "Document your troubleshooting"
    If you encountered join errors or data issues, write down what went wrong and how you solved it. These notes are incredibly valuable for future projects—and for helping classmates!

## What you'll submit

- [ ] QGIS project file (`projects/week03_boundaries_joins.qgz`) with completed joins
- [ ] Joined boundary layer: `data/processed/week03/sa2_with_seifa.gpkg` (or equivalent)
- [ ] At least one derived indicator created with Field Calculator
- [ ] Exported map showing spatial patterns in socio-economic data
- [ ] Your Week 3 reflection entry

## Coming up next week

Week 4 introduces raster and terrain analysis. You'll work with digital elevation models (DEMs) to create hillshades, calculate slopes, and identify areas vulnerable to flooding or landslides. This builds on your Week 3 boundary work—you'll overlay terrain products with socio-economic data to answer questions like "Which disadvantaged communities face the highest flood risk?" Download your DEM tiles (ELVIS for Australia or SRTM for other regions) before next session so you're ready to jump in.
