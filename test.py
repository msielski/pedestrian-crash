from qgis.core import QgsApplication, QgsVectorLayer, QgsProject
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge

def init():
  a = QgsApplication([], True)
  QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS", True)
  QgsApplication.initQgis()
  return a

def show_canvas(app): 
  canvas = QgsMapCanvas()
  bridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), canvas)
  canvas.show()
  app.exec_()

def add_layer():
  path = "./Tran_road_NG911.shp/Tran_road.shp"
  layer = QgsVectorLayer(path, "my layer", "ogr")
  if not layer.isValid():
    print("Layer failed to load!")
  else:
    print(f"{layer.id()} layer loaded")
    QgsProject.instance().addMapLayer(layer, True)

app = init()
add_layer()
show_canvas(app)
app.exitQgis()
