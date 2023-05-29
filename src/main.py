"""Exoplanetary Showdown: Invasion Evasion

A game made by CoDerection.

This code is open-source and available on the following GitHub repository:

[Krishna276/Exoplanetary-Showdown-Invasion-Evasion]\
(https://github.com/Krishna276/Exoplanetary-Showdown-Invasion-Evasion)
"""

from sys import path

from constants import ROOT
from game import Game

path.append(ROOT)

def main() -> None:
    """Run the program."""
    game: Game = Game()
    game.play()

if __name__ == '__main__':
    main()
