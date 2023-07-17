"""Module that runs the game, including all top-level gameplay functions and managing things like sprites."""

import pygame
import pygame_gui

from constants import GAME_SETTINGS, ROOT

class Game:
    """A class that runs the game."""
    def __init__(self) -> None:
        pygame.init()
        scale: float = 0
        self.window_width: int = int(GAME_SETTINGS['window']['width'] * scale)
        self.window_height: int = int(GAME_SETTINGS['window']['height'] * scale)
        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )
        pygame.display.set_caption('Exoplanetary Showdown: Invasion Evasion')
        # pygame.display.set_icon(pygame.image.load(ROOT + GAME_SETTINGS['window']['icon']).convert())
        self.aliens: pygame.sprite.Group = pygame.sprite.Group()
        self.turrets: pygame.sprite.Group = pygame.sprite.Group()
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.ui_manager: pygame_gui.UIManager = pygame_gui.UIManager(
            (self.window_width, self.window_height)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
    
    def _kill(self) -> None:
        self.running = False
    
    def play(self) -> None:
        while self.running:
            self._loop()

    def _loop(self) -> None:
        dt: int = self.clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._kill()
            self.ui_manager.process_events(event)
        self.ui_manager.update(pygame.time.get_ticks())
        self.ui_manager.draw_ui(self.screen)
        pygame.display.flip()

