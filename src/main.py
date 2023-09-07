"""Exoplanetary Showdown: Invasion Evasion

A game made by CoDerection.

This code is distributed open-source and available on the following GitHub repository:

[Krishna276/Exoplanetary-Showdown-Invasion-Evasion]\
(https://github.com/Krishna276/Exoplanetary-Showdown-Invasion-Evasion)
"""

from sys import argv, path

from constants import ROOT

path.append(ROOT)

from game import Game

def main() -> None:
    """Run the program."""
    seed: str | None = None
    while argv:
        option: str = argv.pop(0)
        if option == '-s':
            seed = argv.pop(0)
    game: Game = Game(seed)
    game.play()

if __name__ == '__main__':
    try:
        main()
    finally:
        print('Program Terminated.')
