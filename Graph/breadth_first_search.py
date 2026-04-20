# BFS implementation
"""
BFS is a graph traversal algorithm that visits all nodes in a graph level by level.
It starts at the root node and visits all nodes at the current level before moving to the next level.

Time complexity: O(V + E)
Space complexity: O(V)

Intuition: Start at a node → visit it → push its neighbors → repeat.
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # add neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

# Output: A B C D E F

# Cleaner Version (Avoid duplicate pushes)
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# BFS on Grid
def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set([start])
    queue = deque([start])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()
        print((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))