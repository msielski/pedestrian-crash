# Pedestrian Crash Project

Work in progress. Testing on MacOS Sonoma only so far.

## Install

Install latest QGIS from https://qgis.org/download/.

## Download Data

In project directory at terminal:

- Run `get-gis-data.sh` to download Roads GIS data.
- Run `get-dot-data.sh` specifying county names to download and combine DOT Crash data, for example `get-dot-data.sh Middlesex Union`.

## Process Data

- Run `convert-dot-data.sh` to convert the DOT Crash data into standard CSV format.

## Run

*Note: Currently test.py does not process any of the DOT data as this is still a work in progress.*

Run the following, replace Metuchen with any New Jersey municiaplity name.  Enclose in quotes if containing spaces, like "Red Bank".

```
export PROJ_LIB="/Applications/QGIS.app/Contents/Resources/proj"

/Applications/QGIS.app/Contents/MacOS/bin/python3 test.py Metuchen
```

## License

Distributed under the GPLv3, see [LICENSE](LICENSE) for more information.

## Acknowledgments

[Road Centerlines of NJ - Next Gen 911](https://njogis-newjersey.opendata.arcgis.com/documents/newjersey::road-centerlines-of-nj-next-gen-911-shp/about) are provided by NJ Office of Information Technology, Office of GIS (NJOGIS).

[Crash Data](https://www.nj.gov/transportation/refdata/accident/crash_data.shtm) are provided by NJ Department of Transportation (DOT).
