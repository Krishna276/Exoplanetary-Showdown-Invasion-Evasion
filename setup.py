"""Setup script for Exoplanetary Showdown: Invasion Evasion.

Please ensure that this file is run from the directory you want to install the game into.

This file is not a very technical one. Use main.py to chose a seed.
"""

from os import system

system('pip install pygame')
system('pip install pygame-gui')
system('python src/main.py')
