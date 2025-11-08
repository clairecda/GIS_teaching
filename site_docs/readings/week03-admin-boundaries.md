# Understanding Administrative Boundaries

Administrative boundaries split countries into named geographic units used for governance, statistics, service delivery, and community identity. Knowing how and why these boundaries are defined helps you choose the right level of detail for analysis and interpret your results responsibly.

## Layers of administration

Most countries organise multiple boundary levels:

- **National (ADM0):** Country outline (e.g., Australia, Indonesia). Used for international comparisons, trade agreements, and national reporting.
- **First-order (ADM1):** States, provinces, regions (e.g., New South Wales, Victoria, Queensland). Common for state policy, elections, regional infrastructure planning.
- **Second-order (ADM2 / SA2 / LGA):** Local government areas, municipalities, Statistical Area Level 2. Often align with service delivery, local taxes, and school districts.
- **Statistical areas:** Purpose-built units for data collection (e.g., ABS Statistical Areas, U.S. Census tracts). Optimised for population thresholds, not political governance.

Boundaries can overlap or change over time, so always check metadata for vintage and purpose.

## Why they matter

1. **Census & population statistics:** Statistical areas ensure consistent population thresholds, making indicators like SEIFA or ACS comparable. Using the wrong boundary leads to misleading comparisons.
2. **Health planning:** Agencies align hospital catchments or vaccination campaigns with LGAs or bespoke health regions to allocate resources fairly.
3. **Education:** School zones or education districts determine funding, capacity planning, and student assignment.
4. **Emergency management:** Disaster response, policing, and fire services organise operations by predefined boundaries for coordination and jurisdiction.
5. **Political representation:** Electoral boundaries (federal, state, local) determine who votes where and who represents which communities.

## Working with boundaries in the course

- **Weeks 1–2:** Natural Earth ADM0/ADM1 boundaries for global mapping practice.
- **Week 3:** Statistical Areas Level 2 (SA2) in Australia (or local equivalents) for socio-economic joins (SEIFA, ACS).
- **Week 5:** Crime datasets aggregated by Local Government Areas or police districts—know which boundary the dataset uses.
- **Week 6:** Health accessibility modelling mixes administrative boundaries (for reporting) with network-derived catchments.
- **Weeks 8–10:** Python notebooks reuse boundary IDs (`SA2_CODE`, `GEOID`, `LGA_CODE`) for reproducible joins and summaries.

## Tips for learners

- Read metadata before using a boundary: purpose, steward, update cadence, CRS, ID fields.
- Keep historical versions if comparing across census years—boundaries often shift.
- When combining datasets from multiple countries, harmonise to a comparable level (e.g., ADM1 vs SA2) and note differences in resolution.

## Further reading

- ABS: [Australian Statistical Geography Standard (ASGS)](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)
- UN: [Second Administrative Level Boundaries (SALB) Project](https://www.unsalb.org/)
- Natural Earth: [Cultural Vector Data](https://www.naturalearthdata.com/features/)
- Humanitarian Data Exchange: [Common Operational Datasets – Boundaries](https://data.humdata.org/faq#common-operational-datasets)

Understanding the purpose of your boundary shapes the story you can tell with spatial data—don’t treat them as arbitrary lines on a map.
