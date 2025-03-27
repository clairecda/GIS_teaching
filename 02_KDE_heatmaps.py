import processing
from qgis.core import QgsVectorLayer, QgsProject

# Set your base folder path
base_folder = "/Users/UWA_QGIS/A2"

# File paths for predator and endangered animal GeoPackages
predator_gpkg = f"{base_folder}/01_Endangered_Species_Predator_Distribution/predator.gpkg"
endangered_animal_gpkg = f"{base_folder}/01_Endangered_Species_Predator_Distribution/endangered_animal.gpkg"

# Output raster paths for both KDE heatmaps
predator_heatmap_output = f"{base_folder}/01_Endangered_Species_Predator_Distribution/predator_heatmap.tif"
endangered_animal_heatmap_output = f"{base_folder}/01_Endangered_Species_Predator_Distribution/endangered_animal_heatmap.tif"

# Load the input layers
predator_layer = QgsVectorLayer(predator_gpkg, "predator", "ogr")
endangered_animal_layer = QgsVectorLayer(endangered_animal_gpkg, "endangered_animal", "ogr")

# Add both layers to the QGIS project (optional, for visualization)
QgsProject.instance().addMapLayer(predator_layer)
QgsProject.instance().addMapLayer(endangered_animal_layer)

# Define the parameters common to both layers
radius = 12000  # 12 km radius
pixel_size = 1000  # 1 km pixel size

# Parameters for Predator KDE
predator_params = {
    'INPUT': predator_layer,
    'RADIUS': radius,
    'PIXEL_SIZE': pixel_size,
    'WEIGHT_FIELD': '',
    'KERNEL': 0,  # Default kernel
    'DECAY': 0,   # No decay
    'OUTPUT_VALUE': 0,
    'OUTPUT': predator_heatmap_output
}

# Parameters for Endangered Animal KDE
endangered_animal_params = {
    'INPUT': endangered_animal_layer,
    'RADIUS': radius,
    'PIXEL_SIZE': pixel_size,
    'WEIGHT_FIELD': '',
    'KERNEL': 0,  # Default kernel
    'DECAY': 0,   # No decay
    'OUTPUT_VALUE': 0,
    'OUTPUT': endangered_animal_heatmap_output
}

# Run the KDE (Heatmap) algorithm for both predator and endangered animal layers
processing.run("qgis:heatmapkerneldensityestimation", predator_params)
processing.run("qgis:heatmapkerneldensityestimation", endangered_animal_params)

print(f"Predator heatmap saved to {predator_heatmap_output}")
print(f"Endangered Animal heatmap saved to {endangered_animal_heatmap_output}")
