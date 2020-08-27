from XLStoJSON import *

input_dir = "Sheet"
output_dir = "Sheet"
filename = "example.xls"
xls2json = XLS2JSON(input_dir, output_dir, filename)
xls2json.read()
xls2json.write()