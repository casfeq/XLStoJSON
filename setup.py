from setuptools import setup


setup(
	name="XLStoJSON",
	version="0.0.1",
	author="Carlos A. S. Ferreira",
	author_email="casf.eq@gmail.com",
	description=("This package intends to support the conversion of a tabular dataset file from XLS/XLSX format to JSON format. The table is assumed to have headers for both rows and columns."),
	long_description=open("XLStoJSON/README.md", "r").read(),
	packages=["XLStoJSON"],
	package_data = {"XLStoJSON": ["Sheet/example.xls"]},
	license="BSD",
	url="https://github.com/casfeq/XLStoJSON"
)