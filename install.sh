python3 -c "import subprocess; subprocess.call(['pip3', 'install', 'xlrd==1.2.0'])"
python3 -c "from setuptools import setup; setup(name='XLStoJSON', version='0.0.1', author='Carlos A. S. Ferreira', author_email='casf.eq@gmail.com', description=('This package intends to support the conversion of a tabular dataset file from XLS/XLSX format to JSON format. The table is assumed to have headers for both rows and columns.'), long_description=open('xls2json/README.md', 'r').read(), packages=['xls2json'], package_data = {'xls2json': ['Sheet/example.xls']}, license='BSD', url='https://github.com/casfeq/XLStoJSON')" install --prefix="~/.local"
rm -rf build
rm -rf dist
rm -rf XLStoJSON.egg-info