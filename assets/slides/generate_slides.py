"""
Generate HTML slide decks for each week.

Run from the repository root:

    python assets/slides/generate_slides.py

Each entry in SLIDES defines the title and sections to render.

The generated slides feature:
- Professional teal/blue color scheme matching MkDocs theme
- Keyboard navigation (arrow keys, spacebar, Home/End)
- Responsive design for different screen sizes
- Print-friendly CSS for PDF export
- Slide numbers and navigation controls
- Automatic table of contents
- Accessibility features (ARIA labels, semantic HTML)
"""

from pathlib import Path
from typing import List, Union, Dict, Tuple


SLIDES = {
    "week01.html": {
        "title": "Week 01 – Foundations of GIS",
        "sections": [
            (
                "Week 01 · Foundations of GIS",
                "Where are things? Why are they there? What patterns emerge? GIS helps us answer these questions by connecting location to data—and this course will take you from first maps to scripted analysis.",
            ),
            (
                "The Power of 'Where'",
                [
                    "Every dataset becomes richer when you add location: a crime report becomes a hotspot, a hospital address becomes an access gap.",
                    "GIS integrates WHERE (coordinates) with WHAT (attributes like population, temperature, or price).",
                    "Real-world examples: ride-share apps predicting demand, councils planning new parks, epidemiologists tracking outbreaks.",
                    "By the end of this course, you'll create maps that inform decisions, automate repetitive tasks, and tell compelling stories with data.",
                ],
            ),
            (
                "Thinking Spatially",
                [
                    "A spreadsheet shows \"50 burglaries in Sydney\" — a map reveals they cluster near transit stations at night.",
                    "Scale matters: national policy vs neighbourhood intervention require different geographic units.",
                    "Core spatial concepts: proximity (how close?), adjacency (what's next door?), containment (what's inside?), connectivity (what's linked?).",
                    "Same metric, new story: unemployment rate feels different mapped by suburb than listed in a table.",
                ],
            ),
            (
                "Vector vs Raster Data",
                [
                    "VECTOR = discrete features: a point (bus stop), line (river), polygon (council boundary) plus attributes in a table.",
                    "RASTER = continuous surfaces: a grid of cells (pixels) storing values like elevation, temperature, or satellite reflectance.",
                    "Rule of thumb: use vector for 'things', raster for 'fields' that vary continuously across space.",
                    "Common formats: Shapefile, GeoPackage, GeoJSON (vector); GeoTIFF, NetCDF (raster).",
                ],
            ),
            (
                "Why Metadata Matters",
                [
                    "CRS (Coordinate Reference System): ensures your layers line up. Mix GDA2020 with WGS84 and points shift 1–2 metres!",
                    "Extent: what geographic area does the dataset cover? A national dataset won't give you suburb-level detail.",
                    "Vintage: data from 2016 may not reflect today's reality. Always record download date and source version.",
                    "In QGIS: right-click a layer → Properties → Information tab to view metadata.",
                ],
            ),
            (
                "A Simple GIS Workflow",
                [
                    "1. ACQUIRE — download from authoritative sources (ABS, Natural Earth, OpenStreetMap).",
                    "2. INSPECT — check CRS, extent, attribute fields before trusting the data.",
                    "3. CLEAN — fix missing values, reproject to a common CRS, rename confusing columns.",
                    "4. ANALYSE — spatial queries, overlays, statistics, modelling.",
                    "5. COMMUNICATE — export a well-designed map or dashboard for your audience.",
                ],
            ),
            (
                "Meet QGIS",
                [
                    "Browser panel: connect folders, databases, web services; drag layers onto the map canvas.",
                    "Layers panel: control draw order, visibility, symbology—top layers draw on top.",
                    "Map canvas: your visual workspace; pan, zoom, identify features.",
                    "Processing Toolbox: 400+ analysis tools—we'll unlock these progressively.",
                ],
            ),
            (
                "Lab Step 1: Set Up Your Workspace",
                [
                    "Create folder: intro-gis-course/ on your Desktop or Documents",
                    "Inside it, create: data/raw/, data/processed/, projects/, exports/",
                    "Download Natural Earth countries from naturalearthdata.com (Admin 0 - Countries)",
                    "Unzip to: data/raw/natural_earth/",
                    "Keep raw data untouched — we'll never edit files in data/raw/",
                ],
            ),
            (
                "Lab Step 2: Load and Inspect Data",
                [
                    "Open QGIS → Project → New",
                    "Browser panel → navigate to your data/raw/natural_earth/ folder",
                    "Drag ne_110m_admin_0_countries.shp onto the map canvas",
                    "Right-click layer → Open Attribute Table — explore the fields",
                    "Key fields: NAME (country name), POP_EST (population), CONTINENT",
                ],
            ),
            (
                "Lab Step 3: Apply Symbology",
                [
                    "Right-click layer → Properties → Symbology tab",
                    "Change 'Single Symbol' dropdown to 'Categorized'",
                    "Value: select CONTINENT → click 'Classify' → Apply",
                    "Each continent now has a different colour!",
                    "Try 'Graduated' with POP_EST to see population variation",
                ],
            ),
            (
                "Lab Step 4: Create Print Layout",
                [
                    "Project → New Print Layout → name it 'Week01_Map'",
                    "Add Item → Add Map → draw rectangle on the page",
                    "Add Item → Add Legend (position bottom-left)",
                    "Add Item → Add Scale Bar (position bottom-right)",
                    "Add Item → Add Label → type your title at the top",
                ],
            ),
            (
                "Lab Step 5: Export Your Map",
                [
                    "Add source credit: 'Data: Natural Earth, 2024'",
                    "Add your name and date",
                    "Layout → Export as Image → save to exports/week01_world_map.png",
                    "Choose 300 DPI for high quality",
                    "Congratulations — your first GIS map!",
                ],
            ),
            (
                "Discussion Prompts",
                [
                    "When was the last time you used a map app (Google Maps, transit planner, weather radar)? What questions did it answer?",
                    "Think of a dataset in your field—how might adding location reveal new insights?",
                    "What's one skill you hope to leave this course with?",
                ],
            ),
            (
                "Before Next Week",
                [
                    "Complete the Week 01 reflection prompt in your notes folder.",
                    "Download renewable energy and world cities datasets (see Data Download Checklist).",
                    "Explore QGIS: Help → Sketcher to try drawing, or browse plugins in the Plugin Manager.",
                ],
            ),
        ],
    },
    "week02.html": {
        "title": "Week 02 – Symbology, Labelling & Layouts",
        "sections": [
            (
                "Week 02 · Symbology, Labelling & Layouts",
                "A map is a visual argument. Today we learn the cartographic grammar that transforms raw data into clear, accessible, and persuasive communication.",
            ),
            (
                "Design with Purpose",
                [
                    "Before touching colour: What story does this map tell? Who will read it? What action should they take?",
                    "Comparison maps: 'Which regions are growing?' — use consistent scale and symbology.",
                    "Pattern maps: 'Where are the hotspots?' — graduated colours or density shading.",
                    "Persuasion maps: 'Why invest here?' — highlight key features, de-emphasise distractions.",
                ],
            ),
            (
                "Choosing Colour Ramps",
                [
                    "SEQUENTIAL: light-to-dark for ordered data (low→high population). One hue, varying intensity.",
                    "DIVERGING: two hues from a neutral midpoint (above/below average, temperature anomalies).",
                    "QUALITATIVE: distinct hues for unordered categories (land use types, states). No implied ranking.",
                    "Resource: colorbrewer2.org — pick a ramp, check 'colorblind safe', export to QGIS.",
                ],
            ),
            (
                "Classification Methods",
                [
                    "EQUAL INTERVAL: same-size bins. Good for evenly spread data; misleading when skewed.",
                    "QUANTILES: same number of features per bin. Great for rankings; can hide outliers.",
                    "NATURAL BREAKS (Jenks): minimises variance within classes. Good default; less intuitive bin edges.",
                    "Tip: always inspect histogram before choosing method—know your data's distribution.",
                ],
            ),
            (
                "Accessibility Matters",
                [
                    "8% of men, 0.5% of women have colour vision deficiency—never rely on colour alone.",
                    "Use Color Oracle (free) to simulate how your map appears to colourblind viewers.",
                    "Text contrast: 4.5:1 ratio minimum. Small grey labels on white fail this test.",
                    "Redundant encoding: pair colour with pattern, size, or labels so information survives print/photocopy.",
                ],
            ),
            (
                "Labelling Best Practices",
                [
                    "Less is more: only label features your reader needs to locate.",
                    "Use halos or buffers so text pops from busy backgrounds.",
                    "Curved labels follow coastlines/rivers; straight labels for grids and urban streets.",
                    "Expression-based labelling: show city names only above 1M population to reduce clutter.",
                ],
            ),
            (
                "The Print Layout",
                [
                    "Every finished map needs: Title, Legend, Scale bar, North arrow, Data sources, Author/date.",
                    "Hierarchy: title largest, legend readable, sources smallest but present.",
                    "Alignment: use guides and grids in QGIS Layout View for pixel-perfect placement.",
                    "Export at 300 DPI for print, 150 DPI for web/presentations.",
                ],
            ),
            (
                "Lab Step 1: Load Renewable Energy Data",
                [
                    "Download renewable energy CSV from course data checklist",
                    "Layer → Add Layer → Add Delimited Text Layer",
                    "Select your CSV file, set X=longitude, Y=latitude",
                    "CRS: WGS 84 (EPSG:4326) — the standard for lat/long",
                    "You should see points scattered across the world map",
                ],
            ),
            (
                "Lab Step 2: Style with Graduated Colours",
                [
                    "Right-click layer → Properties → Symbology",
                    "Change to 'Graduated', select capacity field",
                    "Try 'Equal Interval' with 5 classes → Apply",
                    "Now try 'Quantiles' — notice how the map changes",
                    "Which classification tells the story better?",
                ],
            ),
            (
                "Lab Step 3: Choose an Accessible Colour Ramp",
                [
                    "In Symbology, click the colour ramp dropdown",
                    "Choose a sequential ramp (light → dark) like 'YlOrRd'",
                    "Install Color Oracle (colororacle.org) → run it",
                    "Does your map still make sense in grayscale?",
                    "Adjust if needed — accessibility matters!",
                ],
            ),
            (
                "Lab Step 4: Add Labels to Major Sites",
                [
                    "Right-click layer → Properties → Labels tab",
                    "Single Labels → Value: site_name field",
                    "Problem: too many labels! Let's filter them",
                    "Use expression: \"capacity\" > 500 (only show large sites)",
                    "Add buffer/halo: 1mm white to improve readability",
                ],
            ),
            (
                "Lab Step 5: Build Your Layout",
                [
                    "Create new Print Layout → add map, legend, title",
                    "Title: 'Global Renewable Energy Capacity, 2024'",
                    "Legend: remove unneeded items, rename 'capacity' to 'Capacity (MW)'",
                    "Add scale bar, north arrow, and data source",
                    "Export as PDF at 300 DPI for printing",
                ],
            ),
            (
                "Reflection",
                [
                    "What single design change most improved your map's clarity?",
                    "How might your colour choices mislead or exclude certain audiences?",
                    "What's one element you'll pay more attention to in future maps?",
                ],
            ),
        ],
    },
    "week03.html": {
        "title": "Week 03 – Vector Analysis & Attribute Joins",
        "sections": [
            (
                "Week 03 · Vector Analysis & Attribute Joins",
                "Boundaries shape how we see data. Today we connect tabular statistics to spatial units—turning spreadsheets into maps that reveal inequality, opportunity, and change.",
            ),
            (
                "The Boundary Hierarchy",
                [
                    "ADMINISTRATIVE: political/governance units (countries → states → councils). Boundaries change with legislation.",
                    "STATISTICAL: census-defined for data collection (SA1 → SA2 → SA3 → SA4 in Australia; tract → county in US).",
                    "KEY INSIGHT: SA2 ≈ 'community' (3,000-25,000 people), ideal for socio-economic analysis. LGAs better for policy/service planning.",
                    "Always ask: Which boundary aligns with the decision being made?",
                ],
            ),
            (
                "Vintage Matters",
                [
                    "Boundaries change! Australia's ASGS had major revisions in 2011, 2016, 2021.",
                    "Comparing 2016 SEIFA scores on 2021 boundaries = mismatch. Use correspondence tables or note limitations.",
                    "Best practice: record boundary version in metadata AND map footer (e.g., 'SA2 (ASGS 2021)').",
                ],
            ),
            (
                "Attribute Joins Explained",
                [
                    "A join links a table (CSV, Excel) to spatial features via a common key (e.g., SA2_CODE21).",
                    "Key challenges: data types must match (string vs integer), leading zeros get dropped, whitespace sneaks in.",
                    "Before joining: inspect both tables—how many records? Any duplicates? Any missing keys?",
                    "After joining: check for NULLs—unmatched records disappear unless you do a LEFT join.",
                ],
            ),
            (
                "Step-by-Step Join Workflow",
                [
                    "1. Add boundary shapefile and CSV to QGIS.",
                    "2. Open boundary Properties → Joins → Add (+).",
                    "3. Select CSV, choose join field and target field, optionally prefix columns.",
                    "4. Verify in Attribute Table: do values appear? Any NULLs?",
                    "5. Export to GeoPackage to make join permanent.",
                ],
            ),
            (
                "Creating Derived Metrics",
                [
                    "Raw counts mislead: 500 crimes in CBD ≠ 500 crimes in rural town (populations differ).",
                    "Normalise by area, population, or households (crimes per 1,000 residents, GP clinics per km²).",
                    "Field Calculator: \"crime_rate\" = (crimes / population) * 1000",
                    "Rank or categorise: percentiles, deciles, z-scores for comparison across regions.",
                ],
            ),
            (
                "Today's Lab: Mapping Socio-Economic Advantage",
                [
                    "Load SA2 boundaries and SEIFA 2021 index of advantage/disadvantage.",
                    "Join on SA2 code; check for NULLs in regional areas.",
                    "Create choropleth using diverging colour ramp centred on the median score.",
                    "Add context layers (hospitals, schools) and discuss what patterns emerge.",
                ],
            ),
            (
                "Reflection",
                [
                    "What join issues did you encounter? How did you fix them?",
                    "How does your choice of boundary (SA2 vs LGA) change the story?",
                    "What ethical considerations arise when mapping disadvantage?",
                ],
            ),
        ],
    },
    "week04.html": {
        "title": "Week 04 – Raster & Terrain Analysis",
        "sections": [
            (
                "Week 04 · Raster & Terrain Analysis",
                "The Earth's surface shapes where we build, farm, and live. Today we work with elevation data to reveal flood risk, suitable slopes, and the hidden topography beneath our feet.",
            ),
            (
                "Understanding Elevation Models",
                [
                    "DEM (Digital Elevation Model): bare earth surface—ground level without trees or buildings.",
                    "DSM (Digital Surface Model): includes canopy, buildings—first reflected surface.",
                    "DTM (Digital Terrain Model): often DEM + breaklines (ridges, streams) for higher accuracy.",
                    "For most planning tasks, you want a DEM. For visibility/solar analysis, DSM may be better.",
                ],
            ),
            (
                "Resolution & Accuracy",
                [
                    "30m SRTM: free, global coverage, good for regional analysis. Not for site-level design.",
                    "5m ELVIS: Australian national coverage, suitable for catchment studies.",
                    "1m LiDAR: high accuracy, often available from state agencies for urban areas.",
                    "Golden rule: never use a 30m DEM to assess flooding on a single property!",
                ],
            ),
            (
                "Derived Surfaces",
                [
                    "HILLSHADE: simulated sun illumination—makes terrain 'pop' as a basemap.",
                    "SLOPE: angle of incline (degrees or %). Key for erosion, construction, accessibility.",
                    "ASPECT: compass direction a slope faces (N, S, E, W). Critical for solar, agriculture, ecology.",
                    "CONTOURS: lines of equal elevation. Extract from DEM for cartographic display.",
                ],
            ),
            (
                "Zonal Statistics",
                [
                    "Summarise raster values within polygons (mean elevation per suburb, max slope per parcel).",
                    "QGIS: Processing → Raster Analysis → Zonal Statistics.",
                    "Use case: which LGAs have the highest flood exposure (% area below 5m elevation)?",
                    "Always clip raster to study area first—processing 1GB of data you don't need wastes time.",
                ],
            ),
            (
                "Workflow: Flood Risk Example",
                [
                    "1. Download DEM from ELVIS or SRTM.",
                    "2. Clip to LGA boundary; reproject to GDA2020/MGA zone for accurate measurements.",
                    "3. Reclassify elevation: below 5m = high risk, 5-10m = moderate, above 10m = low.",
                    "4. Overlay with population data (SA1) to estimate exposed residents.",
                    "5. Map output with clear legend and source credits.",
                ],
            ),
            (
                "Today's Lab: Terrain Mapping",
                [
                    "Download SRTM tile for your study region via USGS EarthExplorer.",
                    "Generate hillshade and slope in QGIS; style slope with a red-yellow-green ramp (steep = red).",
                    "Clip to SA2 boundary and compute mean slope per zone.",
                    "Discuss: what land-use or planning decisions might use this output?",
                ],
            ),
            (
                "Reflection",
                [
                    "What surprised you about the terrain of your study area?",
                    "How would using a 1m DEM vs 30m DEM change your analysis?",
                    "What additional data layers would strengthen a flood risk story?",
                ],
            ),
        ],
    },
    "week05.html": {
        "title": "Week 05 – Crime Hotspots & Storytelling",
        "sections": [
            (
                "Week 05 · Crime Hotspots & Storytelling",
                "Crime maps shape public perception, police deployment, and community investment. Today we learn techniques for hotspot analysis—and the ethical responsibility that comes with them.",
            ),
            (
                "The Ethics of Crime Mapping",
                [
                    "Crime data reflects what's REPORTED, not what happens. Some crimes under-reported, some neighbourhoods over-policed.",
                    "Maps can reinforce stereotypes: labelling a suburb 'high crime' affects house prices, insurance, perceptions.",
                    "Privacy matters: point-level data can identify victims. Always aggregate to appropriate scale.",
                    "Ask: Who benefits from this map? Who might be harmed?",
                ],
            ),
            (
                "Understanding the Data",
                [
                    "NSW BOCSAR data: recorded offences by LGA, category, month. Strengths: official, consistent. Weaknesses: reporting bias.",
                    "UK Police data: street-level points (anonymised to nearest street). More granular, but location fuzzing affects precision.",
                    "Always filter by time period and offence type relevant to your question—don't conflate shoplifting with assault.",
                ],
            ),
            (
                "Kernel Density Estimation (KDE)",
                [
                    "KDE creates a continuous surface showing intensity of points—'hotter' where incidents cluster.",
                    "Bandwidth (search radius): too small = noisy, too large = over-smoothed. Experiment with 200m, 500m, 1km.",
                    "In QGIS: Processing → Interpolation → Heatmap (Kernel Density Estimation).",
                    "Output is a raster; symbolise with a warm colour ramp (yellow→orange→red).",
                ],
            ),
            (
                "Alternative Aggregation Methods",
                [
                    "HEX BINNING: count points within hexagonal grid cells. Uniform shape, easier to compare than irregular polygons.",
                    "FISHNET GRID: square cells, simpler but corners can distort perception.",
                    "BOUNDARY COUNTS: aggregate to SA2/LGA. Good for policy, but hides within-area variation.",
                    "Normalise by population or area (offences per 1,000 residents) to compare fairly.",
                ],
            ),
            (
                "Telling a Responsible Story",
                [
                    "CONTEXT: pair crime data with street lighting, public transport, SEIFA index.",
                    "LIMITATIONS: state clearly what the data does NOT show (unreported crime, clearance rates).",
                    "SOLUTIONS: if showing a problem, can you also show interventions or assets?",
                    "AUDIENCE: a police briefing differs from a community newsletter. Adjust detail and framing.",
                ],
            ),
            (
                "Today's Lab: Hotspot Mapping",
                [
                    "Load NSW BOCSAR or UK Police data as CSV; geocode or use provided coordinates.",
                    "Run KDE with 500m bandwidth; experiment with 200m and 1km to see effect.",
                    "Create hex bin count for comparison; symbolise both maps.",
                    "Write 2-3 sentences describing findings and noting ONE limitation.",
                ],
            ),
            (
                "Reflection",
                [
                    "How does bandwidth choice change your map's message?",
                    "What factors besides policing might explain the patterns you see?",
                    "How would you present this map to a community group versus a police unit?",
                ],
            ),
        ],
    },
    "week06.html": {
        "title": "Week 06 – Public Health & Accessibility",
        "sections": [
            (
                "Week 06 · Public Health & Accessibility",
                "Healthcare access is a spatial problem. Today we measure who can reach services, who can't, and what that means for equity—using buffers, drive-time polygons, and vulnerability indices.",
            ),
            (
                "Why Access Matters",
                [
                    "Distance to care predicts outcomes: rural residents have higher mortality for treatable conditions.",
                    "Access isn't just distance: consider travel mode, service hours, cultural safety, affordability.",
                    "Equity lens: does everyone in the region have the same opportunity to reach care?",
                    "GIS helps quantify disparities and target interventions (new clinics, transport routes).",
                ],
            ),
            (
                "Vulnerability Indices",
                [
                    "SEIFA (Australia): Index of Relative Disadvantage. Lower score = more disadvantage.",
                    "SVI (US): CDC Social Vulnerability Index—housing, transport, demographics, disability.",
                    "ARIA+ (Australia): Accessibility/Remoteness Index. Measures distance to service centres.",
                    "Combine with facility locations to ask: are services reaching those who need them most?",
                ],
            ),
            (
                "Measuring Accessibility",
                [
                    "BUFFER: simple circle around facility (e.g., 2 km radius). Easy but ignores roads/barriers.",
                    "DRIVE-TIME POLYGON: 10-minute drive from hospital. Requires road network data.",
                    "WALK-TIME: 15-minute walk to GP clinic. Important for non-drivers, elderly.",
                    "Population overlap: count how many residents live within each catchment.",
                ],
            ),
            (
                "Network Analysis in QGIS",
                [
                    "Plugin: QNEAT3 for isochrones (areas reachable within time threshold).",
                    "Data: OpenStreetMap road network (download via QuickOSM plugin).",
                    "Workflow: set origin (clinic), travel mode (car/walk), threshold (10 mins), compute polygon.",
                    "Overlay result on population layer to estimate coverage.",
                ],
            ),
            (
                "Interpreting Gaps",
                [
                    "Map shows 'desert': areas with no clinic within 15-min drive. Who lives there?",
                    "Overlay SEIFA: are deserts in disadvantaged or advantaged areas?",
                    "Suggest interventions: mobile clinic route, new facility location, transit improvement.",
                    "Caveat: isochrone assumes average speed; real travel times vary by traffic, conditions.",
                ],
            ),
            (
                "Today's Lab: GP Clinic Access",
                [
                    "Load GP clinic locations (from OpenStreetMap or provided dataset).",
                    "Generate 10-minute drive-time polygons using QNEAT3.",
                    "Overlay SA2 population and SEIFA to identify underserved, disadvantaged areas.",
                    "Export map with clear legend showing coverage and equity classification.",
                ],
            ),
            (
                "Reflection",
                [
                    "What assumptions does your isochrone make that might not hold?",
                    "How would you validate your accessibility findings with real-world data?",
                    "What other services (pharmacies, hospitals, aged care) might benefit from this analysis?",
                ],
            ),
        ],
    },
    "week07.html": {
        "title": "Week 07 – Bridge to Python & Reproducibility",
        "sections": [
            (
                "Week 07 · Bridge to Python & Reproducibility",
                "QGIS got us here, but what if you need to run the same analysis on 100 datasets? Today we set up Python and learn why reproducibility separates good analysis from great analysis.",
            ),
            (
                "Why Move to Python?",
                [
                    "Automation: run the same workflow on new data with one command—no clicking through menus.",
                    "Reproducibility: share a script and anyone can recreate your results exactly.",
                    "Integration: combine GIS with statistics, machine learning, web dashboards.",
                    "Career value: Python + GIS skills are in demand across government, consulting, research.",
                ],
            ),
            (
                "What is Reproducibility?",
                [
                    "Goal: another person (or future you) can run your code and get the same result.",
                    "Requires: documented data sources, fixed package versions, clear code, no hard-coded paths.",
                    "Why it matters: auditing, collaboration, peer review, reusing your own work a year later.",
                ],
            ),
            (
                "Setting Up Your Environment",
                [
                    "We use Anaconda (conda) to manage Python and packages like GeoPandas, Rasterio, OSMnx.",
                    "An environment.yml file lists exactly which packages (and versions) are installed.",
                    "Everyone in the course uses the same environment = no 'works on my machine' issues.",
                    "Follow the Anaconda Setup guide before Week 8!",
                ],
            ),
            (
                "Project Structure",
                [
                    "data/raw: original downloads—never modify these.",
                    "data/processed: cleaned, reprojected, filtered outputs.",
                    "notebooks: Jupyter notebooks for analysis.",
                    "exports: maps, charts, tables for reports.",
                    "Consistent structure = easier to find files, easier to collaborate.",
                ],
            ),
            (
                "Your First Python GIS Code",
                [
                    "import geopandas as gpd",
                    "gdf = gpd.read_file('data/raw/sa2_2021.gpkg')  # Load spatial data",
                    "gdf = gdf.to_crs('EPSG:7855')  # Reproject to GDA2020/MGA Zone 55",
                    "gdf.plot()  # Quick map—looks familiar?",
                ],
            ),
            (
                "Before Next Week",
                [
                    "Complete the Anaconda Setup guide—install Anaconda, create the intro-gis environment.",
                    "Run the verification script to confirm packages installed correctly.",
                    "Launch Jupyter Lab and create a test notebook with `import geopandas`.",
                    "If you hit issues, bring them to lab—we'll troubleshoot together.",
                ],
            ),
            (
                "Reflection",
                [
                    "What repetitive QGIS task would you most like to automate?",
                    "What challenges do you anticipate learning Python?",
                    "How might reproducibility improve your current workflow?",
                ],
            ),
        ],
    },
    "week08.html": {
        "title": "Week 08 – Python Vector Workflows",
        "sections": [
            (
                "Week 08 · Python Vector Workflows",
                "GeoPandas is 'pandas for maps'—the same data manipulation you'd do in Excel or QGIS, but scripted, repeatable, and scalable. Today we automate vector analysis.",
            ),
            (
                "GeoPandas: The Core Library",
                [
                    "GeoDataFrame = DataFrame + geometry column. Think attribute table with shapes attached.",
                    "gpd.read_file() loads shapefiles, GeoPackages, GeoJSON—any vector format GDAL supports.",
                    "gdf.to_crs() reprojects, just like QGIS Layer → Set CRS but in one line of code.",
                    "gdf.to_file() exports to GeoPackage, Shapefile, etc.",
                ],
            ),
            (
                "Attribute Operations",
                [
                    "Filter: gdf[gdf['state'] == 'NSW'] — like QGIS Select by Attribute.",
                    "Create columns: gdf['density'] = gdf['pop'] / gdf['area_km2']",
                    "Aggregate: gdf.groupby('state').sum() — combine stats by category.",
                    "Merge tables: gdf.merge(csv_df, on='sa2_code') — same as QGIS join.",
                ],
            ),
            (
                "Spatial Operations",
                [
                    "BUFFER: gdf.buffer(1000) — 1 km buffer around each feature.",
                    "SPATIAL JOIN: gpd.sjoin(points, polygons, predicate='within') — which points are inside which polygons?",
                    "OVERLAY: gpd.overlay(gdf1, gdf2, how='intersection') — clip, union, difference.",
                    "DISSOLVE: gdf.dissolve(by='state') — merge polygons by attribute.",
                ],
            ),
            (
                "Quick Visualisation",
                [
                    "gdf.plot() — instant map, good for checking your work.",
                    "gdf.plot(column='population', cmap='viridis', legend=True) — choropleth.",
                    "Add basemap: import contextily; contextily.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)",
                    "For publication maps, export to QGIS or use matplotlib styling.",
                ],
            ),
            (
                "Workflow Example: Crime by LGA",
                [
                    "# Load data",
                    "lga = gpd.read_file('data/raw/lga_2021.gpkg')",
                    "crime = pd.read_csv('data/raw/crime_2023.csv')",
                    "# Join and calculate rate",
                    "lga = lga.merge(crime, on='lga_code')",
                    "lga['crime_rate'] = lga['offences'] / lga['population'] * 1000",
                    "# Export",
                    "lga.to_file('data/processed/lga_crime_rate.gpkg', driver='GPKG')",
                ],
            ),
            (
                "Today's Lab: Automate a Join",
                [
                    "Load SA2 boundaries and SEIFA CSV in Python.",
                    "Merge on SA2 code; create a percentile column using pandas.",
                    "Generate a quick choropleth; export result to GeoPackage.",
                    "Compare time spent vs doing the same in QGIS.",
                ],
            ),
            (
                "Reflection",
                [
                    "What felt faster in Python? What felt harder than QGIS?",
                    "How would you modify this script for new data next year?",
                    "What error messages did you encounter, and how did you solve them?",
                ],
            ),
        ],
    },
    "week09.html": {
        "title": "Week 09 – Raster & Remote Sensing in Python",
        "sections": [
            (
                "Week 09 · Raster & Remote Sensing in Python",
                "Satellites capture the Earth every few days. Today we use Python to process imagery, calculate vegetation indices, and detect change over time—turning pixels into insights.",
            ),
            (
                "Satellite Imagery 101",
                [
                    "Landsat 8/9: 30m resolution, 16-day revisit, free from USGS. Great for long-term studies (since 1972).",
                    "Sentinel-2: 10m resolution, 5-day revisit, free from ESA. Better detail, shorter history (since 2015).",
                    "Bands capture different wavelengths: Red, Green, Blue (what we see), NIR/SWIR (vegetation health, moisture).",
                    "Pre-processing: cloud masking, atmospheric correction. Often done for you in 'Analysis Ready Data' products.",
                ],
            ),
            (
                "Python Libraries for Raster",
                [
                    "RASTERIO: read/write GeoTIFFs, access pixel values, clip to boundaries.",
                    "RIOXARRAY: xarray + rasterio. Handles multi-band, multi-temporal data as labelled arrays.",
                    "RASTERSTATS: zonal statistics—summarise raster values within vector polygons.",
                    "These replace QGIS Processing → Raster tools, but faster and scriptable.",
                ],
            ),
            (
                "Vegetation Index: NDVI",
                [
                    "NDVI = (NIR - Red) / (NIR + Red) — measures vegetation greenness.",
                    "Values: -1 to +1. Dense vegetation ≈ 0.6–0.9. Bare soil/water ≈ 0 or negative.",
                    "Use case: before/after bushfire—healthy forest vs burnt scar.",
                    "In code: ndvi = (nir - red) / (nir + red)",
                ],
            ),
            (
                "Change Detection Workflow",
                [
                    "1. Download pre-event and post-event imagery (same sensor, similar season).",
                    "2. Calculate NDVI for both dates.",
                    "3. Compute difference: ndvi_change = ndvi_post - ndvi_pre",
                    "4. Threshold: areas with change < -0.2 likely lost vegetation.",
                    "5. Summarise per SA2: average change, % area affected.",
                ],
            ),
            (
                "Zonal Statistics",
                [
                    "from rasterstats import zonal_stats",
                    "stats = zonal_stats(sa2_gdf, ndvi_raster, stats=['mean', 'min', 'max'])",
                    "Output: list of dicts with stats for each polygon. Join back to GeoDataFrame.",
                    "Export: gdf.to_file('ndvi_by_sa2.gpkg')",
                ],
            ),
            (
                "Today's Lab: Bushfire Impact",
                [
                    "Load pre- and post-fire Landsat imagery for a study region.",
                    "Calculate NDVI for both dates; compute difference raster.",
                    "Threshold to classify 'severe burn' vs 'moderate' vs 'unaffected'.",
                    "Run zonal stats to report mean NDVI change per LGA.",
                ],
            ),
            (
                "Reflection",
                [
                    "What challenges did you face aligning images from different dates?",
                    "How might cloud cover or seasonality affect your results?",
                    "What other applications (urban growth, drought, flooding) could use this workflow?",
                ],
            ),
        ],
    },
    "week10.html": {
        "title": "Week 10 – Transport Networks & Accessibility",
        "sections": [
            (
                "Week 10 · Transport Networks & Accessibility",
                "Cities are networks: roads, rail, walking paths. Today we model these networks in Python to answer: Who can reach what, how quickly, and who is left behind?",
            ),
            (
                "Networks as Graphs",
                [
                    "NODES: intersections, transit stops, points of interest.",
                    "EDGES: road segments, rail lines, footpaths. Each has length, speed limit, travel time.",
                    "DIRECTED: one-way streets matter for driving; walking is usually undirected.",
                    "GIS + graph theory = powerful accessibility analysis.",
                ],
            ),
            (
                "OSMnx: OpenStreetMap + NetworkX",
                [
                    "OSMnx downloads street networks from OpenStreetMap and converts them to NetworkX graphs.",
                    "import osmnx as ox",
                    "G = ox.graph_from_place('Sydney, Australia', network_type='walk')  # or 'drive', 'bike'",
                    "ox.plot_graph(G)  # instant network visualisation",
                ],
            ),
            (
                "Isochrones: Travel-Time Polygons",
                [
                    "Isochrone = area reachable within a time threshold from a point.",
                    "Example: where can you walk in 15 minutes from Central Station?",
                    "OSMnx: subgraph = ox.truncate.truncate_graph_dist(G, source_node, dist=1200)  # 1.2 km",
                    "Convert node hull to polygon for mapping.",
                ],
            ),
            (
                "Measuring Access",
                [
                    "Count population within each isochrone: who can reach the hospital in 10, 20, 30 minutes?",
                    "Compare across demographics: do disadvantaged areas have worse access?",
                    "Service area analysis: if we add a new bus stop here, how many more people are covered?",
                ],
            ),
            (
                "Network Centrality",
                [
                    "BETWEENNESS: how often does this road appear on shortest paths? High = critical link.",
                    "CLOSENESS: how close is this node to all others? Identifies well-connected locations.",
                    "Use case: if this bridge closes, which routes are affected? Which intersections need traffic lights?",
                ],
            ),
            (
                "Today's Lab: Walk-Time Isochrones",
                [
                    "Download walking network for your study area using OSMnx.",
                    "Generate 5, 10, 15-minute isochrones from a hospital or transit station.",
                    "Overlay SA1 population data to estimate people within each band.",
                    "Export isochrones to GeoPackage for mapping in QGIS.",
                ],
            ),
            (
                "Reflection",
                [
                    "What surprised you about the walkable area around your chosen point?",
                    "How accurate are OSM speed assumptions? What would you change?",
                    "How could transit planners use these isochrones to improve equity?",
                ],
            ),
        ],
    },
    "week11.html": {
        "title": "Week 11 – Design & Storytelling Studio",
        "sections": [
            (
                "Week 11 · Design & Storytelling Studio",
                "You've done the analysis. Now make it land. Today is about refining your maps into visual stories that inform, persuade, and inspire action.",
            ),
            (
                "From Analysis to Story",
                [
                    "Every map should answer: So what? Why does this matter?",
                    "Structure: HOOK (grab attention) → CONTEXT (background) → INSIGHT (finding) → ACTION (what now?).",
                    "Example: 'Three suburbs have no GP clinic within 15 minutes—here's where a new clinic would help most.'",
                    "Remove anything that doesn't serve the story. Simplify ruthlessly.",
                ],
            ),
            (
                "Visual Hierarchy",
                [
                    "Reader's eye follows: largest → brightest → most detailed.",
                    "Title should be prominent; data source can be small.",
                    "Main map = focus. Insets, legends, scale = supporting cast.",
                    "Use whitespace to separate elements and reduce clutter.",
                ],
            ),
            (
                "Typography & Colour Consistency",
                [
                    "Max 2 font families: one for titles, one for body/labels.",
                    "Consistent sizing: establish a scale (e.g., 24pt title, 12pt labels, 9pt sources).",
                    "Reuse your colour palette from earlier maps. Brand consistency builds trust.",
                    "Avoid all-caps except for very short labels (N, S, E, W).",
                ],
            ),
            (
                "Accessibility Review",
                [
                    "Colour contrast ≥ 4.5:1 for all text. Use WebAIM Contrast Checker.",
                    "Colour alone shouldn't carry meaning—add patterns, icons, or labels.",
                    "Minimum 9pt text for print; 12pt for screen display.",
                    "Prepare alt text: 'Choropleth map showing crime rate per LGA in NSW, with darkest shading in inner Sydney.'",
                ],
            ),
            (
                "Peer Critique Protocol",
                [
                    "1. CLARITY: Can you understand the map's message in 10 seconds?",
                    "2. ACCURACY: Are data represented fairly? Any misleading choices?",
                    "3. AESTHETICS: Is it visually balanced? Professional?",
                    "4. ACCESSIBILITY: Would it work for colourblind viewers? Small screens?",
                    "Give specific, actionable feedback: 'The legend is hard to read—try larger font.'",
                ],
            ),
            (
                "Today's Studio",
                [
                    "Bring your draft capstone map (or best map from earlier weeks).",
                    "Present in 2 minutes: What question? What finding? What action?",
                    "Receive feedback from 2 peers using the critique protocol.",
                    "Note 3 specific improvements to implement before Week 12.",
                ],
            ),
            (
                "Reflection",
                [
                    "What feedback surprised you most?",
                    "Which design principle will you prioritise in your revision?",
                    "How has your understanding of 'good' cartography evolved?",
                ],
            ),
        ],
    },
    "week12.html": {
        "title": "Week 12 – Capstone Showcase",
        "sections": [
            (
                "Week 12 · Capstone Showcase & Reflection",
                "Twelve weeks of learning, culminating in your own spatial story. Today you present, reflect, and celebrate—then look ahead to where GIS takes you next.",
            ),
            (
                "Capstone Deliverables",
                [
                    "PROBLEM: What spatial question did you investigate? Why does it matter?",
                    "DATA: What sources did you use? How did you clean/process them?",
                    "ANALYSIS: What methods did you apply (joins, overlays, KDE, network)?",
                    "FINDINGS: What did you discover? Show it in a polished map or dashboard.",
                    "REFLECTION: What worked, what didn't, what would you do differently?",
                ],
            ),
            (
                "Presentation Format",
                [
                    "5 minutes per project (strict—practice your timing).",
                    "Structure: 30 sec problem, 1 min data/methods, 2 min findings/map, 1 min reflection.",
                    "Lead with the insight: 'We found that...' not 'First we downloaded...'.",
                    "Anticipate questions: data limitations, alternative interpretations.",
                ],
            ),
            (
                "Peer Feedback",
                [
                    "CLARITY: Could you understand the story without prior context?",
                    "EVIDENCE: Were methods transparent and reproducible?",
                    "DESIGN: Did the map effectively communicate the finding?",
                    "IMPACT: What decision or action could this analysis support?",
                    "Frame feedback constructively: 'This was strong because... This could improve by...'",
                ],
            ),
            (
                "Course Reflection",
                [
                    "Which skill surprised you with its usefulness?",
                    "What concept still feels challenging?",
                    "How has your view of 'data' or 'maps' changed?",
                    "What would you tell a student starting this course?",
                ],
            ),
            (
                "What's Next?",
                [
                    "SHARE: Publish your project on GitHub, LinkedIn, or a personal portfolio.",
                    "DEEPEN: Take advanced courses in remote sensing, spatial statistics, or web mapping.",
                    "APPLY: Use these skills in research, work, or community projects.",
                    "CONNECT: Join QGIS user groups, GIS subreddits, local meetups.",
                ],
            ),
            (
                "Today's Showcase",
                [
                    "Present your capstone project to the class.",
                    "Give constructive feedback to at least 2 peers.",
                    "Submit final project files and reflection to course portal.",
                    "Celebrate 12 weeks of growth!",
                ],
            ),
            (
                "Thank You",
                [
                    "You've learned to ask spatial questions, find and clean data, analyse patterns, and communicate findings.",
                    "That's a powerful skillset—applicable across planning, health, environment, justice, and more.",
                    "Keep mapping. Keep questioning. Keep learning.",
                    "Good luck on your spatial journey!",
                ],
            ),
        ],
    },
}


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{title} - Introduction to GIS Course">
  <meta name="author" content="Intro to GIS">
  <title>{title}</title>
  <style>
    /* ========== FONTS & RESET ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Fira+Code&display=swap');

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    /* ========== ROOT VARIABLES ========== */
    :root {{
      --primary: #00897b;        /* Teal - main brand color */
      --primary-dark: #00695c;   /* Dark teal */
      --primary-light: #4db6ac;  /* Light teal */
      --secondary: #0277bd;      /* Blue */
      --accent: #ff6f00;         /* Orange accent */
      --bg-main: #ffffff;
      --bg-alt: #f5f7fa;
      --text-primary: #1a202c;
      --text-secondary: #4a5568;
      --text-light: #718096;
      --border: #cbd5e0;
      --shadow: rgba(0, 0, 0, 0.1);
      --shadow-lg: rgba(0, 0, 0, 0.15);
    }}

    /* ========== BASE STYLES ========== */
    html {{
      font-size: 16px;
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      line-height: 1.6;
      color: var(--text-primary);
      background: var(--bg-alt);
      overflow-x: hidden;
    }}

    /* ========== SLIDE CONTAINER ========== */
    #slides-container {{
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }}

    /* ========== INDIVIDUAL SLIDES ========== */
    .slide {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 4rem 6rem;
      background: var(--bg-main);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.4s ease, visibility 0.4s ease;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow-y: auto;
    }}

    .slide.active {{
      opacity: 1;
      visibility: visible;
      z-index: 1;
    }}

    /* Title slide styling with topographic contour pattern */
    .slide.title-slide {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      color: white;
      text-align: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }}

    /* Topographic contour pattern overlay */
    .slide.title-slide::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      opacity: 0.12;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 600'%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 300 Q100 200 200 280 T400 260 T600 300 T850 280'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 350 Q150 280 250 340 T450 320 T650 360 T850 340'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 400 Q120 340 220 390 T420 370 T620 410 T850 390'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 250 Q80 180 180 230 T380 210 T580 250 T850 230'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 200 Q100 140 200 180 T400 160 T600 200 T850 180'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 150 Q120 100 220 130 T420 110 T620 150 T850 130'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 450 Q130 400 230 440 T430 420 T630 460 T850 440'/%3E%3Cpath fill='none' stroke='white' stroke-width='1.5' d='M-50 500 Q140 460 240 490 T440 470 T640 510 T850 490'/%3E%3Cellipse cx='400' cy='300' rx='150' ry='80' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='400' cy='300' rx='100' ry='50' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='400' cy='300' rx='50' ry='25' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='600' cy='450' rx='120' ry='60' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='600' cy='450' rx='70' ry='35' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='200' cy='180' rx='100' ry='50' fill='none' stroke='white' stroke-width='1.5'/%3E%3Cellipse cx='200' cy='180' rx='50' ry='25' fill='none' stroke='white' stroke-width='1.5'/%3E%3C/svg%3E");
      background-size: cover;
      background-position: center;
      pointer-events: none;
    }}

    .slide.title-slide h1 {{
      font-size: 3.5rem;
      font-weight: 700;
      margin-bottom: 1.5rem;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
      line-height: 1.2;
    }}

    .slide.title-slide p {{
      font-size: 1.4rem;
      opacity: 0.95;
      max-width: 800px;
      margin: 0 auto;
      font-weight: 400;
    }}

    /* Table of Contents slide */
    .slide.toc-slide {{
      background: var(--bg-alt);
    }}

    .slide.toc-slide h2 {{
      color: var(--primary);
      border-bottom: 3px solid var(--primary);
      padding-bottom: 0.5rem;
      margin-bottom: 2rem;
    }}

    .slide.toc-slide ol {{
      list-style: none;
      counter-reset: toc-counter;
      max-width: 900px;
    }}

    .slide.toc-slide li {{
      counter-increment: toc-counter;
      padding: 0.8rem 0;
      padding-left: 3rem;
      position: relative;
      font-size: 1.1rem;
      border-bottom: 1px solid var(--border);
    }}

    .slide.toc-slide li:before {{
      content: counter(toc-counter);
      position: absolute;
      left: 0;
      top: 0.8rem;
      width: 2rem;
      height: 2rem;
      background: var(--primary);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 600;
      font-size: 0.9rem;
    }}

    /* Content slides */
    .slide.content-slide h2 {{
      font-size: 2.5rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 2rem;
      padding-bottom: 0.75rem;
      border-bottom: 3px solid var(--primary-light);
    }}

    .slide.content-slide ul {{
      list-style: none;
      padding-left: 0;
      max-width: 1000px;
    }}

    .slide.content-slide li {{
      padding: 0.75rem 0 0.75rem 2.5rem;
      position: relative;
      font-size: 1.15rem;
      line-height: 1.7;
      color: var(--text-secondary);
    }}

    .slide.content-slide li:before {{
      content: '▸';
      position: absolute;
      left: 0.5rem;
      color: var(--primary);
      font-size: 1.3rem;
      font-weight: bold;
    }}

    /* ========== NAVIGATION CONTROLS ========== */
    #nav-controls {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      display: flex;
      gap: 1rem;
      z-index: 1000;
    }}

    .nav-btn {{
      width: 3rem;
      height: 3rem;
      border: none;
      background: var(--primary);
      color: white;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      transition: all 0.3s ease;
      box-shadow: 0 4px 6px var(--shadow);
    }}

    .nav-btn:hover {{
      background: var(--primary-dark);
      transform: translateY(-2px);
      box-shadow: 0 6px 12px var(--shadow-lg);
    }}

    .nav-btn:active {{
      transform: translateY(0);
    }}

    .nav-btn:disabled {{
      background: var(--border);
      cursor: not-allowed;
      opacity: 0.5;
      transform: none;
    }}

    /* ========== SLIDE COUNTER ========== */
    #slide-counter {{
      position: fixed;
      bottom: 2rem;
      left: 2rem;
      background: var(--primary);
      color: white;
      padding: 0.75rem 1.5rem;
      border-radius: 2rem;
      font-weight: 600;
      font-size: 1rem;
      box-shadow: 0 4px 6px var(--shadow);
      z-index: 1000;
    }}

    /* ========== FOOTER ========== */
    .slide-footer {{
      position: absolute;
      bottom: 1.5rem;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.85rem;
      color: var(--text-light);
      text-align: center;
    }}

    .title-slide .slide-footer {{
      color: rgba(255, 255, 255, 0.8);
    }}

    /* ========== KEYBOARD HINT ========== */
    #keyboard-hint {{
      position: fixed;
      top: 2rem;
      right: 2rem;
      background: var(--bg-alt);
      padding: 0.75rem 1.25rem;
      border-radius: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-secondary);
      border: 1px solid var(--border);
      opacity: 0;
      transition: opacity 0.3s ease;
      z-index: 1000;
    }}

    #keyboard-hint.show {{
      opacity: 1;
    }}

    #keyboard-hint kbd {{
      background: white;
      padding: 0.2rem 0.5rem;
      border-radius: 0.25rem;
      border: 1px solid var(--border);
      font-family: 'Fira Code', monospace;
      font-size: 0.8rem;
    }}

    /* ========== RESPONSIVE DESIGN ========== */
    @media (max-width: 1200px) {{
      .slide {{
        padding: 3rem 4rem;
      }}

      .slide.title-slide h1 {{
        font-size: 3rem;
      }}

      .slide.content-slide h2 {{
        font-size: 2.2rem;
      }}
    }}

    @media (max-width: 768px) {{
      .slide {{
        padding: 2rem;
      }}

      .slide.title-slide h1 {{
        font-size: 2rem;
      }}

      .slide.title-slide p {{
        font-size: 1.1rem;
      }}

      .slide.content-slide h2 {{
        font-size: 1.8rem;
      }}

      .slide.content-slide li {{
        font-size: 1rem;
        padding-left: 2rem;
      }}

      #nav-controls {{
        bottom: 1rem;
        right: 1rem;
        gap: 0.5rem;
      }}

      .nav-btn {{
        width: 2.5rem;
        height: 2.5rem;
        font-size: 1rem;
      }}

      #slide-counter {{
        bottom: 1rem;
        left: 1rem;
        padding: 0.5rem 1rem;
        font-size: 0.9rem;
      }}

      #keyboard-hint {{
        display: none;
      }}
    }}

    /* ========== PRINT STYLES ========== */
    @media print {{
      body {{
        background: white;
      }}

      #slides-container {{
        height: auto;
        overflow: visible;
      }}

      .slide {{
        position: relative;
        opacity: 1 !important;
        visibility: visible !important;
        page-break-after: always;
        height: auto;
        min-height: 100vh;
        padding: 2cm;
      }}

      .slide.active {{
        page-break-after: always;
      }}

      #nav-controls,
      #slide-counter,
      #keyboard-hint {{
        display: none !important;
      }}

      .slide.title-slide {{
        background: var(--primary) !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}

      .slide-footer {{
        position: absolute;
        bottom: 1cm;
      }}
    }}
  </style>
