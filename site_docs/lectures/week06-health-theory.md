# Week 6 Lecture · Health Equity & Accessibility

## This week
We explore how geographic access to healthcare shapes health equity outcomes. You'll learn to measure accessibility using network analysis and isochrones, then overlay this with vulnerability indices to identify communities facing barriers to essential services.

## By the end of the week you will
- Explain how spatial access to health services influences health equity and social determinants of health.
- Compare accessibility metrics (buffers, isochrones, gravity models) and understand when to apply each.
- Use vulnerability indices (SEIFA, SVI, ARIA+) to identify populations at highest risk of poor access.
- Communicate accessibility findings with appropriate language that centers action and avoids deficit framing.

## Key vocabulary
Health equity · accessibility · isochrone · service area · catchment · two-step floating catchment area (2SFCA) · SEIFA · social vulnerability index (SVI) · ARIA+ · drive-time analysis · network analysis.

## What happens in class
- Frame health equity through social determinants of health and discuss why location matters, using Australian rural/metropolitan examples.
- Compare accessibility metrics side-by-side: simple buffers vs. drive-time zones vs. gravity models, noting data requirements and assumptions.
- Explore the Malaria Atlas Project as a case study in global health GIS and discuss data integration, uncertainty visualization, and policy impact.
- Work through a live comparison of two accessibility maps (buffer vs. isochrone) to identify how method choice changes findings.
- Brainstorm equity-focused policy interventions based on observed accessibility gaps.

## Prepare beforehand
- Review the [Week 6 lab](../weeks/week06.md) to understand the workflow you'll be implementing.
- Install the QNEAT3 plugin in QGIS ahead of class (see lab instructions).
- Download OpenStreetMap road network data for your study area using the data checklist.

## Connected lab
In the Week 6 lab, you'll generate service areas using QNEAT3, overlay them with SEIFA or other vulnerability data, and create maps that tell an equity-focused accessibility story.

## Further Reading

**Essential:**
- [SEIFA - Socio-Economic Indexes for Areas (ABS)](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia) - Official Australian Bureau of Statistics documentation on SEIFA disadvantage indices and how to interpret them
- [CDC/ATSDR Social Vulnerability Index (SVI)](https://www.atsdr.cdc.gov/placeandhealth/svi/index.html) - US vulnerability mapping tool with data downloads, methodology, and applications for public health planning
- [QNEAT3 Plugin Documentation](https://root676.github.io/) - Official guide to network analysis in QGIS, covering isochrone creation, service area analysis, and routing
- [WHO Handbook on Health Inequality Monitoring (Chapter 7)](https://www.who.int/publications/i/item/9789241548632) - Framework for measuring geographic accessibility and health service distribution globally

**Optional but recommended:**
- [Accessibility and Remoteness Index of Australia (ARIA+)](https://www.health.gov.au/topics/rural-health-workforce/classifications/aria) - Australian Department of Health classification system for measuring remoteness and service access
- [Two-Step Floating Catchment Area Method Explained](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1389236/) - Academic paper introducing 2SFCA methodology for measuring spatial accessibility to healthcare (Luo & Wang, 2003)
- [Malaria Atlas Project](https://malariaatlas.org/) - Global health GIS platform demonstrating spatial modeling, data integration, and disease risk prediction at scale

**Videos:**
- [QGIS Network Analysis and Isochrones](https://www.youtube.com/results?search_query=QGIS+network+analysis+isochrone+service+area) - Search for tutorials on creating service areas and isochrones
- [Health Equity and Social Determinants](https://www.youtube.com/results?search_query=health+equity+social+determinants+of+health+explained) - Search for videos on how place and opportunity shape health outcomes
