# Administrative Boundaries

**Read before:** Week 3 | **Time:** 20 minutes

---

## What are administrative boundaries?

Administrative boundaries are the invisible lines that divide places into named areas. They define where one region ends and another begins — for governance, statistics, service delivery, and identity.

Every time you see data "by suburb," "by state," or "by postcode," you're looking at data aggregated to administrative boundaries.

---

## Why boundaries matter for GIS

In GIS, boundaries let you:

- **Join data to maps** — connect census statistics to geographic areas
- **Aggregate points** — count incidents per suburb, calculate rates per region
- **Compare areas** — which neighbourhoods have the highest income? lowest access to healthcare?
- **Define service areas** — which council is responsible for this location?

**Without understanding boundaries, your analysis can be misleading or wrong.**

---

## Layers of administration

Most countries have multiple boundary levels, from national down to local:

### Global/International

| Level | Examples | Used for |
|-------|----------|----------|
| ADM0 | Countries | International comparisons, trade, treaties |
| ADM1 | States, provinces, regions | State policy, regional planning |
| ADM2 | Counties, districts, LGAs | Local government, service delivery |

### Australia-specific

| Level | Name | Count | Used for |
|-------|------|-------|----------|
| National | Australia | 1 | International reporting |
| State/Territory | NSW, VIC, QLD, etc. | 8 | State government, legislation |
| SA4 | Statistical Area Level 4 | ~90 | Labour markets, regional economy |
| SA3 | Statistical Area Level 3 | ~350 | Regional services, health planning |
| **SA2** | Statistical Area Level 2 | ~2,500 | **Most common for analysis** — suburbs/communities |
| SA1 | Statistical Area Level 1 | ~60,000 | Small area statistics, privacy threshold |
| LGA | Local Government Area | ~550 | Council services, rates, local planning |
| POA | Postal Area | ~2,700 | Postcode-based analysis |

### United States

| Level | Name | Count | Used for |
|-------|------|-------|----------|
| State | States | 50 (+DC, territories) | State policy |
| County | Counties | ~3,000 | Local government |
| Tract | Census Tract | ~85,000 | Demographic analysis |
| Block Group | Block Group | ~240,000 | Small area statistics |

---

## Statistical vs administrative boundaries

**Administrative boundaries** are created for governance:
- Local Government Areas (LGAs)
- Electoral districts
- School zones
- Police districts

**Statistical boundaries** are created for data collection:
- SA2, SA3, SA4 (Australia)
- Census tracts (US)
- Output Areas (UK)

**Key difference:** Statistical boundaries are designed to have similar population sizes, making comparisons fairer. Administrative boundaries vary wildly in population (inner-city council vs rural shire).

---

## The problem with boundaries

### 1. Boundaries change over time

Boundaries are redrawn regularly:
- Census boundaries update every 5-10 years
- Council amalgamations merge LGAs
- Electoral redistributions shift voting districts
- New suburbs are created as cities grow

**Impact:** Data from 2016 may not match 2021 boundaries. A suburb that existed in 2011 may have been split into three.

**Solution:** Always check the "vintage" (year) of your boundaries. Use correspondence files to translate between versions.

### 2. The Modifiable Areal Unit Problem (MAUP)

!!! warning "MAUP is technical AND political"
    The Modifiable Areal Unit Problem isn't just a methodological curiosity—it's a tool of power.

**What is MAUP?** When you aggregate individual data points into areas (like suburbs or councils), the results you get depend on:

1. **Scale** — How big are the areas? (SA2 vs LGA vs state)
2. **Zonation** — Where exactly are the boundary lines drawn?

Change either one, and your statistics change—even though the underlying data is identical. This is the Modifiable Areal Unit Problem.

The same data can tell completely different stories depending on how you draw boundaries.

**Example:** Crime rates in Sydney
- By LGA: "Parramatta has high crime"
- By SA2: "Only 2 suburbs in Parramatta are high crime, the rest are low"
- By postcode: Different pattern again

**The technical problem:** Results change based on the units you choose. Aggregate data to larger areas and patterns smooth out. Use smaller units and hotspots appear. Neither is "wrong"—they're different views of the same reality.

**The political problem:** Boundaries are not neutral. They are drawn by institutions with agendas:

- **Gerrymandering** manipulates electoral boundaries to favour certain parties
- **Redlining** used neighbourhood boundaries to deny services to minority communities
- **"High crime area"** designations justify increased policing in specific neighbourhoods
- **School catchments** can entrench advantage or disadvantage
- **Statistical boundaries** can hide or reveal inequality depending on where lines are drawn

