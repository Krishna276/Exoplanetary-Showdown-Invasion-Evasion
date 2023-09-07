"""Setup script for Exoplanetary Showdown: Invasion Evasion.

Please ensure that this file is run from the directory you want to install the game into.
"""

from os import getcwd, system
from runpy import run_path
from sys import path

system('pip install pygame')
system('pip install pygame-gui')
system('python src/main.py')
