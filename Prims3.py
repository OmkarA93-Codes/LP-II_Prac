import sys

# Prim's Algorithm with Path Output

def prims(graph, vertices):

    V = len(vertices)

    selected = [False] * V
    selected[0] = True

    total_cost = 0
    mst_path = []

    print("Edge \tWeight")

    for _ in range(V - 1):

        minimum = sys.maxsize
        x = y = 0

        for i in range(V):

            if selected[i]:

                for j in range(V):

                    # Find minimum edge
                    if not selected[j] and graph[i][j]:

                        if minimum > graph[i][j]:

                            minimum = graph[i][j]
                            x, y = i, j

        print(f"{vertices[x]} - {vertices[y]}\t{graph[x][y]}")

        # Store path
        mst_path.append(f"{vertices[x]}-{vertices[y]}")

        total_cost += graph[x][y]

        selected[y] = True

    print("\nMST Path:")
    print(" -> ".join(mst_path))

    print("\nTotal Cost =", total_cost)


# Vertex Labels
vertices = ['A', 'B', 'C', 'D', 'E']

# Adjacency Matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Run Prim's Algorithm
prims(graph, vertices)