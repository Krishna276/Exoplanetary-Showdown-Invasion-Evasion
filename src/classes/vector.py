"""Provides the Vector classes.

Type conversion rules for binary operators on vectors:

The following will return a FloatVector:
* Binary operations involving at least one FloatVector
* Multiplication of a Vector by a float
* True division operations

In all other cases, a Vector object is returned.

Note that these vector classes only support scalar multiplication.
"""

from abc import ABC, abstractmethod
from typing import Self

from src.classes.exceptions import VectorOutOfBoundsError

class _BaseVector(ABC):
    """Common base class for all Vectors."""
    def __init__(self) -> None:
        self._x: int
        self._y: int
        self._max_x: int
        self._max_y: int
    
    def __iter__(self):
        yield self._x
        yield self._y

    def __eq__(self, other: object) -> bool:
        if type(other) != type(self):
            return False
        return self._x == other.x and self._y == other.y
    
    
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return FloatVector(self._x / other, self._y / other, self._max_x, self._max_y)
        raise TypeError('Vector objects only support division by ints or floats.')

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass

    @abstractmethod
    def __neg__(self):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __floordiv__(self, other):
        pass

    @abstractmethod
    def __mod__(self, other):
        pass

    @abstractmethod
    def s2(self, other):
        pass

class Vector(_BaseVector):
    """A 2-D vector, a set of x and y coordinates."""
    def __init__(self, x: int, y: int, max_x: int | None = None, max_y: int | None = None) -> None:
        """A 2-D vector, a set of x and y coordinates.
        Args:
            x (int): The x-component of the vector.
            y (int): The y-component of the vector.
            max_x (int | None, optional): The maximum value x can take. Defaults to None.
            max_y (int | None, optional): The maximum value y can take. Defaults to None.
        """
        self._max_x: int | None = max_x
        self._max_y: int | None = max_y
        self._x: int = x
        # Using the setter here allows us to check for out of bounds automatically.
        self.y = y

    @property
    def _outOfBounds(self) -> bool:
        if (
            self._max_x is not None and (self._x < 0 or self._x >= self._max_x)
            or self._max_y is not None and (self._y < 0 or self._y >= self._max_y)
        ):
            return True
        return False

    @property
    def x(self) -> int:
        """The x-component of the vector."""
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x
        if self._outOfBounds:
            raise VectorOutOfBoundsError('Coordinates are out of bounds')

    @property
    def y(self) -> int:
        """The y-component of the vector."""
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y
        if self._outOfBounds:
            raise VectorOutOfBoundsError('Coordinates are out of bounds.')
    
    @property
    def max_x(self) -> int:
        return self._max_x
    
    @property
    def max_y(self) -> int:
        return self._max_y

    def __repr__(self) -> str:
        return f'Vector({self._x}, {self._y}, {self._max_x}, {self._max_y})'

    def __hash__(self) -> int:
        return hash((self._x, self._y))

    def __add__(self, other) -> Self:
        if isinstance(other, Vector):
            return Vector(self._x + other.x, self._y + other.y, self._max_x, self._max_y)
        elif isinstance(other, FloatVector):
            return FloatVector(self._x + other.x, self._y + other.y, self._max_x, self._max_y)
        raise TypeError('A vector may only be added to another vector.')
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self._x * other, self._y * other, self._max_x, self._max_y)
        elif isinstance(other, float):
            return FloatVector(self._x * other, self._y * other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector multiplication are ints and floats.')
    
    def __rmul__(self, other) -> Self:
        return self * other
    
    def __neg__(self) -> Self:
        return Vector(-self._x, -self._y)
    
    def __sub__(self, other) -> Self:
        return self + -other
    
    def __floordiv__(self, other):
        if isinstance(other, int):
            return Vector(self._x // other, self._y // other, self._max_x, self._max_y)
        elif isinstance(other, float):
            return FloatVector(self._x // other, self._y // other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector division are ints and floats.')
    
    def __mod__(self, other):
        if isinstance(other, int):
            return Vector(self._x % other, self._y % other, self._max_x, self._max_y)
        elif isinstance(other, float):
            return FloatVector(self._x % other, self._y % other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector division are ints and floats.')

    @staticmethod
    def fromTuple(t: tuple[int, int], max_x: int | None = None, max_y: int | None = None):
        """Creates a vector object from a tuple.
        Args:
            t (tuple[int, int]): The tuple to create a vector from.
            max_x (int | None, optional): The value to set max_x to. Defaults to None.
            max_y (int | None, optional): The value to set max_y to. Defaults to None.
        Returns:
            Vector: The vector generated form the tuple.
        """
        return Vector(t[0], t[1], max_x, max_y)

    def manhattan(self, other: Self) -> int:
        """Calculates the manhattan distance to another vector.
        Args:
            other (Self): The location to calculate distance to.
        Returns:
            int: The manhattan discance to the location.
        """
        return abs(self._x - other.x) + abs(self._y - other.y)

    def s2(self, other: Self) -> int:
        """Calculates the square of the euclidean distance.
        Args:
            other (Self): The location to calculate displacement to.
        Returns:
            int: The square of the displacemenet to other.
        """
        return (self._x - other.x) ** 2 + (self._y - other.y) ** 2

class FloatVector(_BaseVector):
    """A 2-D vector that can have float values in it, though it cannot be used to index a grid."""
    def __init__(self, x: float, y: float, max_x: float | None = None, max_y: float | None = None) -> None:
        """A 2-D vector that can have float values in it, though it cannot be used to index a grid.

        Args:
            x (float): The x component.
            y (float): The y component.
            max_x (int, optional): The maximum value of x. Defaults to None.
            max_y (int, optional): The maximum value of y. Defaults to None.
        """
        self._max_x: float | None = max_x
        self._max_y: float | None = max_y
        self._x: float = x
        # Using the setter here allows us to check for out of bounds automatically.
        self.y = y

    @staticmethod
    def fromVector(vector: Vector) -> Self:
        return FloatVector(vector.x, vector.y, vector.max_x, vector.max_y)
    
    def toVector(self) -> Vector:
        return Vector(int(self._x), int(self._y), int(self._max_x), int(self._max_y))
    
    @property
    def _outOfBounds(self) -> bool:
        if (
            self._max_x is not None and (self._x < 0 or self._x >= self._max_x)
            or self._max_y is not None and (self._y < 0 or self._y >= self._max_y)
        ):
            return True
        return False
    
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, x: float) -> None:
        self._x = x
        if self._outOfBounds:
            raise VectorOutOfBoundsError('Coordinates are out of bounds')
    
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, y: float) -> None:
        self._y = y
        if self._outOfBounds:
            raise VectorOutOfBoundsError('Coordinates are out of bounds')
    
    @property
    def max_x(self) -> float:
        return self._max_x
    
    @property
    def max_y(self) -> float:
        return self._max_y
    
    def __repr__(self) -> str:
        return f'FloatVector({self._x}, {self._y}, {self._max_x}, {self._max_y})'
    
    def __add__(self, other) -> Self:
        if isinstance(other, _BaseVector):
            return FloatVector(self._x + other.x, self._y + other.y, self._max_x, self._max_y)
        raise TypeError('A float vector may only be added to another float vector.')
    
    def __mul__(self, other) -> Self:
        if isinstance(other, (float, int)):
            return FloatVector(self._x * other, self._y * other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector multiplication are integers or floats.')
    
    def __rmul__(self, other):
        return self * other
    
    def __neg__(self) -> Self:
        return FloatVector(-self._x, -self._y)
    
    def __sub__(self, other) -> Self:
        return self + -other
    
    def __floordiv__(self, other) -> Self:
        if isinstance(other, (float, int)):
            return FloatVector(self._x // other, self._y // other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector division are integers or floats.')
    
    def __mod__(self, other) -> Self:
        if isinstance(other, (float, int)):
            return FloatVector(self._x % other, self._y % other, self._max_x, self._max_y)
        raise TypeError('The only supported types for vector division are integers or floats.')
    
    def s2(self, other: Self) -> float:
        """Calculates the square of the euclidean distance.
        Args:
            other (Self): The location to calculate displacement to.
        Returns:
            float: The square of the displacemenet to other.
        """
        return (self._x - other.x) ** 2 + (self._y - other.y) ** 2


VECTOR_i: Vector = Vector(1, 0)
VECTOR_j: Vector = Vector(0, 1)
VECTOR_0: Vector = Vector(0, 0)

FLOATVECTOR_i: FloatVector = FloatVector(1.0, 0.0)
FLOATVECTOR_j: FloatVector = FloatVector(0.0, 1.0)
FLOATVECTOR_0: FloatVector = FloatVector(0.0, 0.0)
