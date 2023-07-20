from sys import path

path.append(input('Enter repo root path: '))

from PySimpleGUI import Button, Input, Frame, Text, Window, WIN_CLOSED

from src.classes.tile import TileType
from src.constants import BF_GRID_HEIGHT, BF_GRID_WIDTH, TILES
from src.functions.generation import generateMap

COLOURS = [
    '#555555',
    '#0000AA',
    '#AAAAAA',
    '#5555FF',
    '#FFFF55',
    '#00AA00',
    '#AA0000',
    '#55FF55',
    '#FF5555',
    '#000000'
]

# PySimpleGUI.theme(theme: str) to change theme

map_, earth, portal = generateMap(BF_GRID_WIDTH, BF_GRID_HEIGHT, '')

def getColour(x: int, y: int) -> str:
    return COLOURS[map_[x, y].tileType.value]

def compliment(hex_color: str) -> str:
    return '#%02X%02X%02X' % tuple(255 - i for i in tuple(int(hex_color[i:i + 2], 16) for i in range(1, 7, 2)))

layout = [
    [Text('Visual Map Generator')],
    [Text('Not part of the actual game, but this is only to visualise the map generation and pathfinding algorithms.')],
    [Frame('Map', [[
        Text('    ', background_color=getColour(j, i), key=f'-{i},{j}-') for j in range(BF_GRID_WIDTH)
    ] for i in range(BF_GRID_HEIGHT)])],
    [Text('Seed: '), Input('', key='-seed-'), Button('Generate Map'), Button('Pathfind')],
    [Text('Key:')] + [Text(
        TILES[TileType(i).name]['name'], background_color=COLOURS[i], text_color=compliment(COLOURS[i])
    ) for i in range(10)]
]

# Create a PySimpleGUI window
window: Window = Window('Visual Map Generation', layout=layout)

# Run the PySimpleGUI event loop
while True:
    event, values = window.read()
    if event == WIN_CLOSED:
        break
    elif event == 'Generate Map':
        map_, earth, portal = generateMap(BF_GRID_WIDTH, BF_GRID_HEIGHT, values['-seed-'])
        for i in range(BF_GRID_HEIGHT):
            for j in range(BF_GRID_WIDTH):
                window[f'-{i},{j}-'].update(background_color=getColour(j, i))
    elif event == 'Pathfind':
        for coordinates in map_.pathfind(portal, earth):
            window[f'-{coordinates.y},{coordinates.x}-'].update(background_color='#FFFFFF')

# Close the window
window.close()
