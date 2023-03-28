"""Implements the Grid class."""

from heapq import heappop, heappush
from typing import Generic, TypeVar

_T = TypeVar('_T')
_Cost = int | None

class VectorOutOfBoundsError(Exception):
    """A vector is out of bounds."""

class Vector:
    """A 2-D vector, a set of x and y coordinates."""
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

    def __init__(self, x: int, y: int, max_x: int | None = None, max_y: int | None = None) -> None:
        """A 2-D vector, a set of x and y coordinates.

        Args:
            x (int): The x-component of the vector.
            y (int): THe y-component of the vector.
            max_x (int | None, optional): The maximum value x can take. Defaults to None.
            max_y (int | None, optional): The maximum value y can take. Defaults to None.
        """
        self._max_x: int | None = max_x
        self._max_y: int | None = max_y
        self._x: int = x
        self.y = y

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

class _Node(Generic[_T]):
    """A node on the graph."""
    def __init__(self, data: _T, cost: _Cost) -> None:
        self.data: _T = data
        self.cost: _Cost = cost

class Grid(Generic[_T]):
    """An abstract data type representing the battlefield where all the runners run and turrets go."""
    def __init__(self, size: Vector) -> None:
        """An abstract data type representing the battlefield where all the runners run and turrets go.

        Args:
            size (Vector): The dimensions of the grid to create.
        """
        self._grid: list[list[_Node[_T] | None]] = [[None for _ in range(size.x)] for _ in range(size.y)]
        self._width: int = size.x
        self._height: int = size.y
    
    def __getitem__(self, coords: Vector) -> _T:
        return self._grid[coords.y][coords.x].data
    
    def __setitem__(self, coords: Vector, value: tuple[_T, _Cost]) -> None:
        if self._grid[coords.y][coords.x] is not None:
            self._grid[coords.y][coords.x].data, self._grid[coords.y][coords.x].cost = value
        else:
            self._grid[coords.y][coords.x] = _Node[_T](value[0], value[1])
    
    def __iter__(self):
        self._iter_x: int = -1
        self._iter_y: int = -1
        return self
    
    def __next__(self) -> _T:
        self._iter_x = (self._iter_x + 1) % self.width
        if self._iter_x == 0:
            self._iter_y = (self._iter_y + 1) % self.height
        return self._iter_y, self._iter_x, self[Vector(self._iter_x, self._iter_y)]
    
    @property
    def width(self) -> int:
        """How wide the grid is."""
        return self._width
    
    @property
    def height(self) -> int:
        """How tall the grid is."""
        return self._height
    
    def _getCost(self, coords: Vector) -> _Cost:
        return self._grid[coords.y][coords.x].cost
    
    def pathfind(self, start: Vector, end: Vector) -> list[Vector] | None:
        """Uses an A* search to find the path of least resistance.

        Args:
            start (Vector): The location to pathfind from.
            end (Vector): The location to pathfind to.

        Returns:
            list[Vector] | None: The path of least resistance.
        """
        open_set: list[tuple[int, Vector]] = []
        closed_set: set = set()
        heappush(open_set, (0, tuple(start)))
        g_score: dict[Vector, int] = {start: 0}
        f_score: dict[Vector, int] = {start: start.manhattan(end)}
        previous_nodes: dict[Vector, Vector | None] = {start: None}

        while open_set:
            current: Vector | None = Vector.fromTuple(heappop(open_set)[1], self.width, self.height)

            if current == end:
                path: list[Vector] = []
                while current is not None:
                    path.append(current)
                    current = previous_nodes[current]
                path.reverse()
                return path
            
            closed_set.add(current)

            for neighbor in Vector(1, 0), Vector(0, 1), Vector(-1, 0), Vector(0, -1):
                try:
                    next_: Vector = current + neighbor
                except VectorOutOfBoundsError:
                    continue
                if next_ in closed_set or self._getCost(next_) is None:
                    continue
                tentative_g_score = g_score[current] + self._getCost(next_)
                if next_ in g_score and tentative_g_score >= g_score[next_]:
                    continue
                g_score[next_] = tentative_g_score
                f_score[next_] = tentative_g_score + next_.manhattan(end)
                previous_nodes[next_] = current
                heappush(open_set, (f_score[next_], tuple(next_)))
        return None

