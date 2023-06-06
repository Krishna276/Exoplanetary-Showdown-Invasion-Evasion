"""This file generates things like the map."""

from random import Random

from src.classes.grid import Grid
from src.classes.tile import Tile, TileType
from src.classes.vector import Vector
from src.constants import TILES

random: Random = Random()

def _randBinomial(n: int, p: float) -> int:
    """Generates a random numver following the distribution B(n, p)

    Args:
        n (int): The number of trials.
        p (float): The probability of a successful trial.

    Raises:
        ValueError: When n or p are invalid for a Binomial distribution.

    Returns:
        int: The number of successful trials.
    """
    if n < 0 or p < 0.0 or p > 1.0:
        raise ValueError('n must be a whole number, and p must be in the interval [0, 1]')
    return sum([random.random() < p for _ in range(n)])

def generateMap(width: int, height: int) -> Grid[Tile]:
    """Generates the map.

    Args:
        width (int): Width of the map to generate.
        height (int): Height of the map to generate.

    Returns:
        Grid[Tile]: A Grid object representing the generated map.
    """
    map_: Grid[Tile] = Grid[Tile](Vector(width, height))
    # Fill everything with empty space or vacuum tiles.
    for i in range(height):
        for j in range(width):
            map_[i, j] = Tile()
    # Place the earth tile, it should have an expected value of about 90% of the width of the screen.
    # It should generate near the middle of the column.
    map_[_randBinomial(width, 0.9), _randBinomial(height, 0.5)].tileType = TileType.EARTH, TILES[TileType.EARTH]['cost']
    # The mothership should follow a similar distribution, but be skewed to the left.
    return map_

generateMap(10, 10)
