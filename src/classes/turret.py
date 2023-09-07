"""A module that provides the turret class, along with other related things."""

from enum import Enum

from pygame import Rect, RLEACCEL, Surface
from pygame.image import load as load_image
from pygame.sprite import _Group, Sprite

from src.classes.vector import Vector
from src.constants import BF_TILE_LENGTH, TURRETS

class TurretType(Enum):
    """A type of turret."""
    DIRECT = 0
    AOE = 1
    ECON = 2

class Turret(Sprite):
    """A turret on the map."""
    def __init__(self, type: TurretType, position: Vector, *groups: _Group) -> None:
        super().__init__(*groups)
        self.type: TurretType = type
        self.position: Vector = position
        self.surf: Surface = load_image(self.getValue('sprite_path')).convert()
        self.surf.set_colorkey('#00000000', RLEACCEL)
        self.rect: Rect = self.surf.get_rect((position.x * BF_TILE_LENGTH, position.y * BF_TILE_LENGTH))
    
    def update() -> None:
        # I have no idea how I'm going to do this.
        pass
    
    def getValue(self, key: str):
        return TURRETS[self._type.name][key]
