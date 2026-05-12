def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A' ,'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("DFS Traversal:", end=" ")
dfs(graph, 'A')