</head>
<body>
  <div id="slides-container">
{body}
  </div>

  <div id="slide-counter">
    <span id="current-slide">1</span> / <span id="total-slides">0</span>
  </div>

  <div id="nav-controls">
    <button id="prev-btn" class="nav-btn" aria-label="Previous slide" title="Previous (←)">←</button>
    <button id="next-btn" class="nav-btn" aria-label="Next slide" title="Next (→)">→</button>
  </div>

  <div id="keyboard-hint">
    Use <kbd>←</kbd> <kbd>→</kbd> <kbd>Space</kbd> to navigate | <kbd>Home</kbd> <kbd>End</kbd> to jump
  </div>

  <script>
    // Slide navigation system
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const currentSlideSpan = document.getElementById('current-slide');
    const totalSlidesSpan = document.getElementById('total-slides');
    const keyboardHint = document.getElementById('keyboard-hint');

    // Initialize
    totalSlidesSpan.textContent = totalSlides;
    showSlide(0);

    // Show keyboard hint briefly on load
    setTimeout(() => {{
      keyboardHint.classList.add('show');
      setTimeout(() => keyboardHint.classList.remove('show'), 3000);
    }}, 500);

    function showSlide(index) {{
      // Bounds checking
      if (index < 0) index = 0;
      if (index >= totalSlides) index = totalSlides - 1;

      // Update active slide
      slides.forEach((slide, i) => {{
        slide.classList.toggle('active', i === index);
      }});

      currentSlide = index;
      currentSlideSpan.textContent = index + 1;

      // Update button states
      prevBtn.disabled = index === 0;
      nextBtn.disabled = index === totalSlides - 1;

      // Update URL hash without scrolling
      history.replaceState(null, null, `#slide-${{index + 1}}`);
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides - 1) {{
        showSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 0) {{
        showSlide(currentSlide - 1);
      }}
    }}

    function firstSlide() {{
      showSlide(0);
    }}

    function lastSlide() {{
      showSlide(totalSlides - 1);
    }}

    // Event listeners
    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      switch(e.key) {{
        case 'ArrowRight':
        case ' ':
        case 'PageDown':
          e.preventDefault();
          nextSlide();
          break;
        case 'ArrowLeft':
        case 'PageUp':
          e.preventDefault();
          prevSlide();
          break;
        case 'Home':
          e.preventDefault();
          firstSlide();
          break;
        case 'End':
          e.preventDefault();
          lastSlide();
          break;
      }}
    }});

    // Touch/swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', (e) => {{
      touchStartX = e.changedTouches[0].screenX;
    }}, false);

    document.addEventListener('touchend', (e) => {{
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }}, false);

    function handleSwipe() {{
      const swipeThreshold = 50;
      if (touchEndX < touchStartX - swipeThreshold) {{
        nextSlide();
      }}
      if (touchEndX > touchStartX + swipeThreshold) {{
        prevSlide();
      }}
    }}

    // Handle initial hash navigation
    window.addEventListener('load', () => {{
      const hash = window.location.hash;
      if (hash) {{
        const match = hash.match(/slide-(\\d+)/);
        if (match) {{
          const slideNum = parseInt(match[1]) - 1;
          if (slideNum >= 0 && slideNum < totalSlides) {{
            showSlide(slideNum);
          }}
        }}
      }}
    }});
  </script>
