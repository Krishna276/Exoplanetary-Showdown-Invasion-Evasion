"""Module that provides the class that runs the game."""

from datetime import datetime
from enum import Enum
from typing import Self

from pygame import init as init_pygame, KEYDOWN, KEYUP, Rect, Surface, QUIT
from pygame.display import flip as flip_display, set_caption, set_icon, set_mode
from pygame.draw import line as draw_line
from pygame.event import get as get_events
from pygame.key import get_pressed as get_pressed_keys, ScancodeWrapper
from pygame.locals import K_1, K_2, K_3, K_4, K_ESCAPE, K_LALT, K_RALT
from pygame.sprite import Group
from pygame.time import Clock, get_ticks
from pygame.transform import scale
from pygame_gui import UIManager
from pygame_gui.elements import UIImage, UITextBox

from src.classes.alien import Alien, AlienType
from src.classes.grid import Grid
from src.classes.highlight_tile import Highlight
from src.classes.tile import Tile, TileType
from src.classes.tile_sprite import TileSprite
from src.classes.vector import FloatVector, Vector
from src.constants import *
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
    def __init__(self: Self, seed: str | None = None) -> None:
        init_pygame()
        self.screen: Surface = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        set_caption('Exoplanetary Showdown: Invasion Evasion')
        set_icon(load_image(GAME_SETTINGS['window']['icon']).convert())
        self.aliens: Group = Group()
        self.turrets: Group = Group()
        self.all_sprites: Group = Group()
        self.tile_sprites: Group = Group()
        self.path_highlight: Group = Group()
        self.ui_manager: UIManager = UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock: Clock = Clock()
        self.running: bool = True
        self.phase: Phase = Phase.INIT
        self.map: Grid[Tile]
        self.mothership: Vector
        self.earth: Vector
        if seed is None:
            seed = datetime.now().strftime("%Y%m%d%H%M%S")
            print(f'Using seed {seed}')
        self.map, self.earth, self.mothership = generateMap(BF_GRID_WIDTH, BF_GRID_HEIGHT, seed)
        self.alien_path: list[Vector] = self.map.pathfind(self.mothership, self.earth)
        for x in range(BF_GRID_WIDTH):
            for y in range(BF_GRID_HEIGHT):
                if self.map[x, y].tileType not in {TileType.EARTH, TileType.PORTAL}:
                    sprite: TileSprite = TileSprite(self.map[x, y], Vector(x, y))
                    self.tile_sprites.add(sprite)
                    self.all_sprites.add(sprite)
        for tile in self.mothership, self.earth:
            sprite: TileSprite = TileSprite(self.map[tile], tile)
            self.tile_sprites.add(sprite)
            self.all_sprites.add(sprite)
        for tile in self.alien_path:
            self.path_highlight.add(Highlight(tile))
        UITextBox(
            html_text='1, 2, 3 and 4 summon aliens. Alt shows the grid. Esc kills the game.',
            relative_rect=Rect(0, 0, -1, 50),
            manager=self.ui_manager,
            anchors={
                'left': 'left',
                'top': 'top'
            }
        )
        for index, alienType in enumerate([AlienType.ECON, AlienType.HEALER, AlienType.TANK, AlienType.DAMAGE]):
            UIImage(
                relative_rect=Rect(WINDOW_WIDTH - 50 * (index+ 1), 0, 50, 50),
                image_surface=scale(load_image(ALIENS[alienType.name]['sprite_path']), (50, 50))
            )
    
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
        if self.phase == Phase.INIT:
            self.phase = Phase.ATK
        for event in get_events():
            if event.type == QUIT:
                self._kill()
            elif event.type == KEYDOWN:
                if event.key in {K_LALT, K_RALT}:
                    self.all_sprites.add(self.path_highlight)
            elif event.type == KEYUP:
                if self.phase == Phase.ATK:
                    alienType: AlienType | None = None
                    if event.key == K_1:
                        alienType = AlienType.DAMAGE
                    elif event.key == K_2:
                        alienType = AlienType.TANK
                    elif event.key == K_3:
                        alienType = AlienType.HEALER
                    elif event.key == K_4:
                        alienType = AlienType.ECON
                    if alienType is not None:
                        alien = Alien(alienType, FloatVector.fromVector(self.mothership), self.alien_path)
                        self.aliens.add(alien)
                        self.all_sprites.add(alien)
                if event.key in {K_LALT, K_RALT}:
                    self.all_sprites.remove(self.path_highlight)
                elif event.key == K_ESCAPE:
                    self._kill()
            self.ui_manager.process_events(event)
        pressed_keys: ScancodeWrapper = get_pressed_keys()
        self.aliens.update(dt, self.map)
        self.screen.fill('#000000')
        if pressed_keys[K_LALT] or pressed_keys[K_RALT]:
            self._draw_grid()
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
        self.ui_manager.update(get_ticks())
        self.ui_manager.draw_ui(self.screen)
        flip_display()
    
    def play(self: Self) -> None:
        while self.running:
            self._update()

