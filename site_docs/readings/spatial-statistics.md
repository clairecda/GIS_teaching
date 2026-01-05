# Spatial Statistics & Regression

This reading introduces spatial autocorrelation and spatial regression—essential concepts for capstone projects that analyze relationships between variables across space.

---

## Why spatial data is different

### Tobler's First Law of Geography

> "Everything is related to everything else, but near things are more related than distant things."
> — Waldo Tobler, 1970

This simple observation has profound implications for data analysis. If you're studying house prices, crime rates, or health outcomes, nearby locations tend to have similar values—not because they influence each other directly, but because they share similar environments, demographics, and conditions.

This pattern is called **spatial autocorrelation**: the tendency for nearby values to be more similar (positive autocorrelation) or more different (negative autocorrelation) than random.

### Why this breaks standard statistics

Standard regression assumes that observations are **independent**—that knowing one value tells you nothing about nearby values. But spatial data violates this assumption.

**Example:** You want to know if parks reduce crime rates. You run a regression and find a significant negative relationship. But wait—both parks and low crime rates might cluster in wealthy neighbourhoods. The relationship might be spurious, driven by spatial clustering rather than a true causal effect.

If you ignore spatial autocorrelation:

- Your standard errors will be wrong (usually too small)
- Your significance tests will be misleading
- You might find "significant" relationships that don't exist
- You might miss real relationships hidden by spatial patterns

---

## Measuring spatial autocorrelation

### Global Moran's I

**Moran's I** measures whether similar values cluster together across the entire study area. It answers: "Is there an overall pattern of spatial clustering?"

**The value ranges from -1 to +1:**

| Moran's I | Interpretation |
|-----------|----------------|
| +1 | Perfect positive autocorrelation (identical neighbours) |
| 0 | Random spatial pattern (no autocorrelation) |
| -1 | Perfect negative autocorrelation (neighbours are opposites) |

**In practice:**

- Values > 0 with low p-value → Significant clustering (similar values near each other)
- Values ≈ 0 → Random pattern
- Values < 0 with low p-value → Significant dispersion (dissimilar values near each other)

**Example interpretation:**
```
Moran's I: 0.45
p-value: 0.001

Interpretation: There is significant positive spatial autocorrelation
(Moran's I = 0.45, p < 0.001). High values tend to cluster near other
high values, and low values cluster near other low values.
```

### Local Moran's I (LISA)

**Local Indicators of Spatial Association (LISA)** identify *where* clustering occurs. While global Moran's I gives one number for the whole map, LISA gives a value for each location.

**LISA identifies four types of clusters:**

| Cluster Type | Meaning | On map |
|--------------|---------|--------|
| **High-High (HH)** | High value surrounded by high values | Hot spot |
| **Low-Low (LL)** | Low value surrounded by low values | Cold spot |
| **High-Low (HL)** | High value surrounded by low values | Spatial outlier |
| **Low-High (LH)** | Low value surrounded by high values | Spatial outlier |

**LISA maps** show these clusters, helping you identify:

- Where are the hot spots?
- Where are the cold spots?
- Which locations don't fit the pattern (outliers)?

---

## Spatial weights matrices

Both Moran's I and spatial regression require defining "neighbours." A **spatial weights matrix (W)** specifies which locations are considered neighbours and how much weight each neighbour gets.

### Common weight types

**Contiguity-based (for polygons):**

- **Queen contiguity:** Neighbours share an edge OR corner (like a queen in chess)
- **Rook contiguity:** Neighbours share an edge only (like a rook in chess)

**Distance-based (for points or polygons):**

- **Fixed distance:** All locations within X meters are neighbours
- **K-nearest neighbours:** The k closest locations are neighbours
- **Inverse distance:** All locations are neighbours, but closer ones get more weight

### How to choose

| Weight type | Best for |
|-------------|----------|
| Queen contiguity | Administrative boundaries, census data |
| K-nearest neighbours | Point data, irregular polygons |
| Fixed distance | When you have a theoretical reason for a specific distance |

**Start with Queen contiguity** for polygon data—it's the most common choice and usually works well.

