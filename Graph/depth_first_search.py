"""
DFS is a graph traversal algorithm that visits all nodes in a graph depth by depth.
It starts at the root node and visits all nodes at the current depth before moving to the next depth.

Time complexity: O(V + E)
Space complexity: O(V)

Intuition: Start at a node → visit it → visit all its neighbors → repeat.
"""

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A')

# Output: A B D E C F

# Cleaner Version (Avoid duplicate visits)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Iterative DFS (Using Stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # push neighbors (reverse for same order as recursive)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])

    if (r < 0 or c < 0 or r >= rows or c >= cols or
        (r, c) in visited):
        return

    visited.add((r, c))
    print((r, c))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dr, dc in directions:
        dfs_grid(grid, r + dr, c + dc, visited)