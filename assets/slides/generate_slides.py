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
                "Introduce GIS as the blend of location and attribute data, emphasising spatial thinking and how the course will move from QGIS hands-on work to scripted automation.",
            ),
            (
                "What is GIS?",
                [
                    "Integration of spatial data (location) with attribute data (what/who/when).",
                    "Enables analysis, visualisation, and decision-making rooted in geography.",
                    "Combines software, hardware, data, people, and workflows.",
                    "Use cases: transport planning, emergency response, environmental monitoring, public health.",
                    "GIS is more than software—it's a process for asking and answering 'where' questions.",
                ],
            ),
            (
                "Spatial vs Tabular Thinking",
                [
                    "Traditional tables list records; spatial thinking reveals patterns when mapped.",
                    "Questions shift with scale: global vs regional vs local decisions.",
                    "Key spatial relationships: proximity, adjacency, containment, connectivity.",
                    "Embrace context: the same metric can tell a new story when mapped.",
                    "Spatial thinking encourages learners to consider neighbours, networks, and geographic context alongside raw counts.",
                ],
            ),
            (
                "Data Models",
                [
                    "Vector: point (bus stop), line (river), polygon (LGA) with attribute tables.",
                    "Raster: grid of pixels (imagery, elevation, density) storing continuous values.",
                    "Choose the model that matches the phenomenon and question.",
                    "Bridge to Week 02 reading on spatial data models.",
                    "Highlight common vector formats (Shapefile, GeoPackage, GeoJSON) and raster formats (GeoTIFF).",
                ],
            ),
            (
                "Metadata Essentials",
                [
                    "Coordinate Reference System (CRS) — ensures layers align correctly.",
                    "Extent and resolution define the spatial coverage and detail.",
                    "Vintage (time) and licensing impact suitability for analysis.",
                    "QGIS layer properties expose metadata — check before analysis.",
                    "Demonstrate mismatched CRS causing misaligned layers and how to fix with `Set Project CRS`.",
                ],
            ),
            (
                "Starter GIS Workflow",
                [
                    "Acquire data → Inspect metadata → Clean/format → Analyse → Communicate.",
                    "Week 01 lab: set up project workspace, explore Natural Earth datasets, export a quick map.",
                    "Goal: build comfort with the QGIS interface, not perfection.",
                    "Encourage note-taking on data sources, transformations, and export locations to support reproducibility.",
                ],
            ),
            (
                "QGIS Interface Tour",
                [
                    "Browser panel loads local folders and online services; drag layers directly into the map.",
                    "Layers panel controls draw order, visibility, and styling for each dataset.",
                    "Processing Toolbox exposes hundreds of analysis tools—flag this for future weeks.",
                    "Identify tool and Attribute Table demonstrate the link between geometry and attributes.",
                ],
            ),
            (
                "Hands-on Lab Preview",
                [
                    "Create project in `projects/week01_orientation.qgz` with relative paths enabled.",
                    "Add Natural Earth Admin-0 countries; inspect fields such as `NAME`, `POP_EST`, `CONTINENT`.",
                    "Apply categorical symbology by continent, then graduated by population.",
                    "Open Print Layout, add title/legend/scale, export PNG to `exports/week01_quickmap.png`.",
                ],
            ),
            (
                "Discussion & Reflection",
                [
                    "Where have you encountered GIS outputs in everyday life?",
                    "What problems in your domain could benefit from spatial context?",
                    "List one skill you hope to gain from the course.",
                    "How will organising your workspace now make later automation (Week 8+) easier?",
                ],
            ),
            (
                "Next steps & Prep",
                [
                    "Complete Week 01 reflection prompt; note installation or interface questions.",
                    "Ensure renewable energy and world cities datasets are downloaded for Week 02.",
                    "Optional: explore `Help ▶ Keyboard Shortcuts Reference` to speed up navigation.",
                ],
            ),
        ],
    },
    "week02.html": {
        "title": "Week 02 – Symbology, Labelling & Layouts",
        "sections": [
            (
                "Week 02 · Symbology, Labelling & Layouts",
                "Teach learners how to communicate data effectively through cartographic conventions, colour choices, and layout design.",
            ),
            (
                "Map Purpose & Audience",
                [
                    "Clarify the story: comparison, pattern discovery, or persuasion.",
                    "Audience drives level of detail and terminology.",
                    "Every map needs title, legend, source, scale (when relevant), and credits.",
                ],
            ),
            (
                "Symbology Fundamentals",
                [
                    "Match data type to symbology: sequential, diverging, or qualitative scale.",
                    "Limit to 5–7 classes; use intuitive ordering.",
                    "Avoid misleading classifications—experiment with quantile vs natural breaks.",
                    "Use transparency, outlines, and blending to manage overlapping features.",
                ],
            ),
            (
                "Colour & Accessibility",
                [
                    "Colour has cultural connotations—choose palettes intentionally.",
                    "Check contrast ratios (≥ 4.5:1) for text and key map elements.",
                    "Use colour-blind safe palettes (e.g., ColorBrewer).",
                    "Support readability with patterns or redundant encoding when possible.",
                ],
            ),
            (
                "Labelling Principles",
                [
                    "Keep labels concise; avoid duplication in legend and map.",
                    "Use data-driven styling for font size, placement, and visibility by scale.",
                    "Declutter: remove unnecessary labels or leverage inset maps.",
                ],
            ),
            (
                "Layout Design",
                [
                    "Establish visual hierarchy using size, colour, and spacing.",
                    "Use a grid to align map frame, legend, title, and supplemental graphics.",
                    "Balance white space and content to guide the reader’s eye.",
                    "Include narrative elements (subtitle, callouts) to provide context.",
                ],
            ),
            (
                "Workshop Flow",
                [
                    "Review example maps (good & poor) and critique with the class.",
                    "Style renewable energy data in QGIS with graduated symbology.",
                    "Label major world cities using expression-based rules.",
                    "Export a layout and discuss accessibility checklist outcomes.",
                ],
            ),
            (
                "Reflection Prompts",
                [
                    "Which design decision most improved your map?",
                    "How will you communicate data provenance and uncertainty?",
                    "What element will you iterate on before Week 3?",
                ],
            ),
        ],
    },
    "week03.html": {
        "title": "Week 03 – Vector Analysis & Attribute Joins",
        "sections": [
            (
                "Week 03 · Vector Analysis & Attribute Joins",
                "Explore administrative/statistical boundaries, join tabular data, and prepare for socio-economic mapping.",
            ),
            (
                "Boundary Ecosystem",
                [
                    "Administrative vs statistical boundaries (ADM0–ADM2, SA2, LGA).",
                    "Stewardship: ABS, census bureaus, local councils; update cycles.",
                    "Boundary purpose dictates appropriate use (governance, service delivery, statistics).",
                ],
            ),
            (
                "Boundary Change Implications",
                [
                    "Releases (e.g., ASGS 2016 vs 2021) add splits/merges — impacts longitudinal analysis.",
                    "Use correspondence files or area-weighted interpolation to align vintages.",
                    "Document the version used in metadata and map footers.",
                ],
            ),
            (
                "Join Fundamentals",
                [
                    "Unique keys must match in datatype and formatting (pad FIPS codes, trim whitespace).",
                    "Inspect attribute tables before joining; validate record counts afterwards.",
                    "Keep original columns, add derived metrics, and note assumptions.",
                ],
            ),
            (
                "Practical Workflow",
                [
                    "Load SA2 shapefile + SEIFA table (or local equivalents).",
                    "Join on SA2 code, check for nulls/mismatches.",
                    "Create decile/percentile metrics via Field Calculator.",
                    "Filter to region of interest before visualisation.",
                ],
            ),
            (
                "Storytelling Considerations",
                [
                    "Explain why you chose a specific boundary (SA2 vs LGA vs postcode).",
                    "Clarify limitations: boundary changes, disclosure control, missing data.",
                    "Pair quantitative outputs with qualitative context from local knowledge.",
                ],
            ),
            (
                "Reflection Prompts",
                [
                    "Which join challenges did you face and how did you resolve them?",
                    "How do boundary choices influence the narrative of your map?",
                    "What additional data would enrich the socio-economic story?",
                ],
            ),
        ],
    },
    "week04.html": {
        "title": "Week 04 – Raster & Terrain Analysis",
        "sections": [
            (
                "Week 04 · Raster & Terrain Analysis",
                "Introduce DEMs, derived surfaces, and how to integrate raster insights with boundary data.",
            ),
            (
                "DEM Fundamentals",
                [
                    "Digital Elevation Models (DEM) vs Digital Surface Models (DSM) vs DTMs.",
                    "Resolution & accuracy considerations (ELVIS 1\" vs SRTM 30m).",
                    "Importance of CRS for distance/area calculations (project to metres).",
                ],
            ),
            (
                "Data Sources",
                [
                    "Australia: ELVIS portal (Geoscience Australia), state LiDAR datasets.",
                    "Global: SRTM, NASADEM, ASTER GDEM (consider licensing & preprocessing).",
                    "Metadata to capture: tile names, acquisition date, vertical datum.",
                ],
            ),
            (
                "Derived Products",
                [
                    "Hillshade for visual relief, slope/aspect for analysis.",
                    "Contours for cartographic representation.",
                    "Zonal statistics to summarise raster values within polygons.",
                    "Clip to area of interest before heavy processing.",
                ],
            ),
            (
                "Workflow in QGIS",
                [
                    "Load DEM tile, check CRS, reproject if required.",
                    "Use Clip Raster by Mask Layer (SA2/LGA boundary) to focus analysis.",
                    "Generate hillshade and slope; style with grayscale ramp and colour ramp.",
                    "Overlay boundary data to identify vulnerable areas.",
                ],
            ),
            (
                "Applications & Storytelling",
                [
                    "Flood risk assessment, infrastructure planning, habitat suitability.",
                    "Combine with socio-economic layers for resilience narratives.",
                    "Communicate uncertainty (resolution limits, interpolation errors).",
                ],
            ),
            (
                "Reflection",
                [
                    "What terrain insight surprised you the most?",
                    "How does resolution influence the trustworthiness of your map?",
                    "Which datasets would you add to tell a more complete story?",
                ],
            ),
        ],
    },
    "week05.html": {
        "title": "Week 05 – Crime Hotspots & Storytelling",
        "sections": [
            (
                "Week 05 · Crime Hotspots & Storytelling",
                "Introduce spatial crime analysis techniques and emphasise responsible communication.",
            ),
            (
                "Ethics & Context",
                [
                    "Crime data reflects reporting practices and policing focus.",
                    "Communicate uncertainty and avoid reinforcing stereotypes.",
                    "Respect privacy: aggregate to appropriate boundary level, anonymise where required.",
                ],
            ),
            (
                "Data Preparation",
                [
                    "Filter offences by time period and category relevant to the question.",
                    "Convert CSV to GeoPackage for efficient spatial analysis.",
                    "Join to boundaries (LGA, SA2, police districts) to provide context.",
                ],
            ),
            (
                "Hotspot Techniques",
                [
                    "Kernel Density Estimation (KDE) — bandwidth selection influences output.",
                    "Hex binning or fishnet grids for aggregated counts.",
                    "Time-enabled maps to compare periods (e.g., year-on-year trend).",
                ],
            ),
            (
                "Narrative & Delivery",
                [
                    "Frame results alongside community assets (lighting projects, youth programs).",
                    "Include callouts on data limitations, under-reporting, and socio-economic factors.",
                    "Consider stakeholder needs (police, community groups, policy makers).",
                ],
            ),
            (
                "Action Items",
                [
                    "Develop lab instructions with step-by-step KDE setup in QGIS.",
                    "Prepare screenshots illustrating parameter choices and outputs.",
                    "Create reflection prompts focusing on ethical storytelling.",
                ],
            ),
        ],
    },
    "week06.html": {
        "title": "Week 06 – Public Health & Accessibility",
        "sections": [
            (
                "Week 06 · Public Health & Accessibility",
                "Analyse health service accessibility and equity by combining facilities, networks, and vulnerability indices.",
            ),
            (
                "Health Equity Framing",
                [
                    "Social determinants: income, transport, demographics influence health outcomes.",
                    "Access is multidimensional (distance, travel time, service capacity).",
                    "Data gaps: facility opening hours, service offerings, community preferences.",
                ],
            ),
            (
                "Data Inputs",
                [
                    "Vulnerability indicators (SEIFA, ARIA+, SVI).",
                    "Health service locations (National Health Services Directory, HRSA site data).",
                    "Road or transit networks (OpenStreetMap extracts, GTFS).",
                ],
            ),
            (
                "Accessibility Techniques",
                [
                    "Simple buffers and drive-time polygons to approximate catchments.",
                    "Network analysis plugins (QNEAT3, Iso-Area) for walk/drive times.",
                    "Two-step floating catchment methods for supply-demand balance (optional extension).",
                ],
            ),
            (
                "Storytelling & Reporting",
                [
                    "Pair maps with summaries highlighting coverage gaps and equity issues.",
                    "Suggest actionable insights (new clinic locations, transport improvements).",
                    "Include caveats on data freshness, service capacity, and local context.",
                ],
            ),
            (
                "Action Items",
                [
                    "Document plugin setup and troubleshooting tips.",
                    "Create sample outputs (catchment maps, equity tables) for students.",
                    "Prepare reflection questions around equity and reproducibility.",
                ],
            ),
        ],
    },
    "week07.html": {
        "title": "Week 07 – Bridge to Python & Reproducibility",
        "sections": [
            (
                "Week 07 · Bridge to Python & Reproducibility",
                "Introduce managed environments, version control, and standards for reproducible spatial analysis.",
            ),
            (
                "Why Reproducibility?",
                [
                    "Ensures analyses can be repeated, audited, and shared.",
                    "Supports collaboration and transparency.",
                    "Reduces onboarding time for future contributors.",
                ],
            ),
            (
                "Environment Options",
                [
                    "VS Code dev container — consistent stack, easy onboarding.",
                    "Miniforge/conda environment from `resources/environment/environment.yml`.",
                    "Google Colab for lightweight demos (limitations apply).",
                ],
            ),
            (
                "Project Structure",
                [
                    "Use `site_docs/` for published content and `resources/` for support materials.",
                    "Maintain predictable paths (`data/raw`, `data/processed`).",
                    "Track data changes in `resources/docs/data-inventory.md`.",
                ],
            ),
            (
                "Practical Walk-through",
                [
                    "Launch the dev container, run `python resources/environment/verify_setup.py`.",
                    "Open Week 08 notebook, review structure (setup cell, TODO cells, exports).",
                    "Demonstrate relative paths for loading processed data.",
                    "Commit changes with clear messages; capture environment updates.",
                ],
            ),
            (
                "Checklist for Students",
                [
                    "Confirm environment access (dev container or conda).",
                    "Clone repository or sync workspace structure.",
                    "Note any environment issues to raise in lab.",
                    "Identify datasets to automate in Week 08.",
                ],
            ),
        ],
    },
    "week08.html": {
        "title": "Week 08 – Python Vector Workflows",
        "sections": [
            (
                "Week 08 · Python Vector Workflows",
                "Automate QGIS-style vector analysis using GeoPandas, Shapely, and other Python libraries.",
            ),
            (
                "GeoPandas Fundamentals",
                [
                    "Read/write spatial data (`read_file`, `to_file`).",
                    "CRS handling (`to_crs`) to maintain consistent projections.",
                    "Attribute operations using Pandas-style methods (`assign`, `groupby`).",
                ],
            ),
            (
                "Cleaning & Standardisation",
                [
                    "Normalize column names, drop unused fields.",
                    "Handle multi-part geometries (`explode`) if needed.",
                    "Calculate area/length in projected CRS for per-km² metrics.",
                ],
            ),
            (
                "Spatial Joins & Overlays",
                [
                    "Point-in-polygon using `sjoin(predicate=\"within\")`.",
                    "Combine polygons with `overlay` or `dissolve` to match reporting requirements.",
                    "Check results with record counts and summaries.",
                ],
            ),
            (
                "Visualisation & Export",
                [
                    "Create quick choropleths via `GeoDataFrame.plot` with Matplotlib.",
                    "Add basemaps using Contextily if needed.",
                    "Export cleaned summaries to GeoPackage for reuse in QGIS (`neighbourhoods_summary.gpkg`).",
                ],
            ),
            (
                "Best Practices",
                [
                    "Write modular code (functions or notebooks with clear sections).",
                    "Log assumptions and filters inline.",
                    "Version-control notebooks or export scripts for reproducibility.",
                ],
            ),
            (
                "Next Steps",
                [
                    "Connect outputs to Week 09 raster analysis and Week 10 networks.",
                    "Plan for automated reporting (charts, tables) in future weeks.",
                    "Update `resources/docs/data-inventory.md` with processed dataset locations.",
                ],
            ),
        ],
    },
    "week09.html": {
        "title": "Week 09 – Raster & Remote Sensing in Python",
        "sections": [
            (
                "Week 09 · Raster & Remote Sensing in Python",
                "Process multi-temporal rasters, compute change metrics, and summarise results across administrative zones.",
            ),
            (
                "Remote Sensing Basics",
                [
                    "Spectral bands: red, NIR, SWIR; revisit cycles (Sentinel-2, Landsat 8/9).",
                    "Preprocessing considerations: cloud masking, atmospheric correction.",
                    "Resolution/resampling trade-offs for analysis vs visualisation.",
                ],
            ),
            (
                "Python Tools",
                [
                    "Rasterio for reading/writing GeoTIFFs and masking by AOI.",
                    "Rioxarray/xarray for multi-band analysis.",
                    "Rasterstats for zonal statistics over polygons.",
                ],
            ),
            (
                "Change Detection Workflow",
                [
                    "Clip pre- and post-event rasters to area of interest.",
                    "Compute indices (e.g., NDVI) and difference arrays.",
                    "Apply thresholds or classification to interpret magnitude of change.",
                    "Summarise mean/median change per boundary using zonal stats.",
                ],
            ),
            (
                "Visualisation & Reporting",
                [
                    "Plot change rasters with diverging colour ramps.",
                    "Map per-boundary summaries with GeoPandas.",
                    "Export GeoPackages/CSVs for integration into Week 11 design studio or capstone.",
                    "Document assumptions (temporal alignment, cloud cover) in reflections.",
                ],
            ),
            (
                "Action Items",
                [
                    "Select Sentinel or Landsat scenes relevant to class projects.",
                    "Create tutorials for clipping, NDVI calculation, and zonal stats.",
                    "Gather example use cases (deforestation, urban expansion, disaster recovery).",
                ],
            ),
        ],
    },
    "week10.html": {
        "title": "Week 10 – Transport Networks & Accessibility",
        "sections": [
            (
                "Week 10 · Transport Networks & Accessibility",
                "Use OSMnx and network analysis to evaluate mobility, isochrones, and equitable service coverage.",
            ),
            (
                "Graph Concepts",
                [
                    "Nodes (intersections/stops) and edges (streets, transit links).",
                    "Directed vs undirected graphs; weighted edges (length, time).",
                    "Simplification levels: primal vs dual networks.",
                ],
            ),
            (
                "Data Sources",
                [
                    "OpenStreetMap extracts via OSMnx.",
                    "GTFS feeds (transit schedules) for multimodal analysis.",
                    "Population/vulnerability layers for coverage calculations.",
                ],
            ),
            (
                "Workflow Highlights",
                [
                    "Download and simplify network graph with OSMnx.",
                    "Generate walking or driving isochrones around facilities.",
                    "Overlay isochrones with population polygons to quantify coverage.",
                    "Optionally compute centrality metrics to find critical links.",
                ],
            ),
            (
                "Storytelling",
                [
                    "Highlight accessibility disparities across demographics.",
                    "Propose infrastructure or service interventions (new stops, frequency changes).",
                    "Communicate assumptions (speed profiles, data freshness).",
                ],
            ),
            (
                "Next Steps",
                [
                    "Prepare example notebooks showing isochrone generation.",
                    "Collect local GTFS feeds and document licensing.",
                    "Design visuals for Week 11 layout critiques using network outputs.",
                ],
            ),
        ],
    },
    "week11.html": {
        "title": "Week 11 – Design & Storytelling Studio",
        "sections": [
            (
                "Week 11 · Design & Storytelling Studio",
                "Refine map layouts, apply accessibility checks, and craft compelling narratives for the capstone.",
            ),
            (
                "Narrative Structure",
                [
                    "Hook → Context → Insight → Call to action.",
                    "Align visuals with narrative flow; avoid unnecessary decoration.",
                    "Provide plain-language summaries alongside maps.",
                ],
            ),
            (
                "Design Systems",
                [
                    "Use grid-based layouts for consistent alignment.",
                    "Limit font families and maintain hierarchy (titles, labels, body).",
                    "Reuse colour palettes established in earlier weeks.",
                ],
            ),
            (
                "Accessibility Checklist",
                [
                    "Colour contrast meets or exceeds accessibility guidelines.",
                    "Provide alt text or descriptions for screen readers.",
                    "Ensure legends and labels are legible at intended output size.",
                ],
            ),
            (
                "Peer Critique Framework",
                [
                    "Clarity of message (does the map answer the question?).",
                    "Accuracy and integrity of data presentation.",
                    "Aesthetics (hierarchy, balance, typography, colour).",
                    "Accessibility considerations.",
                ],
            ),
            (
                "Action Items",
                [
                    "Develop critique rubric and distribute ahead of studio session.",
                    "Collect sample layouts (strong/weak) for discussion.",
                    "Ensure each student has at least one map ready for feedback.",
                ],
            ),
        ],
    },
    "week12.html": {
        "title": "Week 12 – Capstone Showcase",
        "sections": [
            (
                "Week 12 · Capstone Showcase & Reflection",
                "Present final projects, gather feedback, and document lessons learned.",
            ),
            (
                "Capstone Components",
                [
                    "Problem statement & context.",
                    "Data sources, processing workflow, reproducibility notes.",
                    "Key findings with supporting visuals (maps, charts, tables).",
                    "Recommendations or next steps.",
                ],
            ),
            (
                "Presentation Tips",
                [
                    "Keep it concise (3–5 minutes per project).",
                    "Lead with the insight, then show how you derived it.",
                    "Highlight uncertainties and assumptions.",
                    "Invite feedback and questions.",
                ],
            ),
            (
                "Feedback Framework",
                [
                    "Clarity: Does the narrative make sense?",
                    "Evidence: Are methods/data documented?",
                    "Design: Are visuals accessible and compelling?",
                    "Impact: What action could this analysis support?",
                ],
            ),
            (
                "Reflection & Future Work",
                [
                    "What GIS skills felt most valuable?",
                    "Which topics need deeper exploration post-course?",
                    "How will you share or publish your project (GitHub, blog, portfolio)?",
                ],
            ),
            (
                "Action Items",
                [
                    "Draft capstone brief and rubric; share ahead of Week 12.",
                    "Provide template README for project repositories.",
                    "Collect feedback from peers/instructors for continuous improvement.",
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

    /* Title slide styling */
    .slide.title-slide {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      color: white;
      text-align: center;
      justify-content: center;
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
    footer = f"{week_num} | Intro to GIS | © 2024"

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
    for each week's presentation.
    """
    slide_dir = Path(__file__).parent
    slide_dir.mkdir(parents=True, exist_ok=True)

    for filename, slide_data in SLIDES.items():
        html = generate_slide_deck(filename, slide_data)
        output_path = slide_dir / filename
        output_path.write_text(html, encoding="utf-8")
        print(f"  ✓ Generated {filename}")

    print(f"\nSuccessfully generated {len(SLIDES)} slide decks in {slide_dir}")


if __name__ == "__main__":
    main()