---

## Spatial regression

When you find significant spatial autocorrelation in your residuals (the errors from a standard regression), you need spatial regression.

### The problem with OLS

**Ordinary Least Squares (OLS)** regression assumes independent errors. With spatial data:

```
crime_rate = β₀ + β₁(poverty_rate) + β₂(unemployment) + ε
```

If the errors (ε) are spatially autocorrelated—if the model over-predicts in some areas and under-predicts in nearby areas—your results are unreliable.

### Two main spatial models

**1. Spatial Lag Model (SLM)**

Accounts for spatial dependence in the **outcome variable**. Use when you think a location's value is influenced by neighbouring values.

```
crime_rate = ρ(W × crime_rate) + β₁(poverty_rate) + β₂(unemployment) + ε
```

The ρ (rho) term captures how much a location's crime rate depends on its neighbours' crime rates.

**When to use:** When there's a theoretical reason for spatial spillover. For example:
- Crime might spread between neighbourhoods
- House prices are influenced by nearby house prices
- Disease spreads from person to person

**2. Spatial Error Model (SEM)**

Accounts for spatial dependence in the **error term**. Use when spatial clustering is due to unmeasured variables that are themselves spatially clustered.

```
crime_rate = β₀ + β₁(poverty_rate) + β₂(unemployment) + (λWε + u)
```

The λ (lambda) term captures spatial autocorrelation in the errors.

**When to use:** When you think there are missing spatially-clustered variables. For example:
- You didn't measure "neighbourhood quality" but it affects crime and is spatially clustered
- Environmental factors you didn't include vary smoothly over space

### Choosing between models

| Test | If significant... |
|------|-------------------|
| Run OLS first, check Moran's I of residuals | Residuals are spatially autocorrelated → need spatial model |
| Lagrange Multiplier (LM) test for lag | Spatial lag model might be appropriate |
| Lagrange Multiplier (LM) test for error | Spatial error model might be appropriate |

**Practical approach:**
1. Run OLS regression
2. Check Moran's I of residuals—if not significant, OLS is fine
3. If residuals are autocorrelated, try both spatial lag and spatial error
4. Compare model fit (AIC, log-likelihood)
5. Check that residuals of chosen model are no longer autocorrelated

---

## Interpreting results

### Reading regression output

```
==============================================================================
                   Spatial Lag Model - Maximum Likelihood
==============================================================================
Dependent Variable:    crime_rate        Number of Observations: 150
Mean dependent var:    45.2              Number of Variables:    4
Pseudo R-squared:      0.68

-----------------------------------------------------------
    Variable      Coefficient    Std.Error    z-value   p-value
-----------------------------------------------------------
    CONSTANT        12.45          3.21        3.88     0.0001
    poverty_rate     0.82          0.15        5.47     0.0000
    unemployment     0.34          0.12        2.83     0.0047
    W_crime_rate     0.35          0.08        4.38     0.0000
-----------------------------------------------------------
```

**What to report:**

1. **Model type:** "We used a spatial lag model because..."
2. **Spatial coefficient:** ρ = 0.35 (significant) means crime rates are positively associated with neighbouring crime rates
3. **Variable coefficients:** A 1-unit increase in poverty rate is associated with a 0.82-unit increase in crime rate, controlling for unemployment and spatial dependence
4. **Model fit:** Pseudo R² = 0.68 means the model explains 68% of variation
5. **Residual check:** "Moran's I of residuals was not significant (p = 0.45), indicating the spatial model adequately accounts for spatial autocorrelation"

### Common mistakes

❌ **Running OLS and ignoring spatial autocorrelation**
→ Your significance tests are wrong

❌ **Using spatial regression when there's no spatial autocorrelation**
→ OLS is fine and simpler

❌ **Not checking residuals after spatial regression**
→ Model might still have problems

❌ **Interpreting spatial lag coefficient as causation**
→ Correlation between neighbours doesn't prove one causes the other

---

## Tools in QGIS

### Moran's I

