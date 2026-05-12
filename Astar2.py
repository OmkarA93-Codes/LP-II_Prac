# A* Algorithm using Priority Queue (heapq)
# With Open List, Closed List, Path and Total Cost

import heapq

def astar(graph, heuristic, start, goal):

    # Open List (Priority Queue)
    open_list = []

    # Push start node
    heapq.heappush(open_list, (0, start))

    # Closed List
    closed_list = set()

    # Cost from start node
    cost = {start: 0}

    # Parent tracking
    parent = {start: None}

    while open_list:

        # Node with lowest priority
        current_priority, current = heapq.heappop(open_list)

        # Skip if already visited
        if current in closed_list:
            continue

        # Add node to closed list
        closed_list.add(current)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, cost[goal]

        # Explore neighbors
        for neighbour, weight in graph[current]:

            # Ignore visited nodes
            if neighbour in closed_list:
                continue

            # g(n)
            new_cost = cost[current] + weight

            # Better path found
            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                # f(n) = g(n) + h(n)
                priority = new_cost + heuristic[neighbour]

                # Add to open list
                heapq.heappush(open_list, (priority, neighbour))

                # Store parent
                parent[neighbour] = current

    return None, None


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

# Run A*
path, total_cost = astar(graph, heuristic, 'A', 'D')

# Output
print("A* Path:", " -> ".join(path))
print("Total Cost:", total_cost)