</body>
</html>
"""


def render_title_slide(title: str, description: str, week_num: str, footer: str) -> str:
    """
    Render the title slide for a presentation.

    Args:
        title: The main title of the presentation
        description: Subtitle or description text
        week_num: Week identifier (e.g., "Week 01")
        footer: Footer text with copyright info

    Returns:
        HTML string for the title slide
    """
    return f"""    <div class="slide title-slide active" role="region" aria-label="Title slide">
      <h1>{title}</h1>
      <p>{description}</p>
      <div class="slide-footer">{footer}</div>
    </div>
"""


def render_toc_slide(sections: List[Tuple[str, Union[str, List[str]]]], footer: str) -> str:
    """
    Render a table of contents slide.

    Args:
        sections: List of section tuples (heading, content)
        footer: Footer text with copyright info

    Returns:
        HTML string for the ToC slide
    """
    # Skip the first section (title) when creating ToC
    toc_items = []
    for heading, _ in sections[1:]:
        toc_items.append(f"        <li>{heading}</li>")

    toc_html = "\n".join(toc_items)

    return f"""    <div class="slide toc-slide" role="region" aria-label="Table of contents">
      <h2>Overview</h2>
      <ol>
{toc_html}
      </ol>
      <div class="slide-footer">{footer}</div>
    </div>
