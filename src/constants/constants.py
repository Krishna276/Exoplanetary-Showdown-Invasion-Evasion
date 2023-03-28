"""Loads all the constants for the game."""

from json import load

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
    ALIENS = load(aliens)
    GAME_SETTINGS = load(game_settings)
    TILES = load(tiles)
    TURRETS = load(turrets)
