# Kruskal's Algorithm with Path Output

def find(parent, node):

    if parent[node] != node:
        parent[node] = find(parent, parent[node])

    return parent[node]


def union(parent, rank, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)

    # Cycle detected
    if root_x == root_y:
        return False

    # Union by rank
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x] += 1

    return True


def kruskal(edges, vertices):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    # Initialize sets
    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_cost = 0
    mst_path = []

    print("Edge \tWeight")

    for u, v, w in edges:

        # Add edge if no cycle
        if union(parent, rank, u, v):

            mst.append((u, v, w))
            total_cost += w

            mst_path.append(f"{u}-{v}")

            print(f"{u} - {v}\t{w}")

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

# Run Kruskal's Algorithm
kruskal(edges, vertices)