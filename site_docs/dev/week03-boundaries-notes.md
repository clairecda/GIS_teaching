# Week 3 Lecture · Boundary Systems & Data Joins

## Objectives

- Explain why countries maintain multiple boundary hierarchies (administrative vs statistical).
- Illustrate how boundary changes affect longitudinal analysis.
- Review best practices for joining tabular data (SEIFA, ACS) to polygons.

## Core topics

1. **Boundary ecosystem overview**  
   - Administrative vs statistical boundaries (refer back to [Understanding administrative boundaries](../readings/week03-admin-boundaries.md)).  
   - Who maintains them (ABS, Census, Eurostat, local councils) and release cadences.
2. **Boundary change implications**  
   - Visual timeline of ASGS releases; demonstrate how SA2 splits/merges break comparisons.  
   - Strategies: rebasing, area-weighted interpolation, using correspondence files.
3. **Join fundamentals**  
   - Unique keys, data types, handling nulls.  
   - Demonstrate mismatch scenarios (leading zeros, whitespace, outdated codes).  
   - Using crosswalk tables/correspondence files.
4. **Communication**  
   - Documenting boundary level in maps/reports.  
   - Caution against mixing incomparable geographies (postcodes vs LGAs).

## Suggested visuals

- Diagram of ADM0 → ADM1 → ADM2 → statistical areas.  
- Map showing boundary revisions between ASGS 2016 vs 2021.  
- Flowchart for join process with checks (validate CRS, inspect attribute table, run spot checks).

## Activity ideas

- Quick boundary quiz: identify which boundary fits each policy question.  
- Join debugging: provide messy CSV with different ID formatting, have learners fix and document the process.

## Reading references

- [Administrative boundary explainer](../readings/week03-admin-boundaries.md).  
- ABS: [ASGS overview](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026).  
- ABS: Correspondence files (show where to find them).

## Link to lab

- Prepares learners for the Week 3 vector join exercise.  
- Reinforces why we store cleaned joins in `data/processed/week03/`.
