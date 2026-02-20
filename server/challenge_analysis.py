import geopandas as gpd
from sqlalchemy import create_engine

#Database connection parameters
host ="localhost"
port = "5433"
dbname = "gme221"
user = "postgres"
password = "sangyan"

#Create connection string
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

#Create SQLAlchemy engine
engine = create_engine(conn_str)

# Minimal SQL queries (no spatial operations) 
sql_parcel = "SELECT parcel_pin, geom FROM public.parcel" 
sql_landuse = "SELECT name, geom FROM public.landuse" 

# Load data into GeoDataFrames 
parcels = gpd.read_postgis(sql_parcel, engine, geom_col="geom") 
parcels = parcels.rename_geometry("geometry")

landuse = gpd.read_postgis(sql_landuse, engine, geom_col="geom") 
landuse = landuse.rename_geometry("geometry")

#Reproject to EPSG:3395 for area calculations
parcels = parcels.to_crs(epsg=3395) 
landuse = landuse.to_crs(epsg=3395)
#print(parcels.head())
#print(parcels.geometry)

#Compute total Parcel Area
parcels["total_area"] = parcels.geometry.area 
#print(parcels["total_area"]) 

#Overlay
overlay = gpd.overlay(parcels, landuse, how="intersection") 
overlay["landuse_area"] = overlay.geometry.area 

#Compute Landuse Percentage
overlay["percentage"] = ( 
	overlay["landuse_area"] / overlay["total_area"] 
) * 100 
overlay["percentage"] = overlay["percentage"].round(2) 

# get dominant land use for per parcel 
idx = overlay.groupby("parcel_pin")["percentage"].idxmax() 
dominant = overlay.loc[idx, ["parcel_pin", "name", "percentage"]] 


# Classification focusing on lest than 30% residential zones with a minimum thershold of 100m^2
#dominant_res = overlay[
#    (
#        (overlay["name"] == "Residential Zone - Low Density") |
#        (overlay["name"] == "Residential Zone - Medium Density")
#    ) &
#    (overlay["percentage"] <= 30) &
#    (overlay["landuse_area"] >= 100)
#].copy()

# Classification focusing on lest than 30% residential zones with a minimum thershold of 1000m^2
dominant_res = overlay[
    (
        (overlay["name"] == "Residential Zone - Low Density") |
        (overlay["name"] == "Residential Zone - Medium Density")
    ) &
    (overlay["percentage"] <= 30) &
    (overlay["landuse_area"] >= 1000)
].copy()


#print(dominant_res.head())

#Dominant_res back to EPSG 4326
dominant_res = dominant_res.to_crs(epsg=4326)

#GeoJSON
dominant_res.to_file( 
"output/challenge_result_3_1000.geojson", 
driver="GeoJSON" 
) 
print("GeoJSON saved successfully.")