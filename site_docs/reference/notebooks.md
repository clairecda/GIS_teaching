# Python Notebooks

All course notebooks for Weeks 7-10. You can download them, view on GitHub, or run directly in Google Colab.

---

## Week 7: Hello GIS

Your first Python notebook - environment setup, Jupyter basics, and first GeoPandas code.

| Option | Link |
|--------|------|
| **Run in Colab** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb) |
| View on GitHub | [week07_hello_gis.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week07_hello_gis.ipynb) |

---

## Week 8: Vector Workflows

Replicate QGIS vector operations in Python - filtering, joins, density calculations, choropleth maps.

| Option | Link |
|--------|------|
| **Run in Colab** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week08_vector_workflows.ipynb) |
| View on GitHub | [week08_vector_workflows.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week08_vector_workflows.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week08_vector_workflows.ipynb) |

---

## Week 9: Raster & Remote Sensing

Work with satellite imagery, calculate NDVI, perform change detection and zonal statistics.

| Option | Link |
|--------|------|
| **Run in Colab** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week09_raster_remote_sensing.ipynb) |
| View on GitHub | [week09_raster_remote_sensing.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week09_raster_remote_sensing.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week09_raster_remote_sensing.ipynb) |

---

## Week 10: Transport Networks

Network analysis with OSMnx - download street networks, calculate isochrones, analyze accessibility.

| Option | Link |
|--------|------|
| **Run in Colab** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week10_transport_networks.ipynb) |
| View on GitHub | [week10_transport_networks.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week10_transport_networks.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week10_transport_networks.ipynb) |

---

## Using Google Colab

Google Colab provides a free Python environment in your browser - no installation required.

**First time setup:**

1. Click the "Open in Colab" button above
2. Sign in with your Google account
3. The notebook opens in a temporary environment

**Installing packages:**

Colab has many packages pre-installed, but you may need to add GIS libraries:

```python
# Run this cell first in Colab
!pip install geopandas rasterio rasterstats osmnx contextily
```

**Saving your work:**

- `File → Save a copy in Drive` to save to your Google Drive
- `File → Download → Download .ipynb` to save locally

**Limitations:**

- Sessions timeout after ~12 hours of inactivity
- Large datasets may exceed free memory limits
- Some packages may have version differences

---

## Local Setup (Recommended)

For the best experience, run notebooks locally with the course environment:

1. Follow the [Python Setup Guide](../onboarding/04-python-setup.md)
2. Download notebooks to your `intro-gis/notebooks/` folder
3. Launch Jupyter: `jupyter lab`
4. Open and run notebooks

Local setup gives you:
- Faster performance
- Full control over packages
- Persistent storage
- Offline access
