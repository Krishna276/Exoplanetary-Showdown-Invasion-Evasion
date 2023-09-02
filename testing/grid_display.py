from pygame import init, QUIT, quit
from pygame.display import set_caption, set_mode, update
from pygame.draw import line, rect
from pygame.event import get
from pygame.time import Clock
from pygame_gui import UIManager

init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1345, 760
GRID_SIZE = 50
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BORDER_PERCENTAGE = 0.08  # Smaller border percentage

# Calculate border size based on percentage
border_width = int(SCREEN_WIDTH * BORDER_PERCENTAGE)
border_height = int(SCREEN_HEIGHT * BORDER_PERCENTAGE)

# Pygame setup
screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
set_caption("Grid Window")
clock = Clock()

# Pygame GUI setup
manager = UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a grid with cells, excluding the border area
def draw_grid():
    for x in range(border_width, SCREEN_WIDTH - border_width + 1, GRID_SIZE):
        line(screen, WHITE, (x, border_height), (x, SCREEN_HEIGHT - border_height))
    for y in range(border_height, SCREEN_HEIGHT - border_height + 1, GRID_SIZE):
        line(screen, WHITE, (border_width, y), (SCREEN_WIDTH - border_width, y))

# Main loop
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in get():
        if event.type == QUIT:
            running = False
        manager.process_events(event)
    screen.fill((0, 0, 0))  # Clear the screen
    # Draw the border
    rect(screen, WHITE, (0, 0, border_width, SCREEN_HEIGHT))  # Left border
    rect(screen, WHITE, (0, 0, SCREEN_WIDTH, border_height))  # Top border
    rect(screen, WHITE, (SCREEN_WIDTH - border_width, 0, border_width, SCREEN_HEIGHT))  # Right border
    rect(screen, WHITE, (0, SCREEN_HEIGHT - border_height, SCREEN_WIDTH, border_height))  # Bottom border
    draw_grid()  # Draw the grid
    manager.update(time_delta)
    manager.draw_ui(screen)
    update()

quit()