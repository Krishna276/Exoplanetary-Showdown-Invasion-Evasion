"""A module that provides the turret class, along with other related things."""

from enum import Enum

from src.classes.vector import Vector
from src.constants import TURRETS

class TurretType(Enum):
    """A type of turret."""
    DIRECT = 0
    AOE = 1
    ECON = 2

class Turret:
    """Stores details about turrets."""
    def __init__(self, type: TurretType, position: Vector):
        self._type: TurretType = type
        self._position: Vector = position

    @property
    def type(self) -> TurretType:
        return self._type
    
    @property
    def position(self) -> Vector:
        return self._position
    
    @property
    def name(self) -> str:
        return self._getKey('name')
    
    @property
    def damage(self) -> float:
        return self._getKey('damage')
    
    @property
    def speed(self) -> float:
        return self._getKey('speed')
    
    @property
    def cost(self) -> int:
        return self._getKey('cost')
    
    @property
    def range(self) -> float:
        return self._getKey('range')
    
    @property
    def income(self) -> int:
        return self._getKey('income')
    
    def _getKey(self, key: str):
        return TURRETS[self._type.name][key]
