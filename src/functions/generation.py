"""This file generates things like the map."""

from src.classes.grid import Grid
from src.classes.tile import Tile
from src.classes.vector import Vector

def generateMap(width: int, height: int) -> Grid[Tile]:
    """Generates the map.

    Args:
        width (int): Width of the map to generate.
        height (int): Height of the map to generate.

    Returns:
        Grid[Tile]: A Grid object representing the generated map.
    """
    map_: Grid[Tile] = Grid[Tile](Vector(width, height))
    # The rules for map generation have not been determined yet.
    # Fill everything with empty space or vacuum tiles.
    for i in range(height):
        for j in range(width):
            map_[i, j] = Tile()
    # Place the tiles with effects (like slowness). Order and probabilities of these is TBD.
    # Place portal tile(s) (these will likely be determined by a game setting).
    # Place the earth tile (again, probably a game setting).
    return map_
