# Script starts here - No changes needed below this line

# Install necessary packages if not installed
packages <- c("raster", "terra", "sf")
install_if_needed <- packages[!(packages %in% installed.packages()[,"Package"])]
if(length(install_if_needed)) install.packages(install_if_needed)

# Load required libraries
library(raster)
library(terra)
library(sf)
# Set your base folder path 
base_folder <- "/Users/UWA_QGIS/A2"

# Set the paths to the KDE heatmap GeoTIFF files (generated from Script #2)
endangered_animal_heatmap_path <- file.path(base_folder, "01_Endangered_Species_Predator_Distribution/endangered_animal_heatmap.tif")
predator_heatmap_path <- file.path(base_folder, "01_Endangered_Species_Predator_Distribution/predator_heatmap.tif")

# Load the region boundary (assuming you used the same boundary as in Script #1)
boundary_gpkg <- file.path(base_folder, "00_Data_received/Southwest_region.gpkg")
region_boundary <- st_read(boundary_gpkg, layer = "Southwest_region")

# Folder where reclassified rasters will be saved
output_folder_a <- file.path(base_folder, "01_Endangered_Species_Predator_Distribution")
output_folder_b <- file.path(base_folder, "03_Least_cost_path")
output_folder_c <- file.path(base_folder, "02_Cost_surface_habitat")



# Load the heatmaps as raster objects
endangered_animal_raster <- raster(endangered_animal_heatmap_path)
predator_raster <- raster(predator_heatmap_path)

# Convert region boundary to the correct CRS (EPSG:3577) and rasterize it
region_boundary <- st_transform(region_boundary, crs = st_crs(3577))
region_boundary_raster <- rasterize(region_boundary, predator_raster, field = 1)

# Function to reclassify endangered animal raster (1 = service, 2 = home, 3 = core)
reclassify_endangered_animal <- function(raster_data) {
  # Calculate quantiles for reclassification
  core_thresh <- quantile(raster_data[], 0.50, na.rm = TRUE)  # Core 50%
  home_thresh <- quantile(raster_data[], 0.95, na.rm = TRUE)  # Home 50-95%
  
  # Reclassification matrix
  reclass_matrix <- matrix(c(
    -Inf, core_thresh, 1,    # Core
    core_thresh, home_thresh, 2,  # Home
    home_thresh, Inf, 3      # Service
  ), ncol = 3, byrow = TRUE)
  
  # Apply reclassification
  reclassified_raster <- reclassify(raster_data, reclass_matrix)
  return(reclassified_raster)
}

# Function to reclassify predator raster (4 = core, 3 = home, 2 = service, fill NA with 1)
reclassify_predator <- function(raster_data, mask_region) {
  # Calculate quantiles for reclassification
  core_thresh <- quantile(raster_data[], 0.50, na.rm = TRUE)  # Core 50%
  home_thresh <- quantile(raster_data[], 0.95, na.rm = TRUE)  # Home 50-95%
  
  # Reclassification matrix
  reclass_matrix <- matrix(c(
    -Inf, core_thresh, 2,    # Service
    core_thresh, home_thresh, 3,  # Home
    home_thresh, Inf, 4      # Core
  ), ncol = 3, byrow = TRUE)
  
  # Apply reclassification
  reclassified_raster <- reclassify(raster_data, reclass_matrix)
  
  # Fill NA values with 1
  reclassified_raster[is.na(reclassified_raster[])] <- 1
  
  # Clip the reclassified raster to the region boundary
  reclassified_clipped <- mask(reclassified_raster, mask_region)
  
  return(reclassified_clipped)
}

# Reclassify endangered animal raster
endangered_animal_reclassified <- reclassify_endangered_animal(endangered_animal_raster)

# Reclassify and clip predator raster
predator_reclassified <- reclassify_predator(predator_raster, region_boundary_raster)

# Define output paths for reclassified rasters
endangered_animal_output_path <- file.path(output_folder_a, "endangered_animal_reclassified.tif")
endangered_animal_output_path <- file.path(output_folder_b, "endangered_animal_reclassified.tif")
predator_output_path <- file.path(output_folder_c, "predator_reclassified_clipped.tif")

# Save the reclassified rasters as GeoTIFF
writeRaster(endangered_animal_reclassified, endangered_animal_output_path, format = "GTiff", overwrite = TRUE)
writeRaster(predator_reclassified, predator_output_path, format = "GTiff", overwrite = TRUE)

# Output message
cat("Reclassified rasters saved as:\n")
cat(paste("Endangered Animal Reclassified:", endangered_animal_output_path, "\n"))
cat(paste("Predator Reclassified and Clipped:", predator_output_path, "\n"))
