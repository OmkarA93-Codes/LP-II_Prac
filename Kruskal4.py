# Simple Kruskal Algorithm

def kruskal(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {}

    # Initialize parent
    for vertex in vertices:
        parent[vertex] = vertex

    # Find function
    def find(node):

        while parent[node] != node:
            node = parent[node]

        return node

    total_cost = 0
    mst_path = []

    print("Edge \tWeight")

    # Process edges
    for u, v, w in edges:

        root_u = find(u)
        root_v = find(v)

        # Avoid cycle
        if root_u != root_v:

            print(f"{u} - {v}\t{w}")

            total_cost += w

            mst_path.append(f"{u}-{v}")

            # Union
            parent[root_v] = root_u

    print("\nMST Path:")
    print(" -> ".join(mst_path))

    print("\nTotal Cost =", total_cost)


# Vertices
vertices = ['A', 'B', 'C', 'D', 'E']

# Edges (u, v, weight)
edges = [
    ('A', 'B', 2),
    ('A', 'D', 6),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('B', 'E', 5),
    ('C', 'E', 7),
    ('D', 'E', 9)
]

# Run Kruskal Algorithm
kruskal(vertices, edges)