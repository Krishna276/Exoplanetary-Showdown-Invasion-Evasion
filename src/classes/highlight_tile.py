"""Provides a sprite class that can highlight a tile on the grid."""

from pygame import Surface
from pygame.sprite import Sprite
from pygame.transform import scale

from src.classes.vector import Vector
from src.constants import BF_TILE_LENGTH, GAME_SETTINGS
from src.functions.coordinates import convert2pg
from src.functions.load_asset import load_image

class Highlight(Sprite):
    """A sprite that highlights a tile."""
    def __init__(self, location: Vector, *groups) -> None:
        """A sprite that highlights a tile.

        Args:
            location (Vector): The location to highlight.
        """
        super().__init__(*groups)
        self.surf: Surface = scale(
            load_image(GAME_SETTINGS['battlefield']['tile_highlight_texture']), (BF_TILE_LENGTH, BF_TILE_LENGTH)
        )
        self.surf.set_colorkey('#00000000')
        self.rect = self.surf.get_rect(topleft=tuple(i for i in convert2pg(location)))

