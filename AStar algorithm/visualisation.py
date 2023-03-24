'''Visualises pathfinding with the A* algorithm.'''

from random import choice, randint
from tkinter import Button, Label, Frame, Tk

from AStar import ArrayGrid, astar, TupleCoords

CHOICES: list = [1, 2, 3, 4, 5, 6, 'N', 'N', 'N']

HEIGHT, WIDTH = 35, 70

def getBg(i: int, j: int):
    if (i, j) in (start, end):
        return '#00FF00'
    match grid[i][j]:
        case 'N':
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

path: list[TupleCoords] | None
grid: ArrayGrid
start: TupleCoords
end: TupleCoords

def generate():
    global path, grid, start, end, pathShown
    path = None
    while path is None:
        grid = [[choice(CHOICES) for j in range(WIDTH)] for i in range(HEIGHT)]
        start = (randint(0, HEIGHT - 1), randint(0, WIDTH - 1))
        end = (randint(0, HEIGHT - 1), randint(0, WIDTH - 1))
        path = astar(start, end, grid)
    pathShown = False

generate()

tk_grid = [[Label(frame, background=getBg(i, j), text='     ') for j in range(WIDTH)] for i in range(HEIGHT)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        tk_grid[i][j].grid(row=i, column=j)

frame.pack()

def show():
    global pathShown
    if pathShown:
        for square in path:
            tk_grid[square[0]][square[1]].config(background=getBg(square[0], square[1]))
    else:
        for square in path:
            tk_grid[square[0]][square[1]].config(background='#00FF00')
    pathShown = not pathShown

Button(tk, text='Show/hide path', command=show).pack()

def reset():
    generate()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            tk_grid[i][j].config(background=getBg(i, j))

Button(tk, text="Reset", command=reset).pack()

tk.mainloop()
