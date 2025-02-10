# Pedestrian Crash Project

Work in progress.  Testing moving ArcGIS code to QGIS.

## Install

Testing on MacOS Sonoma only so far.

Install latest QGIS from https://qgis.org/download/.

In project directory at terminal run install.sh to download Roads GIS data.

## Run

Run the following, replace Metuchen with any New Jersey municiaplity name.  Enclose in quotes if containing spaces, like "Red Bank".

```
export PROJ_LIB="/Applications/QGIS.app/Contents/Resources/proj"

/Applications/QGIS.app/Contents/MacOS/bin/python3 test.py Metuchen
```

## License

Distributed under the GPLv3, see [LICENSE](LICENSE) for more information.

## Acknowledgments

[Road Centerlines of NJ - Next Gen 911](https://njogis-newjersey.opendata.arcgis.com/documents/newjersey::road-centerlines-of-nj-next-gen-911-shp/about) is provided by NJ Office of Information Technology, Office of GIS (NJOGIS)


