import xls2json as x2j

input_dir = "xls2json/Sheet"
output_dir = "xls2json/Sheet"
filename = "example.xls"
xls2json = x2j.XLS2JSON(input_dir, output_dir, filename)
xls2json.read()
xls2json.write()