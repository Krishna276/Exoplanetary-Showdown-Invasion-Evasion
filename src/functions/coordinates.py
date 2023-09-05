"""Allows the two coordinate systems used in this game to co-exist."""

from src.classes.vector import Vector, FloatVector
from src.constants import BF_TILE_LENGTH, BORDER_HEIGHT, BORDER_WIDTH

_offset: Vector = Vector(BORDER_WIDTH, BORDER_HEIGHT)

def convert2pg(coords: Vector | FloatVector) -> Vector:
    """Converts from the grid coordinates to on-screen pygame coordinates.

    Args:
        coords (Vector): Grid coordinates.

    Returns:
        Vector: On-screen pygame coordinates.
    """
    result = coords * BF_TILE_LENGTH + _offset
    if isinstance(result, FloatVector):
        return result.toVector()
    return result

def convert2grid(coords: Vector) -> FloatVector:
    """Converts from on-screen pygame coordinates to grid coordinates.

    Args:
        coords (Vector): On-screen pygame coordinates.

    Returns:
        FloatVector: Grid coordinates.
    """
    return (coords - _offset) / BF_TILE_LENGTH

def convert2grid_vector(coords: Vector) -> Vector:
    """Converts to grid coordinates, but rounds both values down, so returns a Vector.
    This can be used an an index in the grid.

    Args:
        coords (Vector): The on-screen coordinates.

    Returns:
        Vector: Grid index (integer coordinates of a tile).
    """
    return convert2grid(coords).toVector()
