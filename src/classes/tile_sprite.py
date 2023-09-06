"""A sprite that shows tiles. They don't move."""

from pygame import Rect, RLEACCEL, Surface
from pygame.sprite import Sprite

from src.classes.tile import Tile
from src.classes.vector import Vector
from src.constants import TILES
from src.functions.coordinates import convert2pg
from src.functions.load_asset import load_image

class TileSprite(Sprite):
    """A sprite that represents a tile."""
    def __init__(self, tile: Tile, location: Vector, *groups) -> None:
        super().__init__(*groups)
        self.surf: Surface = load_image(TILES[tile.tileType.name]['file'])
        self.surf.set_colorkey('#00000000', RLEACCEL)
        self.rect: Rect = self.surf.get_rect(topleft=tuple(i for i in convert2pg(location)))
