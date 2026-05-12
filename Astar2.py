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
         current_cost, current = heapq.heappop(open_list)

         if current == goal:

            path = []

            while current:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, cost[goal]

         for neighbour, weight in graph[current]:

             new_cost = cost[current] + weight
 
             if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                priority = new_cost + heuristic[neighbour]

                heapq.heappush(open_list, (priority, neighbour))

                parent[neighbour] = current


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

path, total_cost = astar(graph, heuristic, 'A', 'D')

# Run A*
path, total_cost = astar(graph, heuristic, 'A', 'D')

# Output
print("A* Path:", " -> ".join(path))
print("Total Cost:", total_cost)
