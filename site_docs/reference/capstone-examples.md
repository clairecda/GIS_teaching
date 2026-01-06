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

## Example 5: Environmental Science

### Koala Habitat Connectivity in Southeast Queensland

**Research question:** How connected are koala habitat patches in the Redlands Coast area, and where are the critical corridors?

**Methods used:**

- Vegetation mapping (state government data)
- Koala sighting records (wildlife surveys + citizen science)
- Land use classification (raster)
- Least-cost path analysis for corridor identification
- Road density as barrier metric

**Key findings:**

- 40% habitat loss in study area since 2010
- Three critical corridors identified connecting major habitat patches
- Two corridors bisected by proposed development areas
- Road mortality hotspots align with corridor crossing points

**Deliverables:**

- Habitat patch map with connectivity scores
- Corridor priority map for conservation planning
- Change detection map (2010 vs 2023)
- Recommendations for wildlife crossing infrastructure

**What made it successful:**

- Combined ecological data with infrastructure analysis
- Used change detection to show trends over time
- Produced actionable conservation recommendations
- Engaged with local wildlife group for data sharing

---

## Methods Quick Reference

Not sure how to do something mentioned in these examples? Here's where to find each technique:

| Method | QGIS | Python | What It Does |
|--------|------|--------|--------------|
| **Choropleth mapping** | [Week 2](../weeks/week02.md) | — | Colour areas by data values (e.g., income by suburb) |
| **Spatial joins** | [Week 3](../weeks/week03.md) | [Week 8](../weeks/week08.md) | Attach data from one layer to another based on location |
| **Zonal statistics** | [Week 4](../weeks/week04.md) | [Week 9](../weeks/week09.md) | Calculate statistics (mean, sum) for areas from raster data |
| **NDVI calculation** | [Week 4](../weeks/week04.md) | [Week 9](../weeks/week09.md) | Measure vegetation health from satellite imagery |
| **Kernel density (KDE)** | [Week 5](../weeks/week05.md) | — | Create heatmaps showing concentration of points |
| **Hotspot analysis (Gi*)** | [Week 5](../weeks/week05.md) | — | Identify statistically significant clusters |
| **Isochrones (service areas)** | [Week 6](../weeks/week06.md) | [Week 10](../weeks/week10.md) | Calculate travel-time zones from locations |
| **Shortest/least-cost paths** | [Week 6](../weeks/week06.md) | [Week 10](../weeks/week10.md) | Find optimal routes considering distance or custom costs |
| **Change detection** | — | [Week 9](../weeks/week09.md) | Compare two time periods to find differences |

**Choose your tool:**

- **QGIS** = Interactive exploration, visual feedback, one-off analyses
- **Python** = Reproducibility, batch processing, scaling to larger datasets

### External Resources

For techniques beyond the course:

- **Walkability indices:** [Walkability methods overview](https://www.walkscore.com/methodology.shtml)
- **Species distribution:** [QGIS Species Distribution tutorial](https://docs.qgis.org/latest/en/docs/training_manual/)
- **Flood risk:** [QGIS Sketcher - terrain analysis](https://www.sketcher.io/)
- **Site suitability:** Search "QGIS weighted overlay analysis"

Don't try to learn a completely new technique for your capstone—build on what you've already practiced in the weekly labs.

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
