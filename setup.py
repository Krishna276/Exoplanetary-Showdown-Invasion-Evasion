"""Setup script for Exoplanetary Showdown: Invasion Evasion.

Please ensure that this file is run from the directory you want to install the game into.

This file is not a very technical one. Use main.py to chose a seed.
"""

from colorama import Fore
from ensurepip import bootstrap
from os import system as run_command
from pathlib import Path
from platform import system as operating_system

DIRECTORY: str = Path(__file__).parent.absolute()

try:
    bootstrap()
    print(f'{Fore.GREEN}PIP auto-installation succeeded.{Fore.RESET}')
except:
    print(f'{Fore.RED}PIP auto-installation failed.{Fore.RESET}')
    print(f"{Fore.YELLOW}If you don't already have PIP installed, then Pygame and Pygame GUI auto-installation will"
        f" fail.{Fore.RESET}"
    )

OS: str = operating_system()
match OS:
    case 'Windows':
        print(f'{Fore.BLUE}Operating system detected: Windows.{Fore.RESET}')
        run_command('py -m pip install pygame')
        run_command('py -m pip install pygame-gui')
        run_command(f'py {DIRECTORY}\\src\\main.py')
    case _:
        print(
            'Sorry, your OS is not supported yet by the setup script.\n'
            'Things you can try:\n'
            '    Install dependencies pip, pygame and pygame-gui yourself, then run src/main.py'
        )
