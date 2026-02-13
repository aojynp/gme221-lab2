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
