from FixedWidthDataParser import FixedWidthDataParser
import sys
import csv

filename_in = sys.argv[1]
layout = sys.argv[2]
filename_out = sys.argv[3]

data_parser = FixedWidthDataParser()
data_parser.setIsDelimited(True)

match layout:
    case "accidents-old":
        data_parser.setColumnWidths([31, 12, 24, 10, 2, 4, 2, 25, 15, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 50, 1, 4, 1, 16, 7, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 1, 35, 1, 25, 2, 2, 2, 8, 8, 1, 80, 5])
    case "drivers-old":
        data_parser.setColumnWidths([31, 2, 25, 2, 5, 2, 10, 1, 1, 2, 3, 30, 30, 1, 2])
    case "occupants-old":
        data_parser.setColumnWidths([31, 2, 2, 2, 2, 2, 3, 1, 2, 2, 1, 2, 2, 2, 4])
    case "pedestrians-old":
        data_parser.setColumnWidths([31, 2, 2, 25, 2, 5, 10, 3, 1, 1, 2, 3, 30, 30, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 4, 2, 1, 1])
    case "vehicles-old":
        data_parser.setColumnWidths([31, 2, 4, 2, 30, 20, 3, 4, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 10, 1, 10, 50, 1])
    case "accidents-new":
        data_parser.setColumnWidths([31, 12, 24, 10, 2, 4, 2, 25, 15, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 50, 1, 4, 1, 16, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 1, 35, 1, 25, 2, 2, 2, 2, 9, 9, 1, 80, 5])
    case "drivers-new":
        data_parser.setColumnWidths([31, 2, 25, 2, 5, 2, 10, 1, 1, 2, 3, 30, 30, 30, 30, 30, 30, 30, 30,  1, 2, 2])
    case "occupants-new":
        data_parser.setColumnWidths([31, 2, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 4])
    case "pedestrians-new":
        data_parser.setColumnWidths([31, 2, 2, 25, 2, 5, 10, 3, 1, 1, 2, 3, 30, 30, 30, 30, 30, 30, 30, 30, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 1, 1])
    case "vehicles-new":
        data_parser.setColumnWidths([31, 2, 4, 2, 30, 20, 3, 4, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 10, 10, 10, 1, 10, 50, 1])

data = data_parser.parse(filename_in)
with open(filename_out, 'w') as f:
    write = csv.writer(f)
    write.writerows(data)
