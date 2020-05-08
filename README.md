# XLStoJSON

This code converts a table dataset from XLS (or XLSX) format to JSON. The table is assumed to have headers for both rows and columns.

## Dependencies

To use, it is necessary

- [python 3](https://www.python.org/downloads/);
- [xlrd](https://pypi.org/project/xlrd/).

## Convert

To convert, just put the \*.xls (or \*.xlsx) files in the apps/input folder, navigate to the apps folder and run the command

```shell
$ python3 main.py
```

The converted \*.json files will be saved in the apps/output folder.