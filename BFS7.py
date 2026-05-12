from collections import deque

def bfs_recursive(graph, queue, visited=None):
    # Initialize the visited set on the first call
    if visited is None:
        visited = set()
        print("BFS Traversal:", end=" ")

    # Base case: if the queue is empty, we are done searching
    if not queue:
        return

    # Dequeue the front node
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        # Enqueue all unvisited neighbours
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    # Recursive call to process the next node in the queue
    bfs_recursive(graph, queue, visited)

# Example undirected graph
graph = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'], 
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# For recursive BFS, we need to initialize the queue with the starting node
start_node = 'A'
initial_queue = deque([start_node])

bfs_recursive(graph, initial_queue)