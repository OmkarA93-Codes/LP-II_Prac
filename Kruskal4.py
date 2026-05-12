# Simple Kruskal's Algorithm (Without Lambda)

def find(parent, node):

    # Find parent of node
    while parent[node] != node:
        node = parent[node]

    return node


def union(parent, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)

    # Connect sets
    parent[root_y] = root_x


def kruskal(vertices, edges):

    # Sort edges by weight manually
    edges.sort()

    parent = {}

    # Initially each node is its own parent
    for vertex in vertices:
        parent[vertex] = vertex

    mst = []
    total_cost = 0
    mst_path = []

    print("Edge \tWeight")

    for weight, u, v in edges:

        # Check cycle
        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            mst.append((u, v, weight))

            total_cost += weight

            mst_path.append(f"{u}-{v}")

            print(f"{u} - {v}\t{weight}")

    print("\nMST Path:")
    print(" -> ".join(mst_path))

    print("\nTotal Cost =", total_cost)


# Vertices
vertices = ['A', 'B', 'C', 'D', 'E']

# Edges (weight, u, v)
edges = [
    (2, 'A', 'B'),
    (6, 'A', 'D'),
    (3, 'B', 'C'),
    (8, 'B', 'D'),
    (5, 'B', 'E'),
    (7, 'C', 'E'),
    (9, 'D', 'E')
]

# Run Kruskal Algorithm
kruskal(vertices, edges)