# Week 3 Lecture · Boundary Systems & Data Joins

## This week
We unpack administrative and statistical boundary systems and learn how to join socio-economic indicators to spatial datasets responsibly.

## By the end of the week you will
- Describe the hierarchy and purpose of common boundaries (SA2, LGA, ADM levels).
- Understand how boundary updates affect longitudinal comparisons and how to mitigate issues.
- Perform attribute joins safely and document assumptions.

## Key vocabulary
ADM0/ADM1/ADM2 · SA2 · LGA · correspondence file · join key · area-weighted interpolation.

## What happens in class
- Review who maintains boundaries (ABS, census bureaus) and why updates occur.
- Demonstrate attribute joins between SA2 and SEIFA, highlighting data-type pitfalls.
- Discuss storytelling implications of choosing different geographies.
- Share troubleshooting techniques (correspondence files, data cleaning) before switching to lab time.

## Prepare beforehand
- Download SA2 + SEIFA datasets using the [data download guide](../onboarding/data-downloads.md).
- Review [Week 3 lecture slides](../assets/slides/week03.html).
- Read [Understanding administrative boundaries](../readings/week03-admin-boundaries.md) and note questions for class.

## Connected lab
The [Week 3 lab](../weeks/week03.md) walks through join workflows, derived metrics, and error checking.

## Further Reading

**Essential:**
- [Australian Statistical Geography Standard (ASGS) - ABS](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/latest-release) - Official documentation on SA2, SA3, SA4 and other Australian boundary structures
- [Understanding Census Geography - ABS](https://www.abs.gov.au/websitedbs/d3310114.nsf/home/geography) - Guide to how census boundaries are designed and updated
- [Joining Tables in QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_vector/vector_properties.html#joins-properties) - Official QGIS documentation on attribute joins and common pitfalls
- [The Modifiable Areal Unit Problem (MAUP)](https://gistbok.ucgis.org/bok-topics/modifiable-areal-unit-problem) - GIS&T Body of Knowledge article explaining boundary choice impacts

**Optional but recommended:**
- [SEIFA Documentation - ABS](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release) - Technical details on Index of Relative Socio-economic Advantage and Disadvantage
- [Correspondence Files Guide - ABS](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/latest-release#correspondences) - How to convert data between different boundary vintages
- [Global Administrative Areas (GADM)](https://gadm.org/data.html) - Free worldwide administrative boundary data with documentation