import heapq

TupleCoords = tuple[int, int]
ArrayGrid = list[list[int | str]]

def astar(start: TupleCoords, goal: TupleCoords, grid: ArrayGrid):
    """
    A* algorithm to find the shortest path from start to goal.
    """
    # Define the heuristic function
    def heuristic(a: TupleCoords, b: TupleCoords):
        # Manhattan Distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Define the cost function
    def cost(next: TupleCoords):
        cost_: int | str = grid[next[0]][next[1]]
        if cost_ == 'N':
            return float('inf')
        return cost_ if isinstance(cost_, int) else 0

    # Initialize the open and closed sets
    open_set: list = []
    closed_set: set = set()

    # Add the start node to the open set
    heapq.heappush(open_set, (0, start))

    # Initialize the g and f scores
    g_score: dict[TupleCoords, int] = {start: 0}
    f_score: dict[TupleCoords, int] = {start: heuristic(start, goal)}
    previous_nodes: dict[TupleCoords, TupleCoords | None] = {start: None}

    # Loop until the open set is empty
    while open_set:
        # Get the node with the lowest f score
        current = heapq.heappop(open_set)[1]

        # Check if we have reached the goal
        if current == goal:
            # Reconstruct the path
            path = []
            while current in previous_nodes:
                path.append(current)
                current = previous_nodes[current]
            path.reverse()
            return path

        # Add the current node to the closed set
        closed_set.add(current)

        # Loop through the neighbors of the current node
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Calculate the next node
            _next = (current[0] + neighbor[0], current[1] + neighbor[1])

            # Check if the next node is valid
            if (
                _next in closed_set
                or _next[0] < 0 or _next[0] >= len(grid) or _next[1] < 0 or _next[1] >= len(grid[0])
                or grid[_next[0]][_next[1]] == 'N'
            ):
                continue

            # Calculate the tentative g score
            tentative_g_score = g_score[current] + cost(_next)

            # Check if the next node is already in the open set
            if _next in g_score and tentative_g_score >= g_score[_next]:
                continue

            # Add the next node to the open set
            g_score[_next] = tentative_g_score
            f_score[_next] = tentative_g_score + heuristic(_next, goal)
            previous_nodes[_next] = current
            heapq.heappush(open_set, (f_score[_next], _next))

    # If we get here, there is no path
    return None

if __name__ == '__main__':
    # Example usage
    grid: ArrayGrid = [
        [1, 1, 1, 1, 1, 'N', 1, 1, 1, 1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1],  # 0
        [1, 1, 1, 'N', 3, 1, 1, 1, 1, 1, 'N', 2, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
        [1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 2, 'N', 1, 1, 1, 1, 1, 1, 1],  # 2
        [1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1],  # 3
        [1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1],  # 4
        [1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 1, 'N', 2, 2, 2, 2, 2, 2, 1, 1],  # 5
        [1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 'N', 1, 2, 1, 1, 1, 1, 2, 1, 1],  # 6
        [1, 1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 'N', 1, 2, 1, 1],  # 7
        [1, 1, 'N', 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 'N', 2, 2, 1, 1],  # 8
        ['N', 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'N', 1, 1, 1, 1, 1, 1, 1]  # 9
    ]
    start: TupleCoords = (4, 0)
    goal: TupleCoords = (5, 19)
    path: list[TupleCoords] = astar(start, goal, grid)
    print(path)

'''
Structured english:
01. Initialize the open list with the start node.
02. Initialize the closed list as empty.
03. For the current node, calculate the cost of the path from the start node to the current node, and the estimated cost of the cheapest path from the current node to the goal node using the heuristic function.
04. If the current node is the goal node, return the path.
05. Otherwise, for each successor node of the current node: a. If the successor node is in the closed list, ignore it. b. If the successor node is not in the open list, add it to the open list and calculate its cost and estimated cost using the heuristic function. c. If the successor node is already in the open list, update its cost and estimated cost if the new values are better.
06. Move the current node to the closed list.
07. If the open list is empty, return failure.
08. Otherwise, sort the open list by the estimated cost of the cheapest path from the start node to the goal node.
09. Set the current node to the node with the lowest estimated cost.
10. Go to step 3.
'''
