# XLStoJSON

This code converts a tabular dataset from XLS/XLSX format to JSON. The table is assumed to have headers for both rows and columns.


## Example

XLS/XLSX data structure input:
```
+-------------------+-----------------------+-----------------------+
|		Label		|		Header 1		|		Header 2		|
+-------------------+-----------------------+-----------------------+
|		Label 1		|		Value 11		|		Value 21		|
|		Label 2		|		Value 12		|		Value 22		|
|		Label 3		|		Value 13		|		Value 23		|
+-------------------+-----------------------+-----------------------+
```
JSON data structure output:
```
{
	"Label 1": {
		"Label": "Label 1",
		"Header_1": "Value 11",
		"Header_2": "Value 21"
	},
	"Label 2": {
		"Label": "Label 2",
		"Header_1": "Value 12",
		"Header_2": "Value 22"
	},
	"Label 3": {
		"Label": "Label 3",
		"Header_1": "Value 13",
		"Header_2": "Value 23"
	}
}
```
## Dependencies

To use, it is necessary

- [python 3](https://www.python.org/downloads/);
- [xlrd](https://pypi.org/project/xlrd/).

## Convert

To convert, just put the \*.xls/\*.xlsx files in the apps/input folder, navigate to the apps folder and run the command

```shell
$ python3 main.py
```

The converted \*.json files will be saved in the apps/output folder.