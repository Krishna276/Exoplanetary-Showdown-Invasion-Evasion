"""This only visualises the grid, it is not part of the actual game."""

from random import choice, randint
from tkinter import Button, Label, Frame, Tk

from classes.grid import Grid
from classes.vector import Vector

CHOICES = [1, 2, 3, 4, 5, 6, None, None, None]

HEIGHT, WIDTH = 35, 70

def getBg(i: int, j: int) -> str:
    """Gets the colour of a square.

    Args:
        i (int): The y-coordinate.
        j (int): The x-coordinate.

    Returns:
        str: A hex code of the colour.
    """
    if Vector(j, i) in (start, end):
        return '#00FF00'
    match grid[Vector(j, i, WIDTH, HEIGHT)]:
        case None:
            return '#FF0000'
        case 1:
            return '#0000FF'
        case 2:
            return '#0000DF'
        case 3:
            return '#0000BF'
        case 4:
            return '#00009F'
        case 5:
            return '#00007F'
        case 6:
            return '#00005F'
        case _:
            return '#FFFFFF'

tk: Tk = Tk()
frame: Frame = Frame(tk)

_path: list[Vector] | None
grid: Grid[int]
start: Vector
end: Vector
pathShown: bool

def generate() -> None:
    """Generates the maze."""
    global _path, grid, start, end, pathShown
    _path = None
    while _path is None:
        grid = Grid[int](Vector(WIDTH, HEIGHT))
        for i in range(HEIGHT):
            for j in range(WIDTH):
                weight: int = choice(CHOICES)
                grid[Vector(j, i)] = weight, weight
        start = Vector(randint(0, WIDTH - 1), randint(0, HEIGHT - 1), WIDTH, HEIGHT)
        end = Vector(randint(0, WIDTH - 1), randint(0, HEIGHT - 1), WIDTH, HEIGHT)
        _path = grid.pathfind(start, end)
    pathShown = False

generate()

tk_grid = [[Label(frame, background=getBg(i, j), text='     ') for j in range(WIDTH)] for i in range(HEIGHT)]

for i in range(HEIGHT):
    for j in range(WIDTH):
        tk_grid[i][j].grid(row=i, column=j)

frame.pack()

def show() -> None:
    """Show the path."""
    global pathShown
    if pathShown:
        for square in _path:
            tk_grid[square.y][square.x].config(background=getBg(square.y, square.x))
    else:
        for square in _path:
            tk_grid[square.y][square.x].config(background='#00FF00')
    pathShown = not pathShown

Button(tk, text='Show/hide path', command=show).pack()

def reset():
    """Reset the maze challenge."""
    generate()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            tk_grid[i][j].config(background=getBg(i, j))

Button(tk, text="Reset", command=reset).pack()

tk.mainloop()

