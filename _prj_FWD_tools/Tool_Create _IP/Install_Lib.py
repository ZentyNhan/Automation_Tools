import os
import sys
import time

Lib = [
    'PyQt5',
    'pyqt5_tools',
    'PyQt5Designer',
    'openpyxl',
    'faker'
    'xml'
]

for lib in Lib:
    os.system('pip install ' + lib)
time.sleep(5)
os.system('python -m pip install --upgrade pip')