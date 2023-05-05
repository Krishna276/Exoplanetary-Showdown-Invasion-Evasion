"""Implements the Tile class. It also implements the TileType enum."""

from enum import Enum

class TileType(Enum):
    """An enum of the tile type."""
    VACUUM = 0
    EARTH = 1
    PORTAL = 2
    SLOW = 3
    SPEED = 4
    NO_DAMAGE = 5
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
        # self._turret: Turret | None = None
    
    @property
    def tileType(self) -> TileType:
        """The tile's type."""
        return self._tileType
    
    @tileType.setter
    def tileType(self, value: TileType) -> None:
        self._tileType = value
    
