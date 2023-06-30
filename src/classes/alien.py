"""A module that provides the Alien class, along with other related things."""

from enum import Enum

from src.classes.vector import FloatVector
from src.constants import ALIENS

class AlienType(Enum):
    """A type of Alien."""
    DAMAGE = 0
    TANK = 1
    HEALER = 2
    ECON = 3

class Alien:
    """An alien on the map, this stores the details about each alien, like where it is on the map."""
    def __init__(self, type: AlienType, position: FloatVector) -> None:
        self._type: AlienType = type
        self._position: FloatVector = position
        self._health: float = ALIENS[type]['max_health']
    
    @property
    def type(self) -> AlienType:
        return self._type

    @property
    def position(self) -> FloatVector:
        return self._position

    @property
    def health(self) -> float:
        return self._health
    
    def changeHealth(self, health: float) -> None:
        self._health += health
    
    def translate(self, vector: FloatVector) -> None:
        self._position += vector
    
    def get(self, key: str):
        return ALIENS[self._type.name][key]

