"""Loads all the constants for the game."""

__all__ = [
    'ALIENS', 'GAME_SETTINGS', 'TILES', 'TURRETS', 'ROOT', 'WINDOW_WIDTH', 'WINDOW_HEIGHT', 'BF_SURF_WIDTH',
    'BF_SURF_HEIGHT', 'BF_GRID_WIDTH', 'BF_GRID_HEIGHT', 'BF_TILE_LENGTH'
]

from json import load
from pathlib import Path

ALIENS: dict = {}
GAME_SETTINGS: dict = {}
TILES: dict = {}
TURRETS: dict = {}

ROOT = str(Path(__file__).parent.parent.parent.absolute())

with (
    open(ROOT + '/src/constants/json/aliens.json', 'r', encoding='UTF-8') as aliens,
    open(ROOT + '/src/constants/json/game_settings.json', 'r', encoding='UTF-8') as game_settings,
    open(ROOT + '/src/constants/json/tiles.json', 'r', encoding='UTF-8') as tiles,
    open(ROOT + '/src/constants/json/turrets.json', 'r', encoding='UTF-8') as turrets
):
    ALIENS = load(aliens)
    GAME_SETTINGS = load(game_settings)
    TILES = load(tiles)
    TURRETS = load(turrets)

_scale: float = GAME_SETTINGS['window']['scale']

WINDOW_WIDTH: int = int(GAME_SETTINGS['window']['width'] * _scale)
WINDOW_HEIGHT: int = int(GAME_SETTINGS['window']['height'] * _scale)

BF_GRID_WIDTH: int = GAME_SETTINGS['battlefield']['width']
BF_GRID_HEIGHT: int = GAME_SETTINGS['battlefield']['height']

BF_TILE_LENGTH: int = int(GAME_SETTINGS['battlefield_surface']['tile_length'] * _scale)

BORDER_WIDTH: int = (WINDOW_WIDTH - BF_GRID_WIDTH * BF_TILE_LENGTH) // 2
BORDER_HEIGHT: int = (WINDOW_HEIGHT - BF_GRID_HEIGHT * BF_TILE_LENGTH) // 2

UNKOWN_TEXTURE: str = GAME_SETTINGS['asset_loading']['unkown_texture']
