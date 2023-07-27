"""Module that provides the class that runs the game."""

from pygame import init as init_pygame, Surface, QUIT
from pygame.display import flip as flip_display, set_caption, set_icon, set_mode
from pygame.event import get
from pygame.image import load as load_image
from pygame.sprite import Group
from pygame.time import Clock, get_ticks
from pygame_gui import UIManager

from src.constants import ROOT, WINDOW_HEIGHT, WINDOW_WIDTH

class Game:
    """A class that runs the game."""
    def __init__(self) -> None:
        init_pygame()
        self.screen: Surface = set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        set_caption('Exoplanetary Showdown: Invasion Evasion')
        # set_icon(load_image(ROOT + GAME_SETTINGS['window']['icon']).convert())
        self.aliens: Group = Group()
        self.turrets: Group = Group()
        self.all_sprites: Group = Group()
        self.ui_manager: UIManager = UIManager(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        self.clock: Clock = Clock()
        self.running: bool = True
    
    def _kill(self) -> None:
        self.running = False
    
    def _update(self) -> None:
        dt: int = self.clock.tick(60)
        for event in get():
            if event.type == QUIT:
                self._kill()
            self.ui_manager.process_events(event)
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        self.ui_manager.update(get_ticks())
        self.ui_manager.draw_ui(self.screen)
        flip_display()
    
    def play(self) -> None:
        while self.running:
            self._update()

