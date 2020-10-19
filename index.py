import subprocess
import sys
import os
import importlib.util

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

name = 'pyqt5'
if name not in sys.modules:
	install(name)
else:
	print('Goodbye')
os.system('python .\gui\main.py')