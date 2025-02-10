from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsFeature,
    QgsProject,
    QgsFeatureRequest,
    QgsWkbTypes
)
from qgis.gui import (
    QgsMapCanvas,
    QgsLayerTreeMapCanvasBridge
)
import sys


# Initialize QGIS.
def init():
    app = QgsApplication([], True)
    QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS", True)
    QgsApplication.initQgis()
    return app


# Show canvas and execute app.
def show_canvas(app):
    canvas = QgsMapCanvas()
    QgsLayerTreeMapCanvasBridge(
        QgsProject.instance().layerTreeRoot(),
        canvas
    )
    canvas.show()
    app.exec_()


# Load roads for given municipality name.
def load_municipality_roads(muni_name):
    path = "./Tran_road_NG911.shp/Tran_road.shp"
    all_roads_layer = QgsVectorLayer(path, "all_roads", "ogr")
    if not all_roads_layer.isValid():
        print("Layer failed to load - did you run install.sh first?")
        sys.exit(1)

    # Make in memory layer with same CRS and geometry type as source.
    geom_type = QgsWkbTypes.displayString(all_roads_layer.wkbType())
    crs = all_roads_layer.crs()
    muni_roads_layer = QgsVectorLayer(
        f"{geom_type}?crs={crs.authid()}",
        "muni_roads",
        "memory"
    )

    # Add fields to the memory layer.
    fields = all_roads_layer.fields()
    provider = muni_roads_layer.dataProvider()
    provider.addAttributes(fields)
    muni_roads_layer.updateFields()

    # Get features from the original layer.
    muni_roads_query = f"POSTCOMM_L = '{muni_name}' OR POSTCOMM_R = '{muni_name}'"
    print(muni_roads_query)
    feature_request = QgsFeatureRequest().setFilterExpression(muni_roads_query)
    features = all_roads_layer.getFeatures(feature_request)

    # Add features to the memory layer.
    new_features = []
    print("Copying features...")
    for feature in features:
        new_feat = QgsFeature(feature)
        new_features.append(new_feat)
    success, added_features = provider.addFeatures(new_features)
    print(f"Features added successfully? {success}, Count: {len(added_features)}")

    # Update extents and add layer to project.
    muni_roads_layer.updateExtents()
    QgsProject.instance().addMapLayer(muni_roads_layer)
    return muni_roads_layer


# Main program.
if len(sys.argv) < 2:
    print("Municipality name is required argument.")
    sys.exit(1)

muni_name = sys.argv[1]
app = init()
muni_roads = load_municipality_roads(muni_name)
show_canvas(app)
app.exitQgis()
