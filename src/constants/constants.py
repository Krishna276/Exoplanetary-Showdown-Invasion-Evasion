"""Loads all the constants for the game."""

from json import load as _load

ALIENS: dict = {}
GAME_SETTINGS: dict = {}
TILES: dict = {}
TURRETS: dict = {}

with (
    open('constants/aliens.json', 'r') as aliens,
    open('constants/game_settings.json') as game_settings,
    open('constants/tiles.json') as tiles,
    open('constants/turrets.json') as turrets
):
    ALIENS = _load(aliens)
    GAME_SETTINGS = _load(game_settings)
    TILES = _load(tiles)
    TURRETS = _load(turrets)
