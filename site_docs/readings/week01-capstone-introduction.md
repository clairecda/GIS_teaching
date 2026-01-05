# Your Capstone Project

**Read in:** Week 1 | **Time:** 10 minutes

---

## What is the capstone?

The capstone is your chance to apply everything you learn to a project you care about. You'll choose a spatial question, gather data, perform analysis, create maps, and tell a story with your findings.

**This isn't a Week 12 task.** You'll work on it throughout the course, building skills each week that feed directly into your final project.

---

## What you'll produce

By Week 12, you'll have:

1. **A spatial question** you've answered with data
2. **Analysis** using techniques from the course (joins, hotspots, accessibility, etc.)
3. **Maps** that communicate your findings clearly
4. **Documentation** explaining your methods and limitations
5. **A short presentation** sharing your work with the class

---

## Timeline: How the weeks connect

| Week | Course topic | Capstone milestone |
|------|--------------|-------------------|
| 1 | GIS fundamentals | **Start thinking:** What spatial questions interest you? |
| 2 | Cartography & design | Consider how you'll visualise your findings |
| 3 | Boundaries & joins | **Choose your study area:** What boundaries will you use? |
| 4 | Raster & elevation | Does your project need terrain or imagery data? |
| 5 | Crime & ethics | **Refine your question:** Is it ethical? What are the limitations? |
| 6 | Health & accessibility | Could accessibility analysis apply to your topic? |
| 7 | Python introduction | Start thinking about automation |
| 8 | Vector workflows | **Data collection deadline:** Have your datasets ready |
| 9 | Remote sensing | Add satellite imagery if relevant |
| 10 | Network analysis | Add routing/accessibility if relevant |
| 11 | Design & storytelling | **Draft maps due:** Get feedback on your visualisations |
| 12 | Capstone presentations | **Final submission:** Present your project |

---

## Choosing your topic

Your project should:

- **Be spatial** — location must matter to the question
- **Use course techniques** — at least 2-3 methods from the course
- **Have available data** — don't pick something you can't get data for
- **Interest you** — you'll spend 12 weeks on this

### Good capstone questions

- "Where should a new community health centre be located in [area]?"
- "How has urban development changed in [suburb] over the past 10 years?"
- "Which neighbourhoods have the poorest access to public transport?"
- "Where are the crime hotspots in [city] and what factors correlate with them?"
- "How does flood risk relate to socioeconomic disadvantage in [region]?"

### Less suitable questions

- "What is the population of Australia?" (not spatial analysis)
- "Map every tree in Sydney" (too large, no question)
- "Predict future climate change" (beyond course scope)

---

## Finding your data

Start looking for data in Week 1. Good sources:

**Australia:**
- [data.gov.au](https://data.gov.au) — Federal open data
- [data.nsw.gov.au](https://data.nsw.gov.au) — NSW open data (similar for other states)
- [ABS](https://www.abs.gov.au) — Census, SEIFA, boundaries
- [ELVIS](https://elevation.fsdf.org.au/) — Elevation data

**Global:**
- [Natural Earth](https://www.naturalearthdata.com/) — Global boundaries
- [OpenStreetMap](https://www.openstreetmap.org/) — Roads, buildings, amenities
- [USGS Earth Explorer](https://earthexplorer.usgs.gov/) — Satellite imagery

**Tip:** Check data availability before committing to a topic.

---

## Project structure

Use the same folder structure you've been using all course:

```
intro-gis/
├── data/
│   ├── raw/           ← Original downloads (never edit!)
│   └── processed/     ← Cleaned/modified data
├── projects/          ← QGIS project files (.qgz)
├── exports/           ← Your map outputs
└── notebooks/         ← Python analysis (Weeks 7+)
```

For your capstone, you might want to keep capstone-specific files together. You could either:

- Use clear naming: `raw/capstone_suburbs.gpkg`, `processed/capstone_analysis.gpkg`
- Create a subfolder: `raw/capstone/`, `processed/capstone/`

The key habit: **raw files stay untouched, processed files show your work**.

---

## Weekly capstone tasks

Add these to your weekly workflow:

**Weeks 1-2:** Brainstorm 3 possible topics. Check data availability.

**Week 3:** Narrow to 1 topic. Download initial boundary data.

**Week 4:** Identify all datasets you'll need. Start downloading.

**Week 5:** Write a 1-paragraph project description. Note ethical considerations.

**Week 6:** Complete data collection. Identify gaps.

**Week 7:** Set up your capstone folder structure. Document data sources.

**Week 8:** Begin analysis. Create first draft maps.

**Week 9-10:** Refine analysis. Add Python automation if relevant.

**Week 11:** Polish maps. Get peer feedback. Write documentation.

**Week 12:** Final presentation. Submit all materials.

---

## Assessment criteria

Your capstone will be assessed on:

| Criteria | What we're looking for |
|----------|------------------------|
| **Question** | Clear, spatial, answerable with available data |
| **Data** | Appropriate sources, documented, properly processed |
| **Analysis** | Uses course techniques correctly, appropriate methods |
| **Visualisation** | Clear maps, good design, tells a story |
| **Documentation** | Methods explained, limitations acknowledged |
| **Presentation** | Clear communication, answers audience questions |

---

## Advanced analysis: spatial statistics

If your capstone involves analyzing relationships between variables (e.g., "Does distance to green space correlate with health outcomes?"), you may need **spatial regression**.

**Why it matters:** Standard regression assumes observations are independent, but spatial data clusters—nearby locations have similar values. Ignoring this can give misleading results.

**Resources for capstone:**

- [Spatial Statistics & Regression reading](spatial-statistics.md) — concepts and interpretation
- [Spatial Statistics notebook](../reference/notebooks.md) — worked Python examples

You don't need to master this in Week 1. Revisit these resources when you start analysis in Weeks 8-10.

---

## Getting help

- **Weekly check-ins:** Mention your capstone progress in class
- **Office hours:** Bring specific questions about your project
- **Peer feedback:** Share drafts with classmates for input
- **Week 11:** Dedicated time for design critique and feedback

---

## Start now

This week:

1. **Brainstorm 3 topics** that interest you
2. **Check data availability** for each
3. **Create your capstone folder** structure
4. **Start a notes file** to track ideas and decisions

Don't wait until Week 12. The best capstones are built gradually throughout the course.
