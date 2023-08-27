"""Exoplanetary Showdown: Invasion Evasion

A game made by CoDerection.

This code is distributed open-source and available on the following GitHub repository:

[Krishna276/Exoplanetary-Showdown-Invasion-Evasion]\
(https://github.com/Krishna276/Exoplanetary-Showdown-Invasion-Evasion)
"""

from sys import path

from constants import ROOT

path.append(ROOT)

from game import Game

def main() -> None:
    """Run the program."""
    game: Game = Game()
    game.play()

if __name__ == '__main__':
    main()