"""


def render_content_slide(heading: str, content: Union[str, List[str]], footer: str) -> str:
    """
    Render a content slide with heading and bullet points or text.

    Args:
        heading: The slide heading
        content: Either a string (for subtitle slides) or list of bullet points
        footer: Footer text with copyright info

    Returns:
        HTML string for the content slide
    """
    if isinstance(content, list):
        items = "\n".join(f"        <li>{item}</li>" for item in content)
        body = f"""      <h2>{heading}</h2>
      <ul>
{items}
      </ul>"""
    else:
        # Subtitle/description slide (typically the first slide after title)
        body = f"""      <h2>{heading}</h2>
      <p style="font-size: 1.3rem; color: var(--text-secondary); max-width: 900px; line-height: 1.8;">{content}</p>"""

    return f"""    <div class="slide content-slide" role="region" aria-label="{heading}">
{body}
      <div class="slide-footer">{footer}</div>
    </div>
"""


def extract_week_number(filename: str) -> str:
    """
    Extract week number from filename.

    Args:
        filename: Filename like "week01.html"

    Returns:
        Formatted week string like "Week 01"
    """
    week_num = filename.replace("week", "").replace(".html", "")
    return f"Week {week_num}"


def generate_slide_deck(filename: str, slide_data: Dict[str, Union[str, List[Tuple[str, Union[str, List[str]]]]]]) -> str:
    """
    Generate a complete HTML slide deck.

    Args:
        filename: Output filename (e.g., "week01.html")
        slide_data: Dictionary containing 'title' and 'sections'

    Returns:
        Complete HTML document as a string
    """
    title = slide_data["title"]
    sections = slide_data["sections"]
    week_num = extract_week_number(filename)
    footer = f"{week_num} | Intro to GIS | © 2025"

    # First section is always the title/intro
    title_heading, title_desc = sections[0]

    # Build all slides
    slides_html = []
    slides_html.append(render_title_slide(title_heading, title_desc, week_num, footer))
    slides_html.append(render_toc_slide(sections, footer))

    # Render remaining content slides
    for heading, content in sections[1:]:
        slides_html.append(render_content_slide(heading, content, footer))

    body = "\n".join(slides_html)
    return HTML_TEMPLATE.format(title=title, body=body)


def main() -> None:
    """
    Main function to generate all slide decks.

    Iterates through the SLIDES dictionary and generates an HTML file
    for each week's presentation. Outputs to site_docs/slides/ for MkDocs hosting.
    """
    # Output to site_docs/slides/ for MkDocs to serve
    repo_root = Path(__file__).parent.parent.parent
    slide_dir = repo_root / "site_docs" / "slides"
    slide_dir.mkdir(parents=True, exist_ok=True)

    for filename, slide_data in SLIDES.items():
        html = generate_slide_deck(filename, slide_data)
        output_path = slide_dir / filename
        output_path.write_text(html, encoding="utf-8")
        print(f"  ✓ Generated {filename}")

    print(f"\nSuccessfully generated {len(SLIDES)} slide decks in {slide_dir}")


if __name__ == "__main__":
    main()
