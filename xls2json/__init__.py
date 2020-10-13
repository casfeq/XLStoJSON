import os
import json
import datetime
import xlrd


class XLS2JSON(object):
	def __init__(self, input_dir, output_dir, filename):
		self.input_dir = input_dir
		self.output_dir = output_dir
		self.filename = filename

	def read(self):
		self.workbook = xlrd.open_workbook("{}/{}".format(self.input_dir, self.filename))
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

	def write(self):
		file = "{}/{}.json".format(self.output_dir, os.path.splitext(self.filename)[0])
		f = open(file, "w+")
		f.write(json.dumps(self.workbook_data, indent="\t", separators=(",", ": ")))
		f.close()