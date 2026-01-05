# Week 5 Lecture · Crime Hotspots & Storytelling

## This week
We explore the ethics of crime mapping and learn kernel density estimation (KDE) techniques to identify hotspots. Learners consider the social impact of crime visualisation and develop responsible communication practices.

## By the end of the week you will
- Apply kernel density estimation to identify crime hotspots and explain how KDE parameters affect results.
- Evaluate the ethical implications of crime mapping including privacy, bias, and community stigma.
- Communicate crime data responsibly using neutral language, context, and appropriate disclaimers.
- Understand how boundary choice, temporal aggregation, and data provenance shape public perception.

## Key vocabulary
Kernel density estimation (KDE) · hotspot · bandwidth · search radius · crime mapping ethics · data bias · privacy aggregation · jittering · hex bins · narrative framing · community impact · spatial autocorrelation.

## Hotspots and spatial autocorrelation

When we identify hotspots, we're essentially detecting **spatial autocorrelation**—the tendency for nearby locations to have similar values. Crime doesn't occur randomly across space; it clusters.

**Why this matters:**

- **KDE** (kernel density estimation) is one way to visualize clustering, but it's descriptive—it shows patterns without testing whether they're statistically significant
- **Moran's I** is a formal statistical test that measures whether spatial clustering exists and is unlikely to occur by chance
- **LISA** (Local Indicators of Spatial Association) identifies specific hot spots and cold spots with statistical significance levels

**The connection:**

| Technique | What it does | Output |
|-----------|--------------|--------|
| KDE | Smooths point data into a continuous surface | Heat map showing intensity |
| Moran's I | Tests if overall clustering exists | Single number (-1 to +1) with p-value |
| LISA | Identifies where clusters are located | Map of significant hot/cold spots |

**For your capstone:** If you're analyzing patterns that cluster spatially (crime, health outcomes, prices), consider whether you need descriptive visualization (KDE) or statistical testing (Moran's I, LISA). See [Spatial Statistics & Regression](../readings/spatial-statistics.md) for detailed guidance.

## What happens in class
- Discuss ethical considerations in crime mapping: data provenance, privacy, bias in policing data, and community impact.
- Demonstrate KDE hotspot analysis in QGIS with various bandwidth settings and compare outputs.
- Critique sample crime maps with differing framing and discuss potential social impacts.
- Workshop responsible storytelling: choosing neutral language, adding socio-economic context, and documenting limitations.
- Review privacy-preserving techniques such as coordinate jittering and hex bin aggregation.

## Prepare beforehand
- Download the crime dataset for Week 5 from the [data download guide](../onboarding/03-download-data.md).
- Read [Ethics in Spatial Analysis](../readings/week05-ethics-in-mapping.md) and note discussion questions.
- Review the [Week 5 lab](../weeks/week05.md) to understand the KDE workflow.

## Connected lab
The [Week 5 lab](../weeks/week05.md) applies KDE hotspot analysis to crime data with careful attention to boundary selection, temporal filtering, and responsible annotation of outputs.

