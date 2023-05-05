"""This file generates things like the map."""

from ..classes.grid import Grid
from ..classes.tile import Tile
from ..classes.vector import Vector

def generateMap(width: int, height: int) -> Grid[Tile]:
    """Generated the map.

    Args:
        width (int): Width of the map to generate.
        height (int): Height of the map to generate.

    Returns:
        Grid[Tile]: A Grid object representing the generated map.
    """
    map_ = Grid(Vector(width, height))
    # The rules fofr map generation have not been determined yet.
    # Fill everything with empty space or vacuum tiles.
    # Place the tiles with effects (like slowness). Order and probabilities of these is TBD.
    # Place portal tile(s) (these will likely be determined by a game setting).
    # Place the earth tile (again, probably a game setting).
    return map_
