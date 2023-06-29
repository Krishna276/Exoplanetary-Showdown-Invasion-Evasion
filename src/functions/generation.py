"""This file generates things like the map.
It uses probability distrubutions like the binomial distribution to generate the map.
The grometric distribution also appears in here too.
"""

from random import Random

from src.classes.grid import Grid
from src.classes.tile import Tile, TileType
from src.classes.vector import Vector, VECTOR_i, VECTOR_j, VectorOutOfBoundsError
from src.constants import GAME_SETTINGS, TILES

def _randBinomial(n: int, p: float, generator: Random) -> int:
    """Generates a random number following the distribution B(n, p)

    Args:
        n (int): The number of trials.
        p (float): The probability of a successful trial.

    Raises:
        ValueError: When n or p are invalid for a Binomial distribution.

    Returns:
        int: The number of successful trials.
    """
    if n < 0 or p < 0.0 or p > 1.0:
        raise ValueError('n must be a whole number, and p must be in the interval [0, 1]')
    return sum([generator.random() < p for _ in range(n)])

def _generateClusterShape(centre: Vector, generator: Random, distance: int = 1) -> set[Vector]:
    cluster: set[Vector] = {centre}
    for offset in VECTOR_i, VECTOR_j, -VECTOR_i, -VECTOR_j:
        try:
            if generator.random() < GAME_SETTINGS['battlefield']['cluster_expansion_probability'] / distance\
                and centre + offset not in cluster:
                cluster = cluster.union(_generateClusterShape(centre + offset, generator, distance + 1))
        except VectorOutOfBoundsError:
            pass
    return cluster

def generateMap(width: int, height: int, seed: int) -> Grid[Tile]:
    """Generates the map.

    Args:
        width (int): Width of the map to generate.
        height (int): Height of the map to generate.

    Returns:
        Grid[Tile]: A Grid object representing the generated map.
    """
    generator: Random = Random(seed)
    # Some things that can be pre-computed as they're same each time.
    cluster_probability: float = 1 / (width * height * GAME_SETTINGS['battlefield']['cluster_density'] + 1)
    possible_types: list[TileType] = [
        TileType.SLOWNESS,
        TileType.SPEED,
        TileType.IMMUNITY,
        TileType.DAMAGE,
        TileType.NO_TURRET,
        TileType.NO_ALIEN,
        TileType.BLOCK
    ]
    while True:
        map_: Grid[Tile] = Grid[Tile](Vector(width, height))
        # Fill everything with empty space or vacuum tiles.
        types: list[list[TileType]] = [[TileType.VACUUM for i in range(width)] for j in range(height)]
        # Add in clusters of all the types of tile
        # Calculate probability from geometric distribution 1/p = mu + 1.
        # We want mu to be one cluster every 20 squares (for cluster density 0.05).
        while generator.random() >= cluster_probability:
            # Spawn a cluster
            cluster_type: TileType = generator.choice(possible_types)
            cluster_centre = Vector(generator.randint(0, width - 1), generator.randint(0, height - 1), width, height)
            for coordinates in _generateClusterShape(cluster_centre, generator):
                types[coordinates.y][coordinates.x] = cluster_type
        # Place the earth tile, it should have an expected value of about 90% of the width of the screen.
        # It should generate near the middle of the column.
        row, col = _randBinomial(height - 1, 0.5, generator), _randBinomial(width - 1, 0.9, generator)
        types[row][col] = TileType.EARTH
        earth_row, earth_col = row, col
        # The mothership should follow a similar distribution, but be skewed to the left.
        while types[row][col] == TileType.EARTH:
            row, col = row, col = _randBinomial(height - 1, 0.5, generator), _randBinomial(width - 1, 0.1, generator)
        types[row][col] = TileType.PORTAL
        # Fill in a Grid[Tile] object
        for i in range(height):
            for j in range(width):
                map_[j, i] = Tile(types[i][j]), TILES[types[i][j].name]['cost']
        # If a valid path exists, then return the filled in Grid.
        if map_.pathfind(Vector(col, row), Vector(earth_col, earth_row)) is not None:
            return map_
