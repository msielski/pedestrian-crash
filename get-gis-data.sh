#!/bin/bash

# This script will download and unzip Road Centerlines of NJ - Next Gen 911
# from https://njogis-newjersey.opendata.arcgis.com/documents/newjersey::road-centerlines-of-nj-next-gen-911-shp/about.
# Provided by NJ Office of Information Technology, Office of GIS (NJOGIS)

curl -O https://geoapps.nj.gov/njgin/road/Tran_road_NG911.shp.zip
unzip -d "data/Tran_road_NG911.shp" "Tran_road_NG911.shp.zip"
rm Tran_road_NG911.shp.zip
