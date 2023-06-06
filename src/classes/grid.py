"""Implements the Grid class."""

from functools import singledispatchmethod
from heapq import heappop, heappush
from typing import Generic, TypeVar

from src.classes.exceptions import VectorOutOfBoundsError
from src.classes.vector import Vector

__all__ = ['Grid']

_T = TypeVar('_T')
_Cost = int | None

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

    @singledispatchmethod
    def __getitem__(self, index) -> _T:
        raise TypeError('You need to specity a Vector or tuple of coordinates to index a grid.')
    
    @__getitem__.register
    def _(self, coords: Vector) -> _T:
        return self._grid[coords.y][coords.x].data
    
    @__getitem__.register
    def _(self, coords: tuple) -> _T:
        if len(coords) != 2:
            raise ValueError('Only two coordinates are allowed.')
        if not isinstance(coords[0], int) or not isinstance(coords[1], int):
            raise TypeError('Coordinates passed in are not integers.')
        return self[Vector(coords[0], coords[1], self.width, self.height)]

    @singledispatchmethod
    def __setitem__(self, index, value) -> None:
        raise TypeError('You need to specity a Vector or tuple of coordinates to index a grid.')

    @__setitem__.register
    def _(self, coords: Vector, value: tuple[_T, _Cost]) -> None:
        if self._grid[coords.y][coords.x] is not None:
            self._grid[coords.y][coords.x].data, self._grid[coords.y][coords.x].cost = value
        else:
            self._grid[coords.y][coords.x] = _Node[_T](value[0], value[1])
    
    @__setitem__.register
    def _(self, coords: tuple[int, int], value: tuple[_T, _Cost]) -> None:
        if len(coords) != 2:
            raise ValueError('Only two coordinates are allowed.')
        if not isinstance(coords[0], int) or not isinstance(coords[1], int):
            raise TypeError('Coordinates passed in are not integers.')
        self[Vector(coords[0], coords[1], self.width, self.height)] = value

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
            list[Vector] | None: The path of least resistance, as a list of the next squares to go to.
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
                return path[::-1]

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

