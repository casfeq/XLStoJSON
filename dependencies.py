import subprocess


dependencies = [
	"xlrd==1.2.0"]
for package in dependencies:
	subprocess.call(["pip3", "install", package])