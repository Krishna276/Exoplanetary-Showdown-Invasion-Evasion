"""Provides the Vector class."""

from src.classes.exceptions import VectorOutOfBoundsError

class Vector:
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
            self._max_x is not None and (self.x < 0 or self.x >= self._max_x)
            or self._max_y is not None and (self.y < 0 or self.y >= self._max_y)
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

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y}, {self._max_x}, {self._max_y})'

    def __iter__(self):
        yield self.x
        yield self.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self._max_x, self._max_y)
        raise TypeError('A vector may only be added to another vector.')
    
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

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

    def manhattan(self, other) -> int:
        """Calculates the manhattan distance to another vector.
        Args:
            other (GridCoordinates): The location to calculate distance to.
        Returns:
            int: The manhattan discance to the location.
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def s2(self, other) -> int:
        """Calculates the square of the euclidean distance.
        Args:
            other (GridCoordinates): The location to calculate displacement to.
        Returns:
            int: The square of the displacemenet to other.
        """
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

class FloatVector:
    """A 2-D vector that can have float values in it, though it cannot be used to index a grid."""
    def __init__(self, x: float, y: float, max_x: int | None = None, max_y: int | None = None) -> None:
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
    
    @property
    def _outOfBounds(self) -> bool:
        if (
            self._max_x is not None and (self.x < 0 or self.x >= self._max_x)
            or self._max_y is not None and (self.y < 0 or self.y >= self._max_y)
        ):
            return True
        return False
    
    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float) -> None:
        self._x = value
    
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float) -> None:
        self._y = value
    
    def __repr__(self) -> str:
        return f'FloatVector({self.x}, {self.y}, {self._max_x}, {self._max_y})'
    
    def __iter__(self):
        yield self.x
        yield self.y
    
    def __add__(self, other):
        if isinstance(other, FloatVector):
            return FloatVector(self.x + other.x, self.y + other.y, self._max_x, self._max_y)
        raise ValueError('A float vector may only be added to another float vector.')
    
    def __neg__(self):
        return FloatVector(-self.x, -self.y)


VECTOR_i: Vector = Vector(1, 0)
VECTOR_j: Vector = Vector(0, 1)

FLOATVECTOR_i: FloatVector = FloatVector(1, 0)
FLOATVECTOR_j: FloatVector = FloatVector(0, 1)
