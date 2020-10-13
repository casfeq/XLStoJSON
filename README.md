# XLStoJSON

This package intends to support the conversion of a tabular dataset file from XLS/XLSX format to JSON format. The table is assumed to have headers for both rows and columns.

## Dependencies & Installation

To use, it is necessary

- [python 3](https://www.python.org/downloads/) (3.8.2);
- [xlrd](https://pypi.org/project/xlrd/) (1.2.0).

You may install MSHtoXDMF and its dependencies by running the command:

```bash
./install.sh
```

## Example

There is an example of the usage of XLStoJSON in "test.py". You may also test the installation by running:

```bash
$ python3 test.py
```

XLS/XLSX data structure input:

```
+-----------------+------------------+------------------+
|      Label      |     Header 1     |     Header 2     |
+-----------------+------------------+------------------+
|      Label 1    |     Value 11     |     Value 21     |
|      Label 2    |     Value 12     |     Value 22     |
|      Label 3    |     Value 13     |     Value 23     |
+-----------------+------------------+------------------+
```
JSON data structure output:

```json
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

## Uninstallation

You may remove this package by running:

```bash
./uninstall.sh
```