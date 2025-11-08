# Understanding Administrative Boundaries

Administrative boundaries split countries into named geographic units used for governance, statistics, service delivery, and community identity. Knowing how and why these boundaries are defined helps you choose the right level of detail for analysis and interpret your results responsibly.

## Layers of administration

Most countries organise multiple boundary levels:

- **National (ADM0):** Country outline (e.g., Australia, Indonesia). Used for international comparisons, trade agreements, and national reporting.
- **First-order (ADM1):** States, provinces, regions (e.g., New South Wales, Victoria, Queensland). Common for state policy, elections, regional infrastructure planning.
- **Second-order (ADM2/SA2/LGA):** Local government areas, municipalities, SA2s. Often align with service delivery, local taxes, school districts.
- **Statistical areas:** Purpose-built units for data collection (e.g., ABS Statistical Area Levels, U.S. Census tracts). Optimised for population thresholds, not necessarily political governance.

Boundaries can overlap or change over time, so always check metadata for vintage and purpose.

## Why they matter

1. **Census & population statistics:** Statistical areas ensure consistent population thresholds so indicators (like SEIFA) are comparable. Choosing the wrong boundary makes comparisons misleading.
2. **Health planning:** Health agencies align hospital catchments or vaccination campaigns with local government districts or bespoke health regions to allocate resources fairly.
3. **Education:** School zones or education districts determine funding, capacity planning, and student assignment.
4. **Emergency management:** Disaster response, policing, and fire services organise operations by predefined boundaries for coordination and jurisdiction.
5. **Political representation:** Electoral boundaries (federal, state, local) determine who votes where and who represents which communities.

## Working with boundaries in the course

- **Week 1–2:** You’ll work with Natural Earth ADM0/ADM1 boundaries for global mapping practice.
- **Week 3:** We dive into Statistical Areas Level 2 (SA2) in Australia (or local equivalents elsewhere) to join socio-economic indicators like SEIFA. Pay attention to population thresholds and naming conventions.
- **Week 5:** Crime data is typically aggregated by Local Government Areas (LGAs) or police districts. Understand which boundary the dataset uses before comparing across regions.
- **Week 6:** Health accessibility modelling often mixes administrative boundaries (for reporting) with network-based catchments. Be explicit when switching between them.
- **Weeks 8–10:** Python workflows reuse these boundaries for reproducible joins and spatial statistics. Consistent coding of boundary IDs (e.g., `SA2_CODE`, `GEOID`, `LGA_CODE`) is essential.

## Tips for learners

- Always read “Data Description” or “Metadata” sections when downloading boundaries or statistics. Look for:
  - Boundary purpose and stewardship agency.
  - Update cadence (e.g., ABS releases ASGS every five years).
  - Coordinate reference system.
  - ID fields (e.g., `SA2_CODE_2021`, `NAME_1`) used for joins.
- Keep a copy of historical boundaries if you compare data across multiple years; boundaries often change between censuses.
- When combining datasets from multiple countries, harmonise to a common level (e.g., ADM1 vs SA2) and note differences in resolution.

## Further reading

- ABS: [Australian Statistical Geography Standard (ASGS)](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026)
- UN: [Second Administrative Level Boundaries (SALB) Project](https://www.unsalb.org/)
- Natural Earth: [Cultural Vector Data](https://www.naturalearthdata.com/features/)
- Humanitarian Data Exchange: [Common Operational Datasets – Boundaries](https://data.humdata.org/faq#common-operational-datasets)

Understanding the underlying purpose of your boundary shapes the story you can tell with spatial data—don’t treat them as arbitrary lines on a map.
