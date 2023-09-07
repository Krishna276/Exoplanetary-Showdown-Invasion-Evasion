"""Implements the Tile class. It also implements the TileType enum."""

from enum import Enum

class TileType(Enum):
    """A type of tile."""
    VACUUM = 0
    EARTH = 1
    PORTAL = 2
    SLOWNESS = 3
    SPEED = 4
    IMMUNITY = 5
    DAMAGE = 6
    NO_TURRET = 7
    NO_ALIEN = 8
    BLOCK = 9

class Tile:
    """A tile on the map."""
    def __init__(self, tileType: TileType = TileType.VACUUM) -> None:
        """A tile on the map.

        Args:
            tileType (TileType): The type of tile to create.
        """
        self._tileType: TileType = tileType
        # Eventually, this will also contain the turret that is placed.
    
    @property
    def tileType(self) -> TileType:
        """The tile's type."""
        return self._tileType
    
    @tileType.setter
    def tileType(self, value: TileType) -> None:
        self._tileType = value
    
