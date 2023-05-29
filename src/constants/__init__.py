"""Loads all the constants for the game."""

__all__ = ['ALIENS', 'GAME_SETTINGS', 'TILES', 'TURRETS', 'ROOT']

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
