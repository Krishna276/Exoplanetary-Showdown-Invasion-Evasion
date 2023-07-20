"""Module that provides the class that runs the game."""

import pygame
import pygame_gui

from src.constants import ROOT, WINDOW_HEIGHT, WINDOW_WIDTH

class Game:
    """A class that runs the game."""
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        pygame.display.set_caption('Exoplanetary Showdown: Invasion Evasion')
        # pygame.display.set_icon(pygame.image.load(ROOT + GAME_SETTINGS['window']['icon']).convert())
        self.aliens: pygame.sprite.Group = pygame.sprite.Group()
        self.turrets: pygame.sprite.Group = pygame.sprite.Group()
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.ui_manager: pygame_gui.UIManager = pygame_gui.UIManager(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
    
    def _kill(self) -> None:
        self.running = False
    
    def _update(self) -> None:
        dt: int = self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._kill()
            self.ui_manager.process_events(event)
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        self.ui_manager.update(pygame.time.get_ticks())
        self.ui_manager.draw_ui(self.screen)
        pygame.display.flip()
    
    def play(self) -> None:
        while self.running:
            self._update()

