"""A module that provides the Alien class, along with other related things."""

from enum import Enum
from random import random
from typing import Self

from pygame import Rect, RLEACCEL, Surface
from pygame.event import post as post_event, Event
from pygame.sprite import Sprite
from pygame.transform import scale

from src.classes.grid import Grid
from src.classes.tile import Tile, TileType
from src.classes.vector import FloatVector, Vector, VECTOR_0, VECTOR_i, VECTOR_j
from src.constants import ALIENS, ALIEN_SPEED_MULTIPLIER, BF_TILE_LENGTH, TILES
from src.constants.events import EARTH_DAMAGED
from src.functions.coordinates import convert2grid_vector, convert2pg
from src.functions.directions import getDirection
from src.functions.load_asset import load_image

class AlienType(Enum):
    """A type of Alien."""
    DAMAGE = 0
    TANK = 1
    HEALER = 2
    ECON = 3

class Alien(Sprite):
    """An alien on the map."""
    def __init__(self, type: AlienType, position: FloatVector, path: list[Vector], *groups) -> None:
        super().__init__(*groups)
        self.type: AlienType = type
        self.health: float = self.getValue('max_health')
        self.surf: Surface = scale(load_image(self.getValue('sprite_path')), (BF_TILE_LENGTH, BF_TILE_LENGTH))
        self.surf.set_colorkey('#00000000', RLEACCEL)
        self.rect: Rect = self.surf.get_rect(
            center=tuple(i for i in convert2pg(position) + (BF_TILE_LENGTH // 2) * (VECTOR_i + VECTOR_j))
        )
        self.remainingPath: list[Vector] = path
        self.target: Vector = self.remainingPath[0]
    
    def update(self, dt: int, grid: Grid[Tile]) -> None:
        currentTile: Vector = convert2grid_vector(Vector(self.rect.centerx, self.rect.centery))
        if grid[currentTile].tileType == TileType.DAMAGE:
            self.health -= 1
        if self.health <= 0:
            self.kill()
            return
        direction: Vector | None = getDirection(currentTile, self.remainingPath)
        speedEffect: float = TILES[grid[currentTile].tileType.name]['speed']
        if direction is None:
            post_event(Event(EARTH_DAMAGED, {'damage': self.getValue('damage')}))
            self.kill()
            return
        speed: float = self.getValue('speed') * speedEffect * ALIEN_SPEED_MULTIPLIER
        if speed < 1 and random() < speed:
            speed = 1
        velocity: FloatVector = direction * speed
        self.rect.move_ip(velocity.x * dt / 1000, velocity.y * dt / 1000)


    
    def getValue(self, key: str):
        """Gets a key from the JSON data.

        Args:
            key (str): The key of the value to get.

        Returns:
            Any: The value of that key, as whatever data type it is.
        """
        return ALIENS[self.type.name][key]

