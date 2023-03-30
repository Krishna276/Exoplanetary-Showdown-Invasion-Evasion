"""Loads all the constants for the game."""
from json import load
from pathlib import Path 

__all__ = ['ALIENS', 'GAME_SETTINGS', 'TILES', 'TURRETS', 'REPO_PATH']

ALIENS: dict = {}
GAME_SETTINGS: dict = {}
TILES: dict = {}
TURRETS: dict = {}

REPO_PATH = str(Path(__file__).parent.parent.parent.absolute())

with (
    open(REPO_PATH + '/src/constants/json/aliens.json', 'r') as aliens,
    open(REPO_PATH + '/src/constants/json/game_settings.json', 'r') as game_settings,
    open(REPO_PATH + '/src/constants/json/tiles.json', 'r') as tiles,
    open(REPO_PATH + '/src/constants/json/turrets.json', 'r') as turrets
):
    ALIENS = load(aliens)
    GAME_SETTINGS = load(game_settings)
    TILES = load(tiles)
    TURRETS = load(turrets)
