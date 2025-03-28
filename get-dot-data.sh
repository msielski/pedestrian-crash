#!/bin/bash

# This script will download NJDOT Crash Tables from
# https://www.nj.gov/transportation/refdata/accident/rawdata01-current.shtm
# and combine by county and table.  Due to data format changes between
# 2016 and 2017, data will be separated into the periods before and after.
#
# File layout information is available at
# https://www.nj.gov/transportation/refdata/accident/masterfile.shtm.

counties=( "Atlantic" "Bergen" "Burlington" "Camden" "CapeMay" "Cumberland" "Essex" "Gloucester" "Hudson" "Hunterdon" "Mercer" "Middlesex" "Monmouth" "Morris" "Ocean" "Passaic" "Salem" "Somerset" "Sussex" "Union" "Warren" )

if [ "$1" = "" ]
then
  echo "Usage: $0 <one or more counties to download data for>"
  echo "  Counties available are: ${counties[*]}"
  echo
  exit 1
fi

counties=( "$@" )
tables=( "Accidents" "Drivers" "Occupants" "Pedestrians" "Vehicles" )

mkdir -p data/2001-2016
mkdir -p data/2017-latest

cd data/2001-2016
for year in {2001..2016}; do
  for county in "${counties[@]}"; do
    for table in "${tables[@]}"; do
      echo "$year $county $table"
      curl -L -O "http://www.state.nj.us/transportation/refdata/accident/$year/${county}${year}${table}.zip"
    done
  done
done
unzip "*.zip"
rm *.zip
for county in "${counties[@]}"; do
  for table in "${tables[@]}"; do 
    cat "$county"*"$table".txt > Combined_"$county"_"$table".csv
  done
done
rm *.txt

cd ../2017-latest
for year in {2017..2022}; do
  for county in "${counties[@]}"; do
    for table in "${tables[@]}"; do
      echo "$year $county $table"
      curl -L -O "http://www.state.nj.us/transportation/refdata/accident/$year/${county}${year}${table}.zip"
    done
  done
done
unzip "*.zip"
rm *.zip
for county in "${counties[@]}"; do
  for table in "${tables[@]}"; do 
    cat "$county"*"$table".txt > Combined_"$county"_"$table".csv
  done
done
rm *.txt

cd ..
