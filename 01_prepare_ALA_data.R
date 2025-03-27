# Install necessary packages if not installed
packages <- c("sf", "sp", "raster", "terra", "dplyr")
install_if_needed <- packages[!(packages %in% installed.packages()[,"Package"])]
if(length(install_if_needed)) install.packages(install_if_needed)

# Load required libraries
library(sf)
library(sp)
library(raster)
library(terra)
library(dplyr)


# -------------------------------------------------------------------------------------------------------------------------- ##
# UPDATE THIS SECTION ONLY

# Instructions for USER:

# 1. Download the predator and endangered species data from ALA, unzip the files, and place the CSV files in the "00_Data_received" folder.
# 2. Update the paths line 28 and 29 below to match your system.


# Set your base folder path 
base_folder <- "/Users/UWA_QGIS/A2"


# Specify the paths to the CSV files
predator_csv <- file.path(base_folder, "00_Data_received/ALA_FOX.csv")
endangered_animal_csv <- file.path(base_folder, "00_Data_received/ALA_Dgeoffroii__WQuoll.csv")

# Folder where outputs will be saved
output_folder <- file.path(base_folder, "01_Endangered_Species_Predator_Distribution")

# Load the area boundaries from the provided GeoPackage (adjust path if necessary)
boundary_gpkg <- file.path(base_folder, "00_Data_received/Southwest_region.gpkg")
area_boundary <- st_read(boundary_gpkg, layer = "Southwest_region")

# -------------------------------------------------------------------------------------------------------------------------- ##

# Script starts here - No changes needed below this line


# Function to create the folder structure
create_folders <- function(base_path) {
  # Create the main folder A2
  if (!dir.exists(base_path)) {
    dir.create(base_path)
  }
  
  # Create the subfolders
  subfolders <- c("01_Endangered_Species_Predator_Distribution", "03_Least_cost_path", "02_Cost_surface_habitat",
                  "04_Fire_hazard", "05_Adapt_capacity", "06_Fire_risk")
  
  for (folder in subfolders) {
    dir.create(file.path(base_path, folder))
  }
}

# Create the folder structure
create_folders(base_folder)

# Ensure the boundary is in the same CRS (EPSG:3577)
area_boundary <- st_transform(area_boundary, crs = 3577)

# Create a 10km buffer around the area boundary
buffer_distance <- 10000  # 10 km buffer
buffered_boundary <- st_buffer(area_boundary, dist = buffer_distance)

# Function to read, reproject, clip data, and save as GeoPackage
process_and_save_data <- function(csv_file, geopackage_name, buffered_boundary) {
  # Read the CSV file
  data <- read.csv(csv_file, check.names = FALSE)
  
  # Remove rows with missing coordinates in latitude and longitude columns
  data_clean <- data[!is.na(data$`Latitude - original`) & !is.na(data$`Longitude - original`), ]
  
  # Create a Simple Features object
  coords <- st_as_sf(data_clean, coords = c("Longitude - original", "Latitude - original"), crs = 4326)
  
  # Reproject to EPSG:3577
  coords_proj <- st_transform(coords, crs = 3577)
  
  # Clip the points to the buffered boundary
  coords_clipped <- st_intersection(coords_proj, buffered_boundary)
  
  # Save the clipped and reprojected data as a GeoPackage
  st_write(coords_clipped, file.path(output_folder, paste0(geopackage_name, ".gpkg")), delete_layer = TRUE)
  
  return(coords_clipped)
}



# Process and save the predator and endangered animal datasets
predator_clipped <- process_and_save_data(predator_csv, "predator", buffered_boundary)
endangered_animal_clipped <- process_and_save_data(endangered_animal_csv, "endangered_animal", buffered_boundary)

# Function to create a hexagonal grid over the area boundary extent and clip it to the area boundary
create_hex_grid <- function(boundary, cell_size, output_file) {
  # Create a hexagonal grid over the bounding box of the buffered boundary
  hex_grid <- st_make_grid(boundary, cellsize = cell_size, square = FALSE)
  
  # Convert the grid to an sf object
  hex_grid_sf <- st_as_sf(hex_grid)
  
  # Clip the hex grid to the area boundary
  hex_grid_clipped <- st_intersection(hex_grid_sf, boundary)
  
  # Save the clipped hex grid as a GeoPackage
  st_write(hex_grid_clipped, output_file, delete_layer = TRUE)
  
  return(hex_grid_clipped)
}
#Hex grids – If you wish to include hex grids in your analysis, then we suggest the following
#hex grid sizes: 6km for Tasmania; 10km for Northern Queensland; and 5km for the Hunter
#River). If using hex grids, make sure that you tie their relevance into your overall analysis and
#discussion.



# Create a hexagonal grid with a cell size of 10km and clip to the area boundary
hex_grid_clipped <- create_hex_grid(area_boundary, cell_size = 10000, 
                                    output_file = file.path(output_folder, "hex_grid.gpkg"))

# Function to count points within hex grid and save as a new layer in GeoPackage
count_points_and_save_layer <- function(hex_grid, points_data, output_gpkg, layer_name) {
  # Perform spatial intersection: check which points fall into each hex grid cell
  intersections <- st_intersects(hex_grid, points_data)
  
  # Count the number of points in each hex grid cell
  counts <- sapply(intersections, length)
  
  # Add the counts to the hex grid
  hex_grid_with_counts <- hex_grid %>%
    mutate(count_points = counts)
  
  # Save as a new layer in the GeoPackage
  st_write(hex_grid_with_counts, output_gpkg, layer = layer_name, delete_layer = TRUE)
  
  return(hex_grid_with_counts)
}

# Specify the path to the output GeoPackage
output_gpkg <- file.path(output_folder, "hex_grid_with_counts.gpkg")

# Create and save the endangered animal count layer
count_points_and_save_layer(hex_grid_clipped, endangered_animal_clipped, output_gpkg, "endangered_animal_count")

# Create and save the predator count layer
count_points_and_save_layer(hex_grid_clipped, predator_clipped, output_gpkg, "predator_count")
