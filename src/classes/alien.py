"""A module that provides the Alien class, along with other related things."""

from enum import Enum

import pygame

from src.classes.vector import FloatVector, Vector
from src.constants import ALIENS

class AlienType(Enum):
    """A type of Alien."""
    DAMAGE = 0
    TANK = 1
    HEALER = 2
    ECON = 3

class Alien(pygame.sprite.Sprite):
    """An alien on the map."""
    def __init__(self, type: AlienType, position: FloatVector, *groups) -> None:
        super().__init__(*groups)
        self.type: AlienType = type
        self.health: float = self.getValue('max_health')
        self.surf: pygame.Surface = pygame.image.load(self.getValue('sprite_path')).convert()
        self.surf.set_colorkey('#00000000', pygame.RLEACCEL)
        self.rect = self.surf.get_rect(center=(position.x, position.y))
    
    def update(self, dt: int, path: ) -> None:
        pass

    
    def getValue(self, key: str):
        """Gets a key from the JSON data.

        Args:
            key (str): The key of the value to get.

        Returns:
            Any: The value of that key, as whatever data type it is.
        """
        return ALIENS[self._type.name][key]

