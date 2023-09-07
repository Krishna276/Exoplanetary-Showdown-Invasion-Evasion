"""Loads assets into the game and handles any errors that arise."""

from pygame import Surface
from pygame.image import load as load_pygame_image

from constants import ROOT, UNKOWN_TEXTURE

def load_image(path: str) -> Surface:
    """Attempts to load an image asset, otherwise gives an unkown texture.

    Args:
        path (str): The relative file path to attempt to load, from the repository's root.

    Returns:
        Surface: A pygame Surface (this function is a wrapper for pygame.image.load).
    """
    try:
        return load_pygame_image(ROOT + path).convert()
    except FileNotFoundError:
        return load_pygame_image(ROOT + UNKOWN_TEXTURE).convert()

