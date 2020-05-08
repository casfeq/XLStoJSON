import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
from libs.xls2json import *

files = CheckFiles()
ClearOutputFolder()
for f in files:
	dataset = XlsReader(f)
	JsonWriter(dataset, f)