1. Install **GeoDa** plugin (or use standalone GeoDa software)
2. `Vector → GeoDa → Spatial Autocorrelation → Moran's I`
3. Select your variable and weight type
4. Examine the Moran scatter plot and significance

### LISA clusters

1. `Vector → GeoDa → Spatial Autocorrelation → Local Moran's I`
2. Creates a new layer with cluster classifications
3. Style by cluster type (HH, LL, HL, LH, not significant)

### Regression

QGIS has limited spatial regression capabilities. For regression:

- Use the **OLS Regression** tool in Processing Toolbox for basic regression
- Export residuals and test for spatial autocorrelation
- For spatial regression models, use Python (see notebook) or standalone GeoDa

---

## Tools in Python

Python's **PySAL** (Python Spatial Analysis Library) provides comprehensive spatial statistics tools.

### Key packages

| Package | Purpose |
|---------|---------|
| `libpysal` | Spatial weights matrices |
| `esda` | Exploratory spatial data analysis (Moran's I, LISA) |
| `spreg` | Spatial regression models |
| `splot` | Visualization for spatial statistics |

### Quick example

```python
import geopandas as gpd
from libpysal.weights import Queen
from esda.moran import Moran, Moran_Local
from spreg import OLS, ML_Lag, ML_Error

# Load data
gdf = gpd.read_file("neighbourhoods.gpkg")

# Create spatial weights
w = Queen.from_dataframe(gdf)
w.transform = 'r'  # Row-standardize

# Global Moran's I
moran = Moran(gdf['crime_rate'], w)
print(f"Moran's I: {moran.I:.3f}, p-value: {moran.p_sim:.4f}")

# Local Moran's I (LISA)
lisa = Moran_Local(gdf['crime_rate'], w)
gdf['lisa_cluster'] = lisa.q  # 1=HH, 2=LH, 3=LL, 4=HL

# OLS regression
y = gdf[['crime_rate']].values
X = gdf[['poverty_rate', 'unemployment']].values
ols = OLS(y, X, w=w, name_y='crime_rate',
          name_x=['poverty_rate', 'unemployment'])
print(ols.summary)

# Spatial lag model
lag = ML_Lag(y, X, w, name_y='crime_rate',
             name_x=['poverty_rate', 'unemployment'])
print(lag.summary)
```

**See the [Spatial Statistics Notebook](../reference/notebooks.md) for complete worked examples.**

---

## For your capstone

If your capstone involves regression analysis:

### Minimum requirements

1. **Check for spatial autocorrelation** in your outcome variable (Moran's I)
2. **Run OLS regression** as a baseline
3. **Check residuals** for spatial autocorrelation
4. **If residuals are autocorrelated**, use spatial regression
5. **Report and interpret** all relevant statistics

### In your write-up

Include:

- Moran's I value and interpretation for key variables
- LISA map showing clusters (if relevant)
- Regression table with coefficients, standard errors, p-values
- Model diagnostics (R², AIC, residual checks)
- Clear interpretation of what the results mean substantively

### What instructors look for

✓ Evidence that you checked for spatial autocorrelation
✓ Appropriate model choice with justification
✓ Correct interpretation of coefficients
✓ Acknowledgment of limitations
✓ Clear visualizations (LISA maps, residual maps)

---

## Summary

| Concept | What it tells you |
|---------|-------------------|
| **Moran's I** | Is there overall spatial clustering? |
| **LISA** | Where are the hot spots and cold spots? |
| **Spatial weights** | Which locations are neighbours? |
| **Spatial lag model** | Outcome depends on neighbours' outcomes |
| **Spatial error model** | Errors are spatially correlated |

**The key insight:** Spatial data requires spatial methods. Ignoring spatial autocorrelation leads to misleading results. Always check, and use spatial regression when needed.

---

## Further reading

- GeoDa Center tutorials: [geodacenter.github.io](https://geodacenter.github.io/)
- PySAL documentation: [pysal.org](https://pysal.org/)
- Anselin, L. (1988). *Spatial Econometrics: Methods and Models*
- Chi, G. & Zhu, J. (2020). *Spatial Regression Models for the Social Sciences*
