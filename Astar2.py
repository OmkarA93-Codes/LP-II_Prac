# A* Algorithm using Priority Queue (heapq)
# Prints path and total cost

import heapq

def astar(graph, heuristic, start, goal):

    # Priority Queue
    open_list = []

    # Push start node
    heapq.heappush(open_list, (0, start))

    # Cost from start node
    cost = {start: 0}

    # Parent tracking
    parent = {start: None}

    while open_list:

        # Node with lowest priority
        current_priority, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            # Return path and total cost
            return path, cost[goal]

        # Explore neighbors
        for neighbour, weight in graph[current]:

            # g(n)
            new_cost = cost[current] + weight

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                # f(n) = g(n) + h(n)
                priority = new_cost + heuristic[neighbour]

                heapq.heappush(open_list, (priority, neighbour))

                parent[neighbour] = current


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

print("A* Path:", path)
print("Total Cost:", total_cost)