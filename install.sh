#!/bin/bash
curl -O https://geoapps.nj.gov/njgin/road/Tran_road_NG911.shp.zip
unzip -d "data/Tran_road_NG911.shp" "Tran_road_NG911.shp.zip"
rm Tran_road_NG911.shp.zip
