import glob
import json
import os
import subprocess

import datetime
import xlrd


def CheckFiles():
	files = []
	if os.path.exists("input"):
		os.chdir("input")
		for file in glob.glob("*.xls"):
			files.append(file)
		for file in glob.glob("*.xlsx"):
			files.append(file)
		if files == []:
			print("There is no *.xls or *.xlsx files in the input folder")
	else:
		print("There is no input folder")
	print("")
	return files


def ClearOutputFolder():
	subprocess.call(["sh", "-c", "rm -rf ../output/*"])
	return


class XlsFile(object):
	def __init__(self, filename):
		self.workbook = xlrd.open_workbook(filename)
		self.workbook_data = {}
		for sheet in range(self.workbook.nsheets):
			worksheet = self.workbook.sheet_by_index(sheet)
			column_headers = self._get_column_headers(worksheet)
			row_headers = self._get_row_headers(worksheet)
			sheet_data = self._get_sheet_data(worksheet, column_headers)
			for row in range(1,worksheet.nrows):
				self.workbook_data[row_headers[row]] = sheet_data[row-1]


	def _get_column_headers(self, worksheet):
		column_headers = worksheet.row_values(0, 0, worksheet.row_len(0))
		return column_headers

	def _get_row_headers(self, worksheet):
		row_headers = worksheet.col_values(0,0,len(worksheet.col_values(0)))
		return row_headers

	def _get_sheet_data(self, worksheet, column_headers):
		rows = worksheet.nrows
		sheet_data = []
		for sheet in range(1, rows):
			row = worksheet.row(sheet)
			row_data = self._get_row_data(row, column_headers)
			sheet_data.append(row_data)
		return sheet_data

	def _get_row_data(self, row, column_headers):
		row_data = {}
		row_counter = 0
		for cell in row:
			if cell.ctype==xlrd.XL_CELL_DATE:
				row_data[column_headers[row_counter].replace(' ', '_')] = datetime.datetime(*xlrd.xldate_as_tuple(cell.value,0)).isoformat()
			else:
				row_data[column_headers[row_counter].replace(' ', '_')] = cell.value
			row_counter += 1
		return row_data


def XlsReader(filename):
	xlsfile = XlsFile(filename)
	dataset = xlsfile.workbook_data
	return dataset


def JsonWriter(dataset, file):
	filename = os.path.splitext(file)[0]
	file = "../output/" + filename + ".json"
	output = open(file, "w+")
	output.write(json.dumps(dataset, indent="\t",  separators=(',', ": ")))
	output.close()
	return