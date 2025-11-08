# Week 4 — Raster & Terrain Analysis

## Learning objectives

1. Explain the difference between elevation rasters, derived surfaces, and how they complement administrative boundaries.
2. Import DEM tiles (ELVIS or SRTM), clip them to an area of interest, and generate basic terrain products (hillshade, slope).
3. Combine raster outputs with boundary data to support environmental resilience and planning questions.

## Pre-work

- Download the elevation datasets outlined in `resources/docs/data-download-guide.md` (ELVIS DEM for Australia or SRTM tile for your study area).
- Review `resources/docs/readings/week02-data-models.md` (vector vs raster) and skim the boundary primer to remember which administrative levels you might overlay.
- Install any required QGIS plugins once confirmed by instructors (e.g., `Profile Tool`, `Raster Terrain Analysis`).

## Session outline (120 minutes)

| Time | Activity | Description | Resources |
| ---- | -------- | ----------- | --------- |
| 0:00–0:20 | Concepts refresher | Discuss DEM sources (ELVIS, SRTM), resolution, and use cases (flood planning, infrastructure). | Slides, `resources/docs/data-download-guide.md` |
| 0:20–0:50 | Hands-on import & clipping | Learners load DEM tile, reproject if needed, clip to AOI using SA2/LGA boundary. | QGIS demo project |
| 0:50–1:20 | Terrain products | Generate hillshade, slope, and contour layers; discuss styling for readability. | Processing Toolbox | 
| 1:20–1:40 | Overlay with boundaries | Combine raster outputs with SEIFA/SA2 or LGA boundaries to identify vulnerable areas. | Joined layer from Week 3 |
| 1:40–2:00 | Share-out & troubleshooting | Showcase results, discuss storage best practices (GeoTIFF, metadata), resolve common issues. | Troubleshooting doc |

## Guided exercise highlights

- Confirm DEM CRS (often geographic WGS84); reproject to projected CRS (e.g., EPSG:7856 for Australia) for accurate slope/area calculations.
- Use `Raster ▶ Extraction ▶ Clip Raster by Mask Layer` with the SA2 or LGA layer from Week 3.
- Generate hillshade via `Raster ▶ Analysis ▶ Hillshade` and slope via `Raster ▶ Terrain Analysis ▶ Slope`. Save outputs in `data/processed/week04/` with descriptive names (e.g., `hillshade_sa2_x.tif`).
- Style hillshade with grayscale ramp and adjust transparency to overlay with polygon boundaries.
- Use Boundary layers to summarise raster values (e.g., zonal statistics) if time permits.

## Discussion prompts

- How does DEM resolution influence the insights you can draw? When would you need higher-resolution LiDAR?
- Which boundary level is most appropriate when communicating terrain risk (state, LGA, SA2)?
- How will you document DEM sources and processing steps for reproducibility?

## Deliverables

- Clipped DEM and at least one derived product (hillshade, slope) saved in `data/processed/week04/`.
- Snapshot or exported map combining terrain output with boundary layer annotations.
- Reflection entry noting one terrain insight and a question for next week (`resources/docs/reflections/week04.md`).

## Accessibility & inclusion notes

- Provide guidance on colour ramps that maintain contrast for colour-blind users.
- Offer alternative text descriptions for hillshade examples.
- Ensure instructions acknowledge different hardware capabilities (large rasters may require patience).

## Looking ahead

- Preview Week 5 focus on crime hotspot analysis; encourage learners to consider how elevation/terrain might influence crime patterns or service access.
