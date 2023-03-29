"""Loads all the constants for the game."""

from json import load as _load
from pathlib import Path as _Path

__all__ = ['ALIENS', 'GAME_SETTINGS', 'TILES', 'TURRETS']

ALIENS: dict = {}
GAME_SETTINGS: dict = {}
TILES: dict = {}
TURRETS: dict = {}

_path = str(_Path(__file__).parent.absolute())

with (
    open(_path + '/json/aliens.json', 'r') as aliens,
    open(_path + '/json/game_settings.json', 'r') as game_settings,
    open(_path + '/json/tiles.json', 'r') as tiles,
    open(_path + '/json/turrets.json', 'r') as turrets
):
    ALIENS = _load(aliens)
    GAME_SETTINGS = _load(game_settings)
    TILES = _load(tiles)
    TURRETS = _load(turrets)
