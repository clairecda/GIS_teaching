# Capstone Project Examples

These examples from previous cohorts illustrate the range of topics, methods, and outputs that make successful capstone projects. Use them for inspiration, but develop your own question that's meaningful to you.

---

## Example 1: Urban Accessibility

### Food Desert Analysis in Western Sydney

**Research question:** Which neighborhoods in Western Sydney have poor walkable access to fresh food retailers?

**Methods used:**

- Point data collection (supermarkets, grocers, farmers markets from OSM)
- Network analysis (15-minute walking isochrones)
- Spatial join with census demographics
- Choropleth mapping of access gaps

**Key findings:**

- 12% of residents in the study area live beyond 15-minute walking distance to any fresh food retailer
- Low-income areas disproportionately affected (2.3x more likely to be in food deserts)
- Three priority zones identified for intervention

**Deliverables:**

- Primary map: Access gap choropleth with retailer locations
- Supporting maps: Income overlay, population density
- 2-page policy brief with recommendations

**What made it successful:**

- Clear, focused question with practical implications
- Combined multiple techniques from the course
- Addressed a real community issue with actionable findings

---

## Example 2: Environmental Analysis

### Urban Heat Island Mapping in Melbourne

**Research question:** How does vegetation cover correlate with surface temperature across Melbourne's suburbs?

**Methods used:**

- Landsat thermal imagery (raster processing)
- NDVI calculation for vegetation index
- Zonal statistics by suburb
- Regression analysis (temperature vs. vegetation)

**Key findings:**

- Strong negative correlation (r = -0.72) between vegetation cover and surface temperature
- Industrial suburbs up to 8 degrees C hotter than leafy residential areas
- Identified 15 priority suburbs for urban greening interventions

**Deliverables:**

- Surface temperature map with suburb boundaries
- NDVI vegetation map for comparison
- Scatter plot of temperature vs. vegetation by suburb
- Jupyter notebook with reproducible analysis

**What made it successful:**

- Leveraged Python skills for raster processing
- Quantified relationships, not just described patterns
- Produced reproducible, documented analysis

---

## Example 3: Public Health

### Emergency Department Accessibility in Rural Queensland

**Research question:** What proportion of rural Queensland residents live beyond 30 minutes drive time from an emergency department?

**Methods used:**

- Hospital location data from Queensland Health
- Road network from OSM
- Drive-time service areas (QNEAT3 plugin)
- Population overlay from census mesh blocks
- Demographic breakdown of underserved populations

**Key findings:**

- 18% of rural residents beyond 30-minute threshold
- Indigenous communities 2.8x more likely to face access barriers
- Western Queensland most underserved; coastal areas well-covered

**Deliverables:**

- Service area map showing 15/30/60 minute zones
- Population heat map of underserved areas
- Demographic profile of affected populations
- Presentation to local health advocacy group

**What made it successful:**

- Directly relevant to health equity discussions
- Used network analysis for realistic travel times
- Engaged with real stakeholders beyond the classroom

---

## Example 4: Crime and Safety

### Bicycle Theft Hotspots in Inner Melbourne

**Research question:** Where are bicycle theft hotspots in inner Melbourne, and how do they relate to cycling infrastructure?

**Methods used:**

- Crime data from Victoria Police (2 years)
- Bicycle parking locations
- Bike lane network
- Kernel density estimation
- Hotspot analysis (Getis-Ord Gi*)

**Key findings:**

- Three major hotspot clusters: CBD, university precincts, major train stations
- Hotspots correlate with high cycling volumes, not poor infrastructure
- Evening hours (6-10pm) show different patterns than daytime

**Deliverables:**

- Hotspot map with infrastructure overlay
- Time-series comparison (day vs. evening)
- Recommendations for bike parking security improvements

**What made it successful:**

- Creative data combination (crime + infrastructure)
- Temporal analysis added depth
- Practical recommendations derived from spatial patterns

---

## Example 5: Urban Planning

### Walkability Score Comparison Across Sydney LGAs

**Research question:** How do walkability conditions vary across Sydney's local government areas?

**Methods used:**

- OpenStreetMap data (roads, footpaths, crossings)
- Points of interest (shops, services, transit)
- Custom walkability index calculation
- Spatial aggregation by statistical area
- Comparative choropleth mapping

**Key findings:**

- Inner-city LGAs score 3-4x higher than outer suburbs
- Newer developments (post-2000) have lower walkability than older suburbs
- Correlation between walkability and median property values

**Deliverables:**

- Walkability index map
- Component maps (path density, POI access, transit access)
- Methodology document explaining index calculation
- Comparison table ranking LGAs

**What made it successful:**

- Created a custom analytical framework (the index)
- Compared across multiple areas systematically
- Documented methodology for reproducibility

---

## Example 6: Transport Analysis

### Public Transit Equity in Brisbane

**Research question:** Do low-income neighborhoods have equitable access to high-frequency public transit?

**Methods used:**

- GTFS data for transit schedules
- Service frequency calculation
- Walking distance buffers around stops
- Census income data join
- Equity analysis comparing access by income quintile

**Key findings:**

- High-frequency transit (10-min or better) serves only 23% of population
- Lowest income quintile actually has best access (inner-city concentration)
- Middle-income suburbs in middle ring most underserved

**Deliverables:**

- Transit frequency map
- Equity comparison chart by income quintile
- Service gap identification map

**What made it successful:**

- Challenged assumptions (expected low-income = poor access)
- Used GTFS data creatively
- Quantified equity with clear metrics

---

## Common Characteristics of Strong Capstones

1. **Focused question:** One clear research question, not three vague ones
2. **Appropriate scope:** Manageable study area; realistic for available time
3. **Multiple methods:** Combined 2-3 techniques from the course
4. **Original analysis:** Not just displaying data; answering a question
5. **Clear communication:** Well-designed maps that tell a story
6. **Honest limitations:** Acknowledged what the analysis couldn't show

---

## Common Pitfalls to Avoid

- **Scope creep:** Starting with one question and adding three more
- **Data hunting:** Spending all your time looking for perfect data that doesn't exist
- **Tool obsession:** Trying to learn ArcGIS/QGIS plugin/Python library you've never used
- **Map overload:** Creating 15 maps when 4 good ones would tell the story
- **Missing the "so what":** Beautiful maps that don't answer a question

---

## Getting Started

1. Review these examples for inspiration
2. Brainstorm 3-5 questions relevant to your interests
3. Check data availability for each
4. Pick the most feasible option with meaningful output
5. Complete the [Capstone Proposal Template](capstone-template.md)
6. Get feedback from peers and instructor before diving in

Your capstone doesn't need to solve a global problem; it needs to demonstrate your skills and answer a question you care about.
