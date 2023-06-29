from time import sleep
from sys import path

path.append(input('Enter root path: '))

from PySimpleGUI import Button, Input, Frame, Text, Window, WIN_CLOSED

from src.classes.tile import TileType
from src.constants import GAME_SETTINGS, TILES
from src.functions.generation import generateMap

WIDTH, HEIGHT = GAME_SETTINGS['battlefield']['width'], GAME_SETTINGS['battlefield']['height']

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

map_, earth, portal = generateMap(WIDTH, HEIGHT, '0')

def getColour(x: int, y: int) -> str:
    return COLOURS[map_[x, y].tileType.value]

last_row = []

for i in range(10):
    last_row.append(Text('    ', background_color=COLOURS[i]))
    last_row.append(Text(TILES[TileType(i).name]['name']))

layout = [
    [Text('Visual Map Generator')],
    [Text('Not part of the actual game, but this is only to visualise the map generation and pathfinding algorithms.')],
    [Frame('Map', [
        [Text('    ', background_color=getColour(j, i), key=f'-{i},{j}-') for j in range(WIDTH)] for i in range(HEIGHT)
    ])],
    [Text('Seed: '), Input('0', key='-seed-'), Button('Generate Map'), Button('Pathfind')],
    [Text('Key:')],
    last_row
]

window: Window = Window('Visual Map Generation', layout=layout)

# Run the PySimpleGUI event loop
while True:
    event, values = window.read()
    if event == WIN_CLOSED:
        break
    elif event == 'Generate Map':
        map_, earth, portal = generateMap(WIDTH, HEIGHT, values['-seed-'])
        for i in range(HEIGHT):
            for j in range(WIDTH):
                window[f'-{i},{j}-'].update(background_color=getColour(j, i))
    elif event == 'Pathfind':
        for coordinates in map_.pathfind(portal, earth):
            window[f'-{coordinates.y},{coordinates.x}-'].update(background_color='#FFFFFF')

# Close the window
window.close()
