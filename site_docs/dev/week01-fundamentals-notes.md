# Week 1 Lecture · Foundations of GIS

Set the tone for the course by introducing what GIS is, how it is used, and the mind-set shift from spreadsheets to spatial storytelling.

## Lecture objectives

By the end of this session learners should be able to:

1. Articulate a working definition of GIS and describe why “where” matters in data analysis.
2. Distinguish between vector and raster data models and cite everyday examples of each.
3. Recognise the importance of metadata (coordinate reference systems, extent, resolution, vintage) when evaluating spatial datasets.
4. Connect the lecture material to the Week 1 lab, which focuses on exploring the QGIS interface and inspecting Natural Earth datasets.

## Recommended structure

### 1. Why GIS? (Slides 1–4)
- Define GIS as the integration of spatial and attribute data, supported by hardware, software, and people.
- Use scenarios from transport planning, emergency response, and public health to show real-world impact.
- Reference the [Esri overview article](../readings/week01-what-is-gis.md) and pull 2–3 quotable stats or graphics.

### 2. Spatial vs tabular thinking (Slides 5–7)
- Contrast a traditional spreadsheet of addresses with a geocoded point map to emphasise pattern recognition.
- Introduce the idea of “scale” (global → regional → local) and how questions change at each level.
- Highlight the concept of geographic context (proximity, adjacency, containment).

### 3. Data models: Vector & raster (Slides 8–11)
- Vector: point (bus stop), line (river, road), polygon (suburb, LGA). Mention topology and attribute tables.
- Raster: grid of pixels capturing continuous phenomena (elevation, temperature, imagery). Touch on resolution and band combinations.
- Tie back to the reading on [Spatial Data Models](../readings/week02-data-models.md) as optional pre-reading for Week 2.

### 4. Metadata essentials (Slides 12–14)
- Break down CRS (geographic vs projected), why mismatched CRS produce misaligned layers, and examples relevant to Australia (EPSG:7856) and global datasets (EPSG:4326).
- Cover extent, resolution, vintage, and licensing. Provide a screenshot of the QGIS layer properties panel showing metadata fields.

### 5. GIS workflow building blocks (Slides 15–17)
- Introduce the lightweight GIS workflow learners will practise: acquire data → inspect metadata → clean/format → analyse/visualise → communicate.
- Position QGIS as the “hands-on” environment they will use in Weeks 1–6 before transitioning to automation.
- Include a slide referencing the Week 1 lab outcomes (set up project, load Natural Earth, export a quick map).

### 6. Closing & reflection (Slides 18–19)
- Summarise key takeaways and preview the next lecture (cartographic conventions).
- Prompt learners to jot down one domain-specific question they hope to answer with GIS.

## Key vocabulary to cover

- **GIS:** Geographic Information System (integration of spatial + attribute data for analysis/visualisation).
- **Spatial data:** Data that includes location (coordinates, addresses, regions).
- **Vector data:** Points, lines, polygons stored with attributes.
- **Raster data:** Gridded pixels storing values; often continuous phenomena.
- **Attribute table:** Tabular data linked to spatial features.
- **Coordinate Reference System (CRS):** Framework used to map the Earth’s surface (e.g., WGS84, GDA2020).
- **Metadata:** “Data about data” — provides context such as source, scale, resolution, date, license.

## Live demo ideas

- Demonstrate a CSV-to-map moment: show a table of city names/coordinates, then drag into QGIS to plot points.
- Open the Natural Earth Admin 0 shapefile and inspect the attribute table; highlight how fields connect to the map.
- Display layer properties to point out CRS, extent, and licensing information.
- Use the Identify tool on a feature to reinforce the link between map and attribute data.

## Sample case-study snippets

- **Transport:** Mapping train station catchments to illustrate first/last mile challenges.
- **Health:** Visualising vaccination clinic locations versus population density to reveal gaps.
- **Environment:** Overlaying flood-prone areas with housing to discuss resilience planning.

## On-slide callouts & visuals

- Diagram showing layers stacking (basemap, points, polygons) akin to a “data sandwich.”
- Graphic comparing vector and raster data side-by-side (e.g., polygon boundary vs DEM tile).
- Screenshot of QGIS interface labelled with Browser, Layers, Processing Toolbox panels.
- Map highlighting CRS mismatch (misaligned layers) versus corrected alignment.

## Discussion prompts

- Where have you encountered GIS outputs in everyday life (navigation apps, weather, election maps)?
- What decisions in your field could change if you understood spatial context better?
- What concerns or opportunities do you see when combining location data with people-centric datasets?

## Instructor tips

- Gauge prior experience with a quick show-of-hands or poll (GIS novices vs experienced users).
- Use local datasets/examples to make the content tangible for your cohort.
- Keep the lecture interactive—pose questions after each section and invite learners to share domain-specific examples.
- Reinforce that the upcoming lab is exploratory; perfection is not expected.

## Suggested follow-up for learners

- Complete the readings and jot down one question to raise during lab.
- Make sure QGIS opens without errors and you can locate the `intro-to-gis-course` workspace.
- Download the Natural Earth layers ahead of the lab (see [Downloading datasets](../onboarding/data-downloads.md)).
