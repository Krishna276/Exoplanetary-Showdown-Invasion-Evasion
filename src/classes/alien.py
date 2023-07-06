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
        self._health: float = self.max_health
    
    @property
    def type(self) -> AlienType:
        return self._type

    @property
    def position(self) -> FloatVector:
        return self._position

    @property
    def health(self) -> float:
        return self._health
    
    @property
    def name(self) -> str:
        return self._getKey('name')
    
    @property
    def damage(self) -> float:
        return self._getKey('damage')
    
    @property
    def max_health(self) -> float:
        return self._getKey('max_health')
    
    @property
    def speed(self) -> float:
        return self._getKey('speed')
    
    @property
    def cost(self) -> int:
        return self._getKey('cost')
    
    @property
    def income(self) -> int:
        return self._getKey('income')
    
    @property
    def healing(self) -> bool:
        return self._getKey('healing')
    
    def _getKey(self, key: str):
        return ALIENS[self._type.name][key]
    
    def changeHealth(self, health: float) -> None:
        """Damage the alien or heal it.

        Args:
            health (float): How much the health should change by, use a negative number to damage them.
        """
        self._health += health
    
    def translate(self, vector: FloatVector) -> None:
        """Move the alien.

        Args:
            vector (FloatVector): The vector to translate by.
        """
        self._position += vector

