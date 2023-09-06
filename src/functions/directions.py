"""A module that provides directions at any given instant in time for aliens."""

from src.classes.vector import Vector

def getDirection(currentTileCoords: Vector, path: list[Vector]) -> Vector | None:
    """Given a path to follow and current precise location, get the direction to go next.

    Args:
        location (FloatVector): The precise location of the alien.
        path (list[Vector]): The path the alien has to follow.

    Returns:
        Vector | None: Returns a vector of the direction to go in, or None if it it at the end of the path (Earth).
    """
    try:
        nextTileCoords: Vector = path[path.index(currentTileCoords) + 1]
    except IndexError:
        return None
    else:
        return nextTileCoords - currentTileCoords
