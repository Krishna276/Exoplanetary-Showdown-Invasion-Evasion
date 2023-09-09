"""Setup script for Exoplanetary Showdown: Invasion Evasion.

Please ensure that this file is run from the directory you want to install the game into.

This file is not a very technical one. Use main.py to chose a seed.
"""

from ensurepip import bootstrap
from os import system as run_command
from pathlib import Path
from platform import system as operating_system

DIRECTORY: str = Path(__file__).parent.absolute()

bootstrap()
OS: str = operating_system()
match OS:
    case 'Windows':
        print('Operating system detected: Windows.')
        run_command('py -m pip install pygame')
        run_command('py -m pip install pygame-gui')
        run_command(f'py {DIRECTORY}\\src\\main.py')
    case 'Linux':
        print('Operating system detected: Linux.')
        run_command('python3 -m pip install pygame')
        run_command('python3 -m pip install pygame-gui')
        run_command(f'python3 {DIRECTORY}/src/main.py')
    case _:
        print(
            'Sorry, your OS is not supported yet by the setup script.\n'
            'Things you can try:\n'
            '    Install dependencies pip, pygame and pygame-gui yourself, then run src/main.py'
        )
