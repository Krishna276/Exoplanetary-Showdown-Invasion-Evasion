"""A sprite that shows tiles. They don't move."""


from typing import Self
from pygame import Rect, RLEACCEL, Surface
from pygame.sprite import Sprite
from pygame.transform import scale

from src.classes.tile import Tile, TileType
from src.classes.vector import Vector, VECTOR_i, VECTOR_j
from src.constants import BF_TILE_LENGTH, TILES
from src.functions.coordinates import convert2pg
from src.functions.load_asset import load_image

class TileSprite(Sprite):
    """A sprite that represents a tile."""
    def __init__(self: Self, tile: Tile, location: Vector, *groups) -> None:
        """A sprite that represents a tile.

        Args:
            tile (Tile): The tile to represent.
            location (Vector): The tile's location on the grid.
        """
        super().__init__(*groups)
        size: int = BF_TILE_LENGTH * 2 if tile.tileType in {TileType.EARTH, TileType.PORTAL} else BF_TILE_LENGTH
        self.surf: Surface = scale(load_image(TILES[tile.tileType.name]['file']), (size, size))
        self.surf.set_colorkey('#00000000', RLEACCEL)
        self.rect: Rect = self.surf.get_rect(
            center=tuple(i for i in convert2pg(location) + (BF_TILE_LENGTH // 2) * (VECTOR_i + VECTOR_j))
        )
