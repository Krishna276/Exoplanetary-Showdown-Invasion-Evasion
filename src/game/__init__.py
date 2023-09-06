"""Module that provides the class that runs the game."""

from enum import Enum
from typing import Self

from pygame import init as init_pygame, KEYUP, Surface, QUIT
from pygame.display import flip as flip_display, set_caption, set_icon, set_mode
from pygame.draw import line as draw_line
from pygame.event import get as get_events
from pygame.locals import K_1, K_2, K_3, K_4
from pygame.sprite import Group
from pygame.time import Clock, get_ticks
from pygame_gui import UIManager

from src.classes.alien import Alien, AlienType
from src.classes.grid import Grid
from src.classes.tile import Tile
from src.classes.vector import FloatVector, Vector
from src.constants import (
    BF_GRID_HEIGHT, BF_GRID_WIDTH, BF_TILE_LENGTH, BORDER_HEIGHT, BORDER_WIDTH, GAME_SETTINGS, ROOT, WINDOW_HEIGHT,
    WINDOW_WIDTH
)
from src.functions.generation import generateMap
from src.functions.load_asset import load_image

class Phase(Enum):
    """The game phases."""
    INIT = 0
    DEF = 1
    ATK = 2
    ELIMINATION = 3

class Game:
    """A class that runs the game."""
    def __init__(self: Self) -> None:
        init_pygame()
        self.screen: Surface = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        set_caption('Exoplanetary Showdown: Invasion Evasion')
        set_icon(load_image(ROOT + GAME_SETTINGS['window']['icon']).convert())
        self.aliens: Group = Group()
        self.turrets: Group = Group()
        self.all_sprites: Group = Group()
        self.tile_sprites: Group = Group()
        self.ui_manager: UIManager = UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock: Clock = Clock()
        self.running: bool = True
        self.phase: Phase = Phase.INIT
        self.map: Grid[Tile]
        self.mothership: Vector
        self.earth: Vector
        self.map, self.earth, self.mothership = generateMap(BF_GRID_WIDTH, BF_GRID_HEIGHT, '')
        self.alien_path: list[Vector] = self.map.pathfind(self.mothership, self.earth)
    
    def _kill(self: Self) -> None:
        self.running = False
    
    def _draw_grid(self: Self) -> None:
        x = BORDER_WIDTH
        for _ in range(BF_GRID_WIDTH + 1):
            draw_line(self.screen, '#FFFFFF', (x, BORDER_HEIGHT), (x, WINDOW_HEIGHT - BORDER_HEIGHT))
            x += BF_TILE_LENGTH
        y = BORDER_HEIGHT
        for _ in range(BF_GRID_HEIGHT + 1):
            draw_line(self.screen, '#FFFFFF', (BORDER_WIDTH, y), (WINDOW_WIDTH - BORDER_WIDTH, y))
            y += BF_TILE_LENGTH
    
    def _update(self: Self) -> None:
        dt: int = self.clock.tick(60)
        for event in get_events():
            if event.type == QUIT:
                self._kill()
            elif event.type == KEYUP:
                if event.key == K_1:
                    self.aliens.add(Alien(AlienType.DAMAGE, FloatVector.fromVector(self.mothership)))
                elif event.key == K_2:
                    self.aliens.add(Alien(AlienType.TANK, FloatVector.fromVector(self.mothership)))
                elif event.key == K_3:
                    self.aliens.add(Alien(AlienType.HEALER, FloatVector.fromVector(self.mothership)))
                elif event.key == K_4:
                    self.aliens.add(Alien(AlienType.ECON, FloatVector.fromVector(self.mothership)))
            self.ui_manager.process_events(event)
        self.aliens.update(dt, self.alien_path, self.map)
        self._draw_grid()
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        self.ui_manager.update(get_ticks())
        self.ui_manager.draw_ui(self.screen)
        flip_display()
    
    def play(self: Self) -> None:
        while self.running:
            self._update()