When someone shows you a map with boundaries, ask: *Who drew these lines? For what purpose? Who benefits from this particular division of space?*

**Impact:** You can (accidentally or deliberately) manipulate findings by choosing boundaries that support your conclusion. A government wanting to show "crime is down" might use larger boundaries that smooth out hotspots. A lobby group wanting more police funding might use smaller units that make problems look concentrated.

**What to do:**
- Be transparent about boundary choice and why you chose it
- Test sensitivity by running analysis at multiple boundary levels
- Report what changes when you use different units
- Ask who created the boundaries and what they were designed for
- Consider whether administrative boundaries serve your analytical question—or obscure it

### 3. Boundaries don't match real-world patterns

Administrative lines are often arbitrary:
- A shopping centre might serve people from 5 different LGAs
- A disease outbreak doesn't stop at suburb boundaries
- Commuters cross boundaries daily

**Impact:** Analysis "by suburb" may miss patterns that cross boundaries.

**Solution:** Consider whether boundaries make sense for your analysis. Sometimes you need custom catchments (service areas, travel time zones) instead.

---

## Working with boundaries in this course

| Week | Boundaries used | Why |
|------|-----------------|-----|
| 1-2 | Natural Earth (countries, states) | Global overview, learning QGIS |
| 3 | SA2 or census tracts | Joining socioeconomic data |
| 5 | LGA or police districts | Crime data aggregation |
| 6 | Custom service areas | Health accessibility (not admin boundaries) |
| 8-10 | SA2, LGA (in Python) | Reproducible joins |

---

## Key fields for joining data

When you download boundary files and data tables, they share a common ID field. You join on this field.

### Australian boundaries

| Boundary | ID field | Example |
|----------|----------|---------|
| SA2 | `SA2_CODE21` or `SA2_CODE_2021` | `117011326` |
| SA3 | `SA3_CODE21` | `11701` |
| LGA | `LGA_CODE21` or `LGA_CODE_2021` | `17200` |
| State | `STE_CODE21` | `1` (NSW) |

### US boundaries

| Boundary | ID field | Example |
|----------|----------|---------|
| State | `STATEFP` | `06` (California) |
| County | `GEOID` | `06037` (LA County) |
| Tract | `GEOID` | `06037101110` |

### Tips for successful joins

1. **Check data types** — `"17200"` (text) won't join to `17200` (number)
2. **Check for leading zeros** — `06037` is different from `6037`
3. **Check vintage** — 2016 codes don't match 2021 boundaries
4. **Check for nulls** — unmatched records indicate a problem

---

## Where to get boundary data

### Australia
- [ABS Digital Boundary Files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files) — SA1, SA2, SA3, SA4, LGA
- State data portals — detailed local boundaries

### United States
- [US Census TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) — States, counties, tracts, block groups
- [Census Reporter](https://censusreporter.org/) — Easy downloads with data

### Global
- [Natural Earth](https://www.naturalearthdata.com/) — Countries, states/provinces (free)
- [GADM](https://gadm.org/) — Global administrative areas (free for non-commercial)
- [geoBoundaries](https://www.geoboundaries.org/) — Open-source global boundaries

---

## Checklist before using boundaries

Before you start analysis:

- [ ] What boundary level am I using? (SA2, LGA, tract?)
- [ ] What vintage/year are these boundaries?
- [ ] Does my data table match this vintage?
- [ ] What's the ID field for joining?
- [ ] Are the data types compatible? (text vs number)
- [ ] Is this the right level for my question?

---

## Common mistakes

| Mistake | What happens | How to avoid |
|---------|--------------|--------------|
| Wrong vintage | Unmatched records, missing data | Check year in filename and metadata |
| Text vs number ID | Join returns no matches | Convert field types before joining |
| Wrong boundary level | Misleading aggregation | Think about what level makes sense |
| Ignoring MAUP | Results depend on arbitrary choice | Test multiple levels, be transparent |
| Assuming boundaries are fixed | Historical comparisons break | Use correspondence files |

---

## Key takeaways

✅ **Always check the vintage** — boundaries change over time

✅ **Match your data to your boundaries** — same year, same ID format

✅ **Choose the right level** — SA2 for communities, LGA for councils, etc.

✅ **Be aware of MAUP** — boundary choice affects results

✅ **Statistical ≠ administrative** — they serve different purposes

✅ **Document your choice** — explain why you used these boundaries

---

## Reflection questions

Before Week 3, think about:

1. What boundaries exist where you live? (suburbs, councils, postcodes?)
2. Have you seen boundary changes affect your area? (council mergers, new suburbs?)
3. When would you choose SA2 vs LGA for analysis?
