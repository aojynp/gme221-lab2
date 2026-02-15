# GmE 221 Laboratory 2

## Overview
This Laborator performs a parcel-landsue overlay analysis using Python (GeoPandas)
Spatial data are retrieved from PostGIS using minimal SQL.
Overlay, area computation, percentage calculation, and classification are executed in Python.
The final  output is exported as a GeoJson file for visualization in QGIS.

------------
## Environment Setup
-Python 3.14.3
-PostgreSQL with PostGIS
-GeoPandas, SQLAlchemy, psycopg2

-------------

## How to Run
1. Activate the virtual environment
2. Run 'analysis.py' to execute the overlay and classification
3. Load the genrated GeoJSON file in QGIS

--------------

##Outputs
-GeoJSON file: 'output/dominant_residential.geojson'
-Visualization in QGIS

--------------------------------
## IO Reflection Milestone (Part B.6)
Geometry in PostGIS and GeoPandas have similarities and also differences. Storing them in PostGIS means you are in the working on the features and/or characteristics of the spatial data. It is like an archive with visual representation if the spatial coordinates are given. PostGIS allows you to view the whole database from tables to vectors or raster. While in the GeoPandas, it gives yppu what you ask/command in string format. It catches the information from the database inorder to answer certain commmands. 

For Part B of the laboratory, IO/input are considered than analysis because it gives you the inputs available from tehe spatial data - the attribute table, hence landuse and parcel. These inputs are essential in the process of "Input/Process/Output" structure of GIS algorithms because it is thee first step. These are the data needed to be manipulated, calculated, and processed in order to get the final output. These input is crucial and can cause unexpected errors along the process and output phases.

-------------------------------------

## Spatial Process and Classification (Part D3)
CRS transformation is necessary before area computation because it  indicates the process possibilities and units. For the EPSG 3395, there is a wide variation of spatial computation due to the metric unit that serves as basis for this type of CRS like instersections then calculate the area or the overlap and with calculated areas. If the unit is degrees like in EPSG 4326, there are only few and/or no computations to be done such as identification of the coordinates in Degrees, Minutes, Seconds or nearest parcel in 1 second or more. 

Overlay creates new spatial units that did not previously exist because it depends on the area of land use within a lot or parcel. This is the results of the intersection. Overlay serves as the spatial geometry presentation to compute the area and percentages.

In terms of classification, it is considered part of the analysis process when determining the fragments of land use types within the lots or parcels. Therefore, it simply means to make and idenfitication through the intersected spatial geometries' data from the attribute table. But, classification is sensitive to silver geometries or topology errors due to the spatial operation process or the intersection of geometries but if the geometries are not aligned or not with the same CRS. Gaps and/or overlaps will exist in the results.

Discussing further on the results, the dominance threshold alter spatial patterns based on the observed tabular results. It focused on the limit of a specific polygon characteristic/feature - 60%-100% Residential Zones within a lot/parcel. This makes a cluster or a group to a specific preference based on the goal or objective presentation. 
